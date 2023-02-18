"""Test the user registration process for Django Learning Log."""

import pyautogui
import time

class UserRegistration:
    """Test for user registration function."""
    def __init__(self, username, password, confirm_password):
        self.username = username
        self.password = password
        self.confirm_password = confirm_password

    def click_register_link(self):
        time.sleep(2)
        pyautogui.click(2299, 117, 1, button='left', duration=2)

    def enter_username(self):
        pyautogui.click(2099, 182, 1, button='left', duration=0.5)
        pyautogui.typewrite(self.username)

    def enter_password(self):
        pyautogui.click(2100, 294, 1, button='left', duration=0.5)
        pyautogui.typewrite(self.password)

    def password_confirmation(self):
        pyautogui.click(2275, 548, 1, button='left', duration=0.5)
        pyautogui.typewrite(self.confirm_password)

    def click_register_button(self):
        pyautogui.click(2004, 659, 1, button='left', duration=0.5)

    def register_user(self):
        self.click_register_link()
        self.enter_username()
        self.enter_password()
        self.password_confirmation()
        self.click_register_button()

if __name__ == '__main__':
    print("Registration script is running, please wait...")
    user = UserRegistration('Austin', 'Case1234', 'Case1234')
    user.register_user()
    print("Registration script is complete.")


'''Backup Code
import pyautogui as pag  # For mouse and keyboard
import time  # For letting the program sleep in a specified time

# Verify that the user can register a new account

# Click Register link in Header
time.sleep(2)
pag.click(2299, 117, 1, button='left', duration=2)

# Click username field
pag.click(2099, 182, 1, button='left', duration=2)
# Type the username
pag.typewrite('Austin')
# Click the password field
pag.click(2100, 294, 1, button='left', duration=2)
# Type the password
pag.typewrite('Case1234')
# Click the confirmation password field
pag.click(2275, 548, 1, button='left', duration=2)
# Type the password
pag.typewrite('Case1234')

# Click the Register button
pag.click(2004, 659, 1, button='left', duration=2)

print("Registration script is complete.")
'''