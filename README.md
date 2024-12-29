<h1 style="text-align:center;">
# Kavach - The Ultimate Protector

```
██╗  ██╗ █████╗ ██╗   ██╗ █████╗  ██████╗██╗  ██╗
██║ ██╔╝██╔══██╗██║   ██║██╔══██╗██╔════╝██║  ██║
█████╔╝ ███████║██║   ██║███████║██║     ███████║
██╔═██╗ ██╔══██║╚██╗ ██╔╝██╔══██║██║     ██╔══██║
██║  ██╗██║  ██║ ╚████╔╝ ██║  ██║╚██████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

              Kavach - The Ultimate Protector
----------------------------------------------------
```
</h1>

<h1 style="color:blue; font-weight:bold;">Overview</h1>

Kavach is a powerful script designed to detect rogue access points, even with MAC randomization, and provides options to either log or deauthenticate them. It is built for educational purposes and to help protect networks and sensitive data.

<h2 style="font-size:24px; font-style:italic;">Role of WiFi Pineapple in Kavach</h2>

The WiFi Pineapple is a key component used in this project to simulate and detect rogue access points effectively. It is a specialized penetration testing tool designed by Hak5 for wireless network auditing. In this project:

Testing Rogue APs: The WiFi Pineapple acts as a rogue access point to mimic malicious networks, making it ideal for simulating attack scenarios.

Traffic Analysis: It captures wireless traffic, enabling the identification of unusual patterns, probing attempts, and unauthorized devices connecting to the network.

MAC Randomization Testing: The WiFi Pineapple can simulate APs with randomized MAC addresses, providing an environment to test Kavach’s ability to detect anomalies and inconsistencies.

Deauthentication Testing: By broadcasting multiple SSIDs, it helps evaluate Kavach’s response to excessive signal variations and the accuracy of deauthentication attacks.

<h2 style="font-size:24px; font-style:italic;">Role of WiFi Adapter in Kavach</h2>

A WiFi adapter with monitor mode and packet injection support is crucial for the Kavach project. The adapter performs the following tasks:

Packet Sniffing: It listens to wireless traffic, capturing management frames (beacons, probes) from nearby networks.

Monitor Mode Operation: It enables passive monitoring without actively connecting to any access point, which is essential for identifying rogue APs.

MAC Address Analysis: It inspects MAC addresses and their associated SSIDs to detect randomization patterns or inconsistencies that signal a rogue AP.

Deauthentication Attacks: The adapter is used to send deauth packets to forcefully disconnect clients from rogue APs, making it effective in mitigating threats in real time.

Signal Strength Monitoring: It measures RSSI (Received Signal Strength Indicator) values, helping Kavach detect anomalies caused by rogue devices broadcasting stronger signals than legitimate networks.

By combining the WiFi Pineapple for controlled testing and the WiFi adapter for scanning and defense, Kavach provides a comprehensive solution for rogue AP detection, logging, and mitigation.

<h1 style="color:blue; font-weight:bold;">Features</h1>

Detects rogue access points, including those with randomized MAC addresses.

Logs details of detected access points.

Sends real-time alerts via Discord webhook.

Supports deauthentication attacks on rogue access points.

Provides detailed logs for further analysis.

User-friendly command-line interface.

<h1 style="color:blue; font-weight:bold;">Requirements</h1>

Kali linux as os

Python 3

Required Python Libraries:

scapy

requests

termcolor

argparse

statistics

<h1 style="color:blue; font-weight:bold;">Setup</h1>

1.Clone this repository:

git clone https://github.com/ShivamAdke/Kavach---The-Ultimate-Protector.git

cd kavach

2.Install dependencies:

pip install -r requirements.txt

3.Update the Discord webhook link in the script:

WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL"

<h1 style="color:blue; font-weight:bold;">Usage</h1>

Run the script with sudo to ensure proper permissions:

<h1 style="color:blue; font-weight:bold;">Command Structure</h1>

sudo python kavach.py -m <mode> -i <interface>

<h1 style="color:blue; font-weight:bold;">Modes:</h1>

1.Log Only - Logs rogue AP activities:

sudo python kavach.py -m 1 -i wlan0

2.Log & Deauth - Logs and deauthenticates rogue APs:

sudo python kavach.py -m 2 -i wlan0

Replace wlan0 with your wireless interface in monitor mode.

<h1 style="color:blue; font-weight:bold;">Output</h1>

Logs are saved to:

/var/log/scanwifi.log

Alerts are sent to the configured Discord Webhook.

<h1 style="color:blue; font-weight:bold;">Example Output</h1>

[Detected] Monday | 12/25/2024 | 10:45:12 | MAC: 00:11:22:33:44:55 | RogueAP Count: 3
[*] Deauth Attack on 00:11:22:33:44:55
[*] Attack completed.

<h1 style="color:blue; font-weight:bold;">Disclaimer</h1>

This tool is strictly for educational and security auditing purposes only. Use it responsibly and with proper authorization. Misuse of this tool may result in legal consequences. The creators are not responsible for any misuse or damage caused.

<h1 style="color:blue; font-weight:bold;">References</h1>

Inspired by tools and techniques demonstrated by Hak5:

Hak5 Tools and Tutorials

<h1 style="color:blue; font-weight:bold;">License</h1>

This project is licensed under the MIT License

<h1 style="color:blue; font-weight:bold;">Contributing</h1>

Feel free to fork this repository, submit issues, or create pull requests to improve this project.

<h1 style="color:blue; font-weight:bold;">Support</h1>

For any queries or issues, reach out via GitHub issues or Discord channel.

<h1 style="color:blue; font-weight:bold;">Authors</h1>

Shivam

<h1 style="color:blue; font-weight:bold;">Important Notes</h1>

Always test this tool in a controlled environment. Do not use it on unauthorized networks.
