import tkinter as tk
from tkinter import messagebox
from .widgets import *

class PlaneCreator:
    def __init__(self, root: tk.Tk, username: str, on_close_callback):
        self.root = tk.Toplevel(root)
        self.root.title('Plane Creator')
        self.root.resizable(False,False)
        self.user = username
        self.plne = None
        
        self.on_close_callback = on_close_callback
        self.root.protocol('WM_DELETE_WINDOW', self.on_close)

        self.frm_main = MenuFrame(self.root).MainFrame(True)
        self.TechnicalCreator()

    def TechnicalCreator(self):
        self.default_init('TECHNICAL')
        MenuLabel(self.frm_creator,'320x320 PNG IMAGE PATH:', '#f0f0f0').GenericLabel()
        self.img_path = MenuEntry(self.frm_creator).TechnicalEntry()
        frm_grid = MenuFrame(self.frm_creator).MainFrame(True)

        frm_a = MenuFrame(frm_grid).GridFrame(0,0)
        MenuLabel(frm_a,'MANUFACTURER:', '#f0f0f0').GenericLabel()
        self.manufacturer = MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'CREATION YEAR:', '#f0f0f0').GenericLabel()
        self.birth_year = MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'MODEL:', '#f0f0f0').GenericLabel()
        self.model = MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'VARIATION:', '#f0f0f0').GenericLabel()
        self.variation = MenuEntry(frm_a).TechnicalEntry()

        frm_b = MenuFrame(frm_grid).GridFrame(0,1)
        MenuLabel(frm_b,'WINGSPAN IN METERS:', '#f0f0f0').GenericLabel()
        self.wingspan = MenuEntry(frm_b).TechnicalEntry()
        MenuLabel(frm_b,'WING POSITION:', '#f0f0f0').GenericLabel()
        self.wingposition = MenuEntry(frm_b).TechnicalEntry()
        MenuLabel(frm_b,'ENGINE POSITION:', '#f0f0f0').GenericLabel()
        self.engn_position = MenuEntry(frm_b).TechnicalEntry()
        MenuLabel(frm_b,'TAIL CONFIGURATION:', '#f0f0f0').GenericLabel()
        self.tail_config = MenuEntry(frm_b).TechnicalEntry()

        frm_c = MenuFrame(frm_grid).GridFrame(1,0)
        MenuLabel(frm_c,'LENGTH IN METERS:', '#f0f0f0').GenericLabel()
        self.length = MenuEntry(frm_c).TechnicalEntry()
        MenuLabel(frm_c,'HEIGHT IN METERS:', '#f0f0f0').GenericLabel()
        self.height = MenuEntry(frm_c).TechnicalEntry()

        frm_d = MenuFrame(frm_grid).GridFrame(1,1)
        MenuLabel(frm_d,'LANDING GEAR:', '#f0f0f0').GenericLabel()
        self.land_gear = MenuEntry(frm_d).TechnicalEntry()
        MenuLabel(frm_d,'SPECIFIC EU ANALYSIS:', '#f0f0f0').GenericLabel()
        self.eu_specific_analysis = MenuEntry(frm_d).TechnicalEntry()
        MenuButton(self.frm_creator, 'NEXT', self.goto_takeoff).MainButton()
    
    def TakeoffCreator(self):
        self.default_init('TAKE OFF')
        frm_grid = MenuFrame(self.frm_creator).MainFrame(True)
        frm_a = MenuFrame(frm_grid).GridFrame(0,0)
        MenuLabel(frm_a,'MTOW IN KILOGRAMS:', '#f0f0f0').GenericLabel()
        self.mtow = MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'MINIMUM DISTANCE IN METERS:', '#f0f0f0').GenericLabel()
        self.to_distance = MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'V2 IN KNOTS:', '#f0f0f0').GenericLabel()
        self.v2 = MenuEntry(frm_a).TechnicalEntry()
        MenuButton(self.frm_creator, 'NEXT', self.goto_init_climb).MainButton()   
    
    def InitClimbCreator(self):
        self.default_init('INITIAL CLIMB')
        frm_grid = MenuFrame(self.frm_creator).MainFrame(True)
        frm_a = MenuFrame(frm_grid).GridFrame(0,0)
        MenuLabel(frm_a,'IAS IN KNOTS:', '#f0f0f0').GenericLabel()
        self.inc_ias = MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'ROC IN FT/MIN:', '#f0f0f0').GenericLabel()
        self.inc_roc = MenuEntry(frm_a).TechnicalEntry()
        MenuButton(self.frm_creator, 'NEXT', self.goto_150_climb).MainButton()   

    def Climb150Creator(self):
        self.default_init('CLIMB TO FL 150')
        self.has_150_data = tk.BooleanVar(value=True)
        MenuCheck(self.frm_creator, 'HAS DATA?', self.has_150_data, self.goto_240_climb).MainButton()
        frm_grid = MenuFrame(self.frm_creator).MainFrame(True)
        frm_a = MenuFrame(frm_grid).GridFrame(0,0)
        MenuLabel(frm_a,'IAS IN KNOTS:', '#f0f0f0').GenericLabel()
        self.c150_ias = MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'ROC IN FT/MIN:', '#f0f0f0').GenericLabel()
        self.c150_roc = MenuEntry(frm_a).TechnicalEntry()
        MenuButton(self.frm_creator, 'NEXT', self.goto_240_climb).MainButton()

    def Climb240Creator(self):
        self.default_init('CLIMB TO FL 240')
        self.has_240_data = tk.BooleanVar(value=True)
        MenuCheck(self.frm_creator, 'HAS DATA?', self.has_240_data, self.goto_mach_climb).MainButton()
        frm_grid = MenuFrame(self.frm_creator).MainFrame(True)
        frm_a = MenuFrame(frm_grid).GridFrame(0,0)
        MenuLabel(frm_a,'IAS IN KNOTS:', '#f0f0f0').GenericLabel()
        self.c240_ias = MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'ROC IN FT/MIN:', '#f0f0f0').GenericLabel()
        self.c240_roc = MenuEntry(frm_a).TechnicalEntry()
        MenuButton(self.frm_creator, 'NEXT', self.goto_mach_climb).MainButton()

    def ClimbMachCreator(self):
        self.default_init('MACH CLIMB')
        self.has_cmach_data = tk.BooleanVar(value=True)
        MenuCheck(self.frm_creator, 'HAS DATA?', self.has_cmach_data, self.goto_cruise).MainButton()
        frm_grid = MenuFrame(self.frm_creator).MainFrame(True)
        frm_a = MenuFrame(frm_grid).GridFrame(0,0)
        MenuLabel(frm_a,'MACH SPEED:', '#f0f0f0').GenericLabel()
        self.cmach_ias = MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'ROC IN FT/MIN:', '#f0f0f0').GenericLabel()
        self.cmach_roc = MenuEntry(frm_a).TechnicalEntry()
        MenuButton(self.frm_creator, 'NEXT', self.goto_cruise).MainButton()

    def CruiseCreator(self):
        self.default_init('CRUISE')
        frm_grid = MenuFrame(self.frm_creator).MainFrame(True)
        frm_a = MenuFrame(frm_grid).GridFrame(0,0)
        MenuLabel(frm_a,'TAS IN KNOTS:', '#f0f0f0').GenericLabel()
        self.tas = MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'MACH SPEED:', '#f0f0f0').GenericLabel()
        self.mach = MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'FLIGHT LEVEL CEILING:', '#f0f0f0').GenericLabel()
        self.ceiling = MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'RANGE IN NAUTICAL MILES:', '#f0f0f0').GenericLabel()
        self.range = MenuEntry(frm_a).TechnicalEntry()
        MenuButton(self.frm_creator, 'NEXT', self.goto_init_dsct).MainButton()

    def InitDescentCreator(self):
        self.default_init('INITIAL DESCENT')
        self.has_dmach_data = tk.BooleanVar(value=True)
        MenuCheck(self.frm_creator, 'HAS DATA?', self.has_dmach_data, self.goto_100_dsct).MainButton()
        frm_grid = MenuFrame(self.frm_creator).MainFrame(True)
        frm_a = MenuFrame(frm_grid).GridFrame(0,0)
        MenuLabel(frm_a,'MACH SPEED:', '#f0f0f0').GenericLabel()
        self.dmach_ias = MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'ROD IN FT/MIN:', '#f0f0f0').GenericLabel()
        self.dmach_rod = MenuEntry(frm_a).TechnicalEntry()
        MenuButton(self.frm_creator, 'NEXT', self.goto_100_dsct).MainButton()

    def Descent100Creator(self):
        self.default_init('DESCENT TO FL 100')
        frm_grid = MenuFrame(self.frm_creator).MainFrame(True)
        frm_a = MenuFrame(frm_grid).GridFrame(0,0)
        MenuLabel(frm_a,'IAS IN KNOTS:', '#f0f0f0').GenericLabel()
        self.d100_ias = MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'ROD IN FT/MIN:', '#f0f0f0').GenericLabel()
        self.d100_rod = MenuEntry(frm_a).TechnicalEntry()
        MenuButton(self.frm_creator, 'NEXT', self.goto_approach).MainButton()

    def ApproachCreator(self):
        self.default_init('APPROACH')
        frm_grid = MenuFrame(self.frm_creator).MainFrame(True)
        frm_a = MenuFrame(frm_grid).GridFrame(0,0)
        MenuLabel(frm_a,'IAS IN KNOTS:', '#f0f0f0').GenericLabel()
        self.appr_ias = MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'MCS IN KNOTS:', '#f0f0f0').GenericLabel()
        self.mcs = MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'ROD IN FT/MIN:', '#f0f0f0').GenericLabel()
        self.appr_rod = MenuEntry(frm_a).TechnicalEntry()
        MenuButton(self.frm_creator, 'NEXT', self.goto_landing).MainButton()

    def LandingCreator(self):
        self.default_init('LANDING')
        frm_grid = MenuFrame(self.frm_creator).MainFrame(True)
        frm_a = MenuFrame(frm_grid).GridFrame(0,0)
        MenuLabel(frm_a,'VAT IN KNOTS:', '#f0f0f0').GenericLabel()
        self.vat = MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'MINIMUM DISTANCE IN METERS:', '#f0f0f0').GenericLabel()
        self.ld_distance = MenuEntry(frm_a).TechnicalEntry()
        MenuButton(self.frm_creator, 'NEXT', self.create_plane).MainButton()
        
    def goto_takeoff(self):
        self.frm_creator.pack_forget()
        if self.validate_image() == True:
            self.TakeoffCreator()

    def goto_init_climb(self):
        self.frm_creator.pack_forget()
        self.InitClimbCreator()

    def goto_150_climb(self):
        self.frm_creator.pack_forget()
        self.Climb150Creator()

    def goto_240_climb(self):
        if self.has_150_data.get() == False:
            self.c150_ias = None
            self.c150_roc = None
        self.frm_creator.pack_forget()
        self.Climb240Creator()

    def goto_mach_climb(self):
        if self.has_240_data.get() == False:
            self.c240_ias = None
            self.c240_roc = None
        self.frm_creator.pack_forget()
        self.ClimbMachCreator()

    def goto_cruise(self):
        if self.has_cmach_data.get() == False:
            self.cmach_ias = None
            self.cmach_roc = None
        self.frm_creator.pack_forget()
        self.CruiseCreator()

    def goto_init_dsct(self):
        self.frm_creator.pack_forget()
        self.InitDescentCreator()

    def goto_100_dsct(self):
        if self.has_dmach_data.get() == False:
            self.dmach_ias = None
            self.dmach_rod = None
        self.frm_creator.pack_forget()
        self.Descent100Creator()

    def goto_approach(self):
        self.frm_creator.pack_forget()
        self.ApproachCreator()

    def goto_landing(self):
        self.frm_creator.pack_forget()
        self.LandingCreator()
    
    def create_plane(self):
        if self.duplicate_image():
            if self.validate_parts() == True:
                try:
                    aircraft = self.info_to_dictionary()
                    messagebox.showinfo('Sucess!', 'Plane has been successfully created!')
                    self.plne = aircraft
                    self.on_close()
                except Exception as e:
                    messagebox.showerror('Error', e)
            else:
                self.on_close()
                self.root.destroy()

    def validate_parts(self) -> bool:
        information = (self.manufacturer, self.birth_year, self.model, self.variation, self.wingspan, self.wingposition, self.engn_position, self.tail_config, self.length, self.height, self.land_gear, self.eu_specific_analysis, self.mtow, self.to_distance, self.v2, self.inc_ias, self.inc_roc, self.tas, self.mach, self.ceiling, self.range, self.d100_ias, self.d100_rod, self.appr_ias, self.mcs, self.appr_rod, self.vat, self.ld_distance)
        optional = {0: (self.has_150_data.get(), self.c150_ias, self.c150_roc), 1: (self.has_240_data.get(),self.c240_ias, self.c240_roc), 2: (self.has_cmach_data.get(), self.cmach_ias, self.cmach_roc), 3: (self.has_dmach_data.get(), self.dmach_ias, self.dmach_rod)}
        str_information = (self.manufacturer, self.model, self.variation, self.wingposition, self.engn_position, self.tail_config, self.land_gear, self.eu_specific_analysis)
        int_information = (self.birth_year, self.mtow, self.to_distance, self.v2, self.inc_ias, self.inc_roc, self.tas, self.ceiling, self.range, self.d100_ias, self.d100_rod, self.appr_ias, self.mcs, self.appr_rod, self.vat, self.ld_distance)
        flt_information = (self.wingspan, self.length, self.height, self.mach)
        
        def check_length(info: tuple, opts: tuple) -> bool:
            for information in info:
                try:
                    if len(information.get()) > 10:
                        messagebox.showerror('Error', f'{information.get()} has more than 10 digits. All information must have at most 10 digits')
                        return False
                    elif len(information.get()) == 0:
                        messagebox.showerror('Error', 'You left empty information!')
                        return False
                    else:
                        return True
                except Exception as e:
                    messagebox.showerror('Error', e)
                    return False
            for optional in opts:
                if optional[0] == True:
                    for information in opts[optional]:
                        try:
                            if len(information.get()) > 10:
                                messagebox.showerror('Error', f'{information.get()} has more than 10 digits. All information must have at most 10 digits')
                                return False
                            elif len(information.get()) == 0:
                                messagebox.showerror('Error', 'You left empty information!')
                                return False
                            else:
                                return True
                        except Exception as e:
                            messagebox.showerror('Error', e)
                            return False
        
        def check_typing(str_info: tuple, int_info: tuple, flt_info: tuple, optional_info: tuple) -> bool:
            for information in str_info:
                try:
                    debug = (str(information.get())).strip()
                    if not debug:
                        messagebox.showerror('Error', ('Invalid information.\nYou left empty information!'))
                        return False
                    if not (debug[0].isalnum() and debug[-1].isalnum()):
                        messagebox.showerror('Error', (f'Invalid information.\n{debug} is invalid information!'))
                        return False
                except Exception as e:
                    messagebox.showerror('Error', ('Error validating information.\n' + str(e)))
                    return False
            for information in str_info:
                try:
                    debug = str(information.get())
                except Exception as e:
                    messagebox.showerror('Error', ('Error converting information to String.\n' + str(e)))
                    return False
            for information in int_info:
                try:
                    debug = int(float(information.get()))
                except Exception as e:
                    messagebox.showerror('Error', ('Error converting information to Integer.\n' + str(e)))
                    return False
            for information in flt_info:
                try:
                    debug = round(float(information.get()),2)
                except Exception as e:
                    messagebox.showerror('Error', ('Error converting information to Float.\n' + str(e)))
                    return False
            for optional in optional_info:
                if optional_info[optional][0] == True:
                    if optional in (2,3):
                        try:
                            debug = round(float(optional_info[optional][1].get()),1)
                            debug = int(float(optional_info[optional][2].get()))
                        except Exception as e:
                            messagebox.showerror('Error', ('Error converting optional information to Float.\n' + str(e)))
                            return False
                    else:
                        for info in optional_info[optional]:
                            if not isinstance(info,bool):
                                try:
                                    debug = int(float(info.get()))
                                except Exception as e:
                                    messagebox.showerror('Error', ('Error converting optional information to Integer.\n' + str(e)))
                                    return False
            return True
        
        if check_length(information, optional) == True:
            if check_typing(str_information, int_information, flt_information, optional) == True:
                return True
            
    def info_to_dictionary(self) -> dict:
        try:
            aircraft_dict: dict = {}

            aircraft_dict['creator'] = str(self.user)
            aircraft_dict['image'] = './images/' + str(self.model.get()) + '-' +str(self.variation.get()) + '.png'
            aircraft_dict['manufacturer'] = str(self.manufacturer.get()).strip()
            aircraft_dict['birth_year'] = int(self.birth_year.get())
            aircraft_dict['model'] = str(self.model.get()).strip()
            aircraft_dict['wingspan'] = round(float(self.wingspan.get()),1)
            aircraft_dict['length'] = round(float(self.length.get()),1)
            aircraft_dict['height'] = round(float(self.height.get()),1)
            aircraft_dict['eu_analysis'] = str(self.eu_specific_analysis.get()).strip()
            aircraft_dict['mtow'] = int(self.mtow.get())
            aircraft_dict['to_distance'] = int(self.to_distance.get())
            aircraft_dict['v2'] = int(self.v2.get())
            aircraft_dict['ic_ias'] = int(self.inc_ias.get())
            aircraft_dict['ic_roc'] = int(self.inc_roc.get())
            aircraft_dict['150_hd'] = bool(self.has_150_data.get())
            aircraft_dict['150_ias'] = int(self.c150_ias.get()) if self.c150_ias else None
            aircraft_dict['150_roc'] = int(self.c150_roc.get()) if self.c150_roc else None
            aircraft_dict['240_hd'] = bool(self.has_240_data.get())
            aircraft_dict['240_ias'] = int(self.c240_ias.get()) if self.c240_ias else None
            aircraft_dict['240_roc'] = int(self.c240_roc.get()) if self.c240_roc else None
            aircraft_dict['machc_hd'] = bool(self.has_cmach_data.get())
            aircraft_dict['machc_ias'] = round(float(self.cmach_ias.get()),1) if self.cmach_ias else None
            aircraft_dict['machc_roc'] = int(self.cmach_roc.get()) if self.cmach_roc else None
            aircraft_dict['tas'] = int(self.tas.get())
            aircraft_dict['mach_cruise'] = round(float(self.mach.get()),1)
            aircraft_dict['ceiling'] = int(self.ceiling.get())
            aircraft_dict['range'] = int(self.range.get())
            aircraft_dict['machd_hd'] = bool(self.has_dmach_data.get())
            aircraft_dict['machd_ias'] = round(float(self.dmach_ias.get()),1) if self.dmach_ias else None
            aircraft_dict['machd_rod'] = int(self.dmach_rod.get()) if self.dmach_rod else None
            aircraft_dict['100_ias'] = int(self.d100_ias.get())
            aircraft_dict['100_rod'] = int(self.d100_rod.get())
            aircraft_dict['approach_ias'] = int(self.appr_ias.get())
            aircraft_dict['mcs'] = int(self.mcs.get())
            aircraft_dict['approach_rod'] = int(self.appr_rod.get())
            aircraft_dict['vat'] = int(self.vat.get())
            aircraft_dict['ld_distance'] = int(self.ld_distance.get())
            aircraft_dict['variation'] = str(self.variation.get()).strip()
            aircraft_dict['wing_position'] = str(self.wingposition.get()).strip()
            aircraft_dict['engine_position'] = str(self.engn_position.get()).strip()
            aircraft_dict['tail_configuration'] = str(self.tail_config.get()).strip()
            aircraft_dict['landing_gear'] = str(self.land_gear.get()).strip()

            return aircraft_dict
        except Exception as e:
            print(f'Error {e} when converting Aircraft object to dictionary.')

    def validate_image(self) -> bool:
        source_path = self.img_path.get()

        if source_path == 'None':
            return True

        try:
            with open(source_path, 'rb') as file:
                file_data = file.read(8)
                return file_data==b'\x89PNG\r\n\x1a\n'
        except Exception as e:
            messagebox.showerror('Error','Invalid Image Path. Path should look like: C:/path/to/image.png\n' + str(e))
            self.on_close()
            self.root.destroy()

    def duplicate_image(self):
        source_path = self.img_path.get()
        if source_path == 'None':
            return True


        destination_path = './images/' + str(self.model.get()) + '-' +str(self.variation.get()) + '.png'

        try:
            with open(source_path, 'rb') as file:
                file_data = file.read()
            with open(destination_path, 'wb') as new_file:
                new_file.write(file_data)
            return True
        except Exception as e:
            messagebox.showerror('Error', e)
            self.on_close()
            self.root.destroy()

    def default_init(self, section: str):
        self.frm_creator = MenuFrame(self.frm_main).MainFrame(True)
        MenuLabel(self.frm_creator, section, 'darkblue', 'white').GenericLabel()

    def on_close(self):
        self.on_close_callback()
        self.root.destroy()