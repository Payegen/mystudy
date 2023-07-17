import pywifi
from pywifi import const    # 引用一些定义

# 判断是否有无限网卡
def gic():
    # 创建一个无线对象
    wifi = pywifi.PyWiFi()
    # print(wifi)
    # 获取第一个无线网卡
    ifaces = wifi.interfaces()[0]
    # print(ifaces)
    # 打印网卡的名
    print(ifaces.name())
    # 打印网卡状态    已连接 4
    # print(ifaces.status())
    # 常数 pywifi里面定义好的
    if ifaces.status() in [const.IFACE_CONNECTED,const.IFACE_INACTIVE]:
        print("已连接")
    else:
        print("未连接")

# gic()

# 扫描附近WiFi
def bies():
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    # 扫描WiFi
    ifaces.scan()
    # 获取扫描结果
    bessis = ifaces.scan_results()
    print(bessis)
    for data in bessis:
        # 输出WiFi名称
        print(data.ssid)

# bies()
