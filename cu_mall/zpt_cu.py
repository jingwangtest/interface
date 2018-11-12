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
token = testlogin_001().test_culogin('token')

# 指定头文件
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'token': token
}


class Cu(unittest.TestCase):
    # 外商城商品加入购物车
    def test_ashop_001(self):
        url = "http://www.ejw.cn/shopingcart"
        params = {"productUuid": "01541123570722", "productSpecUuid": "7664A4244A5C4CDE90121211E7BB774E", "spId": 502,
                  "compId": 176, "empId": 2143}
        result = requests.post(url, data=json.dumps(params), headers=headers).text
        result_act = json.loads(result)
        result_act_pro = result_act["productUuid"]
        result_exp_pro = "01541123570722"
        print(result_exp_pro, result_act_pro)
        self.assertEqual(result_exp_pro, result_act_pro, msg="请求参数异常或加入购物车失败")

    # 企业平台删除购物车
    def test_ashop_002(self):
        try:
            conn = MySQL().connect_mall1('conn')
            cur = conn.cursor()
            sql_data = '502'
            emp_id = '2143'
            cur.execute(
                'select rec_id from shoping_info t where t.sp_id = "' + sql_data + '" and t.emp_id= "' + emp_id + '"')
            rec_id = str(cur.fetchone()[0])
            print(type(rec_id))
            url = "http://cu.ejw.cn/mall/v1/shopingcart/" + rec_id
            print(url)
            result = requests.delete(url, headers=headers).text
            print(result)
            result_exp = "1"
            self.assertEqual(result_exp, result, msg="删除失败")
        except TypeError:
            print("没有需要删除的购物车商品")

    # 企业平台提交订单
    def test_aorder_003(self):
        url = "http://cu.ejw.cn/order/v1/cu/176/order"
        params = {
            "order": {"cuPartnerName": "客户库合并合作伙伴验证-盛秀玲20171103", "cuEmpId": 2143, "cuEmpName": "蒋涛", "systemType": "0",
                      "resSystem": "1", "orderDesc": "自动化测试订单功能"},
            "deliveryAddr": {"recName": "2222222000", "recPhone": "15000000000", "recPost": "333333",
                             "recAddr": "山东 济南 槐荫区 33333333333333333333333333333333", "deliveryDesc": ""},
            "usePlatCouponInfo": [], "spOrderInfos": [
                {"spSpecUuid": "7664A4244A5C4CDE90121211E7BB774E", "amount": 1, "payType": "0", "invoiceType": "1",
                 "cusContractUrl": "https://bj.bcebos.com/v1/hnjing-test/c25ab9a8aadb41e7881ebcb9dceb2814.rar",
                 "otherContractUrl": "", "compQualifyInfos": [{"quaName": "成年人专用",
                                                               "quaImages": "https://bj.bcebos.com/v1/hnjing-test/d26a9fa28b6146b3ad27c1a228a5f885.jpg"}],
                 "useSkuCouponInfo": []}]}
        result = requests.post(url, data=json.dumps(params), headers=headers).status_code
        result_exp_pro = 200
        print(result_exp_pro, result)
        self.assertEqual(result_exp_pro, result, msg="请求参数异常或加入购物车失败")



if __name__ == '__main__':
    unittest.main()
