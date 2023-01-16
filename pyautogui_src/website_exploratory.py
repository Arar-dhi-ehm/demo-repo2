"""
website_exploratory.py
    Capabilities:
        Can login and logout using pyautogui mouse click and keyboard

    Limitations:
        If the coordinates changed, the script needs to be modified as well.
        When run it can't be stopped. Not Trigerring FailSafe rather use ctrl c in terminal.
            Doing Ctrl + C in terminal(shell) executes signal interrupt.
        Mouse cursor is not following move to coordinate in VMware Linux but in Windows it is working.
        Pop up ads might affect the execution of the script.

    Notes:
        standard_user
        secret_sauce
"""

import pyautogui as pag
import random
import time
import webbrowser

#################[ Tab 1 ]################# [Login]
webbrowser.open('https://www.saucedemo.com/')
time.sleep(3)
pag.click(544, 375, 1, button='left', duration=2)
pag.typewrite('standard_user')
pag.press('tab')
pag.typewrite('secret_sauce')
time.sleep(1)
pag.press('enter')

# #################[ Tab 1.1. ]################# [Inventory Page]
# Scroll down
time.sleep(2)
pag.moveTo(1911, 270, 2)
time.sleep(1)
pag.scroll(-4)
time.sleep(2)
pag.scroll(-4)

# Scroll up
time.sleep(1)
pag.scroll(4)
time.sleep(2)
pag.scroll(4)
time.sleep(2)
pag.scroll(4)

# Click filter option
pag.click(1729, 271, duration=1)
time.sleep(1)
# Z-A option
pag.press('down')
time.sleep(1)
pag.press('enter')

pag.click(1729, 271, duration=1)
time.sleep(1)
# Price low to high
pag.press('down')
time.sleep(1)
pag.press('enter')

pag.click(1729, 271, duration=1)
time.sleep(1)
# Price high to low
pag.press('down')
time.sleep(1)
pag.press('enter')

pag.click(1729, 271, duration=1)
time.sleep(1)
# Back to A-Z
pag.press('down')
time.sleep(1)
pag.press('enter')


#################[ Tab 1.2. ]################# [Inventory Page]
# Click an item (saucelabs backpack)
pag.click(561, 417, duration=2)
# Highlight text and copy
time.sleep(2)
pag.mouseDown(901, 598, button='left')
pag.moveTo(821, 578, 2)
pag.mouseUp()
# Copy
pag.hotkey('ctrl', 'c')
# Open google, paste and type usd to php, press enter
time.sleep(2)
webbrowser.open('https://www.google.com/')
time.sleep(3)
pag.click(736, 465, duration=1)
pag.hotkey('ctrl', 'v')
time.sleep(2)
pag.typewrite(' usd to php')
pag.press('enter')
# Close google
time.sleep(6)
pag.hotkey('ctrl', 'w')

# Go back to products
pag.click(150, 281,button='left', duration=2)

# Click Labs-bolt T-shirt
pag.click(540, 744,button='left', duration=2)
# Highlight text and copy
time.sleep(2)
pag.mouseDown(901, 598, button='left')
pag.moveTo(821, 578, 2)
pag.mouseUp()
# Copy
pag.hotkey('ctrl', 'c')
# Open google, paste and type usd to php, press enter
time.sleep(2)
webbrowser.open('https://www.google.com/')
time.sleep(3)
pag.click(736, 465, duration=1)
pag.hotkey('ctrl', 'v')
time.sleep(2)
pag.typewrite(' usd to php')
pag.press('enter')
# Close google
time.sleep(6)
pag.hotkey('ctrl', 'w')

# Click Add to Cart
pag.click(902, 654, button='left', duration=2)
time.sleep(4)

# Remove from Cart
pag.click(902, 654, button='left', duration=2)
time.sleep(4)

# Add Cart Again
pag.click(902, 654, button='left', duration=2)
time.sleep(4)

