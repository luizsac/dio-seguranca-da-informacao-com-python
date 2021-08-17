import os

ip_host = input("IP ou Host a ser pingado: ")

os.system(f"ping -n 6 {ip_host}")