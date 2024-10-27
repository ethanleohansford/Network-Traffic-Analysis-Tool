# Network Traffic Analysis Tool

A simple Network Traffic Analysis Tool implemented in Python that uses the `scapy` library to capture and analyze network packets in real-time.

## Features
- Capture live network packets.
- Display captured packets' summaries.
- Analyze captured traffic for source and destination IP addresses.

## Technologies Used
- **Python**
- **Scapy**: A powerful Python library used for packet manipulation.

## Requirements
- **Python 3.6+**
- **scapy** library

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Network-Traffic-Analysis-Tool.git
   cd Network-Traffic-Analysis-Tool

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
## Usage

1. Start the traffic analyzer:
   ```bash
   sudo python traffic_analyzer.py
   ```
   Note: Running as sudo is often required to capture network packets.
2. Choose the network interface to capture (or press Enter to use the default):
   ```vbnet
   Enter the network interface to capture (or press Enter for default):
   ```
3.Stop capturing packets by pressing Ctrl+C. The tool will then analyze and display the captured traffic.

## Example Output

- Packet captured:
   ```yaml
   Packet Captured: Ether / IP / TCP 192.168.1.10:443 > 192.168.1.20:54321 S
   ```
- Analyzing captured packets:
   ```yaml

   Analyzing captured packets...
   Source: 192.168.1.10 -> Destination: 192.168.1.20
   ```
   
## Limitations

This tool is basic and primarily for educational purposes. It may not handle high traffic volumes efficiently.
Scapy's performance can be limited by the capabilities of your machine and the size of captured packets.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests for enhancements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Conclusion
This simple Network Traffic Analysis Tool demonstrates how to capture and analyze network packets using Python and Scapy. You can enhance it by adding filtering options, saving the captured packets to a file, or implementing more complex analysis techniques.
