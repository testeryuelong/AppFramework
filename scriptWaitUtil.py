# -*-coding:utf-8 -*-
# @Author : Zhigang
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver
from selenium.webdriver.common.by import By

def getElement(driver,locateType,locatorExpression):
    "获取单个页面元素对象"
    try:
        print (locateType)
        print (locatorExpression)
        element=WebDriverWait(driver,5).until\
            (lambda x:x.find_element(by=locateType,value=locatorExpression))
        return element
    except Exception as e:
        raise e


if __name__=="__main__":
    desired_caps = {'platformName': 'Android',
                'platformVersion': '5.1.1',
                'deviceName': '18d1c688',
                'appPackage': 'com.xsteach.appedu',
                'appActivity': 'com.xsteach.components.ui.activity.XSMainActivity',
                # 支持中文输入要添加的代码
                'unicodeKeyboard': True,
                'resetKeyboard': True,
                }

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.implicitly_wait(10)  # 隐式等待

    # 点击个人中心
    # driver.find_element_by_id('com.xsteach.appedu:id/content_rb_mine').click()
    getElement(driver,"id","com.xsteach.appedu:id/content_rb_mine").click()
    # 点击立即登录
    # driver.find_element_by_id('com.xsteach.appedu:id/tvLogin').click()
