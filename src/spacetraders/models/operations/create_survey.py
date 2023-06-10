"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import cooldown as shared_cooldown
from ..shared import survey as shared_survey
from dataclasses_json import Undefined, dataclass_json
from spacetraders import utils
from typing import Optional



@dataclasses.dataclass
class CreateSurveySecurity:
    agent_token: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    




@dataclasses.dataclass
class CreateSurveyRequest:
    ship_symbol: str = dataclasses.field(metadata={'path_param': { 'field_name': 'shipSymbol', 'style': 'simple', 'explode': False }})
    r"""The symbol of the ship"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateSurvey201ApplicationJSONData:
    cooldown: shared_cooldown.Cooldown = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cooldown') }})
    r"""A cooldown is a period of time in which a ship cannot perform certain actions."""
    surveys: list[shared_survey.Survey] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('surveys') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateSurvey201ApplicationJSON:
    r"""Created"""
    data: CreateSurvey201ApplicationJSONData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    




@dataclasses.dataclass
class CreateSurveyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_survey_201_application_json_object: Optional[CreateSurvey201ApplicationJSON] = dataclasses.field(default=None)
    r"""Created"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

