import 模块
from PIL import Image
模块.test()


im=Image.open('1080.png')
print(im.format,im.size,im.mode)
im.thumbnail((200,100))
im.save('thumb.jpg','JPEG')