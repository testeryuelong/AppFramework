# -*-coding:utf-8 -*-
# @Author : Zhigang

import time
import os
from datetime import datetime
from config.project_var import screenshot_path

def getCurrentDate():
    "获取当前的日期"
    currentDate=time.strftime("%Y-%m-%d",time.localtime())
    return currentDate

def getCurrentTime():
    "获取当前的时间"
    timeStr=datetime.now()
    nowTime=timeStr.strftime("%H-%M-%S-%f")
    return nowTime
    # currentTime = time.strftime("%H-%M-%S %X", time.localtime())

def createCurrentDateDir():
    "创建截图存放的目录"
    dirName=os.path.join(screenshot_path,getCurrentDate())
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    return dirName

if __name__=="__main__":
    print (getCurrentDate())
    print (getCurrentTime())
    print (createCurrentDateDir())