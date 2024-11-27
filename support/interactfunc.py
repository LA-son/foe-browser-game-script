import win32con
import win32api
import random
import time
from humancursor import SystemCursor

def press_a():
	win32api.keybd_event(0x41,0,0,0)
	time.sleep(random.uniform(0.049,0.099))
	win32api.keybd_event(0x41,0,win32con.KEYEVENTF_KEYUP,0)
def press_b():
	win32api.keybd_event(0x42,0,0,0)
	time.sleep(random.uniform(0.049,0.099))
	win32api.keybd_event(0x42,0,win32con.KEYEVENTF_KEYUP,0)
def press_r():
	win32api.keybd_event(0x52,0,0,0)
	time.sleep(random.uniform(0.049,0.099))
	win32api.keybd_event(0x52,0,win32con.KEYEVENTF_KEYUP,0)
def press_esc():
	win32api.keybd_event(0x1B,0,0,0)
	time.sleep(random.uniform(0.049,0.099))
	win32api.keybd_event(0x1B,0,win32con.KEYEVENTF_KEYUP,0)
def press_enter():
	win32api.keybd_event(0x0D,0,0,0)
	time.sleep(random.uniform(0.049,0.099))
	win32api.keybd_event(0x0D,0,win32con.KEYEVENTF_KEYUP,0)
def move_mouse(x,y):
	randX = random.randint(x-10,x+10)
	randY = random.randint(y-10,y+10)
	cursor = SystemCursor()
	cursor.move_to([randX,randY],steady=True)
def left_click():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(random.uniform(0.056,0.099))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)