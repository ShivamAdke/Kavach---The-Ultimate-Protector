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

<h1 style="color:blue; font-weight:bold;">Features</h1>

Detects rogue access points, including those with randomized MAC addresses.

Logs details of detected access points.

Sends real-time alerts via Discord webhook.

Supports deauthentication attacks on rogue access points.

Provides detailed logs for further analysis.

User-friendly command-line interface.

<h1 style="color:blue; font-weight:bold;">Requirements</h1>

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
