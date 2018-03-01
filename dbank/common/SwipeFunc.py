#coding=utf-8
#封装滑动方法
import time
class Swipe():
    def swipeUP(driver, t=500, n=1):
        l = driver.get_window_size()
        x1 = l['width'] * 0.5
        y1 = l['height'] * 0.75
        y2 = l['height'] * 0.25
        for i in range(n):
            driver.swipe(x1, y1, x1, y2, t)


    def swipeDown(driver, t=500, n=1):
        l = driver.get_window_size()
        x1 = l['width'] * 0.5
        y1 = l['height'] * 0.25
        y2 = l['height'] * 0.75
        for i in range(n):
            driver.swipe(x1, y1, x1, y2, t)

    def swipeLeft(driver, t=500, n=1):
        l = driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.05
        for i in range(n):
            driver.swipe(x1, y1, x2, y2, t)

    def swipeRight(driver, t=500, n=1):
        l = driver.get_window_size()
        x1 = l['width'] * 0.05
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            driver.swipe(x1, y1, x2, y1, t)

if __name__=="__main__":
    print Swipe().driver.get_window_size()
    time.sleep(5)
    Swipe().swipeLeft(Swipe().driver,n=2)
    time.sleep(5)
    Swipe().swipeRight(Swipe().driver,n=2)