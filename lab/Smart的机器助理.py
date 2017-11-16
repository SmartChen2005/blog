"""
用Python3运行此程序，即可与Smart的机器助理聊天！

more on www.chenhongyi.cc

"""
import requests

user_name = input("Enter your name:")
print("你好"+user_name+"，我是Smart的机器助理")
while 1:
    s = input()
    resp = requests.post("http://www.tuling123.com/openapi/api", data={
        "key": "dfa21a126ed2468ca2b9f49d27d7356e",
        "info": s,
        "userid": user_name
    })
    resp = resp.json()
    print("Smart的机器助理："+resp['text'])