"""
TCP Web Client
Talib Pierson
Fri Feb 12
"""
from socket import *

# SOCK_STREAM for TCP
sock = socket(AF_INET, SOCK_STREAM)

host = input('Server IP address: ')
port = int(input('Server port: '))
path = input('Object path: ')

# Establish connection
sock.connect((host, port))
req = f'GET /{path} HTTP/1.1'
sock.send(req.encode())

msg = sock.recv(1024).decode()
while msg:
    print(msg, end='')
    msg = sock.recv(1024).decode()

sock.close()
