"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import systemfaction as shared_systemfaction
from ..shared import systemtype as shared_systemtype
from ..shared import systemwaypoint as shared_systemwaypoint
from dataclasses_json import Undefined, dataclass_json
from spacetraders import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class System:
    
    factions: list[shared_systemfaction.SystemFaction] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('factions') }})
    sector_symbol: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sectorSymbol') }})
    symbol: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('symbol') }})
    type: shared_systemtype.SystemType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of waypoint."""
    waypoints: list[shared_systemwaypoint.SystemWaypoint] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('waypoints') }})
    x: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('x') }})
    y: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('y') }})
    