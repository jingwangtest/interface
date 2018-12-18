# 运营平台
import requests
import random
import json
import unittest
from comm.login import Zpt
from comm.public_data import MySQL
from comm.Log import Logger
from urllib.parse import quote
import readConfig

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
    # 用户运营-合作伙伴管理-新增合作伙伴
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
            "partner": {"partnerType": "0110", "partnerName": partner_name, "area": "湖南/长沙", "address": "麓谷",
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
        url = 'http://admin.ejw.cn/platform/v1/partnerall?curEmpId=' + adminEmpId
        # 发送服务商接口请求
        qykh_test_01 = requests.post(url, data=json.dumps(paramas), headers=headers)
        print(qykh_test_01.text)
        result_act = qykh_test_01.status_code
        result_exp = 200
        # 判断当前返回码及字段值
        self.assertEqual(result_exp, result_act, msg='审核原因：已存在相同用户企业或其它参数错误')
        log.info("企业客户管理-合作伙伴管理-服务商新增成功")

    # 用户运营-合作伙伴管理-不存在的查询
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

    # 用户运营-合作伙伴管理-存在的查询
    def test_a004_search(self):
        conn = MySQL().connect_os()
        cur = conn.cursor()
        cur.execute("select partner_name from partner where partner_type = 0110;")
        sql_result = cur.fetchone()[0:1]
        parnername = sql_result[0]
        url_01 = 'http://admin.ejw.cn/os/v1/partners?pageNo=1&pageSize=10&partnerType=0010%2C0011%2C0100%2C0101%2C0111%2C0110&partnerName='
        url = url_01 + parnername
        print(url)
        # 发送服务商接口请求
        qykh_test_01 = requests.get(url, headers=headers)
        qykh_test = qykh_test_01.text
        print(qykh_test)
        self.assertIn(parnername, qykh_test, "查询的日志结果不一致")
        log.info("合作伙伴管理-存在的信息查询成功")

    # 用户运营-企业客户管理-存在的用户查询
    def test_b001_search(self):
        try:
            conn = MySQL().connect_portal()
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
        except TypeError:
            log.info("企业客户管理没有用户信息")

    # 用户运营-企业客户管理-不存在的用户查询
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

    # 用户运营-企业客户管理-企业审核
    def test_b003_search(self):
        try:
            conn = MySQL().connect_portal()
            cur1 = conn.cursor()
            cur1.execute(
                'select partner_id,partner_name,area,address,phone from partner where status=0 order by gmt_create desc')
            par_result = cur1.fetchone()
            partner_id, partner_name, area, address, phone = par_result[0], par_result[1], par_result[2], par_result[3], \
                                                             par_result[4]
            print(partner_id, partner_name, area, address, phone)
            url_01 = "http://admin.ejw.cn/platform/v1/partner/"
            url = url_01 + str(partner_id) + '/audit?curEmpId=' + adminEmpId
            print(url)
            params = {"partner": {"partnerName": partner_name, "area": area, "address": address, "phone": phone,
                                  "detail": "", "partnerType": "0001", "organizeType": 1},
                      "employees": {"empName": "盛秀玲", "phone": "15074980908", "email": "", "partnerId": 157,
                                    "userId": 92},
                      "partnerExt": {"standardIndustry": "1"},
                      "partnerBusiness": {"organizeType": 1, "uscCode": "066554132665266565", "businessCode": "",
                                          "companyType": "长城", "registAddress": "台阶", "legalPerson": "灰尘",
                                          "scope": "功能",
                                          "registAuthority": "功勋", "approvalDate": "2018-11-12", "registStatus": "正常",
                                          "registCapital": 40000000}, "partnerQualifys": [
                    {"qualifyType": 1, "qualifyName": "天天向上", "qualifyValidDate": "2019-11-30",
                     "qualifyImage": "https://bj.bcebos.com/v1/hnjing-test/ddf61aa7eaa44621918daa0738ac8b49.jpg?authorization=bce-auth-v1%2Fed6cb82c3c054636aec25bdbc65d7c10%2F2018-11-05T09%3A40%3A35Z%2F-1%2F%2F0aedf26ba5e0a2a625ed4150e27d28b1b57551b920fc694967fe5431c643c903"}],
                      "partnerAudit": {"status": 1}}
            # print(json.dumps(params, ensure_ascii=False, indent=2))
            result_act = requests.put(url, data=json.dumps(params), headers=headers).status_code
            result_exp = 200
            self.assertEqual(result_exp, result_act, msg="返回响应码不一致，请检查是否有错")
            log.info("用户运营-企业客户管理-企业审核通过")
        except TypeError:
            log.info("数据库查询信息为空")

    # 产品运营-产品授权审核-待审核
    def test_b004_search(self):
        conn = MySQL().connect_platform()
        cur = conn.cursor()
        cur.execute(
            "select record_id from product_auth where `status`=3;")
        cur_data = cur.fetchone()
        # print(cur_data)
        if cur_data == None:
            result_exp = None
            self.assertEqual(result_exp, cur_data)
            log.info("产品运营-产品授权审核-待审核-没有需要审核的产品信息")
        else:
            record_id = str(cur_data[0])
            paramas = {"status": 5}
            url_01 = 'http://admin.ejw.cn/platform/v1/productauth/'
            url = url_01 + record_id + '/platformverify?curEmpId=' + adminEmpId
            # print(url)
            # 发送服务商接口请求
            qykh_test_01 = requests.put(url, data=json.dumps(paramas), headers=headers)
            # print(qykh_test_01.text)
            result_act = qykh_test_01.status_code
            result_exp = 200
            # 判断当前返回码及字段值
            self.assertEqual(result_exp, result_act, msg='审核失败：没有存在的企业或其它参数错误')
            log.info("产品运营-产品授权审核-待审核-产品授权审核成功")

    # 用户运营-企业客户管理-合作伙伴管理-企业审核通过-停用
    def test_b005_search(self):
        conn = MySQL().connect_os()
        cur = conn.cursor()
        cur.execute("select partner_id, partner_name from partner where `status`=1 and partner_type=0001")
        cur_data = cur.fetchone()
        print(cur_data)
        partner_id = str(cur_data[0])
        partner_name = cur_data[1]
        print(partner_id, partner_name)
        paramas = {"status": 0}
        url_01 = 'http://admin.ejw.cn/platform/v1/partner/'
        url = url_01 + partner_id + '/status'
        # 发送服务商接口请求
        shtg = requests.put(url, data=json.dumps(paramas), headers=headers)
        result_act = shtg.status_code
        result_exp = 200
        self.assertEqual(result_exp, result_act)
        log.info("企业客户管理-合作伙伴管理-企业审核通过-停用成功")

    # 用户运营-企业客户管理-合作伙伴管理-企业审核通过-启用
    def test_b006_search(self):
        conn = MySQL().connect_os()
        cur = conn.cursor()
        url_sql = "select partner_id, partner_name from partner where `status`=0 and partner_type=0001"
        cur.execute(url_sql)
        cur_data = cur.fetchone()
        print(cur_data)
        partner_id = str(cur_data[0])
        partner_name = cur_data[1]
        print(partner_id, partner_name)
        paramas = {"status": 1}
        url_01 = 'http://admin.ejw.cn/platform/v1/partner/'
        url = url_01 + partner_id + '/status'
        # 发送服务商接口请求
        shtg = requests.put(url, data=json.dumps(paramas), headers=headers)
        result_act = shtg.status_code
        result_exp = 200
        self.assertEqual(result_exp, result_act)
        log.info("企业" + partner_name + "停用成功")

    # 用户运营-企业客户管理-企业审核不通过-删除
    def test_b007_search(self):
        try:
            conn = MySQL().connect_portal()
            cur1 = conn.cursor()
            cur1.execute(
                'select partner_id from partner where `status`=2 ORDER BY gmt_create DESC;')
            par_result = cur1.fetchone()
            partner_id = par_result[0]
            url_01 = "http://admin.ejw.cn/portal/v1/partnerall/"
            url = url_01 + str(partner_id)
            result_act = requests.delete(url, headers=headers).status_code
            result_exp = 200
            self.assertEqual(result_exp, result_act, msg="返回响应码不一致，请检查是否有错")
            log.info("用户运营-企业客户管理-企业审核不通过-删除通过")
        except TypeError:
            log.info("数据库查询信息为空,没有需要删除的企业客户")

    # 系统管理-平台配置-资质模块设置-新增
    def test_c001_search(self):
        conn = MySQL().connect_platform()
        cur = conn.cursor()
        cur.execute('select type_id from qualify_type ORDER BY type_id DESC;')
        sql_result = cur.fetchone()[0:1]
        typeId = sql_result[0]
        # 随机生成社会信用代码
        tempName_01 = ''.join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 4))
        tempName_02 = '自资名称'
        tempName = tempName_01 + tempName_02
        url = 'http://admin.ejw.cn/platform/v1/qualifytemplate'
        paramas = {"typeId": typeId, "tempName": tempName,
                   "tempImage": "http://hnjing-test.bj.bcebos.com/v1/hnjing-test/34b04a41698c4dc28627a19d44801011.jpg"}
        # 发送服务商接口请求
        zzmb = requests.post(url, data=json.dumps(paramas), headers=headers)
        result_exp = 200
        result_act = zzmb.status_code
        # 判断当前返回码及字段值
        self.assertEqual(result_exp, result_act, msg="新增模板失败，请检查失败原因")
        log.info("系统管理-平台配置-资质模块设置-新增资质模块成功")

    # 产品管理-产品授权-待审核
    def test_d001_spsq_dsh(self):
        conn = MySQL().connect_platform()
        cur = conn.cursor()
        cur.execute('select record_id,auth_id from product_auth where `status`= 3')
        cur_data = cur.fetchone()
        # print(type(cur_data))
        result_exp = 200
        if cur_data is None:
            # print("执行A部分")
            self.assertNotEqual(result_exp, cur_data, msg="没有需要授权的产品")
            log.info("没有需要授权的产品")

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

    # 产品运营-上下架审核-待审核
    def test_d002_spsq_dsh(self):
        conn = MySQL().connect_platform()
        cur = conn.cursor()
        cur.execute('select verify_id,product_id from product_verify where `status` = 0')
        cur_data = cur.fetchone()[0:2]
        verify_id = str(cur_data[0])
        product_id = cur_data[1]
        print(verify_id, product_id)
        url_01 = 'http://admin.ejw.cn/platform/v1/productverify/'
        url = url_01 + verify_id + '?curEmpId=' + adminEmpId
        paramas = {"status": 1}
        result = requests.put(url, data=json.dumps(paramas), headers=headers)
        result_exp = 200
        result_act = result.status_code
        self.assertEqual(result_exp, result_act, msg="验证结果不一致")
        log.info("运营平台产品上下架审核能过，信息如下")
        log_exp.info(result_exp)
        log_act.info(result_act)

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
        keywords = "自动化模板auto6532"
        text = quote(keywords, 'utf-8')
        url_01 = 'http://admin.ejw.cn/msg/v1/msgtemplates?pageNo=1&pageSize=10&sort=%7B%22gmtCreate%22%3A%22desc%22%7D&tempType=0&tempName='
        url = url_01 + text
        # print(url)
        # 发送服务商接口请求
        fws_test = requests.get(url, headers=headers)
        result_act = fws_test.text
        self.assertIn(keywords, result_act, "实际结果没有此用户名称")
        log.info("没有此用户信息")

    # 用户运营-标准订单管理-输入正确的订单编号进行查询
    def test_f001_search(self):
        spOrderId = 's1540379515447'
        url_01 = 'http://admin.ejw.cn/order/v1/orders?spOrderId='
        url = url_01 + spOrderId
        # 发送接口请求
        result_act = requests.get(url, headers=headers).text
        # 结果转换为json格式
        result_act_act = json.loads(result_act)
        # 获取data中第一个列表中的spOrderId字段
        result = result_act_act["data"][0]["spOrderId"]
        print(result, spOrderId)
        self.assertEqual(spOrderId, result, msg="成功查询到该订单信息")
        print("续期订单管理-正确的订单编号查询成功。订单编号为：" + spOrderId)

    # 用户运营-标准订单管理-输入不存在的订单编号进行查询
    def test_f002_search(self):
        spOrderId = 's154037951544701'
        url_01 = 'http://admin.ejw.cn/order/v1/orders?spOrderId='
        url = url_01 + spOrderId
        # 发送服务商接口请求
        result_act = requests.get(url, headers=headers)
        result = result_act.text
        self.assertNotIn(spOrderId, result, msg="没有查询到该订单信息")
        print("标准订单管理-不存在的订单编号查询成功。不存在该订单，订单编号为：" + spOrderId)

    # 用户运营-充值订单管理-输入正确的订单编号进行查询
    def test_f003_search(self):
        chargeOrderId = 'a1540348408106'
        url_01 = 'http://admin.ejw.cn/order/v1/chargeorders?chargeOrderId='
        url = url_01 + chargeOrderId
        # 发送服务商接口请求
        result_act = requests.get(url, headers=headers).text
        # 结果转换为json格式
        result_act_act = json.loads(result_act)
        # 获取data中第一个列表中的spOrderId字段
        result = result_act_act["data"][0]["chargeOrderId"]
        print(result, chargeOrderId)
        self.assertEqual(chargeOrderId, result, msg="成功查询到该订单信息")
        print("续期订单管理-正确的订单编号查询成功。订单编号为：" + chargeOrderId)

    # 用户运营-充值订单管理-输入不存在的订单编号进行查询
    def test_f004_search(self):
        chargeOrderId = 'a154034840810601'
        url_01 = 'http://admin.ejw.cn/order/v1/chargeorders?chargeOrderId='
        url = url_01 + chargeOrderId
        # 发送接口请求
        result_act = requests.get(url, headers=headers)
        result = result_act.text
        self.assertNotIn(chargeOrderId, result, msg="成功查询到该订单信息")
        print("充值订单管理-不存在的订单编号查询成功。不存在该订单，订单编号为：" + chargeOrderId)

    # 用户运营-续期订单管理-输入正确的订单编号进行查询
    def test_f005_search(self):
        srvOrderId = 'b1540372446592'
        url_01 = 'http://admin.ejw.cn/order/v1/srvorders?srvOrderId='
        url = url_01 + srvOrderId
        # 发送接口请求
        result_act = requests.get(url, headers=headers).text
        # 结果转换为json格式
        result_act_act = json.loads(result_act)
        # 获取data中第一个列表中的spOrderId字段
        result = result_act_act["data"][0]["srvOrderId"]
        print(result, srvOrderId)
        self.assertEqual(srvOrderId, result, msg="成功查询到该订单信息")
        print("续期订单管理-正确的订单编号查询成功。订单编号为：" + srvOrderId)

    # 用户运营-续期订单管理-输入不存在的订单编号进行查询
    def test_f006_search(self):
        srvOrderId = 'b154037244659201'
        url_01 = 'http://admin.ejw.cn/order/v1/srvorders?srvOrderId='
        url = url_01 + srvOrderId
        # 发送接口请求
        result_act = requests.get(url, headers=headers)
        result = result_act.text
        self.assertNotIn(srvOrderId, result, msg="成功查询到该订单信息")
        log.info("续期订单管理-不存在的订单编号查询成功。不存在该订单，订单编号为：" + srvOrderId)

    # 订单管理-仲裁管理-同意退款
    def test_h001_search(self):
        try:
            conn = MySQL().connect_platform()
            cur = conn.cursor()
            sql = "select examine_auth_id from refund_examine where examine_state=0 and order_comp_id=" + cuComId
            cur.execute(sql)
            ordering = cur.fetchone()[0:1]
            examine_auth_id = str(ordering[0])
            print(examine_auth_id)
            url = "http://admin.ejw.cn/platform/v1/arbitrate/" + examine_auth_id + "?curEmpId=" + adminEmpId
            params = {"examineState": 1, "examineSuggest": "", "refundAmount": 1, "examineEmpId": int(adminEmpId),
                      "examineEmpName": cuEmpName, "spOrderStageNo": 1, "orderEmpId": int(cuEmpId),
                      "orderCompId": int(cuComId), "useCost": 0,
                      "refundFee": 0}
            print(params)
            result_act = requests.put(url, data=json.dumps(params), headers=headers)
            # print(result_act.text)
            result_exp = 200
            self.assertEqual(result_exp, result_act.status_code, msg='发送仲裁失败')
            log.info("申请仲裁成功")
        except TypeError:
            log.info("没有找到需要仲裁的订单")


if __name__ == '__main__':
    unittest.main()
