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
from selenium.webdriver.common.keys import Keys

# 全量变量
url = "http://www1.ejw.cn/api/login"
# logger = Logger(logger='智平台测试').getlog()

# 登录
param1 = {'mobilePhone': '18600000000', 'password': '123456', 'remember': 'true', 'siteName': 'main'}
#r2 = requests.post("http://admin.ejw.cn")

headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'User-Agent':  'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0',
    'Accept - Encoding': 'gzip, deflate',
    'Accept - Language': 'zh - CN, zh;q = 0.9',
    'Referer': 'http://www1.ejw.cn/auth/?backUrl=http%3A%2F%2Fadmin.ejw.cn%2F%23%2F',
    'X-Requested-With': 'XMLHttpRequest'
}

r1 = requests.post(url, data=json.dumps(param1), headers=headers)
# r1 = requests.post(url, data=param1, headers=headers)
print(r1)
s = json.loads(r1.text)
print(s)
token = s["data"]["access_token"]
print(token)