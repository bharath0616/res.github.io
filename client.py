import socket
import select
client_sockets = []

while True:
    # use select to monitor the server socket and all active client sockets for incoming data
    read_sockets, _, _ = select.select([server_socket] + client_sockets, [], [], 1)

    for sock in read_sockets:
        if sock is server_socket:
            # if the server socket is ready to read, accept the incoming connection
            client_socket, client_address = server_socket.accept()
            print('New connection from', client_address)

            # add the new client socket to the list of active client sockets
            client_sockets.append(client_socket)
        else:
            # if a client socket is ready to read, receive data from it
            data = sock.recv(1024)

            if not data:
                # if the client has disconnected, remove its socket from the list of active client sockets
                print('Client disconnected')
                client_sockets.remove(sock)
            else:
                # otherwise, broadcast the received data to all other active client sockets
                for client in client_sockets:
                    if client is not sock:
                        client.send(data)