# -*- coding: utf-8 -*-
from collections import OrderedDict

d1 = dict([('a', 1), ('b', 2), ('c', 3)])  # key无序
print('d1:', d1)
print(type(d1))

print('#############################################')

d2 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])   # key有序
print('d2:', d2)
print(type(d2))







