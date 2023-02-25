import pyautogui
import time
from tqdm import tqdm


class WeaponDismantler:
    def __init__(self):
        self.backpack_icon_pos = (2781, 251)
        self.sort_button_pos = (2656, 734)
        self.staff_pos = (2805, 343)
        self.dismantle_button_pos = (2467, 734)
        self.confirm_button_pos = (2462, 616)

    def click_position(self, position, button='left', duration=0.5):
        pyautogui.click(*position, button=button, duration=duration)

    def dismantle_weapons(self):
        # Click backpack icon
        time.sleep(1)
        self.click_position(self.backpack_icon_pos)

        # Click sort button
        self.click_position(self.sort_button_pos)

        # Click staff
        self.click_position(self.staff_pos)

        # Click dismantle button
        self.click_position(self.dismantle_button_pos)

        # Click confirm button
        self.click_position(self.confirm_button_pos)


if __name__ == '__main__':
    print("Weapon dismantling script is running, please wait...")
    bot = WeaponDismantler()
    with tqdm(total=38) as pbar:
        for i in range(38):
            bot.dismantle_weapons()
            pbar.update(1)
    print("Weapon dismantling script is complete.")
