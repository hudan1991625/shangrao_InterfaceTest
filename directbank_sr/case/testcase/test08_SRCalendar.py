# coding:utf-8
import unittest
import requests
from login import Login
from common.para import *
# from common.modifypara import *

class scheduleInfoAdd(Login):
    # inputbody={}

    # 定期转入设置列表查询
    def scheduleInfoList(self, custId, auth):
        url = com + '/SRCalendar/scheduleInfoList'
        Listbody = {
            "custId": custId,
            "auth": auth
        }
        res = requests.post(url, headers=header, json=Listbody, verify=False)
        print res
        print res.json()
        print '------------------------------'
        # dict=resultdata[0]
        # id_value=dict['id']
        return  res.json()['resultData']

    #定时任务添加接口
    def scheduleInfoAdd(self,custId,auth):
        url=com + '/SRCalendar/scheduleInfoAdd'
        # scheduleInfoAdd.inputbody['custId']=custId
        # scheduleInfoAdd.inputbody['auth'] = auth
        Addbody={
            "custId": custId,
            "auth": auth
        }
        res=requests.post(url,headers=header,json=Addbody,verify=False)
        print res
        print res.json()
        print type(res.json())
        cardNo=res.json()['resultData']['cardNo']
        resultCode=res.json()['resultCode']
        # print cardNo,resultCode
        return cardNo,resultCode

    #定时转入保存接口
    def scheduleInfoSave(self,custId,auth,cardNo):
        url = com + '/SRCalendar/scheduleInfoSave'
        # for transferDay in range(1,29):
        Savebody = {
            "custId": custId,
            "auth": auth,
            "cardNo":cardNo,
            "transferAmount":transferAmount,
            "transferDay":transferDay,
            "sign":'1',
            "remark":""
        }
        print Savebody
        res = requests.post(url, headers=header, json=Savebody, verify=False)
        print res
        print res.json()
        resultCode = res.json()['resultCode']
        return resultCode

    #短信发送接口
    def smsCodeSend(self, custId, auth, cardNo):
        url = com + '/SRCalendar/smsCodeSend'
        Sendbody = {
            "custId": custId,
            "auth": auth,
            "cardNo": cardNo
        }
        res = requests.post(url, headers=header, json=Sendbody, verify=False)
        print res
        print res.json()
        cardNo = res.json()['resultData']['cardNo']
        resultCode = res.json()['resultCode']
        return cardNo, resultCode

    #短信验证接口
    def smsCodeVerify(self, custId, auth, cardNo):
        url = com + '/SRCalendar/smsCodeVerify'
        Verifybody = {
            "custId": custId,
            "auth": auth,
            "cardNo": cardNo,
            "smsCode":smsCode
        }
        res = requests.post(url, headers=header, json=Verifybody, verify=False)
        print res
        print res.json()
        # cardNo = res.json()['resultData']['cardNo']
        resultCode = res.json()['resultCode']
        return resultCode

    def test08_SRCalendar(self):
        data=self.doLogin()
        custId=data[0]
        auth=data[1]
        try:
            self.log.info(u"----调用定时转入列表查询接口----")
            resultdata=self.scheduleInfoList(custId,auth)
            if resultdata==[]:
                self.log.info(u"-----调用定时转入添加接口-----")
                data1 = self.scheduleInfoAdd(custId, auth)
                cardNo = data1[0]
                self.log.info(u"----调用定时转入保存接口----")
                resultCode = self.scheduleInfoSave(custId, auth, cardNo)
                self.assertEqual(resultCode, 0, msg=u'调用定时转入保存接口失败')
                self.log.info(u"----调用定时转入短信发送接口----")
                data2 = self.smsCodeSend(custId, auth, cardNo)
                cardNo = data2[0]
                resultCode = data2[1]
                self.assertEqual(resultCode, 0, msg=u'调用定时转入短信发送接口失败')
                self.log.info(u"----调用定时转入短信验证接口----")
                resultCode = self.smsCodeVerify(custId, auth, cardNo)
                self.assertEqual(resultCode, 0, msg=u'调用定时转入短信验证接口失败')
        except Exception as messages:
            print u"测试失败了:" + str(messages)

if __name__=='__main__':
    unittest.main