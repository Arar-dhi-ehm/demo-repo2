import pyautogui
import time

# Locate center of game
time.sleep(1)
pyautogui.click(2557, 515, 1, button='left', duration=0.5)

# Locate the "branch" image on the screen and click it
branch_location = pyautogui.locateOnScreen(
    '/home/arar/Documents/python_repo/demo-repo2/pyautogui_src/twd/branch_text1.png')
if branch_location is not None:
    branch_center = pyautogui.center(branch_location)
    pyautogui.click(branch_center)
else:
    print("Could not locate the branch image on the screen")

# Locate the "log" image on the screen and click it
log_location = pyautogui.locateOnScreen(
    '/home/arar/Documents/python_repo/demo-repo2/pyautogui_src/twd/log_text1.png')
if log_location is not None:
    log_center = pyautogui.center(log_location)
    pyautogui.click(log_center)
else:
    print("Could not locate the log image on the screen")


# # Locate the "Branch" text on the screen and click it
# branch_location = pyautogui.locateOnScreen(
#     '/home/arar/Documents/python_repo/demo-repo2/pyautogui_src/twd/branch_text1.png', grayscale=True, confidence=0.95, region=(0, 0, 2336, 1080))
# if branch_location is not None:
#     branch_center = pyautogui.center(branch_location)
#     pyautogui.click(branch_center)
# else:
#     print("Could not locate the Branch text on the screen")

# # Locate the "Log" text on the screen and click it
# log_location = pyautogui.locateOnScreen(
#     '/home/arar/Documents/python_repo/demo-repo2/pyautogui_src/twd/log_text1.png', grayscale=True, confidence=0.95, region=(0, 0, 2336, 1080))
# if log_location is not None:
#     log_center = pyautogui.center(log_location)
#     pyautogui.click(log_center)
# else:
#     print("Could not locate the Log text on the screen")
