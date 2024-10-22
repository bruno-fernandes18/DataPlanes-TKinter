class Technical:
    def __init__(self, wingspan: float, lenght: float, height: float, eu_specific_analysis: str):
        self.wingspan: float = round(wingspan, 2)
        self.lenght: float = round(lenght, 2)
        self.height: float = round(height, 2)

        if isinstance(eu_specific_analysis, str):
            self.eu_specific_analysis: str = eu_specific_analysis
        else:
            self.eu_specific_analysis: bool = False

class Take_off:
    def __init__(self, mtow: int, technical: Technical, distance: int, v2: int):
        self.mtow: int = mtow # Maximum Take-Off Weight, kg
        self.mtow_e = '"MTOW" stands for "Maximum Take-Off Weight". It is measured in Kilograms, and defines the maximun weight an aircraft is certified to take off at.'
        
        if self.mtow < 7000: # Wake Turbulence Category, (L,M,H,J)
            self.wtc: str = 'L'
        elif self.mtow < 136000:
            self.wtc: str = 'M'
        elif self.mtow >= 13600:
            self.wtc: str = 'H'
        self.wtc_e = '"WTC" stands for "Wake Turbulence Category". It is based on the MTOW of an aircraft, and may stand for: Light(L), Medium(M), Heavy(H), Super(J).'

        if self.mtow < 15000:
            self.recat_eu: str = 'CAT-F'
        elif self.mtow < 100000:
            if technical.wingspan < 32:
                self.recat_eu: str = 'CAT-E'
            else:
                self.recat_eu: str = 'CAT-D'
            if technical.eu_specific_analysis != False:
                self.recat_eu: str = technical.eu_specific_analysis
        elif self.mtow >= 100000:
            if technical.wingspan < 52:
                self.recat_eu: str = 'CAT-C'
                if technical.eu_specific_analysis != False:
                    self.recat_eu: str = technical.eu_specific_analysis
            elif technical.wingspan < 60:
                if technical.eu_specific_analysis == False:
                    self.recat_eu: str = '!'
                else:
                    self.recat_eu: str = technical.eu_specific_analysis
            elif technical.wingspan < 72:
                self.recat_eu: str = 'CAT-B'
                if technical.eu_specific_analysis != False:
                    self.recat_eu: str = technical.eu_specific_analysis
            elif technical.wingspan < 80:
                self.recat_eu: str = 'CAT-A'
            else:
                self.recat_eu: str = '*'
        self.recat_eu_e = '"RECAT-EU" is a proposition by EUROCONTROL to update wake turbulence categories. The classifications are as following: CAT-A(Super Heavy), CAT-B(Upper Heavy), CAT-C(Lower Heavy), CAT-D(Upper Medium), CAT-E(Lower Medium), CAT-F(Light).'

        self.distance: int = distance # Minimum Runway Lenght, m
        self.distance_e = 'Minimum runway lenght required for take-off. It is measured in meters.'

        self.v2: int = v2 # Take-off Speed, kts
        self.v2_e = 'Indicated Aircraft Speed (IAS) for take-off. It is measured in knots and defines the minimum speed to keep safe flight after take-off.'

class Climb_levels:
    def __init__(self, has_data: bool, ias, roc: int, climb):
        self.has_data: bool = has_data

        if self.has_data == True:
            if isinstance(climb, int): # Indicated Airspeed, knots or mach
                self.ias: int = ias 
            elif isinstance(climb, str):
                self.ias: float = round(ias,2)
            
            self.roc: int = roc # Rate of Climb, ft/min

            if isinstance(climb, int): # or Climb FL (Foot Level), or MACH climb
                self.climb = climb
            elif climb == 'mach':
                self.climb: str = 'MACH'
            else:
                self.climb: bool = False
        else:
            self.ias: bool = False
            self.roc: bool = False
            self.climb: bool = False

class Cruise:
    def __init__(self, tas: int, mach: float, ceiling: int, range: int):
        self.tas: int = tas # True Airspeed, knots

        if mach == -1: # Mach Speed, mach
            self.mach: bool = False
        else:
            self.mach: float = round(mach, 2)
        
        self.ceiling: int = ceiling # Maximum Altitude, ft
        self.range: int = range # Maximum Range, NM

class Descent:
    def __init__(self, has_data: bool, ias, rod: int, descent):
        self.has_data = has_data

        if self.has_data == True: # Indicated Airspeed, knots or mach
            if isinstance(descent, int):
                self.ias: int = ias
            elif isinstance(descent, str):
                self.ias: float = round(ias, 2)
            self.rod: int = rod # Rate of Descent, ft/min
            if isinstance(descent, int):
                self.descent: int = descent
            elif descent == 'mach':
                self.descent: str = 'MACH'
            else:
                self.descent: bool = False

class Approach:
    def __init__(self, ias: int, mcs: int, rod: int):
        self.ias: int = ias # Indicated Airspeed, knots
        self.mcs: int = mcs # Minimum Control Speed, knots
        self.rod: int = rod # Rate of Descent, ft/min

class Landing:
    def __init__(self, vat: int, distance: int):
        self.vat: int = vat # Velocity at Threshold (IAS), knots

        if self.vat < 91: # Aircraft Performance Category, (A,B,C,D,E)
            self.apc: str = 'A'
        elif self.vat < 120:
            self.apc: str = 'B'
        elif self.vat < 140:
            self.apc: str = 'C'
        elif self.vat < 165:
            self.apc: str = 'D'
        elif self.vat >= 166:
            self.apc: str = 'E'

        self.distance: int = distance # Minimum Landing Distance

class Aircraft:
    def __init__(self, Technical_obj: Technical, Take_off_obj: Take_off, Initial_climb_obj: Climb_levels, Climb_150_obj: Climb_levels, Climb_240_obj: Climb_levels, Climb_mach_obj: Climb_levels, Cruise_obj: Cruise, Initial_descent_obj: Descent, Descent_100_obj: Descent, Approach_obj: Approach, Landing_obj: Landing):
        self.technical: Technical = Technical_obj
        self.take_off: Take_off = Take_off_obj

        self.climb_150: Climb_levels = Climb_150_obj
        self.climb_240: Climb_levels = Climb_240_obj
        self.climb_mach: Climb_levels = Climb_mach_obj

        self.cruise: Cruise = Cruise_obj

        self.initial_descent: Descent = Initial_descent_obj
        self.descent_100: Descent = Descent_100_obj

        self.approach: Approach = Approach_obj
        self.landing: Landing = Landing_obj