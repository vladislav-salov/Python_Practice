import keyboard
from time import sleep
import pyperclip

def keyboard_printing():
    for line in pyperclip.paste().split(chr(13)):
        for s in line:
            keyboard.write(s)
            if keyboard.is_pressed('esc'):
                return 0

keyboard.add_hotkey('ctrl + shift + p', keyboard_printing)
keyboard.wait('esc')
