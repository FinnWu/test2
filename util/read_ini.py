import configparser
# import sys
# sys.path.append(r"D://test2")
class ReadIni(object):
    def __init__(self,file_name=None,node=None):#构建一个函数，判断一个对象，可以为空或者不为空，如果为空的时候，就去给他赋予一个值

        if file_name == None:
            file_name = "D://test2//config//LocaElement.ini"
        if node == None:
            self.node = "RegisterElement"
        else:
            self.node = node
        self.cf = self.load_ini(file_name)
    #加载文件
    def load_ini(self,file_name):
        cf = configparser.ConfigParser()  # 使用这个模块
        cf.read(file_name,encoding="utf-8")
        return cf
    #获取value的值
    def get_value(self,key):
        data = self.cf.get(self.node,key)
        return data

if __name__ == '__main__':
    read_init = ReadIni()
    print(read_init.get_value("user_name"))