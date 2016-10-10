# SQLite数据库
import sqlite3

# 增 insert
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), age varchar(20))' )
cursor.execute('insert into user (id, name, age) values (\'2\', \'Jack\', \'18\')')
print(cursor.rowcount)
cursor.close()
conn.commit()
conn.close()

# 查  select...
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('select * from user where id=?', ('1', ))
cursor.execute('select * from user')
values = cursor.fetchall()
print(values)
cursor.close()
conn.commit()
conn.close()

# 改  update
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('update user set age=? where id=?', ('19', '1'))
cursor.execute('select * from user')
values = cursor.fetchall()
print(values)
cursor.close()
conn.commit()
conn.close()


# 删  delete
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('delete from user where id=?', ('2',))
cursor.execute('select * from user')
values = cursor.fetchall()
print(values)
cursor.close()
conn.commit()
conn.close()





