# Redis Sentinel
from redis.sentinel import Sentinel

sentinel = Sentinel([('localhost', 26379)], socket_timeout=0.3, db=15, decode_responses=True)
master = sentinel.master_for('madeira')
slave = sentinel.slave_for('madeira')

# redis 增删改查
master.set('foo', 'bar')
slave.get('foo')
master.delete('foo')

