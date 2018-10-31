# 服务商平台
import requests
import random
import json
import unittest
from comm.login import testlogin_001
import readConfig as readConfig
from comm.public_data import MySQL
from comm.Log import Logger
from urllib.parse import quote

localReadConfig = readConfig.ReadConfig()
token = testlogin_001().test_cplogin('token')
log = Logger(logger="供应商平台").getlog()
log_exp = Logger(logger="供应商平台_预期结果").getlog()
log_act = Logger(logger="供应商平台_实际结果").getlog()
# 指定头文件
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'token': token
}


class Cpgl_cpsxj(unittest.TestCase):
    # 验证登陆是否成功
    def test_a001_login(self):
        global log, log_exp, log_act
        log_exp = Logger(logger="供应商平台_预期结果").getlog()
        log_act = Logger(logger="供应商平台_实际结果").getlog()
        log = Logger(logger="供应商平台").getlog()
        params = {'mobilePhone': '15574841920', 'password': '123456', 'remember': 'true', 'siteName': 'main'}
        url = localReadConfig.get_http_cp('url_cp')

        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0',
            'Accept - Encoding': 'gzip, deflate',
            'Accept - Language': 'zh - CN, zh;q = 0.9',
            'Referer': 'http://www1.ejw.cn/auth/?backUrl=http%3A%2F%2Fadmin.ejw.cn%2F%23%2F',
            'X-Requested-With': 'XMLHttpRequest'
        }
        token_act = requests.post(url, data=json.dumps(params), headers=headers)
        result_exp = 200
        result_act = token_act.status_code
        self.assertEqual(result_exp, result_act, msg="用户登陆失败")
        log_exp.info(result_exp)
        log_act.info(result_act)
        log.info("用户登陆成功")


if __name__ == '__main__':
    unittest.main()
