WRAITHNET 2.1 - Wi-Fi Penetration Testing Toolkit

WRAITHNET is a powerful and comprehensive toolkit designed for Wi-Fi penetration testing. It helps security professionals, researchers, and enthusiasts assess and secure wireless networks. The toolkit includes a variety of penetration testing features like Wi-Fi network scanning, client analysis, deauthentication attacks, WPA password cracking, and more.
Features

    Wi-Fi Network Scanning: Scan available Wi-Fi networks and gather detailed information.

    Client Analysis and WPA Handshake Capture: Analyze connected clients to a specific access point and capture WPA handshakes for later cracking.

    Deauth Attack: Perform a Deauthentication attack to disconnect clients from an access point.

    WPA Brute Force Attack: Brute force WPA passwords using a wordlist.

    Pixie Dust Attack: Run the Pixie Dust attack for offline WPA key recovery.

    Dependency Installation: Automatically installs required dependencies for various Linux distributions.

Installation
Requirements:

    Linux OS (Debian/Ubuntu preferred, other distributions supported)

    Python 3.x

    Required Packages: net-tools, aircrack-ng, reaver, hashcat

Steps to Install:

    Clone the repository to your local machine:

git clone https://github.com/tisheplease/Wraithnet.git
cd WRAITHNET

Install dependencies: The script will attempt to automatically install the required dependencies based on your distribution. To manually install dependencies, use:

sudo apt install net-tools aircrack-ng reaver hashcat

Run the program: To execute the program, run the following command:

    sudo python3 wraithnet.py

    Note: Make sure you have the necessary permissions to run the program (root privileges required for network-related tasks).

Usage

    Launch the program:

    sudo python3 wraithnet.py

    Select an option from the menu to perform various tasks, such as scanning Wi-Fi networks, conducting attacks, or performing analysis.

    Follow the on-screen instructions for each operation.

Authors

    @tisheplease (Lead Developer)

    @mp4dev (Contributor)
