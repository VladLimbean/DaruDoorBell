import os
import keyboard

from managers import NODISPLAY, AUTOEXIT, NOSTATS, HIDEBANNER
from managers import EventManager
from managers import manager, profile 

event    = EventManager()

def listen():
    print('Listening')
    manager.start()
    keyboard.wait(hotkey='q')
    
def exit():
    print('Exiting')
    try:
        manager.stop()
        print('Manager process terminated')
        
    except:
        print('Could not terminate manager')
    
keyboard.add_hotkey('a', profile.click)
keyboard.add_hotkey('q', exit)
listen()
