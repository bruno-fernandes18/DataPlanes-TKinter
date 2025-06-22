from dataclasses import dataclass, field

from .technical import Technical


@dataclass
class Take_off:
    """Take-off performance information."""

    mtow: int
    technical_param: Technical
    distance: int
    v2: int
    wtc: str = field(init=False)
    recat_eu: str = field(init=False)

    def __post_init__(self) -> None:
        self.wtc = self.find_wtc(self.mtow)
        self.recat_eu = self.find_recat_eu(self.mtow, self.technical_param)

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
