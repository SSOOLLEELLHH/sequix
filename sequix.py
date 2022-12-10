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
-----------------------------------------------------------------------")
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
	else:
		print("not found...")