# -*- coding:utf-8 -*-
class Login():
    def login(self, username, password):
        driver=self.driver
        driver.find_element_by_id("com.jd.jrapp:id/logon_account_pwd_login").clear()
        driver.find_element_by_id("com.jd.jrapp:id/logon_account_pwd_login").send_keys(username)
        driver.find_element_by_id("com.jd.jrapp:id/topLayout").clear()
        driver.find_element_by_id('com.jd.jrapp:id/topLayout').send_keys(password)
        driver.find_element_by_id('com.jd.jrapp:id/logon_btn_logon_pwd_login').click()
        '''
        #判断昵称
        name=driver.find_element_by_id("").text
        try:
        assert '' in name
        print "user is right"
        except AssertionError as e:
                print 'user is error'
        self.swipe.swipeDown(driver,n=2)
        #点击设置
        driver.find_element_by_id("").click()
        # 点击退出
        driver.find_element_by_id("").click()
        '''











