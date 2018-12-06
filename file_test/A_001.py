# 运营平台-合作伙伴管理
import requests
import random
import json
import unittest
from comm.login import Zpt
from comm.public_data import MySQL
from comm.Log import Logger
from urllib.parse import quote
import readConfig
import time


# 请求头信息
localReadConfig = readConfig.ReadConfig()
token = Zpt().test_admin_login()
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'token': token
}
cuComId = localReadConfig.read_cu_com_id()
cuComName = localReadConfig.read_cu_com_name()
cuEmpId = localReadConfig.read_cu_emp_id()
cuEmpName = localReadConfig.read_cu_emp_name()
adminEmpId = localReadConfig.read_admin_emp_id()

class admin_yygl(unittest.TestCase):
    # 用户运营-合作伙伴管理-新增服务商
    def test_a001_fws(self):
        global log, log_exp, log_act
        log = Logger(logger="管理平台").getlog()
        log_exp = Logger(logger="管理平台_预期结果").getlog()
        log_act = Logger(logger="管理平台_实际结果").getlog()
        conn = MySQL().connect_bi()
        cur = conn.cursor()
        sql = "select customer_name from bi_ici_customer_info limit 1000;"
        cur.execute(sql)
        name1 = cur.fetchall()

        conn1 = MySQL().connect_os()
        cur1 = conn1.cursor()
        sql1 = "select partner_name from partner;"
        cur1.execute(sql1)
        name2 = cur.fetchall()
        s = tuple(set(name1) - set(name2))
        partner_name = str(s[0][0])

        # 随机生成社会信用代码
        uscCode_01 = ''.join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 10))
        uscCode_02 = '43062419'
        uscCode = uscCode_01 + uscCode_02
        paramas = {
            "partner": {"partnerType": "0100", "partnerName": partner_name, "area": "湖南/长沙", "address": "麓谷",
                        "phone": "0731-86241871", "level": 5, "detail": "楼主"},
            "partnerBusiness": {"uscCode": "91431300187402930W", "beginDate": "1993-04-13",
                                "validDate": "2999-12-31", "companyType": "集体所有制",
                                "registAddress": "娄底市娄星区洪家洲振兴路（涟钢检修厂旁）", "legalPerson": "谢国阳",
                                "registAuthority": "娄底市工商行政管理局", "approvalDate": "2016-03-28",
                                "registStatus": "存续（在营、开业、在册）", "registCapital": 303,
                                "scope": "环保设备设计、制造、安装，铆焊机械零配件加工，拉丝，机电设备安装、维修；工业废料回收开发利用，五金、化工产品（不含专控危险品）、金属材料销售；转运装卸、劳务输出（限涟钢厂内）；废油回收加工。软化丝、废钢切割，防腐工程，建筑材料，政策允许的矿产品、金属材料；炉料生产销售。",
                                "legalPersonIdcode": uscCode},
            "partnerExt": {"standardIndustry": "552", "category": "44"}, "partnerQualifys": [{"qualifyType": 1,
                                                                                              "qualifyImage": "https://bj.bcebos.com/v1/hnjing-test/b5f4b5ed46474606b7c603084fb140cd.jpg",
                                                                                              "qualifyName": "营业执照",
                                                                                              "qualifyBeginDate": "1993-04-13",
                                                                                              "qualifyValidDate": "2999-12-31"},
                                                                                             {"qualifyType": 2,
                                                                                              "qualifyImage": "https://bj.bcebos.com/v1/hnjing-test/21d5c46b4c7543e59be30d435fa7c9c5.jpg,https://bj.bcebos.com/v1/hnjing-test/8288ec28360f4499a76879ddd3ae5d94.jpg",
                                                                                              "qualifyName": "法人身份证",
                                                                                              "qualifyBeginDate": "2018-09-30",
                                                                                              "qualifyValidDate": "2018-09-30"}],
            "employees": {"empName": "测试", "phone": "15814405932", "email": "15814405932@139.com"}}
        url = 'http://admin.ejw.cn/platform/v1/partnerall?curEmpId='+adminEmpId
        # 发送服务商接口请求
        qykh_test_01 = requests.post(url, data=json.dumps(paramas), headers=headers)
        print(qykh_test_01.text)
        result_act = qykh_test_01.status_code
        result_exp = 200
        # 判断当前返回码及字段值
        self.assertEqual(result_exp, result_act, msg='审核原因：已存在相同用户企业或其它参数错误')
        log.info("企业客户管理-合作伙伴管理-服务商新增成功")


    # 用户运营-合作伙伴管理-新增供应商
    def test_a002_gys(self):
        global log, log_exp, log_act
        log = Logger(logger="管理平台").getlog()
        log_exp = Logger(logger="管理平台_预期结果")
        log_act = Logger(logger="管理平台_实际结果")
        conn = MySQL().connect_bi()
        cur = conn.cursor()
        sql = "select customer_name from bi_ici_customer_info limit 1000;"
        cur.execute(sql)
        name1 = cur.fetchall()

        conn1 = MySQL().connect_os()
        cur1 = conn1.cursor()
        sql1 = "select partner_name from partner;"
        cur1.execute(sql1)
        name2 = cur.fetchall()
        s = tuple(set(name1) - set(name2))
        partner_name = str(s[1][0])

        # 随机生成社会信用代码
        uscCode_01 = ''.join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 10))
        uscCode_02 = '43062419'
        uscCode = uscCode_01 + uscCode_02
        paramas = {
            "partner": {"partnerType": "0010", "partnerName": partner_name, "area": "湖南/长沙", "address": "麓谷",
                        "phone": "0731-86241871", "level": 5, "detail": "楼主"},
            "partnerBusiness": {"uscCode": "91431300187402930W", "beginDate": "1993-04-13",
                                "validDate": "2999-12-31", "companyType": "集体所有制",
                                "registAddress": "娄底市娄星区洪家洲振兴路（涟钢检修厂旁）", "legalPerson": "谢国阳",
                                "registAuthority": "娄底市工商行政管理局", "approvalDate": "2016-03-28",
                                "registStatus": "存续（在营、开业、在册）", "registCapital": 303,
                                "scope": "环保设备设计、制造、安装，铆焊机械零配件加工，拉丝，机电设备安装、维修；工业废料回收开发利用，五金、化工产品（不含专控危险品）、金属材料销售；转运装卸、劳务输出（限涟钢厂内）；废油回收加工。软化丝、废钢切割，防腐工程，建筑材料，政策允许的矿产品、金属材料；炉料生产销售。",
                                "legalPersonIdcode": uscCode},
            "partnerExt": {"standardIndustry": "552", "category": "44"}, "partnerQualifys": [{"qualifyType": 1,
                                                                                              "qualifyImage": "https://bj.bcebos.com/v1/hnjing-test/b5f4b5ed46474606b7c603084fb140cd.jpg",
                                                                                              "qualifyName": "营业执照",
                                                                                              "qualifyBeginDate": "1993-04-13",
                                                                                              "qualifyValidDate": "2999-12-31"},
                                                                                             {"qualifyType": 2,
                                                                                              "qualifyImage": "https://bj.bcebos.com/v1/hnjing-test/21d5c46b4c7543e59be30d435fa7c9c5.jpg,https://bj.bcebos.com/v1/hnjing-test/8288ec28360f4499a76879ddd3ae5d94.jpg",
                                                                                              "qualifyName": "法人身份证",
                                                                                              "qualifyBeginDate": "2018-09-30",
                                                                                              "qualifyValidDate": "2018-09-30"}],
            "employees": {"empName": "测试", "phone": "15814405932", "email": "15814405932@139.com"}}
        url = 'http://admin.ejw.cn/platform/v1/partnerall?curEmpId='+adminEmpId
        # 发送服务商接口请求
        qykh_test_01 = requests.post(url, data=json.dumps(paramas), headers=headers)
        print(qykh_test_01.text)
        result_act = qykh_test_01.status_code
        result_exp = 200
        # 判断当前返回码及字段值
        self.assertEqual(result_exp, result_act, msg='审核原因：已存在相同用户企业或其它参数错误')
        log.info("企业客户管理-合作伙伴管理-供应商新增成功")
        cur.close()
        conn.close()
        cur1.close()
        conn1.close()



if __name__ == '__main__':
    unittest.main()
