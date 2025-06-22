import modules as m
from tkinter import messagebox
from datetime import datetime
from typing import Optional


class DatabaseService:
    """Service layer handling interactions with the database."""

    def manager_package(self) -> tuple:
        aircraft_list = m.view_planes()
        ids, names = self.db_to_tuple()
        try:
            creator = tuple(aircraft[1] for aircraft in aircraft_list)
            creation_raw = tuple(aircraft[2] for aircraft in aircraft_list)
            creation = tuple(
                datetime.fromisoformat(date).strftime("%d/%m/%Y")
                for date in creation_raw
            )
        except Exception as e:
            messagebox.showerror('Error', e)

        return tuple(zip(ids, names, creator, creation))

    def db_to_tuple(self) -> tuple:
        """Return tuples with all aircraft ids and names."""
        aircraft_list = m.view_planes()

        def get_ids() -> tuple:
            try:
                return tuple(aircraft[0] for aircraft in aircraft_list)
            except Exception as e:
                messagebox.showerror('Error', e)
                return None

        def get_names() -> tuple:
            try:
                technical_ids = tuple(aircraft[3] for aircraft in aircraft_list)
                technical_raw = (
                    m.get_specific_part('technical', id) for id in technical_ids
                )
                technical_list = tuple(t[0] for t in technical_raw)
                model_tuple = tuple(t[3] for t in technical_list)
                var_tuple = tuple(t[4] for t in technical_list)
                return tuple(
                    model + '-' + variation
                    for model, variation in zip(model_tuple, var_tuple)
                )
            except Exception as e:
                messagebox.showerror('Error', e)
                return None

        return get_ids(), get_names()

    def db_to_obj(self, id: int) -> m.Aircraft:
        parts = m.get_parts(id)
        try:
            tech = parts['technical']
            Technical_obj = m.Technical(
                tech[1], tech[2], tech[3], tech[4], tech[5], tech[6], tech[7],
                tech[8], tech[9], tech[10], tech[11], tech[12]
            )
            Takeoff_obj = m.Take_off(
                parts['takeoff'][1], Technical_obj, parts['takeoff'][2], parts['takeoff'][3]
            )
            Initial_climb_obj = m.Flight_level(True, parts['initialclimb'][1], parts['initialclimb'][2], 'Initial Climb')
            Climb_150_obj = m.Flight_level(True, parts['climb150'][2], parts['climb150'][3], 150)
            Climb_240_obj = m.Flight_level(parts['climb240'][1], parts['climb240'][2], parts['climb240'][3], 240)
            Climb_mach_obj = m.Flight_level(parts['climbmach'][1], parts['climbmach'][2], parts['climbmach'][3], 'MACH')
            Cruise_obj = m.Cruise(parts['cruise'][1], parts['cruise'][2], parts['cruise'][3], parts['cruise'][4])
            Initial_descent_obj = m.Flight_level(parts['initialdescent'][1], parts['initialdescent'][2], parts['initialdescent'][3], 'MACH')
            Descent_100_obj = m.Flight_level(True, parts['descent100'][1], parts['descent100'][2], 100)
            Approach_obj = m.Approach(parts['approach'][1], parts['approach'][2], parts['approach'][3])
            Landing_obj = m.Landing(parts['landing'][1], parts['landing'][2])
        except Exception as e:
            print(f'Error {e} when creating Sub-Objects from Database.')

        try:
            return m.Aircraft(
                Technical_obj, Takeoff_obj, Initial_climb_obj, Climb_150_obj,
                Climb_240_obj, Climb_mach_obj, Cruise_obj, Initial_descent_obj,
                Descent_100_obj, Approach_obj, Landing_obj
            )
        except Exception as e:
            print(f'Error {e} when creating Aircraft Object from Database.')
            raise

    def db_to_dict(self, id: int) -> dict:
        return self.db_to_obj(id).plane_to_dict()

    def plane_to_db(self, user: Optional[str], plane: Optional[dict]) -> bool:
        if user is None:
            messagebox.showerror('Error', 'You must login to add a plane!')
            return False
        try:
            if plane:
                m.boot_parts()
                m.boot_plane()
        except Exception as e:
            messagebox.showerror('Error', e)
            return False
        if plane:
            try:
                p = plane
                data_technical = (
                    p['manufacturer'], p['birth_year'], p['model'], p['variation'],
                    p['wingspan'], p['wing_position'], p['engine_position'],
                    p['tail_configuration'], p['landing_gear'], p['length'],
                    p['height'], p['eu_analysis']
                )
                data_takeoff = (p['mtow'], p['to_distance'], p['v2'])
                data_initialclimb = (p['ic_ias'], p['ic_roc'])
                data_climb150 = (p['150_hd'], p['150_ias'], p['150_roc'])
                data_climb240 = (p['240_hd'], p['240_ias'], p['240_roc'])
                data_climbmach = (p['machc_hd'], p['machc_ias'], p['machc_roc'])
                data_cruise = (p['tas'], p['mach_cruise'], p['ceiling'], p['range'])
                data_initialdescent = (p['machd_hd'], p['machd_ias'], p['machd_rod'])
                data_descent100 = (p['100_ias'], p['100_rod'])
                data_approach = (p['approach_ias'], p['mcs'], p['approach_rod'])
                data_landing = (p['vat'], p['ld_distance'])

                technical_id = m.insert_part('technical', data_technical)
                takeoff_id = m.insert_part('takeoff', data_takeoff)
                initialclimb_id = m.insert_part('initialclimb', data_initialclimb)
                climb150_id = m.insert_part('climb150', data_climb150)
                climb240_id = m.insert_part('climb240', data_climb240)
                climbmach_id = m.insert_part('climbmach', data_climbmach)
                cruise_id = m.insert_part('cruise', data_cruise)
                initialdescent_id = m.insert_part('initialdescent', data_initialdescent)
                descent100_id = m.insert_part('descent100', data_descent100)
                approach_id = m.insert_part('approach', data_approach)
                landing_id = m.insert_part('landing', data_landing)

                m.add_plane(
                    (
                        user,
                        datetime.now(),
                        technical_id,
                        takeoff_id,
                        initialclimb_id,
                        climb150_id,
                        climb240_id,
                        climbmach_id,
                        cruise_id,
                        initialdescent_id,
                        descent100_id,
                        approach_id,
                        landing_id,
                    )
                )
                return True
            except Exception as e:
                messagebox.showerror('Error', e)
                return False
        return False

    def dict_to_db(self, id: int, aircraft_dict: dict) -> None:
        airplane = m.search_plane(id)
        conversion = {
            'approach': 12,
            'climb150': 6,
            'climb240': 7,
            'climbmach': 8,
            'cruise': 9,
            'descent100': 11,
            'initialclimb': 5,
            'initialdescent': 10,
            'landing': 13,
            'takeoff': 4,
            'technical': 3,
        }
        try:
            for key in aircraft_dict:
                if key in conversion:
                    part_id = airplane[conversion[key]]
                    m.update_parts(key, part_id, aircraft_dict[key])
        except Exception as e:
            messagebox.showerror('Error', e)

    def login(self, name: str, password: str):
        m.boot_user()
        user = m.search_user(name)
        if user:
            if user[0][2] == password:
                return user[0][1]
            messagebox.showerror('Alert', 'Invalid Password')
            return None
        messagebox.showerror('Alert', 'Invalid Username')
        return None

    def register(self, name: str, password: str) -> bool:
        m.boot_user()
        try:
            m.add_user(name, password)
            return True
        except Exception as e:
            messagebox.showerror('Error', e)
            return False

    def delete_plane(self, id: int) -> None:
        raw_tuple = m.search_plane(id)
        id_tuple = (
            raw_tuple[12], raw_tuple[6], raw_tuple[7], raw_tuple[8], raw_tuple[9],
            raw_tuple[11], raw_tuple[5], raw_tuple[10], raw_tuple[13], raw_tuple[4],
            raw_tuple[3]
        )
        try:
            m.delete_parts(id_tuple)
        except Exception as e:
            messagebox.showerror('Error', e)
            return
        try:
            m.delete_plane(id)
        except Exception as e:
            messagebox.showerror('Error', e)
            return
        messagebox.showinfo(
            'Success',
            "Plane Successfuly Deleted! If you created an Image you should consider deleting it in this script's directory.",
        )

    def similar_planes(self, id: int, limit: int = 5) -> tuple:
        """Return up to ``limit`` aircraft names similar to the given plane id."""
        base_plane = self.db_to_dict(id)
        ids, names = self.db_to_tuple()
        comparisons = []
        for pid, name in zip(ids, names):
            if pid == id:
                continue
            other = self.db_to_dict(pid)
            diff = 0
            diff += 0 if other['wtc'] == base_plane['wtc'] else 1
            diff += 0 if other['recat_eu'] == base_plane['recat_eu'] else 1
            diff += abs(other['tas'] - base_plane['tas']) / base_plane['tas']
            diff += abs(other['vat'] - base_plane['vat']) / base_plane['vat']
            diff += abs(other['ld_distance'] - base_plane['ld_distance']) / base_plane['ld_distance']
            diff /= 5
            if diff <= 0.1:
                comparisons.append((diff, name))
        if not comparisons:
            return ('No Similar Aircrafts',)
        comparisons.sort(key=lambda x: x[0])
        return tuple(name for _, name in comparisons[:limit])
