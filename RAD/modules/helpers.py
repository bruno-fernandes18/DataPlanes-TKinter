import tkinter as tk
from tkinter import messagebox


def validate_image(path: str) -> bool:
    if path == 'None':
        return True
    try:
        with open(path, 'rb') as file:
            file_data = file.read(8)
            return file_data == b'\x89PNG\r\n\x1a\n'
    except Exception as e:
        messagebox.showerror('Error', 'Invalid Image Path. ' + str(e))
        return False


def duplicate_image(source: str, dest: str) -> bool:
    if source == 'None':
        return True
    try:
        with open(source, 'rb') as file:
            data = file.read()
        with open(dest, 'wb') as new_file:
            new_file.write(data)
        return True
    except Exception as e:
        messagebox.showerror('Error', e)
        return False


def validate_parts(information: tuple, optional: dict, str_information: tuple,
                    int_information: tuple, flt_information: tuple) -> bool:
    def check_length(info: tuple, opts: dict) -> bool:
        for item in info:
            try:
                if len(item.get()) > 10:
                    messagebox.showerror('Error', f'{item.get()} has more than 10 digits')
                    return False
                if len(item.get()) == 0:
                    messagebox.showerror('Error', 'You left empty information!')
                    return False
            except Exception as e:
                messagebox.showerror('Error', e)
                return False
        for key in opts:
            if opts[key][0]:
                for item in opts[key]:
                    if isinstance(item, bool):
                        continue
                    try:
                        if len(item.get()) > 10:
                            messagebox.showerror('Error', f'{item.get()} has more than 10 digits')
                            return False
                        if len(item.get()) == 0:
                            messagebox.showerror('Error', 'You left empty information!')
                            return False
                    except Exception as e:
                        messagebox.showerror('Error', e)
                        return False
        return True

    def check_typing(str_info: tuple, int_info: tuple, flt_info: tuple, optional_info: dict) -> bool:
        for information in str_info:
            try:
                debug = (str(information.get())).strip()
                if not debug:
                    messagebox.showerror('Error', 'Invalid information.')
                    return False
                if not (debug[0].isalnum() and debug[-1].isalnum()):
                    messagebox.showerror('Error', f'{debug} is invalid information!')
                    return False
            except Exception as e:
                messagebox.showerror('Error', 'Error validating information.\n' + str(e))
                return False
        for information in str_info:
            try:
                str(information.get())
            except Exception as e:
                messagebox.showerror('Error', 'Error converting information to String.\n' + str(e))
                return False
        for information in int_info:
            try:
                int(float(information.get()))
            except Exception as e:
                messagebox.showerror('Error', 'Error converting information to Integer.\n' + str(e))
                return False
        for information in flt_info:
            try:
                round(float(information.get()), 2)
            except Exception as e:
                messagebox.showerror('Error', 'Error converting information to Float.\n' + str(e))
                return False
        for key in optional_info:
            if optional_info[key][0]:
                if key in (2, 3):
                    try:
                        round(float(optional_info[key][1].get()), 1)
                        int(float(optional_info[key][2].get()))
                    except Exception as e:
                        messagebox.showerror('Error', 'Error converting optional information.\n' + str(e))
                        return False
                else:
                    for info in optional_info[key]:
                        if not isinstance(info, bool):
                            try:
                                int(float(info.get()))
                            except Exception as e:
                                messagebox.showerror('Error', 'Error converting optional information.\n' + str(e))
                                return False
        return True

    if check_length(information, optional) and check_typing(str_information, int_information, flt_information, optional):
        return True
    return False
