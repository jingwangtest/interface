import requests
import unittest
import json
import random
from emp.login_emp import Emp
from comm.public_data import MySQL

# 请求头信息
token = Emp().emp_login()
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
# 操作员工id
oper_id = '68'


class organ01(unittest.TestCase):
    # 系统管理-组织管理-机构管理-新增机构
    def test_a001oragn(self):
        # 连接openapi数据库获取已授权的企业
        conn = MySQL().connect_open_api()
        cur1 = conn.cursor()
        cur1.execute('select partner_id from app_comp_auth where status = 1')
        partner1 = cur1.fetchall()
        # 连接empos数据库获取已关联机构企业
        conn = MySQL().connect_emp_os()
        cur2 = conn.cursor()
        cur2.execute('select partner_id from organ where deleted = 1')
        partner2 = cur2.fetchall()
        vaules = tuple(set(partner1) - set(partner2))
        partner_id = str(vaules[0][0])
        print(partner_id)
        # 连接openapi库获取企业名称
        conn = MySQL().connect_open_api()
        cur3 = conn.cursor()
        cur3.execute('select partner_name from os_partner where partner_id = "' + partner_id + '" ')
        partnername = cur3.fetchone()[0]
        print(partnername)
        shortEname01 = "zidong"
        shortEname02 = ''.join(random.sample(['a', 'b', 'c', 'd', 'e', 'f', 'p', 'u'], 3))
        shortEname = shortEname01 + shortEname02
        shortname = partnername[0:5]
        print(shortname)
        url = "http://emp.hnjing.com/emp_os/v1/organ"
        params = {"organName": partnername, "sharesType": 0,
                  "oragnShortName": shortname, "oragnShortEname": shortEname, "partnerId": partner_id,
                  "creator": oper_id}
        organ_add = requests.post(url, data=json.dumps(params), headers=headers)
        result_add = json.loads(organ_add.text)
        print(result_add)
        result = result_add["rowNum"]
        result_exp = 1
        self.assertEqual(result_exp, result)
        print("新增机构成功")

    # 系统管理-组织管理-机构管理-查询机构
    def test_a002oragn(self):
        url_dz = "http://emp.hnjing.com/emp_os/v1/organs?pageNum=1&pageSize=20&organName="
        oragnname = "中天控股集团有限公司"
        url = url_dz + oragnname
        oragn_check = requests.get(url, headers=headers)
        result = oragn_check.text
        self.assertIn(oragnname, result)
        print("查询成功")

    # 系统管理-组织管理-组织架构-新增部门
    def test_b001dept(self):
        url = "http://emp.hnjing.com/emp_os/v1/department"
        # deptName01 = ''.join(random.sample(['1', '4', '3', '2', '5', '6'], 3))
        # deptNmame02 = '新增部门张'
        deptName = '新增部门张'
        params = {"departmentName": deptName, "departmentType": 0, "creator": oper_id, "absPath": "/93/",
                  "parentId": 93}
        dept_add = requests.post(url, data=json.dumps(params), headers=headers)
        result_add = dept_add.text
        self.assertIn(deptName, result_add)
        print("新增部门成功")

    # 系统管理-组织管理-组织架构-删除部门
    def test_b002dept(self):
        # 连接数据库
        conn = MySQL().connect_emp_os()
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
    def test_b003dept(self):
        # 连接数据库
        conn = MySQL().connect_emp_os()
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
        params = {"modifier": oper_id, "departmentName": deptName}
        dept_bj = requests.put(url, data=json.dumps(params), headers=headers)
        result_bj = json.loads(dept_bj.text)
        values = result_bj["rowNum"]
        result_exp = 1
        self.assertEqual(result_exp, values)
        print("部门编辑成功")

    # 系统管理-组织管理-组织架构-新增岗位
    def test_c001station(self):
        url = "http://emp.hnjing.com/emp_os/v1/station"
        # stationName01 = ''.join(random.sample(['1', '4', '3', '2', '5', '6'], 3))
        # stationName02 = '新增岗位林'
        stationName = '新增岗位林'
        params = {"stationName": stationName, "stationType": "0", "departmentId": 95, "creator": oper_id}
        station_add = requests.post(url, data=json.dumps(params), headers=headers)
        result_add = json.loads(station_add.text)
        values = result_add["rowNum"]
        result_exp = 1
        self.assertEqual(result_exp, values)
        print("新增岗位成功")

    # 系统管理-组织管理-组织架构-删除岗位
    def test_c002station(self):
        # 连接数据库
        conn = MySQL().connect_emp_os()
        cur = conn.cursor()
        cur.execute(
            'select station_id,station_name from station where station_type = 0 and deleted = 1 and station_name = "新增岗位林" ')
        stat = cur.fetchone()[0:2]
        stat_id = str(stat[0])
        stat_name = stat[1]
        print(stat_id, stat_name)
        url_sc = "http://emp.hnjing.com/emp_os/v1/station/"
        url = url_sc + stat_id
        stat_sc = requests.delete(url, headers=headers)
        result_sc = json.loads(stat_sc.text)
        values = result_sc["rowNum"]
        result_exp = 1
        self.assertEqual(result_exp, values)
        print("岗位删除成功")

    # 系统管理-组织管理-组织架构-编辑岗位
    def test_c003station(self):
        # 连接数据库
        conn = MySQL().connect_emp_os()
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
        params = {"stationName": stationName, "stationType": "0", "departmentId": 95, "modifier": oper_id}
        station_bj = requests.put(url, data=json.dumps(params), headers=headers)
        result_bj = json.loads(station_bj.text)
        print(result_bj)
        values = result_bj["rowNum"]
        result_exp = 1
        self.assertEqual(result_exp, values)
        print("岗位编辑成功")

    # 系统管理-组织管理-角色管理-新增角色
    def test_d001role(self):
        url = "http://emp.hnjing.com/emp_os/v1/role"
        roleName01 = "自动化角色"
        roleName02 = ''.join(random.sample(['1', '2', '3', '5', '7', '9', '8'], 3))
        roleName = roleName01 + roleName02
        params = {"roleName": roleName, "status": 1, "opIds": "3,4,5,6,1,2"}
        role_add = requests.post(url, data=json.dumps(params), headers=headers)
        result_add = str(role_add.text)
        result_exp = "添加角色成功"
        self.assertIn(result_exp, result_add)
        print("新增角色成功")

    # 系统管理-组织管理-角色管理-编辑角色（停用角色）
    def test_d002role(self):
        # 连接数据库获取role_id
        conn = MySQL().connect_emp_os()
        cur = conn.cursor()
        cur.execute('select role_id,role_name from role where role_name like "自动化角色%" and status = 1 ')
        role = cur.fetchone()[0:2]
        role_id = str(role[0])
        role_name = role[1]
        url_bj = "http://emp.hnjing.com/emp_os/v1/role/"
        url = url_bj + role_id
        params = {"roleId": role_id, "roleName": role_name, "status": 0, "opIds": "1,2,3,4,5,6"}
        role_bj = requests.put(url, data=json.dumps(params), headers=headers)
        result_bj = role_bj.text
        result_exp = "修改角色信息成功"
        self.assertIn(result_exp, result_bj)
        print("停用角色成功")

    # 系统管理-组织管理-角色管理-编辑角色（启用角色）
    def test_d003role(self):
        # 连接数据库获取role_id
        conn = MySQL().connect_emp_os()
        cur = conn.cursor()
        cur.execute('select role_id,role_name from role where role_name like "自动化角色%" and status = 0 ')
        role = cur.fetchone()[0:2]
        role_id = str(role[0])
        role_name = role[1]
        url_bj = "http://emp.hnjing.com/emp_os/v1/role/"
        url = url_bj + role_id
        params = {"roleId": role_id, "roleName": role_name, "status": 1, "opIds": "1,2,3,4,5,6"}
        role_bj = requests.put(url, data=json.dumps(params), headers=headers)
        result_bj = role_bj.text
        result_exp = "修改角色信息成功"
        self.assertIn(result_exp, result_bj)
        print("启用角色成功")

    # 系统管理-组织管理-角色管理-查询角色
    def test_d004role(self):
        url_cx = "http://emp.hnjing.com/emp_os/v1/roles?pageSize=20&pageNum=1&roleName="
        roleName = "自动化角色"
        url = url_cx + roleName
        rolecheck = requests.get(url, headers=headers)
        result_check = json.loads(rolecheck.text)
        values = result_check["data"][0]["roleName"]
        self.assertIn(roleName, values)
        print("查询角色成功")

    # 系统管理-组织管理-员工管理-新增员工（邀请员工）
    def test_e001employ(self):
        url = "http://emp.hnjing.com/emp_os/v1/employee"
        employeeName01 = "自动化测试"
        employeeName02 = ''.join(random.sample(['1', '2', '3', '5', '7', '9', '8'], 3))
        employeeName = employeeName01 + employeeName02
        employeeNo = str(''.join(random.sample(['1', '2', '3', '5', '7', '9', '8', '4', '6'], 4)))
        params = {"employeeNo": employeeNo, "employeeName": employeeName, "email": "linshu@hnjing.com",
                  "phone": "15116398872",
                  "creator": oper_id, "depStations": [{"departmentId": 93, "stationId": 113, "isMaster": 1}]}
        employ_add = requests.post(url, data=json.dumps(params), headers=headers)
        result_add = json.loads(employ_add.text)
        values = result_add["rowNum"]
        result_exp = 1
        self.assertEqual(result_exp, values)
        print("发送邀请员工邮件")

    # 系统管理-组织管理-员工管理-员工离职
    def test_e004employ(self):
        # 连接数据库获取employee_id
        conn = MySQL().connect_emp_os()
        cur = conn.cursor()
        cur.execute(
            'select employee_id from employee where employee_name like "自动化测试%" and deleted = 1 and status != 2 ')
        employee_id = str(cur.fetchone()[0])
        url_del = "http://emp.hnjing.com/emp_os/v1/employee/"
        url = url_del + employee_id
        emp_del = requests.delete(url, headers=headers)
        result_del = json.loads(emp_del.text)
        values = result_del["rowNum"]
        result_exp = 1
        self.assertEqual(result_exp, values)
        print("员工离职")


if __name__ == '__main__':
    unittest.main()
