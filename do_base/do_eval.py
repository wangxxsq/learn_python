# Python内内建函数eval的用法
# eval()函数， 将字符串当成有效的表达式来求值并返回计算结果。

# 字符串转化为自动
s = '{"a": 1, "b": 2, "c": 3}'
d1 = eval(s)
print(d1)
print(type(d1))

# 字符串转化为list
s2 = '[1, 2, 3, "a", "b", "c"]'
lst1 = eval(s2)
print(lst1)
print(type(lst1))

# 字符串化为元祖
s3 = '(1, 2, 3, "a", "b", "c")'
t1 = eval(s3)
print(t1)
print(type(t1))
