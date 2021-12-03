from  selenium import webdriver
import time


EMAIL = '登录账户'
PASSWORD = '登录密码'

class CrackGeetest():
    def __init__(self):
        self.url = 'https://account.geetest.com/login'
        self.browser = webdriver.Chrome(executable_path=r"/Users/hayleygao/PycharmProjects/Data_Analysis/day120302/chromedriver")
        #设置显示等待时间
        time.sleep(3)


        self.email = EMAIL
        self.password = PASSWORD

    def crack(self):
        self.browser.get(self.url)



# 程序主入口
if __name__ == '__main__':
    crack = CrackGeetest()
    crack.crack()


