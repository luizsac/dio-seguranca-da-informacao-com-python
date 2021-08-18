import ipaddress

ip = "192.168.0.1"

address = ipaddress.ip_address(ip)
print(address)
print(address + 257)

ip_net = "192.168.0.0/24"

net = ipaddress.ip_network(ip_net, strict=False)  # strict=False para aceitar qualquer ip da rede, ex.: "192.168.0.69/24"
print(net)
for ip in net:
    print(ip)

