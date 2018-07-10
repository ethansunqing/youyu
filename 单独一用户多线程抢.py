import requests
import sys
import io
import time, datetime
import random
from threading import Thread

# 专门抢3000以下的单子

#登录时需要POST的数据


def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start

    return wrapper


token = 'CS1vBi+0VUiNuqRdoMy+qIw9RokQ90Vo9eyDnVX6s6j/Xmuj7Fvx2hSapVSPOtasq25GOgygGTY='

postToken = {'token': token}
# postData = {
#         'token':token,
#         'b_id':'8514'
# }
startTime = datetime.datetime(2018, 7, 8, 10, 59, 30)
# nowtime=datetime.datetime.now()
endTime = datetime.datetime(2018, 7, 10, 11, 1, 5)

#登录时表单提交到的地址（用开发者工具可以看到）
app_buy_url = 'http://47.104.185.138/web/belonging/buy'

app_good_url = 'http://47.104.185.138/web/belonging/get'


def get_goods_ids():
    arr = requests.post(app_good_url, postToken).json()['data']['data']
    # print(arr)
    changdu = len(arr)
    id_list = []
    for i in range(changdu):
        item = {}
        reqs = arr[i]
        item['id'] = reqs["id"]
        item['price'] = reqs["current_price"]
        id_list.append(item)
        return id_list


def ping_postDate(id):
    postData = {'token': token, 'b_id': id}
    return postData


# @async
def work():
    for newid in get_goods_ids():
        id = newid['id']
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
            print("我在等待11:59:30的到来")
            time.sleep(1)
