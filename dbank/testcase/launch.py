# -*- coding:utf-8 -*-
import os
import time
import unittest
from appium import webdriver
class Launch(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        # desired_caps['deviceName'] = '127.0.0.1:62025'
        desired_caps['deviceName'] = '0715f7ea67102e34'
        desired_caps['appPackage'] = 'cn.srbank.directbank'
        desired_caps['No Reset'] = 'True'
        desired_caps['noSign'] = 'True'
        desired_caps['unicodeKeyboard'] = 'True'
        # 将键盘隐藏起来
        desired_caps['resetKeyboard'] = 'True'
        # 自动启动
        desired_caps['autoLaunch'] = 'True'
        # app路径
        desired_caps['app'] = os.path.abspath('E:\\apk\\app-release-sign.apk')
        desired_caps['appActivity'] = 'cn.srbank.directbank.SplashActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # 设置隐性等待时间
        self.driver.implicitly_wait(20)
        ac = self.driver.current_activity
        print(ac)
        # 错误的信息将被打印到这个列表中
        self.verificationErrors = []
        # 是否继续接受下一个警告
        self.accept_next_alert = True
        Is_installed = self.driver.is_app_installed("cn.srbank.directbank")
        if Is_installed == True:
            print Is_installed
        else:
            self.driver.close()
        # 等待主进程   进入欢迎页
        driver = self.driver
        driver.implicitly_wait(5)
        driver.wait_activity(".base.ui.MainActivity", 60)
        # print u"""欢迎页"""
        # for i in range(4): #滑动三次
        #     print u'开始执行滑动', i + 1
        #     driver.swipe(start_x=333, start_y=497, end_x=50, end_y=497, duration=800)
        #     driver.implicitly_wait(5)
        # if driver.find_elements_by_xpath("//android.widget.Button[contains(@text,'立即体验')]"):
        #     driver.find_element_by_id("com.jd.jrapp:id/btn_goto_page").click()
        # if driver.find_elements_by_xpath("//android.widget.Button[contains(@text,'跳过')]"):
        #     driver.find_element_by_id("com.jd.jrapp:id/cancel").click()
        #         # 此处无法
        # driver.implicitly_wait(20)
        ac = driver.current_activity
        print(ac)
        driver.find_element_by_id("cn.srbank.directbank:id/home_login").click()  # 点击登录
        # Swipe().swipeRight(driver, 1000)
        # el =driver.find_element_by_id("com.jd.jrapp:id/item_horizontal_scroll")  按压控件
        # TouchAction(driver).press(el).release().perform()
        driver.implicitly_wait(3)
        ac = driver.current_activity
        print(ac)


    def test_setup(self):
        self.setUp()