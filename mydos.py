import threading
import socket
import requests

url = 'https://www.baidu.com'

port = ''

method = 'get/post'

headers = {'user-agent': 'my-app/0.0.1'}

payload = {'key1': 'value1', 'key2': 'value2'}

request_counter = 0

thread_counter = 0

n = 5



def SendGet(url):
    global request_counter,headers
    try:
        request = requests.get(url,headers=headers,timeout=1)
        # print(request.status_code)
        if request.status_code == 200:
            request_counter+=1
            print('%s 次get请求成功'%request_counter)
            # SendGet(url)
            print(request.headers)
        else:
            print('第%s次请求失败'%request_counter)

    except:
        pass


def SendPost(url):
    global request_counter,payload
    try:
        request = requests.post(url,data=payload,timeout=1)
        request_counter+=1
        print('%s 次post请求成功'%request_counter)
        SendPost(url)
    except:
        pass
class SendGetThreading(threading.Thread):
    def run(self):
        try:
            while True:
                global url
                SendGet(url)
        except:
            pass
class SendPostThreading(threading.Thread):
    def run(self):
        try:
            while True:
                global url
                SendPost(url)
        except:
            pass

if __name__ == '__main__':
    for i in range(n):
        mygetdos = SendGetThreading()
        mygetdos.start()
        mypostdos = SendPostThreading()
        mypostdos.start()


