"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import agent as shared_agent
from ..shared import contract as shared_contract
from dataclasses_json import Undefined, dataclass_json
from spacetraders import utils
from typing import Optional



@dataclasses.dataclass
class AcceptContractSecurity:
    agent_token: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    




@dataclasses.dataclass
class AcceptContractRequest:
    contract_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'contractId', 'style': 'simple', 'explode': False }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AcceptContract200ApplicationJSONData:
    agent: shared_agent.Agent = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('agent') }})
    contract: shared_contract.Contract = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contract') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AcceptContract200ApplicationJSON:
    r"""OK"""
    data: AcceptContract200ApplicationJSONData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    




@dataclasses.dataclass
class AcceptContractResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    accept_contract_200_application_json_object: Optional[AcceptContract200ApplicationJSON] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

