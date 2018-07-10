import requests
import sys
import io
import time, datetime
import random
from threading import Thread
import threading
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

#登录时需要POST的数据
# 手机号17362448271
token = 'CS1vBi+0VUiNuqRdoMy+qIw9RokQ90Vo9eyDnVX6s6j/Xmuj7Fvx2hSapVSPOtasq25GOgygGTY='

postToken = {'token': token}
# postData = {
#         'token':token,
#         'b_id':'8514'
# }
startTime = datetime.datetime(2018, 7, 6, 11, 59, 30)
nowtime = datetime.datetime.now()
endTime = datetime.datetime(2018, 7, 10, 11, 1, 5)

#登录时表单提交到的地址（用开发者工具可以看到）
app_buy_url = 'http://47.104.185.138/web/belonging/buy'

app_good_url = 'http://47.104.185.138/web/belonging/get'


def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()

    return wrapper


def get_goods_ids():
    arr = requests.post(app_good_url, postToken).json()['data']['data']
    for i in range(len(arr)):
        reqs = arr[i]
        id = reqs["id"]
        # print(id)
        return id


def ping_postDate(id):

    postData = {'token': token, 'b_id': id}
    return postData


@async
def work():
    id = get_goods_ids()
    # print(id)
    buy(id)


def buy(id):
    resp = requests.post(app_buy_url, ping_postDate(id))
    print(resp.content.decode('utf-8'))


if __name__ == "__main__":
    while True:
        nowtime = datetime.datetime.now()
        if nowtime > startTime:
            work()
            # r=random.random()
            # print(r)
            # time.sleep(r)
            if nowtime > endTime:
                print("干完收工")
                break
        else:
            print("我在等待11点的到来")
            time.sleep(1)
