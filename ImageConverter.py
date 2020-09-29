#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
from PIL import Image

image_folder = './Scripting/'
output_folder = './Scripting/Output/'
# print(image_folder, output_folder)

for filename in os.listdir(image_folder):
    #print(filename)
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    #print(clean_name)
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    img.save(f'{output_folder}{clean_name}.png','png')
print('all done')

