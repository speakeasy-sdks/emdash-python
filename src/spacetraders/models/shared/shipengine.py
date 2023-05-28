"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import shiprequirements as shared_shiprequirements
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from spacetraders import utils
from typing import Optional

class ShipEngineSymbol(str, Enum):
    ENGINE_IMPULSE_DRIVE_I = 'ENGINE_IMPULSE_DRIVE_I'
    ENGINE_ION_DRIVE_I = 'ENGINE_ION_DRIVE_I'
    ENGINE_ION_DRIVE_II = 'ENGINE_ION_DRIVE_II'
    ENGINE_HYPER_DRIVE_I = 'ENGINE_HYPER_DRIVE_I'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ShipEngine:
    r"""The engine determines how quickly a ship travels between waypoints."""
    
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    requirements: shared_shiprequirements.ShipRequirements = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requirements') }})
    r"""The requirements for installation on a ship"""
    speed: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('speed') }})
    symbol: ShipEngineSymbol = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('symbol') }})
    condition: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('condition'), 'exclude': lambda f: f is None }})
    r"""Condition is a range of 0 to 100 where 0 is completely worn out and 100 is brand new."""
    