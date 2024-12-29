import sys # System settings
import time # Time handling
import argparse # Command-line arguments
from termcolor import colored # Colored text output
from argparse import RawTextHelpFormatter # Text formatting
from scapy.all import * # Network access via NIC
from scapy.layers.dot11 import Dot11, Dot11Deauth, RadioTap, Dot11Beacon # Network control
import logging # Event logging
import requests # Real-time alerts
import statistics # Signal strength analysis

# Logging configuration
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

# Banner and Information
banner_intro = """
██╗  ██╗ █████╗ ██╗   ██╗ █████╗  ██████╗██╗  ██╗
██║ ██╔╝██╔══██╗██║   ██║██╔══██╗██╔════╝██║  ██║
█████╔╝ ███████║██║   ██║███████║██║     ███████║
██╔═██╗ ██╔══██║╚██╗ ██╔╝██╔══██║██║     ██╔══██║
██║  ██╗██║  ██║ ╚████╔╝ ██║  ██║╚██████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

              Kavach - The Ultimate Protector
----------------------------------------------------
"""

Information = """
This script detects rogue access points, even with MAC randomization, and logs or deauthenticates them.
Command to run this code: sudo python kavach.py -m (mode) -i (interface)
Modes:
1 : Log Rogue Access points activities
2 : Log & Deauth Rogue Access points activities

"""

# Command-line argument setup
parser = argparse.ArgumentParser('To run this code you have select mode and Interface', description=Information, formatter_class=RawTextHelpFormatter)
parser.add_argument('-m', '--mode', required=True, dest="mode", type=str, help="modes (1: Log only, 2: Log & Deauth)")
parser.add_argument('-i', '--interface', required=True, help="Interface (Monitor Mode)", type=str)
args = parser.parse_args()

# Webhook URL for alerts
WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL"

# Function to send alerts
def send_discord_alert(message):
    payload = {"content": message}
    requests.post(WEBHOOK_URL, json=payload)

# Log events
def log_event(log_entry):
    with open("/var/log/scanwifi.log", "a") as f:
        f.write(str(log_entry) + "\n")

# Scan for WiFi signals
def scan_packets(packet):
    if packet.haslayer(Dot11Beacon):
        ssid = packet.info.decode('utf-8')
        bssid = packet.addr2
        rssi = packet.dBm_AntSignal
        entry = (bssid, ssid, rssi)
        if entry not in discovered_list:
            discovered_list.append(entry)

# Analyze network activity
def analyze_activity(discovered_list, detected_aps, mode):
    for bssid, ssid, rssi in discovered_list:
        if bssid not in detected_aps:
            detected_aps[bssid] = {"ssids": {ssid}, "rssi_values": [rssi]}
        else:
            detected_aps[bssid]["ssids"].add(ssid)
            detected_aps[bssid]["rssi_values"].append(rssi)

        if len(detected_aps[bssid]["ssids"]) > 1 or len(detected_aps[bssid]["rssi_values"]) > 5:
            if statistics.stdev(detected_aps[bssid]["rssi_values"]) > 3:
                log_time = time.strftime("%A | %x | %X")
                fake_ap_count = len(detected_aps[bssid]["ssids"])
                log_entry = f"{log_time} | MAC: {bssid} | RogueAP Count: {fake_ap_count}"
                print(colored(f"[Detected] {log_entry}", 'blue'))
                rogue_list.append(bssid)
    for bssid in rogue_list:
        if mode == "2":
            deauth_attack(bssid)
            send_discord_alert(f"Deauth on MAC: {bssid} | FakeAP count: {fake_ap_count}")
        else:
            send_discord_alert(f"Log: Rogue AP Detected for MAC: {bssid} | FakeAP count: {fake_ap_count}")
            log_event(log_entry)
    time.sleep(3)
    return rogue_list

# Deauthentication attack
def deauth_attack(target_mac):
    print(colored(f"[*] Deauth Attack on {target_mac}", 'red'))
    deauth_packet = RadioTap() / Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2=target_mac.lower(), addr3=target_mac.lower()) / Dot11Deauth()
    sendp(deauth_packet, iface=args.interface, count=120, inter=.2, verbose=False)
    print(colored("[*] Attack completed.", 'green'))

if __name__ == '__main__':
    interface = args.interface
    mode = args.mode
    os.system("clear")
    print(banner_intro)
    print("Starting Kavach - WiFi Signals Monitoring")
    print(f"Mode: {mode} | Time: {time.strftime('%c')}")

    discovered_list = []
    detected_aps = {}
    while True:
        time.sleep(10)
        rogue_list = []
        sniff(iface=interface, count=4, prn=scan_packets)
        rogue_list = analyze_activity(discovered_list, detected_aps, mode)
        time.sleep(2)