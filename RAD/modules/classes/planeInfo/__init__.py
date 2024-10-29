try:
    from .approach import Approach
    from .cruise import Cruise
    from .flightlevel import Flight_level
    from .landing import Landing
    from .takeoff import Take_off
    from .technical import Technical

    __all__ = ["Approach", "Cruise", "Flight_level", "Landing", "Take_off", "Technical"]
except Exception as e:
    print(f'Error {e} on PlaneInfo Module.')
    input()
