# -*-coding:utf-8-*-
import urllib.request
import re
import os
import urllib
import time
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter import messagebox

#根据给定的网址来获取网页详细信息，得到的html就是网页的源代码  
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html.decode('UTF-8')
#从网页html源代码中分析图片链接并下载保存图片
def getImg(html):
    reg = r'</span><p><a href="(.+?)" target="_blank" class="view_img_link">'#正则表达式
    imgre = re.compile(reg)#将表达式编译一下，提高速度
    imglist = imgre.findall(html)#表示在整个网页中过滤出所有图片的地址，放在imglist中
    global path
    global startpage
    # 将图片保存到path文件夹中，如果没有path文件夹则创建文件夹
    if not os.path.isdir(path):  
        os.makedirs(path)  
    paths = path+'\\'+str(startpage)+'\\'      #保存在 C:\Users\kingking\Desktop\jiandan
    if not os.path.isdir(paths):               #将每个页面的图片分别存放在不同的文件夹
        os.makedirs(paths) 
    for imgurl in imglist:
        #print('正在下载 '+('{}').format(str(time.time())+imgurl[-9:])+'保存至'+path)	
		#打开imglist中保存的图片网址，并下载图片保存在本地，format格式化字符串
        urllib.request.urlretrieve('http:'+imgurl,('{}{}').format(paths,str(time.time())+imgurl[-9:]))     

def donwloadimg(page):
    url = 'http://jandan.net/ooxx/page-'+str(page)#此处链接可以换成别的网站，这就需要分析网站结构了
    print('正在爬取 '+url)
    html = getHtml(url)#获取该网址网页详细信息，得到的html就是网页的源代码	
    try:
        getImg(html)#从网页源代码中分析并下载保存图片
    except:
        pass
        #print('本图片下载失败，即将下载下一张图片')
#实现指定页面下载，从开始页面到结束页面
def donwload():
    global startpage
    global endpage
    startpage = int(startpage_entry.get())
    endpage = int(endpage_entry.get())
    p = startpage
    while startpage < endpage+1:
        donwloadimg(startpage)
        startpage += 1
    #print('从'+str(p)+'到'+str(endpage)+'的图片下载完毕')
	#下载完毕弹出提示消息
    messagebox.showinfo('骚年 注意节制！','从'+str(p)+'页到'+str(endpage)+'页的图片下载完毕')

#文件夹对话框，选择保存位置
def select_save_path():
    global path
    filename = askdirectory()
    path = filename
    #print(path)
	
#三个全局变量，默认保存路径，起始页面，结束页面
path = r'C:\Users\kingking\Desktop\jiandan'
startpage =1
endpage = 1
#下面是用tkinter写的界面，很简单，需要的话就做参考
root = Tk()
root.title('煎蛋网妹子图批量下载器')
root.iconbitmap('ic.ico')

imgframe = Frame(root)
imgframe.pack(side=LEFT)
photo = PhotoImage(file='jd.png')
imgLabel = Label(imgframe,image=photo, width = 120,height = 80)
imgLabel.grid(row=0,column=0,padx=1,pady=1)
Label(imgframe, text='http://jandan.net/').grid(row=1,column=0,padx=1,pady=1)

button_frame = Frame(root)
button_frame.pack(side=RIGHT)
startpage_entry = Entry(button_frame)
startpage_entry.grid(row=0,column=1,padx=3,pady=3)
startpage_entry_label = Label(button_frame,text='请输入开始爬取的页码')
startpage_entry_label.grid(row=0,column=0,padx=3,pady=3)
startpage_entry.insert(0,"1")
endpage_entry = Entry(button_frame)
endpage_entry.grid(row=1,column=1,padx=3,pady=3)
endpage_entry_label = Label(button_frame,text='请输入结束爬取的页码')
endpage_entry_label.grid(row=1,column=0,padx=3,pady=3)
endpage_entry.insert(0,"61")

Button_label = Label(button_frame,text='选择图片保存路径      ')
Button_label.grid(row=2,column=0,padx=3,pady=3)
Button_select_save_path = Button(button_frame, text='选择保存位置', command=select_save_path, width = 16,height = 1)
Button_select_save_path.grid(row=2,column=1,padx=3,pady=3)
DownloadImg = Button(button_frame, text='下载', command=donwload, width = 16,height = 1)
DownloadImg.grid(row=3,column=1,padx=3,pady=3)
mainloop()

