# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 14:04
# @Author  : Amy
# @File    : bd_spider.py
import requests

def bdSpider(kw):
    url = "https://www.baidu.com/s?wd=%s"%kw
    # **kwargs-->动态参数-->{}-->键值对
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }
    response = requests.get(url=url,headers=headers)
    # print(response.text)
    # print(response.request.headers)
    return response.text


# kw = input("请输入：")
# bdSpider(kw)

# 如何实现->获取到这个kw->传到爬虫脚本中->爬取到的页面渲染到自己页面
'''
问题：
后端怎么去获取用户在搜索框输入的内容-->传给bdSpider->爬取到的页面渲染到自己页面
1.通过form表单 将输入内容提交到路由
2.后端从路由中获取
3.传给爬虫并接收爬虫获取的页面
4.后端渲染到页面
'''
