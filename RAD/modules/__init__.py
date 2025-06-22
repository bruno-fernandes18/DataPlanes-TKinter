"""Aggregate exports from subpackages for convenient access."""

from .classes import (
    Aircraft,
    Approach,
    Cruise,
    Flight_level,
    Landing,
    Take_off,
    Technical,
    User,
)
from .frames import (
    AccountMenu,
    AircraftMenu,
    MainMenu,
    PlaneCreator,
    PlaneManager,
)
from .models import (
    add_plane,
    add_user,
    boot_parts,
    boot_plane,
    boot_user,
    delete_parts,
    delete_plane,
    delete_user,
    get_parts,
    get_specific_part,
    insert_part,
    search_plane,
    search_user,
    update_parts,
    update_user,
    view_planes,
    view_users,
)

__all__ = [
    # classes
    "Aircraft",
    "Approach",
    "Cruise",
    "Flight_level",
    "Landing",
    "Take_off",
    "Technical",
    "User",
    # frames
    "AccountMenu",
    "AircraftMenu",
    "MainMenu",
    "PlaneCreator",
    "PlaneManager",
    # models
    "add_plane",
    "add_user",
    "boot_parts",
    "boot_plane",
    "boot_user",
    "delete_parts",
    "delete_plane",
    "delete_user",
    "get_parts",
    "get_specific_part",
    "insert_part",
    "search_plane",
    "search_user",
    "update_parts",
    "update_user",
    "view_planes",
    "view_users",
]
