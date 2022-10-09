#!/usr/bin/python3

import socket
import sys

if len(sys.argv) != 2:
        print("Usage: vrfy.py namelist.txt")
        sys.exit(0)

# Create a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Server
connect = s.connect(('10.11.1.217',25))

# Receive the banner
banner = s.recv(1024)
print(banner)

# Brute force wordlist provided line by line. 
f = open(sys.argv[1])
print("Brute forcing in progress...")
for line in f:
	msg = "VRFY " + line
	print("Trying " + line.upper())
	s.send(msg.encode())
	result = s.recv(1024)
	print(result)
f.close()

# Close the socket
s.close()
