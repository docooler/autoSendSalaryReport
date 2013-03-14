#-*- coding: utf-8 -*-
#!/usr/bin/python
#filename: anku_sendmail.py
#author : doCooler

import smtplib
import anku_composemail
import ConfigParser

class Ak_sendMail:
    def __init__(self):
        self.mail_server      = ''
        self.mail_server_port = ''
        self.from_addr        = ''
        self.to_addr          = ''
        self.msg              = ''
        self.msg              = ''
        self.usr_name         = ''
        self.pss_wrd          = ''
        self.subject          = ''
        self.bodyFile         = ''      
        self.parserConfig()
        
    def set_server_info(self, server_addr, from_addr, server_port = 25):
        self.mail_server = server_addr
        self.port        = server_port
        self.from_addr   = from_addr

    def set_usr_info(self, usr_name, pss_wrd):
        self.usr_name = usr_name
        self.pss_wrd  = pss_wrd

    def set_msg_info(self, to_addr, attachment=[]):
        self.to_addr = to_addr
        self.attachment = attachment
        
    def parserConfig(self):
        cf = ConfigParser.ConfigParser()
        cf.read("smtp_config.ini")
        mail_server = cf.get('smtp', 'smtp_server')
        mail_port   = cf.getint('smtp', 'smtp_port')
        mail_from   = cf.get('smtp', 'smtp_from')
        self.set_server_info(mail_server, mail_from, mail_port)
        
        mail_usr = cf.get('user', 'user_name')
        mail_pass = cf.get('user', 'passwd')
        self.set_usr_info(mail_usr, mail_pass)
        
        mail_sub = cf.get('Info', 'mail_subject')
        self.subject = mail_sub
        mail_body = cf.get('Info', 'mail_content')
        self.bodyFile = mail_body


    def send_mail(self):
        mail_content =  anku_composemail.Ak_mailGen()
        mail_content.set_mail_head(self.to_addr,self.from_addr, self.subject)
        mail_content.set_body_file(self.bodyFile)
        mail_content.set_mail_attach(self.attachment)
        mail_content.gen_mail()
        msg = mail_content.get_mail_content()
        #mail_fd = open("send.eml", "w")
        #mail_fd.write(msg)
        
        self.s = smtplib.SMTP(self.mail_server, self.mail_server_port)
        #self.s.set_debuglevel(1)
        self.s.login(self.usr_name, self.pss_wrd)
        self.s.sendmail(self.from_addr, self.to_addr, msg)
        self.s.quit()
    def quit_mail(self):
        print("quit mail send")
    

if __name__ == '__main__':
    attachment = ['salary.xlsx']
    bodyFile = 'sample.txt'
    subject  = 'salary send report text '
    to_addr  = 'laiyuan.yang@ankuinfo.com'
    
    mail =  Ak_sendMail()
    mail.set_msg_info(to_addr, attachment)
    mail.send_mail()
    mail.quit_mail()
    print ('Done')
    
    
    
    
    

            
        

