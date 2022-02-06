from sqlitedict import SqliteDict
from pynput import keyboard
# from HK_output import *
import HK_output

def add_hotkey(key, function_name):

    #Add input hot key to database
    with SqliteDict('sqlitedict.db') as sqldict:
        sqldict[key] = function_name
        sqldict.commit()

def remove_hotkey(key):
    with SqliteDict('sqlitedict.db') as sqldict:
        del sqldict[key]
        sqldict.commit()
def execute_hotkey():
    with SqliteDict('sqlitedict.db') as sqldict:
        with keyboard.GlobalHotKeys(sqldict) as h:
            h.join()
if __name__ == '__main__':
    # execute_hotkey()
    # remove_hotkey('<alt>+<ctrl>+f+1')
    add_hotkey('<ctrl>+1', HK_output.function_1)
