"""
UDP Ping Server
Talib Pierson
Fri Feb 12
"""
import random
from socket import *

# SOCK_DGRAM for UDP
sock = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
sock.bind(('', 12000))

while True:
    # Receive client packet and arrival address
    msg, addr = sock.recvfrom(1024)
    # Capitalize the message
    msg = msg.upper()

    # Error simulator, 95% success rate
    if random.random() < 0.95:
        # Respond
        sock.sendto(msg, addr)
