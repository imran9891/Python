#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import PyPDF2

with open("./PDF/dummy.pdf", mode='rb') as file:
    print(file)
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open("./PDF/tilt.pdf","wb") as new_file:
        writer.write(new_file)

