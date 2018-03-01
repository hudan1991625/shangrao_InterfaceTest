# coding:utf-8
import unittest
import requests
from common.logger import Log
from common.para import *

class register(unittest.TestCase):
    log = Log()
    def register(self):
        url = com + "/registSendSms"
        rbody=body.copy() #利用copy方法，新建一块内存存放body
        rbody['mobile']=value
        r = requests.post(url, json=rbody, headers=header, verify=False)
        print r.json()
        print type(r.json())
        return r.json()

    def smsCode(self):
        url1 = com + "/registVerifySms"
        print url1
        smsbody=body.copy()
        smsbody['mobile']=value
        smsbody['smsCode'] = smsCode
        r1=requests.post(url1, json=smsbody, headers=header,verify=False)
        self.log.info(u"打印r1.json的值：%s" %r1.json())
        print type(r1.json())
        return r1.json()[u"resultData"][u"token"]  #返回token的值

    def registSetPwd(self,result_token):
        url2 = com + "/registSetPwd"
        print url2,header
        regbody=body.copy()
        regbody['mobile'] = value
        regbody['loginPwd'] = loginPwd
        regbody['token']=result_token
        # smsCode方法中在body中加入了smsCode,传入body前先将其移除,否则报错
        print regbody
        r2=requests.post(url2, json=regbody, headers=header,verify=False)
        print r2
        print r2.json()
        print type(r2.json())
        custId = r2.json()[u'resultData'][u'custId']
        auth = r2.json()[u'resultData'][u'auth']
        return (custId,auth)

    def test01_register(self):
        self.log.info(u"---注册输入手机号，发送短信验证码开始---")
        self.register()
        self.log.info(u"---注册输入手机号成功，发送短信验证码成功---")
        self.log.info(u"---验证短信验证码开始---")
        token = self.smsCode()
        self.log.info(u"短信验证码验证成功，打印token的值：%s" %token)  # 返回的data是token值
        self.log.info(u"---设置登录密码开始---")
        self.registSetPwd(result_token=token)
        self.log.info(u"设置登录密码成功，注册完成---")

if __name__ == "__main__":
    unittest.main()