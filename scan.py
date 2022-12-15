import socket
import time
import threading
import concurrent.futures
import colorama
from colorama import Fore

colorama.init()
print_lock = threading.Lock()

def title():
    title = """

█▀█ █▀█ █▀█ ▀█▀   █▀ █▀▀ ▄▀█ █▄░█
█▀▀ █▄█ █▀▄ ░█░   ▄█ █▄▄ █▀█ █░▀█
by solelh, thanks to retr00exe
"""       
    print(title)                                                                                 

def scan(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(100)
    try:
        scanner.connect((ip, port))
        scanner.close()
        with print_lock:
            print(Fore.WHITE + f"[{port}]" + Fore.GREEN + " Opened")
    except:
        pass

def main():
    title()
    ip = input("Enter the IP or the url to scan (ex: google.com): ")
    print("no bug found")
    time.sleep(1)
    print("[*] Checking from port 1 to port 65535")
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(0xFFFF):
            executor.submit(scan, ip, port + 1)

if __name__ == "__main__":
    main()