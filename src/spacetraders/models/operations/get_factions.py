"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import faction as shared_faction
from ..shared import meta as shared_meta
from dataclasses_json import Undefined, dataclass_json
from spacetraders import utils
from typing import Optional


@dataclasses.dataclass
class GetFactionsRequest:
    
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""How many entries to return per page"""
    page: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    r"""What entry offset to request"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetFactions200ApplicationJSON:
    
    data: list[shared_faction.Faction] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    meta: shared_meta.Meta = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('meta') }})
    

@dataclasses.dataclass
class GetFactionsResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_factions_200_application_json_object: Optional[GetFactions200ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    