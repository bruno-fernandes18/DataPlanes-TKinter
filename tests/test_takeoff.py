import importlib.util
import pathlib
import sys
import types
import pytest

# Dynamically load takeoff and technical modules without executing the rest of
# the project package imports. We emulate the minimal package structure needed
# for their relative imports to work.
ROOT = pathlib.Path(__file__).resolve().parents[1]
PLANEINFO_DIR = ROOT / "RAD" / "modules" / "classes" / "planeInfo"

# Create a fake package for planeInfo
planeinfo_pkg = types.ModuleType("planeInfo")
planeinfo_pkg.__path__ = [str(PLANEINFO_DIR)]
sys.modules["planeInfo"] = planeinfo_pkg

def load_module(mod_name: str, file_name: str):
    spec = importlib.util.spec_from_file_location(f"planeInfo.{mod_name}", PLANEINFO_DIR / file_name)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module

technical_module = load_module("technical", "technical.py")
takeoff_module = load_module("takeoff", "takeoff.py")

Technical = technical_module.Technical
Take_off = takeoff_module.Take_off


def make_technical():
    """Return a minimal Technical instance for testing."""
    return Technical(
        manufacturer="Test",
        birth_year=2020,
        model="T",
        variation="",
        wingspan=30.0,
        wing_position="",
        engn_position="",
        tail_config="",
        land_gear="",
        length=10.0,
        height=5.0,
    )


def test_wtc_light():
    tech = make_technical()
    takeoff = Take_off(mtow=6000, technical_param=tech, distance=0, v2=0)
    assert takeoff.wtc == "L"


def test_wtc_medium():
    tech = make_technical()
    takeoff = Take_off(mtow=10000, technical_param=tech, distance=0, v2=0)
    assert takeoff.wtc == "M"


def test_wtc_heavy():
    tech = make_technical()
    takeoff = Take_off(mtow=150000, technical_param=tech, distance=0, v2=0)
    assert takeoff.wtc == "H"
