WhatsApp Packet Capture Analyzer
--------------------------------

WhatsApp Logo**WhatsApp Packet Capture Analyzer** is a Python-based tool designed to monitor and analyze network traffic associated with WhatsApp communications. By capturing and logging WhatsApp-related packets, this analyzer provides valuable insights into the patterns of WhatsApp conversations without accessing the actual message content. This data can be leveraged for applying machine learning algorithms to identify usage patterns, detect anomalies, or perform other analytical tasks.**Author:**Omar AriasEmail: [oariasz72@gmail.com](mailto:oariasz72@gmail.com)

Table of Contents
-----------------

*   [Features](https://www.perplexity.ai/search/can-you-put-all-of-this-into-a-dZbl2om8Sby8ilYGO4fkYw#features)
    
*   [Prerequisites](https://www.perplexity.ai/search/can-you-put-all-of-this-into-a-dZbl2om8Sby8ilYGO4fkYw#prerequisites)
    
*   [Installation](https://www.perplexity.ai/search/can-you-put-all-of-this-into-a-dZbl2om8Sby8ilYGO4fkYw#installation)
    
*   [Configuration](https://www.perplexity.ai/search/can-you-put-all-of-this-into-a-dZbl2om8Sby8ilYGO4fkYw#configuration)
    
*   [Usage](https://www.perplexity.ai/search/can-you-put-all-of-this-into-a-dZbl2om8Sby8ilYGO4fkYw#usage)
    
*   [Output](https://www.perplexity.ai/search/can-you-put-all-of-this-into-a-dZbl2om8Sby8ilYGO4fkYw#output)
    
*   [Importing Data into Excel](https://www.perplexity.ai/search/can-you-put-all-of-this-into-a-dZbl2om8Sby8ilYGO4fkYw#importing-data-into-excel)
    
*   [Applying Machine Learning](https://www.perplexity.ai/search/can-you-put-all-of-this-into-a-dZbl2om8Sby8ilYGO4fkYw#applying-machine-learning)
    
*   [Improving the Analyzer](https://www.perplexity.ai/search/can-you-put-all-of-this-into-a-dZbl2om8Sby8ilYGO4fkYw#improving-the-analyzer)
    
*   [Ethical and Legal Considerations](https://www.perplexity.ai/search/can-you-put-all-of-this-into-a-dZbl2om8Sby8ilYGO4fkYw#ethical-and-legal-considerations)
    
*   [Troubleshooting](https://www.perplexity.ai/search/can-you-put-all-of-this-into-a-dZbl2om8Sby8ilYGO4fkYw#troubleshooting)
    
*   [Contributing](https://www.perplexity.ai/search/can-you-put-all-of-this-into-a-dZbl2om8Sby8ilYGO4fkYw#contributing)
    
*   [License](https://www.perplexity.ai/search/can-you-put-all-of-this-into-a-dZbl2om8Sby8ilYGO4fkYw#license)
    
*   [Acknowledgements](https://www.perplexity.ai/search/can-you-put-all-of-this-into-a-dZbl2om8Sby8ilYGO4fkYw#acknowledgements)
    
*   [Disclaimer](https://www.perplexity.ai/search/can-you-put-all-of-this-into-a-dZbl2om8Sby8ilYGO4fkYw#disclaimer)
    

Features
--------

*   **Dynamic IP Resolution:** Automatically resolves and updates WhatsApp server IP addresses to ensure accurate packet filtering.
    
*   **IPv4 and IPv6 Support:** Captures both IPv4 and IPv6 packets related to WhatsApp traffic.
    
*   **Packet Direction Determination:** Identifies whether packets are sent or received relative to the local device.
    
*   **Event Classification:** Categorizes events based on packet counts (e.g., SENT, RCVD, OTHER).
    
*   **Clean Output Formatting:** Displays real-time packet information in a neatly formatted console output with right-aligned integer columns for readability.
    
*   **CSV Logging:** Logs captured data into a CSV file, facilitating easy import into Excel or other data analysis tools.
    
*   **Optional Real-Time Plotting:** Visualizes packet traffic over time using matplotlib (can be enabled or disabled).
    
*   **Class-Based Structure:** Organized using Python classes for better maintainability and scalability.
    

Prerequisites
-------------

Before using the WhatsApp Packet Capture Analyzer, ensure that your system meets the following requirements:

Hardware
--------

*   **Network Interface Card (NIC):** A compatible NIC that supports packet capturing (promiscuous mode).
    
*   **Permissions:** Administrative (root) privileges are required to capture network packets.
    

Software
--------

*   **Operating System:** Unix-based systems (e.g., Linux, macOS) are recommended. Packet capturing on Windows may require additional configurations.
    
*   **Python Version:** Python 3.11 is used, with executables located in /usr/local/bin/ (e.g., python3.11, pip3.11).
    

Installation
------------

1\. Clone the Repository
------------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashgit clone https://github.com/oariasz/ws_traffic.git  cd ws_traffic   `

2\. Create a Virtual Environment (Optional but Recommended)
-----------------------------------------------------------

Creating a virtual environment helps manage dependencies and avoid conflicts.

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bash/usr/local/bin/python3.11 -m venv venv  source venv/bin/activate   `

3\. Install Required Python Packages
------------------------------------

Ensure that you have pip3.11 installed. Then, install the necessary packages:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bash/usr/local/bin/pip3.11 install -r requirements.txt   `

If a requirements.txt file is not provided, you can install the required packages individually:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bash/usr/local/bin/pip3.11 install scapy tabulate matplotlib   `

Configuration
-------------

The analyzer is highly configurable through a dictionary within the script. Below are the key configuration parameters and how to set them:

Configuration Parameters
------------------------

Located within the main() function of ws\_traffic.py:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pythonconfig = {      'WHATSAPP_DOMAINS': [          "whatsapp.com",          "api.whatsapp.com",          "web.whatsapp.com",          "wa.me",          "whatsapp.net",          "chat.whatsapp.com",      ],      'IP_UPDATE_INTERVAL': 3600,  # in seconds (1 hour)      'TIME_WINDOW_SECONDS': 1,      'UPDATE_INTERVAL': 1,  # in seconds      'PACKET_HISTORY_LENGTH': 60,  # Last 60 seconds      'EVENT_THRESHOLD': 3,      'DEFAULT_INTERFACE': "en2",      'LOG_FILE': "whatsapp_packet_log.csv",      'ENABLE_PLOTTING': False  # Set to True to enable plotting  }   `

Key Configuration Options
-------------------------

*   **WHATSAPP\_DOMAINS:** List of WhatsApp-related domains to resolve and monitor.
    
*   **IP\_UPDATE\_INTERVAL:** Time interval (in seconds) to re-resolve WhatsApp IP addresses. Defaults to 1 hour.
    
*   **TIME\_WINDOW\_SECONDS:** Duration (in seconds) for each packet capture window.
    
*   **UPDATE\_INTERVAL:** Frequency (in seconds) at which packet capturing occurs.
    
*   **PACKET\_HISTORY\_LENGTH:** Number of recent packet counts to store for plotting purposes.
    
*   **EVENT\_THRESHOLD:** Minimum number of packets to classify an event as SENT or RCVD.
    
*   **DEFAULT\_INTERFACE:** Network interface to monitor (e.g., en2, eth0). Change this based on your system.
    
*   **LOG\_FILE:** Name of the CSV log file where data will be stored.
    
*   **ENABLE\_PLOTTING:** Boolean flag to enable (True) or disable real-time plotting.
    

Usage
-----

1\. Run the Script
------------------

Note: Packet capturing requires administrative privileges. Use sudo to run the script.

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashsudo /usr/local/bin/python3.11 ws_traffic.py   `

Or, if you're using a virtual environment:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashsudo ./venv/bin/python3.11 ws_traffic.py   `

2\. Specify a Different Network Interface (Optional)
----------------------------------------------------

If you wish to use a different network interface (e.g., en3), modify the DEFAULT\_INTERFACE parameter in the configuration dictionary or adjust the script to accept command-line arguments.Example modification in ws\_traffic.py:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pythonimport argparse  def main():      parser = argparse.ArgumentParser(description="WhatsApp Packet Capture Analyzer")      parser.add_argument('-i', '--interface', type=str, help='Network interface to sniff on (e.g., en2)', default='en2')      args = parser.parse_args()      config = {          # ... other configurations ...          'DEFAULT_INTERFACE': args.interface,          # ... other configurations ...      }      # ... rest of the main function ...   `

Then run:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashsudo /usr/local/bin/python3.11 ws_traffic.py --interface en3   `

Output
------

1\. Console Output
------------------

The script prints real-time packet information in a neatly formatted table. Integer columns (S for Sent Packets and R for Received Packets) are right-aligned for better readability.**Sample Console Output:**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   textResolved whatsapp.com: 157.240.229.60  Resolved api.whatsapp.com: 157.240.14.52  Resolved web.whatsapp.com: 157.240.14.52  ...  Time                SRC IP(s)              DST IP(s)              S   R   Event  2024-10-08 20:32:56 185.203.218.118,...   ...                    8   10  RCVD  ...   `

2\. CSV Log File
----------------

All captured data is logged into a CSV file (whatsapp\_packet\_log.csv by default), which can be easily imported into Excel for further analysis.**Sample CSV Content:**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   textTime,SRC IP(s),DST IP(s),S,R,Event  2024-10-08 20:32:56,185.203.218.118,...,8,10,RCVD  ...   `

Importing Data into Excel
-------------------------

To analyze the captured data using Excel:

1.  Open Excel.
    
2.  Navigate to the Data Tab:
    
    *   Click on From Text/CSV.
        
3.  Select the CSV File:
    
    *   Choose whatsapp\_packet\_log.csv.
        
4.  Import Wizard:
    
    *   Ensure that the delimiter is set to Comma.
        
5.  Complete the Import:
    
    *   Click Load to import the data into Excel.
        

Result: You will have a structured table with columns for Time, Source IP(s), Destination IP(s), Sent Packets (S), Received Packets (R), and Event classification.

Applying Machine Learning
-------------------------

With the logged CSV data, you can apply various machine learning algorithms to identify patterns in WhatsApp conversations.

Steps Overview:
---------------

1.  pythonimport pandas as pddf = pd.read\_csv('whatsapp\_packet\_log.csv')
    
    *   Load Data using libraries like pandas.
        
2.  **Feature Engineering**
    
    *   Extract time-based features and aggregate packet counts.
        
3.  **Model Selection**
    
    *   Choose appropriate algorithms for clustering or classification.
        
4.  **Model Evaluation**
    
    *   Assess model performance using metrics like accuracy and precision.
        
5.  **Visualization**
    
    *   Use libraries like matplotlib or seaborn for visualizing patterns.
        

Improving the Analyzer
----------------------

While functional, there are several ways to enhance its capabilities:

1.  Enhanced Packet Filtering:
    
    *   Focus on specific protocols or ports used by WhatsApp.
        
2.  Data Enrichment:
    
    *   Add geolocation data or track data volume over time.
        
3.  Advanced Logging:
    
    *   Log data in JSON format or integrate with databases.
        
4.  Real-Time Notifications:
    
    *   Implement alerting mechanisms for specific events or anomalies.
        
5.  User Interface Enhancements:
    
    *   Develop a web-based interface for monitoring traffic in real-time.
        
6.  Performance Optimization:
    
    *   Optimize packet capturing using multithreading/multiprocessing.
        
7.  Security Enhancements:
    
    *   Secure log files and implement access controls.
        

Ethical and Legal Considerations
--------------------------------

Monitoring network traffic involves handling potentially sensitive data; adhere to ethical guidelines and legal regulations:

1.  Personal Use Only: Intended for personal use only; obtain consent before monitoring network traffic.
    
2.  Authorization: Ensure explicit permission is obtained before monitoring any network.
    
3.  Data Privacy: Handle logged metadata responsibly.
    
4.  Compliance: Be aware of local laws regarding network monitoring.
    
5.  Security: Secure log files from unauthorized access.
    

Troubleshooting
---------------

1.  **Permission Denied Errors**
    
    *   Run with administrative privileges using sudo.
        
2.  **Network Interface Issues**
    
    *   Verify correct interface name using ifconfig.
        
3.  **Dependency Issues**
    
    *   Ensure all required packages are installed.
        
4.  **Log File Not Created or Empty**
    
    *   Check write permissions in the directory.
        
5.  **Real-Time Plot Not Displaying**
    
    *   Verify that matplotlib is installed correctly.
        
6.  **High Resource Usage**
    
    *   Limit PACKET\_HISTORY\_LENGTH or optimize processing logic.
        
7.  **Git Push HTTP Error**
    
    *   Check repository URL and consider using SSH for Git operations.
        

Contributing
------------

Contributions are welcome! Please feel free to submit issues or pull requests on GitHub.

License
-------

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
----------------

Thanks to all contributors and libraries used in this project!

Disclaimer
----------

This tool is intended solely for educational purposes; use it responsibly and ethically within legal boundaries.