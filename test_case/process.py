# 主流程
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
cuComId = localReadConfig.read_cu_com_id()
cuComName = localReadConfig.read_cu_com_name()
cuEmpId = localReadConfig.read_cu_emp_id()
cuEmpName = localReadConfig.read_cu_emp_name()
adminEmpId = localReadConfig.read_admin_emp_id()
createUser = int(localReadConfig.read_sp_user())
spId = localReadConfig.read_sp_com_id()
spEmpId = localReadConfig.read_sp_emp_id()
spComId = localReadConfig.read_sp_com_id()
spComName = localReadConfig.read_sp_com_name()
cpComId = localReadConfig.read_cp_com_id()
cpComName = localReadConfig.read_cp_com_name()
cpEmpId = localReadConfig.read_cp_emp_id()
cpEmpName = localReadConfig.read_cp_emp_name()


class Ces(unittest.TestCase):
    def test_a001(self):
        token = Zpt().cu_login()
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'token': token
        }
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
        result = requests.post(url, data=json.dumps(params), headers=headers)
        result_exp = 200
        # print(result_exp_pro, result_act_pro)
        self.assertEqual(result_exp, result.status_code, msg="请求参数异常或加入购物车失败")
        print("外商城商品加入购物车成功", result.text)

    # 购物车-提交订单
    def test_a002(self):
        token = Zpt().cu_login()
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'token': token
        }
        try:
            conn = MySQL().connect_mall()
            cur = conn.cursor()
            sql = "select product_spec_uuid from shoping_info where sp_id=" + spId + " and emp_id=" + cuEmpId + " and comp_id=" + cuComId
            cur.execute(sql)
            result_sql = cur.fetchone()[0:1]
            uuid = result_sql[0]
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
            print(result_exp_pro, result.text)
        except Ellipsis:
            print("数据库中没有需要下订单的数据")

    # 工单管理-标准订单-接单
    def test_a003(self):
        token = Zpt().sp_login()
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'token': token
        }

        try:
            conn = MySQL().connect_order()
            cur = conn.cursor()
            sql = "select sp_order_id,order_id,pay_price from sp_order_info where sp_partner_id=" + spId + " and order_state=0"
            print(sql)
            cur.execute(sql)
            ordering = cur.fetchone()[0:3]
            sp_order_id = ordering[0]
            order_id = ordering[1]
            pay_price = ordering[2]
            url = "http://sp.ejw.cn/order/v1/sp/" + spId + "/order/" + sp_order_id + "/paystageinfo"
            params = {"spEmpId": int(spEmpId), "spEmpName": "蒋涛", "orderId": order_id,
                      "spCusContractUrl": "https://bj.bcebos.com/v1/hnjing-test/d45fdb0150674e5baa969192921ad626.rar",
                      "stages": [{"spOrderStageNo": 1, "payDesc": "aaaa", "payAmount": int(pay_price)}]}
            print(params)
            result_act = requests.post(url, data=json.dumps(params), headers=headers).status_code
            result_exp = 200
            self.assertEqual(result_exp, result_act, msg='接单失败')
            print("接单成功")
        except TypeError:
            print("没有找到需要接单的订单")

    # 企业后台-订单管理-标准订单管理-付款
    def test_a004(self):
        token = Zpt().cu_login()
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'token': token
        }
        try:
            # 获取当前已加入购物车的spid
            # conn_mail = MySQL().connect_mall()
            # cur_mail = conn_mail.cursor()
            # sql = "select sp_id from shoping_info where comp_id =" + cuComId + " and emp_id= " + cuEmpId + " and sp_id=" + spId
            # cur_mail.execute(sql)
            # result_sql = cur_mail.fetchone()[0:1]
            # sp_id = result_sql[0]
            # print(sp_id)

            # 查询需要付款的订单
            conn = MySQL().connect_order()
            cur = conn.cursor()
            sql = "select b.sp_order_id,b.sp_order_stage_no from sp_order_info a, pay_stage_info b where a.sp_partner_id=" + spId + " and a.sp_order_id=b.sp_order_id and b.pay_state=0;"
            print(sql)
            cur.execute(sql)
            ordering = cur.fetchone()[0:2]
            sp_order_id = str(ordering[0])
            sp_order_stage_no = str(ordering[1])
            url = "http://cu.ejw.cn/order/v1/cu/" + cuComId + "/pay/" + sp_order_id + "/stage/" + sp_order_stage_no
            print(url)
            params = {"cuPartnerName": cuComName, "cuEmpId": int(cuEmpId), "cuEmpName": cuEmpName,
                      "cuAccountPwd": "a123456",
                      "cuEntrustUrl": "", "cuAccountId": "1835115000108339", "cuAccountName": cuComName}
            print(params)
            result_act = requests.post(url, data=json.dumps(params), headers=headers)
            result_exp = 200
            self.assertEqual(result_exp, result_act.status_code, msg='接单失败')
            print("企业后台-订单管理-标准订单管理-付款", result_exp, result_act.text)
        except TypeError:
            print("没有找到需要付款的订单")


if __name__ == '__main__':
    unittest.main()
