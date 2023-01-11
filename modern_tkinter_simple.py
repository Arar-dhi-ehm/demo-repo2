"""
modern_tkinter_simple.py
    Capabilities:

    Limitations:

    Prerequisites:
        Install customtkinter
"""
import tkinter
import customtkinter

# Customize the way your app will look like
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

window = customtkinter.CTk()
window.geometry('400x580')
window.title('CTk Sample-1')

def button_callback():
    print('Button click', combo_box_1.get())

def slider_callback(value):
    progress_bar_1.set(value)

frame = customtkinter.CTkFrame(master=window)
frame.pack(pady=20, padx=60, fill='both', expand=True)

label_1 = customtkinter.CTkLabel(master=frame, justify=tkinter.LEFT)
label_1.pack(pady=12, padx=10)

progress_bar_1 = customtkinter.CTkProgressBar(master=frame)
progress_bar_1.pack(pady=12, padx=10)

button_1 = customtkinter.CTkButton(master=frame, command=button_callback)
button_1.pack(pady=12, padx=10)

slider_1 = customtkinter.CTkSlider(master=frame, command=slider_callback, from_=0, to=1)
button_1.pack(pady=12, padx=10)

entry_1 = customtkinter.CTkEntry(master=frame, placeholder_text='Text Entry')
entry_1.pack(pady=12, padx=10)

option_menu_1 = customtkinter.CTkOptionMenu(frame, values=['Option 1', 'Option 2', 'Option 3', 'More ...'])
option_menu_1.pack(pady=12, padx=10)
option_menu_1.set('Option Menu')

combo_box_1 = customtkinter.CTkComboBox(frame, values=['Option 1', 'Option 2', 'Option 3', 'More ...'])
combo_box_1.pack(pady=12, padx=10)
combo_box_1.set('Option Menu')

check_box_1 = customtkinter.CTkCheckBox(master=frame)
check_box_1.pack(pady=12, padx=10)

radio_button_var = tkinter.IntVar(value=1)  # Why is this line added?

radio_button_1 = customtkinter.CTkRadioButton(master=frame, variable=radio_button_var, value=1)
radio_button_1.pack(pady=12, padx=10)

radio_button_2 = customtkinter.CTkRadioButton(master=frame, variable=radio_button_var, value=2)
radio_button_2.pack(pady=12, padx=10)

switch_1 = customtkinter.CTkSwitch(master=frame)
switch_1.pack(pady=12, padx=10)

# This is the widget. 
window.mainloop()
