#coding:utf-8
import MySQLdb
conn=MySQLdb.Connect(
    host="47.95.227.74",
    user='root',
    passwd='123456',
    db='manager',
    charset='utf8'
)
cursor=conn.cursor()

sql="select * from staff"
sql_insert="insert into User(userId,userName) values(9,'我Love你')"
sql_delete="delete from User where userId<2"
sql_update="update User set userName='我也是' where userId=2"
cursor.execute(sql)



rs=cursor.fetchall()
print rs
for row in rs:
    print "userId=%s,userName=%s" % row
print cursor.rowcount
try:
    cursor.execute(sql_insert)
    cursor.execute(sql_delete)
    cursor.execute(sql_update)

    conn.commit()
except Exception as e:
    print e
conn.rollback()



conn.close()
cursor.close()
