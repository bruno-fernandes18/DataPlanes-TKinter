import sqlite3

def boot_user():
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, password TEXT NOT NULL)'
            )
            conn.commit()
        except sqlite3.Error as e:
            print(f'Error {e} when booting user database.')

def add_user(name: str, password: str):
    boot_user()
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO users VALUES (NULL, ?, ?)', (name, password))
            conn.commit()
        except sqlite3.Error as e:
            print(f'Error {e} when adding user to database.')

def view_users() -> list:
    boot_user()
    users: list = []
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT * FROM users')
            users = cursor.fetchall()
        except sqlite3.Error as e:
            print(f'Error {e} when selecting user from database.')
    return users

def search_user(name: str) -> list:
    boot_user()
    user: list = []
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT * FROM users WHERE name=?', (name,))
            user = cursor.fetchall()
        except sqlite3.Error as e:
            print(f'Error {e} when searching user from database.')
    return user

def update_user(id: int, name: str, password: str) -> None:
    boot_user()
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                'UPDATE users SET name=?, password=? WHERE id=?',
                (name, password, id),
            )
            conn.commit()
        except sqlite3.Error as e:
            print(f'Error {e} when updating user to database.')

def delete_user(id: int) -> None:
    boot_user()
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM users WHERE id=?', (id,))
            conn.commit()
        except sqlite3.Error as e:
            print(f'Error {e} when deleting user from database.')

__all__ = ['boot_user', 'add_user', 'view_users', 'search_user', 'update_user', 'delete_user']