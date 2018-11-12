# -*- coding: utf-8 -*-
# @Time    : 2018/3/18 09:36
# @Author  : jt

import requests
import unittest
import json
import random
from comm.public_data import MySQL
from comm.login import testlogin_001
from comm.Log import Logger

# 请求头信息
token = testlogin_001().test_culogin('token')
print(token)
# 指定头文件
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'token': token
}


#
class empA01(unittest.TestCase):
    def test_oragn1_001(self):
        conn = MySQL().connect_platform1('conn')
        cur1 = conn.cursor()
        cur1.execute('select partner_id from partner where partner_name ="' + name_01 + '"')
        par_result = cur1.fetchone()
        url = "http://admin.ejw.cn/platform/v1/arbitrate/108?curEmpId=1720"
        params = {"partner": {"partnerName": "盛秀玲111", "area": "湖南/长沙/岳麓区", "address": "麓谷", "phone": "0731-2574155",
                              "detail": "", "partnerType": "0001", "organizeType": 1},
                  "employees": {"empName": "盛秀玲", "phone": "15074980908", "email": "", "partnerId": 157, "userId": 92},
                  "partnerExt": {"standardIndustry": "1"},
                  "partnerBusiness": {"organizeType": 1, "uscCode": "066554132665266565", "businessCode": "",
                                      "companyType": "长城", "registAddress": "台阶", "legalPerson": "灰尘", "scope": "功能",
                                      "registAuthority": "功勋", "approvalDate": "2018-11-12", "registStatus": "正常",
                                      "registCapital": 40000000}, "partnerQualifys": [
                {"qualifyType": 1, "qualifyName": "天天向上", "qualifyValidDate": "2019-11-30",
                 "qualifyImage": "https://bj.bcebos.com/v1/hnjing-test/ddf61aa7eaa44621918daa0738ac8b49.jpg?authorization=bce-auth-v1%2Fed6cb82c3c054636aec25bdbc65d7c10%2F2018-11-05T09%3A40%3A35Z%2F-1%2F%2F0aedf26ba5e0a2a625ed4150e27d28b1b57551b920fc694967fe5431c643c903"}],
                  "partnerAudit": {"status": 1}}
        # print(json.dumps(params, ensure_ascii=False, indent=2))
        sss = json.dumps(params)
        # print(sss)
        organ_add = requests.put(url, data=sss, headers=headers)
        print(organ_add)

        result_add = organ_add.text
        print(result_add)
        result_exp = 1
        self.assertIn(result_exp, int(result_add))


if __name__ == '__main__':
    unittest.main()
