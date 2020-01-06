from netmiko import Netmiko
from getpass import getpass
from pprint import pprint


my_device = {
    'host': '192.168.1.190',
    'username': 'cisco',
    'password': getpass(),
    'device_type': 'cisco_ios'
}

net_con = Netmiko(**my_device)

output = net_con.send_command("show arp", use_textfsm=True)
pprint(output)


