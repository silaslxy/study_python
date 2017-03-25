#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2
import httplib


# post方法,请求数据放在data或者body中，不能放在url中
def urllib_post_client():
    list_data = []
    list_data.append('this is http client.')
    http_body = '\r\n'.join(list_data)
    str_url = 'http://192.168.1.103:9002'
    request = urllib2.Request(str_url, data=http_body)
    request.add_header('user_agent', 'Mozilla/5.0')
    req = urllib2.urlopen(request)
    print req.read()


def http_post_client():
    test_data = {'ServiceCode': 'aaaa', 'b': 'bbbbb'}
    test_data = urllib.urlencode(test_data)
    str_url = 'http://192.168.1.103:9002'
    header = {"Host": "192.168.1.103:9002"}
    conn = httplib.HTTPConnection("192.168.1.103", 9002)
    conn.request(method="POST", url=str_url, body=test_data, headers=header)
    response = conn.getresponse()
    print response.read()
    conn.close()
    

# get方法,请求数据直接放在url中
def http_get_client():
    str_url = 'http://192.168.1.103:9002?data=aaaa'
    conn = httplib.HTTPConnection("192.168.1.103", 9002)
    conn.request(method="GET", url=str_url)
    response = conn.getresponse()
    res = response.read()
    print res
    
    
def urllib_get_client():
    str_url = 'http://192.168.1.103:9002?data=aaaa'
    req = urllib2.Request(str_url)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res
    

if __name__ == '__main__':
    http_post_client()
