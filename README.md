# WhatsApp Packet Capture Analyzer

![WhatsApp Logo](https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg)

**WhatsApp Packet Capture Analyzer** is a Python-based tool designed to monitor and analyze network traffic associated with WhatsApp communications. By capturing and logging WhatsApp-related packets, this analyzer provides valuable insights into the patterns of WhatsApp conversations without accessing the actual message content. This data can be leveraged for applying machine learning algorithms to identify usage patterns, detect anomalies, or perform other analytical tasks.

---

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Output](#output)
- [Importing Data into Excel](#importing-data-into-excel)
- [Applying Machine Learning](#applying-machine-learning)
- [Improving the Analyzer](#improving-the-analyzer)
- [Ethical and Legal Considerations](#ethical-and-legal-considerations)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Disclaimer](#disclaimer)

---

## Features

- **Dynamic IP Resolution:** Automatically resolves and updates WhatsApp server IP addresses to ensure accurate packet filtering.
- **IPv4 and IPv6 Support:** Captures both IPv4 and IPv6 packets related to WhatsApp traffic.
- **Packet Direction Determination:** Identifies whether packets are sent or received relative to the local device.
- **Event Classification:** Categorizes events based on packet counts (e.g., SENT, RCVD, OTHER).
- **Clean Output Formatting:** Displays real-time packet information in a neatly formatted console output with right-aligned integer columns for readability.
- **CSV Logging:** Logs captured data into a CSV file, facilitating easy import into Excel or other data analysis tools.
- **Optional Real-Time Plotting:** Visualizes packet traffic over time using `matplotlib` (can be enabled or disabled).
- **Class-Based Structure:** Organized using Python classes for better maintainability and scalability.

---

## Prerequisites

Before using the WhatsApp Packet Capture Analyzer, ensure that your system meets the following requirements:

### Hardware

- **Network Interface Card (NIC):** A compatible NIC that supports packet capturing (promiscuous mode).
- **Permissions:** Administrative (root) privileges are required to capture network packets.

### Software

- **Operating System:** Unix-based systems (e.g., Linux, macOS) are recommended. Packet capturing on Windows may require additional configurations.
- **Python Version:** Python 3.11 is used, with executables located in `/usr/local/bin/` (e.g., `python3.11`, `pip3.11`).

---

## Installation

### 1. Clone the Repository


git clone https://github.com/yourusername/whatsapp-packet-capture-analyzer.git
cd whatsapp-packet-capture-analyzer


## Configuration
The analyzer is highly configurable through a dictionary within the script. Below are the key configuration parameters and how to set them:

1. Configuration Parameters
Located within the main() function of ws_traffic.py:

python
Copiar código
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
    'IP_UPDATE_INTERVAL': 3600,  # in seconds (1 hour)
    'TIME_WINDOW_SECONDS': 1,
    'UPDATE_INTERVAL': 1,  # in seconds
    'PACKET_HISTORY_LENGTH': 60,  # Last 60 seconds
    'EVENT_THRESHOLD': 3,
    'DEFAULT_INTERFACE': "en2",
    'LOG_FILE': "whatsapp_packet_log.csv",
    'ENABLE_PLOTTING': False  # Set to True to enable plotting
}
2. Key Configuration Options
WHATSAPP_DOMAINS: List of WhatsApp-related domains to resolve and monitor.
IP_UPDATE_INTERVAL: Time interval (in seconds) to re-resolve WhatsApp IP addresses. Defaults to 1 hour.
TIME_WINDOW_SECONDS: Duration (in seconds) for each packet capture window.
UPDATE_INTERVAL: Frequency (in seconds) at which packet capturing occurs.
PACKET_HISTORY_LENGTH: Number of recent packet counts to store for plotting purposes.
EVENT_THRESHOLD: Minimum number of packets to classify an event as SENT or RCVD.
DEFAULT_INTERFACE: Network interface to monitor (e.g., en2, eth0). Change this based on your system.
LOG_FILE: Name of the CSV log file where data will be stored.
ENABLE_PLOTTING: Boolean flag to enable (True) or disable (False) real-time plotting.
