from selenium import webdriver
import time

url = "https://www.baidu.com/"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)
driver.quit()