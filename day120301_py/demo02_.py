import tesserocr
from PIL import Image

image = Image.open(r'/Users/hayleygao/PycharmProjects/Data_Analysis/day120301_py/images/WechatIMG172.png')
result = tesserocr.image_to_text(image)
print(result)


