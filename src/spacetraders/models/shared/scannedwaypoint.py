"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import chart as shared_chart
from ..shared import waypointfaction as shared_waypointfaction
from ..shared import waypointorbital as shared_waypointorbital
from ..shared import waypointtrait as shared_waypointtrait
from ..shared import waypointtype as shared_waypointtype
from dataclasses_json import Undefined, dataclass_json
from spacetraders import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ScannedWaypoint:
    r"""A waypoint is a location that ships can travel to such as a Planet, Moon or Space Station."""
    orbitals: list[shared_waypointorbital.WaypointOrbital] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('orbitals') }})
    symbol: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('symbol') }})
    system_symbol: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systemSymbol') }})
    traits: list[shared_waypointtrait.WaypointTrait] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('traits') }})
    r"""The traits of the waypoint."""
    type: shared_waypointtype.WaypointType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of waypoint."""
    x: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('x') }})
    y: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('y') }})
    chart: Optional[shared_chart.Chart] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('chart'), 'exclude': lambda f: f is None }})
    r"""The chart of a system or waypoint, which makes the location visible to other agents."""
    faction: Optional[shared_waypointfaction.WaypointFaction] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('faction'), 'exclude': lambda f: f is None }})
    

