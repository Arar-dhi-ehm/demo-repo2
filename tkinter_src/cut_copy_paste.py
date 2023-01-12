"""
cut_copy_paste.py
    Capabilities:
        Select all text
        Copy text
        Cut text
        Paste text from clipboard
    Limitations:


    Improvements:
        Copy and paste works only within the widget. It should work outside widget.
            - shutil module might work on it.
"""
import tkinter as tk

window = tk.Tk()
window.geometry('400x300')
window.title('shutil')

label_one = tk.Label(window, font=20, text='Name')
label_one.grid(row=0, column=0, padx=2, pady=10)

text_entry = tk.Text(window, font=20, height=4, width=28)
text_entry.grid(row=0, column=1, columnspan=4)

# Declare global variable
global data

def select_all_func():
    # Select all text starting from index 1
    text_entry.tag_add('sel', '1.0', 'end')

def cut_func():
    global data
    if text_entry.selection_get():
        # Fetch the selection
        data=text_entry.selection_get()
        # After fetching selection, delete
        text_entry.delete('sel.first', 'sel.last')

def copy_func():
    global data
    if text_entry.selection_get():
        # Fetch the selection
        data=text_entry.selection_get()

def paste_func():
    global data
    text_entry_bottom.insert(tk.END, data)

# Select all button
select_all_button = tk.Button(window, text='Select All', command=lambda:select_all_func(), font=20)
select_all_button.grid(row=1, column=1, padx=2, pady=5)

# Cut button
cut_button = tk.Button(window, text='Cut', command=lambda:cut_func(), font=20)
cut_button.grid(row=1, column=2)

# Copy button
copy_button = tk.Button(window, text='Copy', command=lambda:copy_func(), font=20)
copy_button.grid(row=1, column=3)

# Paste button
paste_button = tk.Button(window, text='Paste', command=lambda:paste_func(), font=20)
paste_button.grid(row=1, column=4)

text_entry_bottom = tk.Text(window, font=20, height=4, width=28)
text_entry_bottom.grid(row=2, column=1, columnspan=4)

window.mainloop()