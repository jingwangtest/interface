import requests
import json
from comm.login import testlogin_001


# #请求头信息
token = testlogin_001().test_emplogin('token')
url = "http://emp.hnjing.com/api/login"

# 指定头文件
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'token': token
}

class testlogin_001():
    def emplogin(self, token):
        token_act = requests.get(url, headers=headers)
        s = json.loads(token_act.text)
        values = s["data"]["token"]
        return values



