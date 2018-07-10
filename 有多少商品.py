import requests
import sys
import io
import time, datetime
import random
import json
# 专门抢3000以下的单子

#登录时需要POST的数据

token = 'khefLzHW2h6ulE7dVu8hIjYCG8DIm2S89eyDnVX6s6hXue+jZKMfShSapVSPOtasq25GOgygGTY='

postToken = {'token': token}

#登录时表单提交到的地址（用开发者工具可以看到）
app_buy_url = 'http://47.104.185.138/web/belonging/buy'

app_good_url = 'http://47.104.185.138/web/belonging/get'


def get_goods_ids():
    arr = requests.post(app_good_url, postToken).json()['data']['data']
    changdu = len(arr)
    id_list = []
    for i in range(changdu):
        item = {}
        reqs = arr[i]
        # print(reqs)
        item['id'] = reqs["id"]
        item['price'] = reqs["current_price"]
        id_list.append(item)
    return id_list


# 把获取到的id_list组合去重
def get_goods_id_saixuan():
    id_lists = []
    for i in range(10):
        id_list = get_goods_ids()
        id_lists += id_list
    news_ids = []
    for id in id_lists:
        if id not in news_ids:
            news_ids.append(id)
    return print(news_ids)


get_goods_id_saixuan()


def ping_postDate(id):

    postData = {'token': token, 'b_id': id}
    return postData


#     changdu = len(arr)
# id_list = []
# for i in range(changdu):
#     item = {}
#     reqs = arr[i]
#     item['id'] = reqs["id"]
#     item['price'] = reqs["current_price"]
#     if int(item['price']) < 3000:
#         #

#         id_list.append(item)
#         return id_list

#     news_ids = []

# for newid in news_ids:
#     id = newid['id']
#     resp = requests.post(app_buy_url, ping_postDate(id))
#     print(resp.content.decode('utf-8'))
