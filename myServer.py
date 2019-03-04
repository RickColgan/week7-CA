# myServer.py
"""
This module will listen for a connection from a client and return a
certificate to the client
"""

import socket
import threading

def decrypt_message(msg):
    """
    Encrypts a message for this assignment
    :param msg: string
    :return: encrypted message string
    """
    decode_dict = {
         1: 'A',
         2: 'B',
         3: 'C',
         4: 'D',
         5: 'E',
         6: 'F',
         7: 'G',
         8 : 'H',
         9: 'I',
         10: 'J',
         11: 'K',
         12: 'L',
         13: 'M',
         14: 'N',
         15: 'O',
         16: 'P',
         17: 'Q',
         18: 'R',
         19: 'S',
         20: 'T',
         21: 'U',
         22: 'V',
         23: 'W',
         24: 'X',
         25: 'Y',
         26: 'Z',
         27: ' ',
    }
    arr = []
    newmsg = msg.split(' ')
    for val in newmsg:
        if int(val) in decode_dict:
            arr.append(decode_dict[int(val)])
        else:
            arr.append(val)
    data = ''.join(arr)
    return bytes(data, 'utf-8')



# main program starts here

host = '127.0.0.1'
port = 65432
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
            elif data == b'good cert':
                # echo back to client
                print('from:', client_address, data)
                decrypt_message(data)
                if not isinstance(data, bytes):
                    data = bytes(data, 'utf-8')
                client_connection.sendall(data)
            else:
                pass

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

