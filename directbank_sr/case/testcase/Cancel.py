# coding:utf-8
import unittest
import requests
from login import Login
from common.para import *

class Cancel(Login):

    def cancel_entrance(self,custId,auth):
        url=com + '/preCommonVerify'
        Inputbody=body.copy()
        Inputbody['funName']='ACCOUNT'
        Inputbody['funType'] = 'CANCELLOST'
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
        return dic

    #活体需要传入faceData,目前无具体数据,从SDK获取的
    def InputFace(self,token,custId,auth,step):
        url = com + '/commonVerify'
        Inputbody = body.copy()
        Inputbody['funName'] = 'ACCOUNT'
        Inputbody['funType'] = 'CANCELLOST'
        Inputbody['custId'] = custId
        Inputbody['auth'] = auth
        Inputbody['token']=token
        Inputbody['step'] = step
        # Inputbody['faceData'] = faceData
        # Inputbody['faceSDKName'] =faceSDKName
        # Inputbody['faceSDKVersion'] = faceSDKVersion
        print Inputbody
        res = requests.post(url, headers=header, json=Inputbody, verify=False)
        print res
        print res.json()
        resultCode=res.json()['resultCode']
        return resultCode

    def InputVerifyBankCardInfo(self,custId,auth,token,step):
        url = com + '/commonVerify'
        Verifybody=body.copy()
        Verifybody['funName'] = 'ACCOUNT'
        Verifybody['funType'] = 'CANCELLOST'
        Verifybody['custId'] = custId
        Verifybody['auth'] = auth
        Verifybody['token'] = token
        Verifybody['step'] = step
        Verifybody['bankCardMobile'] = bankCardMobile
        Verifybody['bankCardNum'] = bankCardNum
        Verifybody['bankCardType'] = bankCardType
        Verifybody['certNo'] = certNo
        Verifybody['certType'] = certType
        print Verifybody
        res = requests.post(url, headers=header, json=Verifybody, verify=False)
        print res
        print res.json()


    def accountLostAndCancel(self,token,custId,auth):
        url = com + '/accountLostAndCancel'
        finishbody = body.copy()
        finishbody['custId'] = custId
        finishbody['auth'] = auth
        finishbody['token'] = token
        finishbody['type'] = 'TYPE_CANCEL_LOST'
        finishbody['androidInstallChannel'] = 'defaultbank'
        print finishbody
        res = requests.post(url, headers=header, json=finishbody, verify=False)
        print res
        print res.json()
        resultCode=res.json()['resultCode']
        return  resultCode


    def test05_cancel(self):
        try:
            self.log.info("-------调用登录方法开始------")
            reslult_data=self.doLogin()
            custId=reslult_data[0]
            auth=reslult_data[1]
            resultCode=reslult_data[2]
            self.assertEqual(resultCode, 0,msg='登录失败了')
            self.log.info("-------调用挂失接口开始------")
            dict=self.entrance(custId,auth)
            print dict
            token=dict['token']
            step=dict['nextStep']
            self.log.info("-------调用挂失身份验证接口开始------")
            dict1=self.InputCertNo(token=token,custId=custId,auth=auth,step=step)
            self.assertEqual(resultCode, 0, msg='身份验证失败了')
            token=dict1['token']
            self.accountLostAndCancel(token,custId,auth)
            self.assertEqual(resultCode, 0, msg='身份验证失败了')
        except Exception as message:
            print "测试失败了:" + str(message)

if __name__ == '__main__':
    unittest.main()