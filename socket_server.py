#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket


def socket_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('192.168.1.103',9001))
    sock.listen(1)
    
    while True:
        connection, address = sock.accept()
        
        try:
            connection.settimeout(5)
            ret = connection.recv(1024)
            print ret
            
            connection.send('server has recieved client data.')
        except socket.timeout:
            pass
        connection.close()
        
if __name__ == '__main__':
    socket_server()
