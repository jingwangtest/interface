import requests
import unittest
import json
import random
import time
from comm.public_data import MySQL
from comm.login import Zpt
from comm.Log import Logger
import readConfig

# 获取配置文件地址url
localReadConfig = readConfig.ReadConfig()
token = Zpt().cu_login()

# 指定头文件
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'token': token
}

# 指定当前环境的spId、spComId、spName、cuId、cuComId、cuName
spId = localReadConfig.read_sp_com_id()
spName = localReadConfig.read_sp_com_name()
cuComId = localReadConfig.read_cu_com_id()
cuComName = localReadConfig.read_cu_com_name()
cuEmpId = localReadConfig.read_cu_emp_id()
cuEmpName = localReadConfig.read_cu_emp_name()


class Cu(unittest.TestCase):
    # 企业客户入驻申请
    def test_a001_search(self):
        global log, log_exp, log_act
        log_exp = Logger(logger="企业平台_预期结果").getlog()
        log_act = Logger(logger="企业平台_实际结果").getlog()
        log = Logger(logger="企业平台").getlog()
        # 设置企业客户名称
        customName_01 = ''.join(random.sample(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 3))
        customName_02 = '企业入驻申请自动化测试'
        customName = customName_02 + customName_01
        url = 'http://auth.ejw.cn/portal/v1/partnerall'
        paramas = {"partner": {"partnerName": customName, "area": "湖南/长沙/岳麓区", "address": "麓谷广场",
                               "phone": "0731-2574155", "organizeType": 1, "status": 0, "detail": ""},
                   "partnerExt": {"standardIndustry": "9"},
                   "partnerQualify": {
                       "qualifyImage": "https://bj.bcebos.com/v1/hnjing-test/621fe6470e7c469082d5d4cc87363697.jpg?authorization=bce-auth-v1%2Fed6cb82c3c054636aec25bdbc65d7c10%2F2018-11-20T06%3A32%3A03Z%2F-1%2F%2Fcae98671ac479f0dfb7ce7c0cba734c770d1f583fc275424ce2a9f9b41879012"},
                   "employee": {"empName": "盛秀玲", "phone": "15074980908", "status": 1, "sex": 1, "userId": 164}}
        # 发送接口请求
        qyrz = requests.post(url, data=json.dumps(paramas), headers=headers)
        # 设置预期的状态码是 200
        result_exp = 200
        # 获取实际返回的状态码
        result_act = qyrz.status_code
        # 判断实际返回的状态码是否与预期设置的状态码相同
        self.assertEqual(result_exp, result_act)
        log_exp.info(customName)
        log_act.info(qyrz.text)
        log.info("企业客户名称为：" + customName)

    # 外商城商品加入购物车
    def test_b001_shop(self):
        conn = MySQL.connect_mall()
        cur = conn.cursor()
        sql = "select t.product_uuid, t.product_spec_uuid from shoping_info t where t.sp_id=" + spId + " and emp_id=" + \
              cuEmpId
        cur.execute(sql)
        sql_result = cur.fetchone()[0:2]
        productUuid = sql_result[0]
        productSpecUuid = sql_result[1]
        url = "http://www.ejw.cn/shopingcart/" + cuComId
        params = {"productUuid": productUuid, "productSpecUuid": productSpecUuid,
                  "spId": int(spId),
                  "compId": int(cuComId), "empId": int(cuEmpId)}
        result = requests.post(url, data=json.dumps(params), headers=headers).text
        result_exp_pro = "01541123570722"
        # print(result_exp_pro, result_act_pro)
        self.assertIn(result_exp_pro, result, msg="请求参数异常或加入购物车失败")
        log.info("外商城商品加入购物车")
        log_exp.info(result_exp_pro)
        log_act.info(result)

    # 企业平台删除购物车
    def test_b002_shop(self):
        try:
            conn = MySQL().connect_mall()
            cur = conn.cursor()
            cur.execute(
                'select rec_id from shoping_info t where t.sp_id = "' + spId + '" and t.emp_id= "' + cuEmpId + '"')
            rec_id = str(cur.fetchone()[0])
            url = "http://cu.ejw.cn/mall/v1/shopingcart/" + rec_id
            result = requests.delete(url, headers=headers)
            result_exp = "1"
            self.assertEqual(result_exp, result.text, msg="企业平台删除购物车订单，删除失败")
            log.info("企业平台删除购物车订单：操作成功")
            log_exp.info(result_exp)
            log_act.info(result.text)
        except TypeError:
            log.info("没有需要删除的购物车商品")

    # 购物车-提交订单
    def test_c003_order(self):
        try:
            conn = MySQL().connect_mall()
            cur = conn.cursor()
            sql = "select product_spec_uuid from shoping_info where sp_id=" + spId + " and emp_id=" + cuEmpId + " and comp_id=" + cuComId
            cur.execute(sql)
            uuid = cur.fetchone()[0]
            url = "http://cu.ejw.cn/order/v1/cu/" + cuComId + "/order"
            params = {
                "order": {"cuPartnerName": cuComName, "cuEmpId": int(cuEmpId), "cuEmpName": cuEmpName,
                          "systemType": "0",
                          "resSystem": "1", "orderDesc": "自动化测试订单功能"},
                "deliveryAddr": {"recName": "2222222000", "recPhone": "15000000000", "recPost": "333333",
                                 "recAddr": "山东 济南 槐荫区 33333333333333333333333333333333", "deliveryDesc": ""},
                "usePlatCouponInfo": [], "spOrderInfos": [
                    {"spSpecUuid": uuid, "amount": 1, "payType": "0", "invoiceType": "1",
                     "cusContractUrl": "https://bj.bcebos.com/v1/hnjing-test/c25ab9a8aadb41e7881ebcb9dceb2814.rar",
                     "otherContractUrl": "", "compQualifyInfos": [{"quaName": "成年人专用",
                                                                   "quaImages": "https://bj.bcebos.com/v1/hnjing-test/d26a9fa28b6146b3ad27c1a228a5f885.jpg"}],
                     "useSkuCouponInfo": []}]}
            result = requests.post(url, data=json.dumps(params), headers=headers)
            result_exp_pro = 200
            self.assertEqual(result_exp_pro, result.status_code, msg="请求参数异常或加入购物车失败")
            log_exp.info(result_exp_pro)
            log_act.info(result.text)
        except TypeError:
            log.info("数据库中没有需要下订单的数据")

    # 企业后台-已购产品-充值产品下单
    def test_c004_order(self):
        url = 'http://cu.ejw.cn/order/v1/cu/176/chargeorder'
        paramas = {"cuPartnerName": cuComName, "resUrl": "", "systemType": "0",
                   "resSystem": "1", "orderDesc": "", "spChargeAttrId": 156, "amount": 1, "cuEmpId": int(cuEmpId),
                   "cuEmpName": "蒋涛", "invoiceType": "1", "payType": "0", "spPartnerId": int(spId),
                   "spPartnerName": spName,
                   "spOrderId": "s1542332904546", "chargeAccout": "CZ520", "sellPrice": "100.00"}
        # 发送接口请求
        czcp = requests.post(url, data=json.dumps(paramas), headers=headers)
        # 设置预期的状态码是 200
        result_exp = 200
        # 获取实际返回的状态码
        result_act = czcp.status_code
        # 判断实际返回的状态码是否与预期设置的状态码相同
        self.assertEqual(result_exp, result_act)
        log.info("企业后台-已购产品-充值产品下单:执行结果如下")
        log_exp.info(result_exp)
        log_act.info(czcp.text)

    # 企业后台-已购产品-续期产品下单
    def test_c005_order(self):
        url = "http://cu.ejw.cn/order/v1/cu/" + cuComId + "/srvtimeorder"
        paramas = {"cuPartnerName": cuComName, "resUrl": "", "systemType": "0", "resSystem": "1",
                   "orderDesc": "", "spSrvtimeAttrId": 106, "spAttrId": 182, "attrName": "1年", "sellPrice": "200.00",
                   "amount": 1,
                   "cuEmpId": int(cuEmpId), "cuEmpName": cuEmpName, "payType": "0", "invoiceType": "1",
                   "spPartnerId": int(spId),
                   "spPartnerName": spName, "spOrderId": "s1542332904546", "srvtimeAccout": "XQ520"}
        # 发送接口请求
        xqcp = requests.post(url, data=json.dumps(paramas), headers=headers)
        # 设置预期的状态码是 200
        result_exp = 200
        # 获取实际返回的状态码
        result_act = xqcp.status_code
        # 判断实际返回的状态码是否与预期设置的状态码相同
        self.assertEqual(result_exp, result_act)
        # 输出接口返回的数据，此处返回订单编号
        log.info("企业后台-已购产品-续期产品下单:执行结果如下")
        log_exp.info(result_exp)
        log_act.info(xqcp.text)

    # 企业后台-订单管理-标准订单管理-付款
    def test_d001_pay(self):
        global log, log_exp, log_act
        log_exp = Logger(logger="企业平台_预期结果").getlog()
        log_act = Logger(logger="企业平台_实际结果").getlog()
        log = Logger(logger="企业平台").getlog()
        try:
            # 获取当前已加入购物车的spid
            conn_mail = MySQL().connect_mall()
            cur_mail = conn_mail.cursor()
            sql = "select sp_id from shoping_info where comp_id =" + cuComId + " and emp_id= " + cuEmpId + " and sp_id=" + spId
            cur_mail.execute(sql)
            result_sql = cur_mail.fetchone()[0:1]
            sp_id = result_sql[0]
            print(sp_id)

            # 查询需要付款的订单
            conn = MySQL().connect_order()
            cur = conn.cursor()
            sql = "select b.sp_order_id,b.sp_order_stage_no from sp_order_info a, pay_stage_info b where a.sp_partner_id=" + sp_id + " and a.sp_order_id=b.sp_order_id and b.pay_state=0;"
            print(sql)
            cur.execute(sql)
            ordering = cur.fetchone()[0:2]
            sp_order_id = str(ordering[0])
            sp_order_stage_no = str(ordering[1])
            url = "http://cu.ejw.cn/order/v1/cu/" + cuComId + "/pay/" + sp_order_id + "/stage/" + sp_order_stage_no
            # print(url)
            params = {"cuPartnerName": "湖南竞网智赢网络技术有限公司", "cuEmpId": int(cuEmpId), "cuEmpName": "竞网企业", "cuAccountPwd": "a123456",
                      "cuEntrustUrl": "", "cuAccountId": "1829615000103289", "cuAccountName": "湖南竞网智赢网络技术有限公司"}
            result_act = requests.post(url, data=json.dumps(params), headers=headers)
            print(result_act.text)
            result_exp = 200
            self.assertEqual(result_exp, result_act.status_code, msg='接单失败')
            log.info("企业后台-订单管理-标准订单管理-付款")
            log_exp.info(result_exp)
            log_act.info(result_act.text)
        except TypeError:
            log.info("没有找到需要付款的订单")

    # 企业后台-订单管理-标准订单管理-申请退款
    def test_d002_pay(self):
        try:
            conn = MySQL().connect_order()
            cur = conn.cursor()
            sql = "select b.pay_id,a.sp_order_id, b.pay_amount from sp_order_info a, pay_stage_info b where a.order_state=1 and a.sp_partner_id=" + spId + " and b.pay_state=1 and a.sp_order_id=b.sp_order_id;"
            cur.execute(sql)
            ordering = cur.fetchone()[0:3]
            sp_order_id = str(ordering[1])
            pay_id = str(ordering[0])
            pay_amount = ordering[2]
            url = "http://cu.ejw.cn/order/v1/partner/" + spId + "/order/" + sp_order_id + "/paystageinfo/" + pay_id
            print(url)
            params = {"nodeSuggest": "退款申请", "payState": "4", "cuEmpId": int(cuEmpId), "refundAmount": int(pay_amount),
                      "spPartnerName": spName}
            result_act = requests.put(url, data=json.dumps(params), headers=headers)
            result_exp = 200
            self.assertEqual(result_exp, result_act.status_code, msg='退款申请失败')
            log.info("企业后台-订单管理-标准订单管理-申请退款: 退款申请成功")
            log_exp.info(result_exp)
            log_act.info(result_act.text)
        except TypeError:
            log.info("没有找到需要退款的订单")

    # 企业后台-订单管理-标准订单管理-退款详情-申请仲裁
    def test_d003_pay(self):
        try:
            conn = MySQL().connect_order()
            cur = conn.cursor()
            sql = "select b.pay_id,a.sp_order_id,a.amount_Price, b.sp_order_stage_no, a.sp_product_code, a.sp_product_name, a.sp_product_spec_name from sp_order_info a, pay_stage_info b where a.order_state=1 and a.sp_partner_id=" + spId + " and b.pay_state=5 and a.sp_order_id=b.sp_order_id;"
            cur.execute(sql)
            ordering = cur.fetchone()[0:7]
            pay_id = str(ordering[0])
            sp_order_id = str(ordering[1])
            amountPrice = ordering[2]
            spOrderStageNo = ordering[3]
            productCode = ordering[4]
            productName = str(ordering[5])
            productSpecName = ordering[6]
            url = "http://cu.ejw.cn/platform/v1/order/" + sp_order_id + "/arbitrate/" + pay_id
            print(url)
            params = {"amountPrice": int(amountPrice), "spOrderStageNo": spOrderStageNo, "orderType": "1",
                      "productCode": productCode,
                      "productName": productName, "productSpecName": productSpecName, "spName": spName,
                      "spId": int(spId),
                      "cuName": cuComName, "orderCompId": int(cuComId), "orderEmpId": int(cuEmpId),
                      "cuEmpName": cuEmpName,
                      "applyDesc": "自动化-服务商不同意退款，已购产品货物没有送达"}
            result_act = requests.post(url, data=json.dumps(params), headers=headers)
            # print(result_act.text)
            result_exp = 200
            self.assertEqual(result_exp, result_act.status_code, msg='发送仲裁失败')
            log.info("企业后台-订单管理-标准订单管理-申请仲裁: " + sp_order_id + "申请仲裁成功")
            log_exp.info(result_exp)
            log_act.info(result_act)
        except TypeError:
            log.info("没有找到需要仲裁的订单")



if __name__ == '__main__':
    unittest.main()
