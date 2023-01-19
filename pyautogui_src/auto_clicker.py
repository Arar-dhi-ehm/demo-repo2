import pyautogui as pag
import time

# (1 minute, interval=5) == 12 clicks

"""1 hour"""
# time.sleep(5)
# # range is equal to how many clicks before program termination
# for clicks in range(720): 
#     pag.leftClick(1045, 1068, interval=5)

"""5 hours"""
time.sleep(5)
# range is equal to how many clicks before program termination
for clicks in range(3600): 
    pag.leftClick(1045, 1068, interval=5)

"""8 hours"""
# time.sleep(5)
# # range is equal to how many clicks before program termination
# for clicks in range(5760): 
#     pag.leftClick(1045, 1068, interval=5)

print('Click finished')
