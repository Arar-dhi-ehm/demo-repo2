import pyautogui
import time
from tqdm import tqdm


class WeaponCraftingBot:
    def __init__(self):
        self.weapon_button_pos = (2319, 748)
        self.staff_category_pos = (2319, 748)
        self.crude_staff_pos = (2002, 413)
        self.craft_button_pos = (2562, 727)

    def click_position(self, position, button='left', duration=0.5):
        pyautogui.click(*position, button=button, duration=duration)

    def craft_weapon(self):
        # Click weapon button
        time.sleep(1)
        self.click_position(self.weapon_button_pos)

        # Click staff category
        self.click_position(self.staff_category_pos)

        # Create crude staff
        self.click_position(self.crude_staff_pos)

        # Craft crude staff
        self.click_position(self.craft_button_pos)


if __name__ == '__main__':
    print("Staff creation script is running, please wait...")
    bot = WeaponCraftingBot()
    with tqdm(total=36) as pbar:
        for i in range(36):
            bot.craft_weapon()
            pbar.update(1)
    print("Staff creation script is complete.")



# import pyautogui
# import time

# class WeaponCraftingBot:
#     def __init__(self):
#         self.weapon_button_pos = (2319, 748)
#         self.staff_category_pos = (2319, 748)
#         self.crude_staff_pos = (2002, 413)
#         self.craft_button_pos = (2562, 727)

#     def click_position(self, position, button='left', duration=0.5):
#         pyautogui.click(*position, button=button, duration=duration)

#     def craft_weapon(self):
#         # Click weapon button
#         time.sleep(1)
#         self.click_position(self.weapon_button_pos)

#         # Click staff category
#         self.click_position(self.staff_category_pos)

#         # Create crude staff
#         self.click_position(self.crude_staff_pos)

#         # Craft crude staff
#         self.click_position(self.craft_button_pos)

# if __name__ == '__main__':
#     print("Staff creation script is running, please wait...")
#     bot = WeaponCraftingBot()
#     for i in range(40):
#         bot.craft_weapon()
#     print("Staff creation script is complete.")
