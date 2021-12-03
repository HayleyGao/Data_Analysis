from  selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from  PIL import  Image
from io import BytesIO


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
        button = self.browser.find_element(By.CLASS_NAME, 'geetest_btn_click')
        return button


    def open(self):
        ''' 打开网页输入用户名密码, return: None '''
        self.browser.get(self.url)
        time.sleep(2)
        print(self.browser.title)
        email = self.browser.find_element(By.XPATH, '//*[@id="base"]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div/input')
        password = self.browser.find_element(By.XPATH, '//*[@id="base"]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[1]/input')

        # email.click()
        time.sleep(1)
        email.send_keys(self.email)

        # password.click()
        password.send_keys(self.password)


    # part02 获取并储存有无缺口的两张图片(有缺口和无缺口)
    def get_position(self):
        ''' 获取验证码位置, return: 验证码位置(元组) '''
        img = self.browser.find_element(By.XPATH, 'geetest_canvas_img')
        time.sleep(2)
        location = img.location
        size = img.size
        # 获取坐标
        top,bottom,left,right = location['y'],location['y']+size['height'],location['x'],location['x']+size['width']
        return (top, bottom, left, right)


    def get_screenshot(self):
        ''' 获取网页截图, return: 截图对象 '''
        #浏览器截屏
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot)) # BytesIO
        return screenshot


    def get_geetest_image(self, name='captcha.png'):
        ''' 获取验证码图片, return: 图片对象 '''
        top, bottom, left, right = self.get_position()
        print('验证码位置', top, bottom, left, right)
        screenshot = self.get_screenshot()
        #从网页截屏图片中裁剪处理验证图片
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save(name)
        return captcha

    def get_slider(self):
        ''' 获取滑块, return: 滑块对象 '''
        slider = self.browser.find_element((By.XPATH, 'geetest_slider_button'))
        return slider





    def crack(self):

        # part01
        # 输入用户名密码
        self.open()
        # 点击验证按钮
        button = self.get_geetest_button()
        button.click()


        # part02
        # 获取验证码图片
        image1 = self.get_geetest_image('captcha1.png')
        # 点按呼出缺口
        slider = self.get_slider()
        slider.click()
        # 获取带缺口的验证码图片
        image2 = self.get_geetest_image('captcha2.png')





# 程序主入口
if __name__ == '__main__':
    crack = CrackGeetest()
    crack.crack()


