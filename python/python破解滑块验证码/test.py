from selenium import webdriver


driver = webdriver.PhantomJS()


driver.get("https://account.ch.com/NonRegistrations-Regist")

driver.save_screenshot("reglist.png")
