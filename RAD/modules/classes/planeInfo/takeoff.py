from .technical import Technical

class Take_off:
    '''Take Off object containing MTOW, WTC, RECAT-EU and V2 data.'''
    def __init__(self, mtow: int, technical_param: Technical, distance: int, v2: int):
        '''Initializes Take Off object.'''
        try:
            self.mtow: int = mtow        
            self.wtc: str = self.find_wtc(mtow)
            self.recat_eu: str = self.find_recat_eu(mtow, technical_param)
            self.distance: int = distance
            self.v2: int = v2
        except Exception as e:
            print('Error {e} when booting Take Off class')

    def find_wtc(self, mtow: int) -> str:
        '''Returns WTC from MTOW in Kilograms.'''
        try:
            if mtow < 7000:
                return 'L'
            elif mtow < 136000:
                return 'M'
            else:
                return 'H'
        except Exception as e:
            print(f'Error {e} on WTC calculus.')
    def find_recat_eu(self, mtow: int, technical_param: Technical) -> str:
        '''Returns RECAT-EU from MTOW in Kilograms and EU Specific Analysis.'''
        try:
            if mtow < 15000:
                return 'CAT-F'
            elif mtow < 100000:
                if technical_param.wingspan < 32:
                    return 'CAT-E'
                else:
                    if technical_param.eu_specific_analysis != None:
                        if technical_param.eu_specific_analysis != False:
                            return technical_param.eu_specific_analysis
                    else:
                        return 'CAT-D'
            elif mtow >= 100000:
                if technical_param.wingspan < 52:
                    if technical_param.eu_specific_analysis != None:
                        if technical_param.eu_specific_analysis != False:
                            return technical_param.eu_specific_analysis
                    else:
                        return 'CAT-C'
                elif technical_param.wingspan < 60:
                    if technical_param.eu_specific_analysis != None:
                        if technical_param.eu_specific_analysis != False:
                            return technical_param.eu_specific_analysis
                    else:
                        return '!'
                elif technical_param.wingspan < 72:
                    if technical_param.eu_specific_analysis != None:
                        if technical_param.eu_specific_analysis != False:
                            return technical_param.eu_specific_analysis
                    else:
                        return 'CAT-B'
                elif technical_param.wingspan < 80:
                    return 'CAT-A'
                else:
                    return '*'
        except Exception as e:
            print(f'Error {e} on RECAT-EU calculus.')
