import os
import time
print("\n\
███████████████████████▀███████████\n\
█▄─▄▄─█▄─▄█▄─▀█▄─▄█─▄▄▄▄█▄─▄█▄─▄▄─█\n\
██─▄▄▄██─███─█▄▀─██─██▄─██─███─▄▄▄█\n\
▀▄▄▄▀▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▀▀\n\
")
print("coded by @solelh")
clavier = input("enter the RHOST ip adress>>")
hostname = (clavier)
while(1):
    time.sleep(1)
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"
