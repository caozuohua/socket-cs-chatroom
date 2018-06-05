#!/usr/local/bin/python3
import pymysql
from config import *
conn=pymysql.connect(host=hostname,user=user,passwd=password,db=database)
cursor=conn.cursor()
