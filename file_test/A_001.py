# -*- coding: utf-8 -*-
# @Time    : 2018/3/18 09:36
# @Author  : jt

import requests
import unittest
import json
import random
import os
from comm.public_data import MySQL
# from comm.login import testlogin_001
from comm.Log import Logger
#
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
# configPath = os.path.join(proDir, "config.ini")
configPath = "F:\python_script\interface\config.ini"
print(configPath)


cf = configparser.ConfigParser(allow_no_value=True)
cf.read(configPath, encoding='UTF-8')

value = cf.get("DATABASE", 'database_api1')
print(value)


#
# class empA01(unittest.TestCase):
#     # 用户运营-企业客户管理-企业审核不通过-删除
#     def test_b001_search(self):
#         # print('select department_id,department_name from department where department_type = 0 and deleted = 1 and department_name = "新增部门张" ')
#         conn = MySQL().connect_openapi()
#         cur = conn.cursor()
#         cur.execute("select * from api_info")
#         count = cur.fetchone()
#         print(count)
# if __name__ == '__main__':
#     ReadConfig1().get_db_ps()
