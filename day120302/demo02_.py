from  selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



EMAIL = '登录账户'
PASSWORD = '登录密码'

class CrackGeetest():
    def __init__(self):
        self.url = 'https://account.geetest.com/login'
        self.browser = webdriver.Chrome(executable_path=r"/Users/hayleygao/PycharmProjects/Data_Analysis/day120302/chromedriver")

        #设置显示等待时间
        time.sleep(2)
        self.email = EMAIL
        self.password = PASSWORD


    def get_geetest_button(self):
        ''' 获取初始验证按钮,return：按钮对象 '''
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_btn_click')))
        return button


    def open(self):
        ''' 打开网页输入用户名密码, return: None '''
        self.browser.get(self.url)
        time.sleep(2)
        print(self.browser.title)
        email = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="base"]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div/input')))
        password = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="base"]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[1]/input')))

        # email.click()

        time.sleep(1)
        email.send_keys(self.email)

        # password.click()
        password.send_keys(self.password)


    def crack(self):
        # 输入用户名密码
        self.open()
        # 点击验证按钮
        button = self.get_geetest_button()
        button.click()



# 程序主入口
if __name__ == '__main__':
    crack = CrackGeetest()
    crack.crack()


