import requests
import sys
import io
import time, datetime
import random
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

#登录时需要POST的数据

# startTime = datetime.datetime(2018, 7, 3, 10, 58, 0)
# endTime = datetime.datetime(2018, 7, 6, 11, 2, 0)
startTime = datetime.datetime(2018, 7, 5, 10, 59, 0)
endTime = datetime.datetime(2018, 7, 5, 11, 1,1)


# 15373512211号码
postData = {
        'token':'khefLzHW2h6ulE7dVu8hIsce2KCaYgN3jmEQ6iWjiBSqXRwUZBU7CBSapVSPOtasq25GOgygGTY=',
        'b_id':'9121'
}
postData2 = {
        'token':'khefLzHW2h6ulE7dVu8hIsce2KCaYgN3jmEQ6iWjiBSqXRwUZBU7CBSapVSPOtasq25GOgygGTY=',
        'b_id':'9140'
}
postData3 = {
        'token':'khefLzHW2h6ulE7dVu8hIsce2KCaYgN3jmEQ6iWjiBSqXRwUZBU7CBSapVSPOtasq25GOgygGTY=',
        'b_id':'9135'
}

#登录时表单提交到的地址（用开发者工具可以看到）
app_buy_url = 'http://47.104.185.138/web/belonging/buy'

# while True:

 
if __name__=="__main__":
    while True:
        nowtime=datetime.datetime.now()
        if nowtime > startTime:
            json = requests.post(app_buy_url,postData).json()
            json = requests.post(app_buy_url,postData3).json()
            json = requests.post(app_buy_url,postData2).json()
            print(json['msg'])  
            # r=random.random()
            # print(r)
            # time.sleep(r)
            if nowtime>endTime:
                print("干完收工")
                break
        else:
            print("我在等待10:59:30的到来")
            r=random.random()
            time.sleep(r)