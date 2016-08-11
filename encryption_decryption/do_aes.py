import base64
from Crypto.Cipher import AES

BS = 16


# AES加解密(CBC模式，需要key, iv)
def padding(s):
    return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)


def unpadding(s):
    return s[0:-ord(s[-1])]


def aes_encrypt(code, passphrase, iv):
    aes = AES.new(passphrase, AES.MODE_CBC, iv)
    b = aes.encrypt(padding(code))
    sign_code = base64.b64encode(b).decode('utf8')
    return sign_code


# AES加解密(ECB模式，只需要key)
def aes_decrypt(code, passphrase, iv):
    aes = AES.new(passphrase, AES.MODE_CBC, iv)
    encrypted = aes.decrypt(base64.b64decode(code))
    decryption_code = unpadding(encrypted.decode('utf8'))
    return decryption_code


def aes_encryption_ecb(code, secret_key):
    aes = AES.new(secret_key, AES.MODE_ECB)
    b = aes.encrypt(padding(code))
    return base64.b64encode(b).decode('utf8')


def aes_decrypt_ecb(code, secret_key):
    aes = AES.new(secret_key, AES.MODE_ECB)
    encrypted = aes.decrypt(base64.b64decode(code))
    decryption_code = unpadding(encrypted.decode('utf8'))
    return decryption_code


if __name__ == '__main__':
    print(aes_encrypt('hello, world', 'eNCmYq0lyK6GgPhF', '4552684879724199'))
    print(aes_decrypt('L2+3ee3cgTn9Ii5SOsvwtg==', 'eNCmYq0lyK6GgPhF', '4552684879724199'))
    print(aes_encryption_ecb('hello, world', '6224wt16gnv9veja5zldj77nzh28w3tv'))
    print(aes_decrypt_ecb('/PaF7gA4KSw39wOBhFZg0w==', '6224wt16gnv9veja5zldj77nzh28w3tv'))

