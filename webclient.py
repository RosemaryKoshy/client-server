# Import socket module
from socket import *

# Prepare server client
# SOCK_STREAM for TCP, SOCK_DGRAM for UDP
sock = socket(AF_INET, SOCK_STREAM)

host = input('Server IP address: ')
port = int(input('Server port: '))
path = input('Object path: ')

sock.connect((host, port))
req = f'GET /{path} HTTP/1.1'
sock.sendall(req.encode())

msg = sock.recv(1024).decode()
while msg:
    print(msg, end='')
    msg = sock.recv(1024).decode()

sock.close()
