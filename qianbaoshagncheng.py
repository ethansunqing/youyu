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
    'token':
    'se4p4jOkXIKvAgG4Jna7n7NegN9CL+Xl3LHT7IjVE5on/4QKIjCRbRSapVSPOtasq25GOgygGTY=',
    'good_id':
    '20'
}

postData1 = {
    'token':
    '4Bi4BGQJhiEF0bZDZAmdo7NegN9CL+Xl3LHT7IjVE5qUy2wluFyWfxSapVSPOtasq25GOgygGTY=',
    'good_id':
    '20'
}

postToken = {
    'token':
    'se4p4jOkXIKvAgG4Jna7n7NegN9CL+Xl3LHT7IjVE5on/4QKIjCRbRSapVSPOtasq25GOgygGTY='
}
# 4Bi4BGQJhiEF0bZDZAmdo7NegN9CL+Xl3LHT7IjVE5qUy2wluFyWfxSapVSPOtasq25GOgygGTY=
app_goodlist_url = 'http://47.104.185.138/web/good/list'
app_buy_url = 'http://47.104.185.138/web/good/buy'

# while True:

if __name__ == "__main__":
    while True:
        # json = requests.post(app_goodlist_url,postToken).json()['data']['data']
        # reqs = json[0]
        # id = reqs["id"]
        # storage = int(reqs["max"])
        # if storage == 0:
        #     print("我在等待上货")
        # else:
        order1 = requests.post(app_buy_url, postData).json()
        order2 = requests.post(app_buy_url, postData1).json()
        print(order2['msg'])
