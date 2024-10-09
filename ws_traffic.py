#!/usr/bin/env python3
"""
ws_traffic.py

A Python script to capture and display detailed WhatsApp packet information every second.
Includes features such as dynamic IP resolution, IPv4 and IPv6 support, packet direction
determination, event classification, clean output formatting, and logging for offline analysis.

Author: [Your Name]
Date: 2024-10-08
"""

import datetime
from scapy.all import sniff, IP
from scapy.layers.inet6 import IPv6
from collections import deque
import threading
import socket
import sys
import time
import csv
from tabulate import tabulate

class CSVLogger:
    """
    A class to handle logging packet data into a CSV file.
    """

    def __init__(self, log_file):
        """
        Initialize the CSVLogger with the specified log file.

        Parameters:
            log_file (str): The path to the CSV log file.
        """
        self.log_file = log_file
        try:
            # Open the CSV file in write mode and initialize the CSV writer
            self.file = open(self.log_file, 'w', newline='')
            self.writer = csv.writer(self.file)
            # Write the header row
            self.writer.writerow(["Time", "SRC IP(s)", "DST IP(s)", "S", "R", "Event"])
        except IOError as e:
            print(f"Failed to open log file {self.log_file}: {e}")
            sys.exit(1)

    def log(self, row):
        """
        Log a row of data to the CSV file.

        Parameters:
            row (list): A list containing the row data.
        """
        try:
            self.writer.writerow(row)
        except Exception as e:
            print(f"Failed to write to log file: {e}")

    def close(self):
        """
        Close the CSV file.
        """
        try:
            self.file.close()
        except Exception as e:
            print(f"Failed to close log file: {e}")

