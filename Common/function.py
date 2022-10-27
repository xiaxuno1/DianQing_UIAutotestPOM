# --------------------------------------------------
# !/usr/bin/python
# -*- coding: utf-8 -*-
# PN: BeginningPython
# FN: function
# Author: xiaxu
# DATA: 2020/8/7
# Description:包含处理文件的方法，获取路径，url
# ---------------------------------------------------
import os,configparser


def project_path():
    # https: // blog.csdn.net / weixin_39541558 / article / details / 79971971
    '''
    print(path)
    print(os.name) #返回操作系统得我名称nt为window，posix
    print(os.getcwd()) #返回当前工作路径（文件夹）
    print(os.listdir(os.getcwd())) #返回当前文件夹下的所有文件和目录,不会迭代（子目录）
    # os.remove(os.listdir(os.getcwd())[1]) #拒绝访问
    #os.system('cmd') #运行系统命令
    print(os.linesep)  #当前平台使用的行终止符
    print(os.sep) #路径分割符 \
    print(os.path.split(os.getcwd())) #返回路径的目录和文件名。
    print(os.path.isfile(os.getcwd())) #判断给出的是否为文件
    print(os.path.isdir(os.getcwd()))
    print(os.path.exists(os.getcwd())) #判断路径是否存在
    print(os.path.abspath('function.py')) #获取绝对路径
    print(os.path.getsize(os.path.abspath('function.py'))) #获取文件的大小
    print(os.path.splitext(os.path.abspath('function.ini'))) #分离文件名与拓展名1  .tet
    print(os.path.realpath(__file__)) #返回文件的绝对路径
    print(os.path.realpath(__file__).split('common'))
    '''
    #获取项目的路径
    return os.path.split(os.path.realpath(__file__))[0].split('Common')[0]
def login_url():
    '''
    :return:获取登陆界面的url ,从cofig.ini文件读取
    '''
    config = configparser.ConfigParser() #第一步：实例化
    config.read(project_path()+'config.ini') #第二步解析
    '''
    print(config.sections())  #获取所有的section,以列表形式
    print(config.items('url')) #获取section的内容
    print(config.options('url')) #获取section的key
    print(config['url']['url']) #获取section的key的value
    #写入配置文件
    #字典方式
    config.read_dict(
        {'frist_page':{'url':'http://183.222.190.104:8000/mis/csun.html?ui=new'} }
    )
    with open(pronject_path()+'config.ini','a') as fp:
        config.write(fp)
    '''
    return config.get('loginurl','url')  #第三步读取,获取指定section的指定名称内容，以=形式

def main_url():
    '''
    :return:获取系统首页的url ,从cofig.ini文件读取
    '''
    config = configparser.ConfigParser() #第一步：实例化
    config.read(project_path()+'config.ini') #第二步解析
    return config.get('main_url', 'url')  # 第三步读取,获取指定section的指定名称内容，以=形式

if __name__ == '__main__':
    print(project_path())
    print(login_url())
    print(main_url())

