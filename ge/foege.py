import time
import random
import pyautogui
from support import interactfunc as button
import pytesseract
from PIL import Image

path = 'D:/forge/ge/'  

def check_1st_battle():
    for i in range(20):
        try:
            if pyautogui.locateOnScreen(path+'reload.png',region=(1083,889,250,70),grayscale=True,confidence=0.8) is not None:
                return True
                break
        except pyautogui.ImageNotFoundException:
            time.sleep(0.3)

def check_2nd_battle():
    for i in range(20):
        try:
            if pyautogui.locateOnScreen(path+'2ndbattle.png', region=(1116,900,150,40), grayscale=True, confidence=0.8):
                return True
                break
        except pyautogui.ImageNotFoundException:
            time.sleep(0.01)
        try:
            if pyautogui.locateOnScreen(path+'ok.png',region=(870,837,200,70),grayscale=True,confidence=0.8) is not None:
                return False
                break
        except pyautogui.ImageNotFoundException:
            time.sleep(0.3)
       
def check_ok():
    for i in range(20):
        try:
            if pyautogui.locateOnScreen(path+'ok.png',region=(870,837,200,70),grayscale=True,confidence=0.8) is not None:
                return True
                break
        except pyautogui.ImageNotFoundException:
            time.sleep(0.3)

def check_att():
    for i in range(20):
        try:
            x = pyautogui.center(pyautogui.locateOnScreen(path+'att_nego.png',grayscale=True,confidence=0.8))
            return x
            break
        except pyautogui.ImageNotFoundException:
            time.sleep(0.3)
'''                                          
def check_reward_2():
    for i in range(20):
        screenshot = pyautogui.screenshot(region=(695,298,450,80))
        screenshot.save(path+'reward2.png')
        with Image.open(path+'reward2.png','r') as im:
            tess = pytesseract.image_to_string(im, config='--psm 13')
            if 'Personal' in tess:
                return True
                break
        time.sleep(0.3)
   
def check_ge_point():
    for i in range(20):
        screenshot = pyautogui.screenshot(region=(695,298,450,80))
        screenshot.save(path+'point.png')
        with Image.open(path+'point.png','r') as im:
            tess = pytesseract.image_to_string(im, config='--psm 13')
            if 'Guild' in tess:
                return True
                break
        time.sleep(0.3)
'''
def hit(x,y):
    button.move_mouse(x,y) #move to node
    time.sleep(random.uniform(0.15,0.25))
    button.left_click() #click node
    a, b = check_att() #get attack button location
    time.sleep(random.uniform(0.2,0.3))
    button.move_mouse(a,b) #move to attack button
    button.left_click()
    time.sleep(random.uniform(0.3,0.5))
    if check_1st_battle() == True:  #check if 1st battle screen show
        button.press_r()
        time.sleep(random.uniform(0.29,0.44))
        button.press_b()
    if check_2nd_battle() == True: #check if there's 2nd battle
        time.sleep(0.3)
        button.press_b()
        if check_ok() == True:  #check if result battle show
            time.sleep(random.uniform(0.2,0.6))
            button.press_esc()
    elif check_2nd_battle() == False:
        time.sleep(random.uniform(0.2,0.6))
        button.press_esc()
    #if check_ge_point() == True:
    #    time.sleep(random.uniform(0.15,0.34))
    #    button.press_esc()
    time.sleep(0.5)
    
def collect(x,y):
    button.move_mouse(x,y)
    time.sleep(random.uniform(0.39,0.53))
    for i in range(5):
        button.left_click()
        time.sleep(random.uniform(0.17,0.34))
    time.sleep(5)
