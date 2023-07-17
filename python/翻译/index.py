from tkinter import *
import urllib.request
import urllib.parse
import json
def translate(content):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict2.index'
    # 第一种方法
    # head必须是字典类型的参数
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883'
    data = {}
    data['type'] = 'AUTO'
    data['i'] = content
    data['doctype'] = 'json'
    data['xmlVersion'] = '1.8'
    data['keyfrom'] = 'fanyi.web'
    data['ue'] = 'UTF-8'
    data['action'] = 'FY_BY_CLICKBUTTON'
    data['typoResult'] = 'true'
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, data, head)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    target = json.loads(html)
    result = target['translateResult'][0][0]['tgt']
    return result


root = Tk()
root.title('中英互译')
frame = Frame(root)
frame.grid(padx=10, pady=10)

v2 = StringVar()

Label(frame, text='输入要翻译的文字：').grid(row=0, column=0)
Label(frame, text='翻译之后的结果：').grid(row=5, column=0)

e1 = Entry(frame)
e1.grid(row=0, column=1)

e2 = Entry(frame, textvariable=v2, state='readonly') \
    .grid(row=5, column=1)


def trans():
    r = translate(e1.get())
    v2.set(r)
    # print(r)


Button(root, text='翻译', width=10, command=trans).grid(row=10, column=0, sticky=W)
Button(root, text='退出', width=10, command=root.quit).grid(row=10, column=1, sticky=E)
mainloop()