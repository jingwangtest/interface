# 营销管理系统
from selenium import webdriver
import time
import unittest
import json
import requests
import pymysql
import os
import random
# from public.logger import Logger
# from selenium.webdriver.common.keys import Keys

# 全量变量
url = "http://www1.ejw.cn/api/login"
# logger = Logger(logger='智平台测试').getlog()

# 登录
param1 = {'mobilePhone': '18600000000', 'password': '123456', 'remember': 'true', 'siteName': 'main'}

# 请求头信息
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'User-Agent':  'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0',
    'Accept - Encoding': 'gzip, deflate',
    'Accept - Language': 'zh - CN, zh;q = 0.9',
    'Referer': 'http://www1.ejw.cn/auth/?backUrl=http%3A%2F%2Fadmin.ejw.cn%2F%23%2F',
    'X-Requested-With': 'XMLHttpRequest'
}
# 发送登陆请求接口
r1 = requests.post(url, data=json.dumps(param1), headers=headers)
# 获取返回值结果
s = json.loads(r1.text)
# 获取token值
token = s["data"]["access_token"]

# 请求下单功能
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'token': token
}
print(headers)
# 请求参数
url = 'http://admin.ejw.cn/platform/v1/partnerall'
parms = {"partner": {"partnerType": "0101", "partnerName": "长沙艾客美食文化传播有限公司", "area": "湖南/长沙",
                    "address": "岳麓麓谷高新产业区", "phone": "0731-77777777", "level": 0, "detail": "湖南竞科技"},
         "partnerBusiness": {"uscCode": "91430104MA4M2RXY79", "beginDate": "2017-09-01", "validDate": "2067-08-31",
                             "companyType": "有限责任公司(自然人投资或控股)", "registAddress":"湖南省长沙市岳麓区岳麓街道潇湘中路328号麓枫和苑1008-1010房（集群注册）",
                             "legalPerson": "樊润霞", "registAuthority": "长沙市工商行政管理局岳麓分局", "approvalDate": "2017-09-01","registStatus": "存续（在营、开业、在册）",
                             "registCapital": 50, "scope": "存续（在营、开业、在册）", "legalPersonIdcode": "430624199012345678"},
         "partnerExt": {"standardIndustry": "552", "category": "58"}, "partnerQualifys": [{"qualifyType": 1,
                                                                                           "qualifyImage": "http://hnjing-test.bj.bcebos.com/v1/hnjing-test/9a5d4e1dc042404dbdefc10fa0a5c61f.jpg",
                                                                                           "qualifyName": "营业执照", "qualifyBeginDate": "2017-09-01", "qualifyValidDate": "2067-08-31"},
                                                                                          {"qualifyType": 2, "qualifyImage": "http://hnjing-test.bj.bcebos.com/v1/hnjing-test/8e44bf143da344f08702992b2d8a9d3b.jpg,http://hnjing-test.bj.bcebos.com/v1/hnjing-test/0d177f79f7ea46779f6de692395f4eff.jpg",
                                                                                           "qualifyName": "法人身份证", "qualifyBeginDate": "2018-05-31", "qualifyValidDate": "2018-05-31"}], "employees": {"empName": "竞网科技有限公司", "phone": "13025406605", "email": "15814405932@139.com"}}
values = json.dumps(parms)
# 发送服务商接口请求
fws_test = requests.post(url, data=values, headers=headers).text
# 返回状态码信息
respon_act = requests.post(url, data=values, headers=headers).status_code
print(respon)
# s = json.loads(fws_test)          赋值所有的结果值
# att = s["partner"]["partnerName"] 此消息获取json下的用户字段值
respon_exp = 200

if __name__ == '__main__':
    unittest.main()
