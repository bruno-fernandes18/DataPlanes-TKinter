class Approach:
    '''Approach object containing IAS, MCS, and ROD data.'''
    def __init__(self, ias: int, mcs: int, rod: int):
        '''Initializes Approach object.'''
        self.ias: int = ias
        self.mcs: int = mcs
        self.rod: int = rod