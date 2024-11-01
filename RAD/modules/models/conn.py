import sqlite3

def connect_and_cursor(db:str):
    con = sqlite3.connect(db)
    cursor = con.cursor()
    return con, cursor