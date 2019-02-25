from selenium import webdriver
import random
import time

driver = webdriver.Chrome()
#浏览器初始化
def driver_init():
    driver.get('http://www.5itest.cn/register?goto=/')
    driver.maximize_window()
    driver.implicitly_wait(10)
#获取element信息
def get_element(id):
    element_id = driver.find_element_by_id(id)
    return element_id
#获取随机数
def get_range_user():
    user_info = ''.join(random.sample("1234567abcdefg",8))
    print(user_info)
    return user_info

def run_main():
    user_name_info = get_range_user()
    user_email = user_name_info+"@163.com"
    driver_init()
    get_element("register_email").send_keys(user_email)
    get_element("register_nickname").send_keys(user_name_info)
    get_element("register_password").send_keys("111111")
    time.sleep(5)
    driver.close()


run_main()