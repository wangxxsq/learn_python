import redis

r = redis.StrictRedis(host='localhost', port=6379)
# redis 字符串的增删改查
r.set('name', 'test')  # 增
print('ok')
r.get('name')  # 查
r.set('name', 'test2')  # 改
r.delete('name')  # 删

