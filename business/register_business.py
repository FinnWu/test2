#business文件夹下的都是业务层，就是去操作我们的handle层
from Handle.register_handle import RegisterHandle
class RegisterBusiness(object):
    def __init__(self,driver):
        self.register_h = RegisterHandle(driver)
    #用户名错误
    def Login_email_error(self,email,name):
        self.register_h.send_user_email(email)
        self.register_h.send_user_name(name)
        if self.register_h.send_user_text("user_email_error","请输入有效的电子邮件地址") == None:
            print("不通过")
            return True
        else:
            return False

    def Login_name_error(self,email,name):
        self.register_h.send_user_email(email)
        self.register_h.send_user_name(name)
        if self.register_h.send_user_text("user_name_error","字符长度必须大于等于4，一个中文字算2个字符") == None:
            print('名字校验错误')
            return True
        else:
            return False



