#!/usr/bin/python3
# encoding:utf-8

from authmysql.connect import *
import time
import hashlib
 
def md5(arg):
    md5_pwd = hashlib.md5(bytes('abd',encoding='utf-8'))
    md5_pwd.update(bytes(arg,encoding='utf-8'))
    return md5_pwd.hexdigest()
 
def register():
    try:
        while True:
            name=input("[注册]输入你的名字：").strip()
            cursor.execute("select count(*) from user where uname=%s", name)
            count=cursor.fetchone()[0]
            length=len(name)
            if count >= 1:
                print("用户名已存在！")
                continue
            elif length<6:
                print("用户名最少6个字符！")
                continue
            elif length>15:
                print("用户名最多15个字符！")
                continue
            # elif count == 0 and length >= 6 and length =< 15:
            elif count == 0 and (6 <= length <= 15):
                password=input("[注册]输入你的密码：").strip()
                # times = int(time.time())
                times = time.strftime('%Y-%m-%d', time.localtime(time.time()))
                string=name+password+str(times)
                passwd=md5(string)
                # DEBUG
                # name: caozuohua, passwd: e80aecc629b111dacf4fe46a1c8934e5, times: 1528187011
                print('[注册]name: %s, passwd: %s, times: %s' % (name, passwd, times))
                cursor.execute("insert into user(uname, upwd, createtime) values(%s,%s,%s)", (name, passwd, times))
                #if cursor.fetchone()[0] is not None:
                print("Registered succeed!")
                conn.commit()
                return 0
    except:
        conn.rollback()
    conn.close()


if __name__ == '__main__':
    register()
