import time
import pyautogui
from support import interactfunc as button
from support import settings
import random

waitTime = 0.3
path='D:/forge/gbg/'
def check_attack():
	for i in range(20):
		try:
			if settings.stopper is True:
				return
			if pyautogui.locateOnScreen(path+'attack.png',region=(785,634,150,150),grayscale=True,confidence=0.8) is not None:
				return True
				break
		except pyautogui.ImageNotFoundException:
			time.sleep(waitTime)
def check_army():
	for i in range(20):
		try:
			if settings.stopper is True:
				return
			if pyautogui.locateOnScreen(path+'army.png',region=(849,212,50,55),grayscale=True,confidence=0.8) is not None:
				return True
				break
		except pyautogui.ImageNotFoundException:
			time.sleep(waitTime)
def check_2nd():
	for i in range(20):
		try:
			if settings.stopper is True:
				return
			if pyautogui.locateOnScreen(path+'2nd.png',region=(646,892,200,55),grayscale=True,confidence=0.8) is not None:
				return True
				break
		except pyautogui.ImageNotFoundException:
			time.sleep(0.01)
		try:
			if settings.stopper is True:
				return
			if pyautogui.locateOnScreen(path+'ok.png',region=(853,900,180,60),grayscale=True,confidence=0.8) is not None:
				break
		except pyautogui.ImageNotFoundException:
			time.sleep(waitTime)
def check_result():
	for i in range(20):
		try:
			if settings.stopper is True:
				return
			if pyautogui.locateOnScreen(path+'ok.png',region=(853,900,180,60),grayscale=True,confidence=0.8) is not None:
				return True
				break
		except pyautogui.ImageNotFoundException:
			time.sleep(waitTime)
def check_reward():
	for i in range(20):
		try:
			if settings.stopper is True:
				return
			if pyautogui.locateOnScreen(path+'reward.png',region=(818,318,65,50),grayscale=True,confidence=0.8) is not None:
				return True
				break
		except pyautogui.ImageNotFoundException:
			time.sleep(0.01)
		try:
			if settings.stopper is True:
				return
			if pyautogui.locateOnScreen(path+'attack.png',region=(785,634,150,150),grayscale=True,confidence=0.8) is not None:
				break
		except pyautogui.ImageNotFoundException:
			time.sleep(waitTime)
def give_ran():
	return random.uniform(0.4,0.7)
def hit():
	if check_attack() is True:
		time.sleep(give_ran())
		button.press_a()
	if check_army() is True:
		time.sleep(give_ran())
		button.press_r()
		time.sleep(give_ran())
		button.press_b()
	if check_2nd() is True:
		time.sleep(give_ran())
		button.press_b()
	if check_result() is True:
		time.sleep(give_ran())
		button.press_esc()
	if check_reward() is True:
		time.sleep(give_ran())
		button.press_esc()
def flush():
	interactfunc.move_mouse(586,470)
	for i in range(9):
		if settings.stopper is True:
				return
		interactfunc.left_click()
		time.sleep(random.uniform(0.1,0.2))
def load():
	for i in range(9):
		if settings.stopper is True:
				return
		interactfunc.left_click()
		time.sleep(random.uniform(0.1,0.2))
