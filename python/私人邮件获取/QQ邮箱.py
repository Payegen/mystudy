from selenium import webdriver
import time
import User


# 打开浏览器  executable_path='./driver/chromedriver.exe'
wd = webdriver.Chrome()
# 设置窗口大小
# wd.set_window_size(1280,800)
wd.maximize_window()
# 输入网址
wd.get('http://www.baidu.com')
# 截图
wd.save_screenshot("baidu.png")
# 找到输入框
kw = wd.find_element_by_id('kw')
# 在输入框中输入酒店
kw.send_keys("酒店")
# 点击百度一下
wd.find_element_by_id('su').click()
time.sleep(3)
wd.quit()


wd = webdriver.Chrome(executable_path='./driver/chromedriver.exe')
# 隐式等待
#到了一定的时间发现元素还没有加载，则继续等待我们指定的时间，如果超过了我们指定的时间还没有加载就会抛出异常，如果没有需要等待的时候就已经加载完毕就会立即执行
wd.implicitly_wait(10)
wd.get("https://mail.qq.com")
wd.set_window_size(1280,1020)
login_frame = wd.find_element_by_id('login_frame')
# 切换iframe
wd.switch_to.frame(login_frame)

wd.find_element_by_id('switcher_plogin').click()

wd.find_element_by_id('u').send_keys(User.username)
wd.find_element_by_id('p').send_keys(User.password)

wd.find_element_by_id('login_button').click()

# 点击收信
# 切换到收信iframe的框架里
wd.find_element_by_id('readmailbtn_link').click()
main_frame = wd.find_element_by_id('mainFrame')
wd.switch_to.frame(main_frame)

# class 不可以获取中间有空格的  可以取其中唯一一个
# email = wd.find_element_by_class_name('i M')
email = wd.find_elements_by_css_selector('.toarea .F, .toarea .M')

email_count = len(email)
for i in range(email_count):
    # accountNameWithIcon
    # email_ele = wd.find_element_by_class_name('accountNameWithIcon').click()
    email_ele = wd.find_elements_by_css_selector('.toarea .F, .toarea .M')[i]
    time.sleep(1)
    email_ele.click()
    # time.sleep(2)
    # 主题
    subject = wd.find_element_by_id('subject').text
    # 内容
    # content = wd.find_element_by_id('mailContentContainer').text
    # content = wd.find_element_by_id('contentDiv0').text
    print(subject)
    # print(subject,content)
    # 返回  btn_gray btn_space btn_back left
    wd.find_element_by_class_name('btn_back').click()
    # print(email_ele)

wd.quit()
# print(email)

