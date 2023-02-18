"""Test the Topic functionality of Django: Learning Log"""

import pyautogui
import time


class Topic:
    """Test for user's topic function."""
    def __init__(self, topic):
        self.topic = topic

    def click_topics_link(self):
        time.sleep(2)
        pyautogui.click(2175, 118, 1, button='left', duration=2)

    def add_new_topic(self):
    	pyautogui.click(2035, 321, 1, button='left', duration=1)

    def enter_topic(self):
    	pyautogui.click(1964, 248, 1, button='left', duration=1)
    	pyautogui.typewrite(self.topic)

    def click_add_topic_button(self):
    	pyautogui.click(2004, 327, 1, button='left', duration=2)

    def click_topic(self):
        time.sleep(1)
        pyautogui.click(2061, 255, 1, button='left', duration=1)

    # def click_learning_log_link(self):
    # 	pyautogui.click(2016, 111, 1, button='left', duration=1)

    def add_user_topic(self):
        self.click_topics_link()
        self.add_new_topic()
        self.enter_topic()
        self.click_add_topic_button()
        self.click_topic()
        # self.click_learning_log_link()
        # self.click_topics_link()


if __name__ == '__main__':
    print("Topic script is running, please wait...")
    user = Topic('Python')
    user.add_user_topic()
    print("Topic script is complete.")