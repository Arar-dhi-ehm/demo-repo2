"""
modern_tkinter_gui.py
    Capabilities:

    Limitations:

    Prerequisites:
        Install customtkinter
"""

import customtkinter

# Customize the way your app will look like
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

# Widget
window = customtkinter.CTk()
window.geometry('500x350')
window.resizable(height=False,width=False)

# If the login button is clicked, it will print 'Test' 
def login():
    print('Test')


# Create a frame where the stuff will be put in place
frame = customtkinter.CTkFrame(master=window)
frame.pack(pady=20, padx=60, fill='both', expand=True)

# Add label to the frame
label = customtkinter.CTkLabel(master=frame, text='Login System')
label.pack(pady=12, padx=10)

username_entry = customtkinter.CTkEntry(master=frame, placeholder_text='Username')
username_entry.pack(pady=12, padx=10)

password_entry = customtkinter.CTkEntry(master=frame, placeholder_text='Password', show='*')
password_entry.pack(pady=12, padx=10)

# The command=login is the login function you have defined
login_button = customtkinter.CTkButton(master=frame, text='Login', command=login)
login_button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text='Remember Me')
checkbox.pack(pady=12, padx=10)

window.mainloop()