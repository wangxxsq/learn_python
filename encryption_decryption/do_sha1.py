import hashlib


#sha1加密(小写)
def to_sha1(part):
    sha1 = hashlib.sha1()
    sha1.update(part.encode())
    return sha1.hexdigest()


#sha1加密(大写)
def sha1_signature(part):
    sha1 = hashlib.sha1()
    sha1.update(part.encode())
    return sha1.hexdigest().upper()


if __name__ == '__main__':
    print(to_sha1('hello, world'))
    print(sha1_signature('hello, world'))