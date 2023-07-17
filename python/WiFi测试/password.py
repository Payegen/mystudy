import itertools as its
# 迭代器
# its.product(range(2), repeat=3) # --> 000 001 010 011 100 101 110 111

words = "1234568790"
# words = "abc"
# itertools循环迭代的模块
r =its.product(words,repeat=4)

# 打开一个文件用于追加  如果文件存在，在文件末尾追加内容
dic = open("pass.txt","a")
for i in r:
    # 元组(1,1,1,1,1)
    # print(i)
    # 用""来连接
    # print("".join(i))
    dic.write("".join(i))
    dic.write("".join("\n"))
dic.close()