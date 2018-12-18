# 服务商平台
import requests
import random
import json
import time
import unittest
from comm.login import Zpt
from comm.public_data import MySQL
from comm.Log import Logger
import readConfig

token = Zpt().sp_login()
localReadConfig = readConfig.ReadConfig()

# 指定用户createUser、sp_id、spEmpId
createUser = int(localReadConfig.read_sp_user())
spId = localReadConfig.read_sp_com_id()
spEmpId = localReadConfig.read_sp_emp_id()
cuComId = localReadConfig.read_cu_com_id()
cuComName = localReadConfig.read_cu_com_name()
cuEmpId = localReadConfig.read_cu_emp_id()
cuEmpName = localReadConfig.read_cu_emp_name()

# 设置营销锦囊名称
jnName_01 = ''.join(random.sample(['8', '6', '3', '2', '5', '6'], 4))
jnName_02 = '锦囊营销'
jnName = jnName_02 + jnName_01

# 指定头文件
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'token': token
}


class sp_dpgl_01(unittest.TestCase):
    # 店铺管理-案例管理-新增角色
    def test_a001_role_add(self):
        global log, log_exp, log_act
        log_exp = Logger(logger="服务商平台_预期结果").getlog()
        log_act = Logger(logger="服务商平台_实际结果").getlog()
        log = Logger(logger="服务商平台").getlog()
        # 设置案例名称
        caseName_01 = ''.join(random.sample(['8', '6', '3', '2', '5', '6'], 4))
        caseName_02 = '案例生成'
        caseName = caseName_02 + caseName_01
        url = "http://sp.ejw.cn/mall/v1/classcaseinfo"
        params = {"createUser": createUser, "industryId": 22, "caseName": caseName,
                  "caseImage": "http://hnjing-test.bj.bcebos.com/v1/hnjing-test/416e56edd49d453395f99bcac6757777.jpg",
                  "caseDesc": "111", "caseDetail": "<p>1111</p>", "salesStatu": "111", "caseState": "2",
                  "spId": int(spId)}
        result_act = requests.post(url, data=json.dumps(params), headers=headers).text
        self.assertIn(caseName, result_act, msg="新增案例失败")
        log_exp.info(caseName)
        log_act.info(result_act)
        log.info(caseName + "新增成功")

    # 店铺管理-案例管理-删除
    def test_a002_role_del(self):
        # 设置案例名称
        conn = MySQL().connect_mall()
        cur = conn.cursor()
        # 查询出当前要删除案例的id信息
        cur.execute('select case_id from class_case_info t where t.sp_id = "' + spId + '"')
        case_id = str(cur.fetchall()[0][0])
        url_01 = 'http://sp.ejw.cn/mall/v1/classcaseinfo/'
        url = url_01 + case_id
        result_act = requests.delete(url, headers=headers).text
        result_exp = 1
        self.assertEqual(result_exp, int(result_act), msg="删除失败")
        log.info("案例删除成功")

    # 店铺管理-案例管理-已存在的用户名查询
    def test_a003_case_search(self):
        conn = MySQL().connect_mall()
        cur = conn.cursor()
        # 查询出当前要删除案例的id信息
        sql = "select case_name from class_case_info t where t.sp_id =" + spId
        cur.execute(sql)
        case_name = str(cur.fetchall()[0][0])
        url_01 = 'http://sp.ejw.cn/mall/v1/classcaseinfos?spId=' + spId + '&caseState=&pageSize=10&pageNo=1&caseName='
        url = url_01 + case_name
        result_act = requests.get(url, headers=headers).text
        # print(case_name, result_act)
        self.assertIn(case_name, result_act, msg="案例查询失败")
        log.info(case_name + "查询成功")

    # 店铺管理-案例管理-不存在的用户名查询
    def test_a004_case_notsearch(self):
        casename = "天天向上1111111"
        url_01 = 'http://sp.ejw.cn/mall/v1/classcaseinfos?spId=' + spId + '&caseState=&pageSize=10&pageNo=1&caseName='
        url = url_01 + casename
        result_act = requests.get(url, headers=headers).text
        print(casename, result_act)
        self.assertNotIn(casename, result_act, msg="不存在的用户查询失败")
        log.info(casename + "没有此案例")

    # 店铺管理-营销锦囊-增加
    def test_b001_jn_add(self):
        # 设置营销锦囊名称
        jnName_01 = ''.join(random.sample(['8', '6', '3', '2', '5', '6'], 4))
        jnName_02 = '锦囊营销'
        jnName = jnName_02 + jnName_01
        url = "http://sp.ejw.cn/mall/v1/marketingpolicy"
        params = {"spId": int(spId),
                  "policyImage": "http://hnjing-test.bj.bcebos.com/v1/hnjing-test/f8828654e9004d59a785a9238d6ccab0.jpg",
                  "policyState": "2", "createUser": createUser, "policyName": jnName, "industryId": 18,
                  "policyDesc": "智能营销无限给力", "policyContent": "<p>营销大销售了，我们的发展无限潜力<br/></p>"}
        result_act = requests.post(url, data=json.dumps(params), headers=headers).text
        print(result_act)
        self.assertIn(jnName, result_act, msg="锦囊新增失败")
        log.info(jnName + "新增成功")

    # 店铺管理-营销锦囊-删除
    def test_b002_jn_del(self):
        try:
            conn = MySQL().connect_mall()
            cur = conn.cursor()
            # 查询出当前要删除案例的id信息
            cur.execute('select policy_id from marketing_policy t where t.sp_id = "' + spId + '"')
            jinnang = str(cur.fetchall()[0][0])
            url_01 = 'http://sp.ejw.cn/mall/v1/marketingpolicy/'
            url = url_01 + jinnang
            case_delete_act = requests.delete(url, headers=headers).text
            case_delete_exp = 1
            self.assertEqual(case_delete_exp, int(case_delete_act), msg="案例删除失败")
            log.info(jinnang + "删除成功")
        except LookupError:
            print("没有需要删除的锦囊数据")

    # 店铺管理-营销锦囊-已存在的用户名查询
    def test_b003_jn_search(self):
        try:
            conn = MySQL().connect_mall()
            cur = conn.cursor()
            # 查询出当前要删除案例的id信息
            cur.execute('select policy_Name from marketing_policy t where t.sp_id  =  "' + spId + '"')
            result_exp = str(cur.fetchall()[0][0])
            url_01 = "http://sp.ejw.cn/mall/v1/marketingpolicys?spId=" + spId + "&policyState=&pageNo=1&pageSize=10&policyName="
            url = url_01 + result_exp
            result_act = requests.get(url, headers=headers).text
            self.assertIn(result_exp, result_act, msg="案例名称查询失败")
            log.info("查询营销锦囊成功，返回营销锦囊记录，营销锦囊名称为：" + result_exp)
            log_exp.info(result_exp)
            log_act.info(result_act)
        except TypeError:
            log.info("查询列表数据为空")

    # 店铺管理-营销锦囊-不存在的用户名查询
    def test_b004_jn_search(self):
        result_exp = "test000000011111"
        url_01 = "http://sp.ejw.cn/mall/v1/marketingpolicys?spId=" + spId + "&policyState=&pageNo=1&pageSize=10&policyName="
        url = url_01 + result_exp
        result_act = requests.get(url, headers=headers).text
        self.assertNotIn(result_exp, result_act, msg="不存在的用户查询失败")
        log.info(result_exp)
        log.info(result_act)
        log.info("不存在的用户查询成功")

    # 方案管理-方案管理-发布产品
    def test_c000_product_add(self):
        # global log, log_exp, log_act
        # log_exp = Logger(logger="供应商平台_预期结果").getlog()
        # log_act = Logger(logger="供应商平台_实际结果").getlog()
        # log = Logger(logger="供应商平台").getlog()
        prodctName_01 = ''.join(random.sample(['8', '6', '3', '2', '5', '6'], 4))
        prodctName_02 = '服务商标准产品发布'
        prodctName = prodctName_02 + prodctName_01
        url = "http://sp.ejw.cn/ps/v1/sp/" + spId + "/product"
        params = {"typeId": 122, "spProductName": prodctName, "qualification": "135", "spCpProducts": [
            {"cpProductName": "供_标准产品", "cpProductCode": "11540886894520", "spCommonAttrInfos": [
                {"attrType": "1", "attrValue": "", "cpCommonAttrId": 1281, "cpProductCode": "11540886894520",
                 "customAttrValue": "红,黄", "fillValue": "红,黄", "isTemp": "0", "required": "1", "spIsMust": "1",
                 "spIsUpdate": "1", "spFillValue": "红,黄", "spCommonAttrName": "价格"}]}], "spProductSpecs": [
            {"specIsValid": 1, "specSort": 0, "specUuidList": ["216b8d68f94e4e0492aa799479e0b0c1"],
             "spProductSpecName": "红色款式", "sellPrice": "1.00", "spProductSpecAttrs": [
                {"attrName": "价格", "attrValue": "红", "cpSpecAttrId": 10873, "cpCommonAttrId": 1281}]},
            {"specIsValid": 1, "specSort": 1, "specUuidList": ["81afd4c9d2c24b44a4032c6c2c5778ff"],
             "spProductSpecName": "黄色款式", "sellPrice": "1.00", "spProductSpecAttrs": [
                {"attrName": "价格", "attrValue": "黄", "cpSpecAttrId": 10874, "cpCommonAttrId": 1281}]}],
                  "spChargeAttrInfos": [], "spSrvtimeAttrInfos": [], "specMinPrice": 1, "specMaxPrice": 1,
                  "productInfo": "<p>服务商产品发布000111<br/></p>",
                  "images": "https://bj.bcebos.com/v1/hnjing-test/908ceeed0f174f0eae5c846a202ffb6a.jpg",
                  "tempStatus": "1", "spPartnerName": "竞网自动化勿删"}

        result_act = requests.post(url, data=json.dumps(params), headers=headers)
        result_exp = 200
        self.assertEqual(result_exp, result_act.status_code, msg="服务商发布产品失败")
        log_exp.info(result_exp)
        log_act.info(result_act.text)
        log.info("服务商发布产品成功")

    # 方案管理-方案上架审核提交操作
    def test_c001_search(self):
        try:
            # 连接到数据库ps1（分支产品库）
            conn = MySQL().connect_ps()
            # 定义一个游标赋值给变量cur，cur才有权限去执行数据库
            cur = conn.cursor()
            # 数据库中查询服务商id为502，审核状态为-1的产品
            cur.execute(
                'select sp_product_code,sp_product_name from sp_product  where sale_flag = 0 and sp_partner_id = 502 and examine_state = -1')
            # 定义查询数据库表中2个字段sp_product_code，sp_product_name
            cur_data = cur.fetchone()[0:2]
            # 第一个字段赋给变量sp_product_code
            spProductCode = str(cur_data[0])
            # 第二个字段赋给变量sp_product_name
            partnerName = cur_data[1]
            # 打印查询出来的sp_product_code，sp_product_name这2个字段内容
            print(spProductCode, partnerName)
            # url地址
            url = 'http://sp.ejw.cn/sp/v1/verify-saleflag'
            # 参数信息
            params = {"spPartnerId": 502, "spProductCode": spProductCode, "productType": "group",
                      "verifyType": 1, "createUser": 164, "productName": partnerName,
                      "partnerName": "竞网自动化勿删"}
            # 发送上架审核接口请求
            result_act = requests.post(url, data=json.dumps(params), headers=headers)
            # 设置预期返回码200
            result_exp = 200
            # 实际返回码
            result_act_act = result_act.status_code
            # 判断实际返回码是否与预期的一致
            self.assertEqual(result_exp, result_act_act)
            log_exp.info(result_exp)
            log_act.info(result_act_act)
            log.info(partnerName + "上架提交成功")
        except LookupError:
            log.info("没有需要上架的方案数据")

    # 方案管理-取消上架审核（注：需先执行test_b003_search上架操作）
    def test_c002_search(self):
        try:
            # 连接到数据库ps1（分支产品库）
            conn = MySQL().connect_ps()
            # 定义一个游标赋值给变量cur，cur才有权限去执行数据库
            cur = conn.cursor()
            # 数据库中查询服务商id为502，审核状态为0的产品
            cur.execute(
                'select sp_product_code  from sp_product  where sale_flag = 0 and sp_partner_id = 502 and examine_state = 0')
            # url地址
            spProductCode = str(cur.fetchall()[0][0])
            url_01 = 'http://sp.ejw.cn/platform/v1/product/'
            url = url_01 + spProductCode + '/canel-verify'
            result_act = requests.delete(url, headers=headers).text
            print(result_act)
            # 设置预期设为1
            result_exp = 1
            # 判断实际返回码是否与预期的一致
            self.assertEqual(result_exp, int(result_act))
            global log, log_exp, log_act
            log_exp = Logger(logger="服务商平台_预期结果").getlog()
            log_act = Logger(logger="服务商平台_实际结果").getlog()
            log = Logger(logger="服务商平台").getlog()
            log_exp.info(result_exp)
            log_act.info(result_act)
            log.info(spProductCode + "上架审核取消操作成功")
        except LookupError:
            print("没有需要取消上架的方案数据")

    # 方案管理-方案下架审核提交操作
    def test_c003_search(self):
        try:
            # 连接到数据库ps1（分支产品库）
            conn = MySQL().connect_ps()
            # 定义一个游标赋值给变量cur，cur才有权限去执行数据库
            cur = conn.cursor()
            # 数据库中查询服务商id为502，审核状态为-1的产品
            cur.execute(
                'select sp_product_code,sp_product_name from sp_product  where sale_flag = 1 and sp_partner_id = 502 and examine_state = -1')
            # 定义查询数据库表中2个字段sp_product_code，sp_product_name
            cur_data = cur.fetchone()[0:2]
            # 第一个字段赋给变量sp_product_code
            spProductCode = str(cur_data[0])
            # 第二个字段赋给变量sp_product_name
            productName = cur_data[1]
            # 打印查询出来的sp_product_code，sp_product_name这2个字段内容
            print(spProductCode, productName)
            # url地址
            url = 'http://sp.ejw.cn/sp/v1/verify-saleflag'
            # 参数信息
            params = {"spPartnerId": 502, "spProductCode": spProductCode, "productType": "group", "verifyType": 2,
                      "createUser": 164,
                      "productName": productName, "partnerName": "竞网自动化勿删"}
            # 发送上架审核接口请求
            result_act = requests.post(url, data=json.dumps(params), headers=headers)
            # 设置预期返回码200
            result_exp = 200
            # 实际返回码
            result_act_act = result_act.status_code
            # 判断实际返回码是否与预期的一致
            self.assertEqual(result_exp, result_act_act)
            global log, log_exp, log_act
            log_exp = Logger(logger="服务商平台_预期结果").getlog()
            log_act = Logger(logger="服务商平台_实际结果").getlog()
            log = Logger(logger="服务商平台").getlog()
            log_exp.info(result_exp)
            log_act.info(result_act_act)
            log.info(productName + "下架提交成功")
        except LookupError:
            print("没有需要下架的方案数据")

    # 方案管理-方案下架取消提交操作
    def test_c004_search(self):
        try:
            # 连接到数据库ps1（分支产品库）
            conn = MySQL().connect_ps()
            # 定义一个游标赋值给变量cur，cur才有权限去执行数据库
            cur = conn.cursor()
            # 数据库中查询服务商id为502，审核状态为1的产品
            cur.execute(
                'select sp_product_code from sp_product  where sale_flag = 1 and sp_partner_id = 502 and examine_state = 0')
            spProductCode = str(cur.fetchall()[0][0])
            url_01 = 'http://sp.ejw.cn/platform/v1/product/'
            url = url_01 + spProductCode + '/canel-verify'
            # 发送下架取消接口请求
            result_act = requests.delete(url, headers=headers).text
            # 设置预期设为1
            result_exp = 1
            # 判断实际返回码是否与预期的一致
            self.assertEqual(result_exp, int(result_act))
            print(result_act)
            global log, log_exp, log_act
            log_exp = Logger(logger="服务商平台_预期结果").getlog()
            log_act = Logger(logger="服务商平台_实际结果").getlog()
            log = Logger(logger="服务商平台").getlog()
            log_exp.info(result_exp)
            log_act.info(result_act)
            log.info(spProductCode + "下架审核取消操作成功")
        except LookupError:
            print("没有需要下架的方案数据")

    # 方案管理-方案管理-已存在的产品名称查询
    def test_c005_product_serach(self):
        conn = MySQL().connect_ps()
        cur = conn.cursor()
        sql = "select sp_product_name from sp_product t where t.sp_partner_id=" + spId + " order by create_date desc"
        cur.execute(sql)
        productName = str(cur.fetchone()[0])
        log_exp.info(productName)
        url_01 = "http://sp.ejw.cn/ps/v1/spproducts?buyType=&_sort=modifyDate%2Cdesc&pageSize=20&pageNum=1&spPartnerId=" \
                 + spId + "&spProductName="
        url = url_01 + productName
        product_search = requests.get(url, headers=headers)
        # print(product_search.text)
        result_act = product_search.text
        log_act.info(result_act)
        self.assertIn(productName, result_act, msg="查询的产品名字不存在")
        log.info("已有产品名称查询成功")

    # 方案管理-方案管理-不存在的产品名称查询
    def test_c006_product_serach(self):
        productName = 'test11110001'
        log_exp.info(productName)
        url_01 = "http://sp.ejw.cn/ps/v1/spproducts?buyType=&_sort=modifyDate%2Cdesc&pageSize=20&pageNum=1&spPartnerId=" \
                 + spId + "&spProductName="
        url = url_01 + productName
        result_act = requests.get(url, headers=headers).text
        log_act.info(result_act)
        self.assertNotIn(productName, result_act, msg="查询异常或该产品已存在")
        log.info("未查询到该产品信息")

    # 方案管理-供应商授权管理-全部-提交合同
    def test_c007_product_verify(self):
        # 连接ps数据库
        conn1 = MySQL().connect_platform()
        cur1 = conn1.cursor()
        sql = "select auth_id, record_id from product_auth t where t.sp_id=" + spId + " and t.`status`=0"
        cur1.execute(sql)
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

    # 方案管理-供应商授权管理-查询（不存在的）
    def test_c008_product_verify(self):
        productname = "aaaaaxxxxx"
        log_exp.info(productname)
        url_01 = "http://sp.ejw.cn/sp/v1/cp/products?sort=%7B%22createTime%22%3A%22desc%22%7D&pageNo=1&pageSize=10&typeId=&productName="
        url = url_01 + productname
        result_act = requests.get(url, headers=headers).text
        self.assertNotIn(productname, result_act, msg="查询数据异常")
        log_act.info(result_act)
        log.info("不存在的数据查询正常")

    # 方案管理-供应商授权管理-查找（全部）
    def test_c009_product_verify(self):
        url = "http://sp.ejw.cn/platform/v1/productauths?cpId=&spId=" + spId + "&authId=&authType=&status=&pageSize=10&pageNo=1&sort=%7B%22gmtCreate%22%3A%22desc%22%7D"
        result_act = requests.get(url, headers=headers).text
        result_Count = result_act.split("totalCount", 2)[1].split(",")[0].split(":")[1]
        self.assertIsNotNone(result_Count, msg="数据为空或查询异常")
        log_act.info("查询条数为:" + result_Count)

    # 方案管理-供应商授权管理-详情
    def test_c010_product_verify(self):
        url = "http://sp.ejw.cn/os/v1/partners?partnerId=" + spId
        # url = "http://sp.ejw.cn/os/v1/partners?partnerId=190"
        result_act = requests.get(url, headers=headers)
        result_exp = 200
        self.assertEqual(result_exp, result_act.status_code, msg="查看详情存在异常情况")
        log_act.info(result_act.text)

    # 工单管理-标准订单-接单
    def test_c011_order_pay(self):
        global log, log_exp, log_act
        log_exp = Logger(logger="服务商平台_预期结果").getlog()
        log_act = Logger(logger="服务商平台_实际结果").getlog()
        log = Logger(logger="服务商平台").getlog()
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
            print(url)
            params = {"spEmpId": int(spEmpId), "spEmpName": "蒋涛", "orderId": order_id,
                      "spCusContractUrl": "https://bj.bcebos.com/v1/hnjing-test/d45fdb0150674e5baa969192921ad626.rar",
                      "stages": [{"spOrderStageNo": 1, "payDesc": "aaaa", "payAmount": int(pay_price)}]}
            result_act = requests.post(url, data=json.dumps(params), headers=headers).status_code
            result_exp = 200
            self.assertEqual(result_exp, result_act, msg='接单失败')
            log.info("接单成功")
        except TypeError:
            log.info("没有找到需要接单的订单")

    # 工单管理-退款审核-同意退款
    def test_c012_order_pay(self):
        try:
            conn = MySQL().connect_order()
            cur = conn.cursor()
            sql = "select b.pay_id,b.refund_Amount, b.sp_order_id from sp_order_info a, pay_stage_info b where a.order_state=1 and a.sp_partner_id=" + spId + " and b.pay_state=4 and a.sp_order_id=b.sp_order_id;"
            cur.execute(sql)
            ordering = cur.fetchone()[0:3]
            sp_order_id = str(ordering[2])
            refund_Amount = str(ordering[1])
            pay_id = str(ordering[0])
            url = "http://sp.ejw.cn/order/v1/partner/" + spId + "/order/" + sp_order_id + "/paystageinfo/" + pay_id
            print(url)
            params = {"nodeSuggest": "服务商同意退款", "payState": "6", "spEmpId": spEmpId, "spEmpName": "蒋涛",
                      "spPartnerName": "竞网自动化勿删", "refundAmount": refund_Amount, "useCost": "0.00", "refundFee": "0.00"}
            result_act = requests.put(url, data=json.dumps(params), headers=headers).status_code
            print(result_act)
            result_exp = 200
            self.assertEqual(result_exp, result_act, msg='商家退款失败')
            print("商家退款成功")
        except TypeError:
            print("没有找到需要退款的订单")

    # 工单管理-退款审核-不同意退款
    def test_c013_order_pay(self):
        try:
            conn = MySQL().connect_order()
            cur = conn.cursor()
            sql = "select b.pay_id,b.refund_Amount, b.sp_order_id from sp_order_info a, pay_stage_info b where a.order_state=1 and a.sp_partner_id=" + spId + " and b.pay_state=4 and a.sp_order_id=b.sp_order_id;"
            cur.execute(sql)
            ordering = cur.fetchone()[0:3]
            sp_order_id = str(ordering[2])
            refund_Amount = str(ordering[1])
            pay_id = str(ordering[0])
            url = "http://sp.ejw.cn/order/v1/partner/" + spId + "/order/" + sp_order_id + "/paystageinfo/" + pay_id
            params = {"nodeSuggest": "服务商不同意退款", "payState": "5", "spEmpId": spEmpId, "spEmpName": "蒋涛",
                      "spPartnerName": "竞网自动化勿删", "refundAmount": refund_Amount, "useCost": "0.00", "refundFee": "0.00"}
            result_act = requests.put(url, data=json.dumps(params), headers=headers).status_code
            result_exp = 200
            self.assertEqual(result_exp, result_act, msg='商家不退款失败')
            log.info("工单管理-退款审核-商家不同意退款")
        except TypeError:
            log.info("没有找到不退款的订单")

    # 方案管理-优惠券管理-新增优惠券
    def test_c014_coupon_add(self):
        params = {"couponName": "自动化_优惠01", "couponAmount": "1", "useType": "0", "ownType": "1", "fullValue": "",
                  "couponValue": "1", "conditionType": "0", "conditionCount": "", "publishDateStart": 1543248000,
                  "publishDateEnd": 1577721600, "validTimeStart": 1543248000, "validTimeEnd": 1577721600,
                  "description": "这是一张测试券", "createUser": createUser, "compId": 2}
        url = "http://sp.ejw.cn/marketing/v2/coupon-info"
        result = requests.post(url, data=json.dumps(params), headers=headers)
        result_exp = 200
        result_act = result.status_code
        self.assertEqual(result_exp, result_act, msg="优惠券新增失败")


    # 方案管理-优惠券管理-新增优惠码
    # def test_c015_coupon_add(self):
    #     params = {"couponName": "自动化_优惠01", "couponAmount": "1", "useType": "0", "ownType": "1", "fullValue": "",
    #               "couponValue": "1", "conditionType": "0", "conditionCount": "", "publishDateStart": 1543248000,
    #               "publishDateEnd": 1577721600, "validTimeStart": 1543248000, "validTimeEnd": 1577721600,
    #               "description": "这是一张测试券", "createUser": spEmpId, "compId": spId}
    #     url = "http://sp.ejw.cn/marketing/v2/coupon-info"
    #     result = requests.post(url, data=json.dumps(params), headers=headers)
    #     result_exp = 200
    #     result_act = result.status_code
    #     self.assertEqual(result_exp, result_act)


if __name__ == '__main__':
    unittest.main()
