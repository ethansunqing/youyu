import requests
import sys
import io
import threading
import time, datetime
import random
from threading import Thread

# 专门抢3000以下的单子


#登录时需要POST的数据
# 手机号17362448271
class qiangdan():
    def __init__(self):
        self.tokens = [
            '79LUwKTpgo544HluPr1FtDZQfxH4RFXvDQsI7E13H0KHTV7wc2BVp/9XDMFSLU25Wkz2otk3lBE=',
            'l2H/ZE0GOeGfiWujWnnBWjZQfxH4RFXvDQsI7E13H0LqKuhm8Vn3y91wyQ/xToUvWkz2otk3lBE=',
            'X6xnQE5Q/kcPk/kasFQS0TZQfxH4RFXvDQsI7E13H0LBHL9HlfaLwef+rTIhrm9zWkz2otk3lBE=',
            'Qan0NT+mGktIFRMlbORMpTZQfxH4RFXvDQsI7E13H0IDalsl2KVNv9bAwM4UP7cQWkz2otk3lBE=',
            'se4p4jOkXIKvAgG4Jna7n9CNYOF2LiAO9eyDnVX6s6jW/fZ8DWC9BBSapVSPOtasq25GOgygGTY=',
            'GVDQ3gPDZcMw1naYSkOE0NCNYOF2LiAO9eyDnVX6s6gBWORIXIn63hSapVSPOtasq25GOgygGTY=',
            'gIKp851wbsSlx35qx9YwLlgQeo+rUV2F9eyDnVX6s6ipOfQ7nx4/+RSapVSPOtasq25GOgygGTY=',
            'oCPnUHZx8TTb8DfHHRAc+KG9lUyXU/8E9eyDnVX6s6gX3rCNOmFDJhSapVSPOtasq25GOgygGTY=',
            '19nWvoFpUk2KsPQ/NMSyCOZPPtZfEN3M9eyDnVX6s6hjcIWrd/vYhhSapVSPOtasq25GOgygGTY=',
            'OOpStmG5g77oyeTbEquZ6+H41cJqynZK8026izio/NrvCr+LlIl152o3TDu+zm9KohGbzIMnN78=',
            '45oJ3bmBQgf0ZKRG3hnkZOH41cJqynZK8026izio/NpxhBHa/ZTs+Go3TDu+zm9KohGbzIMnN78=',
            'RjPrewlh264SVCJagWZ5PlrB8MqaFDi4f2gJajPwYyl+Y1yOowNi9I1O5P2Ae4oXWkz2otk3lBE='
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


if __name__ == "__main__":
    while True:
        try:
            i = 0
            # 开启线程数目
            tasks_number = 12
            time1 = time.clock()
            while i < tasks_number:
                t = threading.Thread(target=work)
                t.start()
                i += 1
            # print(times/tasks_number)
        except Exception as e:
            print(e)
