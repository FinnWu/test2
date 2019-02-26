#business文件夹下的都是业务层，就是去操作我们的handle层
from Handle.register_handle import RegisterHandle
class RegisterBusiness(object):
    def __init__(self,driver):
        self.register_h = RegisterHandle(driver)
    def Login(self,email,name,password,code):
        self.register_h.send_user_email(email)
        if self.register_h.send_user_test("请输入有效的电子邮件地址"):
            print("pass")
            return True

