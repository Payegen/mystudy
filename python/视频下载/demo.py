# @ Time    : 2019/12/28 22:37
# @ Author  : JuRan
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
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
    # url = 'http://www.pearvideo.com/category_8'

    # 获取网页源代码
    html = requests.get(url, headers=header).text
    # 接下来获取ID 有几种方法
    # 把文本文件处理成可解析对象
    # html = etree.HTML(html)
    # 利用xpath找到需要的id
    # video_id = html.xpath('//div[@class="vervideo-bd"]/a/@href')

    reg = '<a href="(.*?)" class="vervideo-lilink actplay">'
    video_id = re.findall(reg, html)
    # print(video_id)

    # 定义一个空列表
    video_url = []
    starturl = 'http://www.pearvideo.com'
    for i in video_id:
        # 拼接完整URL地址
        newurl = starturl + '/' + i
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
        pname = re.findall(req, html)

        print("正在下载视频:%s" % pname[0])
        path = "video"
        if path not in os.listdir():
            os.mkdir(path)

        urlretrieve(purl[0], path + "/%s.mp4" % pname[0])


download('http://www.pearvideo.com/category_8')
