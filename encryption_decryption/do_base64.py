# -*- coding: utf-8 -*-
#base64编码解码（适用于小段内容的编码）
import base64


s = 'hello, world'
s1 = base64.b64encode(s.encode('utf8'))  #加密
print(s1)
s2 = base64.b64decode(s1).decode()  #解密
print(s2)


s = 'hello, world'
s1 = base64.urlsafe_b64encode(s.encode('utf8'))  # 加密
print(s1)
s2 = base64.urlsafe_b64decode(s1).decode()   # 解密
print(s2)




