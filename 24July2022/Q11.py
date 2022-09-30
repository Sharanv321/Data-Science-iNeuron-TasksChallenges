# Q11) write a code to check ip address of your system

# Importing socket package to print the IP address of the system

import socket
hostname = socket.gethostname()
IPAddress = socket.gethostbyname(hostname)
print("IP address of the computer is : ", IPAddress)