#!/usr/local/bin/python3
from connect import *
import time
import hashlib
 
def md5(arg):
    md5_pwd = hashlib.md5(bytes('abd',encoding='utf-8'))
    md5_pwd.update(bytes(arg,encoding='utf-8'))
    return md5_pwd.hexdigest()
 
def register():
    try:
        while True:
            name=input("输入你的名字：").strip()
            cursor.execute("select count(*) from user where name=%s", name)
            count=cursor.fetchone()[0]
            length=len(name)
            if count == 1:
                print("用户名已存在！")
                continue
            elif length<6:
                print("用户名最少6个字符！")
                continue
            elif length>15:
                print("用户名最多15个字符！")
                continue
            elif count == 0 and length>=6 and length=<15:
                password=input("输入你的密码：").strip()
                time=int(time.time())
                string=name+password+str(time)
                passwd=md5(string)
                cursor.execute("insert into user(name,passwd,createtime) values(%s,%s,%s)",(name,passwd,time))
                break
    except:
        conn.rollback()
    else:
        conn.commit()
    conn.close()
     
register()
