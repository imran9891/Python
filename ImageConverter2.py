#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
from PIL import Image, ImageFilter
os.chdir('C:/Users/AZAZ/Desktop/Python/Images')
pwd = os.getcwd()
print(pwd)
image_path = pwd
converted_path = pwd + '/Folder/'
for filename in os.listdir(image_path):
    # print(filename)
    img = Image.open(f"{image_path}\\{filename}")
    f_img = img.filter(ImageFilter.SHARPEN)
    #f_img.thumbnail((300,300))
    clean_name = os.path.splitext(filename)[0]
    # print(clean_name)
    if not os.path.exists(converted_path):
        os.mkdir('Folder')
    f_img.save(f"{converted_path}\\{clean_name}.png","png")
print('all done')

