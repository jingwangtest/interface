# coding=utf-8

import requests
import re
import chardet

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br'
}

url = "http://blog.csdn.net/d_pokemon?viewmode=list"

html = requests.get(url, headers=header)
html_decode = html.content.decode('UTF-8')
print(html.content)
print('结果： ', html.status_code)
# print('原因： ', html.reason)

text = "JGood is a handsome boy, he is cool, clever, and so on…"
regex = re.compile('link rel=".*?" href="https://.*?"', re.S)
# regex1 = re.compile('link rel=".*?"')
print(regex.findall(html_decode))  # 查找所有包含’oo’的单词
