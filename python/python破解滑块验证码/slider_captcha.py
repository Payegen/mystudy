# Python破解滑块验证码
# 作者: Charles
# 公众号: python工程狮
import os
import re
import time
import Tracks
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


# 匹配原图
def match_source(image, source_path='./sources'):
	for source in sorted(os.listdir(source_path)):
		source_img = Image.open(os.path.join(source_path, source))
		# 根据自己电脑的实际情况调整
		pixel1 = image.getpixel((787, 281))
		pixel2 = source_img.getpixel((787, 292))
		if abs(pixel1[0]-pixel2[0]) < 5:
			return source_img
	return None


# 截取当前验证码图片
def capture_captcha(browser, savename='captcha.png'):
	'''
	captcha = WebDriverWait(browser, 60).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_img')))
	# location = captcha.location
	# size = captcha.size
	# top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size['width']
	# print('[INFO]: Captcha location - (top, bottom, left, right) -> ({}, {}, {}, {})'.format(top, bottom, left, right))
	time.sleep(1)
	left, top, right, bottom = 790, 280, 1100, 480
	screenshot = browser.get_screenshot_as_png()
	screenshot = Image.open(BytesIO(screenshot))
	screenshot.save('sd.png')
	captcha_img = screenshot.crop((left, top, right, bottom))
	captcha_img.save(savename)
	return savename
	'''
	WebDriverWait(browser, 60).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_img')))
	slider = browser.find_element_by_class_name('geetest_slider_button')
	ActionChains(browser).click_and_hold(slider).perform()
	ActionChains(browser).move_by_offset(xoffset=250, yoffset=0).perform()
	time.sleep(0.5)
	browser.save_screenshot(savename)
	ActionChains(browser).release(slider).perform()
	return savename


# 获得滑块对象
def get_slider(browser):
	slider = browser.find_element_by_class_name('geetest_slider_button')
	return slider


# 获得缺口偏移量
def get_gap_offset(image, source_img):
	# 根据自己电脑的实际情况调整
	for i in range(787, 1111):
		for j in range(292, 485):
			pixel1 = image.getpixel((i, j-11))
			pixel2 = source_img.getpixel((i, j))
			if abs(pixel1[0]-pixel2[0]) >= 50 and abs(pixel1[1]-pixel2[1]) >= 50 and abs(pixel1[2]-pixel2[2]) >= 50:
				return i - 793
	return None


# 移动滑块到缺口处
# 输入:
# 	-browser: webdriver.Chrome
# 	-slider: 滑块
# 	-tracks: 轨迹
def move_to_gap(browser, slider, tracks):
	ActionChains(browser).click_and_hold(slider).perform()
	for track in tracks:
		ActionChains(browser).move_by_offset(xoffset=track, yoffset=0).perform()
	ActionChains(browser).pause(0.5).release().perform()


# 破解滑块验证码
def crack_captcha(browser, t_len=12, func_kind=3):
	savename = capture_captcha(browser, savename='captcha.png')
	image = Image.open(savename)
	source_img = match_source(image, source_path='./sources')
	if source_img is None:
		print('[Error]: Fail to match sources...')
		exit(-1)
	distance = get_gap_offset(image, source_img)
	if distance is None:
		print('[Error]: Fail to match sources...')
		exit(-1)
	time.sleep(2)
	slider = get_slider(browser)
	# tracks = Tracks.get_tracks(distance*0.78)
	tracks = Tracks.get_tracks(int(distance*0.8), t_len, func_kind)
	time.sleep(0.5)
	move_to_gap(browser, slider, tracks)
	time.sleep(2)
	browser.close()


# 主函数
def main(url):
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--start-maximized')
	browser = webdriver.Chrome(
		executable_path = './driver/chromedriver.exe',
		chrome_options = chrome_options
		)
	browser.get(url)
	WebDriverWait(browser, 60).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div[MNIST_data-target='account-login']")))
	# 切换到邮箱注册
	email_register = browser.find_element_by_css_selector("div[MNIST_data-target='account-login']")
	email_register.click()
	WebDriverWait(browser, 60).until(expected_conditions.visibility_of_element_located((By.ID, "emailRegist")))
	# 随便填个账号密码
	username = browser.find_element_by_name("EmailInput")
	username.send_keys('2237040591@qq.com')
	password = browser.find_element_by_name("EmailPasswordInput")
	password.send_keys('abcd123456')
	password_confirm = browser.find_element_by_name("EmailPasswordConfirm")
	password_confirm.send_keys('abcd123456')
	# 保证响应
	time.sleep(1)
	# 点击注册按钮
	register_button = browser.find_element_by_id("emailRegist")
	register_button.click()
	crack_captcha(browser)


if __name__ == '__main__':
	url = 'https://account.ch.com/NonRegistrations-Regist'
	main(url)