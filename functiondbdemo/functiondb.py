import sqlite3
#CREATE TABLE AND CREATE CURSOR
def Createtableaddfunc():
    conn = sqlite3.connect('function.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE student (Number REAL, stud_name TEXT)''')

    #STORE gfg() function SQLITE TABLE as pyfunction:
    conn = sqlite3.connect('function.db')
    # init database
    c = conn.cursor()
    #create table
    c.execute('''CREATE TABLE pyfunction (func_defination TEXT)''')
    #store py function
    code = """ def gfg(): print("Thank you geeksforgeeks) """
    c.execute("INSERT INTO pyfunction (func_defination) VALUEs (?)",(code,))
    #terminate transaction
    conn.commit()

# #STORE maximum() function SQLITE TABLE as pyfunction:
def createtableaddtwofunc():
    conn = sqlite3.connect('function.db')
    # init database
    c = conn.cursor()
    #create table
    c.execute('''CREATE TABLE pyfunction (func_defination TEXT)''')
    #stor max() function
    def1 = """ def maximum(): print("Thank you geeksforgeeks) """
    c.execute("INSERT INTO pyfunction (func_defination) VALUEs (?)",(def1,))
    #store py function
    def2 = """a"""
    c.execute("INSERT INTO pyfunction (func_defination) VALUEs (?)",(def2,))
    #display content of table
    c.execute("SELECT * FROM pyfunction;")
    print(c.fetchall())
    #terminate transaction
    conn.commit()

def list_all():
    #LIST FROM DATABASE
    conn = sqlite3.connect('function.db')
    # init database
    c = conn.cursor()
    # #delete from table
    # c.execute('''DELETE FROM pyfunction ''')
    c.execute("SELECT * FROM pyfunction;")
    print(c.fetchall())

#DELETE FROM DATABASE
def delete_from_db(func_to_del):
    conn = sqlite3.connect('function.db')
    # init database
    c = conn.cursor()
    #delete from table
    c.execute('DELETE FROM pyfunction WHERE func_defination = ?', (func_to_del,))
    conn.commit()
def add_function_db(function):
    conn = sqlite3.connect('function.db')
    # init database
    c = conn.cursor()
    #store py function
    c.execute("INSERT INTO pyfunction (func_defination) VALUEs (?)",(function,))
    # #display content of table
    # c.execute("SELECT * FROM pyfunction;")
    # print(c.fetchall())
    #terminate transaction
    conn.commit()

def writefunction(arr_functions):
    with open("hk_functions_db.py", "w") as f:
        lines = "\n".join(arr_functions)
        # print(lines)
        f.write(lines)
def store_db():
    conn = sqlite3.connect('function.db')
    # init database
    c = conn.cursor()
    c.execute("SELECT * FROM pyfunction;")
    tuple_db = c.fetchall()
    db_list =[function for t in tuple_db for function in t]
    return db_list

if __name__ == '__main__':
    #ADD FUNCTION:
    add_function_db("def volumeup_hk(): print('Volume Up')") # works
    #DELETE FUNCTION:
    # delete_from_db("d") # works
    #MUST CONVERT DB INFO INTO LIST
    print(store_db()) #DUE
    #MUST WRITE LIST INTO hk_functions_db.py
    writefunction(store_db())