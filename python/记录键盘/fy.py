from tkinter import *
root = Tk()
root.title('中英互译')
frame = Frame(root)
frame.grid(padx=10, pady=10)

v2 = StringVar()

Label(frame, text='输入要翻译的文字：').grid(row=0, column=0)
Label(frame, text='翻译之后的结果：').grid(row=5, column=0)

e1 = Entry(frame,font=("微软雅黑",15))
e1.grid(row=0, column=1)

# e2 = Entry(frame, textvariable=v2, state='readonly').grid(row=5, column=1)

e2 = Entry(frame,font=("微软雅黑",15),textvariable=v2)
e2.grid(row=5, column=1)


def trans():
    r = translate(e1.get())
    v2.set(r)
    # print(r)


Button(root, text='翻译', width=10, command=trans).grid(row=10, column=0, sticky=W)
Button(root, text='退出', width=10, command=root.quit).grid(row=10, column=1, sticky=E)
mainloop()