# myClient.py
"""
This is the file that will start the client for Week 7's assignment.
"""

import socket
import sys
import threading
import time

from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import Salsa20
from Crypto.Hash import SHA256


host = '127.0.0.1'
port = 65432
CA_port = 23456

def get_cert_from_server(data):
    '''
    This function should get a certificate from the server with a public
    key
    :param data is a str field to be sent and gets converted to bytes
    :return: received data
    '''
    data = bytes(data, 'utf-8')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(data)
        print('get cert sent', data)
        data = s.recv(1024)
        print('get cert recvd', data)

    print()
    print('Received', repr(data))
    return data


def encrypt_message(msg):
    """
    Encrypts a message for this assignment
    :param msg: string
    :return: encrypted message string
    """
    codedict = {
        'a': '1',
        'b': '2',
        'c': '3',
        'd': '4',
        'e': '5',
        'f': '6',
        'g': '7',
        'h': '8',
        'i': '9',
        'j': '10',
        'k': '11',
        'l': '12',
        'm': '13',
        'n': '14',
        'o': '15',
        'p': '16',
        'q': '17',
        'r': '18',
        's': '19',
        't': '20',
        'u': '21',
        'v': '22',
        'w': '23',
        'x': '24',
        'y': '25',
        'z': '26',
        ' ': '27',
    }
    arr = []
    for char in list(msg):
        if char.lower() in codedict:
            arr.append(codedict[char.lower()])
        else:
            arr.append(char)
    return ' '.join(arr)


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
    return ''.join(arr)


def verify_cert_with_CA(data):
    if not isinstance(data, bytes):
        data = bytes(data, 'utf-8')
    print(data)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, CA_port))
        print('verifying cert and sending data', data)
        s.sendall(data)
        data = s.recv(1024)

    print()
    print('Received', repr(data))
    return data


def send_message_to_server(data):
    '''
    This function should send an encrypted message to the server
    :param data is a str field to be sent and gets converted to bytes
    :return: received data
    '''
    data = bytes(data, 'utf-8')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(data)
        data = s.recv(1024)

    print()
    print('sending message:', data)
    print('Received', repr(data))
    return data

certinfo = get_cert_from_server('send cert')
print('got certinfo and going to verify...')
goodcert = verify_cert_with_CA(certinfo)
print('goodcert =', goodcert)
if goodcert == b'good':
    encrypted_msg = encrypt_message('this is a message')
    good_msg = bytes(encrypted_msg, 'utf-8')
    print('sending message to server...')
    send_message_to_server(good_msg)
else:
    print('bad data. aborting...')

