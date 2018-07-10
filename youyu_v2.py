import requests
import sys
import io
import threading
import time, datetime
import random
from threading import Thread

# 专门抢3000以下的单子

#登录时需要POST的数据

tokens = [
    '79LUwKTpgo544HluPr1FtDZQfxH4RFXvDQsI7E13H0KHTV7wc2BVp/9XDMFSLU25Wkz2otk3lBE=',
    'l2H/ZE0GOeGfiWujWnnBWjZQfxH4RFXvDQsI7E13H0LqKuhm8Vn3y91wyQ/xToUvWkz2otk3lBE=',
    'X6xnQE5Q/kcPk/kasFQS0TZQfxH4RFXvDQsI7E13H0LBHL9HlfaLwef+rTIhrm9zWkz2otk3lBE=',
    'Qan0NT+mGktIFRMlbORMpTZQfxH4RFXvDQsI7E13H0IDalsl2KVNv9bAwM4UP7cQWkz2otk3lBE='
]

postToken = {'token': tokens[0]}
# postData = {
#         'token':token,
#         'b_id':'8514'
# }
startTime = datetime.datetime(2018, 7, 9, 14, 47, 0)
nowtime = datetime.datetime.now()
endTime = datetime.datetime(2018, 7, 9, 14, 47, 2)

#登录时表单提交到的地址（用开发者工具可以看到）
app_buy_url = 'http://47.104.185.138/web/belonging/buy'

app_good_url = 'http://47.104.185.138/web/belonging/get'


def get_goods_ids():
    # print(postToken)
    arr = requests.post(app_good_url, postToken).json()['data']['data']
    changdu = len(arr)
    id_list = []
    for i in range(changdu):
        item = {}
        reqs = arr[i]
        item['id'] = reqs["id"]
        item['price'] = reqs["current_price"]
        if int(item['price']) < 8000:
            id_list.append(item)
            # print(id_list)
            return id_list


def work():
    for newid in get_goods_ids():
        id = newid['id']
        for token in tokens:
            postData = {'token': token.title(), 'b_id': id}
            resp = requests.post(app_buy_url, postData)
            # print("token: %s ,id is %s" % (token.title(), id))
            print(resp.content.decode('utf-8'))


if __name__ == "__main__":
    while True:
        nowtime = datetime.datetime.now()
        if nowtime > startTime:
            try:
                i = 0
                tasks_number = 5
                while i < tasks_number:
                    t = threading.Thread(target=work)
                    t.start()
                    i += 1
            except Exception as e:
                print(e)
            # if nowtime > endTime:
            #     print("干完收工")
            #     break
        else:
            print("我在等待11点的到来")
            time.sleep(1)
