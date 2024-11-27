import pyautogui
import time

path = r"D:/forge/gbg/attr_number/"
def check_num(region):
    #---check type of number
    numbers = []
    try:
        im = pyautogui.locateOnScreen(path+'0.png',region=(region),grayscale=True,confidence=0.8)
        numbers.append(0)
    except pyautogui.ImageNotFoundException:
        time.sleep(0.01)
    try:
        im = pyautogui.locateOnScreen(path+'1.png',region=(region),grayscale=True,confidence=0.8)
        numbers.append(1)
    except pyautogui.ImageNotFoundException:
        time.sleep(0.01)
    try:
        im = pyautogui.locateOnScreen(path+'2.png',region=(region),grayscale=True,confidence=0.8)
        numbers.append(2)
    except pyautogui.ImageNotFoundException:
        time.sleep(0.01)
    try:    
        im = pyautogui.locateOnScreen(path+'3.png',region=(region),grayscale=True,confidence=0.9)
        numbers.append(3)
    except pyautogui.ImageNotFoundException:
        time.sleep(0.01)
    try:
        im = pyautogui.locateOnScreen(path+'4.png',region=(region),grayscale=True,confidence=0.8)
        numbers.append(4)
    except pyautogui.ImageNotFoundException:
        time.sleep(0.01)
    try:
        im = pyautogui.locateOnScreen(path+'5.png',region=(region),grayscale=True,confidence=0.8)
        numbers.append(5)
    except pyautogui.ImageNotFoundException:
        time.sleep(0.01)
    try:
        im = pyautogui.locateOnScreen(path+'6.png',region=(region),grayscale=True,confidence=0.8)
        numbers.append(6)
    except pyautogui.ImageNotFoundException:
        time.sleep(0.01)
    try:
        im = pyautogui.locateOnScreen(path+'7.png',region=(region),grayscale=True,confidence=0.8)
        numbers.append(7)
    except pyautogui.ImageNotFoundException:
        time.sleep(0.01)
    try:
        im = pyautogui.locateOnScreen(path+'8.png',region=(region),grayscale=True,confidence=0.8)
        numbers.append(8)
    except pyautogui.ImageNotFoundException:
        time.sleep(0.01)
    try:
        im = pyautogui.locateOnScreen(path+'9.png',region=(region),grayscale=True,confidence=0.8)
        numbers.append(9)
    except pyautogui.ImageNotFoundException:
        time.sleep(0.01)
    #---check if no number
    if not numbers:
        return None
    #---check if duplicate
    result = []
    distance = pow(5,2)
    for num in numbers:
        ele = pyautogui.locateAllOnScreen(path+str(num)+'.png',region=(region),grayscale=True,confidence=0.8)
        elements = []
        for element in ele:
            i = pyautogui.center(element)
            if all(map(lambda x: pow(i[0] - x[0],2) > distance,elements)):
                elements.append(i)
        for item in elements:
            res = [item[0],num]
            result.append(res)
    #---return nested list [positon,number] then sort
    #---seperate num and return
    my_num = []
    for the_num in sorted(result):
        my_num.append(the_num[1])
    return ''.join(map(str,my_num))
