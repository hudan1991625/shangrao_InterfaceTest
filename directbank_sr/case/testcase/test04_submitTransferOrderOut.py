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

    def submitTransferOrderOut(self,custId,auth,bankCardId):
        url=com +'/submitTransferOrderOut'
        print body
        print id(body)
        OrderOutbody=body.copy()
        print OrderOutbody
        print id(OrderOutbody)
        OrderOutbody['amount']=amount_OUT
        OrderOutbody['type']='OUT'
        OrderOutbody['custId']=custId
        OrderOutbody['auth']=auth
        OrderOutbody['bankCardId'] = bankCardId
        OrderOutbody['androidInstallChannel'] = 'defaultbank'
        print OrderOutbody
        print url
        res=requests.post(url,headers=header,json=OrderOutbody,verify=False)
        print res
        print res.json()
        print type(res.json())
        token=res.json()['resultData']['token']
        nextStep=res.json()['resultData']['nextStep']
        return token,nextStep

    def sub_nextStep(self,token,nextStep,custId,auth,bankCardId):
        url = com + '/submitTransferOrderIn'
        nextbody = body.copy()
        nextbody['amount'] = amount_OUT
        nextbody['type'] = 'OUT'
        nextbody['custId'] = custId
        nextbody['auth'] = auth
        nextbody['bankCardId'] = bankCardId
        nextbody['token']=token
        nextbody['step'] = nextStep
        nextbody['verifyData']=tradePwd
        res=requests.post(url,headers=header,json=nextbody,verify=False)
        print res.json()
        resultCode=res.json()['resultCode']
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
            self.log.info(u"---调用出金设置交易金额接口开始---")
            result_values=self.submitTransferOrderOut(custId=custId,auth=auth,bankCardId=bankCardId)
            token=result_values[0]
            nextStep=result_values[1]
            self.log.info(u"---调用出金设置交易金额接口结束---")
            self.log.info(u"---下一步输入交易密码开始---")
            resultCode=self.sub_nextStep(token=token,nextStep=nextStep,custId=custId,auth=auth,bankCardId=bankCardId)
            self.assertEqual(resultCode, 0, msg=u'啊哦，出金失败了!!!')
            self.log.info(u"---出金成功返回结果---")
        except AttributeError as msg:
            print u"尝试未知对象属性错误:"+str(msg)

if __name__=='__main__':
    unittest.main
