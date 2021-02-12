"""
UDP Ping Client
Talib Pierson
Fri Feb 12
"""
import time
from socket import *

# SOCK_DGRAM for UDP
SOCK = socket(AF_INET, SOCK_DGRAM)
HOST = input('Enter host: ')
PORT = int(input('Enter port: '))
SOCK.connect((HOST, PORT))

for i in range(10):
    msg = f'ping {i}'
    t_0 = time.time()
    SOCK.send(msg.encode())
    res = SOCK.recv(1024).decode()
    t_1 = time.time()
    if res != msg.upper():
        print(f'{i} Error: received incorrect response')
    else:
        print(f'{i} RTT={(t_1 - t_0) * 1000} ms')