class WhatsAppPacketCapture:
    """
    A class to capture WhatsApp network packets and log relevant information.
    """

    def __init__(self, config):
        """
        Initialize the WhatsAppPacketCapture with configuration parameters.

        Parameters:
            config (dict): A dictionary containing configuration parameters.
        """
        self.whatsapp_domains = config.get('WHATSAPP_DOMAINS', [])
        self.ip_update_interval = config.get('IP_UPDATE_INTERVAL', 3600)  # in seconds
        self.time_window_seconds = config.get('TIME_WINDOW_SECONDS', 1)
        self.update_interval = config.get('UPDATE_INTERVAL', 1)  # in seconds
        self.packet_history_length = config.get('PACKET_HISTORY_LENGTH', 60)  # last 60 seconds
        self.event_threshold = config.get('EVENT_THRESHOLD', 3)
        self.interface = config.get('DEFAULT_INTERFACE', 'en2')
        self.log_file = config.get('LOG_FILE', 'whatsapp_packet_log.csv')
        self.enable_plotting = config.get('ENABLE_PLOTTING', False)

        # Initialize global variables
        self.packet_counts = deque([0] * self.packet_history_length, maxlen=self.packet_history_length)
        self.timestamps = deque([datetime.datetime.now().strftime("%H:%M:%S")] * self.packet_history_length, maxlen=self.packet_history_length)

        # Resolve WhatsApp IPs at startup
        self.whatsapp_ips = self.get_whatsapp_ips(self.whatsapp_domains)

        # Get local IP addresses
        self.local_ips = self.get_local_ips()

        # Initialize the CSV Logger
        self.logger = CSVLogger(self.log_file)

    def get_whatsapp_ips(self, domains):
        """
        Resolve WhatsApp domains to their current IP addresses.

        Parameters:
            domains (list): List of WhatsApp-related domain names.

        Returns:
            list: List of resolved IP addresses.
        """
        ip_set = set()
        for domain in domains:
            try:
                resolved_ips = socket.gethostbyname_ex(domain)[2]
                ip_set.update(resolved_ips)
                print(f"Resolved {domain}: {', '.join(resolved_ips)}")
            except socket.gaierror:
                print(f"Failed to resolve domain: {domain}")
        return list(ip_set)

    def get_local_ips(self):
        """
        Retrieve all local IP addresses assigned to the device.

        Returns:
            list: List of local IP addresses.
        """
        local_ips = set()
        hostname = socket.gethostname()
        try:
            local_ip = socket.gethostbyname(hostname)
            local_ips.add(local_ip)
        except socket.gaierror:
            pass

        # Retrieve all IP addresses associated with the device
        for info in socket.getaddrinfo(hostname, None):
            ip = info[4][0]
            local_ips.add(ip)
        return list(local_ips)

    def format_ips(self, ip_set, max_ips=2, max_length=25):
        """
        Format IP addresses by limiting the number of IPs displayed and truncating if necessary.

        Parameters:
            ip_set (set): Set of IP addresses.
            max_ips (int): Maximum number of IPs to display.
            max_length (int): Maximum length of the formatted IP string.

        Returns:
            str: Formatted IP addresses string.
        """
        ips = list(ip_set)
        if len(ips) > max_ips:
            formatted = ", ".join(ips[:max_ips]) + ",..."
        else:
            formatted = ", ".join(ips)
        if len(formatted) > max_length:
            return formatted[:max_length-3] + "..."
        return formatted

    def get_packet_direction(self, packet):
        """
        Determine the direction of the packet relative to the local device.

        Parameters:
            packet (scapy.packet.Packet): The captured network packet.

        Returns:
            str: "Sent", "Received", or "Unknown"
        """
        if IP in packet:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            if src_ip in self.local_ips:
                return "Sent"
            elif dst_ip in self.local_ips:
                return "Received"
        if IPv6 in packet:
            src_ip = packet[IPv6].src
            dst_ip = packet[IPv6].dst
            if src_ip in self.local_ips:
                return "Sent"
            elif dst_ip in self.local_ips:
                return "Received"
        return "Unknown"

    def detect_message_event(self, sent_count, received_count):
        """
        Detect send or receive events based on packet counts.

        Parameters:
            sent_count (int): Number of sent packets.
            received_count (int): Number of received packets.

        Returns:
            str: "SENT", "RCVD", or "OTHER"
        """
        if sent_count >= self.event_threshold and sent_count > received_count:
            return "SENT"
        elif received_count >= self.event_threshold and received_count > sent_count:
            return "RCVD"
        else:
            return "OTHER"

    def is_whatsapp_packet(self, packet):
        """
        Check if a packet is from or to a WhatsApp IP address.

        Parameters:
            packet (scapy.packet.Packet): The captured network packet.

        Returns:
            bool: True if packet is WhatsApp-related, False otherwise.
        """
        if IP in packet:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            if src_ip in self.whatsapp_ips or dst_ip in self.whatsapp_ips:
                return True
        if IPv6 in packet:
            src_ip = packet[IPv6].src
            dst_ip = packet[IPv6].dst
            if src_ip in self.whatsapp_ips or dst_ip in self.whatsapp_ips:
                return True
        return False

    def capture_packets(self):
        """
        Capture WhatsApp packets, determine direction, and update counts.
        """
        print(f"Starting packet capture on interface: {self.interface}")
        while True:
            try:
                # Capture packets for the defined update interval
                packets = sniff(
                    iface=self.interface,
                    timeout=self.update_interval,
                    filter="ip or ip6",
                    prn=lambda pkt: pkt if self.is_whatsapp_packet(pkt) else None
                )
                # Filter out None packets
                whatsapp_packets = [pkt for pkt in packets if pkt]
                whatsapp_packet_count = len(whatsapp_packets)
                
                # Initialize counters and IP sets
                sent_count = 0
                received_count = 0
                sent_bytes = 0
                received_bytes = 0
                source_ips = set()
                destination_ips = set()
                
                for pkt in whatsapp_packets:
                    direction = self.get_packet_direction(pkt)
                    pkt_size = len(pkt)
                    if direction == "Sent":
                        sent_count += 1
                        sent_bytes += pkt_size
                        if IP in pkt:
                            source_ips.add(pkt[IP].src)
                            destination_ips.add(pkt[IP].dst)
                        elif IPv6 in pkt:
                            source_ips.add(pkt[IPv6].src)
                            destination_ips.add(pkt[IPv6].dst)
                    elif direction == "Received":
                        received_count += 1
                        received_bytes += pkt_size
                        if IP in pkt:
                            source_ips.add(pkt[IP].src)
                            destination_ips.add(pkt[IP].dst)
                        elif IPv6 in pkt:
                            source_ips.add(pkt[IPv6].src)
                            destination_ips.add(pkt[IPv6].dst)
                
                # Calculate Total Bytes
                total_bytes = sent_bytes + received_bytes
                
                # Detect event classification
                event = self.detect_message_event(sent_count, received_count)
                
                # Get current time
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Prepare source and destination IP strings
                source_ips_str = self.format_ips(source_ips)
                destination_ips_str = self.format_ips(destination_ips)
                
                # Prepare row data
                row = [
                    current_time,
                    source_ips_str,
                    destination_ips_str,
                    sent_count,
                    received_count,
                    event
                ]
                
                # Print the row with padded integers
                # Align 'S' and 'R' to the right for padding
                print(tabulate([row], tablefmt="plain", colalign=("left", "left", "left", "right", "right", "left")))
                
                # Log the data to CSV
                self.logger.log(row)
                
                # Update deques (optional, retained for future plotting)
                self.packet_counts.append(whatsapp_packet_count)
                self.timestamps.append(current_time)
            except Exception as e:
                print(f"Error capturing packets: {e}")

    def update_whatsapp_ips_thread(self):
        """
        Thread function to periodically update WhatsApp IPs by resolving domains.
        """
        while True:
            time.sleep(self.ip_update_interval)
            self.whatsapp_ips = self.get_whatsapp_ips(self.whatsapp_domains)
            print(f"\n[INFO] Updated WhatsApp IPs at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {self.whatsapp_ips}\n")

    def start(self):
        """
        Start the packet capturing and IP updating threads.
        """
        # Start the IP updating thread
        ip_thread = threading.Thread(target=self.update_whatsapp_ips_thread, daemon=True)
        ip_thread.start()

        # Print table headers
        headers = ["Time", "SRC IP(s)", "DST IP(s)", "S", "R", "Event"]
        print(tabulate([headers], headers="firstrow", tablefmt="plain", colalign=("left", "left", "left", "right", "right", "left")))
        
        # Start capturing packets
        self.capture_packets()

