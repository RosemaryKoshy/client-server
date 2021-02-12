"""
TCP Web Server
Talib Pierson
Fri Feb 12
"""
import socket as s

# SOCK_STREAM for TCP
SOCK = s.socket(s.AF_INET, s.SOCK_STREAM)
SOCK.bind(('', 42069))
SOCK.listen()

while True:
    # Establish connection
    print('listening: ', end='')
    connection, _ = SOCK.accept()
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

SOCK.close()
