# -*- codeing = utf-8 -*-
# @Time :2021/10/169:03
# @Author : Jason
# @File :爬取猪八戒网.py
# @Software:PyCharm
import requests
from lxml import etree
url = "https://lyg.zbj.com/search/f/?kw=saas?type=new,saas"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
}
resp = requests.get(url,headers=header)

html = etree.HTML(resp.text)
# 拿到每一个服务商的DIV
divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div")
for div in divs:
    price = div.xpath("./div/div/a/div[2]/div[1]/span[1]/text()")[0]
    tiele1 = div.xpath("./div/div/a/div[2]/div[2]/p/text()")[0]
    cop_name = div.xpath("./div/div/a[1]/div[1]/p/text()")[1]
    n = div.xpath("./div/div/a[1]/div[1]/div/span/text()")[0]
    print(cop_name,tiele1,price,n)