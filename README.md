Kavach - The Ultimate Protector

Overview

Kavach is a powerful script designed to detect rogue access points, even with MAC randomization, and provides options to either log or deauthenticate them. It is built for educational purposes and to help protect networks and sensitive data.

Features

Detects rogue access points, including those with randomized MAC addresses.

Logs details of detected access points.

Sends real-time alerts via Discord webhook.

Supports deauthentication attacks on rogue access points.

Provides detailed logs for further analysis.

User-friendly command-line interface.

Requirements

Python 3

Required Python Libraries:

scapy

requests

termcolor

argparse

statistics

Setup

Clone this repository:

git clone https://github.com/ShivamAdke/Kavach---The-Ultimate-Protector.git
cd kavach

Install dependencies:

pip install -r requirements.txt

Update the Discord webhook link in the script:

WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL"

Usage

Run the script with sudo to ensure proper permissions:

Command Structure

sudo python kavach.py -m <mode> -i <interface>

Modes:

Log Only - Logs rogue AP activities:

sudo python kavach.py -m 1 -i wlan0

Log & Deauth - Logs and deauthenticates rogue APs:

sudo python kavach.py -m 2 -i wlan0

Replace wlan0 with your wireless interface in monitor mode.

Output

Logs are saved to:

/var/log/scanwifi.log

Alerts are sent to the configured Discord Webhook.

Example Output

[Detected] Monday | 12/25/2024 | 10:45:12 | MAC: 00:11:22:33:44:55 | RogueAP Count: 3
[*] Deauth Attack on 00:11:22:33:44:55
[*] Attack completed.

Disclaimer

This tool is strictly for educational and security auditing purposes only. Use it responsibly and with proper authorization. Misuse of this tool may result in legal consequences. The creators are not responsible for any misuse or damage caused.

References

Inspired by tools and techniques demonstrated by Hak5:

Hak5 Tools and Tutorials

License

This project is licensed under the MIT License

Contributing

Feel free to fork this repository, submit issues, or create pull requests to improve this project.

Support

For any queries or issues, reach out via GitHub issues or Discord channel.

Authors

Shivam

Important Notes

Always test this tool in a controlled environment. Do not use it on unauthorized networks.
