#!/usr/bin/env python
"""Create a list of five IP addresses.
Use the .append() method to add an IP address onto the end of the list. Use the .extend()
method to add two more IP addresses to the end of the list.
Use list concatenation to add two more IP addresses to the end of the list.
Print out the entire list of ip addresses. Print out the first IP address in the list. Print out
the last IP address in the list.
Using the .pop() method to remove the first IP address in the list and the last IP address in
the list.
Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address
in the list.
"""
ip_addr_list = ['192.168.0.1', '10.1.1.1', '172.16.34.1', '3.3.3.3', '4.4.4.4']
ip_addr_list.append('192.168.1.1')
ip_addr_list.extend(['192.168.2.1', '10.6.10.1'])
ip_addr_list = ip_addr_list + ['192.168.3.1', '10.6.20.1']
print()
banner = '-' * 80
print(ip_addr_list)
print(banner)
print(f"The first IP address in the list: {ip_addr_list[0]}")
print(banner)
print(f"The last IP address in the list: {ip_addr_list[-1]}")
print(banner)
print(f"The first IP address removed using pop: {ip_addr_list.pop(0)}")
print(banner)
print(f"The last IP address removed using pop: {ip_addr_list.pop()}")
print(banner) 
print("Updating the existing first IP address with new one: ")
ip_addr_list[0] = '2.2.2.2'
print(ip_addr_list)
print(banner)