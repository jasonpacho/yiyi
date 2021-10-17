# -*- codeing = utf-8 -*-
# @Time :2021/10/1613:39
# @Author : Jason
# @File :爬取梨视频.py
# @Software:PyCharm
import requests


url = "https://www.pearvideo.com/video_1743818"
contId = url.split("_")[1]
# contId=1743760
viderStatus = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.34082064386360433"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47",
    #  防盗链: 溯源，查找当前本次请求的上一级
    "Referer": url
}
response = requests.get(viderStatus,headers=headers)
#print(response.text)
dic = response.json()
srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']

srcUrl = srcUrl.replace(systemTime,f"cont-{contId}")
#print(srcUrl)
with open("B.mp4",mode = "wb")as f:
    f.write(requests.get(srcUrl).content)

# "https://video.pearvideo.com/mp4/third/20211015/1634369891913-11549967-154727-hd.mp4
#https://video.pearvideo.com/mp4/third/20211015/cont-1743818-11549967-154727-hd.mp4