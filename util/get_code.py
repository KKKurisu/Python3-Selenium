#coding=utf-8
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
import time
class GetCode:
    def __init__(self,driver):
        self.driver = driver
    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        print(file_name)
        code_element = self.driver.find_element_by_id("getcode_num")
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width']+left
        height = code_element.size['height']+top
        im = Image.open(file_name)
        img = im.crop((left,top,right,height))
        img.save(file_name)
        time.sleep(1)

    #解析图片获取验证码
    def code_online(self,file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("https://route.showapi.com/1274-2", "274787", "1ea4e3d91ac3404da01b319403823a29")
        r.addFilePara("imgFile", file_name) #文件上传时设置
        res = r.post()
        time.sleep(1)
        text = res.json()['showapi_res_body']
        #print(text)
        code = text['texts']
        
        return code