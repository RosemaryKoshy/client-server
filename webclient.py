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
print(req)
sock.send(req.encode())

msg = sock.recv(2048).decode()
sock.close()
print(msg)
