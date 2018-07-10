import requests
import sys
import io
import time, datetime
import random
# 专门抢3000以下的单子

#登录时需要POST的数据

token = 'qPXv9/BsR7GTsxhHWsUWXUOFq8CvfDgr8fwSSLy8n4kBYWZ/AA7+TrAozWrFgp465o3FrZTdE1Pn\nRLQxBmCuNw=='

postToken = {'token': token}
# postData = {
#         'token':token,
#         'b_id':'8514'
# }
startTime = datetime.datetime(2018, 7, 8, 10, 29, 0)
# nowtime=datetime.datetime.now()
endTime = datetime.datetime(2018, 7, 10, 11, 1, 5)

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
        item['id'] = reqs["id"]
        item['price'] = reqs["current_price"]
        if int(item['price']) < 10000:
            #
            id_list.append(item)

            return print(id_list)


# 参考代码 把id 和价格拿出来 组个 列表
# friends_list = []

#     for friend in friends:
#         item = {}
#         item['NickName'] = friend['NickName']
#         item['HeadImgUrl'] = friend['HeadImgUrl']
#         item['Sex'] = sex_dict[str(friend['Sex'])]
#         item['Province'] = friend['Province']
#         item['Signature'] = friend['Signature']
#         item['UserName'] = friend['UserName']

#         friends_list.append(item)
#print(item)


def ping_postDate(id):

    postData = {'token': token, 'b_id': id}
    return postData


def work():
    print(get_goods_ids())
    # for newid in get_goods_ids():
    #     id = newid['id']
    #     buy(id)


def buy(id):
    resp = requests.post(app_buy_url, ping_postDate(id))
    print(resp.content.decode('utf-8'))


work()
# if __name__ == "__main__":
#     while True:
#         nowtime = datetime.datetime.now()
#         if nowtime > startTime:
#             work()
#             # r=random.random()
#             # print(r)
#             # time.sleep(r)
#             if nowtime > endTime:
#                 print("干完收工")
#                 break
#         else:
#             print("我在等待11:59的到来")
#             time.sleep(1)
