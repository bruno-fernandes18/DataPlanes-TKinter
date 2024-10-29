import sqlite3
from .conn import connect_and_cursor
from .planedata import plane_objects

def boot_plane() -> None:
    conn, cursor = connect_and_cursor('planes.db')
    try:
        attributes = ', '.join(f'{key}_id INTEGER, FOREIGN KEY({key}_id) REFERENCES {key}(id)' for key in plane_objects.keys())
        command = f'CREATE TABLE IF NOT EXISTS aircrafts (id INTEGER PRIMARY KEY, {attributes})'
        cursor.execute(command)
        conn.commit()
    except sqlite3.Error as e:
        print(f'Error {e} when booting plane database.')
    cursor.close()
    conn.close()

def add_plane(parts_id: tuple) -> None:
    conn, cursor = connect_and_cursor('planes.db')
    try:
        attributes = ', '.join(['?']*len(parts_id))
        command = f'INSERT INTO aircrafts VALUES (NULL, {attributes})'
        cursor.execute(command, (parts_id))
        conn.commit()
    except sqlite3.Error as e:
        print(f'Error {e} when adding plane to database.')
    cursor.close()
    conn.close()

def view_planes() -> None:
    conn, cursor = connect_and_cursor('planes.db')
    try:
        cursor.execute('SELECT * FROM aircrafts')
    except sqlite3.Error as e:
        print(f'Error {e} when selecting planes from database.')
    cursor.close()
    conn.close()

def search_plane(id: int) -> list:
    conn, cursor = connect_and_cursor('planes.db')
    try:
        cursor.execute('SELECT * FROM aircrafts WHERE id=?',(id))
        aircraft_list = cursor.fetchall()
    except sqlite3.Error as e:
        print(f'Error {e} when searching plane from database.')
    cursor.close()
    conn.close()
    return aircraft_list

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