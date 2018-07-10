import requests
import sys
import io
import time, datetime
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

#登录时需要POST的数据

# startTime = datetime.datetime(2018, 7, 3, 10, 58, 0)
# endTime = datetime.datetime(2018, 7, 3, 11, 2, 0)
startTime = datetime.datetime(2018, 7, 3, 14, 23, 40)
endTime = datetime.datetime(2018, 7, 5, 22, 23,41)
postData = {
        'token':'l2H/ZE0GOeGfiWujWnnBWg+Y02o/uDhEltqlJ/Xn28Uf05I0hrWI9/B3fwqwnAItWkz2otk3lBE=',
        'good_id':'20'
}
postToken={'token':'l2H/ZE0GOeGfiWujWnnBWg+Y02o/uDhEltqlJ/Xn28Uf05I0hrWI9/B3fwqwnAItWkz2otk3lBE='}

app_goodlist_url='http://47.104.185.138/web/good/list'
app_buy_url = 'http://47.104.185.138/web/good/buy'

# while True:

 
if __name__=="__main__":
    while True:
        nowtime = datetime.datetime.now()
        if nowtime > startTime:
            json = requests.post(app_goodlist_url,postToken).json()['data']['data']
            reqs = json[0]
            id = reqs["id"]
            storage = int(reqs["max"])
            if storage == 0:
                print("我在等待上货")
                time.sleep(1) 
            else:
                order = requests.post(app_buy_url,postData).json()
                print(order['msg'])  
                
            # r=random.random()
            # print(r)
            # time.sleep(r)
            # if nowtime>endTime:
            #     print("干完收工")
            #     break
            # else:
            #     print("我在等待上货")
            #     time.sleep(1)   