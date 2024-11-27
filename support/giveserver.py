import pyautogui
import time
import pytesseract
from PIL import Image

path = 'D:/forge/support/'
def get_server():
	x = pyautogui.screenshot(region=(190,63,215,35))
	x.save(path+'url.png')
	with Image.open(path+'url.png','r') as im:
		server = pytesseract.image_to_string(im,config='--psm 13')
	if 'en18' in server:
		return "T"
	elif 'en3' in server:
		return "C"
	elif 'en12' in server:
		return "MK"
	elif 'en13' in server:
		return "N"
	else:
		return None