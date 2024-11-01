class Flight_level:
    '''Flight Level object containing IAS and ROC/ROD data. If there is no data, just set (has_data=False). If Flight Level uses MACH, set (climb="MACH").'''
    def __init__(self, has_data: bool, ias, roc: int, climb):
        '''Initializes Flight Level object.'''
        try:
            self.has_data: bool = has_data
            if self.has_data == True:
                self.ias = round(float(ias),2) if climb == 'MACH' else ias
                self.roc: int = roc
                self.climb: int = climb
            else:
                self.ias: bool = None
                self.roc: bool = None
                self.climb: bool = None
        except Exception as e:
            print(f'Error {e} when booting Flight Level class.')