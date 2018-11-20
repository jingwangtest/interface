# -*- coding: utf-8 -*-
# @Time    : 2018/3/18 09:36
# @Author  : jt

import requests
import unittest
import json
import random
from comm.public_data import MySQL
from comm.login import testlogin_001
from comm.Log import Logger

# 请求头信息
# token = testlogin_001().test_culogin('token')
# print(token)
# # 指定头文件
# headers = {
#     'Content-Type': 'application/json;charset=UTF-8',
#     'token': token
# }


#
class empA01(unittest.TestCase):
    # 用户运营-企业客户管理-企业审核不通过-删除
    def test_b007_search(self):
        params = {'mobilePhone': '13025406605', 'password': '123456', 'remember': True, 'siteName': 'main'}
        url = "http://cu.ejw.cn"

        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0',
            'Accept - Encoding': 'gzip, deflate',
            'Accept - Language': 'zh - CN, zh;q = 0.9',
            'Referer': 'http://www1.ejw.cn/auth/?backUrl=http%3A%2F%2Fcp.ejw.cn%2F%23%2F',
            'X-Requested-With': 'XMLHttpRequest'
        }
        print(headers)
        # r1 = requests.post(url, data=json.dumps(params), headers=headers).text
        # print('新增成功')
        token_act = requests.post(url, data=json.dumps(params), headers=headers).status_code
        print(token_act)
        token_exp = 200
        self.assertEqual(token_exp, token_act)


if __name__ == '__main__':
    unittest.main()

