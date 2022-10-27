# --------------------------------------------------
# !/usr/bin/python
# -*- coding: utf-8 -*-
# PN: DianQing_UIAutotestPOM
# FN: test_login
# Author: xiaxu
# DATA: 2022/7/29
# Description:登陆测试
# ---------------------------------------------------
from ddt import ddt,unpack,file_data,data
from PageObject.login_page import LoginPage
import unittest
from selenium import webdriver
from Common import log

@ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.log = log.FrameLog().log()
        cls.login_op = LoginPage(cls.driver,cls.log)
        cls.log.info("setUpClass成功")
        
    @classmethod
    def tearDownClass(cls) -> None:
        cls.log.info("tearDownClass成功")
        cls.driver.quit()

    @data(["xiaxu","psps2053","http://183.221.24.60:8000/mis/csun.html"])
    @unpack
    def test_login_01(self,usr,psw,except_):
        #print("usr={},psw = {},url = {}".format(usr,psw,except_))
        mainpage_url = self.login_op.login(usr,psw) #返回主页的url
        self.assertEqual(mainpage_url,except_)

if __name__ == '__main__':
    unittest.main()