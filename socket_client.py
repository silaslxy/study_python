#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket


def socket_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('192.168.1.103',9001))
    sock.send('this is a request from client.')
    ret = sock.recv(1024)
    print ret
    sock.close()
    
if __name__ == '__main__':
    socket_client()
