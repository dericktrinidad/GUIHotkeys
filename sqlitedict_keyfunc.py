from sqlitedict import SqliteDict
# from pynput import keyboard
import pynput
# from hk_fun import *
import hk_fun
def init_sqlitedict():
    with SqliteDict('sqlitedict.db') as sqldict:
        sqldict.close()

def save_hk_dict(key, function_name):
    with SqliteDict('sqlitedict.db') as sqldict:
        sqldict[key] = eval('hk_fun.' + function_name)
        sqldict.commit()
    return True

def remove_hk_dict(key):
    with SqliteDict('sqlitedict.db') as sqldict:
        del sqldict[key]
        sqldict.commit()

def get_function_name(hotkey):
    with SqliteDict('sqlitedict.db') as sqldict:
        function_reg = str(sqldict[hotkey]).split(" ")
        function_name = function_reg[1]
        return function_name

def execute_hotkey():
    with SqliteDict('sqlitedict.db') as sqldict:
        with pynput.keyboard.GlobalHotKeys(sqldict) as h:
            h.join()
