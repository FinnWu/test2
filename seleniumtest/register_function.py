from selenium import  webdriver
import random
import time
import sys
sys.path.append('D:/test2')
from seleniumtest.find_element import FindElement
class RegisterFunction(object):
    def __init__(self,url):
        self.driver = self.get_driver(url)
    #获取driver并且打开URL
    def get_driver(self,url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        return driver
    #输入用户信息
    def send_user_info(self,key,data):
        self.get_user_element(key).send_keys(data)#由下面get_user_element的方法获取到定位的元素，那么这里就直接调用获取的值，然后直接输入数据

    #定位元素信息
    def get_user_element(self,key):
        find_element = FindElement(self.driver)#调用find_element里面定位元素的方法
        user_element = find_element.get_element(key)#元素的值是什么
        return user_element
    #获取随机数
    def get_range_user(self):
        user_info = ''.join(random.sample("123456abcdegf",8))
        return user_info

    def main(self):
        user_name_info = self.get_range_user()
        user_mail = user_name_info+"@163.com"
        self.send_user_info("user_email",user_mail)
        self.send_user_info("user_name",user_name_info)
        self.send_user_info("user_password", '111111')
        self.send_user_info("user_yanzhenma",'1111')
        time.sleep(5)
        self.driver.close()

if __name__ == "__main__":
    register_function = RegisterFunction('http://www.5itest.cn/register')
    register_function.main()





