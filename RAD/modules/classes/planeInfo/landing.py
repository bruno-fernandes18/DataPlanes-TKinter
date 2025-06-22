class Landing:
    '''Landing object containing VAT, APC, and Distance data.'''
    def __init__(self, vat: int, distance: int):
        '''Initializes Landing object.'''
        self.vat: int = vat
        self.apc: str = self.find_apc(vat)
        self.distance: int = distance

    def find_apc(self, vat: int) -> str:
        '''Returns APC from VAT in knots.'''
        if vat < 91:
            return 'A'
        elif vat < 121:
            return 'B'
        elif vat < 141:
            return 'C'
        elif vat < 166:
            return 'D'
        elif vat >= 167:
            return 'E'