import requests
import json
from comm.login import Zpt

# #请求头信息
token = Zpt().test_emp_login()
url = "http://emp.hnjing.com/api/login"

# 指定头文件
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'token': token
}


class Emp:
    @staticmethod
    def emp_login():
        token_act = requests.get(url, headers=headers)
        s = json.loads(token_act.text)
        values = s["data"]["token"]
        return values
