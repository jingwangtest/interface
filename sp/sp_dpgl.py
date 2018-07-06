# 服务商-店铺管理
import requests
import random
import json
import unittest
from comm.login import testlogin_001
from comm.sp_data import MySQL

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

class sp_dpgl_01(unittest.TestCase):
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
        result = requests.post(url, data=json.dumps(params), headers=headers)
        print(result)
        print(type(result))
        if result.status_code == 200:
            print(caseName+"新增成功")
        else:
            print(caseName+"新增失败")

    # 店铺管理-案例管理-删除
    def test_a002_role_del(self):
        # 设置案例名称
        caseName_01 = ''.join(random.sample(['8', '6', '3', '2', '5', '6'], 4))
        caseName_02 = '案例生成'
        caseName = caseName_02 + caseName_01
        conn = MySQL().connect_mall1('conn')
        cur = conn.cursor()
        sql_data = '190'
        # 查询出当前要删除案例的id信息
        cur.execute('select case_id from class_case_info t where t.sp_id = "' + sql_data + '"')
        total = str(cur.fetchall()[0][0])
        print(total)
        url_01 = 'http://sp.ejw.cn/mall/v1/classcaseinfo/'
        url = url_01 + total
        print(url)
        case_delete_act = requests.delete(url, headers=headers).text
        print(case_delete_act)
        case_delete_exp = 1
        if case_delete_exp == case_delete_act:
            print("案例删除成功")

    # 店铺管理-案例管理-已存在的用户名查询
    def test_a003_role_del(self):
        conn = MySQL().connect_mall1('conn')
        cur = conn.cursor()
        sql_data = '190'
        # 查询出当前要删除案例的id信息
        cur.execute('select case_name from class_case_info t where t.sp_id = "' + sql_data + '"')
        total = str(cur.fetchall()[0][0])
        print(total)
        url_01 = 'http://sp.ejw.cn/mall/v1/classcaseinfos?spId=190&caseState=&pageSize=10&pageNo=1&caseName='
        url = url_01 + total
        print(url)
        case_search_act = requests.get(url, headers=headers).text
        print(type(case_search_act))
        if total in case_search_act:
            print("案例名称查询信息成功")
        else:
            print("案例名称查询信息失败")

    # 店铺管理-案例管理-不存在的用户名查询
    def test_a004_role_search(self):
        total = "天天向上1111111"
        print(total)
        url_01 = 'http://sp.ejw.cn/mall/v1/classcaseinfos?spId=190&caseState=&pageSize=10&pageNo=1&caseName='
        url = url_01 + total
        print(url)
        case_search_act = requests.get(url, headers=headers).text
        print(type(case_search_act))
        if total in case_search_act:
            print("案例查询fail")
        else:
            print("案例名称查询pass")

        # 店铺管理-营销锦囊-新增角色

    def test_b001_jn_add(self):
        url = "http://sp.ejw.cn/mall/v1/marketingpolicy"
        params = {"spId": 190,
                  "policyImage": "http://hnjing-test.bj.bcebos.com/v1/hnjing-test/f8828654e9004d59a785a9238d6ccab0.jpg",
                  "policyState": "2", "createUser": 24, "policyName": jnName, "industryId": 18,
                  "policyDesc": "智能营销无限给力", "policyContent": "<p>营销大销售了，我们的发展无限潜力<br/></p>"}
        result = requests.post(url, data=json.dumps(params), headers=headers)
        result_code_act = result.status_code
        result_code_exp = 200
        result_text_act = result.text
        if jnName in result_text_act and result_code_exp == result_code_act:
            print(jnName + '营销锦囊新增成功')
        else:
            print(jnName + "营销锦囊新增失败")
        print(result_text_act)

    # 店铺管理-营销锦囊-删除
    def test_b002_jn_del(self):
        conn = MySQL().connect_mall1('conn')
        cur = conn.cursor()
        sql_data = '190'
        # 查询出当前要删除案例的id信息
        cur.execute('select policy_id from marketing_policy t where t.sp_id = "' + sql_data + '"')
        total = str(cur.fetchall()[0][0])
        # print(total)
        url_01 = 'http://sp.ejw.cn/mall/v1/marketingpolicy/'
        url = url_01 + total
        # print(url)
        case_delete_act = requests.delete(url, headers=headers).text
        # print(type(case_delete_act))
        case_delete_exp = 1
        if case_delete_exp == int(case_delete_act):
            print("案例删除成功")
        else:
            print("案例删除失败")

    # 店铺管理-营销锦囊-已存在的用户名查询
    def test_b003_jn_search(self):
        conn = MySQL().connect_mall1('conn')
        cur = conn.cursor()
        sql_data = '190'
        # 查询出当前要删除案例的id信息
        cur.execute('select policy_Name from marketing_policy t where t.sp_id = "' + sql_data + '"')
        total = str(cur.fetchall()[0][0])
        # print(total)
        url_01 = 'http://sp.ejw.cn/mall/v1/marketingpolicys?spId=190&policyState=&pageNo=1&pageSize=10&policyName='
        url = url_01 + total
        # print(url)
        case_search_act = requests.get(url, headers=headers).text
        # print(type(case_search_act))
        if total in case_search_act:
            print("案例名称查询信息成功")
        else:
            print("案例名称查询信息失败")

    # 店铺管理-营销锦囊-不存在的用户名查询
    def test_b004_jn_search(self):
        total = "test000000011111"
        print(total)
        url_01 = 'http://sp.ejw.cn/mall/v1/marketingpolicys?spId=190&policyState=&pageNo=1&pageSize=10&policyName='
        url = url_01 + total
        print(url)
        case_search_act = requests.get(url, headers=headers)
        print(case_search_act)
        if case_search_act == 200:
            print("查询营销锦囊正常")
        else:
            print("查询信息有异常情况")

    # 店铺管理-产品管理-产品上下架管理-发布产品-产品名称查询
    def test_c001_product_search(self):
        conn = MySQL().connect_ps1('conn')
        cur = conn.cursor()
        cur.execute("select t.product_name from product t where t.partner_type=0010 and sale_flag=1 and partner_id=190")
        product_name = cur.fetchone()[0]
        url_01 = "http://sp.ejw.cn/sp/v1/sproductauth?partnerId=190&cpPartnerId=&productType=&productName="
        url = url_01 + product_name
        product_search = requests.get(url, headers=headers)
        product_name_act = json.loads(product_search.text)["products"][0]["partnerName"]
        # print(product_name_act)
        if product_name == product_name_act:
            print("# 店铺管理-产品管理-产品上下架管理-发布产品-产品名称查询： 产品信息查询成功")
        else:
            print("# 店铺管理-产品管理-产品上下架管理-发布产品-产品名称查询： 该服务商没有相应的产品，请先新增产品再发布")

    # 店铺管理-产品管理-产品上下架管理-新增产品
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

        product_search_01 = requests.post(url, data=json.dumps(params), headers=headers)
        print(product_search_01.text)
        if prodctName in product_search_01.text:
            print(prodctName + '新增成功')
        else:
            print(prodctName + '新增失败')

    # 店铺管理-产品管理-产品上下架管理-发布产品-申请审核
    def test_c003_product_verify(self):
        conn = MySQL().connect_ps1('conn')
        cur = conn.cursor()
        cur.execute(
            "select uuid from product t where t.partner_id=190 and t.partner_type=0100 order by create_time desc;")
        product_id = cur.fetchone()[0]
        url = "http://sp.ejw.cn/sp/v1/productverify"
        params = {"partnerId": 190, "productId": product_id, "productType": "group", "verifyType": 1,
                  "createUser": 24, "partnerType": "0100"}
        product_search = requests.post(url, data=json.dumps(params), headers=headers)
        product_name_act = json.loads(product_search.text)
        print(product_name_act)
        if product_name_act == 1:
            print("# 店铺管理-产品管理-产品上下架管理-发布产品审核： 已发送审核邀请")
        else:
            print("# 店铺管理-产品管理-产品上下架管理-发布产品审核： 审核中断")

    # 店铺管理-产品管理-产品上下架管理-发布产品-审核取消
    def test_c004_product_verify(self):
        conn = MySQL().connect_platform1('conn')
        cur = conn.cursor()
        cur.execute(
            "select verify_id from product_verify where partner_id=190 and product_type='group' ORDER BY gmt_modified desc")
        url_02 = str(cur.fetchone()[0])
        url_01 = "http://sp.ejw.cn/platform/v1/productverify/"
        url = url_01 + url_02
        product_search = requests.delete(url, headers=headers)
        product_name_act = json.loads(product_search.text)
        print(product_name_act)
        if product_name_act == 1:
            print("# 店铺管理-产品管理-产品上下架管理-发布产品审核取消： 已取消审核邀请")
        else:
            print("# 店铺管理-产品管理-产品上下架管理-发布产品审核取消： 取消审核中断")

    # 店铺管理-产品管理-产品上下架管理-已存在的产品名称查询
    def test_c005_product_serach(self):
        conn = MySQL().connect_ps1('conn')
        cur = conn.cursor()
        cur.execute(
            "select product_name from product t where t.partner_id=190 and t.partner_type=0100 order by create_time desc")
        productName = str(cur.fetchone()[0])
        url_01 = "http://sp.ejw.cn/sp/v1/sp/190/products?productType=&pageSize=10&pageNo=1&productName="
        url = url_01 + productName
        print(url)
        product_search = requests.get(url, headers=headers)
        # print(product_search.text)
        product_name_act = json.loads(product_search.text)["products"][0]["productName"]
        # print(type(product_name_act))
        if product_name_act == productName:
            print(productName+'查询成功')
        else:
            print(productName+'查询失败')

    # 店铺管理-产品管理-产品上下架管理-不存在的产品名称查询
    def test_c006_product_serach(self):
        productName = 'test11110001'
        url_01 = "http://sp.ejw.cn/sp/v1/sp/190/products?productType=&pageSize=10&pageNo=1&productName="
        url = url_01 + productName
        print(url)
        product_search = requests.get(url, headers=headers)
        # print(product_search.text)
        product_name_01 = product_search.text
        product_name_act = product_name_01.split("products", 2)[1].split(":", 2)[1]
        # print(type(product_name_act))
        if product_name_act in product_name_act:
            print(productName + "查询数据为空")
        else:
            print("查询数据出错")

    # 店铺管理-产品管理-产品上下架管理-产品采购-产品授权
    def test_c007_product_verify(self):
        # 连接ps数据库
        conn1 = MySQL().connect_ps1('conn')
        cur1 = conn1.cursor()
        cur1.execute(
            "select uuid from product t where t.partner_id=190 and t.partner_type=0010 and sale_flag=0 order by create_time desc")
        products = cur1.fetchone()[0]
        url = "http://sp.ejw.cn/platform/v1/productauth"
        params = {"authType": 1, "spId": "190", "cpId": "190", "products": [products]}
        product_verify = requests.post(url, data=json.dumps(params), headers=headers)
        if product_verify.status_code == 200:
            print("授权成功")
        else:
            print("授权失败")

    # 店铺管理-产品管理-产品上下架管理-产品授权-查询（不存在的）
    def test_c008_product_verify(self):
        url = "http://sp.ejw.cn/sp/v1/cp/products?sort=%7B%22createTime%22%3A%22desc%22%7D&typeId=&productName=xxxx&pageNo=1&pageSize=10"
        product_seach = requests.get(url, headers=headers).text
        product_name_act = product_seach.split("products", 2)[1].split(":", 2)[1]
        # print(type(product_name_act))
        if product_name_act in product_name_act:
            print("查询数据为空pass")
        else:
            print("查询数据出错")

   # 店铺管理-产品管理-产品上下架管理-授权管理（全部）
    def test_c009_product_verify(self):
        url = "http://sp.ejw.cn/platform/v1/productauths?cpId=&spId=190&authId=&authType=&status=&pageSize=10&pageNo=1&sort=%7B%22gmtCreate%22%3A%22desc%22%7D"
        try:
            product_seach = requests.get(url, headers=headers).text
            totalCount = int(product_seach.split("totalCount", 2)[1].split(",")[0].split(":")[1])
            if totalCount > 0:
                totalCount = str(totalCount)
                print("符合条件的记录有" + totalCount + "条")
            else:
                print("没有查询到符合的条件")
        except:
            print("请求数据存在异常")

    # 店铺管理-产品管理-产品上下架管理-产品授权管理-详情
    def test_c010_product_verify(self):
        conn = MySQL().connect_platform1('conn')
        cur = conn.cursor()
        cur.execute("select cp_id,auth_id from product_auth where sp_id=190")
        product_name = str(cur.fetchone()[0])
        product_name_01 = str(cur.fetchone()[1])
        print(product_name_01)
        url_01 = "http://sp.ejw.cn/os/v1/partners?partnerId="
        url = url_01+product_name
        try:
            product_seach = requests.get(url, headers=headers).status_code
            if product_seach == 200:
                print("授权单号"+product_name_01+"查询正常")
            else:
                print("授权单号"+product_name_01+"没有查询到该信息")
        except:
            print("查询数据列表为空")





if __name__ == '__main__':
    unittest.main()
