"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import shiprole as shared_shiprole
from dataclasses_json import Undefined, dataclass_json
from spacetraders import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ShipRegistration:
    r"""The public registration information of the ship"""
    faction_symbol: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('factionSymbol') }})
    r"""The symbol of the faction the ship is registered with"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The agent's registered name of the ship"""
    role: shared_shiprole.ShipRole = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('role') }})
    r"""The registered role of the ship"""
    

