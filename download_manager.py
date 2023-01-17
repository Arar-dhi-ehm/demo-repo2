from tkinter import *
from tkinter import messagebox, filedialog
import os

window = Tk()

wrapper_1 = LabelFrame(window, text='File URL')
wrapper_1.pack(fill='both', expand='yes', padx=10, pady=10)

wrapper_2 = LabelFrame(window, text='Download Information')
wrapper_2.pack(fill='both', expand='yes', padx=10, pady=10)



window.geometry('450x400')
window.title('Download Manager')
window.resizable(False, False)

window.mainloop()