#!/usr/bin/python3

import os, sys

# 打开文件
path = "F:\\python_script\\interface\\test_case"
dirs = os.listdir(path)

# 输出所有文件和文件夹
for file in dirs:
    print(file)
