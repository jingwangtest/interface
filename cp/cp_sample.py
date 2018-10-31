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
    # 智营销平台-产品管理-产品名称查询
    def test_b002_cpmc_search(self):
        # 请求下单功能
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'token': token
        }
        # 请求查询参数
        product_name = "%自动化测试%"
        url = 'http://cp.ejw.cn/ps/v1/cpproducts?pageNum=1&pageSize=20&_sort=modifyDate%2Cdesc&cpPartnerId=502&cpProductName=%E8%87%AA%E5%8A%A8%E5%8C%96'
        result_all = requests.get(url, headers=headers).text
        result_json = json.loads(result_all)
        totalCount_exp = result_json["page"]["totalCount"]

        # 连接数据库创建一个游标对象
        conn = MySQL().connect_ps1("conn")
        cur = conn.cursor()
        cur.execute('select count(*) from cp_product t where t.cp_product_name like "' + product_name + '"')
        totalCount_act = cur.fetchone()[0]
        self.assertEqual(totalCount_exp, totalCount_act, "预期结果与实际结果不一致")
        log.info("已存在的产品名称验证成功")


if __name__ == '__main__':
    unittest.main()
