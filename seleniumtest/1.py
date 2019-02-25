from selenium import  webdriver
a = webdriver.Firefox()
a.get('https://www.baidu.com')
a.close()