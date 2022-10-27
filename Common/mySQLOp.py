# --------------------------------------------------
# !/usr/bin/python
# -*- coding: utf-8 -*-
# PN: DBInterface
# FN: mySQLOp
# Author: xiaxu
# DATA: 2021/11/16
# Description:mysql操作得封装
# ---------------------------------------------------
import pymysql,time


class Singleton:
    '''单例模式，只能建立一个对象'''
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            # 重写new方法，当发现已经有实例时，直接返回实例，没有才创建
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
class MySQLOP(Singleton):
    '''
    对数据库操作的类
    '''
    def __init__(self):
        ip = '172.16.32.115'
        port = 3308
        user = 'root'
        psw = 'PSPS2053'
        db = 'wddb20'
        self.conn = pymysql.connect(host=ip,port = port ,user=user, passwd=psw,db=db,autocommit='True')
        self.conn.ping()#不同时返回异常

    def select_table(self,tablename):
        '''
        查询数据操作
        :return:
        '''
        try:
            self.conn.ping()
            data_tuple = ()
            with self.conn.cursor() as cursor:   #使用上下问管理器，不用cursor。close()
                sql = 'SELECT * from {tablename}'\
                    .format(tablename = tablename)
                cursor.execute(sql)
                data_tuple = cursor.fetchall()  #返回所有的记录
        except Exception as e:
            print(e)
        finally:
            return data_tuple
    def truncate_tables(self,*args):
        try:
            with self.conn.cursor() as cursor:  # 使用上下问管理器，不用cursor。close()
                for i in args[0]:
                    sql = 'truncate table {table_name}'.format(table_name = i[0])#传入时将其变成元组
                    cursor.execute(sql)  #
        finally:
            print('执行清空表完成')

    def truncate_table(self,*args):
        try:
            with self.conn.cursor() as cursor:  # 使用上下问管理器，不用cursor。close()
                for i in args:
                    sql = 'truncate table {table_name}'.format(table_name = i)  # 传入时将其变成元组
                    cursor.execute(sql)  #
                    print('清空表完成')
        except Exception as e:
            print('清空表发生异常',e)



if __name__ == '__main__':
    sql = MySQLOP()
    sql.truncate_table('csm_mnl_dyp')
