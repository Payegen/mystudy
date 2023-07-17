import cv2
# https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html

# 加载一张图片
image = cv2.imread("./2.jpg")
# 创建一个窗口
cv2.namedWindow('image')
# 实时监听鼠标点击
def draw(event,x,y,flags,param):
    # 鼠标按下
    if event == cv2.EVENT_LBUTTONDOWN:
        drwaMosaic(x,y)
        # print('鼠标按下')
    # elif event == cv2.EVENT_LBUTTONUP:
    #     print('鼠标抬起')
    # elif event == cv2.EVENT_MOUSEMOVE:
    #     print('鼠标滑动')


# 马赛克->算法问题
# x和y 表示当前鼠标点击屏幕位置
# size表示马赛克点有多大
def drwaMosaic(x,y,size = 20):
    for i in range(size):
        for j in range(size):
            image[x+i][y+j] = image[x][y]


cv2.setMouseCallback('image', draw)
# 显示窗口
# cv2.imshow('image',image)
#


while(1):
    cv2.imshow('image',image)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()