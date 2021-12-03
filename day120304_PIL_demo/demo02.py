from  PIL import  Image

# https://zhuanlan.zhihu.com/p/91785926



BORDER = 6
INIT_LEFT = 60

class CrackGeetest():
    def get_gap(self, image1, image2):
        ''' 获取缺口偏移量, 参数：image1不带缺口图片、image2带缺口图片。返回偏移量 '''
        left = 65
        for i in range(left, image1.size[0]):  #image1.size[0],（x的坐标轴。）
            for j in range(image1.size[1]):
                if not self.is_pixel_equal(image1, image2, i, j):
                    left = i
                    return left
        return left

    def is_pixel_equal(self, image1, image2, x, y):
        '''
        判断两个像素是否相同
        :param image1: 图片1
        :param image2: 图片2
        :param x: 位置x
        :param y: 位置y
        :return: 像素是否相同
        '''
        # 取两个图片的像素点（R、G、B）
        pixel1 = image1.load()[x, y]
        pixel2 = image2.load()[x, y]
        threshold = 60
        if abs(pixel1[0]-pixel2[0])<threshold and abs(pixel1[1]-pixel2[1])<threshold and abs(pixel1[2]-pixel2[2])<threshold: # RGB模式，所以有3个值。但是为什么要设置这个阈值。
            return True
        else:
            return False






if __name__=="__main__":
    crack=CrackGeetest()

    image1=r"/Users/hayleygao/PycharmProjects/Data_Analysis/day120304_PIL_demo/images/image01.jpeg"
    image2=r"/Users/hayleygao/PycharmProjects/Data_Analysis/day120304_PIL_demo/images/image02.jpeg"
    # 获取缺口位置
    gap = crack.get_gap(image1, image2)
    print('缺口位置', gap)



