#!/usr/bin/env python

"""
Create a dictionary representing a network device. The dictionary should have key-value pairs
representing the 'ip_addr', 'vendor', 'username', and 'password' fields.
Print out the 'ip_addr' key from the dictionary.
If the 'vendor' field is 'cisco', then set the 'platform' to 'ios'. If the 'vendor' field is
'juniper', then set the 'platform' to 'junos'.
Create a second dictionary named bgp_fields. The bgp_fields should have a key for 'bgp_as',
'peer_as', and 'peer_ip'.
Using the .update() method add the bgp_fields key-value pairs to the network device dictionary.
Using a for-loop iterate over the dictionary and print out all of the dictionary keys.
Using a single for-loop iterate over the dictionary and print out all of the dictionary keys and
values.
"""

from __future__ import print_function, unicode_literals

net_device = {
    'ip_addr': '192.168.1.190',
    'vendor': 'cisco',
    'username': 'cisco',
    'password': 'cisco'
}

print()
print(net_device['ip_addr'])

if net_device['vendor'].lower() == 'cisco':
    net_device['platform'] = 'ios'
elif net_device['vendor'].lower() == 'juniper':
    net_device['platform'] = 'junos'

bgp_fields = {
    'bgp_as': 65000,
    'peer_as': 65001,
    'peer_ip': '192.168.1.191'
}

net_device.update(bgp_fields)

banner = '-' * 80
print(banner)

for key in net_device:
    print(f"{key:>15}")

print(banner)
print()

print(banner)
for key, value in net_device.items():
    print("{key:>15} ----> {value:>15}".format(key=key, value=value) )
print(banner)
print()