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
token = testlogin_001().test_splogin('token')
log = Logger(logger="服务商平台").getlog()
log_exp = Logger(logger="服务商平台_预期结果").getlog()
log_act = Logger(logger="服务商平台_实际结果").getlog()
# 指定头文件
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'token': token
}


class Cpgl_cpsxj(unittest.TestCase):
    # 店铺管理-产品管理-供应商授权管理-详情
    def test_c010_product_verify(self):
        url = "http://sp.ejw.cn/os/v1/partners?partnerId=190"
        result_act = requests.get(url, headers=headers)
        result_exp = 200
        self.assertEqual(result_exp, result_act.status_code, msg="查看详情存在异常情况")
        log_act.info(result_act.text)



if __name__ == '__main__':
    unittest.main()
