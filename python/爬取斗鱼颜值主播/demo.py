import requests
import re
import json
from urllib.request import urlretrieve
import time
from face_level import face


url = "https://www.douyu.com/g_yz"
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
}

result = requests.get(url,headers=header).text
# $ 是以什么结束  . 匹配除了换行符\n以外的任意一个字符
reg = r"window\.\$DATA = (.*?);.*?var pageType = 'list2';"
data = re.findall(reg,result,re.S)
# print(MNIST_data[0])

dy_data = json.loads(data[0])
path = "./image"
for item in dy_data['list']:
    name = item['rn']
    image_url = item['rs1']
    print("正在下载:%s的图片"%name)
    filepath = path + "/" + name + ".png"
    urlretrieve(image_url,filepath)
    time.sleep(0.2)
    level = face(filepath)
    print("颜值打分%s"%level)
