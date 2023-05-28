# factions

## Overview

Factions

### Available Operations

* [get_faction](#get_faction) - Get Faction
* [get_factions](#get_factions) - List Factions

## get_faction

View the details of a faction.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders(
    security=shared.Security(
        agent_token="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetFactionRequest(
    faction_symbol='delectus',
)

res = s.factions.get_faction(req)

if res.get_faction_200_application_json_object is not None:
    # handle response
```

## get_factions

List all discovered factions in the game.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders(
    security=shared.Security(
        agent_token="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetFactionsRequest(
    limit=272656,
    page=383441,
)

res = s.factions.get_factions(req)

if res.get_factions_200_application_json_object is not None:
    # handle response
```
