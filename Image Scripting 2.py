#!/usr/bin/env python
# coding: utf-8

# In[ ]:


img = Image.open("./Scripting/test.png")
# img.show()
print(img.size)
new_img = img.resize((400,400))
new_img.save("./Scripting/testsmall.png","png") # shrinks but poor aspect ratio

img.thumbnail((400,400))
img.save("./Scripting/testthumbnail.png","png")
print(img.size)

