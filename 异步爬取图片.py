# -*- codeing = utf-8 -*-
# @Time :2021/10/2515:42
# @Author : Jason
# @File :异步爬取图片.py
# @Software:PyCharm
import asyncio
import aiohttp
import requests
urls = [
    "https://kr.rcycsc.com/file/2021/0331/984a1a13158336a8d771bc0a3e672aec.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/0818/7f3219875a2c0ccbbf0856bf45a404c8.jpg",
    "http://i1.shaodiyejin.com/uploads/tu/201911/9999/ca99e50f14.jpg",
]

async def aiodownload(url):
    name = url.rsplit("/",1)[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            with open(name,mode="wb") as f:
                f.write(await resp.content.read())



async def main():
    tasks = []
    for url in urls:
        tasks.append(aiodownload(url))
    await asyncio.wait(tasks)




if __name__ =="__main__":
    asyncio.run(main())