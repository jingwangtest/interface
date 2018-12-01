import requests
import json
import unittest
from comm.login import Zpt
from comm.public_data import MySQL

compId = 23
userId = 612
username = "乐扣杯4"
response_code = 200

cookies_token = Zpt.sp_login()
header = {"Content-Type": "application/json; charset=utf-8", "token": cookies_token}


class task_create(unittest.TestCase):
    # 内容集市新增文章
    def test_c001_add_multi(self):
        url01 = 'http://sp.ejw.cn/saas_contentfair/v1/multi-text/'
        url = url01 + str(compId)
        params = {"title": "新增文章的标题001", "summary": "文章内容", "content": "<p>add</p>",
                  "coverImgUrl": "https://bj.bcebos.com/v1/hnjing-test/38108da310434a24ae39b3acbac290b6.jpg",
                  "createUserId": str(userId), "createUserName": username, "compId": compId}
        add_multi = requests.post(url, data=json.dumps(params), headers=header)
        result_code = add_multi.status_code
        # 判断当前返回码及字段值
        self.assertEqual(response_code, result_code, msg='内容集市_新增文章异常')
        print("内容集市_新增文章成功")

    # 内容发布任务
    def test_c002_create_task(self):
        # 连接scontentfair数据库获取新增文章的文章contentNo
        conn = MySQL().connect_content_fair()
        cur1 = conn.cursor()
        cur1.execute('select content_no from multi_text_info ORDER BY create_date DESC  LIMIT 0,1')
        result_sql = cur1.fetchall()
        # print("数据库返回的结果", result_sql)
        contentNo = result_sql[0][0]
        print(contentNo)
        # 获取当前企业id下所有已绑定的员工id和员工姓名
        conn = MySQL().connect_os()
        cur3 = conn.cursor()
        cur3.execute('select emp_id,emp_name from employee where user_id>0 AND partner_id= "' + str(compId) + '" ')
        result_sql3 = cur3.fetchall()
        print("打印数据库返回的员工id和姓名", result_sql3)
        empIds01 = []
        empIds = []
        i = 0
        while i < len(result_sql3):
            sss = result_sql3[i][0]
            tttt = result_sql3[i][1]
            empIds01 = [{"createUserId": sss, "createUserName": tttt}]
            empIds = empIds + empIds01
            i = i + 1
        else:
            print("退出循环_获取员工id和姓名")
        # 获取循环后的值
        # print(empIds)
        # 设置url地址
        url01 = 'http://sp.ejw.cn/saas_contentfair/v1/share-task/'
        url = url01 + str(compId)
        shareUrl01 = 'http://sp.ejw.cn#/content_market/article_detail?compId='
        shareUrl = shareUrl01 + str(compId) + '&contentNo=' + contentNo
        url01 = 'http://sp.ejw.cn/saas_contentfair/v1/share-task/'
        url = url01 + str(compId)
        params = {"compId": compId, "contentNo": contentNo, "title": "000", "taskDesc": "123",
                  "taskPlanEndTime": "2019-12-30T16:00:00.000Z",
                  "taskCoverUrl": "https://bj.bcebos.com/v1/hnjing-test/707694c447ce45ddb4b03da8f11460e1.jpg",
                  "shareUrl": shareUrl,
                  "taskUrl": "https://user.ejw.cn/#/share-task", "createUserId": userId, "createUserName": username,
                  "empIds": empIds}
        create_task = requests.post(url, data=json.dumps(params), headers=header)
        result_code = create_task.status_code
        if self.assertEqual(response_code, result_code):
            print("内容集市_发布任务异常")
        else:
            jsonData = {}
            jsonData = create_task.json()
            taskId = jsonData['taskId']
            print("内容集市_发布任务的任务id", taskId)
            return taskId


if __name__ == '__main__':
    unittest.main()
