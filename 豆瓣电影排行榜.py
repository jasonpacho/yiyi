# -*- codeing = utf-8 -*-
# @Time :2021/10/155:14
# @Author : Jason
# @File :豆瓣电影排行榜.py
# @Software:PyCharm
import re
import csv
import requests


url = 'https://movie.douban.com/top250?start='

header = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3877.400 QQBrowser/10.8.4506.400"
}
response = requests.get(url,headers=header)

page_content = response.text
#print(page_content)

#解析数据
ojb = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<age>.*?)&nbsp.*?<span '
                r'class="rating_num" property="v:average">(?P<rating>.*?)</span>.*?'
                 r'<span>(?P<pingjia>.*?人评价)</span>',re.S)
result = ojb.finditer(page_content)
f = open("data.csv",mode="w")
csvwriter = csv.writer(f)
for it in result:
    # print(it.group("name"))
    # print(it.group("rating"))
    # print(it.group("pingjia"))
    # print(it.group("age").strip())
    dic = it.groupdict()
    dic['age'] = dic['age'].strip()
    csvwriter.writerow(dic.values())
response.close()
print("over")

