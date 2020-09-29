#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import PyPDF2

template = PyPDF2.PdfFileReader(open('./PDF/super.pdf','rb'))
watermark = PyPDF2.PdfFileReader(open('./PDF/dummy_watermark.pdf','rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
    
    with open('./PDF/watermarked.pdf', mode='wb') as files:
        output.write(files)
print('done')

