from PIL.ImageOps import grayscale
import pyautogui
import time
import keyboard
import numpy as np
from random import randint
import win32api, win32con, win32gui
from get_window import WindowMgr
import automation
import new_map

starter = int(0)
time.sleep(2)

#loop 30min (add random time to avoid getting detected)
def main():
    while keyboard.is_pressed('q') == False and starter == 0:
        w = WindowMgr()
        w.find_window_wildcard("Bombcrypto - Google Chrome")
        w.set_foreground()
        time.sleep(0.5)
        automation.automation()
        time.sleep(3)
        if pyautogui.locateOnScreen('ok_button.jpg', grayscale=True, confidence=0.8) != None:
            main()
        w = WindowMgr()
        w.find_window_wildcard("Bombcrypto - Opera")
        w.set_foreground()
        time.sleep(0.5)
        automation.automation()
        if pyautogui.locateOnScreen('ok_button.jpg', grayscale=True, confidence=0.8) != None:
            main()
        #Wait one hour to rerun and make everyone go to work again
        time.sleep(randint(2400, 3000))
main()

        




