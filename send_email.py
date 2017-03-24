#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import smtplib
from email.mime.text import MIMEText
from email import Utils


class SendEmail:
    def __init__(self, user, password, fromaddr, toaddr):
        self.user = user
        self.password = password
        self.fromaddr = fromaddr
        self.toaddr = toaddr.split(',')
        self.qq_smtp = 'smtp.qq.com'
        self.qq_port = 587
        self.timeout = 10
        self.msg = None
        
    def create_data(self):
        self.msg = MIMEText('this is a test email,please ingored it.')
        self.msg['Subject'] = 'python smtplib'
        self.msg['To'] = ','.join(self.toaddr)
        self.msg['From'] = self.fromaddr
        self.msg['Reply_To'] = self.fromaddr
        self.msg['Message_ID'] = Utils.make_msgid().replace("@", "__Rex@")
        
    
    def send_email(self):
        try:
            socket.setdefaulttimeout(self.timeout)
            server = smtplib.SMTP(self.qq_smtp, self.qq_port)
        
            # Login qq email server
            server.set_debuglevel(1)
            server.starttls()
            server.login(self.user, self.password)
        
            # send email
            for cur_toaddr in self.toaddr:
                server.sendmail(self.fromaddr, cur_toaddr, self.msg.as_string())
            
            server.quit()
            print 'send eamil ok.'
        except Exception,e:
            print 'send email error,reason:%s.' % str(e)
        
def main():
    user = "709817768"
    password = ""
    fromaddr = "709817768@qq.com"
    toaddr = "709817768@qq.com,472959680@qq.com"
    obj_send_eamil = SendEmail(user, password, fromaddr, toaddr)
    obj_send_eamil.create_data()
    obj_send_eamil.send_email()


   
if __name__ == '__main__':
    main()
    