# Import socket module
from socket import *

# Prepare server socket
# SOCK_STREAM for TCP, SOCK_DGRAM for UDP
serverSocket = socket(AF_INET, SOCK_STREAM)
# Your code starts here
serverSocket.bind(('', 42069))
serverSocket.listen()
# Your code ends here
while True:
    # Establish connection
    print('listening: ', end='')
    connectionSocket, addr = serverSocket.accept()  # Your code starts here # Your code ends here
    try:
        message = connectionSocket.recv(1024).decode()  # Your code starts here # Your code ends here
        filename = message.split()[1]
        print(filename[1:])
        f = open(filename[1:])
        outputdata = f.read()  # Your code starts here # Your code ends here

        # Send one HTTP header line to socket
        # Your code starts here
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        # Your code ends here

        # Send object to client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send('\r\n'.encode())

        connectionSocket.close()
    except IOError:
        # Send 404 message
        # Your code starts here
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
        # Your code ends here

        # Close client socket
        # Your code starts here
        connectionSocket.close()
        # Your code ends here

serverSocket.close()
