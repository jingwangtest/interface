import requests
import json
import unittest
from comm.login import Zpt
from contentfair.task_create import task_create
from comm.public_data import MySQL

compId = 23
userId = 612
username = "乐扣杯4"
response_code = 200

cookies_token = Zpt.user_login()
header = {"Content-Type": "application/json; charset=utf-8", "token": cookies_token}

class contentfair_share(unittest.TestCase):
    # 查询用户是否接收到任务
    def test_c003_select_share_task(self):
        taskid = task_create.test_c002_create_task(self)
        url = 'http://user.ejw.cn/saas_contentfair/v1/share-task?pageNo=1&pageSize=20'
        try:
            select_share_task = requests.get(url, headers=header)
            result_code = select_share_task.status_code
            if self.assertEqual(response_code, result_code):
                print("用户中心_查询分享管理列表异常,接口返回码非200")
            else:
                jsonData = {}
                jsonData = select_share_task.json()
                task_id = jsonData['data'][0]['taskId']
                if taskid == task_id:
                    print("用户接收到任务啦！！可以继续执行a002、a003的用例")
                else:
                    print("用户没有收到任务！！")
        except OSError as err:
            print("用户中心_查询分享管理列表,数据为空")

    # 点击分享任务，复制链接操作
    def test_c004_shareParamUrl(self):
        taskid = task_create.test_c002_create_task(self)
        sql = 'select sub_task_id,read_count from share_sub_task_info where task_id=' + str(taskid) + '  and create_user_id=' + str(userId)
        # 查询用户分享任务的子id
        conn = MySQL().connect_content_fair()
        cur1 = conn.cursor()
        cur1.execute(sql)
        result_sql = cur1.fetchall()
        subTaskId = result_sql[0][0]
        start_read = result_sql[0][1]
        url01 = 'http://user.ejw.cn/saas_contentfair/v1/sub-task/'
        url = url01 + str(subTaskId)
        shareParamUrl = requests.put(url, headers=header)
        result_code = shareParamUrl.status_code
        if response_code == result_code:
            #print("用户中心_获取分享链接成功")
            jsonData = {}
            jsonData = shareParamUrl.json()
            shareParamUrl = jsonData['shareParamUrl']
            # 复制链接，进行分享任务操作
            share_task = requests.get(shareParamUrl, headers=header)
            result_code2 = share_task.status_code
            if response_code == result_code2:
                # 查询子任务的阅读数
                conn = MySQL().connect_content_fair()
                cur1 = conn.cursor()
                cur1.execute(sql)
                result_sql = cur1.fetchall()
                end_read = result_sql[0][1]
                if end_read - start_read == 1:
                    print("任务分享成功，用户任务阅览数+1")
                else:
                    print("任务分享失败，用户任务阅览数", end_read)
        else:
            print("用户中心_获取分享链接失败")


if __name__ == '__main__':
    unittest.main()
