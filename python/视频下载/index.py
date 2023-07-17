import requests
# 最主要的功能是从网页抓取数据
from bs4 import BeautifulSoup
import urllib.request
x = 0
def getNovertContent(page = 1):
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81       Safari/537.36",
    # }
    response = requests.get("https://www.dbmeinv.com/dbgroup/show.htm?cid=4&pager_offset={}".format(page))
    # response.encoding = "utf-8"
    html = response.text

    # 创建对象 解析网页  lxml  解析文档
    soup = BeautifulSoup(html,'html.parser')
    # 找到img标签   搜索文档树  还可以传 a  找a标签
    my_girl = soup.find_all('img')
    for gril in my_girl:
        # 获取src路径  获取属性
        link = gril.get('src')
        title = gril.get('title')
        # print(title)
        # print(link)
        global x
        urllib.request.urlretrieve(link,'image\%s.jpg' %title)
        x+=1
        print("正在下载第%s张"%x)


for i in range(1,10):
    print('正在下载第{}页图片'.format(i))
    getNovertContent(i)