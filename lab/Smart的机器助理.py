"""
��Python3���д˳��򣬼�����Smart�Ļ����������죡

more on www.chenhongyi.cc

"""
import requests

user_name = input("Enter your name:")
print("���"+user_name+"������Smart�Ļ�������")
while 1:
    s = input()
    resp = requests.post("http://www.tuling123.com/openapi/api", data={
        "key": "dfa21a126ed2468ca2b9f49d27d7356e",
        "info": s,
        "userid": user_name
    })
    resp = resp.json()
    print("Smart�Ļ�������"+resp['text'])