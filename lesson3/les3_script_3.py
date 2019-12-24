#!/usr/bin/env python
'''
Read the 'show_lldp_neighbors_detail.txt' file. Loop over the lines of this file. Keep reading the
lines until you have encountered the remote "System Name" and remote "Port id". Save these two items
into variables and print them to the screen. You should extract only the system name and port id
from the lines (i.e. your variables should only have 'twb-sf-hpsw1' and '15'). Break out of your
loop once you have retrieved these two items.
'''
from __future__ import print_function, unicode_literals

with open("show_lldp_neighbors_detail.txt") as f:
    show_lldp = f.read()
    
(res1, res2) = (False, False)

for line in show_lldp.splitlines():
    if line.startswith('----'):
        continue
    elif "System Name" in line:
        fields = line.split(':')
        sys_name = fields[1]
        res1  = True
    elif "Port id" in line:
        fields = line.split(':')
        port_id = fields[1]
        res2 = True
    
    if res1 and res2:
        break
print()
print(f"System Name: {sys_name}")
print(f"Port ID: {port_id}")
print()

    
    