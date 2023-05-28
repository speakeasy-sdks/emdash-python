"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import cooldown as shared_cooldown
from ..shared import scannedsystem as shared_scannedsystem
from dataclasses_json import Undefined, dataclass_json
from spacetraders import utils
from typing import Optional


@dataclasses.dataclass
class CreateShipSystemScanSecurity:
    
    agent_token: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class CreateShipSystemScanRequest:
    
    ship_symbol: str = dataclasses.field(metadata={'path_param': { 'field_name': 'shipSymbol', 'style': 'simple', 'explode': False }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateShipSystemScan201ApplicationJSONData:
    
    cooldown: shared_cooldown.Cooldown = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cooldown') }})
    r"""A cooldown is a period of time in which a ship cannot perform certain actions."""
    systems: list[shared_scannedsystem.ScannedSystem] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systems') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateShipSystemScan201ApplicationJSON:
    r"""Created"""
    
    data: CreateShipSystemScan201ApplicationJSONData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    

@dataclasses.dataclass
class CreateShipSystemScanResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_ship_system_scan_201_application_json_object: Optional[CreateShipSystemScan201ApplicationJSON] = dataclasses.field(default=None)
    r"""Created"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    