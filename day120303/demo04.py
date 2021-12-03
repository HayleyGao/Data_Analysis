from  PIL import  Image



# 方法load()返回一个用于读取和修改像素的像素访问对象.
image_file_01=r"/Users/hayleygao/PycharmProjects/Data_Analysis/day120303/image01.jpeg"

im1=Image.open(image_file_01)

pix=im1.load() # 加载图像

print(pix)
# <PixelAccess object at 0x101682810>

print(pix[50,50])
# (176, 231, 130)





