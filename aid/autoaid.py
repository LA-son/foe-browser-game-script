import time
from support import interactfunc as button
import pyautogui

path = 'D:/forge/aid/'
def check_if_server_loaded():
    for i in range(20):
        try:
            if pyautogui.locateOnScreen(path+'off.png',region=(1873,154,40,40),grayscale=True,confidence=0.8) is not None:
                return True
                break
        except pyautogui.ImageNotFoundException:
            time.sleep(0.5)
    return False
def spam_esc():
    for i in range(10):
        button.press_esc()
        time.sleep(0.3)
def check_aid_window_up_or_down():
    for i in range(20):
        try:
            if pyautogui.locateOnScreen(path+'window_aid_button.png',region=(853,988,60,40),grayscale=True,confidence=0.8) is not None:
                return 'Down'
                break
        except pyautogui.ImageNotFoundException:
            time.sleep(0.1)
        try:
            if pyautogui.locateOnScreen(path+'window_aid_button.png',region=(853,827,60,40),grayscale=True,confidence=0.8) is not None:
                return 'Up'
                break
        except pyautogui.ImageNotFoundException:
            time.sleep(0.1)
def check_aid(region):
    for i in range(10):
        try:
            if pyautogui.locateOnScreen(path+'aid.png',region=(region),grayscale=True,confidence=0.8) is not None:
                return True
        except pyautogui.ImageNotFoundException:
            time.sleep(0.2)
def collect():
    for i in range(52):
        try:
            if pyautogui.locateOnScreen(path+'collect.png',region=(545,969,95,30,),grayscale=True,confidence=0.8) is not None:
                return True
                break
        except pyautogui.ImageNotFoundException:
            time.sleep(5)
def reward_close():
    for i in range(10):
        try:
            if pyautogui.locateOnScreen(path+'reward_close.png',region=(924,755,80,25),grayscale=True,confidence=0.8) is not None:
                return True
                break
        except pyautogui.ImageNotFoundException:
            time.sleep(0.3)
def click_aid(region,aidPos):
    if check_aid((region)) is True:
        button.move_mouse(aidPos[0],aidPos[1])
        time.sleep(0.15)
        button.left_click()
    if collect() is True:
        button.move_mouse(555,979)
        button.left_click()
    time.sleep(0.3)
    if reward_close() is True:
        button.move_mouse(934,765)
        button.left_click()
    time.sleep(0.3)
def switch_server(server):
    time.sleep(0.12)
    button.move_mouse(424,78)
    time.sleep(0.1)
    button.left_click()
    time.sleep(0.1)
    pyautogui.typewrite(server)
    time.sleep(0.1)
    button.press_enter()
def aiding():
    spam_esc()
    aidWindowPos = check_aid_window_up_or_down()
    if aidWindowPos == "Down":
        button.move_mouse(883,1009)
        time.sleep(0.2)
        button.left_click()
    elif aidWindowPos == "Up":
        button.move_mouse(887,847)
        time.sleep(0.2)
        button.left_click()
    neighbor = [463,990]
    click_aid((453,980,45,23),neighbor) #neighbor
    guild = [648,986]
    click_aid((638,976,50,28),guild) #guild
    friend = [836,985]
    click_aid((826,975,50,28),friend) #friend
    time.sleep(0.3)
    button.move_mouse(345,846)
    time.sleep(0.1)
    button.left_click()
def start_aid():
    servers = ['https://en3.forgeofempires.com/game/index?','https://en12.forgeofempires.com/game/index?','https://en13.forgeofempires.com/game/index?']
    time.sleep(0.5)
    aiding()
    for server in servers:
        switch_server(server)
        time.sleep(6)
        if check_if_server_loaded() is True:
            aiding()
        else:
            break


