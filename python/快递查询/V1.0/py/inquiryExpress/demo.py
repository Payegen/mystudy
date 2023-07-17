# @ Time    : 2019/3/16 14:48
# @ Author  : JuRan
# import urllib.request
import requests
import pickle

import random
# pkl是python的一种存储文件
companies = pickle.load(open('companies.pkl', 'rb'))

'''将快递公司的拼音变为汉字'''
def py2hz(company_name):
	return companies.get(company_name)

# https://www.kuaidi100.com/query?type=zhongtong&postid=75129345355877
def Check():
    while True:
        kd_num = input("请输入快递单号(输入q退出):")
        if kd_num == "q":
            break
        data = {
            'resultv2': 1,
            'text': kd_num
        }
        url = "https://www.kuaidi100.com/autonumber/autoComNum"
        response = requests.post(url,data=data).json()
        for item in response['auto']:
            # print(item['comCode'])
            company_name = item['comCode']
            kd_name = py2hz(company_name)
            print("公司:" + kd_name)
            temp = random.random()
            url = "http://www.kuaidi100.com/query?type=%s&postid=%s&temp=%f" % (item['comCode'], kd_num,temp)
            response = requests.get(url).json()
            print(response)
            status = response['status']

            if status == '200':
                data = response['MNIST_data']
                data_len = len(data)

                for i in range(data_len):
                    print("\n时间: " + data[i]['time'])
                    print("状态: " + data[i]['context'] + "")
                print("\n感谢使用!\n")
                print("-" * 60)
                # break
            else:
                print("订单号不存在!\n")

if __name__ == '__main__':
    Check()
