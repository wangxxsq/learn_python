import pymongo

conn = pymongo.Connection("localhost", 27017)  # 连接数据库
db = conn.test  # 进入数据库test
user = db.user  # 进入集合user

# 增
info = {"_id": 1, "name": 'xiaoming', "age": 18}  # 插入一条记录
db.user.insert(info)  # 主键("_id")存在，不做任何处理
db.user.save(info)  # 主键("_id")存在，更新记录


'''增加多条数据'''
info = [
    {'_id': 1, "name": 'xioaming', "age": 18},
    {'_id': 2, "name": 'xiaoli', "age": 19},
    {'_id': 3, "name": 'xiaozhang', "age": 20},
]

# 删
db.user.remove(id)  # 根据id删除一条记录
db.user.remove()  # 删除集合里所有记录
db.user.remove({"name": "xiaoming"})  # 删除name=xiaoming的记录
db.user.drop()   # 删除集合

# 改
db.user.update({'_id': 1}, {"$set": {"name": 'xiaoming', "age": '18'}})  # 更新一条记录

# 查
for u in db.user.find({"name": "xiaoming"}):
    print(u)














