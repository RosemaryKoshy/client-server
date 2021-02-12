"""
TCP Web Server
Talib Pierson
Fri Feb 12
"""
from socket import *

# SOCK_STREAM for TCP
sock = socket(AF_INET, SOCK_STREAM)

sock.bind(('', 42069))
sock.listen()

while True:
    # Establish connection
    print('listening: ', end='')
    connection, _ = sock.accept()
    try:
        msg = connection.recv(1024).decode()
        file = msg.split()[1][1:]
        print(file)
        f = open(file)
        data = f.read()

        # Send one HTTP header line to socket
        connection.send('HTTP/1.1 200 OK\r\n\r\n'.encode())

        # Send object to client
        for i in range(0, len(data)):
            connection.send(data[i].encode())
        connection.send('\r\n'.encode())

        connection.close()
    except IOError:
        # Send 404 message
        connection.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())

        # Close client socket
        connection.close()

sock.close()
