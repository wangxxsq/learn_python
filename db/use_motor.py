# 使用Motor
import tornado.gen
import motor.motor_tornado
from tornado.ioloop import IOLoop

client = motor.motor_tornado.MotorClient('mongodb://localhost:27017/')
# client = motor.motor_tornado.MotorClient('localhost', 27017)
db = client.test_database
# db =client['test_database']
collection = db.test_collection
# collection = db['test_collection']

# 使用motor实现mongodb的增删改查


# 插入数据
@tornado.gen.coroutine
def do_insert():
    for i in range(10):
        result = yield db.test_collection.insert({'i': i})
        print(result)


# 查询获取一条数据
@tornado.gen.coroutine
def do_find_one():
    document = yield db.test_collection.find_one({'i': {'$lt': 1}})
    print(document)


# 查询获取多条记录
@tornado.gen.coroutine
def do_find():
    cursor = db.test_collection.find({'i': {'$lt': 5}}).sort('i')
    for document in (yield cursor.to_list(length=100)):
        print(document)


# 异步查询每次获取一条记录
@tornado.gen.coroutine
def do_find2():
    cursor = db.test_collection.find({'i': {'$lt': 5}})
    while (yield cursor.fetch_next):
        document = cursor.next_object()
        print(document)


# 查询使用 sort, limit, skip方法
@tornado.gen.coroutine
def do_find3():
    cursor = db.test_collection.find({'i': {'$lt': 5}})
    cursor.sort('i', -1).limit(2).skip(2)
    while (yield cursor.fetch_next):
        document = cursor.next_object()
        print(document)


# 计算所有符合查询条件的个数
@tornado.gen.coroutine
def do_count():
    n = yield db.test_collection.find().count()  # 计算数据库中所有记录的总数
    n1 = yield db.test_collection.find({'i': {'$gt': 5}}).count()  # 所有大于4的记录总数
    n2 = yield db.test_collection.find({'i': {'$lt': 8, '$gt': 2}}).count()  # 所有大于2且小于8的记录总数
    print('%s %s %s'.format(n, n1, n2))


# 替换
@tornado.gen.coroutine
def do_replace():
    result = yield db.test_collection.replace_one({'i': 4}, {'name': 'xinxin'})
    print(result)


# 更新
def do_update():
    result = db.test_collection.update_one({'i': 5}, {'$set': {'key': 'value'}})  # 更新一条记录
    result_many = db.test_collection.update_many({'i': {'$gt': 6}}, {'$set': {'sss': 'value'}})  # 更新多条信息
    print(result)
    print(result_many)


# 删除
def do_delete():
    result = db.test_collection.delete_one({'i': 3})  # 删除一条记录
    result_many = db.test_collection.delete_many({'i': {'$gt': 4}}) # 删除多条记录
    print(result)
    print(result_many)


# IOLoop.current().run_sync(do_insert)
# IOLoop.current().run_sync(do_find_one)
# IOLoop.current().run_sync(do_find)
# IOLoop.current().run_sync(do_find2)
# IOLoop.current().run_sync(do_find3)
# IOLoop.current().run_sync(do_count)
# IOLoop.current().run_sync(do_replace)
# IOLoop.current().run_sync(do_update)
# IOLoop.current().run_sync(do_delete)










