# Basic commands on a Router
from netmiko import ConnectHandler
import getpass
from dotenv import load_dotenv
import os

load_dotenv()

r1 = {
    'device_type': 'cisco_ios',
    'host': os.getenv('R1_HOST'), 
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
