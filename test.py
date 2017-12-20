#coding:utf-8
import MySQLdb
conn=MySQLdb.Connect(
    host="localhost",
    user='root',
    passwd='123456',
    db='imook',
    charset='utf8'
)
cursor=conn.cursor()

sql="select * from User"
cursor.execute(sql)

print cursor.rowcount

rs=cursor.fetchall()
print rs
for row in rs:
    print "userId=%s,userName=%s" % row


# rs=cursor.fetchall();
# for row in rs:
#     print "userId=%s,userName=%s" % row





conn.close()
cursor.close()
