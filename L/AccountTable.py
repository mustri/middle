from L.Account import Account
from pymongo import MongoClient
PORT = 27017

class AccountTable():
    def __init__(self):
        pass

    def exist(self, a):
        k = a['username']
        client = MongoClient('localhost', PORT)
        db = client.station_database
        cursor = db['account_collections']
        if cursor.find_one({'username': k}) == None:
            client.close()
            return False
        else:
            client.close()
            return True


    def insert_account(self, a):
        client = MongoClient('localhost', PORT)
        db = client.station_database
        cursor = db['account_collections']
        cursor.insert_one(a)
        client.close()

    def login(self, a):
        username = a['username']
        password = a['password']
        client = MongoClient('localhost', PORT)
        db = client.station_database
        cursor = db['account_collections']
        if cursor.find_one({'username': username}) == None:
            return 0    #不存在账号
        else:
            if cursor.find_one({'username': username, 'password': password}) == None:
                return 1    #密码错误
            else:
                return 2    #登陆成功