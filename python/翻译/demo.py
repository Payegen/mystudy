import time
import random
import hashlib
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Referer': 'http://fanyi.youdao.com/',
    # 'Cookie': 'OUTFOX_SEARCH_USER_ID=-481680322@10.169.0.83;'
    'Cookie': 'YOUDAO_MOBILE_ACCESS_TYPE=1; OUTFOX_SEARCH_USER_ID=-948988617@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=1513926823.4449036; JSESSIONID=aaavlPA_zFL7d-CwnkWXw; ___rl__test__cookies=1565249827197'
}

# 这里ctrl+R 替换 (.*?):(.*)   '$1':'$2',  勾选Match Case Regex In Selection 三个选项
data = {
    'i': None,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': None,
    'sign': None,
    'ts': None,
    'bv': None,
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION'
}
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

def translate(word):
    ts = str(int(time.time() * 10000))
    salt = ts + str(int(random.random() * 10))
    # n%A-rKaT5fb[Gy?;N5@Tj
    # sign = 'fanyideskweb' + word + salt + '97_3(jkMYg@T[KZQmqjTK'
    sign = 'fanyideskweb' + word + salt + 'n%A-rKaT5fb[Gy?;N5@Tj'
    sign = hashlib.md5(sign.encode('utf-8')).hexdigest()
    # Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0
    bv = '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    bv = hashlib.md5(bv.encode('utf-8')).hexdigest()

    data['i'] = word
    data['ts'] = ts

    data['salt'] = salt
    data['sign'] = sign
    data['bv'] = bv
    res = requests.post(url, headers=headers, data=data)
    return [res.json()['translateResult'][0][0].get('tgt')]

res = translate('翻译')
print(res)


# 就业
# 选择方向
# 学习的内容

# 0基础 转行
# web开发  工作岗位   多  薪资 高  看职友集
# web开发是什么？ 大家了解嘛  淘宝搜索 注册
# web开发掌握哪些技术

# 看招聘简章
# 大家有没有担心 自己的学历 和工作经验的
# 企业 重视技术 大于 学历

# 大家如果想跟着我来学习的话  我们逻辑教育也是有一套 完整的从零基础到就业 直到加薪的课程

# 课程是由我来授课,我在10月份 也参加了腾讯首届讲师大赛 而且Python类目下 只有我进入到决赛了

# 如果想跟着我来学习的同学 可以加客服老师 我们有一个非常详细的教学安排和授课计划


# 为什么这么多人喜欢自学
# 害怕失败

# 保持方向感,人生规划离不开时代大环境
# 不要低头盲目的去学习任何一门语言,抬头看看这个时代,看看这个社会的进步

# 人工智能大发展,各种语言争奇斗艳
# 很多传统的工作岗位,会被替代,越来越多的人力工作 会被取代 高速公路上的收费员 被干掉了 原先这可是金饭碗
# 我们逻辑教育也是推崇 终身学习 人人为师  为什么要终身学习  学习能力和学习意愿
# 1.01的365次方是非常大的值   而0.99的365次方是一个非常小的值
# 之前我有一位同学，在阿里年薪是50-100之间,他是怎么学习的？
# 花钱去学习各种各样的知识   如何高效学习  时间管理等等
# 如果你长了一个省钱的脑袋  那么赚钱就很难做到

# 技术会更新,速度会变快
# 复合岗位
# 行业将洗牌,越来越专业
# 人才储备越来越充裕,毕业生数量和质量逐年提高
# 如何你还想以比较粗范的学习方式来学习的话,那一定不会有一个好的结果
# 互联网行业野蛮生长期进入尾声
# 面试Java程序员,录取让去学Python

# 也会在我们课程里面加上操作系统和计算机组成原理

# 我们逻辑教育只说我们能做到的 只做我们说过的



