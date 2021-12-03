from  PIL import  Image
from  PIL import  ImageFilter


im=Image.open("/Users/hayleygao/PycharmProjects/Data_Analysis/day120303/WechatIMG173.png",mode='r')

print(im)

print(im.size,im.format,im.mode)

# 一般来说’L’(luminance)表示灰度图像,’RGB’表示真彩图像,’CMYK’表示预先压缩的图像。
# 旦你得到了打开的Image对象之后，就可以使用其众多的方法对图像进行处理了，比如使用im.show()可以展示上面得到的图像。


# 重新保存成为jpg格式
# save(filename,format)(保存指定格式的图像)
# im.save("/Users/hayleygao/PycharmProjects/Data_Analysis/day120303/WechatIMG173.jpg")



#  thumbnail(size,resample)(创建缩略图)
im.thumbnail((50,50),resample=Image.BICUBIC)
# 第一个参数是指定的缩略图的大小，第二个是采样的，有Image.BICUBIC，PIL.Image.LANCZOS，PIL.Image.BILINEAR，PIL.Image.NEAREST这四种采样方法。默认是Image.BICUBIC。
# im.show()


# 裁剪
# crop(box)(裁剪矩形区域)


#
#convert方法可以改变图像的mode,一般是在’RGB’(真彩图)、’L’(灰度图)、’CMYK’(压缩图)之间转换。

# 转换成为灰度图，然后从灰度图转换回"RGB图"
im_L=im.convert("L")
# im_L.show()
im_rgb=im_L.convert('RGB')
# im_rgb.show()

print(im_L.mode)
print(im_rgb.mode)



# filter 过滤方法
# ilter方法可以将一些过滤器操作应用于原始图像，比如模糊操作，查找边、角点操作等
# BLUR(模糊操作),GaussianBlur(高斯模糊),MedianFilter(中值过滤器)，FIND_EDGES(查找边)等

image_file_02=r"/Users/hayleygao/PycharmProjects/Data_Analysis/day120303/image02.png"

image_file_03=r"/Users/hayleygao/PycharmProjects/Data_Analysis/day120303/image03.png"


image02=Image.open(image_file_02)
image03=Image.open(image_file_03)

# BLUR(模糊操作)
im_blur=image03.filter(ImageFilter.BLUR)
im_blur.show()











