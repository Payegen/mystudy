# @ Time    : 2019/2/28 16:15
# @ Author  : JuRan

import cv2

# 加载一张图片
image = cv2.imread('./2.jpg')
# 创建一个窗口
cv2.namedWindow('image')
# 监听鼠标状态的监听
def draw(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('鼠标按下')
    elif event == cv2.EVENT_MOUSEMOVE:
        print('鼠标移动')
    elif event == cv2.EVENT_LBUTTONUP:
        print('鼠标抬起')

# 监听鼠标回调事件
cv2.setMouseCallback('image',draw)

# 展示窗口
cv2.imshow('image',image)

# 窗口等待
cv2.waitKey(0)

# 销毁窗口
cv2.destroyAllWindows()


