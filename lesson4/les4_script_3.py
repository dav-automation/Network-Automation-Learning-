#!/usr/bin/env python

"""
Read in the "show_version.txt" file. From this file use regular expressions to extract the
os_version, serial_number, and configuration register value.
Your output should look as follows:
          OS Version: 15.4(2)T1
       Serial Number: FTX0000038X
     Config Register: 0x2102
"""

from __future__ import print_function, unicode_literals
import re

with open("show_version.txt") as f:
    show_ver = f.read()

match = re.search(r"^Cisco IOS Software,.* Version (.*),", show_ver, flags=re.M)
if match:
    os_version = match.group(1)

match = re.search(r"^Processor board ID (.*)\s*$", show_ver, flags=re.M)
if match:
    serial_number = match.group(1)

match = re.search(r"^Configuration register is (.*)\s*$", show_ver, flags=re.M)
if match:
    config_register = match.group(1)

print()
print(f"{'OS Version': >20}: {os_version:15}")
print(f"{'Serial Number':>20}: {serial_number:15}")
print(f"{'Config Register':>20}: {config_register:15}")
print()
    


