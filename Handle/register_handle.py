#handle文件下都是操作层，写的是操作流程,我的理解就是你要输入用户名这里是要怎么去操作
from Page_test.register_page import RegisterPage#调用Page层，提供定位的元素信息
class RegisterHandle(object):
    def __init__(self,driver):
        self.register_p = RegisterPage(driver)
    #输入邮箱
    def send_user_email(self,email):
        self.register_p.get_email_element().send_keys(email)

    #输入用户名
    def send_user_name(self,name):
        self.register_p.get_name_element().send_keys(name)
    #输入密码
    def send_user_password(self,password):
        self.register_p.get_password_element().send_keys(password)
    #输入验证码
    def send_code(self,code):
        self.register_p.get_code_element().send_keys(code)
    #点击注册按钮
    def send_login_button(self,):
        self.register_p.get_Login_button_element().clcik()
    #获取文字信息
    def send_user_text(self,info,user_info):
        if info == 'user_email_error':
            self.register_p.get_email_element().get_attribute('vlaue')
        elif info == 'user_user_error':
            self.register_p.get_name_element().get_attribute('vlaue')