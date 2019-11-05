import os
import keyboard

from managers import AudioManager, NODISPLAY, AUTOEXIT, NOSTATS, HIDEBANNER
from managers import EventManager

manager  = AudioManager()
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
    

def play_test():
    test = 'assets/Darude-Sandstorm.mp3'
    manager.init_audio_process(test, config=[NODISPLAY, AUTOEXIT, NOSTATS, HIDEBANNER])

keyboard.add_hotkey('a', play_test)
keyboard.add_hotkey('q', exit)
listen()


    
#TODO: add event system / or probably remove it entirely ...
#TODO: add audio process type / event listener
# sample audio