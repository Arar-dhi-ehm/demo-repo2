"""Test the user login process for Django Learning Log."""

import pyautogui
import time

class UserLogin:
	"""Test for user login function."""
	def __init__(self, username, password):
		self.username = username
		self.password = password

	def click_login_link(self):
		time.sleep(2)
		pyautogui.click(2412, 119, 1, button='left', duration=2)

	def enter_username(self):
		pyautogui.click(2099, 182, 1, button='left', duration=0.5)
		pyautogui.typewrite('Austin')

	def enter_password(self):
		pyautogui.click(2102, 256, 1, button='left', duration=0.5)
		pyautogui.typewrite('Case1234')

	def click_login_button(self):
		pyautogui.click(1989, 333, 1, button='left', duration=0.5)

	def login_user(self):
		self.click_login_link()
		self.enter_username()
		self.enter_password()
		self.click_login_button()


if __name__ == '__main__':
    print("Login script is running, please wait...")
    user = UserLogin('Austin', 'Case1234')
    user.login_user()
    print("Login script is complete.")