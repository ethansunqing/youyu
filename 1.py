import requests
import sys
import io
import time, datetime
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

#登录时需要POST的数据

# startTime = datetime.datetime(2018, 7, 3, 10, 58, 0)
# endTime = datetime.datetime(2018, 7, 3, 11, 2, 0)
startTime = datetime.datetime(2018, 7, 3, 14, 23, 40)

postData = {
        'token':'se4p4jOkXIKvAgG4Jna7n7NegN9CL+Xl3LHT7IjVE5qZ53gSkDxVnhSapVSPOtasq25GOgygGTY=',
        'good_id':'20'
}
postToken={'token':'se4p4jOkXIKvAgG4Jna7n7NegN9CL+Xl3LHT7IjVE5qZ53gSkDxVnhSapVSPOtasq25GOgygGTY='}

app_goodlist_url='http://47.104.185.138/web/good/list'
app_buy_url = 'http://47.104.185.138/web/good/buy'

# while True:
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
 
if __name__=="__main__":
#     while True:        
                order = requests.post(app_buy_url,postData,headers=headers).json()
                print(order['msg'])  
                