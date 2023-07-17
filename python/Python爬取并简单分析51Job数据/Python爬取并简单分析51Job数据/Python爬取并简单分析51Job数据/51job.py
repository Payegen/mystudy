'''

Python全栈开发交流群：976191019

'''
import time
import random
import pickle
import requests
from lxml import etree


headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
			'Host': 'search.51job.com'
		}


# 51job小爬虫
def Spider(keyword, num_page=100):
	data = {}
	error_time = 0
	for i in range(1, num_page+1):
		print('[INFO]: Start to get the data in page-%d' % i)
		url = 'http://search.51job.com/list/000000,000000,0000,00,9,99,%s,2,%d.html' % (keyword, i)
		try:
			res = requests.get(url, headers=headers)
			res.encoding = 'gbk'
			html = etree.HTML(res.text)
			page_data_list = html.xpath("//div[@class='dw_table']")
			for pdl in page_data_list:
				# 职位
				position = pdl.xpath("./div/p/span/a/@title")
				# 公司名称
				company = pdl.xpath("./div/span[@class='t2']/a/text()")
				# 工作地区
				area = pdl.xpath("./div[@class='el']/span[@class='t3']")
				# 工资
				wage = pdl.xpath("./div[@class='el']/span[@class='t4']")
				# 发布时间
				publishtime = pdl.xpath("./div[@class='el']/span[@class='t5']")
				# 详情页链接
				link = pdl.xpath("./div/p/span/a/@href")
				# 数据保存
				for j in range(len(position)):
					data[company[j]] = [position[j], area[j].text, wage[j].text, publishtime[j].text, link[j]]
			time.sleep(1 + random.random())
		except:
			error_time += 1
			time.sleep(60)
			if error_time > 3:
				break
	with open('data.pkl', 'wb') as f:
		pickle.dump(data, f)


if __name__ == '__main__':
	Spider('python', 775)