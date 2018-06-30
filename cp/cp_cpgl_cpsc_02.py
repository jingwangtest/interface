import requests
import unittest
import readConfig as readConfig
import json
from comm.login import testlogin_001

localReadConfig = readConfig.ReadConfig()
# url = localReadConfig.get_http('url')
token_01 = testlogin_001().test_login_001('token')
name = "%自动化测试%"


class Cpgl_cpsxj(unittest.TestCase):
    # 智营销平台-组织架构管理-部门员工管理-按已存在的姓名查询
    def test_a003_bmyg_serach(self):
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'token': token_01
        }
        url = "http://cp.ejw.cn/cp/v1/partner/277/employees?jobNoOrEmpName=xcebdj&pageNo=1&pageSize=10&sort=%7B%22gmtCreate%22%3A%22desc%22%7D"
        result = requests.get(url, headers=headers).text
        result_01 = json.loads(result)
        result_act = result_01["data"][0]["empName"]
        result_exp = 'xcebdj'
        if result_exp == result_act:
            print("用户xcebdj查询成功")
        else:
            print("没有查询到此用户")

    # 智营销平台-组织架构管理-部门员工管理-不存在的姓名查询
    def test_a004_bmyg_serach(self):
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'token': token_01
        }
        url = "http://cp.ejw.cn/cp/v1/partner/277/employees?jobNoOrEmpName=xxxxx&pageNo=1&pageSize=10&sort={'gmtCreate': 'desc'}"
        print(url)
        result = requests.get(url, headers=headers).text
        result_01 = json.loads(result)
        print(result_01)
        data = result_01["data"]
        print(data)
        # 设置预期条件
        if len(data) == 0:
            print("没有此用户的查询信息，查询检验成功")
        else:
            print("查询核验失败")


if __name__ == '__main__':
    unittest.main()
