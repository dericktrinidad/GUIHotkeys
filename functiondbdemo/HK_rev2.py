from pynput import keyboard
from rev_1.HK_dict import HOTKEYS

with keyboard.GlobalHotKeys(HOTKEYS) as h:
    h.join()

