# -*- coding: utf-8 -*-
import xlrd
import unittest
import requests
import json
import interface.readConfig as readConfig

localReadConfig = readConfig.ReadConfig()


class read(unittest.TestCase):
    def get_sheet1(self):
        # 打开文件
        workbook = xlrd.open_workbook(r'F:\file_excel\sample.xlsx')
        # 根据sheet索引或者名称获取sheet内容
        sheet1 = workbook.sheet_by_name('Sheet1')
        return

        # sheet的名称，行数，列数
        max_nrows_num = sheet1.nrows
        max_ncols_num = sheet1.ncols
        print(sheet1.name, max_ncols_num, max_nrows_num)

        # 获取整行和整列的值（数组）
        num_rows = sheet1.row_values(0)  # 获取第四行内容
        cols = sheet1.col_values(2)  # 获取第三列内容
        # print(num_rows)
        # print(cols)

        # 获取单元格内容
        # print(sheet1.cell(2, 2).value)
        # print(sheet1.cell_value(2, 0).encode('utf-8'))
        # print(sheet1.row(4)[0].value.encode('utf-8'))

        # 获取单元格内容的数据类型(ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error)
        # print(sheet1.cell(2, 2).ctype)
        # 获取总行数据
        nrows = sheet2.nrows
        print(nrows)
        for i in range(nrows):
            # print(sheet1.row_values(i))
            if i == 0:
                continue
            a = int(sheet2.row_values(i)[0])
            b = int(sheet2.row_values(i)[1])
            print(type(a), type(b))
            params = {'mobilePhone': a, 'password': b, 'remember': 'true', 'siteName': 'main'}
            url = localReadConfig.get_http('url')

            headers = {
                'Content-Type': 'application/json;charset=UTF-8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0',
                'Accept - Encoding': 'gzip, deflate',
                'Accept - Language': 'zh - CN, zh;q = 0.9',
                'Referer': 'http://www1.ejw.cn/auth/?backUrl=http%3A%2F%2Fadmin.ejw.cn%2F%23%2F',
                'X-Requested-With': 'XMLHttpRequest'
            }
            print(headers)
            # r1 = requests.post(url, data=json.dumps(params), headers=headers).text
            # print('新增成功')
            token_act = requests.post(url, data=json.dumps(params), headers=headers)
            print(token_act)
            s = json.loads(token_act.text)
            print("登陆成功")


if __name__ == '__main__':
    unittest.main()
