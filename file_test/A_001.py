# 运营平台-合作伙伴管理
import requests
import random
import json
import unittest
from comm.login import Zpt
from comm.public_data import MySQL
from comm.Log import Logger
from urllib.parse import quote
import readConfig
import time


# 请求头信息
localReadConfig = readConfig.ReadConfig()
token = Zpt().test_admin_login()
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'token': token
}
cuComId = localReadConfig.read_cu_com_id()
cuComName = localReadConfig.read_cu_com_name()
cuEmpId = localReadConfig.read_cu_emp_id()
cuEmpName = localReadConfig.read_cu_emp_name()
adminEmpId = localReadConfig.read_admin_emp_id()
spId = localReadConfig.read_sp_com_id()

# # coding:utf-8
# a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
#
# # 用列表生成式，生成新的列表
# b = [i for i in a if i > 0]
# print(b)
# print("大于0的个数：%s" % len(b))
#
# # 字符串切片
# a = "axbyczdjf"
# print(a[::2])

conn = MySQL.connect_mall()
cur = conn.cursor()
sql = "select t.product_uuid, t.product_spec_uuid from shoping_info t where t.sp_id=" + spId + " and emp_id=" + \
      cuEmpId
cur.execute(sql)
sql_result = cur.fetchone()[0:2]
productUuid = sql_result[0]
productSpecUuid = sql_result[1]
url = "http://www.ejw.cn/shopingcart/" + cuComId
params = {"productUuid": productUuid, "productSpecUuid": productSpecUuid,
          "spId": int(spId),
          "compId": int(cuComId), "empId": int(cuEmpId)}
print(params)


