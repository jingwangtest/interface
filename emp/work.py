import requests
import unittest
import json
import random
from emp.login_emp import Emp
from comm.public_data import MySQL
from comm.Log import Logger

log = Logger(logger="EMP").getlog()
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

class work01(unittest.TestCase):
    # 系统管理 - 智平台组织管理-组织架构-同步员工
    def test_a001syn(self):
        #连接数据库
        conn = MySQL().connect_emp_os()
        cur1 = conn.cursor()
        cur1.execute('select employee_no,employee_name,email,phone,user_id from employee where employee_name = "测试03" and deleted = 1 and status = 1')
        syn = cur1.fetchone()[0:5]
        employee_no = syn[0]
        employee_name = syn[1]
        email = syn[2]
        phone = syn[3]
        user_id = syn[4]
        url = "http://emp.hnjing.com/emp_os/v1/employees-syn"
        params = [{"employeeNo":employee_no,"employeeName":employee_name,
                   "email":email,"phone":phone,"userId":user_id,"partnerId":190,"departmentName":""}]
        empl_syn = requests.post(url, data=json.dumps(params), headers=headers)
        result_syn = empl_syn.text
        result_exp = "success"
        self.assertIn(result_exp, result_syn)
        log.info("员工同步成功")

    # 系统管理 -流程管理-工单模板配置-新增未发布工单模板
    def test_b001work(self):
        workname01 = "自动化测试模板"
        workname02 = ''.join(random.sample(['1', '2', '3', '5', '6', '8', '9'], 3))
        workname = workname01 + workname02
        url = "http://emp.hnjing.com/emp_os/v1/work-order-temp"
        params = {"workName":workname}
        work_add = requests.post(url, data=json.dumps(params), headers=headers)
        result = work_add.text
        self.assertIn(workname, result)
        log.info(workname + "新增工单模板成功")

    # 系统管理 - 流程管理 - 工单列表-工单查询
    def test_b002work(self):
        url_check = "http://emp.hnjing.com/emp_os/v1/work-procinsts?pageNum=1&pageSize=20&workInstType=1&sort=%7B%22startTime%22:%22desc%22%7D&workName="
        workname = "空间新开工单"
        url = url_check + workname
        work = requests.get(url, headers=headers)
        result = work.text
        self.assertIn(workname, result)
        log.info(workname + " 工单查询成功")

    # 系统管理 -流程管理 - 智平台流程配置 -配置工单模板
    def test_b003work(self):
        url = "http://emp.hnjing.com/emp_os/v1/zyxprocess/56"
        pararm = {"workId":12,"workName":"400电话新开工单",
                  "zyxprocessNode":[{"zyxNodeId":"315","zyxNodeName":"续期工单流程阶段","nodeId":"task1","nodeName":"400电话信息录入"}]}
        work_zyx = requests.put(url, data=json.dumps(pararm), headers=headers)
        result = work_zyx.text
        result_exp = 1
        self.assertEqual(result_exp, int(result))
        log.info("配置工单模板成功")

if __name__ == '__main__':
    unittest.main()