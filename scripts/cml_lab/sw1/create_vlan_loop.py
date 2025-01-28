# Creating VLANs on a Switch with for loop
from netmiko import ConnectHandler
import getpass

sw1 = {
    'device_type': 'cisco_ios',
    'host': '10.10.20.173',
    'username': input('Enter your username: '),
    'password': getpass.getpass('Enter your password: ')
}

net_connect = ConnectHandler(**sw1)

net_connect.enable()

net_connect.send_command('conf t', expect_string=r'[\#>]', read_timeout=60)


for n in range(11, 13):
    print(f'Creating VLAN {n}...')
    create_vlans = [
        f'vlan {n}',
        f'name VLAN{n}',
        'exit',
        ]
    output = net_connect.send_config_set(create_vlans)
    print(f'Output for VLAN {n}: {output}')
    print('-' * 80)

net_connect.send_command('end', expect_string=r'[\#>]', read_timeout=60)
output = net_connect.send_command('copy running-config startup-config', 
                                  expect_string=r'Destination filename \[startup-config\]\?', 
                                  read_timeout=60)
output += net_connect.send_command('\n')
print(output)

net_connect.disconnect()