import pyautogui # Note that pyautogui will prompt for accessibility permissions
import random
import time

while True:
    x = random.randint(600, 700)
    y = random.randint(200, 700)
    pyautogui.moveTo(x, y, 0.5)
    time.sleep(2)