# 运营平台-合作伙伴管理
import requests
import random
import json
import unittest
from comm.login import testlogin_001
from comm.public_data import MySQL
from comm.Log import Logger
from urllib.parse import quote

log = Logger(logger="管理平台").getlog()

# 请求头信息
token = testlogin_001().test_adminlogin('token')
print(token)
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'token': token
}


class admin_yygl(unittest.TestCase):
    def test_a001(self):
        text = quote("自动化模板auto5366", 'utf-8')
        log.info(text)

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
            "partner": {
                "partnerType": "0010",
                "partnerName": prodctName,
                "area": "湖南/长沙",
                "address": "岳麓",
                "phone": "0371-86241125",
                "level": 5,
                "detail": "im"
            },
            "partnerBusiness": {
                "uscCode": uscCode,
                "beginDate": "2014-01-06",
                "validDate": "2064-01-05",
                "companyType": "有限责任公司(自然人投资或控股)",
                "registAddress": "长沙市开福区车站北路649号天都大厦第1幢N单元21层21022号房",
                "legalPerson": "欧阳凤贵",
                "registAuthority": "长沙市工商行政管理局开福分局",
                "approvalDate": "2016-12-27",
                "registStatus": "存续（在营、开业、在册）",
                "registCapital": 1000,
                "scope": "智能化技术研发；工程和技术研究和试验发展；",
                "legalPersonIdcode": "430624199802031256"
            },
            "partnerExt": {
                "standardIndustry": "612",
                "category": "44"
            },
            "partnerQualifys": [{
                "qualifyType": 1,
                "qualifyImage": "https://bj.bcebos.com/v1/hnjing-test/310327dcbb4e4f6da4955aa803677bf7.jpg",
                "qualifyName": "营业执照",
                "qualifyBeginDate": "2014-01-06",
                "qualifyValidDate": "2064-01-05"
            }, {
                "qualifyType": 2,
                "qualifyImage": "https://bj.bcebos.com/v1/hnjing-test/1d058c38f44741e0a3183ebe488302c4.jpg,https://bj.bcebos.com/v1/hnjing-test/d18a5950035f4c75815a371289d23a45.jpg",
                "qualifyName": "法人身份证",
                "qualifyBeginDate": "2018-07-09",
                "qualifyValidDate": "2018-07-31"
            }],
            "employees": {
                "empName": "测试",
                "phone": "15812205665",
                "email": "15814405932@139.com"
            }
        }
        values = json.dumps(parms)
        # 发送服务商接口请求
        fws_test = requests.post(url, data=values, headers=headers)
        result_exp = 200
        result_act = fws_test.status_code
        # print(fws_test.text)
        self.assertEqual(result_exp, result_act)
        log.info("新增服务商成功ABCDEFG111abcd")


if __name__ == '__main__':
    unittest.main()
