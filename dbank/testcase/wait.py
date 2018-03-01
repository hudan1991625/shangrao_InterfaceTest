# coding:utf-8
from appium import webdriver
desired_caps = {
                'platformName': 'Android',
                'deviceName': '127.0.0.1:62001',
                'platformVersion': '4.4.2',
                'appPackage': 'com.baidu.yuedu',
                'appActivity': 'com.baidu.yuedu.splash.SplashActivity'
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# sleep(10)  # 不用sleep

# 获取当前界面activity
ac = driver.current_activity
print(ac)

# 等主页面activity出现,30秒内
driver.wait_activity(".base.ui.MainActivity", 30)

# 点知道了
driver.find_element_by_id("com.baidu.yuedu:id/positive").click()