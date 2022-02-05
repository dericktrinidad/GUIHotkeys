import sqlite3

def create_table():
    conn = sqlite3.connect('function.db')
    c = conn.cursor()
    #create table
    c.execute('''CREATE TABLE pyfunction (func_defination TEXT)''')

def delete_from_db(func_to_del):
    conn = sqlite3.connect('function.db')
    # init database
    c = conn.cursor()
    #delete from table
    c.execute('DELETE FROM pyfunction WHERE func_defination = ?', (func_to_del,))
    conn.commit()
def add_function_db(function):
    conn = sqlite3.connect('function.db')
    c = conn.cursor()
    c.execute("INSERT INTO pyfunction (func_defination) VALUEs (?)",(function,))
    conn.commit()

def list_db():
    conn = sqlite3.connect('function.db')
    # init database
    c = conn.cursor()
    c.execute("SELECT * FROM pyfunction;")
    tuple_db = c.fetchall()
    db_list = [function for t in tuple_db for function in t]
    return db_list

def getlibraries():
    libraries = ['import keyboard', 'import pyautogui']
    return libraries

# def checklibraries():
#     libs = getlibraries()
#     with open("hk_fun.py", "r") as f:
#         if not libs in f.read():
#             with open("hk_fun.py", "a") as f:
#                 f.write(0, "\n".join(libs))

def append_functions(arr_functions, function_name):
    output = "\n\t".join(arr_functions)
    hotkey_function = "\ndef " + function_name + "():\n\t" + output
    with open("hk_fun.py", "a") as f:
        lines = hotkey_function
        f.write(lines)

def writefunction(arr_functions):
    with open("hk_fun.py", "w") as f:
        lines = "\n".join(arr_functions)
        f.write(lines)

def update_hk_functions():
    updated_list = getlibraries() + list_db()
    with open("hk_fun.py", "w") as f:
        lines = "\n".join(updated_list)
        f.write(lines)


def add_hk_db(key, function_name, arr_output):
    #Format Function
    output = "\n\t".join(arr_output)
    hotkey_function = "def " + function_name + "():\n\t" + output
    add_function_db(hotkey_function)
    #Convert database to a list and write to hotkey_function.py
    # writefunction(getlibraries() + list_db())