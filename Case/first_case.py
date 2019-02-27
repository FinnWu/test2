#这个文件下是测试用例层，就是去执行操作
from business.register_business import RegisterBusiness
class FristCase(object):
    def __init__(self,driver):
        self.login = RegisterBusiness(driver)

    def test_email_error(self):
        email_error = self.login.Login_email_error('123','1133')
        if email_error == True:
            print('pass')

    def test_name_error(self):
        name_error = self.login.Login_name_error("qwe@qq.com",'ss')
        if name_error == True:
            print('pass')



