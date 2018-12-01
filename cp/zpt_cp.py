import requests
import unittest
import readConfig as readConfig
import json
import random
from comm.public_data import MySQL
from comm.login import Zpt
from comm.Log import Logger

# 获取配置文件地址url
localReadConfig = readConfig.ReadConfig()
token = Zpt().cp_login()

# 指定头文件
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'token': token
}

cpComId = localReadConfig.read_cp_com_id()
cpComName = localReadConfig.read_cp_com_name()
cpEmpId = localReadConfig.read_cp_emp_id()
cpEmpName = localReadConfig.read_cp_emp_name()


class Cp(unittest.TestCase):
    # 企业设置-部门员工管理-按已存在的姓名查询
    def test_a002_bmyg_serach(self):
        global log, log_exp, log_act
        log_exp = Logger(logger="供应商平台_预期结果").getlog()
        log_act = Logger(logger="供应商平台_实际结果").getlog()
        log = Logger(logger="供应商平台").getlog()
        try:
            conn = MySQL.connect_os()
            cur = conn.cursor()
            sql = "select a.emp_name,b.dep_id from employee a,department b where a.partner_id=b.partner_id and a.emp_id=" + cpEmpId
            cur.execute(sql)
            sql_result = cur.fetchone()[0:2]
            emp_name = sql_result[0]
            dep_id = str(sql_result[1])
            url = "http://cp.ejw.cn/cp/v1/partner/" + cpComId + "/employees?depId=" + dep_id + "&pageNo=1&pageSize=10&sort=%7B%22gmtCreate%22%3A%22desc%22%7D&curEmpId=" + cpEmpId + "&jobNoOrEmpName=" + emp_name
            result = requests.get(url, headers=headers)
            result_act = result.text
            self.assertIn(emp_name, result_act, msg="没有查询到该用户信息")
            log.info("企业设置-部门员工管理, 已存在的员工信息查询信息如下：")
            log_exp.info(emp_name)
            log_act.info(result_act)
        except TypeError:
            log.info("该企业不存在用户信息")

    # 企业设置-部门员工管理-按不存在的姓名查询
    def test_a003_bmyg_serach(self):
        try:
            conn = MySQL.connect_os()
            cur = conn.cursor()
            sql = "select b.dep_id from employee a,department b where a.partner_id=b.partner_id and a.emp_id=" + cpEmpId
            cur.execute(sql)
            sql_result = cur.fetchone()[0:1]
            dep_id = str(sql_result[0])
            emp_name = "xxxxxxxxxxxxxxxxxxx"
            url = "http://cp.ejw.cn/cp/v1/partner/" + cpComId + "/employees?depId=" + dep_id + "&pageNo=1&pageSize=10&sort=%7B%22gmtCreate%22%3A%22desc%22%7D&curEmpId=" + cpEmpId + "&jobNoOrEmpName=" + emp_name
            result = requests.get(url, headers=headers)
            result_act = result.text
            self.assertNotIn(emp_name, result_act, msg="没有查询到该用户信息")
            log.info("企业设置-部门员工管理, 不存在的员工信息查询如下：")
            log_exp.info(emp_name)
            log_act.info(result_act)
        except TypeError:
            log.info("该企业不存在用户信息")

    # 角色权限管理-新增角色
    def test_a004_role_add(self):
        global log, log_exp, log_act
        log_exp = Logger(logger="供应商平台_预期结果").getlog()
        log_act = Logger(logger="供应商平台_实际结果").getlog()
        log = Logger(logger="供应商平台").getlog()
        name_02 = ''.join(random.sample(['a', 'b', 'c', 'd', 'e', '1', '5', '6', 'x', 'aaa'], 6))
        name_01 = '自动化测试角色'
        Name = name_01 + name_02
        # print(Name)
        url = "http://cp.ejw.cn/os/v1/partner/" + cpComId + "/role"
        params = {"roleName": Name, "appName": "cp"}
        # print(params)
        role_code_act = requests.post(url, data=json.dumps(params), headers=headers)
        role_code_exp = 200
        self.assertEqual(role_code_exp, role_code_act.status_code)
        log.info("企业设置-部门及员工管理, 新增角色结果如下：")
        log_exp.info(role_code_exp)
        log_act.info(role_code_act.text)

    # 企业设置-部门及员工管理-新增
    def test_a005_bmyg_add(self):
        try:
            conn = MySQL.connect_os()
            cur = conn.cursor()
            sql = "select a.role_id,b.dep_id from role a,department b where a.app_name='cp' and a.partner_id=" + cpComId + " and  b.partner_id=a.partner_id and depart_name="+"'自动化';"
            cur.execute(sql)
            sql_result = cur.fetchone()[0:2]
            roles = sql_result[0]
            depId = sql_result[1]
            empName = ''.join(random.sample(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'j'], 6))
            jobNo = ''.join(random.sample(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], 6))
            mobile_02 = ''.join(random.sample(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], 8))
            mobile_01 = '131'
            mobile = mobile_01 + mobile_02
            mail_01 = '@qq.com'
            mail = mobile + mail_01
            params = [
                {"roles": [roles], "departments": [{"depId": depId, "position": 1}], "empName": empName, "jobNo": jobNo,
                 "email": mail, "phone": mobile, "status": 1,
                 "entryDate": "2018-05-02T16:00:00.000Z"}]
            url = "http://cp.ejw.cn/cp/v1/partner/"+cpComId+"/employees"
            result_act = requests.post(url, data=json.dumps(params), headers=headers)
            result_exp = 200
            self.assertEqual(result_exp, result_act.status_code)
            log.info("企业设置-部门及员工管理, 新增员工结果如下：")
            log_exp.info(result_exp)
            log_act.info(result_act.text)
        except TypeError:
            log.info("数据库异常或角色、部门信息为空")

    # 产品管理-发布产品
    def test_b001_fbcp(self):
        name_02 = ''.join(random.sample(['a', 'b', 'c', 'd', 'e', '1', '5', '6', 'x'], 6))
        name_01 = '供_自动化测试勿删'
        productName = name_01 + name_02
        # 请求下单功能
        url = "http://cp.ejw.cn/cp/v1/partner/"+cpComId+"/product?curEmpId="+cpEmpId
        parms = {"typeId": 136, "productInfo": "<p>塑料袋</p>",
                 "images": "https://bj.bcebos.com/v1/hnjing-test/cb4ef37d38ff46c8bc74fdfc2bed6899.jpg",
                 "qualification": "135", "tempStatus": "1", "flowId": 135, "specMinPrice": 0.1, "specMaxPrice": 0.1,
                 "cpPartnerName": cpComName, "buyType": "0", "cpCommonAttrInfos": [
                {"cpCommonAttrId": None, "attrFormType": "text", "attrLayerType": "2", "attrIsValid": "1",
                 "required": "1", "attrOrder": None, "attrType": "0", "attrValue": "", "fillValue": "颜色标准尺寸",
                 "cpCommonAttrName": "域名描述", "isTemp": "1"},
                {"cpCommonAttrId": None, "cpCommonAttrName": "空间", "attrValue": "500M,1G,10G",
                 "attrFormType": "checkbox", "attrLayerType": "1", "attrType": "1", "fillValue": "500M", "attrOrder": 2,
                 "required": "1", "customAttrValue": "", "isTemp": "1"},
                {"cpCommonAttrId": None, "cpCommonAttrName": "域名", "attrValue": "中文域名,英文域名", "attrFormType": "checkbox",
                 "attrLayerType": "1", "attrType": "1", "fillValue": "中文域名", "attrOrder": 1, "required": "1",
                 "customAttrValue": "", "isTemp": "1"}], "cpProductName": productName, "productSpecs": [
                {"specSort": 0, "sellPrice": "0.10", "cpProductSpecAttrs": [{"attrValue": "500M", "attrName": "空间"},
                                                                            {"attrValue": "中文域名", "attrName": "域名"}]}]}
        values = json.dumps(parms)
        # 返回状态码信息
        respon_act = requests.post(url, data=values, headers=headers)
        self.assertIn(productName, respon_act.text, msg="参数异常")
        log.info("产品" + productName + "发布结果如下：")
        log_exp(productName)
        log_act(respon_act.text)

    # 产品管理-产品名称查询
    def test_b002_cpmc_search(self):
        # 请求查询参数
        product_name = "%自动化测试%"
        url = 'http://cp.ejw.cn/ps/v1/cpproducts?pageNum=1&pageSize=20&_sort=modifyDate%2Cdesc&cpPartnerId=502&cpProductName=%E8%87%AA%E5%8A%A8%E5%8C%96'
        result_all = requests.get(url, headers=headers).text
        result_json = json.loads(result_all)
        totalCount_exp = result_json["page"]["totalCount"]

        # 连接数据库创建一个游标对象
        conn = MySQL().connect_ps()
        cur = conn.cursor()
        cur.execute('select count(*) from cp_product t where t.cp_product_name like "' + product_name + '"')
        totalCount_act = cur.fetchone()[0]
        self.assertEqual(totalCount_exp, totalCount_act, "预期结果与实际结果不一致")
        log.info("已存在的产品名称验证成功")

    # 产品管理-产品选择日期查询
    def test_b003_cpmc_search(self):
        # 请求查询参数
        url_get = 'http://cp.ejw.cn/ps/v1/cpproducts?pageNum=1&pageSize=20&_sort=modifyDate%2Cdesc&cpPartnerId=502&modifyTimeStart=2018-10-14T16%3A00%3A00.000Z&modifyTimeEnd=2018-11-30T15%3A59%3A59.000Z'
        result_all = requests.get(url_get, headers=headers).text
        # result_json = json.loads(result_all.text)
        # totalCount_exp = result_json["data"][0]["productName"]
        # print(result_all)

        # 连接数据库
        conn = MySQL().connect_ps()
        # 创建一个游标对象
        cur = conn.cursor()
        # order = "order by create_time desc"
        date_01 = '2018-05-02 00:00:00'
        sql_03 = 'and t.create_date < "2019-05-02 23:59:59"'
        sql_01 = " order by create_date desc"
        sql_02 = 'select t.cp_product_name from cp_product t where t.cp_partner_id=502 and t.create_date > "' + date_01 + '" '
        # 拼接sql语句
        sql = sql_02 + sql_03 + sql_01
        # print(sql)
        # 执行sql命令
        cur.execute(sql)
        # 取当前游标productName数据
        totalCount_act = cur.fetchone()[0]
        self.assertIn(totalCount_act, result_all, msg="数据查询不正确")
        log.info("产品查询日期正常")


if __name__ == '__main__':
    unittest.main()
