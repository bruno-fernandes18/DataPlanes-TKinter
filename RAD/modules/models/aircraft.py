import sqlite3
from datetime import datetime
from .conn import connect_and_cursor
from .planedata import plane_objects

def boot_plane() -> None:
    conn, cursor = connect_and_cursor('planes.db')
    try:
        attributes = ', '.join(f'{key}_id INTEGER' for key in plane_objects.keys())
        foreign_keys = ', '.join(f'FOREIGN KEY({key}_id) REFERENCES {key}(id)' for key in plane_objects.keys())
        command = f'CREATE TABLE IF NOT EXISTS aircrafts (id INTEGER PRIMARY KEY, creator TEXT, created_date DATETIME, {attributes}, {foreign_keys})'
        cursor.execute(command)
        conn.commit()
    except sqlite3.Error as e:
        print(f'Error {e} when booting plane database.')
    cursor.close()
    conn.close()

def add_plane(data: tuple) -> None:
    conn, cursor = connect_and_cursor('planes.db')
    try:
        attributes = ', '.join(['?']*len(data))
        command = f'INSERT INTO aircrafts VALUES (NULL, {attributes})'
        cursor.execute(command, data)
        conn.commit()
    except sqlite3.Error as e:
        print(f'Error {e} when adding plane to database.')
    cursor.close()
    conn.close()

def view_planes() -> list:
    conn, cursor = connect_and_cursor('planes.db')
    try:
        cursor.execute('SELECT * FROM aircrafts')
        aircrafts = cursor.fetchall()
    except sqlite3.Error as e:
        print(f'Error {e} when selecting planes from database.')
    cursor.close()
    conn.close()
    return aircrafts

def search_plane(id: int) -> tuple:
    conn, cursor = connect_and_cursor('planes.db')
    try:
        cursor.execute('SELECT * FROM aircrafts WHERE id=?',(id))
        aircraft = cursor.fetchall()[0]
    except sqlite3.Error as e:
        print(f'Error {e} when searching plane from database.')
    cursor.close()
    conn.close()
    return aircraft

def delete_plane(id: int) -> None:
    conn, cursor = connect_and_cursor('planes.db')
    try:
        cursor.execute('DELETE FROM aircrafts WHERE id=?', (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f'Error {e} when deleting plane from database.')
    cursor.close()
    conn.close()

__all__ = ['boot_plane', 'add_plane', 'view_planes', 'search_plane', 'delete_plane']