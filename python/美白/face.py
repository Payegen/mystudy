# @ Time    : 2019/2/27 13:43
# @ Author  : JuRan
import keyboard
from PIL import ImageGrab   # pip install pillow
import time

from demo1 import face

def screen():
    # print("代码执行到这里了-开始截图")
    # 开始截图  阻塞程序运行
    keyboard.wait(hotkey='ctrl+alt+a')
    # print("我按了ctrl+alt+a键")
    keyboard.wait(hotkey='enter')
    # print("我按了enter键-结束截图")
    # 暂停程序
    time.sleep(0.5)
    # 读取剪切板里面的图片
    image = ImageGrab.grabclipboard()
    # 保存图片
    image.save('screen.png')

for _ in range(10):
    screen()
    # print("-"*50)
    print(face('./screen.png'))
    # print("-" * 50)