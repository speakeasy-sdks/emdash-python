"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import shiprequirements as shared_shiprequirements
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from spacetraders import utils
from typing import Optional

class ShipFrameSymbol(str, Enum):
    FRAME_PROBE = 'FRAME_PROBE'
    FRAME_DRONE = 'FRAME_DRONE'
    FRAME_INTERCEPTOR = 'FRAME_INTERCEPTOR'
    FRAME_RACER = 'FRAME_RACER'
    FRAME_FIGHTER = 'FRAME_FIGHTER'
    FRAME_FRIGATE = 'FRAME_FRIGATE'
    FRAME_SHUTTLE = 'FRAME_SHUTTLE'
    FRAME_EXPLORER = 'FRAME_EXPLORER'
    FRAME_MINER = 'FRAME_MINER'
    FRAME_LIGHT_FREIGHTER = 'FRAME_LIGHT_FREIGHTER'
    FRAME_HEAVY_FREIGHTER = 'FRAME_HEAVY_FREIGHTER'
    FRAME_TRANSPORT = 'FRAME_TRANSPORT'
    FRAME_DESTROYER = 'FRAME_DESTROYER'
    FRAME_CRUISER = 'FRAME_CRUISER'
    FRAME_CARRIER = 'FRAME_CARRIER'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ShipFrame:
    r"""The frame of the ship. The frame determines the number of modules and mounting points of the ship, as well as base fuel capacity. As the condition of the frame takes more wear, the ship will become more sluggish and less maneuverable."""
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    fuel_capacity: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fuelCapacity') }})
    module_slots: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('moduleSlots') }})
    mounting_points: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mountingPoints') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    requirements: shared_shiprequirements.ShipRequirements = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requirements') }})
    r"""The requirements for installation on a ship"""
    symbol: ShipFrameSymbol = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('symbol') }})
    condition: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('condition'), 'exclude': lambda f: f is None }})
    r"""Condition is a range of 0 to 100 where 0 is completely worn out and 100 is brand new."""
    

