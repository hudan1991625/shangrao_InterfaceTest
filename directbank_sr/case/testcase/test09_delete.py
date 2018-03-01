# coding:utf-8
import unittest
import requests
from login import Login
from common.para import *

#限制定时转入只有一条数据,先执行添加接口创建定时任务,再调用此用例做删除
class Delete(Login):
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
        data=res.json()['resultData']
        if data==[]:
            return data
        else:
            for i in range(len(data)):
                data1= data[i]
                if i == 0:
                    id = data1['id']
                    print id
                    return id
                else:
                    pass

    #定期转入设定详情接口
    def scheduleInfoDetail(self,custId,auth,id):
        url = com + '/SRCalendar/scheduleInfoDetail'
        Detailbody = {
            "custId": custId,
            "auth": auth,
            "id": id
        }
        res = requests.post(url, headers=header, json=Detailbody, verify=False)
        print res
        print res.json()
        # cardNo = res.json()['resultData']['cardNo']
        resultCode = res.json()['resultCode']
        return resultCode

    # 首页当天收支情况展示
    def dailyTrade(self,custId,auth):
        url = com + '/SRCalendar/dailyTrade'
        dailyTradebody = {
            "custId": custId,
            "auth": auth,
            "queryDate": queryDate
        }
        print dailyTradebody
        res = requests.post(url, headers=header, json=dailyTradebody, verify=False)
        print res
        print res.json()
        return res.json()['resultCode']

    # 首页记账展示
    def tally(self, custId, auth):
        url = com + '/SRCalendar/tally'
        tallybody = {
            "custId": custId,
            "auth": auth,
            "pageSize": pageSize,
            "curPage": curPage,
            "queryDate": queryDate
            }
        res = requests.post(url, headers=header, json=tallybody, verify=False)
        print res
        print res.json()
        return res.json()['resultCode']

    # 金融日历——查询jrid绑定关系接口
    def getJrId(self, custId, auth):
        url = com + '/SRCalendar/getJrId'
        getJrIdbody = {
            "custId": custId,
            "auth": auth
        }
        res = requests.post(url, headers=header, json=getJrIdbody, verify=False)
        print res
        print res.json()
        return res.json()['resultCode']

    # SRCalendar/authJrid
    def authJrid(self, custId, auth):
        url = com + '/SRCalendar/authJrid'
        Jridbody = {
            "custId": custId,
            "auth": auth
        }
        print Jridbody
        res = requests.post(url, headers=header, json=Jridbody, verify=False)
        print res
        print res.json()
        return res.json()['resultCode']

    # 定时设置删除接口
    def scheduleInfoDel(self, custId, auth,id):
        url = com + '/SRCalendar/scheduleInfoDel'
        Delbody = {
            "custId": custId,
            "auth": auth,
            "id": id
        }
        res = requests.post(url, headers=header, json=Delbody, verify=False)
        print res
        print res.json()
        return res.json()['resultCode']

    def test09_delete(self):
        data=self.doLogin()
        custId=data[0]
        auth=data[1]
        self.log.info("---------------调用定时转入列表查询接口------------")
        data1=self.scheduleInfoList(custId,auth)
        id=data1
        self.log.info("-----------调用定时转入详情接口------------")
        resultCode=self.scheduleInfoDetail(custId,auth,id)
        self.assertEqual(resultCode,0,msg='调用定时转入详情接口失败')
        self.log.info("----调用首页转入转出接口----")
        resultCode = self.dailyTrade(custId, auth)
        self.assertEqual(resultCode, 0, msg='调用首页转入转出接口失败')
        self.log.info("----调用首页记账接口接口----")
        resultCode = self.tally(custId, auth)
        self.assertEqual(resultCode, 0, msg='调用首页记账接口失败')
        # resultCode = self.getJrId(custId, auth)
        # if resultCode == 2:
        #     self.log.info("----调用查询jrid绑定关系接口----")
        #     resultCode = self.authJrid(custId, auth)
        #     self.assertEqual(resultCode, 0, msg='调用查询jrid绑定关系接口失败')
        #     print '----------------------------------------------------'
        # elif resultCode == 1:
        #     self.log.info("调用jrid绑定关系接口失败")
        # else:
        #     self.log.info("用户有jrId，直接进入记账页面")
        self.log.info("--------调用定时转入删除接口------------")
        resultCode=self.scheduleInfoDel(custId,auth,id)
        self.assertEqual(resultCode, 0, msg='调用定时转入删除接口失败')

if __name__=='__main__':
    unittest.main