import pyautogui
from time import sleep

sleep(3)

for _ in range(1100):
    pyautogui.write("babby")
    pyautogui.press('Enter')