import requests
import unittest
import json
import random
from comm.login import testlogin_001
from comm.Log import Logger


# 请求头信息
token = testlogin_001().test_emplogin('token')
headers = {
    'Host': 'emp.hnjing.com',
    'Connection': 'keep-alive',
    'token': token,
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
    'Referer': 'http://emp.hnjing.com/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}
class emp_01(unittest.TestCase):
    #def test_oragn_001(self):
        #organName = '长沙伊特诺教育咨询有限公司'
        #url = "http://emp.hnjing.com/emp_os/v1/organ"
        #params = {"organName":"长沙伊特诺教育咨询有限公司","sharesType":0,
        #          "oragnShortName":"教育咨询","oragnShortEname":"zixun","partnerId":190,"creator":68}
        #organ_add = requests.post(url,data=json.dumps(params),headers=headers)
        #result_add = organ_add.text
        #result_exp = 1
        #self.assertIn(result_exp,int(result_add))
        #print("新增成功")

    def test_oragn_002(self):
        url_dz = "http://emp.hnjing.com/emp_os/v1/organs?pageNum=1&pageSize=20&organName="
        oragnname = "中天控股集团有限公司"
        url = url_dz + oragnname
        print(url)
        oragn_check = requests.get(url,headers=headers)
        result = oragn_check.text
        self.assertIn(oragnname,result)
        print("查询成功")

if __name__ == '__main__':
     unittest.main()