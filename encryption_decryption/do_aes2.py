# -*- coding: utf-8 -*-

# 对业务数据进行AES加密表示成十六进制字符串
# 加密算法参数：
# 密钥的大小（以位为单位）KeySize = 128
# 操作块大小（以位为单位）BlockSize = 128
# 加密模式CipherMode.CBC
# 填充模式PaddingMode.PKCS7或PaddingMode.PKCS5
# 注：key与iv为十六进制字符串，长度为32字符，转成字节长度是16字节
import json
import binascii
from Crypto.Cipher import AES

# 加密前业务数据：
code = {
    "key1": 'key1',
    "key2": 'key2',
    "key3": 'key3',
    "key4": 'key4',
}
key = '7A9B48C4960551045B467B89015B528E'
iv = '787B4DD7A9229B3316A6868F537468D5'

BS = 16


def padding(s):
    return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)


def unpadding(s):
    return s[0:-ord(s[-1])]


# 加密代码如下：
def aes_encrypt(code, secret_key, iv):
    aes = AES.new(secret_key, AES.MODE_CBC, iv)
    b = aes.encrypt(padding(code))
    return binascii.hexlify(b).decode()


# 解密代码如下：

def aes_decrypt(code, passphrase, iv):
    aes = AES.new(passphrase, AES.MODE_CBC, iv)
    encrypted = aes.decrypt(binascii.unhexlify(code))
    decryption_code = unpadding(encrypted.decode())
    return decryption_code

if __name__ == '__main__':
    key = binascii.unhexlify(key)
    iv = binascii.unhexlify(iv)
    code = json.dumps(code)
    print(aes_encrypt(code, key, iv))
    s = 'b3eda8d1b762d1784b520a7d11d774d765e2c920b1b996c130d3c3e884e8b16ec431ac98457b2e5e47e5feaf2eadc702e9465534e9abb66ad1bb2135d0a153fbc67dfc6067462db65a390b45818ea734'
    print(aes_decrypt(s, key, iv))

