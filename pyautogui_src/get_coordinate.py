"""
get_coordinate.py
    Capabilities:
        Used for getting the x and y coordinate of the mouse cursor
        
    Prerequisites:
        The user needs to download and install pyautogui package
"""


import pyautogui as pag
import time

time.sleep(3)
coordinate = pag.position()

print(coordinate)  

# alert will give us hint that we got the coordinate
pag.alert(text=coordinate, title='DONE!', button='OK')

