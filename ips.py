import ipaddress

ip = '192.168.0.0/0 '

#ip = '192.168.0.1'

#endereco = ipaddress.ip_address(ip)

rede = ipaddress.ip_network(ip, strict=False)

for ip in rede:
    print(ip)

print(rede)