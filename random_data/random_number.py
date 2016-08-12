# -*- coding: utf-8 -*-
import binascii
import os
import random
import string


# 生成4位随机码
def token(size):
    return binascii.hexlify(os.urandom(size)).decode("utf8")


# 获取32位随机字符串
def gen_key(size, chars=None):
    if chars is None:
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits

    return ''.join(random.choice(chars) for _ in range(size))


if __name__ == '__main__':
    print(token(2))
    print(gen_key(16, string.digits))  # 随机数字（16位）
    print(gen_key(16, string.ascii_uppercase))  # 随机大写字母
    print(gen_key(16, string.ascii_lowercase))  # 随机小写字母
    print(gen_key(16, string.ascii_uppercase + string.ascii_lowercase + string.digits))  # 随机大小写、数字
    print(gen_key(32, string.ascii_uppercase + string.ascii_lowercase + string.digits))  # 随机大小写、数字（32位）



