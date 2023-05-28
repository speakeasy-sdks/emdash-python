"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class WaypointType(str, Enum):
    r"""The type of waypoint."""
    PLANET = 'PLANET'
    GAS_GIANT = 'GAS_GIANT'
    MOON = 'MOON'
    ORBITAL_STATION = 'ORBITAL_STATION'
    JUMP_GATE = 'JUMP_GATE'
    ASTEROID_FIELD = 'ASTEROID_FIELD'
    NEBULA = 'NEBULA'
    DEBRIS_FIELD = 'DEBRIS_FIELD'
    GRAVITY_WELL = 'GRAVITY_WELL'
