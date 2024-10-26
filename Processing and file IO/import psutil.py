import psutil

interfaces = psutil.net_if_addrs()
for interface_name, addresses in interfaces.items():
    print(f"Interface: {interface_name}")
    for address in addresses:
        print(f"  - {address.family.name}: {address.address}")