import unittest
import requests
import json
from comm.login import testlogin_001

# 获取配置文件地址url
# localReadConfig = readConfig.ReadConfig()
token_01 = testlogin_001().test_www1login('token')

class cc001(unittest.TestCase):
    # 验证登陆是否成功
    def test_a001_login(self):
        params = {"mobilePhone": "18511338082", "password": "123456", "remember": "true", "siteName": "main"}
        # url = localReadConfig.get_http_cp('url_cp')
        url = "http://www1.ejw.cn/api/login"
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0',
            'Accept - Encoding': 'gzip, deflate',
            'Accept - Language': 'zh - CN, zh;q = 0.9',
            'Referer': 'http://www1.ejw.cn/auth/?backUrl=http%3A%2F%2Fwww1.ejw.cn%2F%23%2F',
            'X-Requested-With': 'XMLHttpRequest'
        }
        token_act = requests.post(url, data=json.dumps(params), headers=headers)
        result_exp = 200
        result_act = token_act.status_code
        self.assertEqual(result_exp, result_act, msg="用户登陆失败")
        print("用户登录成功")
        # global log, log_exp, log_act
        # log_exp = Logger(logger="供应商平台_预期结果").getlog()
        # log_act = Logger(logger="供应商平台_实际结果").getlog()
        # log = Logger(logger="供应商平台").getlog()
        # log_exp.info(result_exp)
        # log_act.info(result_act)
        # log.info("用户登陆成功")

    # 验证创建工单是否成功
    def test_a002_login(self):
        params = {"action": "2", "orderType": "14", "customerName": "", "customerId": "", "contactName": "张胜男", "customerTel": "18511338082", "contactTime": "2018-07-16 17:05:21", "contactType": "1", "serviceType": "consulting", "subServiceType": "consulting3", "serviceObj": "1", "actualDispose": "", "content": "工单管理中创建一个cc工单", "fileList": [], "limitHour": "3", "skillGroup": 27, "disposeUserId": 1725, "projectId": "31"}
        # url = localReadConfig.get_http_cp('url_cp')
        url = "http://192.168.150.105:8054/cc/v1/ticket"
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'token': token_01
        }
        token_act = requests.post(url, data=json.dumps(params), headers=headers)
        print(token_act)
        result_exp = 200
        result_act = token_act.status_code
        self.assertEqual(result_exp, result_act, msg="创建工单失败")
        print("创建工单成功")
        # global log, log_exp, log_act
        # log_exp = Logger(logger="供应商平台_预期结果").getlog()
        # log_act = Logger(logger="供应商平台_实际结果").getlog()
        # log = Logger(logger="供应商平台").getlog()
        # log_exp.info(result_exp)
        # log_act.info(result_act)
        # log.info("用户登陆成功")


if __name__ == '__main__':
    unittest.main()