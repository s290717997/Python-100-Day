"""
图像裁剪
这个没有工作，不知道为什么，准备用opencv的库来处理图像了，
所以这个库就不研究了
"""

from PIL import Image

image = Image.open('C:\\Users\\Administrator\\Desktop\\123.jpg')
rect = 20, 20, 50, 100
image.crop(rect).show()