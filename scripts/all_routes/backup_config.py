#Creating backup config files
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


def backup_config(net_connect, router_host):
    
    print(f'\nBacking up configuration from {router_host}...')

    net_connect.send_command('terminal length 0')
    show_output = net_connect.send_command('show running-config')

    filename = f'{router_host}_running_config.txt'
    with open(filename, 'w') as f:
        f.write(show_output)
    
    print(f'Configuration backup saved as {filename}\n')


for router in routers:
    try:
        net_connect = ConnectHandler(**router)
        net_connect.enable()

        backup_config(net_connect, router['host'])
        
        net_connect.disconnect()
        print(f'Backup completed on router {router["host"]}\n')

    except Exception as e:
        print(f'Error backing up router {router["host"]}: {str(e)}')