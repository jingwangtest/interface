# -*- coding: utf-8 -*-
# @Time    : 2018/3/18 09:36
# @Author  : jt

import requests
import unittest
import json
a = True
params = {"mobilePhone": "13588880003", "password": "123456", "remember": a, "siteName": "main"}
url = "http://auth.ejw.cn/api/login"

headers = {
    'Host': 'auth.ejw.cn',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '92',
    'Origin': 'http://auth.ejw.cn',
    'Content-Type': 'application/json;charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3554.0 Safari/537.36',
    'Referer': 'http://auth.ejw.cn/?backUrl=http%3A%2F%2Fcu.ejw.cn%2F%23%2F',
    'X-Requested-With': 'XMLHttpRequest',
    'token': 'null',
    'user-id': ''
}

print(headers)
# r1 = requests.post(url, data=json.dumps(params), headers=headers).text
# print('新增成功')
token_act = requests.post(url, data=json.dumps(params), headers=headers)
print(token_act)
print(token_act.status_code)
# s = json.loads(token_act.text)
# values = s["data"]["access_token"]
# print(values)
