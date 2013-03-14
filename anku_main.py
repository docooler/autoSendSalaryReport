#-*- coding: utf-8 -*-
#!/usr/bin/python
#filename : anku_main.py
#author   : doCooler

import os
import anku_sendmail
import ConfigParser
import anku_parserxlsx

class sendSalaryText:
    def __init___(self):
        self.mail_session =  ''

    def sendReport(self,to_addr, attachment = []):
        #print("debug sendReport")
        self.mail_session.set_msg_info(to_addr, attachment)
        self.mail_session.send_mail()
        print('send mail to ' + to_addr + ' Done')

    def sendAll(self):
        self.mail_session =  anku_sendmail.Ak_sendMail()
        xls = anku_parserxlsx.rw_excel()
        #检测
        ret = xls.check_excel()
        if ret == 1:
            return 1
        print("check excel ok!")
            
        rows = xls.get_rows()
        rows += 1
        for i in range(1, rows):
            to_addr = xls.gen_excel(i)
            print ("send mail to " + to_addr)
            strattach = 'tmp' + repr(i) + '.xls'
            print (strattach)
            attachname = [strattach]
            #print (attachname)
            
            self.sendReport(to_addr,attachname)
            xls.del_excel(i)
            
        #self.mail_session.quit_mail()
        return 0
        
    

if __name__ == "__main__":
    session = sendSalaryText()
    ret = session.sendAll()
    if ret == 0:
        print ("Send Sucess!")
    else:
        print ("Send Failed!")
            
