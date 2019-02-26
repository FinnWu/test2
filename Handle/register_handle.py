#handle文件下都是操作层，写的是操作流程,我的理解就是你要输入用户名这里是要怎么去操作
from Page_test.register_page import RegisterPage#调用Page层，提供定位的元素信息
class RegisterHandle(object):
    def __init__(self):
        self.register_p = RegisterPage()
    #输入邮箱
    def send_user_email(self):
        pass

    #输入用户名
    def send_user_name(self):
        pass
    #输入密码
    def send_user_password(self):
        pass
    #输入验证码
    def send_code(self):
        pass
    #点击注册按钮
    def send_login_button(self):
        pass