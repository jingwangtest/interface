# coding=utf-8

from comm.public_data import MySQL

conn_partner = MySQL().connect_os1('conn')
cur1 = conn_partner.cursor()
cur1.execute('select partner_name from partner where partner_type = 0010')
par_result = list(cur1.fetchall())
for i in par_result:
    t = str(i).split(',', 2)[0].split('\'', 2)[1]
    # print(t)
    if "中国石化集团有限责任公司（供应商" == str(t):
        break
    else:
        print('继续执行')

