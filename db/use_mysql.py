# 使用数据库MYSQL
import mysql.connector

conn = mysql.connector.connect(user='root', password='11111', database='test')

# 增
cursor = conn.cursor()
cursor.execute('create table user(id int(20) primary key, name varchar(20), age varchar(20))')
cursor.execute('insert into user(id, name, age) values (%s, %s, %s)', ['1', 'xiaoming', '18']) # 插入一条数据

cursor.executemany('insert into user(id, name, age) values (%s, %s, %s)', (    # 插入多条数据
    ('1', 'xioaming', '18'),
    ('2', 'zhangsan', '19'),
    ('3', 'xioali', '20'),
))

print(cursor.rowcount)
conn.commit()
cursor.close()
conn.close()

# 查
cursor = conn.cursor()
cursor.execute('select * from user where id=%s', ('1', ))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()

# 改
cursor = conn.cursor()
cursor.execute('update user set age=%s where id=%s', ('19', '1'))

cursor.execute('select * from user')
values = cursor.fetchall()
print(values)
conn.commit()
cursor.close()
conn.close()


# 删
cursor = conn.cursor()
cursor.execute('delete from user where id=\'1\'')
cursor.close()
conn.commit()
conn.close()













