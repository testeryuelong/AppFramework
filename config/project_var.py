# -*-coding:utf-8 -*-
# @Author : Zhigang

import os

# 绝对路径
project_var=os.path.dirname(os.path.dirname(__file__))

# 设备信息配置文件路径
devices_config_path=os.path.join(project_var,"config","devices_config.ini")

# 日志文件路径
logger_file_path=os.path.join(project_var,"config","Logger.conf")

# 截图文件路径
screenshot_path=os.path.join(project_var,"screenshots")

# 数据文件路径
data_file_path=os.path.join(project_var,"sourcedata","appcase.xlsx")

# 测试用例列号
testCaseId=1
testCaseDesc=2
testCaseFrameType=3
testCaseSheetName=4
testCaseIsExecute=6
testCaseExecuteTime=7
testCaseExecuteResult=8

# 测试步骤列号
testStepDesc=1
testStepKeyWords=2
testStepLocateMode=3
testStepLocateExp=4
testStepOperateValue=5
testStepExecuteTime=6
testStepExecuteResult=7
testStepErrorInfo=8
testStepErrorScreenshot=9


if __name__=="__main__":
    print (project_var)
    print (devices_config_path)
    print (logger_file_path)
    print (screenshot_path)