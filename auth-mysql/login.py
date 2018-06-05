#!/usr/local/bin/python3
# encoding:utf-8

from connect import *
import hashlib
import sys

def md5(arg):
    md5_pwd = hashlib.md5(bytes('abd',encoding='utf-8'))
    md5_pwd.update(bytes(arg,encoding='utf-8'))
    return md5_pwd.hexdigest()
     
def login():
    name=input("输入你的名字：").strip()
    cursor.execute("select count(*) from user where uname=%s",name)
    count=cursor.fetchone()[0]
    # print(count)
    if count == 1:
        i=0
        while (i<3):
            cursor.execute("select createtime from user where uname=%s",name)
            time=cursor.fetchone()[0]
            password=input("输入你的密码：").strip()
            string=name+password+str(time)
            passwd=md5(string)
            cursor.execute("select upwd from user where uname=%s",name)
            password_db=cursor.fetchone()[0]
            print("DEBUG: password_db= %s", password_db)
            i=i+1
            j=3-i
            if passwd == password_db:
                print("登录成功！%s，欢迎您。" % name)
                conn.close()
                break
            elif passwd != password_db:
                print("密码错误，请重新输入！")
                print("您还可以输入%s次！" % j)
                continue
            break
    elif count == 0:
        print("您的账户不存在！")
    else:
        print("ERROR! There are more than one user account named \'%s\'" % name)
login()
