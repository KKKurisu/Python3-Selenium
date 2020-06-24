#coding=utf-8
from features.lib.pages.base_page import *
from selenium.webdriver.common.by import By
class RegisterPage(BasePage):
    def __init__(self,context):
        super(RegisterPage,self).__init__(context.driver)
    
    def send_register(self):
        #user_email = (By.ID,"register_email")
        self.find_element(By.ID,'register_email').send_keys("test@qq.com")
