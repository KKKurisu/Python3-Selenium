#coding=utf-8
from selenium import webdriver
#from lib.pages.base_page import BasePage

def before_all(context):
    context.driver = webdriver.Chrome()
    #context.driver.get('http://www.5itest.cn/register')

def after_all(context):
    context.driver.close()