"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import ship as shared_ship
from dataclasses_json import Undefined, dataclass_json
from spacetraders import utils
from typing import Optional


@dataclasses.dataclass
class GetMyShipSecurity:
    
    agent_token: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetMyShipRequest:
    
    ship_symbol: str = dataclasses.field(metadata={'path_param': { 'field_name': 'shipSymbol', 'style': 'simple', 'explode': False }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetMyShip200ApplicationJSON:
    r"""OK"""
    
    data: shared_ship.Ship = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    r"""A ship"""
    

@dataclasses.dataclass
class GetMyShipResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_my_ship_200_application_json_object: Optional[GetMyShip200ApplicationJSON] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    