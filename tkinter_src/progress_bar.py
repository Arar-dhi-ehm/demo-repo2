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
    tasks = 10
    current_task = 0
    while(current_task < tasks):
        time.sleep(1)
        # Everytime the progress bar button is clicked, it will fill the bar by 10.
        progress_bar['value'] += 10
        # Increment task with each iteration
        current_task += 1
        # Cast the label output to string
        percent.set(str(int((current_task / tasks) * 100)) + '%')
        text.set(str(current_task) + '/' + str(tasks) + " tasks completed")
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
progress_button = Button(text='upload', command=start).pack()

window.mainloop()
