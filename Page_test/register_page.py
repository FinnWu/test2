#读取页面的信息放到了page层，然后由handle去调用page层，为了给handle这层提供有哪些元素,
from Base.find_element import FindElement

class RegisterPage(object):
    def __init__(self,driver):
        self.fd = FindElement(driver)
    def get_email_element(self):#读取email的定位信息
        return self.fd.get_element("user_email")
