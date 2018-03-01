import unittest
from time import sleep

from appium import webdriver
from desired_caps import desired_Caps


class Login():

    # 用户登录
    def mlogin(self, driver, mobile, password):
        """
        #权限确定
        sleep(5)
        if driver.find_elements_by_xpath("//android.widget.Button[contains(@text,'总是允许')]"):
                driver.find_element_by_xpath("//android.widget.Button[contains(@text,'总是允许')]").click()
        if driver.find_elements_by_xpath("//android.widget.Button[contains(@text,'始终允许')]"):
                driver.find_element_by_xpath("//android.widget.Button[contains(@text,'始终允许')]").click()
        if driver.find_elements_by_xpath("//android.widget.Button[contains(@index,'1')]"):
                driver.find_element_by_xpath("//android.widget.Button[contains(@index,'1')]").click()
        # 通过引导页
        sleep(2)
        Swipe().swipeLeft(driver, 1000)
        sleep(5)
        Swipe().swipeLeft(driver, 1000)
        sleep(5)
        driver.find_element_by_id('com.www.diandou:id/start_Button').click()
        """
        # 登录
        # driver.find_element_by_id('com.www.diandou:id/rl_mine').click()
        driver.find_element_by_id('com.www.diandou:id/et_phone').send_keys(mobile)
        driver.find_element_by_id('com.www.diandou:id/et_password').send_keys(password)
        driver.find_element_by_id('com.www.diandou:id/btn_login').click()

    # 用户退出
    def mloginout(self, driver):

        sleep(2)
        driver.find_element_by_id('com.www.diandou:id/rl_mine').click()
        driver.find_element_by_id('com.www.diandou:id/iv_setting').click()
        driver.find_element_by_id('com.www.diandou:id/btn_exit').click()
        driver.find_element_by_id('com.www.diandou:id/dialog_sure').click()
        sleep(1)

class AndriodTest(unittest.TestCase):
    '''登录和退出'''
    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test end")

    def test_mobile(self):
        '''登录和退出'''
        desired_caps = desired_Caps()
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(2)
        try:
            Login().mloginout(driver)
            sleep(1)
            # 调用登录退出方法
            mobile = 17732056982
            password = 123456
            Login().mlogin(driver, mobile, password)
            sleep(1)

        finally:
            # 退出程序
            driver.quit()
            sleep(5)

if __name__ == '__main__':
    unittest.main()




