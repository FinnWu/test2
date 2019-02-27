from selenium import  webdriver
import random
import sys
sys.path.append('D:/test2')
from Base.find_element import FindElement

class RegisterFunction(object):
    def __init__(self,url,i):
        self.driver = self.get_driver(url,i)
    #获取driver并且打开URL
    def get_driver(self,url,i):
        if  i == 1:#使用循环判断启动多个浏览器，把i参数化
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
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
        self.send_user_info("user_code",'1111')
        self.get_user_element("user_button").click()#点击定位信息才知道验证码是否正确
        user_yanzhenme_error = self.get_user_element("user_code_error")
        if user_yanzhenme_error == None:
            print('pass')
        else:
            self.driver.save_screenshot("D:/test2/Screenshot/"+user_name_info+'.png')#错误时，截取屏幕信息


        self.driver.close()

if __name__ == "__main__":
    for i in range(3):

        register_function = RegisterFunction('http://www.5itest.cn/register',i)
        register_function.main()





