import requests
import unittest
from emp.login_emp import testlogin_001

# 请求头信息
token = testlogin_001().emplogin('token')
# 指定头文件
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'token': token
}


class emp_01(unittest.TestCase):
    def test_oragn_002(self):
        url_dz = "http://emp.hnjing.com/emp_os/v1/organs?pageNum=1&pageSize=20&organName="
        oragnname = "中天控股集团有限公司"
        url = url_dz + oragnname
        print(url)
        oragn_check = requests.get(url, headers=headers)
        result = oragn_check.text
        self.assertIn(oragnname, result)
        print("查询成功")


if __name__ == '__main__':
    unittest.main()
