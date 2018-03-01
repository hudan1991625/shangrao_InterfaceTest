# -*- coding:utf-8 -*-
import os,time
import unittest
from appium import webdriver
from common.SwipeFunc import Swipe

class Login(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        #desired_caps['deviceName'] = '127.0.0.1:62025'
        desired_caps['deviceName'] = '0715f7ea67102e34'
        desired_caps['appPackage'] = 'com.jd.jrapp'
        desired_caps['No Reset'] = 'True'
        desired_caps['unicodeKeyboard'] ='True'
        # 将键盘隐藏起来
        desired_caps['resetKeyboard'] = 'True'
        # 自动启动
        desired_caps['autoLaunch'] = 'True'
        # app路径
        desired_caps['app'] = os.path.abspath('E:\\apk\\jrapp.apk')
        desired_caps['appActivity'] = 'com.jd.jrapp.WelcomeActivity'
        self.driver= webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        #设置隐性等待时间
        self.driver.implicitly_wait(20)
        ac = self.driver.current_activity
        print(ac)
        #错误的信息将被打印到这个列表中
        self.verificationErrors = []
        #是否继续接受下一个警告
        self.accept_next_alert = True
        Is_installed = self.driver.is_app_installed("com.jd.jrapp")
        if Is_installed == True:
            print Is_installed
        else:
            self.driver.close()
        #等待主进程   进入欢迎页
        driver=self.driver
        #driver.implicitly_wait(5)
        driver.wait_activity(".base.ui.MainActivity", 20)
        ac = driver.current_activity
        print(ac)
        print u"""欢迎页"""
        for i in range(3):  # 滑动三次,不包含3
            print u'开始执行滑动', i + 1
        driver.implicitly_wait(2)
        # S=Swipe()
        # S.swipeRight(self,t=1000, n=4)
        # Swipe.swipeRight(self,driver,t=1000, n=4)
        # driver.swipe(start_x=333, start_y=497, end_x=50, end_y=497, duration=800)
        if driver.find_elements_by_xpath("//android.widget.Button[contains(@text,'立即体验')]"):
            driver.find_element_by_id("com.jd.jrapp:id/btn_goto_page").click()
        if driver.find_elements_by_xpath("//android.widget.Button[contains(@text,'跳过')]"):
            driver.find_element_by_id("com.jd.jrapp:id/cancel").click()
            # 此处无法
        driver.implicitly_wait(20)
        driver.find_element_by_id("com.jd.jrapp:id/iv_fourth_icon").click() #点击我的
        #Swipe().swipeRight(driver, 1000)
        # el =driver.find_element_by_id("com.jd.jrapp:id/item_horizontal_scroll")  按压控件
        # TouchAction(driver).press(el).release().perform()
        driver.implicitly_wait(5)
        ac = driver.current_activity
        print(ac)
        elment = driver.findElementByXPath("//android.widget.TextView[contains(@text,'立即登录')]")
        elment.click()

    def login(self, username, password):
        driver=self.driver
        driver.find_element_by_id("com.jd.jrapp:id/logon_account_pwd_login").clear()
        driver.find_element_by_id("com.jd.jrapp:id/logon_account_pwd_login").send_keys(username)
        driver.find_element_by_id("com.jd.jrapp:id/topLayout").clear()
        driver.find_element_by_id('com.jd.jrapp:id/topLayout').send_keys(password)
        driver.find_element_by_id('com.jd.jrapp:id/logon_btn_logon_pwd_login').click()

    def loginout(self):
        driver=self.driver
        time.sleep(2)
        driver.find_element_by_id('com.www.diandou:id/rl_mine').click() #待修改
        driver.find_element_by_id('com.www.diandou:id/iv_setting').click()
        driver.find_element_by_id('com.www.diandou:id/btn_exit').click()
        driver.find_element_by_id('com.www.diandou:id/dialog_sure').click()
        time.sleep(1)

    def test1_login(self):
        self.setUp()
        #如果已经登录则退出登录
        try:
            self.loginout()
            time.sleep(1)
            # 调用登录退出方法
            usrname = '18710469348'
            passwd = "hudan1991625"
            self.login(usrname, passwd)
            time.sleep(2)
        finally:
            # 退出程序
            self.driver.close()
            time.sleep(5)

    def tearDown(self):
        print "test case end"

    if __name__ == '__main__':
        unittest.main()