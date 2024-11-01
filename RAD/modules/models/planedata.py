import sqlite3
from .conn import connect_and_cursor

plane_objects = {
    'approach': ('ias INTEGER', 'mcs INTEGER', 'rod INTEGER'),
    'climb150': ('has_data BOOLEAN','ias INTEGER', 'roc INTEGER'),
    'climb240': ('has_data BOOLEAN','ias INTEGER', 'roc INTEGER'),
    'climbmach': ('has_data BOOLEAN','ias FLOAT', 'roc INTEGER'),
    'cruise': ('tas INTEGER', 'mach FLOAT', 'ceiling INTEGER', 'range INTEGER'),
    'descent100': ('ias INTEGER', 'rod INTEGER'),
    'initialclimb': ('ias INTEGER', 'roc INTEGER'),
    'initialdescent': ('has_data BOOLEAN','ias FLOAT', 'roc INTEGER'),
    'landing': ('vat INTEGER', 'distance INTEGER'),
    'takeoff': ('mtow INTEGER', 'distance INTEGER', 'v2 INTEGER'),
    'technical': ('manufacturer TEXT', 'birth INTEGER', 'model TEXT', 'variation TEXT', 'wingspan FLOAT', 'wingposition TEXT', 'engineposition TEXT', 'tailconfiguration TEXT', 'landinggear TEXT', 'length FLOAT', 'height FLOAT', 'euanalysis TEXT')
}

plane_reference = {
    'approach': ('ias', 'mcs', 'rod'),
    'climb150': ('ias', 'roc'),
    'climb240': ('ias', 'roc'),
    'climbmach': ('ias', 'roc'),
    'cruise': ('tas', 'mach', 'ceiling', 'range'),
    'descent100': ('ias', 'rod'),
    'initialclimb': ('ias', 'roc'),
    'initialdescent': ('ias', 'roc'),
    'landing': ('vat', 'distance'),
    'takeoff': ('mtow', 'distance', 'v2'),
    'technical': ('manufacturer', 'birth', 'model', 'variation', 'wingspan', 'wingposition', 'engineposition', 'tailconfiguration', 'landinggear', 'length', 'height')
}

plane_order = ('approach', 'climb150', 'climb240', 'climbmach', 'cruise', 'descent100', 'initialclimb', 'initialdescent', 'landing', 'takeoff', 'technical')

def boot_parts():
    conn,cursor = connect_and_cursor('planes.db')
    for key in plane_objects:
        try:
            attributes = ', '.join(plane_objects[key])
            command = f'CREATE TABLE IF NOT EXISTS {key} (id INTEGER PRIMARY KEY, {attributes})'
            cursor.execute(command)
            conn.commit()
        except sqlite3.Error as e:
            print(f'Error {e} when booting {key} database')
    cursor.close()
    conn.close()

def insert_part(table: str, data_to_insert: tuple):
    conn, cursor = connect_and_cursor('planes.db')
    if table in plane_objects:
        try:
            attributes = ', '.join(['?']*len(data_to_insert))
            command = f'INSERT INTO {table} VALUES (NULL, {attributes})'
            cursor.execute(command, data_to_insert)
            conn.commit()
        except sqlite3.Error as e:
            print(f'Error {e} when inserting data in {table} database')
    else:
        print("There isn't such table...")
    part_id = cursor.lastrowid
    
    cursor.close()
    conn.close()
    
    return part_id

def get_parts(id: int):
    conn, cursor = connect_and_cursor('planes.db')
    parts = {}
    try:
        for key in plane_objects:
            command = f'SELECT * FROM {key} WHERE id=?'
            cursor.execute(command,(id,))
            information = cursor.fetchall()
            parts[key] = information[0]
    except sqlite3.Error as e:
        print(f'Error {e} when getting information from Airplane parts.')
    cursor.close()
    conn.close()
    return parts

def get_specific_part(table: str, id: int):
    conn, cursor = connect_and_cursor('planes.db')
    try:
        command = f'SELECT * FROM {table} WHERE id=?'
        cursor.execute(command,(str(id),))
        infolist = cursor.fetchall()
    except sqlite3.Error as e:
        print(f'Error {e} when getting information from Airplane parts.')
    cursor.close()
    conn.close()
    return infolist

def update_parts(table: str, id: int, data_to_update: tuple):
    conn, cursor = connect_and_cursor('planes.db')
    try:
        attributes = ', '.join([f"{piece} = ?" for piece in plane_reference[table]])
        command = f'UPDATE {table} SET {attributes} WHERE id={id}'
        cursor.execute(command, data_to_update)
        conn.commit()
    except sqlite3.Error as e:
        print(f'Error {e} when updating data in {table} database.')
    cursor.close()
    conn.close()

def delete_parts(id_tuple: tuple):
    conn, cursor = connect_and_cursor('planes.db')
    try:
        for i in range(len(plane_objects)):
            command = f'DELETE FROM {plane_order[i]} WHERE id=?'
            cursor.execute(command,(id_tuple[i],))
        conn.commit()
    except sqlite3.Error as e:
        print(f'Error {e} when deleting parts from tables')
    cursor.close()
    conn.close()

__all__ = ['boot_parts', 'insert_part', 'get_parts', 'get_specific_part', 'update_parts', 'delete_parts']