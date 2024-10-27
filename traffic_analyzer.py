from scapy.all import *
import time

class NetworkTrafficAnalyzer:
    def __init__(self):
        self.packets = []

    def packet_callback(self, packet):
        """Callback function to process each packet."""
        self.packets.append(packet)
        print(f"Packet Captured: {packet.summary()}")
        
    def start_capture(self, interface=None):
        """Start capturing packets."""
        print("Starting packet capture...")
        if interface:
            sniff(iface=interface, prn=self.packet_callback, store=False)
        else:
            sniff(prn=self.packet_callback, store=False)

    def analyze_traffic(self):
        """Analyze the captured traffic."""
        print("\nAnalyzing captured packets...\n")
        for packet in self.packets:
            if IP in packet:
                ip_src = packet[IP].src
                ip_dst = packet[IP].dst
                print(f"Source: {ip_src} -> Destination: {ip_dst}")

def main():
    analyzer = NetworkTrafficAnalyzer()
    interface = input("Enter the network interface to capture (or press Enter for default): ")
    
    try:
        analyzer.start_capture(interface)
    except KeyboardInterrupt:
        print("\nCapture stopped. Analyzing traffic...")
        analyzer.analyze_traffic()

if __name__ == "__main__":
    main()
