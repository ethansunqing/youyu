import requests
import sys
import io
import threading
import time, datetime
import random
from threading import Thread
import multiprocessing

# 专门抢3000以下的单子


#登录时需要POST的数据
# 手机号17362448271
class qiangdan():
    def __init__(self):
        self.tokens = [
            'Qan0NT+mGktIFRMlbORMpTZQfxH4RFXvDQsI7E13H0IDalsl2KVNv9bAwM4UP7cQWkz2otk3lBE='
        ]

        self.postToken = {'token': self.tokens[0]}

        self.app_buy_url = 'http://47.104.185.138/web/belonging/buy'

        self.app_good_url = 'http://47.104.185.138/web/belonging/get'

    def get_goods_ids(self):
        arr = requests.post(self.app_good_url,
                            self.postToken).json()['data']['data']
        changdu = len(arr)
        id_list = []
        for i in range(changdu):
            item = {}
            reqs = arr[i]
            item['id'] = reqs["id"]
            item['price'] = reqs["current_price"]
            if int(item['price']) < 4000:
                id_list.append(item)
                return id_list

    def xiadan(self):
        for newid in self.get_goods_ids():
            id = newid['id']
            for token in self.tokens:
                postData = {'token': token.title(), 'b_id': id}
                resp = requests.post(self.app_buy_url, postData)
                print(resp.content.decode('utf-8'))


startTime = datetime.datetime(2018, 7, 8, 10, 59, 30)
nowtime = datetime.datetime.now()
endTime = datetime.datetime(2018, 7, 10, 11, 0, 5)


def work():
    work = qiangdan()
    return work.xiadan()


tokens = [
    'se4p4jOkXIKvAgG4Jna7n9CNYOF2LiAO9eyDnVX6s6jW/fZ8DWC9BBSapVSPOtasq25GOgygGTY=',
    'GVDQ3gPDZcMw1naYSkOE0NCNYOF2LiAO9eyDnVX6s6gBWORIXIn63hSapVSPOtasq25GOgygGTY=',
    'gIKp851wbsSlx35qx9YwLlgQeo+rUV2F9eyDnVX6s6ipOfQ7nx4/+RSapVSPOtasq25GOgygGTY=',
    'oCPnUHZx8TTb8DfHHRAc+KG9lUyXU/8E9eyDnVX6s6gX3rCNOmFDJhSapVSPOtasq25GOgygGTY='
]

if __name__ == "__main__":
    while True:
        pool = multiprocessing.Pool(processes=4)
        for i in range(10):
            msg = "hello %d" % (i)
            pool.apply_async(work, (msg, ))
        pool.close()
        pool.join()
        print("Sub-process(es) done.")
