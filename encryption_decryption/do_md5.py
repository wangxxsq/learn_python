# -*- coding: utf-8 -*-
import hashlib


# MD5小写签名
def to_md5(part):
    m = hashlib.md5()
    m.update(part.encode())
    return m.hexdigest()


# MD5大写签名
def md5_signature(part):
    m = hashlib.md5()
    m.update(part.encode())
    return m.hexdigest().upper()


if __name__ == '__main__':
    print(to_md5('hello, world'))
    print(md5_signature('hello, world'))

