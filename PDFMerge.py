#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### PDF MERGER
import PyPDF2

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for item in pdf_list:
        print(item)
        merger.append(item)
    merger.write('./PDF/super.pdf')
    return 'done combining'

i=0
files=[]
limit = int(input('How many pdf files you want to merge: '))
while i<limit:
    name = './PDF/' + input('File Name: ') +'.pdf'
    files.append(name)
    i += 1
print(pdf_combiner(files))

