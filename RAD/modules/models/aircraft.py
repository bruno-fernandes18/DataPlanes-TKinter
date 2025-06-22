import sqlite3
from datetime import datetime
from .planedata import plane_objects

def boot_plane() -> None:
    with sqlite3.connect('planes.db') as conn:
        cursor = conn.cursor()
        try:
            attributes = ', '.join(f'{key}_id INTEGER' for key in plane_objects.keys())
            foreign_keys = ', '.join(
                f'FOREIGN KEY({key}_id) REFERENCES {key}(id)' for key in plane_objects.keys()
            )
            command = (
                f'CREATE TABLE IF NOT EXISTS aircrafts '
                f'(id INTEGER PRIMARY KEY, creator TEXT, created_date DATETIME, {attributes}, {foreign_keys})'
            )
            cursor.execute(command)
            conn.commit()
        except sqlite3.Error as e:
            print(f'Error {e} when booting plane database.')

def add_plane(data: tuple) -> None:
    with sqlite3.connect('planes.db') as conn:
        cursor = conn.cursor()
        try:
            attributes = ', '.join(['?'] * len(data))
            command = f'INSERT INTO aircrafts VALUES (NULL, {attributes})'
            cursor.execute(command, data)
            conn.commit()
        except sqlite3.Error as e:
            print(f'Error {e} when adding plane to database.')

def view_planes() -> list:
    with sqlite3.connect('planes.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT * FROM aircrafts')
            aircrafts = cursor.fetchall()
        except sqlite3.Error as e:
            print(f'Error {e} when selecting planes from database.')
        return aircrafts

def search_plane(id: int) -> tuple:
    with sqlite3.connect('planes.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT * FROM aircrafts WHERE id=?', (id,))
            aircraft = cursor.fetchall()[0]
        except sqlite3.Error as e:
            print(f'Error {e} when searching plane from database.')
        return aircraft

def delete_plane(id: int) -> None:
    with sqlite3.connect('planes.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM aircrafts WHERE id=?', (id,))
            conn.commit()
        except sqlite3.Error as e:
            print(f'Error {e} when deleting plane from database.')

__all__ = ['boot_plane', 'add_plane', 'view_planes', 'search_plane', 'delete_plane']