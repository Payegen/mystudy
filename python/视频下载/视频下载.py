from urllib.request import urlretrieve
import requests
# 解析库   XPath 是一门在 XML 文档中查找信息的语言
# lxml，使用的是 Xpath 语法，同样是效率比较高的解析方法
from lxml import etree
import re
import os
import time

# 获取页面源代码
# 获取视频id
# 拼接完整URL
# 获取视频播放地址
# 下载视频

# 传url 为了下载更多
def download(url):
    # 模拟浏览器发送请求
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
    # url = 'http://www.pearvideo.com/category_8'

    # 获取网页源代码
    html = requests.get(url,headers=header).text
    # 接下来获取ID 有几种方法
    # 把文本文件处理成可解析对象
    # html = etree.HTML(html)
    # 利用xpath找到需要的id
    # video_id = html.xpath('//div[@class="vervideo-bd"]/a/@href')

    reg = '<a href="(.*?)" class="vervideo-lilink actplay">'
    video_id = re.findall(reg,html)
    # print(video_id)

    # 定义一个空列表
    video_url = []
    starturl = 'http://www.pearvideo.com'
    for i in video_id:
        # 拼接完整URL地址
        newurl = starturl +'/'+ i
        # 添加
        video_url.append(newurl)

    for playurl in video_url:
        # 获取播放页源代码
        html = requests.get(playurl).text
        # 正则匹配  匹配播放地址
        req = 'ldUrl="",srcUrl="(.*?)",vdoUrl'
        # 编译正则表达式字符串为对象，目的是增加效 率
        # reg = re.compile(reg)
        purl = re.findall(req, html)
        # 获取视频标题
        req = '<h1 class="video-tt">(.*?)</h1>'
        pname = re.findall(req,html)

        print("正在下载视频:%s"%pname[0])
        path = "video"
        if path not in os.listdir():
            os.mkdir(path)

        urlretrieve(purl[0],path+"/%s.mp4"%pname[0])

download('http://www.pearvideo.com/category_8')


# n = 12
# def downloadmore():
#     while True:
#         global n
#         if n > 48:
#             # 跳出循环
#             return
#         # 找到规律
#         url = "http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=9&start=%d"%n
#         # url = "http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=8&start=%d&mrd=0.1864387383822984&hotContIds=1365471,1367413,1367109"%n
#         n += 12
#         time.sleep(1)
#         # 调用下载方法
#         download(url)

# category = [9,10,1,2,5,8,4,3,31,6,59]
# for category_id in category:
#     downloadmore(category_id)

# downloadmore()

# 从事非本专业的 %82.3   10%左右的人 失业
# 47.8% 从事销售  2000 - 5000
# 10%   从事IT 互联网行业  6000-8000
# 选对行业 比努力更重要
# 互联网行业要比

# Java  C  Python
# C语言   运行速度快   底层语言
# Java    高级语言
# Python   高级语言  简洁
# C > java > python     运行速度
# 现在是微乎其微的差别
# 开发效率
# Python > jave > c

# 老师建议大家学习Python
# web   后端开发
# 爬虫   爬取信息  采集信息  采集网站数据  大数据  数据分析

# 工作岗位 多
# 薪资    高
# 学习难度  低

# 付费的课程
# 如果想跟着老师来学习  会提供专业的技术指导，以及符合企业级的课程内容
# 大家只需要400 预定就可以获得阿里云大数据的认证课程
# 那么接下来跟大家说一下我们系统学习班是怎么上课的


# 人与人最小的差别是智商  最大的差别是努力坚持
# 也许你的父母觉得从事公务员才是稳定的工作
# 还这么年轻  为什么不给自己一次拼搏的机会

# 如果证明自己的勇气 就不要怪自己的现状不好

# 人们通常喜欢吃生活的苦  不愿意去吃学习的苦
# 生活的苦是自己不能控制的 是被动去吃的   但是学习的苦 是自己主动去吃的
# 学习的苦是主动去吃苦，生活的苦是不得不吃的苦。主动吃苦的人会得到更多的回报，被动吃苦的人只是为了生存。
# 便学习的结果，可能让自己薪资翻倍，甚至可能从此过上高富帅白富美的生活，
# 但也没有嗑瓜子和刷抖音这样正反馈更快更强的事物有吸引力



# 爬虫的设计思路
# 1 首先确定需要爬去的网页URL地址
# 2 通过HTTP/HTTPS协议来获取对应的HTML页面
# 3 提取HTML页面里面有用的数据

# 为什么选择python来做爬虫
# 代码简介  开发效率高

# 自己读书你只能学到你想学的，而系统学习你能学到你需要学的。
# 单纯的自学就是从学习的方向、学习内容、学习步骤、学习计划、学习方法都要自己在茫茫如大海中探索