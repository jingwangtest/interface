# -*- coding: utf-8 -*-
# @Time    : 2018/3/18 09:36
# @Author  : jt

# 服务商平台
import requests
import random
import json
import unittest
import pymysql
from comm.login import Zpt
from comm.public_data import MySQL
from comm.Log import Logger
import readConfig as readConfig

token = Zpt().cp_login()
localReadConfig = readConfig.ReadConfig()

cpComId = localReadConfig.read_cp_com_id()
cpComName = localReadConfig.read_cp_com_name()
cpEmpId = localReadConfig.read_cp_emp_id()
cpEmpName = localReadConfig.read_cp_emp_name()

#
# # 指定头文件
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'token': token
}
# #
# # 在配置文件下面读取mysql数据库
# host = localReadConfig.get_db_host()
# print(host)
# port = int(localReadConfig.get_db_port())
# print(port, type(port))
# username = localReadConfig.get_db_username()
# print(username, type(username))
# # password = 'hnjing&@test'
# password = localReadConfig.get_db_password()
# print(password, type(password))
# charset = 'utf8'
#
#
# ps = localReadConfig.get_db_ps()
# conn = pymysql.connect(
#     host=host,
#     port=port,
#     user=username,
#     passwd=password,
#     db=ps,
#     charset=charset
# )
#
# # 创建一个游标对象
# cur = conn.cursor()
# # order = "order by create_time desc"
# date_01 = '2018-05-02 00:00:00'
# sql_03 = 'and t.create_date < "2019-05-02 23:59:59"'
# sql_01 = " order by create_date desc"
# sql_02 = 'select t.cp_product_name from cp_product t where t.cp_partner_id=502 and t.create_date > "' + date_01 + '" '
# # 拼接sql语句
# sql = sql_02 + sql_03 + sql_01
# # print(sql)
# # 执行sql命令
# cur.execute(sql)
# # 取当前游标productName数据
# totalCount_act = cur.fetchone()[0]
# print(totalCount_act)


name_02 = ''.join(random.sample(['a', 'b', 'c', 'd', 'e', '1', '5', '6', 'x'], 6))
name_01 = '供_自动化测试勿删'
productName = name_01 + name_02
# 请求下单功能
url = "http://cp.ejw.cn/cp/v1/partner/" + cpComId + "/product?curEmpId=" + cpEmpId
parms = {"typeId": 136, "productInfo": "<p>塑料袋</p>",
         "images": "https://bj.bcebos.com/v1/hnjing-test/cb4ef37d38ff46c8bc74fdfc2bed6899.jpg",
         "qualification": "135", "tempStatus": "1", "flowId": 135, "specMinPrice": 0.1, "specMaxPrice": 0.1,
         "cpPartnerName": cpComName, "buyType": "0", "cpCommonAttrInfos": [
        {"cpCommonAttrId": None, "attrFormType": "text", "attrLayerType": "2", "attrIsValid": "1",
         "required": "1", "attrOrder": None, "attrType": "0", "attrValue": "", "fillValue": "颜色标准尺寸",
         "cpCommonAttrName": "域名描述", "isTemp": "1"},
        {"cpCommonAttrId": None, "cpCommonAttrName": "空间", "attrValue": "500M,1G,10G",
         "attrFormType": "checkbox", "attrLayerType": "1", "attrType": "1", "fillValue": "500M", "attrOrder": 2,
         "required": "1", "customAttrValue": "", "isTemp": "1"},
        {"cpCommonAttrId": None, "cpCommonAttrName": "域名", "attrValue": "中文域名,英文域名", "attrFormType": "checkbox",
         "attrLayerType": "1", "attrType": "1", "fillValue": "中文域名", "attrOrder": 1, "required": "1",
         "customAttrValue": "", "isTemp": "1"}], "cpProductName": productName, "productSpecs": [
        {"specSort": 0, "sellPrice": "0.10", "cpProductSpecAttrs": [{"attrValue": "500M", "attrName": "空间"},
                                                                    {"attrValue": "中文域名", "attrName": "域名"}]}]}
values = json.dumps(parms)
# 返回状态码信息
respon_act = requests.post(url, data=values, headers=headers)

print(respon_act.text)
