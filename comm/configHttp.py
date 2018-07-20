import requests
import unittest
import readConfig as readConfig
import json

# from interface.comm.Log import MyLog as Log

localReadConfig = readConfig.ReadConfig()
url = localReadConfig.get_http('url')
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0',
    'Accept - Encoding': 'gzip, deflate',
    'Accept - Language': 'zh - CN, zh;q = 0.9',
    'Referer': 'http://www1.ejw.cn/auth/?backUrl=http%3A%2F%2Fadmin.ejw.cn%2F%23%2F',
    'X-Requested-With': 'XMLHttpRequest'
}
params = {'mobilePhone': '13822236665', 'password': '123456', 'remember': 'true',
          'siteName': 'main'}

class ConfigHttp(unittest.TestCase):
    def test_post(self):
        try:
            response_act = requests.post(url, headers=headers, data=json.dumps(params)).status_code
            response_exp = 200
            if self.assertEqual(response_exp, response_act):
                print("登陆成功")
            # response.raise_for_status()
        except:
            print("请求错误")


if __name__ == '__main__':
    unittest.main()
