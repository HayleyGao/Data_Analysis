from  PIL import  Image

# https://download.csdn.net/download/weixin_38548434/12865240?spm=1001.2101.3001.5697


# 获取图片指定像素点的像素


file_path=r'/Users/hayleygao/PycharmProjects/Data_Analysis/day120303/WechatIMG173.png'

def getPngPix(pngPath=file_path,pieIX=1,pieIY=1):
    img_src=Image.open(pngPath)
    img_src=img_src.convert('RGBA')
    str_strlist=img_src.load()
    data=str_strlist[pieIX,pieIY]
    img_src.close()
    return  data

print(getPngPix()) #(255, 255, 255, 255)
