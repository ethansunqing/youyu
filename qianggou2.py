import requests
import sys
import io
import time, datetime
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

#登录时需要POST的数据

# 手机号18631599942
postData = {
        'token':'l2H/ZE0GOeGfiWujWnnBWoSl28h/w/TKpNeI62THHxngf+9cDBHP0MhhCkwG5o/PWkz2otk3lBE=',
        'b_id':'9136'
}

postData1 = {
        'token':'l2H/ZE0GOeGfiWujWnnBWoSl28h/w/TKpNeI62THHxngf+9cDBHP0MhhCkwG5o/PWkz2otk3lBE=',
        'b_id':'8640'
}
postData2 = {
        'token':'l2H/ZE0GOeGfiWujWnnBWoSl28h/w/TKpNeI62THHxngf+9cDBHP0MhhCkwG5o/PWkz2otk3lBE=',
        'b_id':'8639'
}

#登录时表单提交到的地址（用开发者工具可以看到）
while True:
        app_buy_url = 'http://47.104.185.138/web/belonging/buy'

        json = requests.post(app_buy_url,postData).json()
        json = requests.post(app_buy_url,postData1).json()
        json = requests.post(app_buy_url,postData2).json()
        print(json['msg']) 
