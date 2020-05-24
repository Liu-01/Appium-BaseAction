from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class BaseAction():
    # 引用driver对象
    def __init__(self,driver):
        self.driver=driver
        # 先借用一下init_driver方便编写函数
        # self.driver=init_driver()
        # 查找元素
    def find_element(self,log):
        # ele = self.driver.find_element(log[0],log[1])
        # return ele
        return WebDriverWait(self.driver,10,0.5).until(lambda x:x.find_element(log[0],log[1]))

    def find_elements(self,log):
        return WebDriverWait(self.driver,10,0.5).until(lambda x:x.find_elements(log[0],log[1]))
    # 点击元素
    def click(self,log):
        self.find_element(log).click()
    # 打开app
    def open_app(self,package,activity):
        self.driver.start_activity(package,activity)
    # 获取页面的大小
    def get_size(self):
        z=self.driver.get_window_size()
        return z
    # 滑动屏幕
    def swip_half_screen(self):
        self.driver.swipe(start_x=(self.get_size().get('width'))*0.5,start_y=(self.get_size().get('height'))*0.9\
                          ,end_x=(self.get_size().get('width'))*0.5,end_y=(self.get_size().get('height'))*0.2,duration=1000)
     # 通过坐标滑动屏幕
    def swip_screen_freedom(self,x0,y0,x1,y1):
        self.driver.swipe(start_x=x0,start_y=y0,end_x=x1,end_y=y1,duration=2000)
    # 返回键
    def back_keyevent(self):
        self.driver.keyevent(4)
    # 菜单键
    def menu_keyevent(self):
        self.driver.keyevent(82)
    # 关闭虚拟机
    def quit(self):
        self.driver.quit()
    # 获取页面元素
    def get_window_source(self):
        return self.driver.page_source
    # 获取元素坐标
    def ele_location(self,log):
       return self.find_element(log).location
    # 按住屏幕
    def press_srceen(self,log):
        TouchAction(self.driver).press(self.find_element(log)).perform()
        # 点击屏幕通过元素
    def tap_screen_by_element(self,log):
        TouchAction(self.driver).tap(self.find_element(log)).perform()
    # 点击屏幕通过坐标
    def tap_screen_by_location(self,x,y):
        TouchAction(self.driver).tap(x,y).perform()
        # 长按屏幕
    def long_press(self,log,time):
        TouchAction(self.driver).long_press((self.find_element(log)),duration=time).perform()
    # def move_to(self,value,log):
    #     TouchAction(self.driver).press(self.find_element(value)).wait(1000).move_to(self.find_element(log)).perform()
    # 移动
    def drag_and_down(self,log,log2):
        self.driver.drag_and_drop(self.find_element(log),self.find_element(log2))
    # 截图
    def get_screenshot_as_file(self):
        self.driver.get_screenshot_as_file('../report/pic.png')
    # 下拉通知栏
    def open_notifications(self):
        self.driver.open_notifications()
    # 查看网络
    def network_connection(self):
        return self.driver.network_connection
    # toast
    def find_toast(self,message):
        ele= WebDriverWait(self.driver, 10, 0.5).until(
            lambda x: x.find_element_by_xpath('//*[contains(@text,"' + message + '")]'))
        return ele.text

