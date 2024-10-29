import sqlite3
from .conn import connect_and_cursor

def boot_user():
    conn, cursor = connect_and_cursor('users.db')
    try:
        cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, password TEXT NOT NULL)')
        conn.commit()
    except sqlite3.Error as e:
        print(f'Error {e} when booting user database.')
    cursor.close()
    conn.close()

def add_user(name: str, password: str):
    conn, cursor = connect_and_cursor('users.db')
    try:
        cursor.execute('INSERT INTO users VALUES (NULL, ?, ?)', (name, password))
        conn.commit()
    except sqlite3.Error as e:
        print(f'Error {e} when adding user to database.')
    cursor.close()
    conn.close()

def view_users():
    conn, cursor = connect_and_cursor('user.db')
    try:
        cursor.execute('SELECT * FROM users')
    except sqlite3.Error as e:
        print(f'Error {e} when selecting user from database.')
    cursor.close()
    conn.close()

def search_user(name: str):
    conn, cursor = connect_and_cursor('user.db')
    try:
        cursor.execute('SELECT * FROM users WHERE name=?',(name))
    except sqlite3.Error as e:
        print(f'Error {e} when searching user from database.')
    cursor.close()
    conn.close()

def update_user(id: int, name: str, password: str):
    conn, cursor = connect_and_cursor('user.db')
    try:
        cursor.execute('UPDATE users SET name=?, password=? WHERE id=?', (name,password,id))
        cursor.commit()
    except sqlite3.Error as e:
        print(f'Error {e} when updating user to database.')
    cursor.close()
    conn.close()

def delete_user(id: int):
    conn, cursor = connect_and_cursor('user.db')
    try:
        cursor.execute('DELETE FROM users WHERE id=?', (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f'Error {e} when deleting user from database.')
    cursor.close()
    conn.close()

__all__ = ['boot_user', 'add_user', 'view_users', 'search_user', 'update_user', 'delete_user']