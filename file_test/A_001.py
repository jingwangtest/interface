# -*- coding: utf-8 -*-
# @Time    : 2018/3/18 09:36
# @Author  : jt

import requests
import unittest
import json
import random
import os
import datetime
from comm.public_data import MySQL
from cc.cc_login import cc001

# 请求头信息
token = cc001().cc_login('token')
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'token': token
}

# 连接openapi数据库获取已授权的企业
conn = MySQL().connect_open_api()
cur1 = conn.cursor()
# cur1.execute('select partner_id, partner_name from app_comp_auth where status = 1')
cur1.execute('select t1.partner_id,t2.partner_name from app_comp_auth t1 left join os_partner t2 on t1.partner_id = t2.partner_id where t1.status = 1;')
partner1 = cur1.fetchall()
print(type(partner1), len(partner1), partner1)
# 连接empos数据库获取已关联机构企业
# conn = MySQL().connect_emp_os()
# cur2 = conn.cursor()
# cur2.execute('select partner_id from organ where deleted = 1')
# partner2 = cur2.fetchall()
#
# s = tuple(set(partner1) - set(partner2))
# s_test = str(s[0][0])
