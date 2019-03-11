#读取页面的信息放到了page层，然后由handle去调用page层，为了给handle这层提供有哪些元素,
from Base.find_element import FindElement

class RegisterPage(object):
    def __init__(self,driver):
        self.fd = FindElement(driver)
    def get_email_element(self):#读取email的定位信息
        return self.fd.get_element("user_email")

    def get_name_element(self):
        return self.fd.get_element("user_name")

    def get_password_element(self):
        return self.fd.get_element("user_password")

    def get_code_element(self):
        return self.fd.get_element("user_code")

    def get_Login_button_element(self):
        return self.fd.get_element("user_button")
    def get_user_email_error(self):
        return self.fd.get_element("user_email_error")
    def get_user_name_error(self):
        return self.fd.get_element("user_name_error")