# Check Cart
pag.click(1868, 190, button='left', duration=2)
time.sleep(7)

# Continue Shopping
pag.click(297, 679, button='left', duration=2)
time.sleep(4)
# Scroll down
time.sleep(1)
pag.scroll(-4)

# Click Sauce Labs Onesie
pag.click(540, 498, button='left', duration=2)
# Highlight text and copy
time.sleep(2)
pag.mouseDown(901, 598, button='left')
pag.moveTo(821, 578, 2)
pag.mouseUp()
# Copy
pag.hotkey('ctrl', 'c')
# Open google, paste and type usd to php, press enter
time.sleep(2)
webbrowser.open('https://www.google.com/')
time.sleep(3)
pag.click(736, 465, duration=1)
pag.hotkey('ctrl', 'v')
time.sleep(2)
pag.typewrite(' usd to php')
pag.press('enter')
# Close google
time.sleep(6)
pag.hotkey('ctrl', 'w')

# Click Add to Cart
pag.click(902, 654, button='left', duration=2)
time.sleep(4)

# Check Cart
pag.click(1868, 190, button='left', duration=2)
time.sleep(7)

# Continue Shopping
pag.click(289, 876, button='left', duration=2)
time.sleep(4)

# Click an item (saucelabs backpack)
pag.click(561, 417, duration=2)
# Highlight text and copy
time.sleep(2)
pag.mouseDown(901, 598, button='left')
pag.moveTo(821, 578, 2)
pag.mouseUp()
# Copy
pag.hotkey('ctrl', 'c')
# Open google, paste and type usd to php, press enter
time.sleep(2)
webbrowser.open('https://www.google.com/')
time.sleep(3)
pag.click(736, 465, duration=1)
pag.hotkey('ctrl', 'v')
time.sleep(2)
pag.typewrite(' usd to php')
pag.press('enter')
# Close google
time.sleep(6)
pag.hotkey('ctrl', 'w')

# Click Add to Cart
pag.click(902, 654, button='left', duration=2)
time.sleep(4)

# Check Cart
pag.click(1868, 190, button='left', duration=2)
time.sleep(7)

# Scroll down, pause, then Check out
time.sleep(2) # delete this
# Scroll down
pag.scroll(-1)
time.sleep(7)
# Click Check Out
pag.click(1629, 931, button='left', duration=2)
time.sleep(3)

# Fill out form
pag.click(780, 384, button='left', duration=2)
pag.typewrite('Juan')
pag.press('tab')
pag.typewrite('Dela Cruz')
pag.press('tab')
random_number = random.randint(2020,2380)
pag.typewrite(str(random_number))

# Scroll up and down and click continue
time.sleep(3)
pag.scroll(1) 

time.sleep(3)
pag.scroll(-1)

# Click Continue
time.sleep(1)
pag.click(1424, 649, 2, button='left', duration=2)
time.sleep(1)
pag.click(1599, 829, button='left', duration=2)

# Scroll up and down
time.sleep(3)
pag.scroll(1) 

time.sleep(3)
pag.scroll(-5)

# Copy total prize and convert to php
# Highlight text and copy
time.sleep(2)
pag.mouseDown(391, 746, button='left')
pag.moveTo(330, 731, 2)
pag.mouseUp()
# Copy
pag.hotkey('ctrl', 'c')
# Open google, paste and type usd to php, press enter
time.sleep(2)
webbrowser.open('https://www.google.com/')
time.sleep(3)
pag.click(736, 465, duration=1)
pag.hotkey('ctrl', 'v')
time.sleep(2)
pag.typewrite(' usd to php')
pag.press('enter')
# Close google
pag.click(1624, 840, button='left', duration=2)
time.sleep(7) 

pag.hotkey('ctrl', 'w')

# Click Finish
time.sleep(3)
pag.click(1624, 840, button='left', duration=2)

# Script is finished
pag.alert(text='Script is finished.', title='DONE!', button='OK')
