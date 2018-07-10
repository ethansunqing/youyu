import requests
import sys
import io

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

#登录时需要POST的数据


postData = {
        'password':'CqINzImv602zC3PR8pkV7w==',
        'userName':'13701539116'
}




postData2 ={
    
        'Content-Length': '88',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': '47.104.185.138',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip'
          }


#设置请求头
headers =   {
            'wup_version': '3.0',
            'secureSessionId': '34922182069849729e9b1af689b9f0ef_0629_SZ',
            'strategylastUpdateTime': '1484104904000',
            'appVer': '1.00',
            'bundleId': 'com.yy.ch',
            'sdkVer': '2.6.6',
            'prodId': '1400018291',
            'cmd': '840',
            'platformId':'1',
            'A37': 'WIFI',
            'A38': 'WIFI',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G9550 Build/R16NW)',
            'Host': 'astat.bugly.qq.com:8011',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'Content-Length': '1088',



             }

#登录时表单提交到的地址（用开发者工具可以看到）

app_login_url = 'http://47.104.185.138/web/user/login'

json = requests.post(app_login_url,postData).json()
errorCode = json['error']
if errorCode == 0:
    appToken = json['data']['token']
    print(appToken)
    appDealListUrl = 'http://47.104.185.138/web/deal/list/top10?token='+appToken
    json = requests.post(appDealListUrl).json()
    errorCode = json['error']
    if errorCode == 0:
        print(json['data'])   
    else:
        print(json['msg'])
else:
    print(json['msg'])

# print(resp.content.decode('utf-8'))