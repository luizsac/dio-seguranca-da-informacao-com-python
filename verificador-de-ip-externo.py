import re
import json
from urllib.request import urlopen

url = "https://ipinfo.io/json"
response = urlopen(url)
data = json.load(response)

ip = data["ip"]
org = data["org"]
city = data["city"]
country = data["country"]
region = data["region"]

print("Detalhes do IP externo:")
print(f"IP: {ip}\nRegião: {region}\nPaís: {country}\nCidade: {city}\nEmpresa: {org}")
