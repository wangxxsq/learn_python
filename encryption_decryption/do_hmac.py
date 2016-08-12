# -*- coding: utf-8 -*-
import hmac
from hashlib import sha1


# 加密
def hash_hmac(key, code, sha1):
    hmac_code = hmac.new(key.encode(), code.encode(), sha1)
    return hmac_code.hexdigest()


# 解密


if __name__ == '__main__':
    print(hash_hmac('08F5B4886112BC6F1E04FE42DACDB2E8', 'xinxin', sha1))
