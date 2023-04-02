import pyautogui
import time

# Click Alchemist's Pot
time.sleep(1)
pyautogui.click(2622, 525, 1, button='left', duration=1)

# Click potion button
pyautogui.click(2561, 452, 1, button='left', duration=1)

# Drag from bottom to the top
pyautogui.dragTo(2612, 360, button='left')

# Click Swiftness Potion
# time.sleep(0.5)
# pyautogui.click(2604, 636, 1, button='left', duration=1)

# Click Dark Potion
time.sleep(0.5)
pyautogui.click(2585, 766, 1, button='left', duration=1)

# Click Craft
time.sleep(0.5)
pyautogui.click(2631, 766, 1, button='left', duration=1)

# Click Alchemist's Pot again
time.sleep(1)
pyautogui.click(2622, 525, 1, button='left', duration=1)

