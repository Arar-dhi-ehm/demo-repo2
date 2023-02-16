import pyautogui as pag  # For mouse and keyboard
import random  # Give random number
import time  # For letting the program sleep in a specified time
import webbrowser  # For opening a specified website using default browser


class Automation:
    def __init__(self):
        self.pag = pag
        self.pag.FAILSAFE = True

    def login(self):
        webbrowser.open('https://www.saucedemo.com/')
        time.sleep(3)
        self.pag.click(544, 375, 1, button='left', duration=2)
        self.pag.typewrite('standard_user')
        self.pag.press('tab')
        self.pag.typewrite('secret_sauce')
        time.sleep(1)
        self.pag.press('enter')

    def inventory_page(self):
        # Scroll down
        time.sleep(2)
        self.pag.moveTo(1911, 270, 2)
        time.sleep(1)
        self.pag.scroll(-4)
        time.sleep(2)
        self.pag.scroll(-4)

        # Scroll up
        time.sleep(1)
        self.pag.scroll(4)
        time.sleep(2)
        self.pag.scroll(4)
        time.sleep(2)
        self.pag.scroll(4)

        # Click filter option
        self.pag.click(1729, 271, duration=1)
        time.sleep(1)
        # Z-A option
        self.pag.press('down')
        time.sleep(1)
        self.pag.press('enter')

        self.pag.click(1729, 271, duration=1)
        time.sleep(1)
        # Price low to high
        self.pag.press('down')
        time.sleep(1)
        self.pag.press('enter')

        self.pag.click(1729, 271, duration=1)
        time.sleep(1)
        # Price high to low
        self.pag.press('down')
        time.sleep(1)
        self.pag.press('enter')

        self.pag.click(1729, 271, duration=1)
        time.sleep(1)
        # Back to A-Z
        self.pag.press('down')
        time.sleep(1)
        self.pag.press('enter')

    def saucelabs_backpack(self):
        # Click an item (saucelabs backpack)
        self.pag.click(561, 417, duration=2)
        # Highlight text and copy
        time.sleep(2)
        self.pag.mouseDown(901, 598, button='left')
        self.pag.moveTo(821, 578, 2)
        self.pag.mouseUp()
        # Copy
        self.pag.hotkey('ctrl', 'c')
        # Open google, paste and type usd to php, press enter
        time.sleep(2)
        webbrowser.open('https://www.google.com/')
        time.sleep(3)
        self.pag.click(736, 465, duration=1)
        self.pag.hotkey('ctrl', 'v')
        time.sleep(2)
        self.pag.typewrite(' usd to php')
        self.pag.press('enter')
        # Close google
        time.sleep(6)
        self.pag.hotkey('ctrl', 'w')

    # def labs_bolt_tshirt(self):
    #     # Click Labs-bolt T-shirt
