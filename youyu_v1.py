import requests
import sys
import io
import time, datetime
import random
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

#登录时需要POST的数据
# 手机号17362448271
token = 'X6xnQE5Q/kcPk/kasFQS0VV6+gbzh5YdLfRBYAfqxh5oDmA0hT7vkseYOpRS4IJJWkz2otk3lBE='


postToken ={'token':token}
# postData = {
#         'token':token,
#         'b_id':'8514'
# }
startTime = datetime.datetime(2018, 7, 6, 11, 59, 30)
nowtime=datetime.datetime.now()
endTime = datetime.datetime(2018, 7, 8, 11, 32, 5)


#登录时表单提交到的地址（用开发者工具可以看到）
app_buy_url = 'http://47.104.185.138/web/belonging/buy'

app_good_url='http://47.104.185.138/web/belonging/get'
def get_goods_ids():   
    arr=requests.post(app_good_url,postToken).json()['data']['data']
    for i in range(len(arr)):
        reqs= arr[i]
        id=reqs["id"]
        # print(id)
        return id



def ping_postDate(id):
    
    postData = {
        'token':token,
        'b_id':id
        }
    return postData

def work():
    id = get_goods_ids()
    print(id)
    buy(id)
    
  

def buy(id):
    resp=requests.post(app_buy_url,ping_postDate(id))
    print(resp.content.decode('utf-8'))

# while True:
# for i in range(1,10):
# if nowtime == endTime:
    
# else:
#     test()
#     time.sleep(2)


# arr=get_goods_ids()
# id = arr.json()['id']
# for i in range(10):
#     print(arr1[i])

# arr=get_goods_ids()
# for i in range(len(arr)):
#     reqs= arr[i]
#     # id = arr[i].json().['id']
#     # print(reqs)
#     id=reqs["id"]
#     print(id)


    # print ("序号：%s   值：%s" % (i + 1, arr1[i]))

# if a>b:
#     return True
# else:
#     return False



if __name__=="__main__":
    while True:
        nowtime=datetime.datetime.now()
        if nowtime > startTime:
            work()
            # r=random.random()
            # print(r)
            # time.sleep(r)
            if nowtime>endTime:
                print("干完收工")
                break
        else:
            print("我在等待11点的到来")
            time.sleep(1)

