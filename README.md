# PMKID Attack Script
This Python script performs a PMKID attack on a Wi-Fi network to obtain the Pairwise Master Key ID (PMKID) hash, which can be used to crack the Wi-Fi password. The script uses the hcxdumptool and hashcat tools to capture the PMKID hash and crack it, respectively.

# Prerequisites
Linux operating system
hcxdumptool and hcxpcapngtool tools installed
hashcat tool installed
termcolor Python package installed
# Usage
Clone the repository:

```
git clone https://github.com/0xissam/pmkider.git
```
Change directory to the cloned repository:

```
cd pmkider
```
Run the script:

```
python3 pmkider.py
```
Follow the prompts to enter the interface on monitor mode and the MAC address of the target access point.

Wait for the script to capture the PMKID hash and write it to a file called hash.hc22000.

When prompted, choose whether to crack the hash using hashcat. If you choose to crack the hash, the script will run hashcat with the PMKID hash file as input and the /usr/share/wordlists/rockyou.txt wordlist.
