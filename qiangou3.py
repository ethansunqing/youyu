import requests
import sys
import io

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

#登录时需要POST的数据


postData = {
        'token':'qPXv9/BsR7GTsxhHWsUWXUOFq8CvfDgrDERkehuumAGqT6WW1CuhCAqm++sNrM2J5o3FrZTdE1PnRLQxBmCuNw==',
        'b_id':'8880'
}
postData2 = {
        'token':'qPXv9/BsR7GTsxhHWsUWXUOFq8CvfDgrDERkehuumAGqT6WW1CuhCAqm++sNrM2J5o3FrZTdE1PnRLQxBmCuNw==',
        'b_id':'8873'
}
postData3 = {
        'token':'qPXv9/BsR7GTsxhHWsUWXUOFq8CvfDgrDERkehuumAGqT6WW1CuhCAqm++sNrM2J5o3FrZTdE1PnRLQxBmCuNw==',
        'b_id':'8573'
}

#登录时表单提交到的地址（用开发者工具可以看到）
app_buy_url = 'http://47.104.185.138/web/belonging/buy'

while True:

        json = requests.post(app_buy_url,postData).json()
        json = requests.post(app_buy_url,postData2).json()
        json = requests.post(app_buy_url,postData3).json()
        print(json['msg'])