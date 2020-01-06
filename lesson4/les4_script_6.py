#!/usr/bin/env python
"""
This is my own example. Create a script that reads show version document , determine if it is an 
IOS-XR, IOS-XE or NX-OS firmware show version document. And determine the firmware / OS version.
For this example, use show_version1.txt, show_version2.txt and show_version3.txt 
"""
from __future__ import print_function, unicode_literals
import re

with open("show_version3.txt") as f:
    show_ver = f.read()

banner = '-' * 80

#Check if the show_version doc is for Nexus and detemine the NXOS Version:
if 'Nexus' in show_ver:
    match = re.search(r"^ NXOS: version (.*)$", show_ver, flags=re.M)
    if match:
        os_ver = match.group(1)
        print()
        print(banner)
        print(f"{'NXOS VERSION':>20}: {os_ver:15}")
        print(banner)
        
# Check if the show_version doc is for IOS-XE and determine the IOS-XE version:
elif 'XE' in show_ver:
    match = re.search(r"^Cisco IOS.*, Version (.*)$", show_ver, flags=re.M)
    if match:
        os_ver = match.group(1)
        print()
        print(banner)
        print(f"{'IOS-XE VERSION':>20}: {os_ver:15}")
        print(banner)

# Check if the show_version if for IOS-XR and determine the IOS-XR version
elif 'XR' in show_ver:
    match = re.search(r"^Cisco IOS.*, Version (.*)", show_ver, flags=re.M)
    if match:
        match1 = match.group(1)
        os_ver = re.sub(r"\[Default\]", "", match1)
        os_ver = os_ver.strip()
        print()
        print(banner)
        print(f"{'IOS-XR VERSION':>20}: {os_ver:15}")
        print(banner)
        print()

    