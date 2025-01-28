#Creating a loopback interface on a Router
from netmiko import ConnectHandler
import getpass

r1 = {
    'device_type': 'cisco_ios',
    'host': '10.10.20.171',
    'username': input('Enter your username: '),
    'password': getpass.getpass('Enter your password: '),
    'secret': getpass.getpass('Enter enable password: '),
}

net_connect = ConnectHandler(**r1)

net_connect.enable()

commands = [
    'conf t',
    'interface loopback 0',
    'ip address 1.1.1.1 255.255.255.0',
    'end',
    'show ip int brief'
]

for command in commands:
    print(f'Running: {command}')
    output = net_connect.send_command(command, expect_string=r'[\#>]', read_timeout=60)
    print(output)
    print('-' * 80)

net_connect.disconnect()
