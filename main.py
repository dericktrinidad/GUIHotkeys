from sqlitedict import SqliteDict
from pynput import keyboard
import os.path
import sqlite3_opfuncs as func_db
import sqlitedict_keyfunc as hk_dict
from sqlitedict import SqliteDict
import time
import importlib
import sys

def init_databases():
    #CHECK IF FUNCTION.DB EXIST IN DIRECTORY
    if not os.path.exists('function.db'):
        func_db.create_table()
    # CHECK IF SQLITEDICT EXIST IN DRIECTORY
    if not os.path.exists('sqlitedict.db'):
        hk_dict.init_sqlitedict()

def create_hotkey(key, function_name, arr_output):
    #write function to hk fun
    func_db.write_hk_fun(key, function_name, arr_output)

#save key and function in dictionary database
def save_hotkey_db(key, function_name):
    hk_dict.save_hk_dict(key, function_name)

#Remove_hotkey from database
def remove_hotkey(key):
    #get function
    function = get_fullfunction(key)
    # remove function
    func_db.delete_from_db(function)
    #del dict
    hk_dict.remove_hk_dict(key)
    #print function in hk_fun.py
    func_db.update_hk_functions()


#FUTURE GUI: display all hotkeys in database
def get_hotkeys():
    pass


def get_fullfunction(key):
    #find function name from dictionary from key
    function_name = hk_dict.get_function_name(key)
    List_functions = func_db.list_db()
    for function in List_functions:
        if function_name in function:
            return function
        else:
            print("function does not exist")
def create_hotkeys(key, func_name, func_arr):
    #write functions to hk_fun
    func_db.append_functions(func_arr,func_name)
    #reload hk_fun.py
    importlib.reload(sys.modules['hk_fun'])
    #store functions in db
    func_db.add_hk_db(key, func_name, func_arr)
    #store functions to dict
    hk_dict.save_hk_dict(key, func_name)


if __name__ == '__main__':
    try:
        #create/check data bases
        init_databases()

        #read libraries
        #add_hk

        # create_hotkeys('<alt>+<ctrl>+f+1', 'volume_up', ["print('Volume Up')", "pyautogui.press('volumeup')"])
        # create_hotkeys('<alt>+<ctrl>+f+2', 'volume_down', ["print('Volume Down')", "pyautogui.press('volumedown')"])
        # # remove hk
        # remove_hotkey('<alt>+<ctrl>+f+1')
        # # remove_hk2
        # remove_hotkey('<alt>+<ctrl>+f+2')

        # RUN_HOTKEYS
        hk_dict.execute_hotkey()

    except IndexError as e:
        print(e)


# #COMMENT OUT WHEN NOT USING
# #snakviz tool to test runtime speed of code
# def snakeviz():
#     import cProfile
#     import pstats
#
#     #enter any function here to test runtime speed
#     with cProfile.Profile() as pr:
#         # create_hotkeys('<alt>+<ctrl>+f+1', 'volume_up', ["print('Volume Up')", "pyautogui.press('volumeup')"])
#         remove_hotkey('<alt>+<ctrl>+f+1')
#     stats = pstats.Stats(pr)
#     stats.sort_stats(pstats.SortKey.TIME)
#     #stats.print_stats()
#     #dump stats as a file
#     stats.dump_stats(filename='main.prof')
#     #EXICUTE DUMP FILE WITH FOLLOWING COMMANDS:
#     #snakeviz ./main.prof