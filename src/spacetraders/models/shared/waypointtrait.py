"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from spacetraders import utils

class WaypointTraitSymbol(str, Enum):
    r"""The unique identifier of the trait."""
    UNCHARTED = 'UNCHARTED'
    MARKETPLACE = 'MARKETPLACE'
    SHIPYARD = 'SHIPYARD'
    OUTPOST = 'OUTPOST'
    SCATTERED_SETTLEMENTS = 'SCATTERED_SETTLEMENTS'
    SPRAWLING_CITIES = 'SPRAWLING_CITIES'
    MEGA_STRUCTURES = 'MEGA_STRUCTURES'
    OVERCROWDED = 'OVERCROWDED'
    HIGH_TECH = 'HIGH_TECH'
    CORRUPT = 'CORRUPT'
    BUREAUCRATIC = 'BUREAUCRATIC'
    TRADING_HUB = 'TRADING_HUB'
    INDUSTRIAL = 'INDUSTRIAL'
    BLACK_MARKET = 'BLACK_MARKET'
    RESEARCH_FACILITY = 'RESEARCH_FACILITY'
    MILITARY_BASE = 'MILITARY_BASE'
    SURVEILLANCE_OUTPOST = 'SURVEILLANCE_OUTPOST'
    EXPLORATION_OUTPOST = 'EXPLORATION_OUTPOST'
    MINERAL_DEPOSITS = 'MINERAL_DEPOSITS'
    COMMON_METAL_DEPOSITS = 'COMMON_METAL_DEPOSITS'
    PRECIOUS_METAL_DEPOSITS = 'PRECIOUS_METAL_DEPOSITS'
    RARE_METAL_DEPOSITS = 'RARE_METAL_DEPOSITS'
    METHANE_POOLS = 'METHANE_POOLS'
    ICE_CRYSTALS = 'ICE_CRYSTALS'
    EXPLOSIVE_GASES = 'EXPLOSIVE_GASES'
    STRONG_MAGNETOSPHERE = 'STRONG_MAGNETOSPHERE'
    VIBRANT_AURORAS = 'VIBRANT_AURORAS'
    SALT_FLATS = 'SALT_FLATS'
    CANYONS = 'CANYONS'
    PERPETUAL_DAYLIGHT = 'PERPETUAL_DAYLIGHT'
    PERPETUAL_OVERCAST = 'PERPETUAL_OVERCAST'
    DRY_SEABEDS = 'DRY_SEABEDS'
    MAGMA_SEAS = 'MAGMA_SEAS'
    SUPERVOLCANOES = 'SUPERVOLCANOES'
    ASH_CLOUDS = 'ASH_CLOUDS'
    VAST_RUINS = 'VAST_RUINS'
    MUTATED_FLORA = 'MUTATED_FLORA'
    TERRAFORMED = 'TERRAFORMED'
    EXTREME_TEMPERATURES = 'EXTREME_TEMPERATURES'
    EXTREME_PRESSURE = 'EXTREME_PRESSURE'
    DIVERSE_LIFE = 'DIVERSE_LIFE'
    SCARCE_LIFE = 'SCARCE_LIFE'
    FOSSILS = 'FOSSILS'
    WEAK_GRAVITY = 'WEAK_GRAVITY'
    STRONG_GRAVITY = 'STRONG_GRAVITY'
    CRUSHING_GRAVITY = 'CRUSHING_GRAVITY'
    TOXIC_ATMOSPHERE = 'TOXIC_ATMOSPHERE'
    CORROSIVE_ATMOSPHERE = 'CORROSIVE_ATMOSPHERE'
    BREATHABLE_ATMOSPHERE = 'BREATHABLE_ATMOSPHERE'
    JOVIAN = 'JOVIAN'
    ROCKY = 'ROCKY'
    VOLCANIC = 'VOLCANIC'
    FROZEN = 'FROZEN'
    SWAMP = 'SWAMP'
    BARREN = 'BARREN'
    TEMPERATE = 'TEMPERATE'
    JUNGLE = 'JUNGLE'
    OCEAN = 'OCEAN'
    STRIPPED = 'STRIPPED'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class WaypointTrait:
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    r"""A description of the trait."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the trait."""
    symbol: WaypointTraitSymbol = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('symbol') }})
    r"""The unique identifier of the trait."""
    

