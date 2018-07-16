# 服务商平台
import requests
import random
import json
import unittest
from comm.login import testlogin_001
from comm.public_data import MySQL
from comm.Log import Logger

token = testlogin_001().test_splogin('token')

# 设置营销锦囊名称
jnName_01 = ''.join(random.sample(['8', '6', '3', '2', '5', '6'], 4))
jnName_02 = '锦囊营销'
jnName = jnName_02 + jnName_01

# 指定头文件
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'token': token
}


class test_sp_dpgl_01(unittest.TestCase):
    # 店铺管理-案例管理-新增角色
    def test_a001_role_add(self):
        # 设置案例名称
        caseName_01 = ''.join(random.sample(['8', '6', '3', '2', '5', '6'], 4))
        caseName_02 = '案例生成'
        caseName = caseName_02 + caseName_01
        url = "http://sp.ejw.cn/mall/v1/classcaseinfo"
        params = {"createUser": 24, "industryId": 18, "caseName": caseName,
                  "caseImage": "http://hnjing-test.bj.bcebos.com/v1/hnjing-test/416e56edd49d453395f99bcac6757777.jpg",
                  "caseDesc": "111", "caseDetail": "<p>1111</p>", "salesStatu": "111", "caseState": "2", "spId": 190}
        result_act = requests.post(url, data=json.dumps(params), headers=headers).text
        self.assertIn(caseName, result_act, msg="新增案例失败")
        global log, log_exp, log_act
        log_exp = Logger(logger="服务商平台_预期结果").getlog()
        log_act = Logger(logger="服务商平台_实际结果").getlog()
        log = Logger(logger="服务商平台").getlog()
        log_exp.info(caseName)
        log_act.info(result_act)
        log.info(caseName + "新增成功")

    # 店铺管理-案例管理-删除
    def test_a002_role_del(self):
        # 设置案例名称
        conn = MySQL().connect_mall1('conn')
        cur = conn.cursor()
        sql_data = '190'
        # 查询出当前要删除案例的id信息
        cur.execute('select case_id from class_case_info t where t.sp_id = "' + sql_data + '"')
        case_id = str(cur.fetchall()[0][0])
        print('select case_id from class_case_info t where t.sp_id = "' + sql_data + '"')
        url_01 = 'http://sp.ejw.cn/mall/v1/classcaseinfo/'
        url = url_01 + case_id
        result_act = requests.delete(url, headers=headers).text
        result_exp = 1
        self.assertEqual(result_exp, int(result_act), msg="删除失败")
        log.info("案例删除成功")

    # 店铺管理-案例管理-已存在的用户名查询
    def test_a003_role_del(self):
        conn = MySQL().connect_mall1('conn')
        cur = conn.cursor()
        sql_data = '190'
        # 查询出当前要删除案例的id信息
        cur.execute('select case_name from class_case_info t where t.sp_id = "' + sql_data + '"')
        case_name = str(cur.fetchall()[0][0])
        url_01 = 'http://sp.ejw.cn/mall/v1/classcaseinfos?spId=190&caseState=&pageSize=10&pageNo=1&caseName='
        url = url_01 + case_name
        result_act = requests.get(url, headers=headers).text
        # print(case_name, result_act)
        self.assertIn(case_name, result_act, msg="案例查询失败")
        log.info("已存在的案例名称查询成功")

    # 店铺管理-案例管理-不存在的用户名查询
    def test_a004_role_search(self):
        casename = "天天向上1111111"
        url_01 = 'http://sp.ejw.cn/mall/v1/classcaseinfos?spId=190&caseState=&pageSize=10&pageNo=1&caseName='
        url = url_01 + casename
        result_act = requests.get(url, headers=headers).text
        print(casename, result_act)
        self.assertNotIn(casename, result_act, msg="不存在的用户查询失败")
        log.info("案例管理-不存在的用户名查询无异常")

    # 店铺管理-营销锦囊-增加
    def test_b001_jn_add(self):
        # 设置营销锦囊名称
        jnName_01 = ''.join(random.sample(['8', '6', '3', '2', '5', '6'], 4))
        jnName_02 = '锦囊营销'
        jnName = jnName_02 + jnName_01
        url = "http://sp.ejw.cn/mall/v1/marketingpolicy"
        params = {"spId": 190,
                  "policyImage": "http://hnjing-test.bj.bcebos.com/v1/hnjing-test/f8828654e9004d59a785a9238d6ccab0.jpg",
                  "policyState": "2", "createUser": 24, "policyName": jnName, "industryId": 18,
                  "policyDesc": "智能营销无限给力", "policyContent": "<p>营销大销售了，我们的发展无限潜力<br/></p>"}
        result_act = requests.post(url, data=json.dumps(params), headers=headers).text
        print(result_act)
        self.assertIn(jnName, result_act, msg="锦囊新增失败")
        log.info(jnName + "新增成功")

    # 店铺管理-营销锦囊-删除
    def test_b002_jn_del(self):
        conn = MySQL().connect_mall1('conn')
        cur = conn.cursor()
        sql_data = '190'
        # 查询出当前要删除案例的id信息
        cur.execute('select policy_id from marketing_policy t where t.sp_id = "' + sql_data + '"')
        total = str(cur.fetchall()[0][0])
        url_01 = 'http://sp.ejw.cn/mall/v1/marketingpolicy/'
        url = url_01 + total
        case_delete_act = requests.delete(url, headers=headers).text
        case_delete_exp = 1
        self.assertEqual(case_delete_exp, int(case_delete_act), msg="案例删除失败")
        log.info("案例删除成功")

    # 店铺管理-营销锦囊-已存在的用户名查询
    def test_b003_jn_search(self):
        conn = MySQL().connect_mall1('conn')
        cur = conn.cursor()
        sql_data = '190'
        # 查询出当前要删除案例的id信息
        cur.execute('select policy_Name from marketing_policy t where t.sp_id = "' + sql_data + '"')
        result_exp = str(cur.fetchall()[0][0])
        url_01 = 'http://sp.ejw.cn/mall/v1/marketingpolicys?spId=190&policyState=&pageNo=1&pageSize=10&policyName='
        url = url_01 + result_exp
        result_act = requests.get(url, headers=headers).text
        log_exp.info(result_exp)
        log_act.info(result_act)
        self.assertIn(result_exp, result_act, msg="案例名称查询失败")
        log.info("案例名称查询成功")

    # 店铺管理-营销锦囊-不存在的用户名查询
    def test_b004_jn_search(self):
        result_exp = "test000000011111"
        url_01 = 'http://sp.ejw.cn/mall/v1/marketingpolicys?spId=190&policyState=&pageNo=1&pageSize=10&policyName='
        url = url_01 + result_exp
        result_act = requests.get(url, headers=headers).text
        self.assertNotIn(result_exp, result_act, msg="不存在的用户查询失败")
        log.info(result_exp)
        log.info(result_act)
        log.info("不存在的用户查询成功")

    # 店铺管理-产品管理-我发布的的产品-发布产品-产品名称查询
    def test_c001_product_search(self):
        conn = MySQL().connect_ps1('conn')
        cur = conn.cursor()
        cur.execute("select t.product_name from product t where t.partner_type=0100 and partner_id=190")
        # product_name = quote(cur.fetchone()[0], 'utf-8')
        product_name = cur.fetchone()[0]
        url_01 = "http://sp.ejw.cn/sp/v1/sp/190/products?productType=&sort=%7B%22createTime%22%3A%22desc%22%7D&pageSize=10&pageNo=1&productName="
        url = url_01 + product_name
        print(url)
        result_act = requests.get(url, headers=headers).text
        self.assertIn(product_name, result_act, msg="未查询到该产品信息")
        log_exp.info(product_name)
        log_act.info(result_act)
        log.info("查询该产品信息成功")

    # 店铺管理-产品管理-我发布的产品-新增产品
    def test_c002_product_add(self):
        prodctName_01 = ''.join(random.sample(['8', '6', '3', '2', '5', '6'], 4))
        prodctName_02 = '服务商产品发布'
        prodctName = prodctName_02 + prodctName_01
        url = "http://sp.ejw.cn/ps/v1/productgroup"
        params = {"typeId": 55, "partnerId": 190, "partnerType": "0100", "productName": prodctName,
                  "productType": "single",
                  "productInfo": "<p>专用wifi路由器</p>",
                  "images": "http://hnjing-test.bj.bcebos.com/v1/hnjing-test/476abb2ebc524f54ba4b17d23a2a6764.jpg",
                  "createUserid": 24, "qualification": "110", "specMinPrice": 1, "specMaxPrice": 1, "tempStatus": "0",
                  "productSetupAttributes": [{"attrId": 108, "fillValue": "100M光纤", "customAttrValue": ""}],
                  "productCustomAttributes": [], "productSpecs": [
                {"specUuidList": ["333dd082e72841438d9979236e472697"], "productSpecName": "1", "sellPrice": "1.00",
                 "stock": 100}]}

        result_act = requests.post(url, data=json.dumps(params), headers=headers)
        self.assertIn(prodctName, result_act.text, msg="服务商发布产品失败")
        log_exp.info(prodctName)
        log_act.info(result_act)
        log.info("服务商发布产品成功")

    # 店铺管理-产品管理-产品上下架管理-已存在的产品名称查询
    def test_c005_product_serach(self):
        conn = MySQL().connect_ps1('conn')
        cur = conn.cursor()
        cur.execute(
            "select product_name from product t where t.partner_id=190 and t.partner_type=0100 order by create_time desc")
        productName = str(cur.fetchone()[0])
        log_exp.info(productName)
        url_01 = "http://sp.ejw.cn/sp/v1/sp/190/products?productType=&pageSize=10&pageNo=1&productName="
        url = url_01 + productName
        product_search = requests.get(url, headers=headers)
        # print(product_search.text)
        result_act = json.loads(product_search.text)["products"][0]["productName"]
        log_act.info(result_act)
        self.assertEqual(productName, result_act, msg="查询的产品名字不存在")
        log.info("已有产品名称查询成功")

    # 店铺管理-产品管理-产品上下架管理-不存在的产品名称查询
    def test_c006_product_serach(self):
        productName = 'test11110001'
        log_exp.info(productName)
        url_01 = "http://sp.ejw.cn/sp/v1/sp/190/products?productType=&pageSize=10&pageNo=1&productName="
        url = url_01 + productName
        result_act = requests.get(url, headers=headers).text
        log_act.info(result_act)
        self.assertNotIn(productName, result_act, msg="查询异常或该产品已存在")
        log.info("未查询到该产品信息")

    # 店铺管理-产品管理-供应商授权管理-全部-提交合同
    def test_c007_product_verify(self):
        # 连接ps数据库
        # 连接ps数据库
        conn1 = MySQL().connect_platform1('conn')
        cur1 = conn1.cursor()
        cur1.execute(
            "select auth_id, record_id from product_auth t where t.sp_id='190' and t.`status`=0;")
        auth_id = cur1.fetchone()[0]
        record_id = cur1.fetchone()[1]
        log.info("授权审核的uuid：" + auth_id)
        url_01 = "http://sp.ejw.cn/platform/v1/productauth/"
        url = url_01+str(record_id)+"?curEmpId=1721"
        print(url)
        params = {"contractId": auth_id, "contractName": "script.rar",
                  "contractBeginDate": "2018-07-13T00:00:00+08:00", "contractValidDate": "2018-07-31T23:59:59+08:00",
                  "contractSpFile": "https://bj.bcebos.com/v1/hnjing-test/890d51e8ec26441da124f4f009cff36f.rar?authorization=bce-auth-v1%2Fed6cb82c3c054636aec25bdbc65d7c10%2F2018-07-13T01%3A51%3A01Z%2F-1%2F%2Ffcdc2fb8500561d8a195514e0d324075dd7c820a1fe7706defcd281460680773"}
        result_act = requests.put(url, data=json.dumps(params), headers=headers)
        result_exp = 1
        log_act.info(result_act)
        self.assertEqual(result_exp, int(result_act.text), msg="数据异常，产品授权不通过")
        log.info("产品授权审核通过")

    # 店铺管理-产品管理-供应商授权管理-查询（不存在的）
    def test_c008_product_verify(self):
        productname = "aaaaaxxxxx"
        log_exp.info(productname)
        url_01 = "http://sp.ejw.cn/sp/v1/cp/products?sort=%7B%22createTime%22%3A%22desc%22%7D&pageNo=1&pageSize=10&typeId=&productName="
        url = url_01+productname
        result_act = requests.get(url, headers=headers).text
        log_act.info(result_act)
        self.assertNotIn(productname, result_act, msg="查询数据异常")
        log.info("不存在的数据查询正常")

    # 产品管理-供应商授权管理-查找（全部）
    def test_c009_product_verify(self):
        url = "http://sp.ejw.cn/platform/v1/productauths?cpId=&spId=190&authId=&authType=&status=&pageSize=10&pageNo=1&sort=%7B%22gmtCreate%22%3A%22desc%22%7D"
        result_act = requests.get(url, headers=headers).text
        result_Count = result_act.split("totalCount", 2)[1].split(",")[0].split(":")[1]
        self.assertIsNotNone(result_Count, msg="数据为空或查询异常")
        log_act.info("查询条数为:" + result_Count)

    # 店铺管理-产品管理-供应商授权管理-详情
    def test_c010_product_verify(self):
        url = "http://sp.ejw.cn/os/v1/partners?partnerId=190"
        result_act = requests.get(url, headers=headers)
        result_exp = 200
        self.assertEqual(result_exp, result_act.status_code, msg="查看详情存在异常情况")
        log_act.info(result_act.text)


if __name__ == '__main__':
    unittest.main()
