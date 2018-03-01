# coding:utf-8
import unittest
import requests
from common.para import *
class Value:
    value=14140000005
    def __init__(self):
        Value.value+=1
    def get_value(self):
        print 'mobile is %s'%Value.value
        print type(Value.value)
        return Value.value


class register(Value,unittest.TestCase):

    def register(self,data):
        url = com + "/registSendSms"
        rbody=body.copy() #利用copy方法，新建一块内存存放body
        rbody['mobile']=data
        print rbody
        r = requests.post(url, json=rbody, headers=header, verify=False)
        print r
        print r.json()
        print type(r.json())
        return r.json()

if __name__=='__main__':
    S = Value()
    data=S.get_value()
    q=register()
    resultcode=q.register(data)
    if resultcode!=0:

        q.register(data)
    unittest.main