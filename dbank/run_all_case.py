#coding:utf-8
import unittest
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import os
import time

def send_mail(file_new):
    f=open(file_new,'rb')
    mail_body=f.read()
    f.close()
    msg=MIMEText(mail_body,'html','utf-8')
    msg['Subject']=Header("APP自动化测试报告",'utf-8')
    smtp=smtplib.SMTP()
    smtp.connect("smtp.yeah.net")
    #发件人地址
    smtp.login("luckhudan@yeah.net","1991625")
    #收件人地址
    smtp.sendmail("luckhudan@yeah.net","1443758765@qq.com",msg.as_string())
    smtp.quit()
    print ("email has sent out")

def new_report(testreport):
    lists=os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getmtime(testreport+"\\"+fn))
    file_new=os.path.join(testreport,lists[-1])
    print (file_new)
    return file_new

def all_case():
    #待执行测试用例目录
    test_dir="E:\\dbank\\testcase"
    testcase=unittest.TestSuite()
    #使用discover方法，三个参数，分别是用例的目录，匹配运行的用例，顶层目录名称
    discover=unittest.defaultTestLoader.discover(test_dir,pattern="test_*.py",top_level_dir=None)

    #discover方法筛选的用例，循环添加至测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testcase.addTests(test_case)
    print testcase
    return testcase


if __name__=="__main__":
     #返回实例
     now = time.strftime("%Y-%m-%d %H_%M_%S")
     filename = 'E:\\dbank\\report\\' + now + '_result.html'
     #打开html文件，若没有则自动创建
     fp=open(filename,"wb")
     runner=HTMLTestRunner(stream=fp,title=u'工银小白银行测试报告',description=u'用例执行情况：')
     #运行所有实例
     runner.run(all_case())
     fp.close()

     # 发送测试报告
     test_report='E:\\dbank\\report'
     new_report = new_report(test_report)
     send_mail(new_report)