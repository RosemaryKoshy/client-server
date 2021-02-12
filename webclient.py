"""
TCP Web Client
Talib Pierson
Fri Feb 12
"""
from socket import *

# SOCK_STREAM for TCP
SOCK = socket(AF_INET, SOCK_STREAM)
HOST = input('Enter host: ')
POST = int(input('Enter port: '))
PATH = input('Enter path: ')
SOCK.connect((HOST, POST))

# Send HTTP get request to host
REQ = f'GET /{PATH} HTTP/1.1'
SOCK.send(REQ.encode())

# Receive and output data
msg = SOCK.recv(1024).decode()
while msg:
    print(msg, end='')
    msg = SOCK.recv(1024).decode()

SOCK.close()
