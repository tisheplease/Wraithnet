# WRAITHNET - Wi-Fi Penetration Testing Toolkit

WRAITHNET is a comprehensive toolkit for Wi-Fi penetration testing, designed to help security enthusiasts, researchers, and pentesters test and secure wireless networks. The toolkit includes several essential penetration testing features like Wi-Fi network scanning, client analysis, deauth attacks, password cracking, and more.

## Features
- **Wi-Fi Network Scanning**: Scan available Wi-Fi networks and gather detailed information.
- **Client Analysis**: Analyze connected clients to a specific access point.
- **Deauth Attack**: Perform a Deauthentication attack to disconnect clients from an access point.
- **WPA Handshake Capture**: Capture WPA handshakes for later cracking.
- **WPA Brute Force Attack**: Brute force WPA passwords using a wordlist.
- **Pixie Dust Attack**: Run Pixie Dust attack for offline WPA key recovery.
- **PMKID Attack**: Run PMKID attack for cracking WPA passwords.
- **MAC Spoofing**: Change the MAC address of your network interface.
- **Dependency Installation**: Automatically installs required dependencies for various Linux distributions.

## Installation

### Requirements:
- **Linux OS** (Debian/Ubuntu preferred, other distributions supported)
- **Python 3.x**
- **Required Packages**: `net-tools`, `aircrack-ng`, `reaver`, `hashcat`

### Steps to Install:
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/tisheplease/Wraithnet.git
   cd WRAITHNET

    Install dependencies: The script will attempt to automatically install required dependencies based on your distribution. To manually install dependencies, use:

sudo apt install net-tools aircrack-ng reaver hashcat

Run the program: To run the program, execute:

    sudo python3 wraithnet.py

    Make sure you have the necessary permissions to run the program (root privileges required for network-related tasks).

Usage

    Launch the program:

    sudo python3 wraithnet.py

    Select an option from the menu to perform various tasks such as scanning Wi-Fi networks, conducting attacks, or performing analysis.

    Follow the on-screen instructions for each operation.

Authors

    @tisheplease (Lead Developer)

    @mp4dev (Contributor)
