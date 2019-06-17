# -*-coding:utf-8 -*-
# @Author : Zhigang

import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from utils.ReadConfig import read_config
from config.project_var import devices_config_path
from utils.WaitUtil import WaitUtil
from utils.ObjectMap import *
from utils.DirAndTime import *

# 定义全局变量driver和waitUtil
driver=None
waitUtil=None

def get_desired_caps(device):
    """
    从配置文件中获取连接信息
    :param device：设备名称
    """
    try:
        platformname,platformversion,devicename=read_config(devices_config_path,device)
    except Exception as e:
        raise e
    else:
        desired_caps = {'platformName': platformname,
                        'platformVersion': platformversion,
                        'deviceName': devicename,
                        'appPackage': 'com.xsteach.appedu',
                        'appActivity': 'com.xsteach.components.ui.activity.XSMainActivity',
                        # 支持中文输入要添加的代码
                        'unicodeKeyboard': True,
                        'resetKeyboard': True,
                        }
        return desired_caps

def open_app(device):
    """打开app
    :param device：设备名称"""
    global driver, waitUtil
    desired_caps=get_desired_caps(device)
    try:
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        waitUtil = WaitUtil(driver)
    except Exception as e:
        raise e

def close_app():
    "关闭app"
    global driver
    try:
        driver.close_app()
    except Exception as e:
        raise e

def sleep(sleepSeconds,*args):
    "强制等待"
    try:
        time.sleep(int(sleepSeconds))
    except Exception as e:
        raise e

def clear(locationType,locatorExpression,*args):
    "清除输入框默认内容"
    global  driver
    try:
        getElement(driver,locationType,locatorExpression).clear()
    except Exception as e:
        raise e

def input_string(locationType,locatorExpression,inputContent):
    "在页面输入框输入数据"
    global  driver
    clear(locationType, locatorExpression)
    try:
        getElement(driver,locationType,locatorExpression).send_keys(inputContent)
    except Exception as e:
        raise e

def click(locationType,locatorExpression,*args):
    "点击页面元素"
    global driver
    try:
        getElement(driver,locationType,locatorExpression).click()
    except Exception as e:
        raise e

def assert_string_in_pagesource(assertString,*args):
    "断言页面源码是否存在某关键字或关键字符串"
    global  driver
    try:
        assert assertString in driver.page_source,"{s} not found in page source!".format(s=assertString)
    except AssertionError as e:
        raise AssertionError(e)
    except Exception  as e:
        raise e

def waitVisibilityOfElementLocated(locationType,locatorExpression,*args):
    "显示等待页面元素出现在DOM中，并且可见，存在返回该页面元素对象"
    global waitUtil
    try:
        waitUtil.visibilityOfElementLocated(locationType,locatorExpression)
    except  Exception as e:
        raise e

def capture_screen(*args):
    "截取屏幕图片"
    global  driver
    # 获取当前时间，精确到毫秒
    currTime=getCurrentTime()
    # 拼接异常图片保存的绝对路径及名称
    picNameAndPath=createCurrentDateDir()+"\\"+str(currTime)+".png"
    try:
        "截取屏幕图片，并保存为本地文件"
        driver.get_screenshot_as_file(picNameAndPath.replace("\\",r"\\"))
    except Exception as e:
        raise e
    else:
        return picNameAndPath

def scroll_down():
    global driver
    screen = driver.get_window_size()
    action = TouchAction(driver)
    action.press(x=screen['width']/2,y=screen['height']/2)
    action.move_to(x=0,y=screen['height']/10)
    action.release()
    action.perform()

if __name__=="__main__":
    # from selenium import webdriver
    # driver=webdriver.Chrome()
    capture_screen()