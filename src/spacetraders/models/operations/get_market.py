"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import market as shared_market
from dataclasses_json import Undefined, dataclass_json
from spacetraders import utils
from typing import Optional



@dataclasses.dataclass
class GetMarketRequest:
    system_symbol: str = dataclasses.field(metadata={'path_param': { 'field_name': 'systemSymbol', 'style': 'simple', 'explode': False }})
    r"""The system symbol"""
    waypoint_symbol: str = dataclasses.field(metadata={'path_param': { 'field_name': 'waypointSymbol', 'style': 'simple', 'explode': False }})
    r"""The waypoint symbol"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetMarket200ApplicationJSON:
    r"""OK"""
    data: shared_market.Market = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    




@dataclasses.dataclass
class GetMarketResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_market_200_application_json_object: Optional[GetMarket200ApplicationJSON] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

