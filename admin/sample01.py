# 运营平台-合作伙伴管理
import requests
import random
import json
import unittest
from comm.login import testlogin_001
from comm.public_data import MySQL
from comm.Log import Logger

# 请求头信息
token = testlogin_001().test_adminlogin('token')
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'token': token
}


class admin_yygl(unittest.TestCase):
    # 运营管理-合作伙伴管理-新增服务商
    def test_a002_yygl(self):
        global log
        log = Logger(logger="管理平台").getlog()
        name_01 = "林丽娟自创供应商dg"
        conn_partner = MySQL().connect_os1('conn')
        cur1 = conn_partner.cursor()
        cur1.execute('select partner_id from partner where partner_name ="' + name_01 + '"')
        par_result = cur1.fetchone()

        if par_result == None:
            # 随机生成社会信用代码
            uscCode_01 = ''.join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 10))
            uscCode_02 = '43062419'
            uscCode = uscCode_01 + uscCode_02
            paramas = {
                "partner": {"partnerType": "0010", "partnerName": name_01, "area": "湖南/长沙", "address": "麓谷",
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
            url = 'http://admin.ejw.cn/platform/v1/partnerall?curEmpId=1699'
            # 发送服务商接口请求
            qykh_test_01 = requests.post(url, data=json.dumps(paramas), headers=headers)
            print(qykh_test_01.text)
            result_act = qykh_test_01.status_code
            result_exp = 200
            # 判断当前返回码及字段值
            self.assertEqual(result_exp, result_act, msg='审核原因：已存在相同用户企业或其它参数错误')
            log.info("企业客户管理-合作伙伴管理-供应商新增成功")

        else:
            # 获取partner_id的值
            partner_id = par_result[0]
            name_id = str(partner_id)
            print(name_id)
            # 获取emp_id的值
            cur1.execute('select emp_id from employee where partner_id = "' + name_id + '"')
            results_data_01 = cur1.fetchone()
            # print(results_data_01)
            employee_id = results_data_01[0]
            emp_id = str(employee_id)
            print(emp_id)
            # 删除除长沙艾客美食文化传播有限公司相关联的数据用户信息
            cur1.execute('delete from employee_link_role where emp_id = "' + emp_id + '"')
            cur1.execute('delete from employee where partner_id = "' + name_id + '"')
            cur1.execute('delete from partner_business where partner_id= "' + name_id + '"')
            cur1.execute('delete from partner_ext where partner_id= "' + name_id + '"')
            cur1.execute('delete from partner_qualify where partner_id= "' + name_id + '"')
            cur1.execute('delete from partner where partner_name="' + name_01 + '"')
            conn_partner.commit()
            cur1.close()
            conn_partner.close()
            # 随机生成社会信用代码
            uscCode_01 = ''.join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 10))
            uscCode_02 = '43062419'
            uscCode = uscCode_01 + uscCode_02
            paramas = {
                "partner": {"partnerType": "0101", "partnerName": name_01, "area": "湖南/长沙", "address": "麓谷",
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
            url = 'http://admin.ejw.cn/platform/v1/partnerall?curEmpId=1699'
            # 发送服务商接口请求
            qykh_test_01 = requests.post(url, data=json.dumps(paramas), headers=headers)
            print(qykh_test_01.text)
            result_act = qykh_test_01.status_code
            result_exp = 200
            # 判断当前返回码及字段值
            # 判断当前返回码及字段值
            self.assertEqual(result_exp, result_act, msg='审核原因：已存在相同用户企业或其它参数错误')
            log.info("企业客户管理-合作伙伴管理-供应商新增成功")


if __name__ == '__main__':
    unittest.main()
