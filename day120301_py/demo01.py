from  PIL import  Image
import  pytesseract  # 作用和tesserocr相似。
import  tesserocr


# 首先需要下载 tesseract，它为 tesserocr
# https://blog.csdn.net/ltf201834/article/details/85011710
# https://www.cnblogs.com/Jimc/p/9772930.html


image_file=r"/Users/hayleygao/PycharmProjects/Data_Analysis/day120301_py/images/WechatIMG172.png"

im=Image.open(image_file)
print(im)
# <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=214x102 at 0x11EDF4910>
print('-------------')

text1=tesserocr.image_to_text(im)
print(text1)







