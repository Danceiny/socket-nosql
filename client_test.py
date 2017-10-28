#!/usr/bin/python 
# -*- coding: utf-8 -*-

import socket
import time 

HOST = 'localhost'
PORT = 50505
SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def main():
    SOCKET.connect((HOST, PORT))
    data = "PUT;foo;1;INT"
    data2 = "GET;foo;;"
    #SOCKET.sendall(bytearray(data, 'utf-8'))
    #response = SOCKET.recv(4096).decode()
    #print response
    SOCKET.sendall(bytearray(data2, 'utf-8'))
    response = SOCKET.recv(4096).decode()
    print response

if __name__ == '__main__':
    main()
