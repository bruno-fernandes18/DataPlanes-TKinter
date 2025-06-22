import sqlite3

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
    with sqlite3.connect('planes.db') as conn:
        cursor = conn.cursor()
        for key in plane_objects:
            try:
                attributes = ', '.join(plane_objects[key])
                command = f'CREATE TABLE IF NOT EXISTS {key} (id INTEGER PRIMARY KEY, {attributes})'
                cursor.execute(command)
                conn.commit()
            except sqlite3.Error as e:
                print(f'Error {e} when booting {key} database')

def insert_part(table: str, data_to_insert: tuple):
    with sqlite3.connect('planes.db') as conn:
        cursor = conn.cursor()
        if table in plane_objects:
            try:
                attributes = ', '.join(['?'] * len(data_to_insert))
                command = f'INSERT INTO {table} VALUES (NULL, {attributes})'
                cursor.execute(command, data_to_insert)
                conn.commit()
            except sqlite3.Error as e:
                print(f'Error {e} when inserting data in {table} database')
        else:
            print("There isn't such table...")
        part_id = cursor.lastrowid

        return part_id

def get_parts(id: int):
    with sqlite3.connect('planes.db') as conn:
        cursor = conn.cursor()
        parts = {}
        try:
            for key in plane_objects:
                command = f'SELECT * FROM {key} WHERE id=?'
                cursor.execute(command, (id,))
                information = cursor.fetchall()
                parts[key] = information[0]
        except sqlite3.Error as e:
            print(f'Error {e} when getting information from Airplane parts.')
        return parts

def get_specific_part(table: str, id: int):
    with sqlite3.connect('planes.db') as conn:
        cursor = conn.cursor()
        try:
            command = f'SELECT * FROM {table} WHERE id=?'
            cursor.execute(command, (id,))
            infolist = cursor.fetchall()
        except sqlite3.Error as e:
            print(f'Error {e} when getting information from Airplane parts.')
        return infolist

def update_parts(table: str, id: int, data_to_update: tuple):
    with sqlite3.connect('planes.db') as conn:
        cursor = conn.cursor()
        try:
            attributes = ', '.join([f"{piece} = ?" for piece in plane_reference[table]])
            command = f'UPDATE {table} SET {attributes} WHERE id=?'
            cursor.execute(command, (*data_to_update, id))
            conn.commit()
        except sqlite3.Error as e:
            print(f'Error {e} when updating data in {table} database.')

def delete_parts(id_tuple: tuple):
    with sqlite3.connect('planes.db') as conn:
        cursor = conn.cursor()
        try:
            for i in range(len(plane_objects)):
                command = f'DELETE FROM {plane_order[i]} WHERE id=?'
                cursor.execute(command, (id_tuple[i],))
            conn.commit()
        except sqlite3.Error as e:
            print(f'Error {e} when deleting parts from tables')

__all__ = ['boot_parts', 'insert_part', 'get_parts', 'get_specific_part', 'update_parts', 'delete_parts']