import unittest
import requests
import json
from comm.login import testlogin_001

# 获取配置文件地址url
# localReadConfig = readConfig.ReadConfig()
#token_01 = testlogin_001().test_www1login('token')

class cc001(unittest.TestCase):
    # 验证登陆是否成功
    def test_a001_login(self):
        params = {"mobilePhone": "18511338082", "password": "123456", "remember": True, "siteName": "main"}
        # url = localReadConfig.get_http_cp('url_cp')
        url = "http://auth.ejw.cn/api/login"
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'Accept - Encoding': 'gzip, deflate',
            'Accept - Language': 'en-US,en;q=0.9',
            'Referer': 'http://auth.ejw.cn/?backUrl=http%3A%2F%2F192.168.150.105%3A8057%2Fcc%2Fv1%2F%23%2F',
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

