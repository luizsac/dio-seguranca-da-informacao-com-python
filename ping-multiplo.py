import os
from time import sleep

with open("hosts.txt", "r") as file:
    hosts = file.read().splitlines()

print(hosts)

for host in hosts:
    os.system(f"ping -n 2 {host}")
    print("-" * 60)
    sleep(5)  # em segundos