//微信公众号：python工程狮，关注获取更多编程视频资源福利
import requests

# 余票检测
def check_ticket():
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryX?leftTicketDTO.train_date=2019-02-26&leftTicketDTO.from_station=CSQ&leftTicketDTO.to_station=BJP&purpose_codes=ADULT'
    # 模拟浏览器去请求
    header = {
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
	}
    res = requests.get(url,headers = header)
    # 是一种轻量级的数据交换格式，易于人阅读和编写。
    res = res.json()
    result = res['MNIST_data']['result']
    # print(result)
    '''
    无座  26
    软座  23
    硬座  29
    硬卧  28
    '''
    num = 0
    for i in result:
        # print(i.split('|'))
        # 字符串切割
        temp_list = i.split("|")
        for n in temp_list:
            # print(num,n)
            num += 1
        print('-' * 50)
        num = 0
        if temp_list[26] == "有":
            print("无座有票",temp_list[3])
        else:
            print("无座无票",temp_list[3])

if __name__ == '__main__':
    check_ticket()