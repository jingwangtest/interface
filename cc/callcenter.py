import unittest
import requests
import json
import random
import datetime

from cc.cc_login import cc001

# 请求头信息
token = cc001().cc_login('token')
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'token': token
}

class task_001(unittest.TestCase):

    # 新建任务类型
    def test_a00l(self):
        #随机生成任务类型名称
        typename_01 = ''.join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 3))
        typename_02 = 'test'
        typename = typename_02 + typename_01
        params = {"typeName": typename, "show": True}
        url = "http://192.168.150.34:8057/cc/v1/taskmanage/type"
        # 发送请求
        test_act = requests.post(url, data=json.dumps(params), headers=headers)
        result_act = test_act.text
        result_json = json.loads(result_act)
        result_id = result_json["id"]
        print(type(result_id), result_id)
        # result_exp = 200
        # print(result_exp, test_act)
        # # # # 判断当前返回码及字段值
        # self.assertEqual(result_exp, test_act, msg='新增任务类型失败')
        # print("新增任务类型成功")
        #log.info("新增任务类型成功")

    #新建任务计划
    def test_a002(self):
        # 随机生成计划名称
        planname_01 = ''.join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 3))
        planname_02 = 'plan'
        planname = planname_02 + planname_01
        params = {"planName": planname, "planDesc": "新建计划类型", "bizTemplateId": 5, "taskType": 142, "createUserName": ""}
        url = "http://192.168.150.34:8057/cc/v1/taskmanage/plan/type"
        # 发送请求
        test_act = requests.post(url, data=json.dumps(params), headers=headers).status_code
        result_exp = 200
        print(result_exp, test_act)
        # 判断当前返回码及字段值
        self.assertEqual(result_exp, test_act, msg='新增计划类型失败')
        print("新增计划类型成功")
        #log.info("新增计划类型成功")

    # 新增电话计划
    def test_a003(self):
        params = {"planType": 201, "taskTotal": 3, "expireTime": "2018-11-16T16:00:00.000Z", "dispatchType": 2, "taskType": 82, "fileKey": "35d8d35f1b5fbbbda14ebfb5d22ecceb"}
        url = "http://192.168.150.34:8057/cc/v1/taskmanage/partner/out/plan"
        #发送请求
        test_act = requests.post(url, data=json.dumps(params), headers=headers).status_code
        result_exp = 200
        print(result_exp, test_act)
        #判断当前返回码及字段值
        self.assertEqual(result_exp, test_act, msg='新增电话计划失败')
        print('新增电话计划成功')

    #新建群发短信
    def test_a004(self):
        now = datetime.datetime.utcnow()
        send_time = now.strftime('%Y-%m-%dT%XZ')
        params = {"sendTime": send_time, "taskType": 142, "planType": 203, "smsTemplateId": 42, "taskTotal": 1, "bizType": "直通车", "content": "通过服务弹屏页面发送短信", "fileKey": "0e214fdfbeeedbf71fcdbb0afc5693e0"}
        url = "http://192.168.150.34:8057/cc/v1/taskmanage/broadcastsms/plan"
        # 发送请求
        test_act = requests.post(url, data=json.dumps(params), headers=headers).status_code
        result_exp = 200
        print(result_exp, test_act)
        # 判断当前返回码及字段值
        self.assertEqual(result_exp, test_act, msg='群发短信失败')
        print("群发短信成功")

    #创建工单
    def test_a005(self):
        customername = "湖南阳光富源test有限公司"
        customerid = "20130109050456"
        contactname = "张san"
        customerTel = "18511338082"
        now = datetime.datetime.now()
        now_time = now.strftime('%Y-%m-%d %X')
        content = "test创建工单"
        params = {"action": "2", "orderType": "4", "customerName": customername, "customerId": customerid, "contactName": contactname, "customerTel": customerTel, "contactTime": now_time, "contactType": "1", "serviceType": "consulting", "subServiceType": "consulting1", "serviceObj": "1", "actualDispose": "", "content": content, "fileList": [], "limitHour": "24", "skillGroup": 33, "disposeUserId": 1696, "projectId": "39"}
        url = "http://192.168.150.34:8057/cc/v1/ticket"
        #发送请求
        test_act = requests.post(url, data=json.dumps(params), headers=headers).status_code
        result_exp = 200
        print(result_exp, test_act)
        #判断当前返回码及字段值
        self.assertEqual(result_exp, test_act, msg= '创建工单失败')
        print('创建工单成功')

    #处理工单
    def test_a006(self):
        content = "暂存一次"
        workOrderId = 187
        # params = {"action": 3, "content": content, "tags": null, "fileList": [], "urgeSrc": null, "urgeMessage": null, "urgeSms": null, "urgeEmail": null, "workOrderId": workOrderId}
        params = {"action": 3, "content": content, "workOrderId": workOrderId}
        url = "http://192.168.150.34:8057/cc/v1/workOrderDisposeFlow"
        #发送请求
        test_act = requests.post(url, data=json.dumps(params), headers=headers).status_code
        result_exp = 200
        print(result_exp, test_act)
        # 判断当前返回码及字段值
        self.assertEqual(result_exp, test_act, msg='暂存失败')
        print('暂存成功')

    #创建质检模板
    def test_a007(self):
        name = "加分制_test001"
        params = {"name": name, "summary": "这是一个质检模板", "mode": 1, "passScore": "66", "items": [{"name": "语音速度", "summary": "不快不慢", "weight": "88"}]}
        url = "http://192.168.150.34:8057/cc/v1/quality-inspection-template"
        #发送请求
        test_act = requests.post(url, data = json.dumps(params), headers = headers).status_code
        result_exp = 200
        print(result_exp, test_act)
        #判断当前返回码及返回值
        self.assertEqual(result_exp, test_act, msg = '创建失败')
        print('创建成功')


if __name__ == '__main__':
    unittest.main()