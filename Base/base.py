 # --------------------------------------------------
# !/usr/bin/python
# -*- coding: utf-8 -*-
# PN: BeginningPython
# FN: base
# Author: xiaxu
# DATA: 2020/8/11
# Description:定义基础操作，元素定位，窗口切换等操作
# ---------------------------------------------------
import time
from Common.function import  project_path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from Common.log import FrameLog
import unittest


class Base():

    def __init__(self,driver,log):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.log = log

    def get_url(self,*args):
        self.driver.get(args[0])

    #此处接受任意多个非关键字参数
    def findele(self,*args):
        try:
            self.log.info('通过'+args[0]+'定位,元素是'+args[1])
            return self.driver.find_element(*args)  #之所以要返回是因为，定位是为了操作
        except:
            self.log.error('定位元素失败')

    #定义点击方式
    def click(self,*args):
        print(args[0],args[1])
        self.findele(*args).click()

    #定义输入值方法
    def send_key(self,value,*args):
        """只接收三个"""
        self.findele(args[0],args[1]).send_keys(value)

    #调用JS方法
    def js(self,str):
        self.driver.execute_script(str)

    #返回url
    def url(self):
        return self.driver.current_url

    #后退
    def back(self):
        self.driver.back()

    #前进
    def forward(self):
        self.driver.forward()

    #退出
    def quit(self,*args):
        """这里的args没有使用，但是传入时为了能够统一调用方法;为了接口的统一性"""
        self.driver.quit()

    #定义iframe的选择方法
    def iframe_in(self,*args):
        iframe_loc = self.findele(*args)
        #print(iframe_loc)
        self.driver.switch_to.frame(iframe_loc)

    #定义iframe的退出方法
    def iframe_out(self,*args):
        self.driver.switch_to.default_content()

    #定义显示等待
    def ele_wait_dispaly(self,*args):
        #print("显示等待中......",args)
        return WebDriverWait(self.driver,10,0.5).until(
            EC.visibility_of_all_elements_located(args))

    # 强制等待
    def wait_sleep(self,time_):
        time.sleep(eval(time_))

    #定义断言
    def assert_equal(self,name,value,expect):
        try:
            reality = self.findele(name, value).text
            assert expect == reality, '断言失败，实际结果为：{}'.format(reality)
            return True
        except Exception as e:
            print('断言失败信息：' + str(e))
            return False
    #相对定位器 上下左右中

    #句柄的切换
    def handle_switch(self,index = 1):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[index])

    #定义下拉框选择
    def select_ele(self,*args,method ="index" ):
        desktop_ele = self.findele(args[0],args[1])
        method = args[2]
        value = args[3]
        if method in "index":
           return Select(desktop_ele).select_by_index(value)
        elif method in "value":
            return (desktop_ele).select_by_value(value)
        elif method in "text":
            return Select(desktop_ele).select_by_visible_text(value)
        else:
            print("未知的下拉框定位方法:",value)

    def cookie_op(self,*args,method = "cookies"):
        if "cookies" in method:
            return self.driver.get_cookies()
        elif "add" in method:
            self.driver.add_cookie(args[0])

if __name__ == '__main__':
    frame_log = FrameLog()
    log = frame_log.log()
    keys = Keyword("Firefox",log)
    url =' http://183.221.24.60:8000/login.html'
    getattr(keys,"get_url")(url)
    getattr(keys, "iframe_in")("id","login_oa")
    getattr(keys,'click')('css selector', 'td.logintype:nth-child(1)')
    a= None
    getattr(keys,"quit")(a)