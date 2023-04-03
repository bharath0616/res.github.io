import socket
import select

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a public host, and a well-known port
server_socket.bind(('0.0.0.0', 1234))

# set the socket to non-blocking mode
server_socket.setblocking(False)

# listen for incoming connections
server_socket.listen(5)
print('Server listening on port 1234')

