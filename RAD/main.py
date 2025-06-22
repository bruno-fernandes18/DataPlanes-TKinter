import tkinter as tk
from tkinter import messagebox
from datetime import datetime
try:
    import modules as m
except Exception as e:
    print(f'Error {e} when importing modules.')

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.service = m.DatabaseService()
        self.default()
        self.root.mainloop()
    def default(self):
        self.root.geometry('1920x1080')
        self.root.state('zoomed')
        self.root.iconphoto(True, tk.PhotoImage(file='./images/img-lg.png'))
        self.user = None
        self.window = m.MainMenu(self.root, self.user, self.open_airplane, self.open_creator, self.open_manager, self.regis_call, self.login_call, self.logoff_call)
    def open_mainmenu(self):
        self.window = m.MainMenu(
            self.root,
            self.user,
            self.open_airplane,
            self.open_creator,
            self.open_manager,
            self.regis_call,
            self.login_call,
            self.logoff_call,
        )
    def open_airplane(self):
        ids, names = self.service.db_to_tuple()
        self.window = m.AircraftMenu(self.root, names, ids, self.service.db_to_dict, self.open_mainmenu)
    def open_creator(self):
        self.creator = m.PlaneCreator(self.root, self.user, self.clse_creator)
        self.window.btn_database.config(state=tk.DISABLED)
        self.window.disable_buttons()
    def open_manager(self):
        package = self.service.manager_package()
        self.manager = m.PlaneManager(self.root, package, self.service.delete_plane, self.clse_manager)
        self.window.disable_buttons()
    def clse_creator(self):
        self.service.plane_to_db(self.user, self.creator.plne)
        self.creator.plne = None
        self.window.reenable_buttons()
    def clse_manager(self, id:int, aircraft_dict: dict):
        self.window.reenable_buttons()
        self.service.dict_to_db(id, aircraft_dict)
    def login_call(self, name: str, password: str) -> bool:
        user = self.service.login(name, password)
        if user:
            self.user = user
            return True
        return False
    def logoff_call(self):
        self.user = None
    def regis_call(self, name: str, password: str) -> bool:
        if self.service.register(name, password):
            self.user = name
            return True
        return False

    


try:
    app = App()
except Exception as e:
    print(f'Error {e} when starting Main script.')
    input()
