import pyautogui
import time
from tqdm import tqdm


class AlchemistBot:
    def __init__(self):
        self.alchemist_pot_position = (2622, 525)
        self.potion_button_position = (2561, 452)
        self.swiftness_potion_position = (2604, 636)
        self.dark_potion_position = (2585, 766)
        self.craft_button_position = (2631, 766)
        self.bottom_position = (2620, 792)
        self.top_position = (2620, 212)
        self.click_duration = 0.3
        self.wait_duration = 0.3

    def run(self, num_iterations=400):
        time.sleep(2)
        for i in tqdm(range(num_iterations)):
            # Click Alchemist's Pot
            time.sleep(self.wait_duration)
            pyautogui.click(*self.alchemist_pot_position,
                            button='left', duration=self.click_duration)

            # Click potion button
            pyautogui.click(*self.potion_button_position,
                            button='left', duration=self.click_duration)

            # Drag from bottom to the top
            pyautogui.moveTo(*self.bottom_position, duration=self.click_duration)
            pyautogui.dragTo(*self.top_position,
                         duration=self.click_duration, button='left')
            pyautogui.mouseUp()

            pyautogui.moveTo(*self.bottom_position,
                             duration=self.click_duration)
            pyautogui.dragTo(*self.top_position,
                             duration=self.click_duration, button='left')
            pyautogui.mouseUp()

            # Click Dark Potion
            time.sleep(self.wait_duration)
            pyautogui.click(*self.dark_potion_position,
                            button='left', duration=self.click_duration)

            # Click Craft
            time.sleep(self.wait_duration)
            pyautogui.click(*self.craft_button_position,
                            button='left', duration=self.click_duration)

            # Click Alchemist's Pot again
            time.sleep(self.wait_duration)
            pyautogui.click(*self.alchemist_pot_position,
                            button='left', duration=self.click_duration)


if __name__ == '__main__':
    print("Farm potion script is running, please wait...")
    bot = AlchemistBot()
    bot.run(num_iterations=400)
    print("Farm potion script is complete.")
