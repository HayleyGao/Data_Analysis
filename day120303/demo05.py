from  PIL import  Image



# 方法load()返回一个用于读取和修改像素的像素访问对象.
image_file_01=r"/Users/hayleygao/PycharmProjects/Data_Analysis/day120303/image04.png"

im1=Image.open(image_file_01)

im_load=im1.load() # 加载图像

print(im_load)
# <PixelAccess object at 0x101682810>

print(im_load[50,30])
#(220, 182, 178, 255)  # 为什么会有四个值？RGB不是只有三个？







