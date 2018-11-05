# 运营平台-合作伙伴管理
import requests
import random
import json
import unittest
from comm.login import testlogin_001
from comm.Log import Logger
from comm.public_data import MySQL

log = Logger(logger="服务商平台").getlog()

# 请求头信息
token = testlogin_001().test_splogin('token')
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'token': token
}

# 随机生成社会信用代码
uscCode_01 = ''.join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 10))
uscCode_02 = '43062419'
uscCode = uscCode_01 + uscCode_02
log_exp = Logger(logger="服务商平台_预期结果").getlog()
log_act = Logger(logger="服务商平台_实际结果").getlog()
log = Logger(logger="服务商平台").getlog()


class admin_yygl(unittest.TestCase):
    # 产品管理-产品上下架管理-已存在的产品名称查询
    def test_c005_product_serach(self):
        conn = MySQL().connect_ps1('conn')
        cur = conn.cursor()
        cur.execute("select sp_product_name from sp_product t where t.sp_partner_id=502 order by create_date desc")
        productName = str(cur.fetchone()[0])
        log_exp.info(productName)
        url_01 = "http://sp.ejw.cn/ps/v1/spproducts?buyType=&_sort=modifyDate%2Cdesc&pageSize=20&pageNum=1&spPartnerId=502&spProductName="
        url = url_01 + productName
        product_search = requests.get(url, headers=headers)
        # print(product_search.text)
        result_act = product_search.text
        log_act.info(result_act)
        self.assertIn(productName, result_act, msg="查询的产品名字不存在")
        log.info("已有产品名称查询成功")

    # 产品管理-产品上下架管理-不存在的产品名称查询
    def test_c006_product_serach(self):
        productName = 'test11110001'
        log_exp.info(productName)
        url_01 = "http://sp.ejw.cn/ps/v1/spproducts?buyType=&_sort=modifyDate%2Cdesc&pageSize=20&pageNum=1&spPartnerId=502&spProductName="
        url = url_01 + productName
        result_act = requests.get(url, headers=headers).text
        log_act.info(result_act)
        self.assertNotIn(productName, result_act, msg="查询异常或该产品已存在")
        log.info("未查询到该产品信息")

    # 产品管理-供应商授权管理-全部-提交合同
    def test_c007_product_verify(self):
        # 连接ps数据库
        conn1 = MySQL().connect_platform1('conn')
        cur1 = conn1.cursor()
        cur1.execute(
            "select auth_id, record_id from product_auth t where t.sp_id='502' and t.`status`=0")
        try:
            result_data = cur1.fetchone()[0:2]
            auth_id = result_data[0]
            record_id = result_data[1]
            print(auth_id, record_id)
            url_01 = "http://sp.ejw.cn/platform/v1/productauth/"
            url = url_01 + str(record_id) + "?curEmpId=2121"
            print(url)
            params = {"contractId": auth_id, "contractName": "script.rar",
                      "contractBeginDate": "2018-07-13T00:00:00+08:00",
                      "contractValidDate": "2018-07-31T23:59:59+08:00",
                      "contractSpFile": "https://bj.bcebos.com/v1/hnjing-test/890d51e8ec26441da124f4f009cff36f.rar?authorization=bce-auth-v1%2Fed6cb82c3c054636aec25bdbc65d7c10%2F2018-07-13T01%3A51%3A01Z%2F-1%2F%2Ffcdc2fb8500561d8a195514e0d324075dd7c820a1fe7706defcd281460680773"}

            result_act = requests.put(url, data=json.dumps(params), headers=headers)
            log_act.info(result_act)
            result_exp = 1
            self.assertEqual(result_exp, int(result_act.text), msg="数据异常，产品授权不通过")
            log.info("提交合同成功-待供应商审核")
        except TypeError:
            log.info("没有需要授权的产品信息")


if __name__ == '__main__':
    unittest.main()
