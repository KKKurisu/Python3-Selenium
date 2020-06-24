#coding=utf-8
from selenium import webdriver
import time
import traceback
from selenium.webdriver.common.by import By
class BasePage:
    def __init__(self,driver,url='http://www.5itest.cn/register'):
        self.url = url
        self.driver = driver
        self.timeout = 20

    def find_element(self,*loc):
        '''
        查找元素
        '''
        return self.driver.find_element(*loc)
    
    def visit(self,url):
        '''
        打开url
        '''
        self.driver.get(url)
    
    def get_title(self):
        '''
        获取title
        '''
        title = self.driver.title
        return title
    
