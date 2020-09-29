#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from PIL import Image, ImageFilter

img = Image.open('./Scripting/MM3.jpg')

print(img)
print(img.format)
print(img.size)
print(img.mode)
print(dir(img))
img.show()

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("./Scripting/blurMM3.png", "png")

filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save("./Scripting/smoothMM3.png", "png")

filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save("./Scripting/sharpenMM3.png", "png")

filtered_img = img.convert('L')
filtered_img.save("./Scripting/greyMM3.png", "png")

crooked = img.rotate(90)
crooked.save("./Scripting/rot90MM3.png", "png")

crooked = img.rotate(180)
crooked.save("./Scripting/rot180MM3.png", "png")

resize = filtered_img.resize((300, 300))
resize.save("./Scripting/smallMM3.png", "png")

box = (400, 400, 800, 800)
region = img.crop(box)
region.save("./Scripting/croppedMM3.png", "png")

