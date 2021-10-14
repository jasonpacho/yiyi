# -*- codeing = utf-8 -*-
# @Time :2021/10/1412:28
# @Author : Jason
# @File :有道翻译.py
# @Software:PyCharm
import requests


def youdaoTranslate(value, count):
    if value == '':
        print('输入内容为空@_@')
        return False
    else:
        # Request URL
        responseURL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        # 待提交准备Post给url的Data:定义为dict
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3877.400 QQBrowser/10.8.4506.400"
        }
        form_Data = {}
        form_Data['i'] = value
        form_Data['from'] = 'AUTO'
        form_Data['to'] = 'AUTO'
        form_Data['smartresult'] = 'dict'
        form_Data['client'] = 'fanyideskweb'
        form_Data['doctype'] = 'json'
        form_Data['version'] = '2.1'
        form_Data['keyfrom'] = 'fanyi.web'
        form_Data['action'] = 'FY_BY_REALTIME'
        form_Data['typoResult'] = 'false'
        # 使用urlencode方法转换标准格式　
        r = requests.post(responseURL, data=form_Data,headers=headers)
        result = r.json()
        # 使用JSON
        # 找到翻译结果
        # 这里推荐一个格式化JSON的好工具：https://c.runoob.com/front-end/53
        translate_result_main = result['translateResult'][0][0]['tgt']
        # 打印翻译结果
        print(f'{count}. {translate_result_main}\n\n')
        return True


if __name__ == '__main__':
    try:
        count = 1
        while True:
            print('-' * 26)
            word = input('请输入待翻译的单词或句子:\n').strip()
            if youdaoTranslate(word, count) == True:
                count += 1
    except KeyboardInterrupt:
        print('\a手动退出!欢迎再来')

