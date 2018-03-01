# coding:utf-8
import unittest
import requests
from login import Login
from common.para import *
from common.modifypara import *

class TradePwd(Login):

    def tradepwd_entrance(self,custId,auth):
        url=com + '/preCommonVerify'
        Inputbody=body.copy()
        Inputbody['funName']='TRADEPWD'
        Inputbody['funType'] = 'MODIFY'
        Inputbody['custId']=custId
        Inputbody['auth'] = auth
        print Inputbody
        res=requests.post(url,headers=header,json=Inputbody,verify=False)
        print res
        print type(res.json())
        print res.json()
        verifyStepList=res.json()['resultData']['verifyStepList']
        print type(verifyStepList)
        print '--------------------------------'
        for i ,dic in enumerate(verifyStepList):
            if dic['canBack']==True:
                print verifyStepList.pop(i)
            else:
                pass
        return dic      #返回nextStep,token


    def InputLoginPwd(self,token,custId,auth,step):
        url = com + '/commonVerify'
        Inputbody = body.copy()
        Inputbody['funName'] = 'TRADEPWD'
        Inputbody['funType'] = 'MODIFY'
        Inputbody['custId'] = custId
        Inputbody['auth'] = auth
        Inputbody['token']=token
        Inputbody['step'] = step
        Inputbody['loginPwd'] = loginPwd
        print Inputbody
        res = requests.post(url, headers=header, json=Inputbody, verify=False)
        print res
        print res.json()
        verifyStepList = res.json()['resultData']['verifyStepList']
        self.log.info("verifyStepList的结果是%s" %verifyStepList)
        print type(verifyStepList)
        for i ,dic in enumerate(verifyStepList):
            if dic['canBack']==True:
                print verifyStepList.pop(i)
            else:
                pass
        return dic  #返回step,token,resultCode


    def InputVerifyBankCardInfo(self,token,custId,auth,step):
        url = com + '/commonVerify'
        Inputbody = body.copy()
        Inputbody['custId'] = custId
        Inputbody['auth'] = auth
        Inputbody['token'] = token
        Inputbody['funName'] = 'TRADEPWD'
        Inputbody['funType'] = 'MODIFY'
        Inputbody['bankCardMobile'] = bankCardMobile
        Inputbody['bankCardNum'] = bankCardNum
        Inputbody['bankCardType'] = bankCardType
        Inputbody['certNo'] = certNo
        Inputbody['certType'] = certType
        Inputbody['step'] = step
        Inputbody['androidInstallChannel'] = 'defaultbank'
        print Inputbody
        res = requests.post(url, headers=header, json=Inputbody, verify=False)
        print res
        print res.json()
        verifyStepList = res.json()['resultData']['verifyStepList']
        for i, dic in enumerate(verifyStepList):
            if dic['canBack'] == True:
                print verifyStepList.pop(i)
            else:
                pass
        return dic  # 返回step,token,resultCode


    def InputSMS(self,custId,auth,token,step):
        url = com + '/commonVerify'
        Inputbody = body.copy()
        Inputbody['custId'] = custId
        Inputbody['auth'] = auth
        Inputbody['token'] = token
        Inputbody['smsCode'] = smsCode
        Inputbody['funName'] = 'TRADEPWD'
        Inputbody['funType'] = 'MODIFY'
        Inputbody['step'] = step
        Inputbody['androidInstallChannel'] = 'defaultbank'
        print Inputbody
        res = requests.post(url, headers=header, json=Inputbody, verify=False)
        print res
        print res.json()
        verifyStepList = res.json()['resultData']['verifyStepList']
        for i, dic in enumerate(verifyStepList):
            if dic['canBack'] == True:
                print verifyStepList.pop(i)
            else:
                pass
        return dic # 返回step,token

    def modifyTradePwd(self,custId,auth,token):
        url = com + '/modifyTradePwd'
        Inputbody = body.copy()
        Inputbody['custId'] = custId
        Inputbody['auth'] = auth
        Inputbody['token'] = token
        Inputbody['newTradePwd'] = newTradePwd
        Inputbody['androidInstallChannel'] = 'defaultbank'
        print Inputbody
        res = requests.post(url, headers=header, json=Inputbody, verify=False)
        print res
        print res.json()
        resultCode = res.json()['resultCode']
        return resultCode  # 返回resultCode

    def test07_tradePwd(self):
        try:
            self.log.info(u"-------调用登录方法开始------")
            reslult_data=self.doLogin()
            custId=reslult_data[0]
            auth=reslult_data[1]
            resultCode=reslult_data[2]
            self.assertEqual(resultCode, 0,msg=u'登录失败了')
            self.log.info(u"-------通用验证,调用修改交易密码接口开始------")
            dict=self.tradepwd_entrance(custId,auth)
            print dict
            token=dict['token']
            step=dict['nextStep']
            self.log.info(u"-------通用验证输入登录密码------")
            dict1=self.InputLoginPwd(token,custId,auth,step)
            token=dict1['token']
            step = dict1['nextStep']
            self.log.info(u"-------通用验证四要素鉴权------")
            dict2=self.InputVerifyBankCardInfo(token,custId,auth,step)
            # self.assertEqual(resultCode, 0, msg='四要素鉴权失败')
            token = dict2['token']
            step = dict2['nextStep']
            self.log.info(u"-------通用验证,输入短信验证码------")
            dict3=self.InputSMS(custId,auth,token,step)
            token1 = dict3['token']
            self.log.info(u"-------通用验证,设置交易密码------")
            resultCode=self.modifyTradePwd(custId, auth, token1)
            self.assertEqual(resultCode, 0, msg=u'交易密码设置失败')
        except Exception as message:
            print u"测试失败了:" + str(message)

if __name__ == '__main__':
    unittest.main()
