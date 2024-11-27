import sys
sys.path.insert(1,'/forge')
import tkinter
import win32gui
from gbg import gbgmain
from support import settings
from ge import firsthalf, secondhalf
from aid import autoaid

settings.init()
def set_stopper_true():
	settings.stopper = True
def set_stopper_false():
	settings.stopper = False
def winEnumHandler(hwnd,top_windows):
	top_windows.append((hwnd,win32gui.GetWindowText(hwnd)))
def set_foreground():
	top_windows = []
	win32gui.EnumWindows(winEnumHandler,top_windows)
	for i in top_windows:
		if 'forge' in i[1].lower():
			win32gui.ShowWindow(i[0],5)
			win32gui.SetForegroundWindow(i[0])
			break
root = tkinter.Tk()
root.geometry('200x80+1200+0')
root.attributes('-alpha',0.5,'-topmost',True)

#start button
gbgStartButton = tkinter.Button(root,text='gbg',command=lambda:[set_foreground(),set_stopper_false(),gbgmain.start_gbg_thread()])
gbgStartButton.grid(row = 0,column=0,padx=(2,2))
#stop gbg button
gbgStopButton = tkinter.Button(root,text='stop',command=lambda:[set_foreground(),set_stopper_true()])
gbgStopButton.grid(row = 0,column=1,padx=(2,2))
#gbg five
gbgFive = tkinter.Button(root,text='5',command=lambda:[set_foreground(),set_stopper_false(),gbgmain.start_five_thread()])
gbgFive.grid(row = 0,column=2,padx=(2,2))
#gbgten
gbgTen = tkinter.Button(root,text='10',command=lambda:[set_foreground(),set_stopper_false(),gbgmain.start_ten_thread()])
gbgTen.grid(row = 0,column=3,padx=(2,2))

#ge 1st half
geFirstButton = tkinter.Button(root,text='ge 1',command=lambda:[set_foreground(),firsthalf.start_1st_ge()])
geFirstButton.grid(row = 1,column=0,padx=(2,2))
#ge 2nd half
geSecondButton = tkinter.Button(root,text='ge 2',command=lambda:[set_foreground(),secondhalf.start_2nd_ge()])
geSecondButton.grid(row = 1,column=1,padx=(2,2))

#aid button
aidButton = tkinter.Button(root,text='aid',command=lambda:[set_foreground(),autoaid.start_aid()])
aidButton.grid(row=1,column=4,padx=(2,2))

root.mainloop()
