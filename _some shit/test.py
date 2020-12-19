import os
from datetime import datetime
import json

class Info:
    timestamp = 0
    ts: int

    def __init__(self):
        self.timestamp = int(datetime.now().timestamp())

    def __init__(self, timestamp):
        self.timestamp = timestamp

    @classmethod
    def hello(cls):
        print('Hello')    

    @staticmethod
    def world():
        print('World')

def example():
    path = os.getcwd()
    print(path)

    now = datetime.now()
    print(now)

    now_text = now.strftime('%Y-%m-%d %H-%M-%S')
    print(now_text)

    ts = now.timestamp()
    print(ts)
    print(int(ts))
    print(type(ts))

    print(datetime.fromtimestamp(int(ts)))

def write():
    info = Info()
    json_text = json.dumps(info.__dict__, indent = 4)
    print(json_text)
    print(info.__dict__)

    with open('file.txt', 'w') as f:
        f.write(json_text + '\n')

def read():
    Info.hello()
    Info.world()
    
    with open('file.txt', 'r') as f:
        json_text = json.loads(f.read())
        print(json_text)
        print(type(json_text))
        #1606673013
        info = Info(**json_text)
        print(info.timestamp)


read()
i = Info()
