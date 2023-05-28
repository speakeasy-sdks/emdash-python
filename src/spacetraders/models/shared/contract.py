"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import contractterms as shared_contractterms
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from spacetraders import utils
from typing import Optional

class ContractType(str, Enum):
    PROCUREMENT = 'PROCUREMENT'
    TRANSPORT = 'TRANSPORT'
    SHUTTLE = 'SHUTTLE'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Contract:
    
    accepted: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accepted') }})
    r"""Whether the contract has been accepted by the agent"""
    expiration: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expiration'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""Deprecated in favor of deadlineToAccept"""
    faction_symbol: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('factionSymbol') }})
    r"""The symbol of the faction that this contract is for."""
    fulfilled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fulfilled') }})
    r"""Whether the contract has been fulfilled"""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    terms: shared_contractterms.ContractTerms = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('terms') }})
    type: ContractType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    deadline_to_accept: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deadlineToAccept'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The time at which the contract is no longer available to be accepted"""
    