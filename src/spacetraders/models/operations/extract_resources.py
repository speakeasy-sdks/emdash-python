"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import cooldown as shared_cooldown
from ..shared import extraction as shared_extraction
from ..shared import shipcargo as shared_shipcargo
from ..shared import survey as shared_survey
from dataclasses_json import Undefined, dataclass_json
from spacetraders import utils
from typing import Optional



@dataclasses.dataclass
class ExtractResourcesSecurity:
    agent_token: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ExtractResourcesRequestBody:
    survey: Optional[shared_survey.Survey] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('survey'), 'exclude': lambda f: f is None }})
    r"""A resource survey of a waypoint, detailing a specific extraction location and the types of resources that can be found there."""
    




@dataclasses.dataclass
class ExtractResourcesRequest:
    ship_symbol: str = dataclasses.field(metadata={'path_param': { 'field_name': 'shipSymbol', 'style': 'simple', 'explode': False }})
    r"""The ship symbol"""
    request_body: Optional[ExtractResourcesRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ExtractResources201ApplicationJSONData:
    cargo: shared_shipcargo.ShipCargo = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cargo') }})
    cooldown: shared_cooldown.Cooldown = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cooldown') }})
    r"""A cooldown is a period of time in which a ship cannot perform certain actions."""
    extraction: shared_extraction.Extraction = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('extraction') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ExtractResources201ApplicationJSON:
    r"""Created"""
    data: ExtractResources201ApplicationJSONData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    




@dataclasses.dataclass
class ExtractResourcesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    extract_resources_201_application_json_object: Optional[ExtractResources201ApplicationJSON] = dataclasses.field(default=None)
    r"""Created"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

