from PIL.ImageOps import grayscale
import pyautogui
import time
import keyboard
import numpy as np
from random import randint
import win32api, win32con, win32gui

starter = int(0)
time.sleep(2)


#Function to screen in the heroes page
def move_mouse_clicked(x,y):
    for i in range(2):
        win32api.SetCursorPos((x-400,y))
        print("scrolling screen to the last hero")
        time.sleep(0.1)
        pyautogui.dragTo(x-400, y-340, 1, button='left')
#Main
def automation():

    #reload page to start the loop
    pyautogui.keyDown('f5')
    time.sleep(0.1)
    pyautogui.keyUp('f5')
    time.sleep(6) #increase this if your connnection takes more than 5 sec to load the button
    #Connect Wallet Button click
    if pyautogui.locateOnScreen('connect_wallet_button.jpg', grayscale=True, confidence=0.8) != None:
        connect_wallet_button = pyautogui.locateOnScreen('connect_wallet_button.jpg', confidence=0.8)
        connect_walletButton_x, connect_walletButton_y = pyautogui.center(connect_wallet_button)
        #print("Connect Wallet Button position: X:", connect_walletButton_x, "Y:", connect_walletButton_y)
        pyautogui.click(connect_walletButton_x, connect_walletButton_y)
        time.sleep(3)

        #Addon small screen select wallet button
        if pyautogui.locateOnScreen('select_wallet_button.jpg', grayscale=True, confidence=0.8) != None:
            selectwallet_button = pyautogui.locateOnScreen('select_wallet_button.jpg', confidence=0.8)
            selectwalletButton_x, selectwalletButton_y = pyautogui.center(selectwallet_button)
            #print("Connect select Button position: X:", selectwalletButton_x, "Y:", selectwalletButton_y)
            pyautogui.click(selectwalletButton_x, selectwalletButton_y)
            time.sleep(4)
        
        #Addon small screen select wallet button2(BLACK FOR OPERA)
        if pyautogui.locateOnScreen('select_wallet_button2.jpg', grayscale=True, confidence=0.8) != None:
            selectwallet_button2 = pyautogui.locateOnScreen('select_wallet_button2.jpg', confidence=0.8)
            selectwalletbutton2_x, selectwalletbutton2_y = pyautogui.center(selectwallet_button2)
            #print("Connect select button2 position: X:", selectwalletbutton2_x, "Y:", selectwalletbutton2_y)
            pyautogui.click(selectwalletbutton2_x, selectwalletbutton2_y)
            time.sleep(4)

        #find notification sign button(opera bugged workaround)
        if pyautogui.locateOnScreen('notification_button.jpg', grayscale=True, confidence=0.8) != None:
            selectwallet_button = pyautogui.locateOnScreen('notification_button.jpg', confidence=0.8)
            selectwalletButton_x, selectwalletButton_y = pyautogui.center(selectwallet_button)
            #print("Connect select Button position: X:", selectwalletButton_x, "Y:", selectwalletButton_y)
            pyautogui.click(selectwalletButton_x, selectwalletButton_y)
            time.sleep(2)
        
        #sign2 contract to connect
        if pyautogui.locateOnScreen('sign2_wallet_button.jpg', grayscale=True, confidence=0.8) != None:
            sign2_wallet_button = pyautogui.locateOnScreen('sign2_wallet_button.jpg', confidence=0.8)
            sign2_walletButton_x, sign2_walletButton_y = pyautogui.center(sign2_wallet_button)
            #print("Connect sign2 Button position: X:", sign2_walletButton_x, "Y:", sign2_walletButton_y)
            time.sleep(3)
            pyautogui.click(sign2_walletButton_x, sign2_walletButton_y)
            time.sleep(90) #sleep(14) here
            print("if the game didnt load until this message was show, rerun with sleep(14) bigger")

        #sign contract to connect
        if pyautogui.locateOnScreen('sign_wallet_button.jpg', grayscale=True, confidence=0.8) != None:
            sign_wallet_button = pyautogui.locateOnScreen('sign_wallet_button.jpg', confidence=0.8)
            sign_walletButton_x, sign_walletButton_y = pyautogui.center(sign_wallet_button)
            #print("Connect sign Button position: X:", sign_walletButton_x, "Y:", sign_walletButton_y)
            time.sleep(3)
            pyautogui.click(sign_walletButton_x, sign_walletButton_y)
            time.sleep(90) #sleep(15) here
            print("if the game didnt load until this message was show, rerun with sleep(15) bigger")
        
        #Access the heroes page
        if pyautogui.locateOnScreen('heroes_button.jpg', grayscale=True, confidence=0.8) != None:
            heroes_button = pyautogui.locateOnScreen('heroes_button.jpg', confidence=0.8)
            heroes_Button_x, heroes_Button_y = pyautogui.center(heroes_button)
            #print("Connect Heroes Button position: X:", heroes_Button_x, "Y:", heroes_Button_y)
            pyautogui.click(heroes_Button_x, heroes_Button_y)
            time.sleep(1)

        #Using the upgrade button, get a position to scroll to the last active hero
        if pyautogui.locateOnScreen('upgrade_button.jpg', grayscale=True, confidence=0.8) != None:
            upgrade_button = pyautogui.locateOnScreen('upgrade_button.jpg', confidence=0.8)
            upgrade_Button_x, upgrade_Button_y = pyautogui.center(upgrade_button)
            #print("Connect upgrade Button position: X:", upgrade_Button_x, "Y:", upgrade_Button_y)
            time.sleep(1)
            move_mouse_clicked(upgrade_Button_x, upgrade_Button_y)
            time.sleep(1)

        #Click for them to work until everyone is working
        while pyautogui.locateOnScreen('work_button.jpg', grayscale=True, confidence=0.8) != None:
            work_button = pyautogui.locateOnScreen('work_button.jpg', confidence=0.8)
            work_Button_x, work_Button_y = pyautogui.center(work_button)
            #print("Button ~To Work~  found, position: X:", work_Button_x, "Y:", work_Button_y)
            pyautogui.moveTo(work_Button_x, work_Button_y)
            pyautogui.click()
            time.sleep(1)

        #after getting everyone to work, exit
        if pyautogui.locateOnScreen('exit_button.jpg', grayscale=True, confidence=0.8) != None:
            print("Exiting heroes screen")
            exit_button = pyautogui.locateOnScreen('exit_button.jpg', confidence=0.8)
            exit_Button_x, exit_Button_y = pyautogui.center(exit_button)
            #print("Exit button position: X:", exit_Button_x, "Y:", exit_Button_y)
            pyautogui.moveTo(exit_Button_x, exit_Button_y)
            pyautogui.click()
            time.sleep(1)

        #ACESS THE ADVENTURE    
        if pyautogui.locateOnScreen('treasure_button.jpg', grayscale=True, confidence=0.8) != None:
            treasure_button = pyautogui.locateOnScreen('treasure_button.jpg', confidence=0.8)
            treasure_Button_x, treasure_Button_y = pyautogui.center(treasure_button)
            print("Adventure button position: X:", treasure_Button_x, "Y:", treasure_Button_y)
            pyautogui.moveTo(treasure_Button_x, treasure_Button_y)
            pyautogui.click()





