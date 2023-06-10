"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import shiptype as shared_shiptype
from ..shared import shipyardship as shared_shipyardship
from ..shared import shipyardtransaction as shared_shipyardtransaction
from dataclasses_json import Undefined, dataclass_json
from spacetraders import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ShipyardShipTypes:
    type: Optional[shared_shiptype.ShipType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Shipyard:
    ship_types: list[ShipyardShipTypes] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shipTypes') }})
    r"""The list of ship types available for purchase at this shipyard."""
    symbol: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('symbol') }})
    r"""The symbol of the shipyard. The symbol is the same as the waypoint where the shipyard is located."""
    ships: Optional[list[shared_shipyardship.ShipyardShip]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ships'), 'exclude': lambda f: f is None }})
    r"""The ships that are currently available for purchase at the shipyard."""
    transactions: Optional[list[shared_shipyardtransaction.ShipyardTransaction]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transactions'), 'exclude': lambda f: f is None }})
    r"""The list of recent transactions at this shipyard."""
    

