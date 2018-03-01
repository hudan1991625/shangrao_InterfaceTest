# coding:utf-8
import unittest
import requests
from common.para import *
from common.logger import Log

class Login(unittest.TestCase):
    log=Log()
    def login(self):
        url= com + '/login'
        loginBody=body.copy()
        loginBody['value']=value
        loginBody['loginPwd']='111111'
        loginBody['forceLogin']='true'
        print loginBody
        r2=requests.post(url,headers=header,json=loginBody,verify=False)
        print r2.json()
        print type(r2.json())   #dict
        custId=r2.json()[u'resultData'][u'custId']
        auth=r2.json()[u'resultData'][u'auth']
        resultCode=r2.json()['resultCode']
        return custId,auth,resultCode


    def doLogin(self):
        try:
            self.log.info(u"----------开始登录---------")
            # res =self.login()
            # self.log.info("------登录成功!--------")
            # print res
            print '-------------'
            return self.login()
        except TypeError as msg:
            print u"出错啦！"+str(msg)

if __name__=='__main__':
    unittest.main