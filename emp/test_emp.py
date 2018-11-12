import requests
import unittest
import json
import random
from comm.login import testlogin_001
from comm.Log import Logger

#请求头信息
token = testlogin_001().test_emplogin('token')
print(token)

# emp公共登陆组件


headers = {
    'cache-control': 'no-cache',
    'Host': 'emp.hnjing.com',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3554.0 Safari/537.36',
    'Content-Type': 'application/json',
    'Refere': 'http://emp.hnjing.com/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'token': token
}

url = "http://emp.hnjing.com/emp_os/v1/organs?pageNum=1&pageSize=20"
# oragnname = "中天控股集团有限公司"
print(url)
oragn_check = requests.get(url, headers=headers).text
print(oragn_check)

