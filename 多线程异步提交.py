#coding=utf8
'''
random.randint(a, b):用于生成一个指定范围内的整数。
其中参数a是下限，参数b是上限，生成的随机数n: a &lt;= n &lt;= b
random.choice(sequence)：从序列中获取一个随机元素
参数sequence表示一个有序类型（列表，元组，字符串）
'''
# import httplib,json
import requests
import json
import time
import threading
from random import randint, choice


#创建请求函数
def postRequest(threadNum):

    postJson = {
        'token':
        '4Bi4BGQJhiEF0bZDZAmdo88gZSo5q18fzsU0BllzFzErIsT96ibqxRSapVSPOtasq25GOgygGTY=',
        'good_id':
        '20'
    }

    #定义一些文件头
    # headerdata = {

    #     "content-type":"application/json",
    #      }

    #请求服务,例如：www.baidu.com
    hostServer = "http://47.104.185.138/web/good/buy"
    #发送请求

    #获取请求响应
    response = requests.post(hostServer, postJson)
    #打印请求状态
    if response.status_code in range(200, 300):
        print(u"线程" + str(threadNum) + u"状态码：" + str(response.status_code))


def run(threadNum, internTime, duration):
    #创建数组存放线程
    threads = []
    try:
        #创建线程
        for i in range(1, threadNum):
            #针对函数创建线程
            t = threading.Thread(target=postRequest, args=(i, ))
            #把创建的线程加入线程组
            threads.append(t)
    except Exception as e:
        print(e)

    try:
        #启动线程
        for thread in threads:
            thread.setDaemon(True)
            thread.start()
            time.sleep(internTime)

        #等待所有线程结束
        for thread in threads:
            thread.join(duration)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    startime = time.strftime("%Y%m%d%H%M%S")

    now = time.strftime("%Y%m%d%H%M%S")
    duratiion = input(u"输入持续运行时间:")
    while (startime + str(duratiion)) != now:
        run(100, 0, int(duratiion))
        now = time.strftime("%Y%m%d%H%M%S")
