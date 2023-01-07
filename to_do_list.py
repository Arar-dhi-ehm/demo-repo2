"""
to_do_list.py
    Capabilities:
        Can mark the tasks as done
        Can save and load tasks for later
        Vertical and Horizontal scrollbar for long string
    Limitations:
        Can't delete all tasks. Delete one by one.
        Can't mark all. Mark one by one.
"""

import tkinter
import tkinter.messagebox
import pickle
from tkinter import *

window = tkinter.Tk()
window.title("My ToDo List App")


def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Hi there!", message="Please enter your task in the app. "
                                                                  "Then click the \"Add task\" button again.")


def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        tkinter.messagebox.showwarning(title="Hi there!", message="Please select a task in the app. "
                                                                  "Then click the \"Delete task\" button again.")


def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except IndexError:
        tkinter.messagebox.showwarning(title="Hi there!", message="Sorry, can't find tasks.dat.")


def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))


# Executes this to mark completed
def mark_completed():
    try:
        marked = listbox_tasks.curselection()
        temp = marked
        # Store the text of selected item in a string
        temp_marked = listbox_tasks.get(marked)
        # Update it
        temp_marked = "[✔] " + temp_marked
        # Delete it and then insert it
        listbox_tasks.delete(temp)
        listbox_tasks.insert(temp, temp_marked)
    except TclError:
        tkinter.messagebox.showwarning(title="Hi there!", message="Please select a task in the app. "
                                                                  "Then click the \"Mark as done\" button again.")


# Create GUI
frame_tasks = tkinter.Frame(window)
frame_tasks.pack()

# Bottom Scrollbar (part 1)
scrollbar_tasks_bottom = tkinter.Scrollbar(frame_tasks, orient=HORIZONTAL)
scrollbar_tasks_bottom.pack(side=tkinter.BOTTOM, fill=tkinter.X)

# Listbox
listbox_tasks = tkinter.Listbox(frame_tasks, bg="black", fg="white", height=15, width=50, border=5, activestyle=NONE,
                                relief=RIDGE, font=('Calibri', 12))
listbox_tasks.pack(side=tkinter.LEFT, fill=tkinter.X)

# Right Scrollbar
scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Bottom Scrollbar (part 2)
listbox_tasks.config(xscrollcommand=scrollbar_tasks_bottom.set)
scrollbar_tasks_bottom.config(command=listbox_tasks.xview)

# Entry window where user can type.
entry_task = tkinter.Entry(window, width=65)
entry_task.pack(fill='x', padx=20)

button_add_task = tkinter.Button(window, text="Add task", width=48, command=add_task)
# fill='x' means can stretch horizontally. padx mean external padding horizontally. pady means external pad. vertically.
button_add_task.pack(fill='x', padx=20, pady=3)

button_delete_task = tkinter.Button(window, text="Delete task", width=48, command=delete_task)
button_delete_task.pack(fill='x', padx=20, pady=3)

button_load_tasks = tkinter.Button(window, text="Load tasks", width=48, command=load_tasks)
button_load_tasks.pack(fill='x', padx=20, pady=3)

button_save_tasks = tkinter.Button(window, text="Save tasks", width=48, command=save_tasks)
button_save_tasks.pack(fill='x', padx=20, pady=3)

mark_as_done = tkinter.Button(window, text="Mark as done", width=48, command=mark_completed)
mark_as_done.pack(fill='x', padx=20, pady=3)

# mainloop() method puts everything on the display, and responds to user input until the program terminates.
window.mainloop()
