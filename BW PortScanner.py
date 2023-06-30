#!/bin/python3

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
        print("Invalid amount of arguments.")
        print("Syntax: python3 scanner.py")

__course__ = 'Cybersecurity CY033023'
__version__ = '1.0.1'
__maintainer__ = 'Brian White'
__description__ = 'Basic Scanner'

#Banner added...
print("=" * 30)
print('Course: ' + __course__)
print('Version: ' + __version__)
print('Maintainer: ' + __maintainer__)
print('Description: ' + __description__)
print("=" * 26)
print('')
print("Scanning for open ports...")
print('')
print('=' * 28)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("=" * 40)

try:
        for port in range(1, 10000):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = s.connect_ex((target,port)) #returns an error indicator - if port is open it throws a 0, otherwise 1
                if result == 0:
                        print("Port {} is open".format(port))
                s.close()

except KeyboardInterrupt:
        print("=" * 16)
        print("\nExiting program")
        print("=" * 16)
        sys.exit()

except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()

except socket.error:
        print("Could not connect to server.")
        sys.exit()