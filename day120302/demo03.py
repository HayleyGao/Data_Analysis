from  selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By





chrome=webdriver.Chrome(executable_path=r"/Users/hayleygao/PycharmProjects/Data_Analysis/day120302/chromedriver")
chrome.maximize_window()


url="https://auth.geetest.com/login/"
chrome.get(url)
print(chrome.title)



email_input=chrome.find_element_by_xpath('//*[@id="base"]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div/input')

pwd_input=chrome.find_element_by_xpath('//*[@id="base"]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[1]/input')



# email_input.click()
email_input.send_keys("email")

# pwd_input.click()
pwd_input.send_keys("pwd")


geetest_btn=chrome.find_element_by_xpath('//*[@id="captchaIdLogin"]/div/div[1]/div[1]')
geetest_btn.click()

login_btn=chrome.find_element_by_xpath('//*[@id="base"]/div[2]/div/div[2]/div[3]/div/form/div[5]')

time.sleep(1)


