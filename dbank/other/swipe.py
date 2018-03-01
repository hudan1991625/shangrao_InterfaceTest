from time import sleep
from appium import webdriver
from desired_caps import desired_Caps
import unittest

class Swipe():

    #获取屏幕宽和高

    def getSize(self, driver):
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        return (x, y)

    #向左滑动
    def swipeLeft(self, driver, t):
        l = self.getSize(driver)
        x1 = int(l[0]*0.9)
        y1 = int(l[1]*0.5)
        x2 = int(l[0]*0.1)
        driver.swipe(x1, y1, x2, y1, t)
    #向右滑动
    def swipeRight(self, driver, t):
        l = self.getSize(driver)
        x1 = int(l[0]*0.1)
        y1 = int(l[1]*0.5)
        x2 = int(l[0]*0.9)
        driver.swipe(x1, y1, x2, y1, t)

    #向上滑动
    def swipeUp(self, driver, t):
        l = self.getSize(driver)
        x1 = int(l[0]*0.5)
        y1 = int(l[1]*0.8)
        y2 = int(l[1]*0.2)

        driver.swipe(x1, y1, x1, y2, t)

    #向下滑动
    def swipeDown(self, driver, t):
        l = self.getSize(driver)
        x1 = int(l[0]*0.5)
        y1 = int(l[1]*0.2)
        y2 = int(l[1]*0.8)
        driver.swipe(x1, y1, x1, y2, t)

#单元测试
class Test(unittest.TestCase):

    def setUp(self):
        print("test start")

    def test_case(self):
        desired_caps = desired_Caps()
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(5)
        #已登录用户在我的页面上滑和下滑
        sleep(2)
        Swipe().swipeUp(driver, 1000)
        sleep(2)
        Swipe().swipeDown(driver, 1000)
        sleep(2)
        #退出程序
        driver.quit()


    def tearDown(self):
        print("test end")


