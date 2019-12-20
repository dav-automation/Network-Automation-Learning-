#!/usr/bin/env python
"""
You have the following three variables from the arp table of a router:
mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"
Process these ARP entries and print out a table of "IP ADDR" to "MAC ADDRESS". The output
should look like following:
             IP ADDR          MAC ADDRESS
-------------------- --------------------
        10.220.88.29       5254.abbe.5b7b
        10.220.88.30       5254.ab71.e119
        10.220.88.32       5254.abc7.26aa
Two columns, 20 characters wide, data right aligned, a header column.
"""
mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

field1  = mac1.split()
mac1 = field1[3]
ip_addr1 = field1[1]

field2  = mac2.split()
mac2 = field2[3]
ip_addr2 = field2[1]

field3  = mac3.split()
mac3 = field3[3]
ip_addr3 = field3[1]

print()
print(f"{'IP ADDR':>20} {'MAC ADDRESS':>20}")
print(f"{'-'*20:>20} {'-'*20:>20}")
print(f"{ip_addr1:>20} {mac1:>20}")
print(f"{ip_addr2:>20} {mac2:>20}")
print(f"{ip_addr3:>20} {mac3:>20}")

