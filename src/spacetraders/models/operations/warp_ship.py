"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import shipfuel as shared_shipfuel
from ..shared import shipnav as shared_shipnav
from dataclasses_json import Undefined, dataclass_json
from spacetraders import utils
from typing import Optional



@dataclasses.dataclass
class WarpShipSecurity:
    agent_token: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class WarpShipRequestBody:
    waypoint_symbol: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('waypointSymbol') }})
    r"""The target destination."""
    




@dataclasses.dataclass
class WarpShipRequest:
    ship_symbol: str = dataclasses.field(metadata={'path_param': { 'field_name': 'shipSymbol', 'style': 'simple', 'explode': False }})
    request_body: Optional[WarpShipRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class WarpShip200ApplicationJSONData:
    fuel: shared_shipfuel.ShipFuel = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fuel') }})
    r"""Details of the ship's fuel tanks including how much fuel was consumed during the last transit or action."""
    nav: shared_shipnav.ShipNav = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nav') }})
    r"""The navigation information of the ship."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class WarpShip200ApplicationJSON:
    r"""The successful transit information including the route details and changes to ship fuel, supplies, and crew wages paid. The route includes the expected time of arrival."""
    data: WarpShip200ApplicationJSONData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    




@dataclasses.dataclass
class WarpShipResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    warp_ship_200_application_json_object: Optional[WarpShip200ApplicationJSON] = dataclasses.field(default=None)
    r"""The successful transit information including the route details and changes to ship fuel, supplies, and crew wages paid. The route includes the expected time of arrival."""
    

