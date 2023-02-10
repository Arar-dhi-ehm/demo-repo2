"""photo_editor.py
"""

import os
import tkinter.messagebox
from PIL import Image, ImageEnhance, ImageFilter

path = '/Documents/automation_scripts/automation_project/python_edit_images'
path_out = '/Documents/automation_scripts/automation_project/edited_py_images'

# Access all the image file in the path and edit all images.
for filename in os.listdir(path):
    # Open image using this library
    image = Image.open(f'{path}/{filename}')
    
    # Sharpen the image
    edit = image.filter(ImageFilter.SHARPEN)

    clean_name = os.path.splitext(filename)[0]
    # Save edited photos to path_out
    edit.save(f'.{path_out}/{clean_name}_edited.jpg')

# print(os.getcwd)

tkinter.messagebox.showinfo(title='Done', message='Script is finished.')
# Link: https://youtu.be/vEQ8CXFWLZU?t=219