class Plotter:
    """
    A class to handle real-time plotting of WhatsApp packet traffic.
    """

    def __init__(self, timestamps, packet_counts, packet_history_length=60, update_interval=1):
        """
        Initialize the Plotter with data queues and plotting parameters.

        Parameters:
            timestamps (deque): Deque containing timestamps.
            packet_counts (deque): Deque containing packet counts.
            packet_history_length (int): Number of data points to display.
            update_interval (int): Interval between plot updates in seconds.
        """
        self.timestamps = timestamps
        self.packet_counts = packet_counts
        self.packet_history_length = packet_history_length
        self.update_interval = update_interval

    def start(self):
        """
        Start the real-time plot.
        """
        import matplotlib.pyplot as plt
        from matplotlib.animation import FuncAnimation

        plt.figure(figsize=(10, 6))

        def update_graph(frame):
            """
            Update the plot with the latest data.
            """
            plt.cla()  # Clear the current axes
            plt.plot(list(self.timestamps), list(self.packet_counts), marker='o', linestyle='-', color='blue')
            plt.title(f"WhatsApp Traffic Over Time (Last {self.packet_history_length} Seconds)")
            plt.xlabel("Time")
            plt.ylabel("Packet Count")
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.grid(True)

        ani = FuncAnimation(plt.gcf(), update_graph, interval=self.update_interval * 1000)
        plt.show()

def main():
    """
    The main entry point of the script.
    """
    # Configuration parameters
    config = {
        'WHATSAPP_DOMAINS': [
            "whatsapp.com",
            "api.whatsapp.com",
            "web.whatsapp.com",
            "wa.me",
            "whatsapp.net",
            "chat.whatsapp.com",
            # Add more domains if necessary
        ],
        'IP_UPDATE_INTERVAL': 3600,  # in seconds
        'TIME_WINDOW_SECONDS': 1,
        'UPDATE_INTERVAL': 1,  # in seconds
        'PACKET_HISTORY_LENGTH': 60,  # Last 60 seconds
        'EVENT_THRESHOLD': 3,
        'DEFAULT_INTERFACE': "en2",
        'LOG_FILE': "whatsapp_packet_log.csv",
        'ENABLE_PLOTTING': False  # Set to True to enable plotting
    }

    # Initialize the packet capture object
    capture = WhatsAppPacketCapture(config)

    # If plotting is enabled, initialize the Plotter
    if config['ENABLE_PLOTTING']:
        plotter = Plotter(capture.timestamps, capture.packet_counts, config['PACKET_HISTORY_LENGTH'], config['UPDATE_INTERVAL'])
        plot_thread = threading.Thread(target=plotter.start, daemon=True)
        plot_thread.start()

    # Start capturing packets
    capture.start()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPacket capturing stopped by user.")
        sys.exit(0)
