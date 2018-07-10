import requests
import re

import time, datetime

# 头部信息
headers = {
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

# 登陆方法
def login(url):
    # response = requests.get(url,headers=headers)
    response = requests.post(url,headers)
    return print(response.content.decode('utf-8'))


# 第一次访问获取csrf值
'''
def get_login_web(url):
    r_session  = requests.Session()
    page = r_session.get('http://localhost/login')
    reg = r'<meta name="csrf-token" content="(.+)">'
    csrf = re.findall(reg,page.content)[0]


    login_page = login(url,csrf,r_session)
    print(login_page)
'''

if __name__ == "__main__":
    url = "http://47.104.185.138/web/deal/list/top10?token=khefLzHW2h6ulE7dVu8hIsYGx7UZQqX+mc6PcW+nYKhlX8GnbQ9y1RSapVSPOtasq25GOgygGTY="
    # url='https://api.imjad.cn/cloudmusic/?type=song&id=12037229'
    
    startTime = datetime.datetime(2018, 6, 29, 16, 10, 0)
    nowtime=datetime.datetime.now()
    # print('Program not starting yet...')
    while True:
        # for i in range(1,10):
            login(url)
            time.sleep(2)
    print('Program now starts on %s' % nowtime)
    print('Executing...')
    True