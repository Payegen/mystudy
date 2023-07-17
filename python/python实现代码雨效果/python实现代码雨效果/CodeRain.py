import sys
import random
import pygame
from pygame.locals import *


# 屏幕大小
WIDTH = 800
HEIGHT = 600
# 下落速度范围
SPEED = [15, 30]
# 字母大小范围
SIZE = [5, 30]
# CODE长度范围
LEN = [1, 8]


# 随机生成一个颜色
def randomColor():
	return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


# 随机生成一个速度
def randomSpeed():
	return random.randint(SPEED[0], SPEED[1])


# 随机生成一个大小
def randomSize():
	return random.randint(SIZE[0], SIZE[1])


# 随机生成一个长度
def randomLen():
	return random.randint(LEN[0], LEN[1])


# 随机生成一个位置
def randomPos():
	return (random.randint(0, WIDTH), -20)


# 随机生成一个字符串
def randomCode():
	return random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890')


# 定义代码精灵类
class Code(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.font = pygame.font.Font('./font.ttf', randomSize())	# 随机字体大小
		self.speed = randomSpeed()			# 随机速度
		self.code = self.getCode()			# 随机长度
		self.image = self.font.render(self.code, True, randomColor())	# 使用已有的文本创建一个位图image，返回值为一个image  随机颜色
		self.image = pygame.transform.rotate(self.image, random.randint(87, 93))	# 讲图像随机旋转角度
		self.rect = self.image.get_rect()
		self.rect.topleft = randomPos()		# 随机位置

	def getCode(self):
		length = randomLen()
		code = ''
		for i in range(length):
			code += randomCode()
		return code
	def update(self):
		self.rect = self.rect.move(0, self.speed)
		if self.rect.top > HEIGHT:
			self.kill()


pygame.init()			# 初始函数，使用pygame的第一步
screen = pygame.display.set_mode((WIDTH, HEIGHT))	#生成主屏幕screen；第一个参数是屏幕大小
pygame.display.set_caption('Code Rain-居然')	# 窗口命名

clock = pygame.time.Clock()					# 初始化一个clock对象
codesGroup = pygame.sprite.Group()			# 精灵组，一个简单的实体容器
while True:
	clock.tick(24)							# 控制游戏绘制的最大帧率为30
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit(0)
	# screen.fill((1, 1, 1))					# 填充
	screen.fill((0, 0, 0))						# 填充背景颜色

	codeobject = Code()
	codesGroup.add(codeobject)				# 添加精灵对象
	codesGroup.update()
	codesGroup.draw(screen)
	pygame.display.update()