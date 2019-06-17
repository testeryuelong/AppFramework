# -*-coding:utf-8 -*-
# @Author : Zhigang

from configparser import ConfigParser
from config.project_var import devices_config_path

def read_config(path,sectionName):
    """读取配置文件"""
    cf=ConfigParser()
    cf.read(path)
    if sectionName not in cf.sections():
        return "无此设备记录"
    platformName=cf.get(sectionName,"platformName")
    platformVersion=cf.get(sectionName,"platformVersion")
    deviceName=cf.get(sectionName,"deviceName")
    return platformName,platformVersion,deviceName

if __name__=="__main__":
    # 不封装方法直接读取
    cf=ConfigParser()
    cf.read(devices_config_path)
    print (cf.sections())
    print (cf.items("Redmi_Note_3"))
    print (cf.options("Redmi_Note_3"))
    print (cf.get("Redmi_Note_3","platformName"))
    print (read_config(devices_config_path,"Redmi_Note_3"))