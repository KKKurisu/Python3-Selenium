from PIL import Image
from util.ShowapiRequest import ShowapiRequest
import time




file_name=r"D:/1/test001.jpg"
r = ShowapiRequest("https://route.showapi.com/1274-2","274787","1ea4e3d91ac3404da01b319403823a29" )
r.addFilePara("imgFile", "D:/1/test001.png") #文件上传时设置
res = r.post()
time.sleep(1)
print(res)
text = res.text
print(text)
code = text['remark']
print(code)