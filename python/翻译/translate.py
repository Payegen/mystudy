import requests
import pyttsx3

def translate():
    # 获取用户输入的单词
    content = entry.get()
    # while True:
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    # url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    # 字典
    data = {}
    # u = 'fanyideskweb'
    # d = content
    # f = str(int(time.time() * 1000) + random.randint(1, 10))
    # c = 'ebSeFb%=XZ%T[KZ)c(sy!'
    # sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()
    data['action'] = 'FY_BY_CLICKBUTTION'
    data['client'] = 'fanyideskweb'
    data['doctype'] = 'json'
    data['from'] = 'AUTO'
    data['i'] = content
    data['keyfrom'] = 'fanyi.web'
    # MNIST_data['salt'] = f
    # MNIST_data['sign'] = sign
    data['smartresult'] = 'dict'
    data['to'] = 'AUTO'
    data['typoResult'] = 'false'
    data['version'] = '2.1'

    result = requests.post(url, data=data)
    # print(result)
    translate = result.json()

    translate = translate['translateResult'][0][0]['tgt']
    v2.set(translate)

    engine = pyttsx3.init()
    # 播放语音
    engine.say(translate)
    # 运行并且等待
    engine.runAndWait()
    # return translate



from tkinter import *
root = Tk()
root.title('中英互译')

# 窗口大小
root.geometry('370x100')
root.geometry('+500+300')
# 标签控件
lable = Label(root, text='输入要翻译的文字：')
# grid 网格式布局   pack 包  place 位置
lable.grid(row=0, column=0)
lable1 = Label(root, text='翻译之后的结果：')
lable1.grid(row=1, column=0)


entry = Entry(root,font=("微软雅黑",15))
entry.grid(row=0, column=1)

# e2 = Entry(frame, textvariable=v2, state='readonly').grid(row=5, column=1)

# 有些时候是需要跟踪变量的值的变化，以保证值的变更随时可以显示在界面上
v2 = StringVar()
entry1 = Entry(root,font=("微软雅黑",15),textvariable=v2)
entry1.grid(row=1, column=1)

# 按钮标签
button = Button(root, text='翻译', width=10, command=translate)
button.grid(row=2, column=0, sticky=W)
button1 = Button(root, text='退出', width=10, command=root.quit)

button1.grid(row=2, column=1, sticky=E)
root.mainloop()
