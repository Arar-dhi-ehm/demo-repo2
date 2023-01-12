"""
progress_bar.py
    Capabilities:
        
    Limitations:

    Improvements:
        If the upload button is clicked again, it must show an error message
"""

from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 50
    download = 0
    speed = 1
    while(download < GB):
        time.sleep(0.05)
        # Everytime the progress bar button is clicked, it will fill the bar by 10.
        progress_bar['value'] += (speed / GB) * 100
        # Increment task with each iteration
        download += speed
        # Cast the label output to string
        percent.set(str(int((download / GB) * 100)) + '%')
        text.set(str(download) + '/' + str(GB) + " GB completed")
        # Refresh window with each iteration
        window.update_idletasks()

window = Tk()
window.title('Progress Bar')

# This will update percent with a new text per iteration
percent = StringVar()
text = StringVar()

# Create progress bar
progress_bar = Progressbar(window, orient=HORIZONTAL, length=300)
progress_bar.pack(pady=10)

# Create a label that shows percent
percent_label = Label(window, textvariable=percent).pack()
task_label = Label(window, textvariable=text).pack()

# Create a button for progress bar
progress_button = Button(text='Download', command=start).pack()

window.mainloop()
