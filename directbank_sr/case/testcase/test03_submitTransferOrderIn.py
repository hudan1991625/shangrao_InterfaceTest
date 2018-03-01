# coding:utf-8
import unittest
import requests
from common.para import *
from common.logger import Log
from login import Login

class SubTransferOrderIN(Login):
    log=Log()

    def queryTransferCard(self,custId,auth):
        url = com + '/queryTransferCard'
        qbody=body.copy()
        qbody['custId'] = custId
        qbody['auth'] = auth
        print qbody
        res=requests.post(url,headers=header,json=qbody,verify=False)
        print res.json()
        inBankCardId=res.json()['resultData']['inBankCardId']
        outBankCardId = res.json()['resultData']['outBankCardId']
        resultCode=res.json()['resultCode']
        return (inBankCardId,outBankCardId,resultCode)

    def subTransferOrderIN(self,custId,auth,bankCardId):
        url=com +'/submitTransferOrderIn'
        print body
        print id(body)
        subbody=body.copy()
        print subbody
        print id(subbody)
        subbody['amount']=amount_IN
        subbody['type']='IN'
        subbody['custId']=custId
        subbody['auth']=auth
        subbody['bankCardId'] = bankCardId
        print subbody
        print url
        res=requests.post(url,headers=header,json=subbody,verify=False)
        print res
        print res.json()
        print type(res.json())
        token=res.json()['resultData']['token']
        nextStep=res.json()['resultData']['nextStep']
        return token,nextStep

    def sub_nextStep(self,token,nextStep,custId,auth,bankCardId):
        url = com + '/submitTransferOrderIn'
        nextbody = body.copy()
        nextbody['amount'] = amount_IN
        nextbody['type'] = 'IN'
        nextbody['custId'] = custId
        nextbody['auth'] = auth
        nextbody['bankCardId'] = bankCardId
        nextbody['token']=token
        nextbody['step'] = nextStep
        nextbody['verifyData']=tradePwd
        print nextbody
        res=requests.post(url,headers=header,json=nextbody,verify=False)
        print res
        print res.json()
        resultCode = res.json()['resultCode']
        return resultCode

    def test_subTransferOrderIN(self):
        try:
            result=self.doLogin()
            print result
            custId = result[0]
            auth = result[1]
            self.log.info(u"-----调用资金划拨卡片查询接口开始-----")
            data=self.queryTransferCard(custId=custId,auth=auth)
            bankCardId=data[0]
            resultCode=data[2]
            self.assertEqual(resultCode,0,msg=u'测试失败了') #加断言，判断返回结果是否成功
            self.log.info(u"-----调用资金划拨卡片查询接口结束，获取绑卡id----")
            self.log.info(u"---调用入金设置交易金额接口开始---")
            result_values=self.subTransferOrderIN(custId=custId,auth=auth,bankCardId=bankCardId)
            token=result_values[0]
            nextStep=result_values[1]
            self.log.info(u"---调用入金设置交易金额接口结束---")
            self.log.info(u"---下一步输入交易密码开始---")
            resultCode=self.sub_nextStep(token=token,nextStep=nextStep,custId=custId,auth=auth,bankCardId=bankCardId)
            self.assertEqual(resultCode,0,msg=u'啊哦，入金失败了!!!')
            self.log.info(u"---入金成功返回结果---")
        except AttributeError as msg:
            print u"尝试未知对象属性错误:"+str(msg)

if __name__=='__main__':
    unittest.main
