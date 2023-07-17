import pygame

SCREEN_WIDTH = 1000  # 窗口的宽度
SCREEN_HEIGHT = 650 # 窗口的高度
FREQUENCE = 50 # 频率

FONT_NAME = "corbel"
# 字体大小
FONT_SIZE = 25
from random import randint
import random

# 代码下落速度
LOW_SPEED = 5
HIGH_SPEED = 10

# 随机颜色
def randomcolor():
    # 转换颜色
    return (randint(0,255),randint(0,255),randint(0,255))

# 随机速度
def randomspeed():
    return randint(LOW_SPEED, HIGH_SPEED)

# 随机名字
def randomoname():
    # 序列
    array = ["T","o","n","y"]
    # 随机选取一个元素
    return random.choice(array)


class Word(pygame.sprite.Sprite):
	def __init__(self, bornposition):
		pygame.sprite.Sprite.__init__(self)
		self.value = randomvalue()
		# 加载系统默认字体
		self.font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
		# 传输到屏幕
		self.img = self.font.render(str(self.value), True, randomcolor())
		self.speed = randomspeed()
		# 获取大小 设置速度
		self.rect = self.img.get_rect()
		# 设置显示的位置为左上角
		self.rect.topleft = bornposition

	def update(self):
		# 将对象进行移动
		self.rect = self.rect.move(0, self.speed)
		# 如果移动太远 大于 窗口高度
		if self.rect.top > SCREEN_HEIGHT:
			# 删除
			self.kill()


# 初始化
pygame.init()
# 设置窗口组件大小及位置
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
# 窗口标题
pygame.display.set_caption("逻辑Tony的黑客帝国 ^_^ ")
# 创建计时器对象 -> 可以控制游戏循环的频率
clock = pygame.time.Clock()
# 精灵 -> 可以看成是一个容器
group = pygame.sprite.Group()
group_count = SCREEN_WIDTH // FONT_SIZE
# 循环 -> 意味着游戏的正式开始！也意味着让程序长时间停留至界面
while True :
	# 指定循环频率 -> 每秒循环50次
    time = clock.tick(FREQUENCE)
	# 监听用户事件
    for event in pygame.event.get() :
		# 判断用户是否点击了关闭按钮
		if event.type == QUIT:
			# 退出
			pygame.quit()
			# 终止当前正在执行的Python程序
			exit()
	# 更新屏幕显示
    pygame.display.update()

for i in range(0, group_count):
	group.add(Word((i * FONT_SIZE, -FONT_SIZE)))
	group.update()
	# 绘制帧
	group.draw(screen)

