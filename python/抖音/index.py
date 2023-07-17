import os
from PIL import Image

def screen():
    # 截图保存在手机上          -p path 路径
    os.system('adb shell screencap -p /sdcard/screen.png')
    # 传到电脑上
    os.system('adb pull /sdcard/screen.png')


def getDistance():
    # 读取图片
    image = Image.open('screen.png')
    # height = image.size
    width,height = image.size
    # print(height,width)
    for i in range(915,916):
        for j in range(0,height):
            if image.getpixel((i,j))[:3] == (254,119,146):
                yield j

if __name__ == '__main__':
    for _ in range(10):
        # screen()
        xPosition = getDistance()
        for x in xPosition:
            print(x)