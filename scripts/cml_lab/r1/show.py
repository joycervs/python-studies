# Basic commands on a Router
from netmiko import ConnectHandler
import getpass

r1 = {
    'device_type': 'cisco_ios',
    'host': '10.10.20.171', 
    'username': input('Enter your username: '),
    'password': getpass.getpass('Enter your password: ') 
}

net_connect = ConnectHandler(**r1)
net_connect.enable()

commands = [
    'show version',
    'show ip int brief',
]

for command in commands:
    print(f"Running: {command}")
    output = net_connect.send_command(command)
    print(output)
    print("-" * 80)

net_connect.disconnect()