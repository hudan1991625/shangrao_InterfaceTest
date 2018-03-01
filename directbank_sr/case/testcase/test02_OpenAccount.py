# coding:utf-8
import unittest
import requests
from common.para import *
from common.logger import Log
class OpenAccount(unittest.TestCase):
    log=Log()
    #未开户用户登录
    def login(self):
        url= com + '/login'
        loginBody=body.copy()
        loginBody['value']=value
        loginBody['loginPwd']=loginPwd
        loginBody['forceLogin']='true'
        print loginBody
        r2=requests.post(url,headers=header,json=loginBody,verify=False)
        print r2.json()
        print type(r2.json())   #dict
        custId=r2.json()[u'resultData'][u'custId']
        auth=r2.json()[u'resultData'][u'auth']
        return custId,auth

    #开户过程中的身份验证
    def openAccountVerifyCertInfo(self,custId,auth):
        url3= com+'/openAccountVerifyCertInfo'
        openbody=body.copy()
        print openbody
        openbody['auth']=auth
        openbody['custId'] = custId
        openbody['certName'] = certName
        openbody['certNo'] = certNo
        openbody['frontURL'] = 'TYPE_IDCARD382485515362250752'
        openbody['backURL'] = 'TYPE_IDCARD382485557485645824'
        openbody['checkState'] = 'true'
        openbody['validDateBegin'] = '20170626'
        openbody['validDateEnd'] = '20200626'
        openbody['address'] = '陕西省商洛市商南县'
        print openbody
        r3 = requests.post(url3, headers=header, json=openbody, verify=False)
        print r3.json()
        print type(r3.json())
        print r3.json()[u'resultData'][u'token']
        return r3.json()[u'resultData'][u'token']

    def verifyCardSupportBiz(self,custId,auth):
        url4 = com + '/verifyCardSupportBiz'
        verifybody=body.copy()
        verifybody['custId'] = custId
        verifybody['bankCardNum'] = bankCardNum
        verifybody['auth'] = auth
        verifybody['bizCode'] = 'OPENACCOUNT'
        r4 = requests.post(url4, headers=header, json=verifybody, verify=False)
        print r4.json()
        print type(r4.json())
        bankCardType = r4.json()[u'resultData'][u'bankCardInfo'][u'bankCardType']
        bankCode = r4.json()[u'resultData'][u'bankCardInfo'][u'bankInfo'][u'bankCode']
        print bankCardType, bankCode
        return (bankCardType, bankCode)

    def bindCardSendSms(self,custId,token,auth,bankCardType,bankCode):
        url5 = com + '/bindCardSendSms'
        bindbody=body.copy()
        bindbody['auth'] = auth
        bindbody['bankCardMobile'] = value
        bindbody['custId'] = custId
        bindbody['certName'] = certName
        bindbody['bankCardNum'] = bankCardNum
        bindbody['certNo'] = certNo
        bindbody['token'] = token
        bindbody['cardType'] = bankCardType
        bindbody['bankCode'] = bankCode
        r5 = requests.post(url5, headers=header, json=bindbody, verify=False)
        print r5.json()
        print type(r5.json())
        extStr = r5.json()[u'resultData'][u'extStr']
        print extStr
        return extStr

    def bindCardVerifySms(self,custId,auth,bankCardType,bankCode):
        url6=com +'/bindCardVerifySms'
        bindCardbody=body.copy()
        bindCardbody['certName']=certName
        bindCardbody['custId'] = custId
        bindCardbody['auth'] = auth
        bindCardbody['bankCardNum'] = bankCardNum
        bindCardbody['certNo'] = certNo
        bindCardbody['bankCardMobile'] = value
        bindCardbody['cardType'] = bankCardType
        bindCardbody['smsCode'] = smsCode
        bindCardbody['bankCode'] = bankCode
        r6=requests.post(url6,headers=header,json=bindCardbody,verify=False)
        print r6.json()
        print type(r6.json())
        print r6.json()['resultData']['token']
        return r6.json()['resultData']['token']

    def createAccount(self,custId,auth,token,bankCardType):
        url7 = com + '/createAccount'
        creatbody=body.copy()
        creatbody['certName']=certName
        creatbody['custId'] = custId
        creatbody['auth'] = auth
        creatbody['bankCardNum'] = bankCardNum
        creatbody['certNo'] = certNo
        creatbody['bankCardMobile'] = value
        creatbody['cardType'] = bankCardType
        creatbody['token'] = token
        creatbody['tradePwd'] = tradePwd
        creatbody['idfa'] = '95a530774abe457daac6b8b2c67550a7'
        creatbody['idfv'] = '152ee8a97961473ea8dc0412ca95604f'
        r7=requests.post(url7,headers=header,json=creatbody,verify=False)
        print r7
        print r7.json()
        print type(r7.json())
        return r7.json()['resultData']['secAccountNo']

    #测试开户过程中的身份验证,若加上此步骤，会出现两次登录，获取的auth值不一致，引起后面报错
    # def test02_openAccountVerifyCertInfo(self):
    #     self.log.info(u"开户第一步,上传身份证正反面")
    #     data = self.login()
    #     self.log.info(u"从登录结果中取出登录态,打印auth是%s" % data)
    #     self.openAccountVerifyCertInfo(Auth=data)

    #测试判断银行卡号是否支持指定业务接口
    def test02_OpenAccount(self):
        self.log.info(u"---调用登录获取auth开始---")
        result_data= self.login()
        custId=result_data[0]
        auth=result_data[1]
        self.log.info(u"---登录成功---")
        self.log.info(u"---调用开户身份验证接口开始，获取token---")
        result_token=self.openAccountVerifyCertInfo(custId=custId,auth=auth)
        self.log.info(u"---开户身份验证接口返回成功---")
        self.log.info(u"---调用判断银行卡号是否支持指定业务接口开始---")
        result=self.verifyCardSupportBiz(custId=custId,auth=auth)
        self.log.info(u"打印银行卡类型和银行编码%s %s:" %result) #输出两个值
        self.log.info(u"---调用判断银行卡号是否支持指定业务接口通过---")
        token=result_token
        bankCardType=result[0]
        bankCode=result[1]
        self.log.info(u"---调用绑卡发短信接口开始---")
        self.bindCardSendSms(custId,token,auth,bankCardType,bankCode)
        self.log.info(u"----绑卡发短信接口通过---")
        self.log.info(u"---调用绑卡验证短信接口开始---")
        bind_token=self.bindCardVerifySms(custId,auth,bankCardType,bankCode)
        self.log.info(u"---绑卡验证短信接口通过---")
        self.log.info(u"---调用开户接口开始-----")
        token=bind_token
        self.createAccount(custId,auth,token,bankCardType)

if __name__ == "__main__":
    unittest.main()


