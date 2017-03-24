#!/usr/bin/env python
# -*- coding:utf-8 -*-

import SocketServer
import BaseHTTPServer


class ThreadingServer(SocketServer.ThreadingMixIn, BaseHTTPServer.HTTPServer):
    pass


class PostHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def Send_Resp200(self):
        self.send_response(200)
        self.send_header('Error_Code','0')
        self.end_headers()
        
    def do_POST(self):
        recv_value = self.rfile.read(int(self.headers['Content-Length']))
        print recv_value
        #self.send_response(200)
        self.wfile.write('now http server is ok.')
        self.send_response(200)
        
server = ThreadingServer(('192.168.1.103',9002), PostHandler)

try:
    print 'http server is running.'
    server.serve_forever()
except:
    server.socket.close()
    print 'http server is stop.'