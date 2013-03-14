#-*- coding: utf-8 -*-
#!/usr/bin/python
#filename : anku+_parserxlsx.py
#auther :doCooler


from win32com.client import constants,Dispatch
import os , sys
import codecs
import shutil


class rw_excel:
    def __init__(self):
        self.readfile = 'salary.xlsx'
        self.writefile = 'write.xlsx'
        self.templefile = 'temple.xlsx'
        self.mailCol    = 33
        self.rows = 0
        self.open_excel()
        self.gen_rows()
        
        
    def __del__(self):
        self.readXlsBook.Close(SaveChanges=0)
        self.readXlsApp.Quit()
        
    def open_excel(self):
        f =  os.getcwd() + "\\" + "工资表" + '.xls'
        f_open = (f)
        self.readXlsApp = Dispatch("Excel.Application")
        self.readXlsApp.Visible = False
        self.readXlsBook = self.readXlsApp.Workbooks.Open(f_open)
        sheet_name = '工资表模板'
        #print (sheet_name)
        self.readSht = self.readXlsBook.Worksheets(sheet_name)
        
        
    def gen_excel(self, rows):
        f =  os.getcwd() + "\\" + "tmp" + repr(rows) +'.xls'
        if os.path.exists(f):
            os.remove(f)
        shutil.copy("send.xls", f)
        
        rows += 5
        f_open = (f)
        xlsApp = Dispatch("Excel.Application")
        xlsApp.Visible = False
        xlsBook = xlsApp.Workbooks.Open(f_open)
        sheet_name = '工资表模板'
        #print (sheet_name)
        writeSht = xlsBook.Worksheets(sheet_name)
        
        to_addr = self.readSht.Cells(rows, self.mailCol).Value
        print(to_addr)
        
        for j in range(1,40):
            if j == self.mailCol:
                continue
            writeSht.Cells(6,j).Value = self.readSht.Cells(rows, j).Value
            #print (writeSht.Cells(6,j).Value)
        xlsBook.Close(SaveChanges=1)
        #xlsApp.Quit()
        return to_addr
        
    def del_excel(self, rows):
        f =  os.getcwd() + "\\" + "tmp" + repr(rows) +'.xls'
        if os.path.exists(f):
            os.remove(f)
            
        
    def gen_rows(self):
        i = 6
        self.rows = 0
        while True:
            if self.readSht.Cells(i, 2).Value == None:
                return self.rows

            #print(self.readSht.Cells(i, 2).Value)
            i += 1
            self.rows +=1
            #print(repr(self.rows))
            
    def get_rows(self):
        return self.rows
    
    def check_excel(self):
        rows = self.rows + 6
        #print(repr(rows))
        for i in range(6, rows):
            if self.readSht.Cells(i, self.mailCol).Value == None:
                name = self.readSht.Cells(i, 2).Value
                print("Error: 第" + repr(i) + "行" + name + "没有填写邮件信息请填写后再试" )
                return 1
            #print(self.readSht.Cells(i, self.mailCol).Value)
        return 0
    
        
        
      
        
    

if __name__ == '__main__':
    xls = rw_excel()
    #xls.open_excel()
    rows = xls.get_rows()
    print(repr(rows))
    ret = xls.check_excel()
    print(repr(ret))
    for i in range(1, rows):
        xls.gen_excel(i)
    #xls.del_excel(1)
