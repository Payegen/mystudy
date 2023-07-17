# 视频转字符动画
import os
import cv2
import sys
import time
import ctypes
import subprocess
import numpy as np


# 暗蓝色
FOREGROUND_DARKBLUE = 0x01
# 暗绿色
FOREGROUND_DARKGREEN = 0x02
# 暗天蓝色
FOREGROUND_DARKSKYBLUE = 0x03
# 暗红色
FOREGROUND_DARKRED = 0x04
# 暗粉红色
FOREGROUND_DARKPINK = 0x05
# 暗黄色
FOREGROUND_DARKYELLOW = 0x06
# 暗白色
FOREGROUND_DARKWHITE = 0x07
# 暗灰色
FOREGROUND_DARKGRAY = 0x08
# 蓝色
FOREGROUND_BLUE = 0x09
# 绿色
FOREGROUND_GREEN = 0x0a
# 天蓝色
FOREGROUND_SKYBLUE = 0x0b
# 红色
FOREGROUND_RED = 0x0c
# 粉红色
FOREGROUND_PINK = 0x0d
# 黄色
FOREGROUND_YELLOW = 0x0e
# 白色
FOREGROUND_WHITE = 0x0f
# 上面颜色对应的RGB值
cmd_colors = {
				'FOREGROUND_DARKBLUE': [FOREGROUND_DARKBLUE, (0, 0, 139)],
				'FOREGROUND_DARKGREEN': [FOREGROUND_DARKGREEN, (0, 100, 0)],
				'FOREGROUND_DARKSKYBLUE': [FOREGROUND_DARKSKYBLUE, (2, 142, 185)],
				'FOREGROUND_DARKRED': [FOREGROUND_DARKRED, (139, 0, 0)],
				'FOREGROUND_DARKPINK': [FOREGROUND_DARKPINK, (231, 84, 128)],
				'FOREGROUND_DARKYELLOW': [FOREGROUND_DARKYELLOW, (204, 204, 0)],
				'FOREGROUND_DARKWHITE': [FOREGROUND_DARKWHITE, (255, 250, 250)],
				'FOREGROUND_DARKGRAY': [FOREGROUND_DARKGRAY, (169, 169, 169)],
				'FOREGROUND_BLUE': [FOREGROUND_BLUE, (0, 0, 255)],
				'FOREGROUND_GREEN': [FOREGROUND_GREEN, (0, 128, 0)],
				'FOREGROUND_SKYBLUE': [FOREGROUND_SKYBLUE, (135, 206, 235)],
				'FOREGROUND_RED': [FOREGROUND_RED, (255, 0, 0)],
				'FOREGROUND_PINK': [FOREGROUND_PINK, (255, 192, 203)],
				'FOREGROUND_YELLOW': [FOREGROUND_YELLOW, (255, 255, 0)],
				'FOREGROUND_WHITE': [FOREGROUND_WHITE, (255, 255, 255)]
			}
CHARS = " .,-'`:!1+*abcdefghijklmnopqrstuvwxyz<>()\/{}[]?234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ%&@#$"


'''
Function:
	视频转图片
Input:
	-videopath: 视频路径
	-size: 指定图片大小
	-interval: 视频每interval帧取一帧
Return:
	-img_list: 图像列表
'''
def video2imgs(videopath, size, interval=1):
	img_list = list()
	capture = cv2.VideoCapture(videopath)
	i = -1
	while capture.isOpened():
		i += 1
		ret, frame = capture.read()
		if ret:
			if i % interval == 0:
				# frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
				img = cv2.resize(frame, size, interpolation=cv2.INTER_AREA)
				img_list.append(img)
		else:
			break
	capture.release()
	return img_list


'''
# 根据距离将图片的RGB值转为Windows-CMD窗口支持的颜色
def RGB2Cmdcolor(color):
	cmd_color = None
	min_distance = 1e6
	for key, value in cmd_colors.items():
		distance = np.square(np.array(color) - np.array(value[1])).sum()
		if distance < min_distance:
			min_distance = distance
			cmd_color = value[0]
	return cmd_color
'''


'''
Function:
	图像转字符画
Input:
	-img(np.array): 图像
Return:
	-img_chars: 像素点对应的字符集合
'''
def img2chars(img):
	img_chars = []
	height, width, channel = img.shape
	for row in range(height):
		line = ""
		for col in range(width):
			percent = int(np.array(img[row][col]).sum() / 3) / 255
			char_idx = int(percent * (len(CHARS) - 1))
			line += CHARS[char_idx] + ' '
		img_chars.append(line)
	return img_chars


'''
Function:
	视频转字符画s
Input:
	-imgs: 视频里捕获的所有图片
Return:
	-video_chars: img_chars的集合
'''
def imgs2chars(imgs):
	video_chars = []
	for img in imgs:
		video_chars.append(img2chars(img))
	return video_chars


'''
Function:
	播放字符画s
Input:
	-video_chars: imgs2chars中获取的video_chars
	-iscmd(bool): 是否在Windows的cmd窗口播放
	-color: 颜色选择, cmd中有效
'''
def play(video_chars, color=None, iscmd=True):
	if color and iscmd:
		STD_OUTPUT_HANDLE = -11
		std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
		color_choice = None
		if color.isdigit():
			color_choice = list(cmd_colors.values())[int(color)][0]
		else:
			color_choice = cmd_colors.get(color)[0]
		if color_choice is not None:
			_ = ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, color_choice)
	width, height = len(video_chars[0][0]), len(video_chars[0])
	for img_chars in video_chars:
		for row in range(height):
			print(img_chars[row])
		time.sleep(1/24)
		if iscmd:
			os.system('cls')
		else:
			subprocess.call("clear")


# 主函数
def main(videopath, color=None, iscmd=True):
	imgs = video2imgs(videopath=videopath, size=(64, 48), interval=1)
	video_chars = imgs2chars(imgs)
	input("[INFO]: Complete Pre-processing! Enter <enter> button to start to play...")
	if iscmd:
		os.system('cls')
	else:
		subprocess.call("clear")
	play(video_chars, color=color, iscmd=True)


if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file', help='Video file.')
	parser.add_argument('-c', '--color', help='Color for playing.')
	args = parser.parse_args()
	main(args.file, color=args.color)