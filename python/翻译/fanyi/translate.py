from tkinter import *
from tkinter import messagebox
import requests

def translate():
    # 获取用户输入的单词
    content = entry.get()  
    if content == '':
        messagebox.showinfo('提示','请输入要翻译的内容')
    else:
        # while True:
        url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        # url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        data = {}
        # 找到JS文件 搜索fanyideskweb  解释
        # u = 'fanyideskweb'
        # d = content
        # f = str(int(time.time() * 1000) + random.randint(1, 10))
        # c = 'ebSeFb%=XZ%T[KZ)c(sy!'
        # sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()

        header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
        data['action'] = 'FY_BY_CLICKBUTTION'
        data['client'] = 'fanyideskweb'
        data['doctype'] = 'json'
        data['from'] = 'AUTO'
        data['i'] = content
        data['keyfrom'] = 'fanyi.web'
        # 时间戳是指格林威治时间1970年01月01日00时00分00秒(北京时间1970年01月01日08时00分00秒)起至现在的总秒数
        # MNIST_data['salt'] = f
        # MNIST_data['sign'] = sign
        data['smartresult'] = 'dict'
        data['to'] = 'AUTO'
        data['typoResult'] = 'false'
        data['version'] = '2.1'

        result = requests.post(url, data=data,headers=header)

        translate = result.json()

        translate = translate['translateResult'][0][0]['tgt']
        res.set(translate)
        # print(translate)
        # return translate['translateResult'][0][0]['tgt']
        return ""


from tkinter import *
root = Tk()
root.title('中英互译')
# frame = Frame(root)
# frame.grid(padx=10, pady=10)

# 获取屏幕 宽、高
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
w = 600
h = 300
# 计算 x, y 位置
x = str(int((ws/2) - (w/2)))
y = str(int((hs/2) - (h/2)))

# 窗口大小
root.geometry('370x100')
# 窗口位置
root.geometry('+500+300')
# 标签控件
lable = Label(root, text='输入要翻译的文字：')
# grid 网格式布局   pack 包  place 位置
lable.grid(row=0, column=0)
lable1 = Label(root, text='翻译之后的结果：')
lable1.grid(row=1, column=0)

# 输入控件  第一个
entry = Entry(root,font=("微软雅黑",15))
entry.grid(row=0, column=1)

# e2 = Entry(frame, textvariable=v2, state='readonly').grid(row=5, column=1)

# 有些时候是需要跟踪变量的值的变化，以保证值的变更随时可以显示在界面上
res = StringVar()
# 输入控件 第二个
entry1 = Entry(root,font=("微软雅黑",15),textvariable=res)
entry1.grid(row=1, column=1)

# 按钮标签
button = Button(root, text='翻译', width=10, command=translate)
# 你可以使用sticky选项去指定对齐方式 N/S/E/W，分别代表上/下/左/右
button.grid(row=2, column=0, sticky=W)

button1 = Button(root, text='退出', width=10, command=root.quit)
button1.grid(row=2, column=1, sticky=E)
# 显示窗口  消息循环
root.mainloop()


# 爬虫怎么抓取网页数据？

# 网页三大特征
# 1 网页都有自己唯一的URL
# 2 网页都是HTML来描述页面信息
# 3 网页都使用HTTP/HTTPS协议来传输HTML数据

# 爬虫的设计思路
# 1 首先确定需要爬去的网页URL地址
# 2 通过HTTP/HTTPS协议来获取对应的HTML页面
# 3 提取HTML页面里面有用的数据

# 为什么选择python来做爬虫
# 代码简介  开发效率高