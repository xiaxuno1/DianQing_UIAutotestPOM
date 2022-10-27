# --------------------------------------------------
# !/usr/bin/python
# -*- coding: utf-8 -*-
# PN: DianQing_UIAutotestPOM
# FN: login_page
# Author: xiaxu
# DATA: 2022/7/29
# Description:登陆PO
# ---------------------------------------------------
from Base.base import Base
import time


class LoginPage(Base):
    url = "http://183.221.24.60:8000/login.html"
    #定义页面属性(不需要变动的量)
    iframe = ("id","login_oa")
    passwd_login_btn = ("css selector","td.logintype:nth-child(1)")
    usr_name = ("css selector","#Mac_Card")
    login_btn = ("css selector",
                 "#pwdlogin_div > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1)\
                 > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1)\
                > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) \
            > tr:nth-child(4) > td:nth-child(1) > img:nth-child(2)")
    passwd = ("xpath",'//*[@id="password"]')
    login_btn2 = ("css selector","#page_img")
    #定义页面方法
    def login(self,usr,psw):
        """登陆方法"""
        self.log.info("调用登录方法")
        self.get_url(self.url)
        self.iframe_in(*self.iframe)
        self.click(*self.passwd_login_btn)
        """输入 用户名"""
        self.send_key(usr,*self.usr_name)
        self.click(*self.login_btn)
        """输入密码"""
        time.sleep(2)
        self.send_key(psw,*self.passwd)
        """点击 登陆"""
        self.click(*self.login_btn2)
        self.iframe_out()
        time.sleep(5)
        return self.url
