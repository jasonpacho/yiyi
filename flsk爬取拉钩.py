# -*- codeing = utf-8 -*-
# @Time :2021/10/2210:52
# @Author : Jason
# @File :flsk爬取拉钩.py
# @Software:PyCharm
from selenium.webdriver import Chrome
import time #导入时间，防止方位过快
# 导入键盘模块，
from selenium.webdriver.common.keys import Keys
web = Chrome() #创建一个浏览器
# 指定一个网站
web.get("https://www.lagou.com")
# 进入页面，找到叉子，然后使用click来点击
web.find_element_by_xpath('//*[@id="cboxClose"]').click()
time.sleep(1) #点击完休息1秒
#找到搜索框并输入查找的python，然后使用键盘模块，enter
web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python',Keys.ENTER)
n = 1
alst = web.find_elements_by_class_name('position_link')
for a in alst:
    #找到h3标签并点击
    a.find_element_by_tag_name('h3').click()
    # 窗口的转换
    web.switch_to.window(web.window_handles[-1]) # 跳转到第一个窗口
    # 拿到招聘信息
    text = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]').text
    # 将信息保存到文件中
    f = open("abc/需求_%s.txt" % n,mode="w")
    f.write(text)
    f.close()
    # 关闭窗口
    web.close()
    #调整窗口到最开始的页面
    web.switch_to.window(web.window_handles[0])
    time.sleep(1)
    n +=1

