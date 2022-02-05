from pynput import keyboard
from HK_dict import HOTKEYS

with keyboard.GlobalHotKeys(HOTKEYS) as h:
    h.join()

