import time


# 导入webdriver包
from appium import webdriver
# 搞模拟器
from selenium.webdriver.support.wait import WebDriverWait
def init_driver():
    desired_caps={}
    # 系统名称
    desired_caps['platformName']='Android'
    # 系统版本
    desired_caps['platformVersion']='5.1.1'
    # 设备名称
    desired_caps['deviceName']='127.0.0.1:62001'
    # app包名
    desired_caps['appPackage']='com.android.settings'
    # app启动名
    desired_caps['appActivity'] = '.Settings'
    # 是否运行中文输入
    desired_caps['unicodeKeyboard']='True'
    # 是否收起键盘
    desired_caps['resetKeyboard']='True'
    # 自动运行
    desired_caps['autoLaunch']='False'
    # toast
    desired_caps['automationName']='Uiautomator2'
    # 声明对象
    driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
    return driver



