import requests
import unittest
import readConfig as readConfig
import json
import random
from comm.public_data import MySQL
from comm.login import testlogin_001
from comm.Log import Logger
# 获取配置文件地址url
localReadConfig = readConfig.ReadConfig()
token_01 = testlogin_001().test_cplogin('token')

class Cpgl(unittest.TestCase):
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

    # 智营销平台-企业设置-部门员工管理-按已存在的姓名查询
    def test_a002_bmyg_serach(self):
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'token': token_01
        }
        empname = "测试"
        url_01 = "http://cp.ejw.cn/cp/v1/partner/402/employees?depId=236&pageNo=1&pageSize=10&sort=%7B%22gmtCreate%22%3A%22desc%22%7D&curEmpId=1723&jobNoOrEmpName="
        url = url_01 + empname
        result = requests.get(url, headers=headers)
        result_act = result.text
        self.assertIn(empname, result_act, msg="没有查询到该用户信息")
        log_exp.info(empname)
        log_act.info(result_act)
        log.info(empname + "查询成功")

    # 智营销平台-企业设置-部门员工管理-按不存在的姓名查询
    def test_a003_bmyg_serach(self):
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'token': token_01
        }
        empname = "测试sadfasfasfsfasfd"
        url_01 = "http://cp.ejw.cn/cp/v1/partner/402/employees?pageNo=1&pageSize=10&sort=%7B%22gmtCreate%22%3A%22desc%22%7D&curEmpId=1723&jobNoOrEmpName="
        url = url_01 + empname
        result = requests.get(url, headers=headers)
        result_act = result.text
        self.assertNotIn(empname, result_act, msg="没有查询到该用户信息")
        log.info(empname + "查询成功")

    # 智营销平台-角色权限管理-新增角色
    def test_a004_role_add(self):
        name_02 = ''.join(random.sample(['a', 'b', 'c', 'd', 'e', '1', '5', '6', 'x', 'aaa'], 6))
        name_01 = '自动化测试角色'
        Name = name_01 + name_02
        # print(Name)
        url = "http://cp.ejw.cn/os/v1/partner/402/role"
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json;charset=UTF-8',
            'token': token_01
        }
        params = {"roleName": Name, "appName": "cp"}
        # print(params)
        role_code_act = requests.post(url, data=json.dumps(params), headers=headers).status_code
        role_code_exp = 200
        self.assertEqual(role_code_exp, role_code_act)
        log.info("角色新增成功")

    # 智营销平台-企业设置-部门及员工管理-新增
    def test_a005_bmyg_add(self):
        empName = ''.join(random.sample(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'j'], 6))
        jobNo = ''.join(random.sample(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], 6))
        mobile_02 = ''.join(random.sample(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], 8))
        mobile_01 = '131'
        mobile = mobile_01 + mobile_02
        mail_01 = '@qq.com'
        mail = mobile + mail_01
        params = [{"roles": [1954], "departments": [{"depId": 428, "position": 1}], "empName": empName, "jobNo": jobNo,
                   "email": mail, "phone": mobile, "status": 1,
                   "entryDate": "2018-05-02T16:00:00.000Z"}]
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'token': token_01
        }
        url = "http://cp.ejw.cn/cp/v1/partner/402/employees"
        result_exp = requests.post(url, data=json.dumps(params), headers=headers).status_code
        result_act = 200
        self.assertEqual(result_exp, result_act)
        # log = Logger(logger="供应商平台").getlog()
        log.info(empName + "员工新增成功")

    # 智营销平台-产品管理-发布产品
    def test_b001_fbcp(self):
        name_02 = ''.join(random.sample(['a', 'b', 'c', 'd', 'e', '1', '5', '6', 'x'], 6))
        name_01 = '自动化测试'
        productName = name_01 + name_02
        # 请求下单功能
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'token': token_01
        }
        # print(headers)
        # 请求参数
        url = 'http://cp.ejw.cn/cp/v1/partner/402/product?curEmpId=1723'
        parms = {"productSetupAttributes": [{"attrId": 102, "customAttrValue": "", "fillValue": "11"},
                                            {"attrId": 106, "customAttrValue": "", "fillValue": "模压"},
                                            {"attrId": 107, "customAttrValue": "", "fillValue": "内容,信息,数据"},
                                            {"attrId": 103, "customAttrValue": "", "fillValue": "111"}],
                 "productCustomAttributes": [], "productSpecs": [{"sellPrice": "1.00", "stock": 1,
                                                                  "productSpecAttributes": [
                                                                      {"attrId": 103, "attrValue": "111", "code": 1,
                                                                       "isCustomAttr": "0"},
                                                                      {"attrId": 107, "attrValue": "内容", "code": 1,
                                                                       "isCustomAttr": "0"}]},
                                                                 {"sellPrice": "1.00", "stock": 1,
                                                                  "productSpecAttributes": [
                                                                      {"attrId": 103, "attrValue": "111", "code": 1,
                                                                       "isCustomAttr": "0"},
                                                                      {"attrId": 107, "attrValue": "信息", "code": 1,
                                                                       "isCustomAttr": "0"}]},
                                                                 {"sellPrice": "1.00", "stock": 1,
                                                                  "productSpecAttributes": [
                                                                      {"attrId": 103, "attrValue": "111", "code": 1,
                                                                       "isCustomAttr": "0"},
                                                                      {"attrId": 107, "attrValue": "数据", "code": 1,
                                                                       "isCustomAttr": "0"}]}], "typeId": 1,
                 "partnerId": 402, "partnerType": "0100", "productName": productName, "productType": "single",
                 "productInfo": "<p>这是一个自动化测试过程</p>",
                 "images": "https://bj.bcebos.com/v1/hnjing-test/9f35b1bcc51a46a68e4d9a1ddd791b3f.jpg,https://bj.bcebos.com/v1/hnjing-test/7a064e7669a746979e457f341bece02f.jpg",
                 "qualification": "23", "createUserid": 164, "specMinPrice": 1, "specMaxPrice": 1, "tempStatus": "1",
                 "flowId": 96}
        values = json.dumps(parms)
        # 返回状态码信息
        respon_act = requests.post(url, data=values, headers=headers).text
        self.assertIn(productName, respon_act, msg="参数异常")
        log.info("产品"+productName+"发布成功")

    # 智营销平台-产品管理-产品上下架管理-产品名称查询
    def test_b002_cpmc_search(self):
        # 请求下单功能
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'token': token_01
        }
        # 请求查询参数
        product_name = "%自动化测试%"
        url = 'http://cp.ejw.cn/cp/v1/partner/402/products?pageNo=1&pageSize=10&sort=%7B%22createTime%22%3A%22desc%22%7D&productName=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95'
        result_all = requests.get(url, headers=headers).text
        result_json = json.loads(result_all)
        totalCount_exp = result_json["page"]["totalCount"]

        # 连接数据库创建一个游标对象
        conn = MySQL().connect_ps1("conn")
        cur = conn.cursor()
        cur.execute('select count(*) from product t where t.product_name like "' + product_name + '"')
        totalCount_act = cur.fetchone()[0]
        self.assertEqual(totalCount_exp, totalCount_act, "预期结果与实际结果不一致")
        log.info("已存在的产品名称验证成功")

    # 智营销平台-产品管理-产品上下架管理-产品选择日期查询
    def test_b003_cpmc_search(self):
        # 请求下单功能
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'token': token_01
        }
        # print(headers)
        # 请求查询参数
        url_get = 'http://cp.ejw.cn/cp/v1/partner/402/products?pageNo=1&pageSize=10&sort=%7B%22createTime%22%3A%22desc%22%7D&createTimeStart=2018-05-01T16%3A00%3A00.000Z&createTimeEnd=2019-05-02T15%3A59%3A59.000Z'
        result_all = requests.get(url_get, headers=headers).text
        # result_json = json.loads(result_all.text)
        # totalCount_exp = result_json["data"][0]["productName"]
        # print(result_all)

        # 连接数据库
        conn = MySQL().connect_ps1("conn")
        # 创建一个游标对象
        cur = conn.cursor()
        # order = "order by create_time desc"
        date_01 = '2018-05-02 00:00:00'
        sql_03 = 'and t.create_time < "2019-05-02 23:59:59"'
        sql_01 = " order by create_time desc"
        sql_02 = 'select t.product_name from product t where t.partner_id=402 and t.create_time > "' + date_01 + '" '
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
