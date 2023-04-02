from selenium import webdriver
import time
import pandas as pd

url = 'https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_0d2b00de9e7645e4a464acdba040714a'

# 创建驱动器
driver = webdriver.Chrome
# driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

driver.get(url)
driver.find_element_by_xpath('//*[@id="key"]').send_keys("手机")  # 在搜索框搜索手机
driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button/i').click()  # 点击搜索

time.sleep(2)  # 睡眠一会，否则会读取不到数据

driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')  # 将页面拉到底部

time.sleep(2)  # 拉取数据需要睡一会

# 注意：是使用elements获取全部数据，不是使用element
phone_list = driver.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')  # 获取当前页所有手机信息

price = []  # 手机价格
phone_name = []  # 手机名称
praise = []  # 评价条数
shop_name = []  # 店铺名

# 打印当前页的所有手机信息
for phone in phone_list:
    # print(phone.text)
    phone_info = str(phone.text).split('\n')
    # print(phone_info)
    price.append(phone_info[0])
    phone_name.append(phone_info[1])
    praise.append(phone_info[2])
    shop_name.append(phone_info[3])
    # print('-------------------------------------------------')

# 存储手机信息
phone_dict = {'手机型号': phone_name,
              '价格': price,
              '评价条数': praise,
              '店铺名': shop_name
              }
phone = pd.DataFrame(phone_dict)
print(phone)
phone.to_csv("京东手机数据表.csv",index=False)

time.sleep(2)
driver.quit()  # 关闭网页
