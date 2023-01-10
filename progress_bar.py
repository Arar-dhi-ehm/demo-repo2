"""
progress_bar.py
    Capabilities:

    Limitations:

    Improvements:
"""

from tkinter import *
from tkinter.ttk import *
import time

def start():
    pass

window = Tk()
window.title('Progress Bar')

# Create progress bar
progress_bar = Progressbar(window, orient=HORIZONTAL, length=300)
progress_bar.pack(pady=10)

# Create a button for progress bar
progress_button = Button(text='upload', command=start).pack()

window.mainloop()
