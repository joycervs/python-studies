#Creating a loopback interface on Router 1 and 2
from netmiko import ConnectHandler
import getpass
from dotenv import load_dotenv
import os

load_dotenv()

r1_ip = os.getenv('R1_HOST')
r2_ip = os.getenv('R2_HOST')

if not r1_ip or not r2_ip:
    print('Please specify your IP address')
    exit(1)

user = 'cisco'
password = getpass.getpass('Enter user password: ')
enable_password = getpass.getpass('Enter enable password: ')

routers = [
    {
        'device_type': 'cisco_ios',
        'host' : r1_ip,
        'username': user,
        'password': password,
        'secret': enable_password,
    },
    {
        'device_type': 'cisco_ios',
        'host' : r2_ip,
        'username': user,
        'password': password,
        'secret': enable_password,
    }
]


def config_loopbacks(net_connect, router_host):
    for l in range(4):
        commands = [
            f'interface loopback{l}'
        ]

        print('-' * 40)
        print(f'>>>> ROUTER {router_host}')
        print(f'Configuring interface loopback{l}...')
        output = net_connect.send_config_set(commands)
        print(f'Applied configuration:\n{output}')


for router in routers:
    try:
        net_connect = ConnectHandler(**router)
        net_connect.enable()

        config_loopbacks(net_connect, router['host'])
        
        print("\nInterface status: ")
        show_output = net_connect.send_command('show ip interface brief')
        print(show_output)

        net_connect.disconnect()
        print(f'Configuration completed on the router {router["host"]}\n')

    except Exception as e:
        print(f'Error configuring router {router["host"]}: {str(e)}')