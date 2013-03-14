1.安酷工资表.xls是工资模板，可以增加相应的同事到后面。但是现在不能
  增加相应的列，因为现在的邮件地址是固定到一个地方的。如果邮件地址的
  列被更改就不能发送程序。
 
2.smtp_config.ini是相应的配置文件。
  #配置邮箱smtp地址，目前版本不支持ssl发送邮件
  [smtp]
  smtp_server = smtp.ym.163.com
  smtp_port   = 25
  smtp_from   = test@163.com
  
  #配置smtp登陆信息，用户名和密码
  [user]
  user_name = test@163.com
  passwd    = 123456
  
  #定制邮件内容，sample.txt里面是发送邮件的正文，可以更改这个文件的内容来更改相应邮件内容
  #mail_subject 是发送邮件的主题。目前不支持中文格式只能用英文。
  [Info]
  mail_content = sample.txt
  mail_subject = salary detail message 

 
3.如果有什么问题请联系yi01625@163.com
