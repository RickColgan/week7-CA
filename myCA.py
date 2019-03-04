# myCA.py
"""
This module will listen for a connection from a client and return a
certificate to the client
"""

import socket
import threading


# main program starts here
host = '127.0.0.1'
port = 23456
socket_timeout = 60

public_key = b'ABC123'

def handle_echo(client_connection, client_address):
    '''
    This function handles reading data sent by client, echoing it back
    and closing the connection in case of a timeout (60 secs) or "quit"
    command
    :param client_connection:
    :param client_address:
    :return:
    '''
    client_connection.settimeout(socket_timeout)
    try:
        while True:
            data = client_connection.recv(1024)
            # close connection if 'quit' received from client
            if data == b'quit\r\n' or data == b'quit\n':
                print(client_address,'disconnected.')
                client_connection.shutdown(1)
                client_connection.close()
                break
            elif data == public_key:
                client_connection.sendall(b'good')
            elif data:
                # echo back to client
                print('from:', client_address, data)
                if not isinstance(data, bytes):
                    data = bytes(data, 'utf-8')
                client_connection.sendall(data)
    except socket.timeout:
        print(client_address, 'timed out.')
        client_connection.shutdown(1)
        client_connection.close()

def listen(host, port):
    '''
    This function opens a socket and listens on the specified port. When
    a connection is received, it is transferred to another socket so the
    main socket is not blocked and can accept new clients
    :param host:
    :param port:
    :return:
    '''
    # create the main socket
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind((host, port))
    connection.listen(5)

    # Every time a client connects, allow a dedicated socket and a
    # dedicated thread to handle communication with that client without
    # blocking the others. Once the new thread has taken over, wait
    # for the next client.
    while True:
        current_connection, client_address = connection.accept()
        print(client_address, 'connected.')
        handler_thread = threading.Thread(
            target=handle_echo,
            args = (current_connection, client_address)
        )
        # daemon makes sure all threads are killed if the main server
        # process gets killed
        handler_thread.daemon = True
        handler_thread.start()

if __name__ == '__main__':
    try:
        listen(host, port)
    except KeyboardInterrupt:
        print('exiting...')
        pass

