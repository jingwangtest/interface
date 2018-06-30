# 运营平台-合作伙伴管理
import requests
import random
import json
import unittest
from comm.login import testlogin_001
from comm.sp_data import MySQL

# 请求头信息
token = testlogin_001().test_adminlogin('token')
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'token': token
}


class admin_yygl(unittest.TestCase):
    # 运营管理-合作伙伴管理-新增服务商
    def test_a001_yygl(self):
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
            "partner": {"partnerType": "0100", "partnerName": prodctName, "area": "湖南/长沙/岳麓区", "address": "岳麓麓谷高新产业区",
                        "phone": "0731-77777777", "detail": "竞网科技有限公司", "level": 5},
            "partnerExt": {"standardIndustry": "552", "category": "44"}, "partnerQualify": {
                "qualifyImage": "http://hnjing-test.bj.bcebos.com/v1/hnjing-test/d544d89bbf89455a9d91e0a5405400eb.jpg",
                "qualifyName": "楼想", "qualifyValidDate": "2018-09-30T00:00:00+08:00", "qualifyType": 1},
            "partnerBusiness": {"qualifyName": "楼想", "companyType": "有限责任公司(自然人投资或控股",
                                "registAddress": "湖南省长沙市岳麓区岳麓街道潇湘中路328号麓枫和苑1008-1010房（集群注册）", "legalPerson": "樊润霞",
                                "registAuthority": "长沙市工商行政管理局岳麓分局", "approvalDate": "2018-05-08T00:00:00+08:00",
                                "registStatus": "存续", "registCapital": 50, "scope": "存续",
                                "businessLicense": "businessLicense", "uscCode": uscCode,
                                "businessCode": ""},
            "employees": {"empName": "竞网科技有限公司", "phone": "13025406605", "email": "15814405932@139.com"}}
        values = json.dumps(parms)
        # 发送服务商接口请求
        fws_test = requests.post(url, data=values, headers=headers)
        # 返回状态码信息
        # print(fws_test.text)
        # s = json.loads(fws_test)          赋值所有的结果值
        # att = s["partner"]["partnerName"] 此消息获取json下的用户字段值
        result_exp = 200
        result_act = fws_test.status_code
        self.assertEqual(result_exp, result_act)
        print("新增服务商成功ABCDEFG111abcd")

    # 运营管理-合作伙伴管理-新增供应商
    def test_a002_yygl(self):
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
            "partner": {"partnerType": "0010", "partnerName": prodctName, "area": "湖南/长沙/岳麓区", "address": "岳麓麓谷高新产业区",
                        "phone": "0731-77777777", "detail": "竞网科技有限公司", "level": 5},
            "partnerExt": {"standardIndustry": "552", "category": "44"}, "partnerQualify": {
                "qualifyImage": "http://hnjing-test.bj.bcebos.com/v1/hnjing-test/d544d89bbf89455a9d91e0a5405400eb.jpg",
                "qualifyName": "楼想", "qualifyValidDate": "2018-09-30T00:00:00+08:00", "qualifyType": 1},
            "partnerBusiness": {"qualifyName": "楼想", "companyType": "有限责任公司(自然人投资或控股",
                                "registAddress": "湖南省长沙市岳麓区岳麓街道潇湘中路328号麓枫和苑1008-1010房（集群注册）", "legalPerson": "樊润霞",
                                "registAuthority": "长沙市工商行政管理局岳麓分局", "approvalDate": "2018-05-08T00:00:00+08:00",
                                "registStatus": "存续", "registCapital": 50, "scope": "存续",
                                "businessLicense": "businessLicense", "uscCode": uscCode,
                                "businessCode": ""},
            "employees": {"empName": "竞网科技有限公司", "phone": "13025406605", "email": "15814405932@139.com"}}
        values = json.dumps(parms)
        # 发送服务商接口请求
        fws_test = requests.post(url, data=values, headers=headers)
        # 返回状态码信息
        # print(fws_test.text)
        # s = json.loads(fws_test)          赋值所有的结果值
        # att = s["partner"]["partnerName"] 此消息获取json下的用户字段值
        result_exp = 200
        result_act = fws_test.status_code
        self.assertEqual(result_exp, result_act)
        print("新增供应商成功")

    # 运营管理-合作伙伴管理-不存在的查询
    def test_a003_search(self):
        # 随机生成企业名称
        serach_01 = ''.join(random.sample(['8', '6', '3', '2', '5', '6'], 6))
        serach_02 = '随机查询'
        serach_name = serach_02 + serach_01
        url_01 = 'http://admin.ejw.cn/os/v1/partners?pageSize=10&pageNo=1&partnerType=0010%2C0011%2C0100%2C0101%2C0111%2C0110&partnerName='
        url = url_01 + serach_name
        # 发送服务商接口请求
        qykh_test_01 = requests.get(url, headers=headers)
        qykh_test = qykh_test_01.text
        # 返回状态码信息
        totalCount = qykh_test.split("startRow", 2)[1].split(",", 2)[1].split(":", 2)[1]
        result_exp = 0
        result_act = int(totalCount)
        self.assertEqual(result_exp, result_act, msg='查询的结果与实际结果不一致')

    # 运营管理-合作伙伴管理-存在的查询
    def test_a004_search(self):
        conn = MySQL().connect_os1('conn')
        cur = conn.cursor()
        cur.execute("select partner_name from partner")
        parnername = str(cur.fetchone()[0])
        url_01 = 'http://admin.ejw.cn/os/v1/partners?pageSize=10&pageNo=1&partnerType=0010%2C0011%2C0100%2C0101%2C0111%2C0110&partnerName='
        url = url_01+parnername
        # 发送服务商接口请求
        qykh_test_01 = requests.get(url, headers=headers)
        qykh_test = qykh_test_01.text
        # 返回状态码信息
        totalCount = qykh_test.split("startRow", 2)[1].split(",", 2)[1].split(":", 2)[1]
        # 判断当前返回码及字段值
        result_act = int(totoalCount)
        result_exp = 1
        self.assertEqual(result_exp, result_act, "查询的日志结果不一致")
        # if qykh_test_01.status_code == 200 and int(totalCount) == 1:
        #     print("企业用户"+parnername+"成功")
        # else:
        #     print("企业用户"+parnername+"失败")

    # 运营管理-企业客户管理-存在的用户查询
    def test_b001_search(self):
        conn = MySQL().connect_portal1('conn')
        cur = conn.cursor()
        cur.execute("select partner_name from partner where `status`=0")
        parnername = str(cur.fetchone()[0])
        url_01 = 'http://admin.ejw.cn/portal/v1/partners?sort=%7B%22gmtCreate%22%3A%22desc%22%7D&status=0&pageNo=1&pageSize=10&partnerName='
        url = url_01+parnername
        # 发送服务商接口请求
        qykh_test_01 = requests.get(url, headers=headers)
        qykh_test = qykh_test_01.text
        # 判断当前返回码及字段值
        self.assertIn(parnername, qykh_test, msg="没有查询到此用户信息")

    # 运营管理-企业客户管理-不存在的用户查询
    def test_b002_search(self):
        # 随机生成企业名称
        serach_01 = ''.join(random.sample(['8', '6', '3', '2', '5', '6', '0', 'a'], 8))
        serach_02 = '企业竞争力'
        serach_name = serach_02 + serach_01
        url_01 = 'http://admin.ejw.cn/portal/v1/partners?sort=%7B%22gmtCreate%22%3A%22desc%22%7D&status=0&pageNo=1&pageSize=10&partnerName='
        url = url_01+serach_name
        # 发送服务商接口请求
        qykh_test_01 = requests.get(url, headers=headers)
        qykh_test = qykh_test_01.text
        # 返回状态码信息
        totalCount = qykh_test.split("startRow", 2)[1].split(",", 2)[1].split(":", 2)[1]
        result_exp = 200;
        self.assertEqual(result_exp, totalCount)
        # if qykh_test_01.status_code == 200 and int(totalCount) == 0:
        #     print("不存在企业用户"+serach_name+"查询成功")
        # else:
        #     print("不存在企业用户"+serach_name+"查询失败")

    # 运营管理-企业客户管理-合作伙伴管理-企业审核
    def test_b003_search(self):
        # 随机生成社会信用代码
        uscCode_01 = ''.join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 10))
        uscCode_02 = '43062419'
        uscCode = uscCode_01 + uscCode_02

        conn = MySQL().connect_portal1('conn')
        cur = conn.cursor()
        cur.execute("select partner_id,partner_name,area,address,phone from partner where `status`=0")
        cur_data = cur.fetchone()[0:5]
        partner_id = str(cur_data[0])
        partner_name = cur_data[1]
        area = cur_data[2]
        address = cur_data[3]
        phone = cur_data[4]
        # print(cur_data, partner_id, partner_name, area, address, phone)

        paramas = {"partnerAudit": {"status": 1, "auditUser": 13},
                   "partner": {"status": 1, "partnerName": partner_name, "area": area, "address": address,
                               "phone": phone,
                               "detail": "", "organizeType": 1, "partnerType": "0001"},
                   "partnerExt": {"standardIndustry": "612"},
                   "partnerQualify": {"qualifyType": 1, "qualifyName": partner_name,
                                      "qualifyValidDate": "2019-05-31T00:00:00+08:00",
                                      "qualifyImage": "https://bj.bcebos.com/v1/dev-con/4c62757db4204f33907aa7eb43c1d6bd.jpg"},
                   "employees": {"status": 1, "sex": 1, "empName": "威胜管理员", "phone": "15074980908", "email": "",
                                 "partnerId": 4},
                   "partnerBusiness": {"organizeName": "威胜电子", "registAuthority": "岳麓区地点", "organizeType": 1,
                                       "uscCode": uscCode, "companyType": "1", "registAddress": "长沙岳麓区",
                                       "legalPerson": "楼想",
                                       "scope": "长沙岳麓区", "issueAuthority": "",
                                       "approvalDate": "2020-05-09T00:00:00+08:00",
                                       "registStatus": "1", "registCapital": 5000}}

        url_01 = 'http://admin.ejw.cn/platform/v1/partner/'
        url = url_01 + partner_id + '/audit'
        # 发送服务商接口请求
        qykh_test_01 = requests.put(url, data=json.dumps(paramas), headers=headers)
        result_act = qykh_test_01.status_code
        result_exp = 200
        # 判断当前返回码及字段值
        self.assertEqual(result_exp, result_act, msg='审核不通过')

    # 运营管理-企业客户管理-合作伙伴管理-企业审核通过-停用
    def test_b004_search(self):
        conn = MySQL().connect_os1('conn')
        cur = conn.cursor()
        cur.execute("select partner_id, partner_name from partner where `status`=1 and partner_type=0001")
        cur_data = cur.fetchone()[0:2]
        # print(cur_data)
        partner_id = str(cur_data[0])
        partner_name = cur_data[1]
        print(partner_id, partner_name)
        paramas = {"status": 0}
        url_01 = 'http://admin.ejw.cn/platform/v1/partner/'
        url = url_01 + partner_id + '/status'
        # 发送服务商接口请求
        shtg = requests.put(url, data=json.dumps(paramas), headers=headers)
        # requests.get("http://admin.ejw.cn/os/v1/partners?sort=%7B%22gmtCreate%22%3A%22desc%22%7D&pageSize=10&pageNo=1&partnerType=0001%2C0011%2C0101%2C0111", headers=headers)
        result_act = shtg.status_code
        result_exp = 200
        self.assertEqual(result_exp, result_act)

    # 运营管理-企业客户管理-合作伙伴管理-企业审核通过-启用
    def test_b005_search(self):
        conn = MySQL().connect_os1('conn')
        cur = conn.cursor()
        cur.execute("select partner_id, partner_name from partner where `status`=0 and partner_type=0001")
        cur_data = cur.fetchone()[0:2]
        # print(cur_data)
        partner_id = str(cur_data[0])
        partner_name = cur_data[1]
        print(partner_id, partner_name)
        paramas = {"status": 1}
        url_01 = 'http://admin.ejw.cn/platform/v1/partner/'
        url = url_01 + partner_id + '/status'
        # 发送服务商接口请求
        shtg = requests.put(url, data=json.dumps(paramas), headers=headers)
        # requests.get("http://admin.ejw.cn/os/v1/partners?sort=%7B%22gmtCreate%22%3A%22desc%22%7D&pageSize=10&pageNo=1&partnerType=0001%2C0011%2C0101%2C0111", headers=headers)
        result_exp = 200
        result_act = shtg.status_code
        self.assertEqual(result_exp, result_act, msg=企业审核不通过)

    # 运营管理-企业客户管理-资质模板管理-新增
    def test_c001_search(self):
        # 随机生成社会信用代码
        tempName_01 = ''.join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 4))
        tempName_02 = '自资名称'
        tempName= tempName_01 + tempName_02
        url = 'http://admin.ejw.cn/platform/v1/qualifytemplate'
        paramas = {"typeId": 96, "tempName": tempName,
                   "tempImage": "http://hnjing-test.bj.bcebos.com/v1/hnjing-test/34b04a41698c4dc28627a19d44801011.jpg"}
        # 发送服务商接口请求
        zzmb = requests.post(url, data=json.dumps(paramas), headers=headers)
        result_exp = 200
        result_act = zzmb.status_code
        # 判断当前返回码及字段值
        self.assertEqual(result_exp, result_act)
        print("新增资质模板成功")

    # 产品管理-产品授权-待审核
    def test_d001_spsq_dsh(self):
        conn = MySQL().connect_platform1('conn')
        cur = conn.cursor()
        cur.execute('select record_id,auth_id from product_auth where `status`= 3')
        cur_data = cur.fetchone()[0:2]
        record_id = str(cur_data[0])
        auth_id = cur_data[1]
        # print(record_id, auth_id)
        url_01 = 'http://admin.ejw.cn/platform/v1/productauth/'
        url = url_01 + record_id + '/platformverify'
        paramas = {"status": 5}
        result = requests.put(url, data=json.dumps(paramas), headers=headers)
        result_exp = 200
        result_act = result.status_code
        self.assertEqual(result_exp, result_act)
        print("产品授权通过")

    # 产品管理-产品审核-待审核
    def test_d002_spsq_dsh(self):
        conn = MySQL().connect_platform1('conn')
        cur = conn.cursor()
        cur.execute('select verify_id,product_id from product_verify where `status` = 0')
        cur_data = cur.fetchone()[0:2]
        verify_id = str(cur_data[0])
        product_id = cur_data[1]
        print(verify_id, product_id)
        url_01 = 'http://admin.ejw.cn/platform/v1/productverify/'
        url = url_01 + verify_id
        paramas = {"status": 1}
        result = requests.put(url, data=json.dumps(paramas), headers=headers)
        result_exp = 200
        result_act = result.status_code
        self.assertEqual(result_exp, result_act)
        print("产品审核通过")

    # 站内信管理-手动模板管理-新增
    def test_e001_zlxgl(self):
        # 随机生成模块名称
        template_01 = ''.join(random.sample(['8', '6', '3', '2', '5', '6'], 4))
        template_02 = '自动化模板auto'
        template = template_02 + template_01
        url = 'http://admin.ejw.cn/msg/v1/msgtemplate'
        parms = {"tempType": 1, "title": template, "content": "自动化模板信息"}
        values = json.dumps(parms)
        # 发送服务商接口请求
        fws_test = requests.post(url, data=values, headers=headers)
        result_act = fws_test.status_code
        result_exp = 200
        self.assertEqual(result_exp, result_act)
        print("手动模板管理新增成功")

    # 站内信管理-手动模板管理-不存在的名称查询
    def test_e002_zlxgl(self):
        keywords = "xxxxxxxxxxxxxxxxxxxxxxxx"
        url_01 = 'http://admin.ejw.cn/msg/v1/msgtemplates?tempType=1&pageNo=1&pageSize=10&sort=%7B%22gmtCreate%22%3A%22desc%22%7D&keywords='
        url = url_01 + keywords
        # 发送服务商接口请求
        fws_test = requests.get(url, headers=headers)
        result_act = fws_test.text
        self.assertIn(keywords, result_act)
        print("没有此用户信息")

    # 站内信管理-手动模板管理-已存在的查询
    def test_e003_zlxgl(self):
        keywords = "自动化模板auto"
        url_01 = 'http://admin.ejw.cn/msg/v1/msgtemplates?tempType=1&pageNo=1&pageSize=10&sort=%7B%22gmtCreate%22%3A%22desc%22%7D&keywords='
        url = url_01 + keywords
        # 发送服务商接口请求
        fws_test = requests.get(url, headers=headers)
        result_act = fws_test.text
        self.assertIn(keywords, result_act)
        print("已存在的用户查询成功")

    # 站内信管理-手动模板管理-已存在的查询
    def test_e004_zlxgl(self):
        title_01 = ''.join(random.sample(['8', '6', '3', '2', '5', '6'], 4))
        title_02 = '公告验证测试'
        title = title_02+title_01
        url = 'http://admin.ejw.cn/msg/v1/platform/sendmessage'
        data = {"receiverType": "00001", "title": title, "content": "公告验证测试"}
        # 发送服务商接口请求
        fws_test = requests.post(url, data=json.dumps(data),  headers=headers)
        result_act = fws_test.text
        self.assertIn(title, result_act)
        print("已存在的用户查询成功")

    # 站内信管理-手动模板管理-不存在的查询
    def test_e005_zlxgl(self):
        keywords = "公告验证测试"
        url_01 = 'http://admin.ejw.cn/msg/v1/sendmessages?keywords=xxxxxxxx&pageNo=1&pageSize=10&status=1&sort=%7B%22gmtCreate%22%3A%22desc%22%7D'
        url = url_01 + keywords
        # 发送服务商接口请求
        fws_test = requests.get(url, headers=headers)
        result_act = fws_test.text
        self.assertIn(keywords, result_act)
        print("不存在的用户查询成功")


if __name__ == '__main__':
    unittest.main()




