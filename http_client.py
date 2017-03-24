#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import httplib


def http_client():
    lst_data = []
    lst_data.append('this is http client.')
    http_body = '\r\n'.join(lst_data)
    str_url = 'http://192.168.1.103:9002'
    request = urllib2.Request(str_url, data=http_body)
    request.add_header('user_agent', 'Mozilla/5.0')
    req = urllib2.urlopen(request)
    print req.read()
    
if __name__ == '__main__':
    http_client()
    