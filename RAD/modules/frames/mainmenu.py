import tkinter as tk
from .widgets import *

class MainMenu:
    def __init__(self,root: tk.Tk, redirect_callback):
        try:
            self.root = root
            self.root.title('DataPlanes')

            self.plane_callback = redirect_callback

            self.frm_account = MenuFrame(self.root).AccountFrame()

            MenuLabel(self.frm_account, 'Not Logged!').AccountLabel()

            MenuButton(self.frm_account, 'Login').AccountButton('right')
            MenuButton(self.frm_account, 'Register').AccountButton('left')

            self.frm_main = MenuFrame(self.root).MainFrame()
            
            MenuButton(self.frm_main, 'Database', self.redirect_plane).MainButton()
            MenuButton(self.frm_main, 'Add Plane').MainButton()
            MenuButton(self.frm_main, 'Manage Plane').MainButton()
            MenuButton(self.frm_main, 'Exit', self.close).MainButton()
        except Exception as e:
            print(f'Error {e} when booting class Main Menu.')
    
    def close(self):
        self.root.destroy()
    def redirect_plane(self):
        self.frm_main.destroy()
        self.frm_account.destroy()
        self.plane_callback()