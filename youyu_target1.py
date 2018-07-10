import requests
import sys
import io

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

#登录时需要POST的数据


postData = {
        'password':'CqINzImv602zC3PR8pkV7w==',
        'userName':'13701539116'
}

#设置请求头
headers = {
        'Content-Length': '98',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': '47.104.185.138',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip'
          }

#登录时表单提交到的地址（用开发者工具可以看到）

app_login_url = 'http://47.104.185.138/web/user/login'

json = requests.post(app_login_url,postData).json()
errorCode = json['error']
if errorCode == 0:
    appToken = json['data']['token']
    appDealListUrl = 'http://47.104.185.138/web/deal/list/top10?token='+appToken
    json = requests.get(appDealListUrl).json()
    errorCode = json['error']
    if errorCode == 0:
        print(json['data'])   
    else:
        print(json['msg'])
else:
    print(json['msg'])

# print(resp.content.decode('utf-8'))

