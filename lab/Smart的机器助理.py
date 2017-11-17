import requests
user = input("Enter user name:")
print("Smart的机器助理:你好,"+user+"!我是Smart的机器助理")
while True:
    s = input(user+":")
    resp = requests.post("http://www.tuling123.com/openapi/api", data={
        "key": "dfa21a126ed2468ca2b9f49d27d7356e",
        "info": s,
        "userid": user
    })
    resp = resp.json()
    print("Smart的机器助理:"+resp['text'])
