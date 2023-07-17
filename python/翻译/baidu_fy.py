import requests

def py():
    url = 'http://fanyi.baidu.com/v2transapi/'
    while True:
        print('感谢百度翻译，禁止用于商业用途')
        print('----------------------------')
        content=input("中译英请输入1，英译中请输入2，退出请输入Q\n")
        if content in['Q']:
            break;
        elif content in['2']:
            content=input("请输入翻译内容\n")
            data={
               ' from':'en','to':'zh','query':content  ,
               'transtype':'translang',
               'simple_means_flag':'3',
            }
        elif content in['1']:
            content=input("请输入翻译内容\n")
            data={
               ' from':'zh','to':'en','query':content  ,
               'transtype':'translang',
               'simple_means_flag':'3',
            }

        headers ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0'}
        response = requests.post(url,data,headers=headers)
        head = response.headers

            #text = response.text
            #text = json.loads(text)
            #res = text['trans_result']['MNIST_data'][0]['dst']
            #print(res)
            #print(head['Content-Type'])
        print(response.json()['trans_result']['MNIST_data'][0]['dst'])

py()

if __name__=="__main__":
    py()