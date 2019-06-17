# AppFramework
基于appium的混合驱动框架

AppTest:

--action
    --AppAction.py     # 关键字函数

--config  
    --Logger.conf         # 日志配置配文件
    --devices_config.ini      # 设备信息配置文件
    --project_var.py            # 工程路径及变量

-- screenshots
    --截图，以当前日志为目录名，当前时间为图片名称

--sourcedata
    --appcase.xlsx    # 数据操作文件，读取数据并记录测试结果

--testscript
    --runscript.py    #  运行主程序
    --TestLog.log     #  记录操作日志

--utils    # 封装常用模块
    --DirAndTime.py    # 时间模块
    --Log.py                  # 日志模块
    --ObjectMap.py     # 获取页面元素模块
    --ParseExcel.py       # 读取excel模块
    --ReadConfig.py     # 读取配置文件模块
    --WaitUtil.py           # 显示等待模块

---可忽略
script.py   # 未封装简单版本
scriptWaitUtil.py    # 显示等待方法验证
