class AircraftBuilder:
    def __init__(self):
        self.aircraft = {}

    def set(self, key, value):
        self.aircraft[key] = value
        return self

    def build(self):
        return dict(self.aircraft)
