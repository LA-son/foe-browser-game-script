import time
import threading
from gbg.gbgfunc import *
from support.interactfunc import *
from support import giveserver, givenum, settings

attrRegion = 333,161,60,25
rangeUnit = 936,657
canonUnit = 881,657
firstSlot = 680,735

def five():
	baseAttr = givenum.check_num(attrRegion)
	while True:
		if settings.stopper is True:
			print('gbg stopped')
			break
		if int(givenum.check_num(attrRegion)) > (int(baseAttr)+4):
			break
		hit()
def ten():
	baseAttr = givenum.check_num(attrRegion)
	while True:
		if settings.stopper is True:
			print('gbg stopped')
			break
		if int(givenum.check_num(attrRegion)) > (int(baseAttr)+9):
			break
		hit()
def gbg_init():
	print('gbg start')
	server = giveserver.get_server()
	if server is None:
		print('server get error')
	if server == "T":
		for i in range(600):
			if settings.stopper is True:
				print('gbg stopped')
				break
			attrNum = givenum.check_num(attrRegion)
			if attrNum is None:
				break
			if int(attrNum) > 104:
				break
			hit()
	if server == "C":
		for i in range(200):
			if settings.stopper is True:
				print('gbg stopped')
				break
			attrNum = givenum.check_num(attrRegion)
			if attrNum is None:
				break
			if int(attrNum) > 29:
				break
			hit()
	if server == "MK":
		for i in range(250):
			if settings.stopper is True:
				print('gbg stopped')
				break
			attrNum = givenum.check_num(attrRegion)
			if attrNum is None:
				break
			if int(attrNum) > 19:
				break
			hit()

def start_gbg_thread():
	t1 = threading.Thread(target = gbg_init)
	t1.start()
def start_five_thread():
	t2 = threading.Thread(target = five)
	t2.start()
def start_ten_thread():
	t3 = threading.Thread(target = ten)
	t3.start()