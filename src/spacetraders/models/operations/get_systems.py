"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import meta as shared_meta
from ..shared import system as shared_system
from dataclasses_json import Undefined, dataclass_json
from spacetraders import utils
from typing import Optional


@dataclasses.dataclass
class GetSystemsRequest:
    
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""How many entries to return per page"""
    page: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    r"""What entry offset to request"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSystems200ApplicationJSON:
    r"""OK"""
    
    data: list[shared_system.System] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    meta: shared_meta.Meta = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('meta') }})
    

@dataclasses.dataclass
class GetSystemsResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_systems_200_application_json_object: Optional[GetSystems200ApplicationJSON] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    