import unittest
from appium import webdriver
class Test(unittest.TestCase):
#装饰器截图
    driver = webdriver.Firefox()  # 全局参数driver

    def setUp(self):
        self.driver.get("https://www.baidu.com")

    @Screen(driver)
    def test01(self):
        u'''这个是失败的案例'''
        self.driver.find_element_by_id("11kw").send_keys("python")
        self.driver.find_element_by_id("su").click()

    @Screen(driver)
    def test_02(self):
        u'''这个是通过的案例'''
        self.driver.find_element_by_id("kw").send_keys("yoyo")
        self.driver.find_element_by_id("su").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()