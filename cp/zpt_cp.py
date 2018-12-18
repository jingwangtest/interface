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
    def test_a001_bmyg_serach(self):
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
            url = "http://cp.ejw.cn/cp/v1/partner/" + cpComId + "/employees?&pageNo=1&pageSize=10&sort=%7B%22gmtCreate%22%3A%22desc%22%7D&curEmpId=" + cpEmpId + "&jobNoOrEmpName=" + emp_name
            result = requests.get(url, headers=headers)
            result_act = result.text
            self.assertIn(emp_name, result_act, msg="没有查询到该用户信息")
            log.info("企业设置-部门员工管理, 已存在的员工信息查询信息如下：")
            log_exp.info(emp_name)
            log_act.info(result_act)
        except TypeError:
            log.info("该企业不存在用户信息")

    # 企业设置-部门员工管理-按不存在的姓名查询
    def test_a002_bmyg_serach(self):
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
    def test_a003_role_add(self):
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
    def test_a004_bmyg_add(self):
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
        global log, log_exp, log_act
        log_exp = Logger(logger="供应商平台_预期结果").getlog()
        log_act = Logger(logger="供应商平台_实际结果").getlog()
        log = Logger(logger="供应商平台").getlog()
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
        log_exp.info(productName)
        log_act.info(respon_act.text)

    # 产品管理-产品名称查询
    def test_b002_cpmc_search(self):
        # 连接数据库创建一个游标对象
        conn = MySQL().connect_ps()
        cur = conn.cursor()
        sql = "select cp_product_name from cp_product t where t.cp_partner_id = " + cpComId
        cur.execute(sql)
        sql_result = cur.fetchone()[0:1]
        cp_product_name = sql_result[0]
        # 请求查询参数
        url = "http://cp.ejw.cn/ps/v1/cpproducts?pageNum=1&pageSize=20&_sort=modifyDate%2Cdesc&cpPartnerId="+cpComId+"&cpProductName="+cp_product_name
        # url = 'http://cp.ejw.cn/ps/v1/cpproducts?pageNum=1&pageSize=20&_sort=modifyDate%2Cdesc&cpPartnerId=502&cpProductName=%E8%87%AA%E5%8A%A8%E5%8C%96'
        result_all = requests.get(url, headers=headers).text
        self.assertIn(cp_product_name, result_all, "预期结果与实际结果不一致")
        log.info("已存在的产品名称验证成功")

    # 产品管理-产品选择日期查询
    def test_b003_cpmc_search(self):
        # 连接数据库
        conn = MySQL().connect_ps()
        # 创建一个游标对象
        cur = conn.cursor()
        # 拼接sql语句
        sql = "select t.cp_product_name from cp_product t where t.cp_partner_id=" + cpComId + " and t.create_date >" + "'2018-05-02 00:00:00'" + " and t.create_date <" + "'2019-05-02 23:59:59'" + "order by create_date desc;"
        # 执行sql命令
        cur.execute(sql)
        # 取当前游标productName数据
        totalCount_act = cur.fetchone()[0]

        # 请求查询参数
        url_get = "http://cp.ejw.cn/ps/v1/cpproducts?pageNum=1&pageSize=20&_sort=modifyDate%2Cdesc&cpPartnerId="+cpComId+"&modifyTimeStart=2018-05-02T16%3A00%3A00.000Z&modifyTimeEnd=2019-05-02T15%3A59%3A59.000Z"
        result_all = requests.get(url_get, headers=headers).text

        self.assertIn(totalCount_act, result_all, msg="数据查询不正确")
        log.info("产品查询日期正常")

    # 产品管理-产品上架审核提交操作
    def test_p001_search(self):
        try:
            # 连接到数据库ps1（分支产品库）
            conn = MySQL().connect_ps()
            # 定义一个游标赋值给变量cur，cur才有权限去执行数据库
            cur = conn.cursor()
            # 数据库中查询供应商id为502，产品状态为0（已下架）、审核状态为空或上架审核不通过
            cur.execute(
                'select cp_product_code,cp_product_name,cp_partner_id from cp_product  where sale_flag = 0 and cp_partner_id = "' + cpComId + '" and examine_state  in(-1,2)')
            # 定义查询数据库表中3个字段 cpProductCode，ProductName,partnerId
            cur_data = cur.fetchone()[0:3]
            print(cur_data, type(cur_data))
            # 第一个字段赋给变量sp_product_code
            cpProductCode = cur_data[0]
            # 第二个字段赋给变量ProductName
            ProductName = cur_data[1]
            # 第三个字段赋给变量partnerId
            partnerId = cur_data[2]
            # 打印查询出来的cpProductCode，ProductName这2个字段内容
            print(cpProductCode, ProductName)
            # url地址
            url_01 = 'http://cp.ejw.cn/cp/v1/partner/'
            url_02 = url_01 + str(partnerId) + '/product/' + str(cpProductCode) + '/release?curEmpId='
            url = url_01 + str(partnerId) + '/product/' + str(cpProductCode) + '/release?curEmpId=' + str(cpEmpId)
            # 发送上架审核接口请求
            result_act = requests.put(url, headers=headers).text
            # 设置预期返回1
            result_exp = 1
            # 判断实际返回码是否与预期的一致
            self.assertEqual(result_exp, int(result_act))
            log_exp.info(result_exp)
            log_act.info(result_act)
            log.info(ProductName + "产品上架提交成功")
        except LookupError:
            log.info("没有需要上架的产品数据")

    # 产品管理-产品上架取消提交操作
    def test_p002_search(self):
        try:
            # 连接到数据库ps1（分支产品库）
            conn = MySQL().connect_ps()
            # 定义一个游标赋值给变量cur，cur才有权限去执行数据库
            cur = conn.cursor()
            # 数据库中查询供应商id为502，产品状态为0（已下架），审核状态为0（待上架审核）
            cur.execute(
                'select cp_product_code,cp_product_name,cp_partner_id from cp_product  where sale_flag = 0 and cp_partner_id = "' + cpComId + '" and examine_state = 0')
            # url地址，将产品编号设置为变量，将数据库查询出来的产品编号赋值给变量spProductCode
            # 将查询出来的企业ID值赋值给变量cpProductCode
            cpProductCode = str(cur.fetchall()[0][0])
            # 拼接请求地址
            url_01 = 'http://cp.ejw.cn/platform/v1/product/'
            url = url_01 + str(cpProductCode) + '/canel-verify?curEmpId=' + str(cpEmpId)
            # 打印请求地址，以便于核对请求地址是否拼接正确
            print(url)
            # 请求结果存入变量result_act
            result_act = requests.delete(url, headers=headers).text
            # 打印实际返回结果，以便于核对是否正确
            print(result_act)
            # 设置预期设为1
            result_exp = 1
            # 判断实际返回的内容是否与预期的一致
            self.assertEqual(result_exp, int(result_act))
            log_exp.info(result_exp)
            log_act.info(result_act)
            log.info(cpProductCode + "产品上架审核取消操作成功")
        except LookupError:
            log.info("没有需要取消上架产品的数据")

    # 产品管理-产品下架审核提交操作
    def test_p003_search(self):
        try:
            # 连接到数据库ps1（分支产品库）
            conn = MySQL().connect_ps()
            # 定义一个游标赋值给变量cur，cur才有权限去执行数据库
            cur = conn.cursor()
            # 数据库中查询供应商id为502，产品状态为1（已上架）、审核状态为空或下架审核不通过
            cur.execute(
                'select cp_product_code,cp_product_name,cp_partner_id from cp_product  where sale_flag = 1 and cp_partner_id =  "' + cpComId + '"  and examine_state=1')
            # 定义查询数据库表中3个字段 cpProductCode，ProductName,partnerId
            cur_data = cur.fetchone()[0:3]
            print(cur_data, type(cur_data))
            # 第一个字段赋给变量sp_product_code
            cpProductCode = cur_data[0]
            # 第二个字段赋给变量ProductName
            ProductName = cur_data[1]
            # 第三个字段赋给变量partnerId
            partnerId = cur_data[2]
            # 打印查询出来的cpProductCode，ProductName这2个字段内容
            print(cpProductCode, ProductName)
            # url地址
            url_01 = 'http://cp.ejw.cn/cp/v1/partner/'
            url_02 = url_01 + str(partnerId) + '/product/' + str(cpProductCode) + '/release?curEmpId='
            url = url_01 + str(partnerId) + '/product/' + str(cpProductCode) + '/off?curEmpId=' + str(cpEmpId)
            # 发送上架审核接口请求
            result_act = requests.put(url, headers=headers).text
            # 设置预期返回1
            result_exp = 1
            # 判断实际返回码是否与预期的一致
            self.assertEqual(result_exp, int(result_act))
            log_exp.info(result_exp)
            log_act.info(result_act)
            log.info(ProductName + "产品下架提交成功")
        except TypeError:
            log.info("没有需要下架的产品数据")

    # 产品管理-产品下架取消提交操作
    def test_p004_search(self):
        try:
            # 连接到数据库ps1（分支产品库）
            conn = MySQL().connect_ps()
            # 定义一个游标赋值给变量cur，cur才有权限去执行数据库
            cur = conn.cursor()
            # 数据库中查询供应商id为502，产品状态为1（已上架），审核状态为0（待下架审核）
            cur.execute(
                'select cp_product_code from cp_product  where sale_flag = 1 and cp_partner_id = "' + cpComId + '" and examine_state = 0')
            # 将查询出来的企业ID值赋值给变量cpProductCode
            result_sql = cur.fetchone()[0:1]
            cpProductCode = str(result_sql[0])
            # 产品编号打印出来，以便于核对是否正确
            log.info(cpProductCode)
            # 拼接请求地址
            url_01 = 'http://cp.ejw.cn/platform/v1/product/'
            url = url_01 + str(cpProductCode) + '/canel-verify?curEmpId=' + str(cpEmpId)
            # 打印请求地址，以便于核对请求地址是否拼接正确
            log.info(url)
            # 请求结果存入变量result_act
            result_act = requests.delete(url, headers=headers).text
            # 打印实际返回结果，以便于核对是否正确
            log.info(result_act)
            # 设置预期设为1
            result_exp = 1
            # 判断实际返回的内容是否与预期的一致
            self.assertEqual(result_exp, int(result_act))
            log_exp.info(result_exp)
            log_act.info(result_act)
            log.info(cpProductCode + "产品下架审核取消操作成功")
        except TypeError:
            log.info("没有需要取消产品下架审核的数据")


if __name__ == '__main__':
    unittest.main()
