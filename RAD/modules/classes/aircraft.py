from .planeInfo import *

class Aircraft:
    def __init__(self, Technical_obj: Technical, Take_off_obj: Take_off, Initial_climb_obj: Flight_level, Climb_150_obj: Flight_level, Climb_240_obj: Flight_level, Climb_mach_obj: Flight_level, Cruise_obj: Cruise, Initial_descent_obj: Flight_level, Descent_100_obj: Flight_level, Approach_obj: Approach, Landing_obj: Landing ) -> 'Aircraft':
        '''Initializes Aircraft object.'''
        try:
            self.technical: Technical = Technical_obj
            self.take_off: Take_off = Take_off_obj
            self.initial_climb: Flight_level = Initial_climb_obj

            self.climb_150: Flight_level = Climb_150_obj
            self.climb_240: Flight_level = Climb_240_obj
            self.climb_mach: Flight_level = Climb_mach_obj

            self.cruise: Cruise = Cruise_obj

            self.initial_descent: Flight_level = Initial_descent_obj
            self.descent_100: Flight_level = Descent_100_obj

            self.approach: Approach = Approach_obj
            self.landing: Landing = Landing_obj
        except Exception as e:
            print(f'Error {e} when booting Aircraft class.')
    def debug_airplane(self) -> 'Aircraft':
        '''Return an Aircraft object with default values.'''
        try:
            self.technical = Technical('Boeing',1996,'737','700',34.3,'Low','Underwing','Regular','Trycicle',33.6,12.6)
            self.take_off = Take_off(66320, self.technical, 1800, 150)
            self.initial_climb = Flight_level(True, 165,3000, 5000)
            self.climb_150 = Flight_level(True, 280, 2500, 150)
            self.climb_240 = Flight_level(True, 280, 2500, 240)
            self.climb_mach = Flight_level(True, 0.74, 1500, 'MACH')
            self.cruise = Cruise(460,0.78,410,2500)
            self.initial_descent = Flight_level(True, 0.76, 800, 'MACH')
            self.descent_100 = Flight_level(True, 280, 3500, 100)
            self.approach = Approach(250, 190, 1500)
            self.landing = Landing(137, 1400)
            return self
        except Exception as e:
            print(f'Error {e} when creating debug airplane.')
    def plane_to_dict(self) -> dict:
        '''Returns a dictionary from Aircraft object.'''
        try:
            aircraft_dict: dict = {}

            aircraft_dict['image'] = './images/' + self.technical.model + '-' + self.technical.variation + '.png'
            aircraft_dict['manufacturer'] = self.technical.manufacturer
            aircraft_dict['birth_year'] = self.technical.birth_year
            aircraft_dict['model'] = self.technical.model
            aircraft_dict['wingspan'] = self.technical.wingspan
            aircraft_dict['length'] = self.technical.length
            aircraft_dict['height'] = self.technical.height
            aircraft_dict['recat_eu'] = self.take_off.recat_eu
            aircraft_dict['wtc'] = self.take_off.wtc
            aircraft_dict['mtow'] = self.take_off.mtow
            aircraft_dict['to_distance'] = self.take_off.distance
            aircraft_dict['v2'] = self.take_off.v2
            aircraft_dict['ic_ias'] = self.initial_climb.ias
            aircraft_dict['ic_roc'] = self.initial_climb.roc
            aircraft_dict['150_ias'] = self.climb_150.ias
            aircraft_dict['150_roc'] = self.climb_150.roc
            aircraft_dict['240_ias'] = self.climb_240.ias
            aircraft_dict['240_roc'] = self.climb_240.roc
            aircraft_dict['machc_ias'] = self.climb_mach.ias
            aircraft_dict['machc_roc'] = self.climb_mach.roc
            aircraft_dict['tas'] = self.cruise.tas
            aircraft_dict['mach_cruise'] = self.cruise.mach
            aircraft_dict['ceiling'] = self.cruise.ceiling
            aircraft_dict['range'] = self.cruise.range
            aircraft_dict['machd_ias'] = self.initial_descent.ias
            aircraft_dict['machd_rod'] = self.initial_descent.roc
            aircraft_dict['100_ias'] = self.descent_100.ias
            aircraft_dict['100_rod'] = self.descent_100.roc
            aircraft_dict['approach_ias'] = self.approach.ias
            aircraft_dict['mcs'] = self.approach.mcs
            aircraft_dict['approach_rod'] = self.approach.rod
            aircraft_dict['vat'] = self.landing.vat
            aircraft_dict['apc'] = self.landing.apc
            aircraft_dict['ld_distance'] = self.landing.distance
            aircraft_dict['variation'] = self.technical.variation
            aircraft_dict['wing_position'] = self.technical.wing_position
            aircraft_dict['engine_position'] = self.technical.engn_position
            aircraft_dict['tail_configuration'] = self.technical.tail_config
            aircraft_dict['landing_gear'] = self.technical.land_gear

            return aircraft_dict
        except Exception as e:
            print(f'Error {e} when converting Aircraft object to dictionary.')