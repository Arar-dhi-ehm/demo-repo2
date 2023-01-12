import webbrowser
import time
import pyautogui as pag

#################[ Tab 1 ]################# [Login]
time.sleep(3)
webbrowser.open('https://www.saucedemo.com/')
time.sleep(3)
pag.click(544, 375, 1, button='left', duration=2)
pag.typewrite('standard_user')
pag.press('tab')
pag.typewrite('secret_sauce')
time.sleep(2)
pag.press('enter', 2)