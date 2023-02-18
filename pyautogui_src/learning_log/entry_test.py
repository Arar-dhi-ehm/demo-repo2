"""Test the Entry functionality of Django: Learning Log"""

import pyautogui
import time
from topic_test import Topic


class Entry(Topic):
    """Test for user's entry function."""
    def __init__(self, entry):
        self.entry = entry

    def click_add_new_entry(self):
        pyautogui.click(2024, 319, 1, button='left', duration=1)

    def enter_entry(self):
        pyautogui.click(1966, 348, 1, button='left', duration=1)
        pyautogui.typewrite(self.entry)

    def scroll_page_left(self):
        pyautogui.click(2234, 245, 1, button='left', duration=0.5)
        pyautogui.press(['left', 'left', 'left'])

    def click_add_entry_button(self):
        pyautogui.click(2008, 676, 1, button='left', duration=2)

    def add_user_entry(self):
        self.click_topics_link()
        self.click_topic()
        self.click_add_new_entry()
        self.enter_entry()
        self.scroll_page_left()
        self.click_add_entry_button()


if __name__ == '__main__':
    print("Entry script is running, please wait...")
    user = Entry(
    	'Python is a very popular general-purpose interpreted, '
    		'interactive, object-oriented, '
    		'and high-level programming language.'
    			)
    user.add_user_entry()
    print("Entry script is complete.")