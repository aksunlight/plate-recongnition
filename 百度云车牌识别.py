# coding=utf-8
import base64
import requests

# client_id为官网获取的AK，client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=FwUMziTC7FGKLxHcwyDfGWhE&client_secret=UUd4GbeSjBzvv68rIWnlOsMK9LHfXlGG'
response = requests.get(host)
access_token = response.json()['access_token']

'''
车牌识别
'''
# 二进制方式打开图片文件
f = open('12.png', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate"
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)

if response:
    result = response.json()
    with open('识别结果.txt', 'a', encoding='utf-8') as fp:
        fp.write('图片：' + f.name + '\n')
        fp.write('车牌号：' + result['words_result']['number'] + '  ' + '车牌颜色：' + result['words_result']['color'] + '\n')
        fp.write('百度智能云车牌识别：' + str(result) + '\n\n')
        print(result, type(result))
