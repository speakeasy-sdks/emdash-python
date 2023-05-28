"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import shipcargo as shared_shipcargo
from dataclasses_json import Undefined, dataclass_json
from spacetraders import utils
from typing import Optional


@dataclasses.dataclass
class JettisonSecurity:
    
    agent_token: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class JettisonRequestBody:
    
    symbol: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('symbol') }})
    units: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('units') }})
    

@dataclasses.dataclass
class JettisonRequest:
    
    ship_symbol: str = dataclasses.field(metadata={'path_param': { 'field_name': 'shipSymbol', 'style': 'simple', 'explode': False }})
    request_body: Optional[JettisonRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Jettison200ApplicationJSONData:
    
    cargo: shared_shipcargo.ShipCargo = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cargo') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Jettison200ApplicationJSON:
    r"""OK"""
    
    data: Jettison200ApplicationJSONData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    

@dataclasses.dataclass
class JettisonResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    jettison_200_application_json_object: Optional[Jettison200ApplicationJSON] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    