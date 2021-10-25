# -*- codeing = utf-8 -*-
# @Time :2021/10/2311:57
# @Author : Jason
# @File :豆瓣.py
# @Software:PyCharm
import requests
from lxml import etree

url = 'https://movie.douban.com/top250?start='
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
}
resp = requests.get(url=url,headers=header).text
tree = etree.HTML(resp)
li_list = tree.xpath('//*[@id="content"]/div/div[1]/ol/li')
for li in li_list:
    #电影名
    title_list = li.xpath('./div/div[2]/div/a/span[1]/text()')[0]
    #转换位字符串
    title = "".join(title_list)

    #电影的别名
    other_title = li.xpath('./div/div[2]/div/a/span[3]/text()')
    # 这里是将获取到的列表转换成字符串
    other_title = "".join(other_title)
    # 因为是字符串使用可以使用split方法进行提取
    other = "".join(other_title.split())

    #导演及主演
    bd_list = li.xpath('./div/div[2]/div[2]/p/text()')
    #将返回的列表转换成字符串
    bd = "".join(bd_list)
    #因为字符串里的空格太多，所以使用split
    bd = " ".join(bd.split())

    # 电影的导语
    quote_list = li.xpath('./div/div[2]/div[2]/p[2]/span/text()')
    quote = "".join(quote_list)

    # 电影评分
    rating_list = li.xpath('./div/div[2]/div[2]/div/span[2]/text()')
    rating = "".join(rating_list)
    rating = "评分: "+rating
    #多少人评价
    proper_list = li.xpath('./div/div[2]/div[2]/div/span[4]/text()')
    proper = "".join(proper_list)
    list = title+other+bd+quote+rating+proper


print("完成")