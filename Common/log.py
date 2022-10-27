# --------------------------------------------------
# !/usr/bin/python
# -*- coding: utf-8 -*-
# PN: BeginningPython
# FN: log
# Author: xiaxu
# DATA: 2020/8/10
# Description:日志类
# ---------------------------------------------------
import logging,time
from Common.function import project_path


class FrameLog():
    '''
    定义日志格式和内容，用法：调用模块
    log.error('input your error messege!')
    '''
    def __init__(self,logger = None):
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        #创建handler，用于设置日志格式
        self.log_time = time.strftime('%Y%m%d')
        self.log_path = project_path()+'/log/'
        self.log_name = self.log_path+self.log_time+'log.log'
        print(self.log_name)
        fh = logging.FileHandler(self.log_name,'a',encoding='utf-8') #设置输出文档的位置
        console = logging.StreamHandler() #设置输出到控制台
        fh.setLevel(logging.DEBUG)
        console.setLevel(logging.INFO) #设置输出的级别
        #设置handler的输出内容格式
        form = logging.Formatter(
            '%(asctime)-17s %(levelname)-8s %(pathname)s %(lineno)-5d %(message)s')  # -8S 左对齐，占位符8位，设置输出内容格式
        fh.setFormatter(form)
        console.setFormatter(form)
        #将logger添加到handler
        self.logger.addHandler(fh) #添加指定的句柄给logger
        self.logger.addHandler(console)
        #logger.error(str)
        #关闭操作
        #self.logger.removeHandler(fh) #移除句柄
        #fh.close()

    def log(self):
        return self.logger

if __name__ == '__main__':
    frame_log = FrameLog()
    log = frame_log.log()
    log.info("this is a info message")
    log.debug("this is a debug message")
    log.error("this is a error message")
    log.warning('this is a warn message')
    log.critical('this is a critical message')





