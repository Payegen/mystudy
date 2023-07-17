import hashlib
# python3中已经废除了MD5模块
str = "juran"
# 创建md5对象
h1 = hashlib.md5()
# 声明encode
h1.update(str.encode(encoding='utf-8'))
print(h1.hexdigest())


# Unicode-objects must be encoded before hashing
# print(hashlib.md5("juran"))
