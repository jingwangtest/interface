# -*- coding: utf-8 -*-
# @Time    : 2018/3/18 09:36
# @Author  : jt

import requests
import json
import readConfig as readConfig
localReadConfig = readConfig.ReadConfig()


class Zpt:
    # cp公共登陆组件
    @staticmethod
    def cp_login():
        url = localReadConfig.get_http_cp()
        username = localReadConfig.read_cp_login()
        params = {'mobilePhone': username, 'password': '123456', 'remember': True, 'siteName': 'main'}

        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0',
            'Accept - Encoding': 'gzip, deflate',
            'Accept - Language': 'zh - CN, zh;q = 0.9',
            'Referer': 'http://www.ejw.cn/auth/?backUrl=http%3A%2F%2Fcp.ejw.cn%2F%23%2F',
            'X-Requested-With': 'XMLHttpRequest'
        }
        print(headers)
        # r1 = requests.post(url, data=json.dumps(params), headers=headers).text
        # print('新增成功')
        token_act = requests.post(url, data=json.dumps(params), headers=headers)
        print(token_act)
        s = json.loads(token_act.text)
        values = s["data"]["access_token"]
        return values

    # sp公共登陆组件
    @staticmethod
    def sp_login():
        url = localReadConfig.get_http_sp()
        username = localReadConfig.read_sp_login()
        params = {'mobilePhone': username, 'password': '123456', 'remember': True, 'siteName': 'main'}
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0',
            'Accept - Encoding': 'gzip, deflate',
            'Accept - Language': 'zh - CN, zh;q = 0.9',
            'Referer': 'http://www.ejw.cn/auth/?backUrl=http%3A%2F%2Fsp.ejw.cn%2F%23%2F',
            'X-Requested-With': 'XMLHttpRequest'
        }
        print(headers)
        # r1 = requests.post(url, data=json.dumps(params), headers=headers).text
        # print('新增成功')
        token_act = requests.post(url, data=json.dumps(params), headers=headers)
        print(token_act)
        s = json.loads(token_act.text)
        values = s["data"]["access_token"]
        return values

    # cu公共登陆组件
    @staticmethod
    def cu_login():
        url = localReadConfig.get_http_cu()
        username = localReadConfig.read_cu_login()
        params = {'mobilePhone': username, 'password': '123456', 'remember': True, 'siteName': 'main'}
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0',
            'Accept - Encoding': 'gzip, deflate',
            'Accept - Language': 'zh - CN, zh;q = 0.9',
            'Referer': 'http://www.ejw.cn/auth/?backUrl=http%3A%2F%2Fcu.ejw.cn%2F%23%2F',
            'X-Requested-With': 'XMLHttpRequest'
        }
        print(headers)
        # r1 = requests.post(url, data=json.dumps(params), headers=headers).text
        # print('新增成功')
        token_act = requests.post(url, data=json.dumps(params), headers=headers)
        # print(token_act)
        s = json.loads(token_act.text)
        values = s["data"]["access_token"]
        return values

    # admin公共登陆组件
    @staticmethod
    def test_admin_login():
        url = localReadConfig.get_http_admin()
        username = localReadConfig.read_admin_login()
        params = {'mobilePhone': username, 'password': '123456', 'remember': True, 'siteName': 'main'}

        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0',
            'Accept - Encoding': 'gzip, deflate',
            'Accept - Language': 'zh - CN, zh;q = 0.9',
            'Referer': 'http://www1.ejw.cn/auth/?backUrl=http%3A%2F%2Fadmin.ejw.cn%2F%23%2F',
            'X-Requested-With': 'XMLHttpRequest'
        }
        print(headers)
        # r1 = requests.post(url, data=json.dumps(params), headers=headers).text
        # print('新增成功')
        token_act = requests.post(url, data=json.dumps(params), headers=headers)
        print(token_act)
        s = json.loads(token_act.text)
        values = s["data"]["access_token"]
        return values

    # www1公共登陆组件
    @staticmethod
    def test_www_login():
        url = localReadConfig.get_http_www()
        username = localReadConfig.read_www_login()
        params = {"mobilePhone": username, "password": "123456", "remember": True, "siteName": "main"}
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0',
            'Accept - Encoding': 'gzip, deflate',
            'Accept - Language': 'zh - CN, zh;q = 0.9',
            'Referer': 'http://www1.ejw.cn/auth/?backUrl=http%3A%2F%2Fwww1.ejw.cn%2F%23%2F',
            'X-Requested-With': 'XMLHttpRequest'
        }
        token_act = requests.post(url, data=json.dumps(params), headers=headers)
        s = json.loads(token_act.text)
        values = s["data"]["access_token"]
        return values

    # www1公共登陆组件
    @staticmethod
    def user_login():
        url = localReadConfig.get_http_user()
        username = localReadConfig.read_sp_login()
        params = {"mobilePhone": username, "password": "123456", "remember": True, "siteName": "main"}
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0',
            'Accept - Encoding': 'gzip, deflate',
            'Accept - Language': 'zh - CN, zh;q = 0.9',
            'Referer': 'http://user.ejw.cn/auth/?backUrl=http%3A%2F%2Fwww.ejw.cn%2F%23%2F',
            'X-Requested-With': 'XMLHttpRequest'
        }
        token_act = requests.post(url, data=json.dumps(params), headers=headers)
        s = json.loads(token_act.text)
        values = s["data"]["access_token"]
        return values

    # emp公共登陆组件
    @staticmethod
    def test_emp_login():
        url = localReadConfig.get_http_emp()
        username = localReadConfig.read_emp_login()
        params = {"mobilePhone": username, "password": "123456", "remember": True, "siteName": "main"}
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'user-id': '3',
            'Host': 'auth.ejw.cn',
            'Origin': 'http://auth.ejw.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3554.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept - Encoding': 'gzip, deflate',
            'Accept - Language': 'zh - CN, zh;q = 0.9',
            'Referer': 'http://auth.ejw.cn/auth/?backUrl=http%3A%2F%2Femp.ejw.cn%2F%23%2F',
            'X-Requested-With': 'XMLHttpRequest'
        }
        token_act = requests.post(url, data=json.dumps(params), headers=headers)
        s = json.loads(token_act.text)
        # print(s)
        values = s["data"]["access_token"]
        return values

