import requests
import unittest
import json
import random
from emp.login_emp import testlogin_001
from comm.public_data import MySQL

# 请求头信息
token = testlogin_001().emplogin('token')
headers = {
    'cache-control': 'no-cache',
    'Host': 'emp.hnjing.com',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3554.0 Safari/537.36',
    'Content-Type': 'application/json',
    'Refere': 'http://emp.hnjing.com/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'token': token
}


class emp_01(unittest.TestCase):
    # 系统管理-组织管理-机构管理-新增机构
    # def test_oragn_001(self):
    # organName = '长沙伊特诺教育咨询有限公司'
    # url = "http://emp.hnjing.com/emp_os/v1/organ"
    # params = {"organName":"长沙伊特诺教育咨询有限公司","sharesType":0,
    #          "oragnShortName":"教育咨询","oragnShortEname":"zixun","partnerId":190,"creator":68}
    # organ_add = requests.post(url,data=json.dumps(params),headers=headers)
    # result_add = organ_add.text
    # result_exp = 1
    # self.assertIn(result_exp,int(result_add))
    # print("新增机构成功")

    # 系统管理-组织管理-机构管理-查询机构
    def test_oragn_002(self):
        url_dz = "http://emp.hnjing.com/emp_os/v1/organs?pageNum=1&pageSize=20&organName="
        oragnname = "中天控股集团有限公司"
        url = url_dz + oragnname
        print(url)
        oragn_check = requests.get(url, headers=headers)
        result = oragn_check.text
        self.assertIn(oragnname, result)
        print("查询成功")

    # 系统管理-组织管理-组织架构-新增部门
    def test_department_001(self):
        url = "http://emp.hnjing.com/emp_os/v1/department"
        # deptName01 = ''.join(random.sample(['1', '4', '3', '2', '5', '6'], 3))
        # deptNmame02 = '新增部门张'
        deptName = '新增部门张'
        params = {"departmentName": deptName, "departmentType": 0, "creator": "68", "absPath": "/93/", "parentId": 93}
        dept_add = requests.post(url, data=json.dumps(params), headers=headers)
        result_add = dept_add.text
        self.assertIn(deptName, result_add)
        print("新增部门成功")

    # 系统管理-组织管理-组织架构-删除部门
    def test_department_002(self):
        # 连接数据库
        conn = MySQL().connect_empos('conn')
        cur = conn.cursor()
        cur.execute(
            'select department_id,department_name from department where department_type = 0 and deleted = 1 and department_name = "新增部门张" ')
        dept = cur.fetchone()[0:2]
        dept_id = str(dept[0])
        dept_name = dept[1]
        print(dept_id, dept_name)
        url_sc = "http://emp.hnjing.com/emp_os/v1/department/"
        url = url_sc + dept_id
        dept_sc = requests.delete(url, headers=headers)
        result_sc = json.loads(dept_sc.text)
        values = result_sc["rowNum"]
        result_exp = 1
        self.assertEqual(result_exp, values)
        print("部门删除成功")

    # 系统管理-组织管理-组织架构-编辑部门
    def test_department_003(self):
        # 连接数据库
        conn = MySQL().connect_empos('conn')
        cur = conn.cursor()
        cur.execute('select department_id,department_name from department ')
        dept = cur.fetchone()[0:2]
        dept_id = str(dept[0])
        dept_name = dept[1]
        print(dept_id, dept_name)
        url_bj = "http://emp.hnjing.com/emp_os/v1/department/"
        url = url_bj + dept_id
        # 编辑后名称
        deptName01 = ''.join(random.sample(['1', '4', '3', '2', '5', '6'], 3))
        deptNmame02 = '技术中心'
        deptName = deptNmame02 + deptName01
        params = {"modifier": 68, "departmentName": deptName}
        dept_bj = requests.put(url, data=json.dumps(params), headers=headers)
        result_bj = json.loads(dept_bj.text)
        values = result_bj["rowNum"]
        result_exp = 1
        self.assertEqual(result_exp, values)
        print("部门编辑成功")

    # 系统管理-组织管理-组织架构-新增岗位
    def test_station_001(self):
        url = "http://emp.hnjing.com/emp_os/v1/station"
        stationName01 = ''.join(random.sample(['1', '4', '3', '2', '5', '6'], 3))
        stationName02 = '新增岗位林'
        stationName = stationName02 + stationName01
        params = {"stationName": stationName, "stationType": "0", "departmentId": 95, "creator": "68"}
        station_add = requests.post(url, data=json.dumps(params), headers=headers)
        result_add = json.loads(station_add.text)
        values = result_add["rowNum"]
        result_exp = 1
        self.assertEqual(result_exp, values)
        print("新增岗位成功")

    # 系统管理-组织管理-组织架构-编辑岗位
    def test_station_002(self):
        # 连接数据库
        conn = MySQL().connect_empos('conn')
        cur = conn.cursor()
        cur.execute('select station_id,station_name from station ')
        station = cur.fetchone()[0:2]
        station_id = str(station[0])
        station_name = station[1]
        print(station_id, station_name)
        url_bj = "http://emp.hnjing.com/emp_os/v1/station/"
        url = url_bj + station_id
        # 编辑后名称
        stationName01 = ''.join(random.sample(['1', '4', '3', '2', '5', '6'], 3))
        stationName02 = '测试岗位林'
        stationName = stationName02 + stationName01
        params = {"stationName": stationName, "stationType": "0", "departmentId": 95, "modifier": "68"}
        station_bj = requests.put(url, data=json.dumps(params), headers=headers)
        result_bj = json.loads(station_bj.text)
        print(result_bj)
        values = result_bj["rowNum"]
        result_exp = 1
        self.assertEqual(result_exp, values)
        print("岗位编辑成功")


if __name__ == '__main__':
    unittest.main()
