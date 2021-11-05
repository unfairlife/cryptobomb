from PIL.ImageOps import grayscale
import pyautogui
import time
import keyboard
import numpy as np
from random import randint
from get_window import WindowMgr
import automation
import new_map

starter = int(0)
time.sleep(2)

#loop 30min (add random time to avoid getting detected)
# Set your Browser name here. Two examples are provided, chrome and opera(gx).
def main():
    while keyboard.is_pressed('q') == False and starter == 0:
        w = WindowMgr()
        w.find_window_wildcard("Bombcrypto - Google Chrome")
        w.set_foreground()
        time.sleep(0.5)
        automation.automation()
        time.sleep(3)
        #If the login page fails and the button "ok" is located, try to run again
        if pyautogui.locateOnScreen('ok_button.jpg', grayscale=True, confidence=0.8) != None:
            main()
       # w = WindowMgr()
     #   w.find_window_wildcard("Bombcrypto - Opera")
     #   w.set_foreground()
      #  time.sleep(0.5)
      #  automation.automation()
    #Re-run the script and keep looking if theres new map button
        for i in range(50):
            #loop 25~30min (add random time to avoid getting detected)
            time.sleep(randint(24, 30))
            #Search if the map is finished > change map
            new_map.new_map()
            print("finished run ", i, "of  50")
main()

        





