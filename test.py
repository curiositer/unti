# from unti import app
# app.config['SECRET_KEY']

# import json
# from os import path
# import mysql.connector
# f = open(path.join(path.dirname(__file__), 'config.json'), 'r')
# config = json.load(f)
# f.close()
#
# db = mysql.connector.connect(**config)
#
# cursor=db.cursor()
# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = ('Google', 'https://www.google.com')
# # sql="create table sites (name varchar(100) ,url varchar(100) )" # 创建表
# # cursor.execute(sql)
# cursor.execute(sql, val)
# db.commit()   # 添加数据时需要进行commit操作
# db.close()

# from werkzeug.security import generate_password_hash
# hash = generate_password_hash('123')     # 密码加密（多次加密同一密码得到不同结果，为防止通过对比加密后字符串进行解密）
# print(hash)
#
# from werkzeug.security import check_password_hash
# result = check_password_hash(hash, 'foobar')    # 密码验证
# print(result)

# import time
# a = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))     # 时间表示
# print(a)

import json
from werkzeug.security import generate_password_hash
import uuid

h = 'host'
p = 'port'
u = 'user'
print(type(generate_password_hash('1111')))
print(str(uuid.uuid4()))

with open("config.json", 'w+') as f:
    try:
        profiles = json.load(f)
    except ValueError:
        profiles = {}
    # print(profiles[h])
    profiles[h] = [generate_password_hash('1111'),str(uuid.uuid4())]
    print(profiles)
    f.write(json.dumps(profiles))

    print(json.dumps(profiles))

PROFILE_FILE = "profiles.json"
with open(PROFILE_FILE, 'w+') as f:
    try:
        profiles = json.load(f)
    except ValueError:
        profiles = {}  # 文件以字典方式存储，username为索引
    profiles[self.username] = [password_hash,
                               self.id]
    f.write(json.dumps(profiles))