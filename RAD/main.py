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
        self.default()
        self.root.mainloop()
    def default(self):
        self.root.geometry('1920x1080')
        self.root.state('zoomed')
        self.root.iconphoto(True, tk.PhotoImage(file='./images/img-lg.png'))
        self.user = None
        self.window = m.MainMenu(self.root, self.user, self.open_airplane, self.open_creator, self.open_manager, self.regis_call, self.login_call, self.logoff_call)
    def open_mainmenu(self):
        self.user = None
        self.window = m.MainMenu(self.root, self.user,self.open_airplane, self.open_creator, self.open_manager, self.regis_call, self.login_call, self.logoff_call)
    def open_airplane(self):
        ids, names = self.db_to_tuple()
        self.window = m.AircraftMenu(self.root, names, ids, self.db_to_dict, self.open_mainmenu)
    def open_creator(self):
        self.creator = m.PlaneCreator(self.root, self.user, self.clse_creator)
        self.window.btn_database.config(state=tk.DISABLED)
        self.window.disable_buttons()
    def open_manager(self):
        package = self.manager_package()
        self.manager = m.PlaneManager(self.root, package, self.delete_plane, self.clse_manager)
        self.window.disable_buttons()
    def clse_creator(self):
        self.plane_to_db()
        self.window.reenable_buttons()
    def clse_manager(self, id:int, aircraft_dict: dict):
        self.window.reenable_buttons()
        self.dict_to_db(id,aircraft_dict)
    def manager_package(self) -> tuple:
        aircraft_list = m.view_planes()
        ids, names = self.db_to_tuple()
        try:
            creator = tuple(aircraft[1] for aircraft in aircraft_list)
            creation_raw = tuple(aircraft[2] for aircraft in aircraft_list)
            creation = tuple(datetime.fromisoformat(date).strftime("%d/%m/%Y") for date in creation_raw)
        except Exception as e:
            messagebox.showerror('Error',e)

        manager_tuple = tuple(zip(ids, names, creator, creation))
        return manager_tuple
    def db_to_tuple(self) -> tuple:
        '''Returns two Tuples: one containing all Aircraft ids, the other containing its names in "Model-Variation" format.'''
        aircraft_list = m.view_planes()
        def get_ids() -> tuple:
            try:
                ids = tuple(aircraft[0] for aircraft in aircraft_list)
                return ids
            except Exception as e:
                messagebox.showerror('Error',e)
                return None
        def get_names() -> tuple:
            try:
                technical_ids = tuple(aircraft[3] for aircraft in aircraft_list)
                technical_raw = (m.get_specific_part('technical', id) for id in technical_ids)
                technical_list = tuple(technical[0] for technical in technical_raw)
                model_tuple = tuple(technical[3] for technical in technical_list)
                var_tuple = tuple(technical[4] for technical in technical_list)
                aircraft_tuple = tuple(model +'-'+ variation for model,variation in zip(model_tuple, var_tuple))
                return aircraft_tuple
            except Exception as e:
                messagebox.showerror('Error',e)
                return None

        return get_ids(), get_names()
    def db_to_obj(self, id: int) -> m.Aircraft:
        '''Returns Airplane objectic from a specific plane in database.'''
        parts_dict = m.get_parts(id)

        try:
            Technical_obj = m.Technical(parts_dict['technical'][1],parts_dict['technical'][2],parts_dict['technical'][3],parts_dict['technical'][4],parts_dict['technical'][5],parts_dict['technical'][6],parts_dict['technical'][7],parts_dict['technical'][8],parts_dict['technical'][9],parts_dict['technical'][10],parts_dict['technical'][11],parts_dict['technical'][12])
            Takeoff_obj = m.Take_off(parts_dict['takeoff'][1],Technical_obj,parts_dict['takeoff'][2],parts_dict['takeoff'][3])
            Initial_climb_obj = m.Flight_level(True, parts_dict['initialclimb'][1],parts_dict['initialclimb'][2],'Initial Climb')
            Climb_150_obj = m.Flight_level(True,parts_dict['climb150'][2],parts_dict['climb150'][3], 150)
            Climb_240_obj = m.Flight_level(parts_dict['climb240'][1],parts_dict['climb240'][2],parts_dict['climb240'][3], 240)
            Climb_mach_obj = m.Flight_level(parts_dict['climbmach'][1],parts_dict['climbmach'][2],parts_dict['climbmach'][3], 'MACH')
            Cruise_obj = m.Cruise(parts_dict['cruise'][1],parts_dict['cruise'][2],parts_dict['cruise'][3],parts_dict['cruise'][4])
            Initial_descent_obj = m.Flight_level(parts_dict['initialdescent'][1],parts_dict['initialdescent'][2],parts_dict['initialdescent'][3], 'MACH')
            Descent_100_obj = m.Flight_level(True,parts_dict['descent100'][1],parts_dict['descent100'][2], 100)
            Approach_obj = m.Approach(parts_dict['approach'][1],parts_dict['approach'][2],parts_dict['approach'][3])
            Landing_obj = m.Landing(parts_dict['landing'][1],parts_dict['landing'][2])
        except Exception as e:
            print(f'Error {e} when creating Sub-Objects from Database.')

        try:
            Aircraft = m.Aircraft(Technical_obj, Takeoff_obj, Initial_climb_obj, Climb_150_obj, Climb_240_obj, Climb_mach_obj, Cruise_obj, Initial_descent_obj, Descent_100_obj, Approach_obj, Landing_obj)
        except Exception as e:
            print(f'Error {e} when creating Aircraft Object from Database.')
        return Aircraft
    def db_to_dict(self, id: int) -> dict:
        '''Returns a Dictionary from a specific plane in database.'''
        Aircraft = self.db_to_obj(id)
        return Aircraft.plane_to_dict()
    def plane_to_db(self) -> None:
        if self.user == None:
            messagebox.showerror('Error', 'You must login to add a plane!')
            self.creator.plne = None
            return

        try:
            if self.creator.plne:
                m.boot_parts()
                m.boot_plane()
        except Exception as e:
            messagebox.showerror('Error', e)
            self.creator.plne = None
            return
        
        if self.creator.plne:
            try:
                part = self.creator.plne
                data_technical = (part['manufacturer'],part['birth_year'],part['model'],part['variation'],part['wingspan'],part['wing_position'],part['engine_position'],part['tail_configuration'],part['landing_gear'],part['length'],part['height'],part['eu_analysis'])
                data_takeoff = (part['mtow'],part['to_distance'],part['v2'])
                data_initialclimb = (part['ic_ias'],part['ic_roc'])
                data_climb150 = (part['150_hd'],part['150_ias'],part['150_roc'])
                data_climb240 = (part['240_hd'],part['240_ias'],part['240_roc'])
                data_climbmach = (part['machc_hd'],part['machc_ias'],part['machc_roc'])
                data_cruise = (part['tas'],part['mach_cruise'],part['ceiling'],part['range'])
                data_initialdescent = (part['machd_hd'],part['machd_ias'],part['machd_rod'])
                data_descent100 = (part['100_ias'],part['100_rod'])
                data_approach = (part['approach_ias'],part['mcs'],part['approach_rod'])
                data_landing = (part['vat'],part['ld_distance'])

                technical_id = m.insert_part('technical', data_technical)
                takeoff_id = m.insert_part('takeoff', data_takeoff)
                initialclimb_id = m.insert_part('initialclimb', data_initialclimb)
                climb150_id = m.insert_part('climb150', data_climb150)
                climb240_id = m.insert_part('climb240', data_climb240)
                climbmach_id = m.insert_part('climbmach', data_climbmach)
                cruise_id = m.insert_part('cruise', data_cruise)
                initialdescent_id = m.insert_part('initialdescent', data_initialdescent)
                descent100_id = m.insert_part('descent100', data_descent100)
                approach_id = m.insert_part('approach', data_approach)
                landing_id = m.insert_part('landing', data_landing)
                
                m.add_plane((self.user, datetime.now(), technical_id, takeoff_id, initialclimb_id, climb150_id, climb240_id, climbmach_id, cruise_id, initialdescent_id, descent100_id, approach_id, landing_id))

            except Exception as e:
                messagebox.showerror('Error', e)
                self.creator.plne = None
                return
            
        self.creator.plne = None
        return
    def dict_to_db(self, id:int, aircraft_dict: dict):
        airplane = m.search_plane(id)
        
        conversion = {
            'approach': 12,
            'climb150': 6,
            'climb240': 7,
            'climbmach': 8,
            'cruise': 9,
            'descent100': 11,
            'initialclimb': 5,
            'initialdescent': 10,
            'landing': 13,
            'takeoff': 4,
            'technical': 3
        }
        
        try:
            for key in aircraft_dict:
                if key in conversion:
                    part_id = airplane[conversion[key]]
                    print(key)
                    print(part_id)
                    print(aircraft_dict[key])
                    m.update_parts(key,part_id,aircraft_dict[key])
        except Exception as e:
            messagebox.showerror('Error',e)
    def login_call(self, name: str, password: str) -> bool:
        m.boot_user()
        user = m.search_user(name)
        if user:
            if user[0][2] == password:
                self.user = user
                return True
            else:
                messagebox.showerror('Alert','Invalid Password')
                return False
        else:
            messagebox.showerror('Invalid Username')
            return False
    def logoff_call(self):
        self.user = None
    def regis_call(self, name: str, password: str) -> bool:
        m.boot_user()
        try:
            m.add_user(name,password)
            self.user = name
            return True
        except Exception as e:
            messagebox.showerror('Error',e)
            return False

    
    def delete_plane(self, id: int) ->None:
        '''Deletes plane and parts from Database'''
        raw_tuple = m.search_plane(id)
        id_tuple = (raw_tuple[12], raw_tuple[6], raw_tuple[7],raw_tuple[8],raw_tuple[9],raw_tuple[11],raw_tuple[5],raw_tuple[10],raw_tuple[13],raw_tuple[4],raw_tuple[3])
        try:
            m.delete_parts(id_tuple)
        except Exception as e:
            messagebox.showerror('Error',e)
            return
        try:
            m.delete_plane(id)
        except Exception as e:
            messagebox.showerror('Error',e)
            return
        messagebox.showinfo('Success',"Plane Successfuly Deleted! If you created an Image you should consider deleting it in this script's directory.")


try:
    app = App()
except Exception as e:
    print(f'Error {e} when starting Main script.')
    input()