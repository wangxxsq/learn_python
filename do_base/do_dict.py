# -*- coding: utf-8 -*-
# 从字典取值，有两种方法，最好使用dict.get()取值。
# dict["key"]  ,当键值不存在，程序会异常。
# dict.get("key") , 当键值不存在，会返回None，不会报错，程序扔进行下去。

d = {'a': 1, 'b': 2, 'c': 3}
print(d['a'])  # 输出1
print(d['x'])  # 程序报异常
print(d.get('a'))  # 输出1
print(d.get('x'))  # 返回None


