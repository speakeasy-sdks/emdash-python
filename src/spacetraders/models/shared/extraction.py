"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import extractionyield as shared_extractionyield
from dataclasses_json import Undefined, dataclass_json
from spacetraders import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Extraction:
    ship_symbol: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shipSymbol') }})
    yield_: shared_extractionyield.ExtractionYield = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('yield') }})
    

