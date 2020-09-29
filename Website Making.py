#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Created a simple html file (index.html)

# <html>
# <head>
#     <title>Machine Learning</title>
#     <link rel="stylesheet" type="text/css" href="style.css"
# </head>
# <body>
#     I am a ML Expert
#     <script src='script.js'></script>
# </body>
# </html>

# 2. Create a simple css file (style.css)

# body {
#     background-color: gold
# }

# 3. Created a simple js file (script.js)
    
# console.log('hii')
    
# 4. Setup Flask
# 5. Create a virtual environment using: python -m venv venv
# 6. Activate the virtual environment: venv\Scripts\activate.bat
# 7. Install Flask: pip install flask in the virtual environment
# 8. Export the Flask in the current environment: set FLASK_APP = server.py (production-phase)
# 9. Run the Flask : flask run p python -m flask run
# 10. To make changes in the run time: set FLASK_ENV = development (development-phase)

    
# * render_template Library: allows us to send html files in the server. Looks for html files in templates folder so just create it.
# * Static Files: css and javascript files/ Create a static named folder.
# * Assets Folder: contaimns images and .ico files of favicons.
# * Favicons: To set it give commands in the head section.
# * <link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico')}}">
# * url_for library: to evaluate the expressions.
# * redirect module: to redirect to the other hml web page.
# * from flask import Flask, render_template, url_for, redirect.


# In[ ]:




