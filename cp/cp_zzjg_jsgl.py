import requests
import random
import json
import unittest
from comm.login import testlogin_001

token = testlogin_001().test_cplogin('token')


class cp_zzjg_jsgl_01(unittest.TestCase):
    # 智营销平台-组织架构管理-角色管理
    def test_a001_role_add(self):
        name_02 = ''.join(random.sample(['a', 'b', 'c', 'd', 'e', '1', '5', '6', 'x', 'aaa'], 6))
        name_01 = '自动化测试角色'
        Name = name_01 + name_02
        print(Name)
        url = "http://cp.ejw.cn/os/v1/partner/277/role"
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json;charset=UTF-8',
            'token': token
        }
        params = {"roleName": Name, "appName": "cp"}
        # print(params)
        role_code_act = requests.post(url, data=json.dumps(params), headers=headers).status_code
        role_code_exp = 200
        self.assertEqual(role_code_exp, role_code_act)
        print("角色新增成功")

    # 智营销平台-组织架构管理-部门员工管理-新增
    def test_a002_bmyg_add(self):
        empName = ''.join(random.sample(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'j'], 6))
        jobNo = ''.join(random.sample(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], 6))
        mobile_02 = ''.join(random.sample(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], 8))
        mobile_01 = '131'
        mobile = mobile_01 + mobile_02
        mail_01 = '@qq.com'
        mail = mobile + mail_01
        params = [{"roles": [771], "departments": [{"depId": 203, "position": 2}], "empName": empName, "jobNo": jobNo,
                   "email": mail, "phone": mobile, "status": 1,
                   "entryDate": "2018-05-02T16:00:00.000Z"}]
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'token': token
        }
        url = "http://cp.ejw.cn/cp/v1/partner/277/employees"
        result_exp = requests.post(url, data=json.dumps(params), headers=headers).status_code
        result_act = 200
        self.assertEqual(result_exp, result_act)
        print("新增部门管理成功")

    # 智营销平台-组织架构管理-部门员工管理-按已存在的姓名查询
    def test_a003_bmyg_serach(self):
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'token': token
        }
        url = "http://cp.ejw.cn/cp/v1/partner/277/employees?jobNoOrEmpName=xcebdj&pageNo=1&pageSize=10&sort=%7B%22gmtCreate%22%3A%22desc%22%7D"
        result = requests.get(url, headers=headers).text
        result_01 = json.loads(result)
        result_act = result_01["data"][0]["empName"]
        result_exp = 'xcebdj'
        self.assertEqual(result_exp, result_act)
        print("预期结果与实际结果一致")

    # 智营销平台-组织架构管理-部门员工管理-不存在的姓名查询
    def test_a004_bmyg_serach(self):
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'token': token
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
