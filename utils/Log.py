# -*-coding:utf-8 -*-
# @Author : Zhigang

import logging.config
from config.project_var import logger_file_path

#读取日志的配置文件
logging.config.fileConfig(logger_file_path)

#选择一个日志格式
logger=logging.getLogger("example02")

def debug(message):
    "打印debug级别的信息"
    logger.debug(message)

def info(message):
    "打印info级别的信息"
    logger.info(message)

def warning(message):
    "打印warnning级别的信息"
    logger.warning(message)

if __name__=="__main__":
    info("hi")
    debug("world")
    warning("gloryroad")