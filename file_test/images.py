import requests
import json

# 获取所有人的图片
# filename = urllib3.urlretrieve(url)
# id = 1
# while id < 465:
#     images_name = "D:/images/" + str(id).zfill(10) + ".jpg"
#     print(images_name)
#     url = 'http://106.12.113.59:8088/photo/' + str(id).zfill(10) + '.jpg'
#     print(url)
#     sss = requests.get(url)
#     id = int(id) + 1
#     print(images_name)
#     with open(images_name, "wb")as f:
#         f.write(sss.content)


# 获取所有人照片，并将照片文件名字填写成部门+姓名.jpg
sss = requests.get("http://106.12.113.59:8088/sys/GetAllDepartUserTree").text
sss01 = json.loads(sss)
id = sss01["Data"]
print(type(id), id)
id01 = json.loads(id)
# print(type(id01), id01[0]["text"], id01[0]["children"][0]["id"])
for i in id01:
    # print(type(i), i["id"], i["text"], type(i["children"]), i["children"])
    t = i["children"]
    for y in t:
        # print(i["text"], y["id"], y["text"])
        s = str(i["text"]) + "_" + str(y["text"])
        url = 'http://106.12.113.59:8088/photo/' + str(y["id"]) + '.jpg'
        print(s, url)
        sss_result = requests.get(url)
        images_name = "D:/images01/" + s + ".jpg"
        with open(images_name, "wb")as f:
            f.write(sss_result.content)


