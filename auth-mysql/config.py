# mysql info for host,user,password

"""
DATABASE: users
TABLE: user
FIELD: uid, uname, upwd, createtime
DESC user:
     +------------+--------------+------+-----+---------+----------------+
     | Field      | Type         | Null | Key | Default | Extra          |
     +------------+--------------+------+-----+---------+----------------+
     | uid        | int(11)      | NO   | PRI | NULL    | auto_increment |
     | uname      | varchar(100) | NO   |     | NULL    |                |
     | upwd       | varchar(100) | NO   |     | NULL    |                |
     | createtime | date         | YES  |     | NULL    |                |
     +------------+--------------+------+-----+---------+----------------+
"""

hostname = "localhost"
port = "3306"
user = "root"
password = "123123"
database = "users"
