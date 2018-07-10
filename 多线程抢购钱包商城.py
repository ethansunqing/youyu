# -*- coding: utf-8 -*-
import requests
import threading
import time
from threading import Thread


class postrequests():
    def __init__(self):
        self.url = 'http://47.104.185.138/web/good/buy'
        self.postData = {
            'token':
            'l2H/ZE0GOeGfiWujWnnBWjZQfxH4RFXvDQsI7E13H0LqKuhm8Vn3y91wyQ/xToUvWkz2otk3lBE=',
            'good_id':
            '20'
        }

    def post(self):
        try:
            r = requests.post(self.url, self.postData)
            print(r.text)
        except Exception as e:
            print(e)


def login():
    login = postrequests()
    return login.post()
    # if __name__ == '__main__':
    #     login()


try:
    i = 0
    # 开启线程数目
    tasks_number = 150
    # print('测试启动')
    time1 = time.clock()
    while i < tasks_number:
        t = threading.Thread(target=login)
        t.start()
    #     i +=1
    # time2 = time.clock()
    # times = time2 - time1
    # print(times)
    # print(times/tasks_number)
except Exception as e:
    print(e)
