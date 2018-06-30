# 运营平台-合作伙伴管理
import requests
import random
import json
import unittest
from interface.comm.login import testlogin_001
from interface.comm.sp_data import MySQL

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
        if fws_test.status_code == 200:
            print(prodctName + "新增成功")
        else:
            print(prodctName + "新增失败")

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
        if fws_test.status_code == 200:
            print(prodctName + "新增成功")
        else:
            print(prodctName + "新增失败")



if __name__ == '__main__':
    unittest.main()
