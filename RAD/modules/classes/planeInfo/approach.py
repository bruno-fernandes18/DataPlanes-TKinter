from dataclasses import dataclass


@dataclass
class Approach:
    """Approach phase data."""

    ias: int = 0
    mcs: int = 0
    rod: int = 0
