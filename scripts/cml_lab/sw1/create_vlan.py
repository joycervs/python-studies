# Creating VLANs on a Switch
from netmiko import ConnectHandler
import getpass
from dotenv import load_dotenv
import os

load_dotenv()

sw1 = {
    'device_type': 'cisco_ios',
    'host': os.getenv('SW1_HOST'),
    'username': input('Enter your username: '),
    'password': getpass.getpass('Enter your password: ')
}

net_connect = ConnectHandler(**sw1)
net_connect.enable()

config_vlans = [
    'conf t', 
    'vlan 30',
    'name Dev',
    'exit',
    'vlan 40',
    'name Prod',
    'exit',
    'vlan 50',
    'name Lab',
    'end',
    'show ip int brief',
    'show vlan brief',
    'copy running-config startup-config',
]

for command in config_vlans:
    print(f'Running: {command}')
    output = net_connect.send_command(command, expect_string=r'[\#>]', read_timeout=60) 
    print(output)
    print('-' * 80)

net_connect.disconnect()
