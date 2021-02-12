"""
UDP Ping Client
Talib Pierson
Fri Feb 12
"""
import time
import socket as s

# SOCK_DGRAM for UDP
SOCK = s.socket(s.AF_INET, s.SOCK_DGRAM)
SOCK.settimeout(1)
HOST = input('Enter host: ')
PORT = int(input('Enter port: '))
SOCK.connect((HOST, PORT))

MSG_COUNT = 10
res_count = 0
delay_tot = 0

for i in range(MSG_COUNT):
    msg = f'ping {i}'
    t_0 = time.time()
    SOCK.send(msg.encode())
    try:
        res = SOCK.recv(1024).decode()
        t_1 = time.time()
        delay = (t_1 - t_0) * 1000
        res_count += 1
        delay_tot += delay
        print(res)
        print(f'{i} RTT={delay} ms')
    except s.timeout as e:
        print(f'{i} RTT=*')

print('average delay:', delay_tot / MSG_COUNT)
print('response rate:', res_count / MSG_COUNT)
