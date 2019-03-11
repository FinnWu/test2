#这个文件下是测试用例层，就是去执行操作
import sys
sys.path.append("D:\\test2")
from business.register_business import RegisterBusiness
import time
from selenium import webdriver
import unittest
class FirstCase(unittest.TestCase):
    def setUp(self):
        print()
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.login = RegisterBusiness(self.driver)
    def tearDown(self):
        self.driver.close()
        print()
    

    def test_email_error(self):
        email_error = self.login.Login_email_error("123","123")
        if email_error == True:
            print('执行失败')
        else:
            print('执行成功')



    def test_name_error(self):
        name_error = self.login.Login_name_error("qwe@qq.com",'ss')
        if name_error == True:
            print('执行失败')
        else:
            print('执行成功')
        time.sleep(5)



if __name__ == "__main__":
    unittest.main()
    




