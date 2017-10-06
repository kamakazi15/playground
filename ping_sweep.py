#!/usr/bin/env python3

# Simple ping sweep script

import os
import sys

if len(sys.argv) < 1:
    print("Usage: ping_sweep.py <IP_address>")
    exit(0)

for ip in sys.argv[1:]:
    response = os.system("ping -c 1 -W 2 " + ip + " > /dev/null")
    if response == 0:
        print(ip, "is up!")
    else:
        print(ip, "is down...")