import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from .widgets import *
from .updategui import *

class PlaneManager:
    def __init__(self, root: tk.Tk, package: tuple, delete_callback, close_callback):
        try:
            self.root = tk.Toplevel(root, bg='darkblue')
            self.root.geometry('800x450')
            self.root.resizable(False,False)

            self.aircraft_dict = {}
            self.id = None

            self.close_callback = close_callback
            self.delete_callback = delete_callback
            self.root.protocol('WM_DELETE_WINDOW', self.on_close)
        except Exception as e:
            messagebox.showerror('Error', e)

        self.tree = ttk.Treeview(self.root, columns=('ID','Name','Creator','Creation Date'), show='headings', selectmode='browse')
        self.default_tree()
        for data in package:
            self.tree.insert('','end',values=data)
        self.tree.bind("<ButtonRelease-1>", self.on_button_click)
        
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        
        self.tree.pack()

        self.lbl_selection = MenuLabel(self.root, ' ').SelectionLabel()
        self.btn_delete = MenuButton(self.root, 'DELETE PLANE', self.delete_plane).ManagerButton('red','left')
        self.btn_update = MenuButton(self.root, 'UPDATE PLANE', self.update_plane).ManagerButton('lightblue','right')

    def default_tree(self):
        self.tree.heading('ID',text='ID')
        self.tree.column('ID',width=48)
        self.tree.heading('Name',text='Name')
        self.tree.column('Name',width=360)
        self.tree.heading('Creator',text='Creator')
        self.tree.column('Creator',width=180)
        self.tree.heading('Creation Date',text='Creation Date')
        self.tree.column('Creation Date',width=120)
    def on_button_click(self, event):
        sel = self.tree.selection()
        if not sel:
            return
        item = sel[0]
        name = self.tree.item(item, 'values')[1]
        self.lbl_selection.config(text=name)
    def delete_plane(self):
        self.disable_buttons()
        self.root.grab_set()
        if messagebox.askyesno('Plane Deleter', 'Are you sure?'):
            sel = self.tree.selection()
            if not sel:
                self.reenable_buttons()
                self.root.grab_release()
                return
            item = sel[0]
            id = self.tree.item(item, 'values')[0]
            self.delete_callback(id)
            self.on_close()
        else:
            self.reenable_buttons()
        self.root.grab_release()
    def update_plane(self):
        self.disable_buttons()
        self.root.withdraw()
        sel = self.tree.selection()
        if not sel:
            self.root.deiconify()
            self.reenable_buttons()
            return
        item = sel[0]
        id = self.tree.item(item, 'values')[0]
        UpdateMain(self.root, id, self.receive_plane)
    
    def receive_plane(self, id, airplane_dict):
        self.aircraft_dict = airplane_dict
        self.id = id
        self.root.deiconify()
    def reenable_buttons(self):
        self.btn_delete.config(state=tk.NORMAL)
        self.btn_update.config(state=tk.NORMAL)
    def disable_buttons(self):
        self.btn_delete.config(state=tk.DISABLED)
        self.btn_update.config(state=tk.DISABLED)
    def on_close(self) -> dict:
        if self.id is not None:
            try:
                self.close_callback(self.id,self.aircraft_dict)
            except Exception as e:
                messagebox.showerror('Error', e)
        self.root.destroy()