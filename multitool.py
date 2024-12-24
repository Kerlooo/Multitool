import os            # system commands
import socket         # port scanning, dns, connections
import scapy.all     # network analysis
import psutil        # system monitoring
import hashlib       # hashing
import requests      # http requests
#import pyOpenSSL     # SSL certificates 
#import python-nmap   # network scanning
import watchdog      # file system monitoring
import PIL          # metadata extraction
import ipaddress    # IP handling
import cryptography  # encryption/encoding
import logging      # logging capabilities



# Main function
def main():
    print("Welcome to the Multitool!")
    print("[1] Network")
    print(" [2] System")
    print("  [3] Security")
    print("   [4] Utilities")
    print("    [5] Exit")
    choice = input("Please select a category: ")
    
    if choice == "1":
        network()
    elif choice == "2":
        system()
    elif choice == "3":
        security()
    elif choice == "4":
        utilities()
    elif choice == "5":
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice")
        main()


def network():
    os.system('clear')
    print("Network Tools: ")
    print("[1] Port Scanner")
    print(" [2] DNS Lookup")
    print("  [3] Ping Sweep")
    print("   [4] IP Geolocation")


def system():
    os.system('clear')
    print("System Tools")
    print("[1] System Information")
    print(" [2] Process Monitoring")
    print("  [3] System info gather")
    print("   [4] File hash calculator")

def security():
    os.system('clear')
    print("Security Tools")
    print("[1] Password strength checker")
    print(" [2] Base64 encoder/decoder")
    print("  [3] URL encoder/decoder")
    

def utilities():
    os.system('clear')
    print("Utilities")

if __name__ == "__main__":
    main()
    