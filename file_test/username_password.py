b = 13801111000
i = 0
# 生成10000条测试密码数据
# while i < 5000:
#     a = "INSERT INTO `user_secret` (`user_id`, `password`, `create_time`, `update_time`) VALUES ((select id from user u where u.mobile_phone='"
#     c = "'), 'E10ADC3949BA59ABBE56E057F20F883E', SYSDATE(), SYSDATE());"
#     sql_restult = a + str(b) + c
#     print(sql_restult)
#     b = int(b) + 1
#     # print(b)
#     i = i + 1

# 生成1000条测试帐号数据
# while i < 1000:
#     a = "INSERT INTO `user` (`user_name`, `nick_name`, `mobile_phone`, `image`, `email`, `im_way`, `join_status`, `user_level`, `type`, `create_time`, `update_time`, `status`) VALUES ("
#     c = ", NULL, "
#     d = ", NULL, NULL, NULL, '0', '0', '1', SYSDATE(), SYSDATE(), '0');"
#     sql_restult = a + '\'' + str(b) + '\'' + c + str(b) + d
#     print(sql_restult)
#     b = int(b) + 1
#     # print(b)
#     i = i + 1


# 参数化1000测试数据
while i < 100:
    print(str(b)+',', '123456')
    b = int(b) + 1
    i = i + 1
