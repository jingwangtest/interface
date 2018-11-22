import requests
import json

class cc001():
    # 验证登陆是否成功
    def cc_login(self, token):
        params = {"mobilePhone": "17708490601", "password": "123456", "remember": True, "siteName": "main"}
        url = "http://auth.ejw.cn/api/login"
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'Accept - Encoding': 'gzip, deflate',
            'Accept - Language': 'en-US,en;q=0.9',
            'Referer': 'http://auth.ejw.cn/?backUrl=http%3A%2F%2F192.168.150.34%3A8057%2Fcc%2Fv1%2F%23%2F',
            'X-Requested-With': 'XMLHttpRequest'
        }
        print(headers)
        token_act = requests.post(url, data=json.dumps(params), headers=headers)
        # print(token_act)
        # result_exp = 200
        # result_act = token_act.status_code
        # self.assertEqual(result_exp, result_act, msg="用户登陆失败")
        # print("用户登录成功")
        s = json.loads(token_act.text)
        # print(s)
        values = s["data"]["access_token"]
        # print(values)
        return values