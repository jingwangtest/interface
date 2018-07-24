# 运营平台-合作伙伴管理
import requests
import random
import json
import unittest
from comm.login import testlogin_001
from comm.public_data import MySQL
from comm.Log import Logger
from urllib.parse import quote

# 请求头信息
token = testlogin_001().test_adminlogin('token')
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'token': token
}


class admin_yygl(unittest.TestCase):
    # 运营管理-合作伙伴管理-新增服务商
    def test_a001_yygl(self):
        global log
        log = Logger(logger="管理平台").getlog()
        # 随机生成企业名称
        prodctName_01 = ''.join(random.sample(['8', '6', '3', '2', '5', '6'], 4))
        prodctName_02 = '企业名称auto'
        prodctName = prodctName_02 + prodctName_01

        # 随机生成社会信用代码
        uscCode_01 = ''.join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 10))
        uscCode_02 = '43062419'
        uscCode = uscCode_01 + uscCode_02
        url = 'http://admin.ejw.cn/platform/v1/partnerall'
        parms = {
            "partner": {
                "partnerType": "0101",
                "partnerName": prodctName,
                "area": "湖南/长沙",
                "address": "岳麓",
                "phone": "0371-86241125",
                "level": 5,
                "detail": "im"
            },
            "partnerBusiness": {
                "uscCode": uscCode,
                "beginDate": "2014-01-06",
                "validDate": "2064-01-05",
                "companyType": "有限责任公司(自然人投资或控股)",
                "registAddress": "长沙市开福区车站北路649号天都大厦第1幢N单元21层21022号房",
                "legalPerson": "欧阳凤贵",
                "registAuthority": "长沙市工商行政管理局开福分局",
                "approvalDate": "2016-12-27",
                "registStatus": "存续（在营、开业、在册）",
                "registCapital": 1000,
                "scope": "智能化技术研发；工程和技术研究和试验发展；网络集成系统建设、维护、运营、租赁；"
                         "计算机网络系统工程服务；电气设备服务；",
                "legalPersonIdcode": "430624199802031256"
            },
            "partnerExt": {
                "standardIndustry": "612",
                "category": "44"
            },
            "partnerQualifys": [{
                "qualifyType": 1,
                "qualifyImage": "https://bj.bcebos.com/v1/hnjing-test/310327dcbb4e4f6da4955aa803677bf7.jpg",
                "qualifyName": "营业执照",
                "qualifyBeginDate": "2014-01-06",
                "qualifyValidDate": "2064-01-05"
            }, {
                "qualifyType": 2,
                "qualifyImage": "https://bj.bcebos.com/v1/hnjing-test/1d058c38f44741e0a3183ebe488302c4.jpg,https://bj.bcebos.com/v1/hnjing-test/d18a5950035f4c75815a371289d23a45.jpg",
                "qualifyName": "法人身份证",
                "qualifyBeginDate": "2018-07-09",
                "qualifyValidDate": "2018-07-31"
            }],
            "employees": {
                "empName": "测试",
                "phone": "15812205665",
                "email": "15814405932@139.com"
            }
        }
        values = json.dumps(parms)
        # 发送服务商接口请求
        fws_test = requests.post(url, data=values, headers=headers)
        result_exp = 200
        result_act = fws_test.status_code
        # print(fws_test.text)
        self.assertEqual(result_exp, result_act, msg="预期结果与实际结果不一致")
        log.info("新增服务商成功pass123456")

    # 运营管理-合作伙伴管理-新增供应商
    def test_a002_yygl(self):
        # 随机生成企业名称
        prodctName_01 = ''.join(random.sample(['8', '6', '3', '2', '5', '6'], 6))
        prodctName_02 = '企业名称auto'
        prodctName = prodctName_02 + prodctName_01

        # 随机生成社会信用代码
        uscCode_01 = ''.join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 10))
        uscCode_02 = '43062419'
        uscCode = uscCode_01 + uscCode_02
        url = 'http://admin.ejw.cn/platform/v1/partnerall'
        parms = {
            "partner": {
                "partnerType": "0010",
                "partnerName": prodctName,
                "area": "湖南/长沙",
                "address": "岳麓",
                "phone": "0371-86241125",
                "level": 5,
                "detail": "im"
            },
            "partnerBusiness": {
                "uscCode": uscCode,
                "beginDate": "2014-01-06",
                "validDate": "2064-01-05",
                "companyType": "有限责任公司(自然人投资或控股)",
                "registAddress": "长沙市开福区车站北路649号天都大厦第1幢N单元21层21022号房",
                "legalPerson": "欧阳凤贵",
                "registAuthority": "长沙市工商行政管理局开福分局",
                "approvalDate": "2016-12-27",
                "registStatus": "存续（在营、开业、在册）",
                "registCapital": 1000,
                "scope": "智能化技术研发；工程和技术研究和试验发展；",
                "legalPersonIdcode": "430624199802031256"
            },
            "partnerExt": {
                "standardIndustry": "612",
                "category": "44"
            },
            "partnerQualifys": [{
                "qualifyType": 1,
                "qualifyImage": "https://bj.bcebos.com/v1/hnjing-test/310327dcbb4e4f6da4955aa803677bf7.jpg",
                "qualifyName": "营业执照",
                "qualifyBeginDate": "2014-01-06",
                "qualifyValidDate": "2064-01-05"
            }, {
                "qualifyType": 2,
                "qualifyImage": "https://bj.bcebos.com/v1/hnjing-test/1d058c38f44741e0a3183ebe488302c4.jpg,https://bj.bcebos.com/v1/hnjing-test/d18a5950035f4c75815a371289d23a45.jpg",
                "qualifyName": "法人身份证",
                "qualifyBeginDate": "2018-07-09",
                "qualifyValidDate": "2018-07-31"
            }],
            "employees": {
                "empName": "测试",
                "phone": "15812205665",
                "email": "15814405932@139.com"
            }
        }
        values = json.dumps(parms)
        # 发送服务商接口请求
        fws_test = requests.post(url, data=values, headers=headers)
        result_exp = 200
        result_act = fws_test.status_code
        # print(fws_test.text)
        self.assertEqual(result_exp, result_act, msg="供应商新增失败")
        log.info("服务商已新增成功")

    # 运营管理-合作伙伴管理-不存在的查询
    def test_a003_search(self):
        # 随机生成企业名称
        serach_01 = ''.join(random.sample(['8', '6', '3', '2', '5', '6'], 6))
        serach_02 = '随机查询'
        serach_name = serach_02 + serach_01
        url_01 = 'http://admin.ejw.cn/os/v1/partners?pageNo=1&pageSize=10&partnerType=0010%2C0011%2C0100%2C0101%2C0111%2C0110&partnerName='
        url = url_01 + serach_name
        # 发送服务商接口请求
        qykh_test_01 = requests.get(url, headers=headers)
        qykh_test = qykh_test_01.text
        # 返回状态码信息
        totalCount = qykh_test.split("startRow", 2)[1].split(",", 2)[1].split(":", 2)[1]
        result_exp = 0
        result_act = int(totalCount)
        self.assertEqual(result_exp, result_act, msg='查询的结果与实际结果不一致')
        log.info("合作伙伴管理-不存在的用户查询成功")

    # 运营管理-合作伙伴管理-存在的查询
    def test_a004_search(self):
        conn = MySQL().connect_os1('conn')
        cur = conn.cursor()
        cur.execute("select partner_name from partner where partner_name='竞网测试同步sdf'")
        parnername = str(cur.fetchone()[0])
        url_01 = 'http://admin.ejw.cn/os/v1/partners?pageNo=1&pageSize=10&partnerType=0010%2C0011%2C0100%2C0101%2C0111%2C0110&partnerName='
        url = url_01 + parnername
        # 发送服务商接口请求
        qykh_test_01 = requests.get(url, headers=headers)
        qykh_test = qykh_test_01.text
        # 返回状态码信息
        totalCount = qykh_test.split("startRow", 2)[1].split(",", 2)[1].split(":", 2)[1]
        # 判断当前返回码及字段值
        result_act = int(totalCount)
        result_exp = 1
        self.assertEqual(result_exp, result_act, "查询的日志结果不一致")
        log.info("合作伙伴管理-存在的信息查询成功")

    # 运营管理-企业客户管理-存在的用户查询
    def test_b001_search(self):
        conn = MySQL().connect_portal1('conn')
        cur = conn.cursor()
        cur.execute("select partner_name from partner where `status`=0")
        parnername = str(cur.fetchone()[0])
        url_01 = 'http://admin.ejw.cn/portal/v1/partners?sort=%7B%22gmtCreate%22%3A%22desc%22%7D&status=0&pageNo=1&pageSize=10&partnerName='
        url = url_01 + parnername
        # 发送服务商接口请求
        qykh_test_01 = requests.get(url, headers=headers)
        qykh_test = qykh_test_01.text
        # 判断当前返回码及字段值
        self.assertIn(parnername, qykh_test, msg="没有查询到此用户信息")
        log.info("企业客户管理-存在的用户查询成功")

    # 运营管理-企业客户管理-不存在的用户查询
    def test_b002_search(self):
        # 随机生成企业名称
        serach_01 = ''.join(random.sample(['8', '6', '3', '2', '5', '6', '0', 'a'], 8))
        serach_02 = '企业竞争力'
        serach_name = serach_02 + serach_01
        url_01 = 'http://admin.ejw.cn/portal/v1/partners?sort=%7B%22gmtCreate%22%3A%22desc%22%7D&status=0&pageNo=1&pageSize=10&partnerName='
        url = url_01 + serach_name
        # 发送服务商接口请求
        qykh_test_01 = requests.get(url, headers=headers)
        qykh_test = qykh_test_01.text
        # 返回状态码信息
        totalCount = qykh_test.split("startRow", 2)[1].split(",", 2)[1].split(":", 2)[1]
        result_exp = 0
        self.assertEqual(result_exp, int(totalCount))
        log.info("企业客户管理-不存在的用户查询成功")

    # 运营管理-企业客户管理-合作伙伴管理-企业审核
    def test_b003_search(self):
        # 随机生成社会信用代码
        uscCode_01 = ''.join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 10))
        uscCode_02 = '43062419'
        uscCode = uscCode_01 + uscCode_02

        conn = MySQL().connect_portal1('conn')
        cur = conn.cursor()
        cur.execute(
            "select partner_id,partner_name,area,address,phone from partner where `status`=0 order by gmt_create desc")
        cur_data = cur.fetchone()[0:5]
        print(cur_data)
        partner_id = str(cur_data[0])
        partner_name = cur_data[1]
        area = cur_data[2]
        address = cur_data[3]
        phone = cur_data[4]
        # print(cur_data, partner_id, partner_name, area, address, phone)

        paramas = {"partnerAudit": {"status": 1},
                   "partner": {"status": 1, "partnerName": partner_name, "area": area, "address": address,
                               "phone": phone, "detail": "陈名绑定企业客户", "organizeType": 1, "partnerType": "0001"},
                   "partnerExt": {"standardIndustry": "612"},
                   "partnerQualify": {"qualifyType": 1, "qualifyName": "测试专用", "qualifyValidDate": "2019-07-31",
                                      "qualifyImage": "https://bj.bcebos.com/v1/dev-con/0a64c4444a034356915cf0747317450f.jpg"},
                   "employees": {"status": 1, "sex": 1, "empName": "陈名", "phone": "18686086818",
                                 "email": "15814405932@139.com", "partnerId": 43, "userId": 9},
                   "partnerBusiness": {"organizeName": "陈名绑定企业客户管理员", "registAuthority": "无限网络登记", "organizeType": 1,
                                       "uscCode": uscCode, "companyType": "1111", "registAddress": "121331",
                                       "legalPerson": "张三", "scope": "经营经济任务", "issueAuthority": "",
                                       "approvalDate": "2019-07-31", "registStatus": "无状态", "registCapital": 10000},
                   "partnerQualifys": [{"qualifyType": 1, "qualifyName": "测试专用", "qualifyValidDate": "2019-07-31",
                                        "qualifyImage": "https://bj.bcebos.com/v1/dev-con/0a64c4444a034356915cf0747317450f.jpg"}]}

        url_01 = 'http://admin.ejw.cn/platform/v1/partner/'
        url = url_01 + partner_id + '/audit'
        # 发送服务商接口请求
        qykh_test_01 = requests.put(url, data=json.dumps(paramas), headers=headers)
        # print(qykh_test_01.text)
        result_act = qykh_test_01.status_code
        result_exp = 200
        # 判断当前返回码及字段值
        self.assertEqual(result_exp, result_act, msg='审核原因：数据库已存在相同用户企业或其它参数错误')
        log.info("企业客户管理-合作伙伴管理-企业审核成功")

    # # 运营管理-企业客户管理-合作伙伴管理-企业审核通过-停用
    # def test_b004_search(self):
    #     conn = MySQL().connect_os1('conn')
    #     cur = conn.cursor()
    #     cur.execute("select partner_id, partner_name from partner where `status`=1 and partner_type=0001")
    #     cur_data = cur.fetchone()[0:2]
    #     # print(cur_data)
    #     partner_id = str(cur_data[0])
    #     partner_name = cur_data[1]
    #     print(partner_id, partner_name)
    #     paramas = {"status": 0}
    #     url_01 = 'http://admin.ejw.cn/platform/v1/partner/'
    #     url = url_01 + partner_id + '/status'
    #     # 发送服务商接口请求
    #     shtg = requests.put(url, data=json.dumps(paramas), headers=headers)
    #     # requests.get("http://admin.ejw.cn/os/v1/partners?sort=%7B%22gmtCreate%22%3A%22desc%22%7D&pageSize=10&pageNo=1&partnerType=0001%2C0011%2C0101%2C0111", headers=headers)
    #     result_act = shtg.status_code
    #     result_exp = 200
    #     self.assertEqual(result_exp, result_act)
    #     log.info("企业客户管理-合作伙伴管理-企业审核通过-停用成功")

    # # 运营管理-企业客户管理-合作伙伴管理-企业审核通过-启用
    # def test_b005_search(self):
    #     conn = MySQL().connect_os1('conn')
    #     cur = conn.cursor()
    #     cur.execute("select partner_id, partner_name from partner where `status`=0 and partner_type=0001")
    #     cur_data = cur.fetchone()[0:2]
    #     print(cur_data)
    #     partner_id = str(cur_data[0])
    #     partner_name = cur_data[1]
    #     print(partner_id, partner_name)
    #     paramas = {"status": 1}
    #     url_01 = 'http://admin.ejw.cn/platform/v1/partner/'
    #     url = url_01 + partner_id + '/status'
    #     # 发送服务商接口请求
    #     shtg = requests.put(url, data=json.dumps(paramas), headers=headers)
    #     # requests.get("http://admin.ejw.cn/os/v1/partners?sort=%7B%22gmtCreate%22%3A%22desc%22%7D&pageSize=10&pageNo=1&partnerType=0001%2C0011%2C0101%2C0111", headers=headers)
    #     result_exp = 200
    #     result_act = shtg.status_code
    #     self.assertEqual(result_exp, result_act, msg="企业审核不通过")
    #     log.info("企业" + partner_name + "停用成功")

    # 运营管理-企业客户管理-资质模板管理-新增
    def test_c001_search(self):
        # 随机生成社会信用代码
        tempName_01 = ''.join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 4))
        tempName_02 = '自资名称'
        tempName = tempName_01 + tempName_02
        url = 'http://admin.ejw.cn/platform/v1/qualifytemplate'
        paramas = {"typeId": 96, "tempName": tempName,
                   "tempImage": "http://hnjing-test.bj.bcebos.com/v1/hnjing-test/34b04a41698c4dc28627a19d44801011.jpg"}
        # 发送服务商接口请求
        zzmb = requests.post(url, data=json.dumps(paramas), headers=headers)
        result_exp = 200
        result_act = zzmb.status_code
        # 判断当前返回码及字段值
        self.assertEqual(result_exp, result_act)
        log.info("新增资质模板成功")

    # 产品管理-产品授权-待审核
    def test_d001_spsq_dsh(self):
        conn = MySQL().connect_platform1('conn')
        cur = conn.cursor()
        cur.execute('select record_id,auth_id from product_auth where `status`= 3')
        cur_data = cur.fetchone()
        # print(type(cur_data))
        result_exp = 200
        if cur_data is None:
            # print("执行A部分")
            self.assertNotEqual(result_exp, cur_data, msg="没有需要授权的产品")

        else:
            # print("执行B部分")
            record_id = cur_data[0]
            auth_id = cur_data[1]
            print(record_id, auth_id)
            url_01 = 'http://admin.ejw.cn/platform/v1/productauth/'
            url = url_01 + str(record_id) + '/platformverify'
            paramas = {"status": 5}
            result = requests.put(url, data=json.dumps(paramas), headers=headers)
            result_act = result.status_code
            self.assertEqual(result_exp, result_act, msg="产品授权-审核不通过")
            log.info("产品授权-审核通过")

    # 产品运营-产品审核-待审核
    def test_d002_spsq_dsh(self):
        conn = MySQL().connect_platform1('conn')
        cur = conn.cursor()
        cur.execute('select verify_id,product_id from product_verify where `status` = 0')
        cur_data = cur.fetchone()[0:2]
        verify_id = str(cur_data[0])
        product_id = cur_data[1]
        print(verify_id, product_id)
        url_01 = 'http://admin.ejw.cn/platform/v1/productverify/'
        url = url_01 + verify_id + '?curEmpId=1720'
        paramas = {"status": 1}
        result = requests.put(url, data=json.dumps(paramas), headers=headers)
        result_exp = 200
        result_act = result.status_code
        self.assertEqual(result_exp, result_act)
        print("产品审核通过")

    # 消息管理-手动模板-新增
    def test_e001_zlxgl(self):
        # 随机生成模块名称
        template_01 = ''.join(random.sample(['8', '6', '3', '2', '5', '6'], 4))
        template_02 = '自动化模板auto'
        template = template_02 + template_01
        url = 'http://admin.ejw.cn/msg/v1/msgtemplate'
        parms = {"tempName": template, "msgTitle": template, "msgLevel": 0, "sendSms": 0, "sendMail": 0, "sendMsg": 1,
                 "contentMsg": "<p>自动化随机发送站内消息</p>", "tempType": 0}
        values = json.dumps(parms)
        # 发送服务商接口请求
        fws_test = requests.post(url, data=values, headers=headers)
        result_act = fws_test.status_code
        result_exp = 200
        self.assertEqual(result_exp, result_act, msg="手动模板管理-新增失败")
        log.info("手动模板管理新增成功")

    # 消息管理-模板管理-手动模板-不存在的名称查询
    def test_e002_zlxgl(self):
        keywords = "xxxxxxxxxxxxxxxxxxxxxxxx"
        text = quote(keywords, 'utf-8')
        url_01 = 'http://admin.ejw.cn/msg/v1/msgtemplates?pageNo=1&pageSize=10&sort=%7B%22gmtCreate%22%3A%22desc%22%7D&tempType=0&tempName='
        url = url_01 + text
        # print(url)
        # 发送服务商接口请求
        fws_test = requests.get(url, headers=headers)
        result_act = fws_test.text
        self.assertNotIn(keywords, result_act, "查询到此用户信息")
        log.info("查询成功，没有此用户信息")

    # 消息管理-模板管理-手动模板-存在的名称查询
    def test_e003_zlxgl(self):
        keywords = "自动化模板auto5366"
        text = quote(keywords, 'utf-8')
        url_01 = 'http://admin.ejw.cn/msg/v1/msgtemplates?pageNo=1&pageSize=10&sort=%7B%22gmtCreate%22%3A%22desc%22%7D&tempType=0&tempName='
        url = url_01 + text
        # print(url)
        # 发送服务商接口请求
        fws_test = requests.get(url, headers=headers)
        result_act = fws_test.text
        self.assertIn(keywords, result_act, "实际结果没有此用户名称")
        log.info("没有此用户信息")


if __name__ == '__main__':
    unittest.main()
