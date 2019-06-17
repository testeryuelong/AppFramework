# -*-coding:utf-8 -*-
# @Author : Zhigang

from appium import webdriver
import time

# 启动app,此过程中会提示在手机上安装Appium Setting
# Redmi_Note_3
desired_caps = {'platformName': 'Android',
                'platformVersion': '5.1.1',
                'deviceName': '18d1c688',
                'appPackage': 'com.xsteach.appedu',
                'appActivity': 'com.xsteach.components.ui.activity.XSMainActivity',
                # 支持中文输入要添加的代码
                'unicodeKeyboard':True,
                'resetKeyboard':True,
                }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)  # 隐式等待
# print (driver)

# 点击个人中心
driver.find_element_by_id('com.xsteach.appedu:id/content_rb_mine').click()

# 点击立即登录
driver.find_element_by_id('com.xsteach.appedu:id/tvLogin').click()

# 定位输入手机号
username=driver.find_element_by_id('com.xsteach.appedu:id/etUser')
username.clear()
username.send_keys('18730603667')

# 定位密码框
password=driver.find_element_by_id('com.xsteach.appedu:id/etPwd')
password.clear()
password.send_keys('123456yuzg')

# 点击登录按钮
driver.find_element_by_id('com.xsteach.appedu:id/btnLogin').click()


# 确定是否登录成功
user=driver.find_element_by_id('com.xsteach.appedu:id/tvUser').text


# print (driver.find_element_by_id('com.xsteach.appedu:id/tv_integral').text)
assert "我的积分" in driver.page_source


# 点击首页
driver.find_element_by_id('com.xsteach.appedu:id/content_rb_home').click()

# 点击搜索课程输入框
driver.find_element_by_id('com.xsteach.appedu:id/rl_home_top_search').click()

# 点击输入框
editSearch=driver.find_element_by_id('com.xsteach.appedu:id/editText')
editSearch.clear()
editSearch.click()

driver.find_element_by_xpath('//android.widget.TextView[contains(@text,"UI设计")]').click()

time.sleep(3)

driver.find_element_by_xpath('//android.widget.TextView[contains(@text,"取消")]').click()

# 再次点击个人中心
driver.find_element_by_id('com.xsteach.appedu:id/content_rb_mine').click()

# 点击设置
driver.find_element_by_id('com.xsteach.appedu:id/me_set_relative').click()


# 滑动页面
from appium.webdriver.common.touch_action import TouchAction
def test_scroll_down(driver):
    screen = driver.get_window_size()
    action = TouchAction(driver)
    action.press(x=screen['width']/2,y=screen['height']/2)
    action.move_to(x=0,y=screen['height']/10)
    action.release()
    action.perform()

test_scroll_down(driver)

# 退出当前账号
driver.find_element_by_id('com.xsteach.appedu:id/logout_user_tv').click()


# 点击确定,通过id、xpath定位
driver.find_element_by_id('com.xsteach.appedu:id/btnYes').click()
# driver.find_element_by_xpath('//android.widget.Button[contains(@text,"确定")]').click()

time.sleep(3)
# 关闭app
driver.close_app()
