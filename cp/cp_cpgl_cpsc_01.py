import requests
import unittest
import interface.readConfig as readConfig
import json
import random
import pymysql
from comm.login import testlogin_001
# from interface.comm.Log import MyLog as Log
# 获取配置文件地址url
localReadConfig = readConfig.ReadConfig()
token_01 = testlogin_001().test_login_001('token')

class Cpgl_cpsxj(unittest.TestCase):
    # 验证登陆是否成功
    def test_a001_login(self):
        params = {'mobilePhone': '13822236665', 'password': '123456', 'remember': 'true', 'siteName': 'main'}
        url = localReadConfig.get_http('url')

        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0',
            'Accept - Encoding': 'gzip, deflate',
            'Accept - Language': 'zh - CN, zh;q = 0.9',
            'Referer': 'http://www1.ejw.cn/auth/?backUrl=http%3A%2F%2Fadmin.ejw.cn%2F%23%2F',
            'X-Requested-With': 'XMLHttpRequest'
        }
        token_act = requests.post(url, data=json.dumps(params), headers=headers)
        #print(token_act)
        s = json.loads(token_act.text)
        result_exp = 200
        result_act = token_act.status_code
        self.assertEqual(result_exp, result_act)
        print("用户登陆成功")
        # 获取token
        token = s["data"]["access_token"]

    # 智营销平台-产品管理-产品上下架管理-发布产品
    def test_b001_fbcp(self):
        name_02 = ''.join(random.sample(['a', 'b', 'c', 'd', 'e', '1', '5', '6', 'x'], 6))
        name_01 = '自动化测试'
        productName = name_01 + name_02
        # 请求下单功能
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'token': token_01
        }
        # print(headers)
        # 请求参数
        url = 'http://cp.ejw.cn/cp/v1/partner/277/product'
        parms = {
            "productSetupAttributes": [{
                "attrId": 108,
                "customAttrValue": "",
                "fillValue": "100M光纤"
            }, {
                "attrId": 109,
                "customAttrValue": "",
                "fillValue": "100M"
            }],
            "productCustomAttributes": [],
            "productSpecs": [{
                "sellPrice": "10.00",
                "stock": 1000,
                "productSpecAttributes": [{
                    "attrId": 109,
                    "attrValue": "100M",
                    "code": None,
                    "isCustomAttr": "0"
                }]
            }],
            "typeId": 55,
            "partnerId": 277,
            "partnerType": "0100",
            "productName": productName,
            "productType": "single",
            "productInfo": "<p>这是一个自动化测试过程</p>",
            "images": "http://hnjing-test.bj.bcebos.com/v1/hnjing-test/386cfac505874611b12f1e57101d50e0.jpg,http://hnjing-test.bj.bcebos.com/v1/hnjing-test/3034582b9ea24c6e966138fa2eea406c.jpg",
            "qualification": "71",
            "createUserid": 203,
            "specMinPrice": 10,
            "specMaxPrice": 10,
            "tempStatus": "1",
            "flowId": 70
        }
        values = json.dumps(parms)
        # 发送服务商接口请求
        # fws_test = requests.post(url, data=values, headers=headers).text
        # print(fws_test)
        # 返回状态码信息
        respon_act = requests.post(url, data=values, headers=headers).status_code
        # print(respon_act)
        # s = json.loads(fws_test)          赋值所有的结果值
        # att = s["partner"]["partnerName"] 此消息获取json下的用户字段值
        respon_exp = 200
        self.assertEqual(respon_exp, respon_act)
        print("发布产品成功")

    # 智营销平台-产品管理-产品上下架管理-产品名称查询
    def test_b002_cpmc_search(self):
        # 请求下单功能
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'token': token_01
        }
        # 请求查询参数
        url = 'http://cp.ejw.cn/cp/v1/partner/277/products?pageNo=1&pageSize=10&sort=%7B%22createTime%22%3A%22desc%22%7D&productName=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95'
        result_all = requests.get(url, headers=headers).text
        result_json = json.loads(result_all)
        totalCount_exp = result_json["page"]["totalCount"]
        # print(totalCount_exp)

        # 连接bidetect数据库信息
        conn = pymysql.connect(host='192.168.150.33', port=3306, user='root', passwd='hnjing&@test', db='ps',
                               charset='utf8')
        # 创建一个游标对象
        cur = conn.cursor()
        product_name = "%自动化测试%"
        cur.execute('select count(*) from product t where t.product_name like "' + product_name + '"')
        totalCount_act = cur.fetchone()[0]
        # print(totalCount_act)
        self.assertEqual(totalCount_exp, totalCount_act)
        print("查询产品名称日期")

    # 智营销平台-产品管理-产品上下架管理-产品选择日期查询
    def test_b003_cpmc_search(self):
        # 请求下单功能
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'token': token_01
        }
        # print(headers)
        # 请求查询参数
        url_get = 'http://cp.ejw.cn/cp/v1/partner/277/products?pageNo=1&pageSize=10&sort=%7B%22createTime%22%3A%22desc%22%7D&createTimeStart=2018-05-01T16%3A00%3A00.000Z&createTimeEnd=2018-05-02T15%3A59%3A59.000Z'
        result_all = requests.get(url_get, headers=headers)
        result_json = json.loads(result_all.text)
        totalCount_exp = result_json["data"][0]["productName"]
        print(totalCount_exp)

        # 连接bidetect数据库信息
        conn = pymysql.connect(host='192.168.150.33', port=3306, user='root', passwd='hnjing&@test', db='ps',
                               charset='utf8')
        # 创建一个游标对象
        cur = conn.cursor()
        # order = "order by create_time desc"
        date_01 = '2018-05-02 00:00:00'
        sql_03 = 'and t.create_time < "2018-05-02 23:59:59"'
        sql_01 = " order by create_time desc"
        sql_02 = 'select t.product_name from product t where t.partner_id=277 and t.create_time > "' + date_01 + '" '
        # 拼接sql语句
        sql = sql_02+sql_03+sql_01
        # 执行sql命令
        cur.execute(sql)
        # 取当前游标productName数据
        totalCount_act = cur.fetchone()[0]
        print(totalCount_act)
        self.assertEqual(totalCount_exp, totalCount_act)
        print("查询2018-05-02的日期正确")



if __name__ == '__main__':
    unittest.main()
