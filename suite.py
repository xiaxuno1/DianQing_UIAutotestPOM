# --------------------------------------------------
# !/usr/bin/python
# -*- coding: utf-8 -*-
# PN: DianQing_UIAutotestPOM
# FN: suite
# Author: xiaxu
# DATA: 2022/8/1
# Description:测试套件
# ---------------------------------------------------
import unittest,time
from Common.function import project_path
from TestCases import test_login
import HTMLTestRunner


if __name__ == '__main__':
    test_path = project_path()+"TestCases\\"
    """配置测试用例的路径"""
    print(test_path)
    tests = unittest.defaultTestLoader.discover(start_dir=test_path,
                                        pattern="test*.py",top_level_dir=None)
    """测试套"""
    #suite = unittest.TestSuite()
    """添加测试用例"""
    #suite.addTest(test_login.TestLogin("test_login_01"))
    """添加测试运行器"""
    #runner_text = unittest.TextTestRunner() #运行器的格式为text
    """利用HTMLTestRunner生成html格式的测试报告"""
    reporter_name = time.strftime("%Y-%m-%d",time.localtime(time.time()))+"testReporter"
    strem_path = project_path()+"/Reporter/"+reporter_name+".html"
    title = "OA 自动化测试报告"
    description = "系统自动化测试报告"
    strem = open(strem_path,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=strem,title=title,description=description)
    runner.run(tests)
    strem.close()

