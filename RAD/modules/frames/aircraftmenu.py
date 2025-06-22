import tkinter as tk
from tkinter import messagebox
from .widgets import *

class AircraftMenu:
    def __init__(self, root: tk.Tk, names_tuple: tuple, planes_tuple: tuple, aircraft_callback, return_callback, similar_planes: tuple = ('','','','','')):
        try:
            self.aircraft_callback = aircraft_callback
            self.return_callback = return_callback
        except:
            messagebox.showerror('Error', 'Error loading Aircraft Menu callback functions.')
        
        try:
            self.root = root
            self.tupled_plane = planes_tuple
            self.tupled_names = names_tuple
            self.strvar_plane = tk.StringVar(value=self.tupled_names[0])
            self.strvar_default()
            try:
                self.img = tk.PhotoImage(file=self.aircraft['image'])
            except:
                self.img = tk.PhotoImage(file='./images/default.png')
        except Exception as e:
            print(f'Error {e} when booting class Airplane Menu.')

        self.frm_main = MenuFrame(self.root).MainFrame(True, False)
        
        frm_profile = MenuFrame(self.frm_main).ProfileFrame()

        frm_upper_profile = MenuFrame(frm_profile).AvatarFrame()
        self.lbl_img = MenuLabel(frm_upper_profile).ImageLabel(self.img)
        self.combobox = MenuComboBox(frm_upper_profile, self.strvar_plane, self.tupled_names).NameComboBox()
        self.combobox.current(0)
        self.combobox.bind("<<ComboboxSelected>>", self.on_strvar_change)

        frm_lower_profile = MenuFrame(frm_profile).MainFrame(True)
        
        frm_identity = MenuFrame(frm_lower_profile).ProfileDescFrame()
        self.lbl_manufacturer = MenuLabel(frm_identity, f"Manufacturer: {self.aircraft['manufacturer']}", 'darkgray').GenericLabel()
        self.lbl_year = MenuLabel(frm_identity, f"Made in {self.aircraft['birth_year']}", 'lightgray').GenericLabel()
        self.lbl_model = MenuLabel(frm_identity, f"Model: {self.aircraft['model']}", 'darkgray').GenericLabel()

        frm_technical = MenuFrame(frm_lower_profile).ProfileDescFrame()
        self.lbl_wingspan = MenuLabel(frm_technical, f"Wingspan: {self.aircraft['wingspan']} m", 'lightgray').GenericLabel()
        self.lbl_lenght = MenuLabel(frm_technical, f"Length: {self.aircraft['length']} m", 'darkgray').GenericLabel()
        self.lbl_height = MenuLabel(frm_technical, f"Height: {self.aircraft['height']} m", 'lightgray').GenericLabel()

        frm_category = MenuFrame(frm_technical).ProfileDescFrame()
        self.lbl_recat_eu_p = MenuLabel(frm_category, f"RECAT-EU: \"{self.aircraft['recat_eu']}\"", 'darkgray').CategoryLabel('right')
        self.lbl_wtc_p = MenuLabel(frm_category, f"WTC: \"{self.aircraft['wtc']}\"", 'darkgray').CategoryLabel('left')

        frm_informations = MenuFrame(self.frm_main).MainFrame()

        frm_takeoff = MenuFrame(frm_informations).GridFrame(0,0)
        MenuLabel(frm_takeoff, 'Take Off').GenericLabel()
        self.lbl_mtow = MenuLabel(frm_takeoff, f"MTOW: {self.aircraft['mtow']} kg").GenericLabel()
        self.lbl_to_wtc = MenuLabel(frm_takeoff, f"WTC: \"{self.aircraft['wtc']}\"").GenericLabel()
        self.lbl_to_recat_eu = MenuLabel(frm_takeoff, f"RECAT-EU: \"{self.aircraft['recat_eu']}\"").GenericLabel()
        self.lbl_to_distance = MenuLabel(frm_takeoff, f"Distance: {self.aircraft['to_distance']} m").GenericLabel()
        self.lbl_v2 = MenuLabel(frm_takeoff, f"V2: {self.aircraft['v2']} kt").GenericLabel()

        frm_initial_climb = MenuFrame(frm_informations).GridFrame(1,0)
        MenuLabel(frm_initial_climb, 'Initial Climb (to 5.000ft)').GenericLabel()
        self.lbl_ic_ias = MenuLabel(frm_initial_climb, f"IAS: {self.aircraft['ic_ias']} kt").GenericLabel()
        self.lbl_ic_roc = MenuLabel(frm_initial_climb, f"ROC: {self.aircraft['ic_roc']} ft/min").GenericLabel()
        MenuLabel(frm_initial_climb, '').GenericLabel()
        MenuLabel(frm_initial_climb, '').GenericLabel()
        MenuLabel(frm_initial_climb, '').GenericLabel()

        frm_150FL_climb = MenuFrame(frm_informations).GridFrame(2,0)
        MenuLabel(frm_150FL_climb, 'FL 150 Climb').GenericLabel()
        self.lbl_150FLc_ias = MenuLabel(frm_150FL_climb, f"IAS: {self.aircraft['150_ias']} kt").GenericLabel()
        self.lbl_150FLc_roc = MenuLabel(frm_150FL_climb, f"ROC: {self.aircraft['150_roc']} ft/min").GenericLabel()
        MenuLabel(frm_150FL_climb, '').GenericLabel()
        MenuLabel(frm_150FL_climb, '').GenericLabel()
        MenuLabel(frm_150FL_climb, '').GenericLabel()

        frm_240FL_climb = MenuFrame(frm_informations).GridFrame(0,1)
        MenuLabel(frm_240FL_climb, 'FL 240 Climb').GenericLabel()
        self.lbl_240FLc_ias = MenuLabel(frm_240FL_climb, f"IAS: {self.aircraft['240_ias']} kt").GenericLabel()
        self.lbl_240FLc_roc = MenuLabel(frm_240FL_climb, f"ROC: {self.aircraft['240_roc']} ft/min").GenericLabel()
        MenuLabel(frm_240FL_climb, '').GenericLabel()
        MenuLabel(frm_240FL_climb, '').GenericLabel()
        MenuLabel(frm_240FL_climb, '').GenericLabel()

        frm_mach_climb = MenuFrame(frm_informations).GridFrame(1,1)
        MenuLabel(frm_mach_climb, 'MACH Climb').GenericLabel()
        self.lbl_machc_ias = MenuLabel(frm_mach_climb, f"MACH: {self.aircraft['machc_ias']}").GenericLabel()
        self.lbl_machc_roc = MenuLabel(frm_mach_climb, f"ROC: {self.aircraft['machc_roc']} ft/min").GenericLabel()
        MenuLabel(frm_mach_climb, '').GenericLabel()
        MenuLabel(frm_mach_climb, '').GenericLabel()
        MenuLabel(frm_mach_climb, '').GenericLabel()

        frm_cruise = MenuFrame(frm_informations).GridFrame(2,1)
        MenuLabel(frm_cruise, 'Cruise').GenericLabel()
        self.lbl_tas = MenuLabel(frm_cruise, f"TAS: {self.aircraft['tas']} kt").GenericLabel()
        self.lbl_mach_cruise = MenuLabel(frm_cruise, f"MACH: {self.aircraft['mach_cruise']}").GenericLabel()
        self.lbl_ceiling = MenuLabel(frm_cruise, f"Ceiling: FL {self.aircraft['ceiling']}").GenericLabel()
        self.lbl_range = MenuLabel(frm_cruise, f"Range: {self.aircraft['range']} NM").GenericLabel()
        MenuLabel(frm_cruise, '').GenericLabel()

        frm_initial_descent = MenuFrame(frm_informations).GridFrame(0,2)
        MenuLabel(frm_initial_descent, 'Initial Descent (to FL 240)').GenericLabel()
        self.lbl_id_ias = MenuLabel(frm_initial_descent, f"MACH: {self.aircraft['machd_ias']} kt").GenericLabel()
        self.lbl_id_rod = MenuLabel(frm_initial_descent, f"ROD: {self.aircraft['machd_rod']} ft/min").GenericLabel()
        MenuLabel(frm_initial_descent, '').GenericLabel()
        MenuLabel(frm_initial_descent, '').GenericLabel()
        MenuLabel(frm_initial_descent, '').GenericLabel()

        frm_100FL_descent = MenuFrame(frm_informations).GridFrame(1,2)
        MenuLabel(frm_100FL_descent, 'FL 100 Descent').GenericLabel()
        self.lbl_100FLd_ias = MenuLabel(frm_100FL_descent, f"IAS: {self.aircraft['100_ias']} kt").GenericLabel()
        self.lbl_100FLd_rod = MenuLabel(frm_100FL_descent, f"ROD: {self.aircraft['100_rod']} ft/min").GenericLabel()
        MenuLabel(frm_100FL_descent, '').GenericLabel()
        MenuLabel(frm_100FL_descent, '').GenericLabel()
        MenuLabel(frm_100FL_descent, '').GenericLabel()

        frm_approach = MenuFrame(frm_informations).GridFrame(2,2)
        MenuLabel(frm_approach, 'Approach').GenericLabel()
        self.lbl_approach_ias = MenuLabel(frm_approach, f"IAS: {self.aircraft['approach_ias']} kt").GenericLabel()
        self.lbl_approach_mcs = MenuLabel(frm_approach, f"MCS: {self.aircraft['mcs']} kt").GenericLabel()
        self.lbl_approach_rod = MenuLabel(frm_approach, f"ROD: {self.aircraft['approach_rod']} ft/min").GenericLabel()
        MenuLabel(frm_approach, '').GenericLabel()
        MenuLabel(frm_approach, '').GenericLabel()

        frm_landing = MenuFrame(frm_informations).GridFrame(0,3)
        MenuLabel(frm_landing, 'Landing').GenericLabel()
        self.lbl_vat = MenuLabel(frm_landing, f"VAT: {self.aircraft['vat']} kt").GenericLabel()
        self.lbl_apc = MenuLabel(frm_landing, f"APC: \"{self.aircraft['apc']}\"").GenericLabel()
        self.lbl_ld_distance = MenuLabel(frm_landing, f"Distance: {self.aircraft['ld_distance']} m").GenericLabel()
        MenuLabel(frm_landing, '').GenericLabel()
        MenuLabel(frm_landing, '').GenericLabel()

        frm_recognition = MenuFrame(frm_informations).GridFrame(1,3)
        MenuLabel(frm_recognition, 'Recognition').GenericLabel()
        self.lbl_variation = MenuLabel(frm_recognition, f"Variation: {self.aircraft['variation']}").GenericLabel()
        self.lbl_wing_position = MenuLabel(frm_recognition, f"Wing Position: {self.aircraft['wing_position']}").GenericLabel()
        self.lbl_engn_position = MenuLabel(frm_recognition, f"Engine Position: {self.aircraft['engine_position']}").GenericLabel()
        self.lbl_tail_config = MenuLabel(frm_recognition, f"Tail Setting: {self.aircraft['tail_configuration']}").GenericLabel()
        self.lbl_land_gear = MenuLabel(frm_recognition, f"Landing Gear: {self.aircraft['landing_gear']}").GenericLabel()

        frm_similar = MenuFrame(frm_informations).GridFrame(2,3)
        MenuLabel(frm_similar, 'Similar Aircrafts').GenericLabel()
        for plane in similar_planes:
            MenuLabel(frm_similar, plane).GenericLabel()
        
        MenuButton(self.frm_main, 'BACK', self.return_command).MainButton()

    def strvar_default(self):
        selected_id = self.strvar_plane.get()
        name_index = self.tupled_names.index(selected_id)
        id = self.tupled_plane[name_index]
        self.aircraft = self.aircraft_callback(id)
    
    def on_strvar_change(self, event=None):
        selected_id = self.strvar_plane.get()
        name_index = self.tupled_names.index(selected_id)
        id = self.tupled_plane[name_index]
        self.aircraft = self.aircraft_callback(id)
        self.update_labels()

    def update_labels(self):
        try:
            self.img = tk.PhotoImage(file=self.aircraft['image'])
        except:
            self.img = tk.PhotoImage(file='./images/default.png')
        self.lbl_img.config(image=self.img)
        self.lbl_manufacturer.config(text= f'Manufacturer: {self.aircraft["manufacturer"]}')
        self.lbl_year.config(text= f'Made in {self.aircraft["birth_year"]}')
        self.lbl_model.config(text= f'Model: {self.aircraft["model"]}')
        self.lbl_wingspan.config(text =f'Wingspan: {self.aircraft["wingspan"]} m')
        self.lbl_lenght.config(text =f'Length: {self.aircraft["length"]} m')
        self.lbl_height.config(text= f'Height: {self.aircraft["height"]} m')
        self.lbl_recat_eu_p.config(text= f'RECAT-EU: "{self.aircraft["recat_eu"]}"')
        self.lbl_wtc_p.config(text= f"WTC: \"{self.aircraft['wtc']}\"")
        self.lbl_mtow.config(text= f"MTOW: {self.aircraft['mtow']} kg")
        self.lbl_to_wtc.config(text= f"WTC: \"{self.aircraft['wtc']}\"")
        self.lbl_to_recat_eu.config(text= f"RECAT-EU: \"{self.aircraft['recat_eu']}\"")
        self.lbl_to_distance.config(text= f"Distance: {self.aircraft['to_distance']} m")
        self.lbl_v2.config(text= f"V2: {self.aircraft['v2']} kt")
        self.lbl_ic_ias.config(text= f"IAS: {self.aircraft['ic_ias']} kt")
        self.lbl_ic_roc.config(text= f"ROC: {self.aircraft['ic_roc']} ft/min")
        self.lbl_150FLc_ias.config(text= f"IAS: {self.aircraft['150_ias']} kt")
        self.lbl_150FLc_roc.config(text= f"ROC: {self.aircraft['150_roc']} ft/min")
        self.lbl_240FLc_ias.config(text= f"IAS: {self.aircraft['240_ias']} kt")
        self.lbl_240FLc_roc.config(text= f"ROC: {self.aircraft['240_roc']} ft/min")
        self.lbl_machc_ias.config(text= f"MACH: {self.aircraft['machc_ias']}")
        self.lbl_machc_roc.config(text= f"ROC: {self.aircraft['machc_roc']} ft/min")
        self.lbl_tas.config(text= f"TAS: {self.aircraft['tas']} kt")
        self.lbl_mach_cruise.config(text= f"MACH: {self.aircraft['mach_cruise']}")
        self.lbl_ceiling.config(text= f"Ceiling: FL {self.aircraft['ceiling']}")
        self.lbl_range.config(text= f"Range: {self.aircraft['range']} NM")
        self.lbl_id_ias.config(text= f"MACH: {self.aircraft['machd_ias']} kt")
        self.lbl_id_rod.config(text= f"ROD: {self.aircraft['machd_rod']} ft/min")
        self.lbl_100FLd_ias.config(text= f"IAS: {self.aircraft['100_ias']} kt")
        self.lbl_100FLd_rod.config(text= f"ROD: {self.aircraft['100_rod']} ft/min")
        self.lbl_approach_ias.config(text= f"IAS: {self.aircraft['approach_ias']} kt")
        self.lbl_approach_mcs.config(text= f"MCS: {self.aircraft['mcs']} kt")
        self.lbl_approach_rod.config(text= f"ROD: {self.aircraft['approach_rod']} ft/min")
        self.lbl_vat.config(text= f"VAT: {self.aircraft['vat']} kt")
        self.lbl_apc.config(text= f"APC: \"{self.aircraft['apc']}\"")
        self.lbl_ld_distance.config(text= f"Distance: {self.aircraft['ld_distance']} m")
        self.lbl_variation.config(text= f"Variation: {self.aircraft['variation']}")
        self.lbl_wing_position.config(text= f"Wing Position: {self.aircraft['wing_position']}")
        self.lbl_engn_position.config(text= f"Engine Position: {self.aircraft['engine_position']}")
        self.lbl_tail_config.config(text= f"Tail Setting: {self.aircraft['tail_configuration']}")
        self.lbl_land_gear.config(text= f"Landing Gear: {self.aircraft['landing_gear']}")

        # frm_similar = MenuFrame(frm_informations).GridFrame(2,3)
        # MenuLabel(frm_similar, 'Similar Aircrafts').GenericLabel()
        # for plane in similar_planes:
        #     MenuLabel(frm_similar, plane).GenericLabel()

    def return_command(self):
        self.frm_main.destroy()
        self.return_callback()
