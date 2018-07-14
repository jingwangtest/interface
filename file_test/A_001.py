# 运营平台-合作伙伴管理
import requests
import random
import json
import unittest
from comm.login import testlogin_001
from comm.public_data import MySQL

# 请求头信息
token = testlogin_001().test_adminlogin('token')
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'token': token
}


class admin_yygl(unittest.TestCase):
    # 运营管理-合作伙伴管理-存在的查询
    def test_a004_search(self):
        conn = MySQL().connect_os1('conn')
        cur = conn.cursor()
        cur.execute("select partner_name from partner")
        parnername = str(cur.fetchone()[0])
        print(parnername)
        url_01 = 'http://admin.ejw.cn/os/v1/partners?pageSize=10&pageNo=1&partnerType=0010%2C0011%2C0100%2C0101%2C0111%2C0110&partnerName='
        url = url_01 + parnername
        # 发送服务商接口请求
        qykh_test_01 = requests.get(url, headers=headers)
        qykh_test = qykh_test_01.text
        print(qykh_test)
        # 返回状态码信息
        totalCount = qykh_test.split("startRow", 2)[1].split(",", 2)[1].split(":", 2)[1]
        print(totalCount)
        # 判断当前返回码及字段值
        result_act = int(totalCount)
        result_exp = 1
        self.assertEqual(result_exp, result_act, "查询的日志结果不一致")




if __name__ == '__main__':
    unittest.main()
