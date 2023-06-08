# systems

## Overview

Systems

### Available Operations

* [get_jump_gate](#get_jump_gate) - Get Jump Gate
* [get_market](#get_market) - Get Market
* [get_shipyard](#get_shipyard) - Get Shipyard
* [get_system](#get_system) - Get System
* [get_system_waypoints](#get_system_waypoints) - List Waypoints
* [get_systems](#get_systems) - List Systems
* [get_waypoint](#get_waypoint) - Get Waypoint

## get_jump_gate

Get jump gate details for a waypoint.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders(
    security=shared.Security(
        agent_token="",
    ),
)

req = operations.GetJumpGateRequest(
    system_symbol='ad',
    waypoint_symbol='natus',
)

res = s.systems.get_jump_gate(req)

if res.get_jump_gate_200_application_json_object is not None:
    # handle response
```

## get_market

Retrieve imports, exports and exchange data from a marketplace. Imports can be sold, exports can be purchased, and exchange goods can be purchased or sold. Send a ship to the waypoint to access trade good prices and recent transactions.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders(
    security=shared.Security(
        agent_token="",
    ),
)

req = operations.GetMarketRequest(
    system_symbol='sed',
    waypoint_symbol='iste',
)

res = s.systems.get_market(req)

if res.get_market_200_application_json_object is not None:
    # handle response
```

## get_shipyard

Get the shipyard for a waypoint. Send a ship to the waypoint to access ships that are currently available for purchase and recent transactions.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders(
    security=shared.Security(
        agent_token="",
    ),
)

req = operations.GetShipyardRequest(
    system_symbol='dolor',
    waypoint_symbol='natus',
)

res = s.systems.get_shipyard(req)

if res.get_shipyard_200_application_json_object is not None:
    # handle response
```

## get_system

Get the details of a system.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders(
    security=shared.Security(
        agent_token="",
    ),
)

req = operations.GetSystemRequest(
    system_symbol='laboriosam',
)

res = s.systems.get_system(req)

if res.get_system_200_application_json_object is not None:
    # handle response
```

## get_system_waypoints

Fetch all of the waypoints for a given system. System must be charted or a ship must be present to return waypoint details.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()

req = operations.GetSystemWaypointsRequest(
    limit=943749,
    page=902599,
    system_symbol='fuga',
)

res = s.systems.get_system_waypoints(req, operations.GetSystemWaypointsSecurity(
    agent_token="",
))

if res.get_system_waypoints_200_application_json_object is not None:
    # handle response
```

## get_systems

Return a list of all systems.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders(
    security=shared.Security(
        agent_token="",
    ),
)

req = operations.GetSystemsRequest(
    limit=449950,
    page=359508,
)

res = s.systems.get_systems(req)

if res.get_systems_200_application_json_object is not None:
    # handle response
```

## get_waypoint

View the details of a waypoint.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders(
    security=shared.Security(
        agent_token="",
    ),
)

req = operations.GetWaypointRequest(
    system_symbol='iste',
    waypoint_symbol='iure',
)

res = s.systems.get_waypoint(req)

if res.get_waypoint_200_application_json_object is not None:
    # handle response
```
