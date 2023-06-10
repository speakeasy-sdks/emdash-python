# fleet

## Overview

Fleet

### Available Operations

* [create_chart](#create_chart) - Create Chart
* [create_ship_ship_scan](#create_ship_ship_scan) - Scan Ships
* [create_ship_system_scan](#create_ship_system_scan) - Scan Systems
* [create_ship_waypoint_scan](#create_ship_waypoint_scan) - Scan Waypoints
* [create_survey](#create_survey) - Create Survey
* [dock_ship](#dock_ship) - Dock Ship
* [extract_resources](#extract_resources) - Extract Resources
* [get_my_ship](#get_my_ship) - Get Ship
* [get_my_ship_cargo](#get_my_ship_cargo) - Get Ship Cargo
* [get_my_ships](#get_my_ships) - List Ships
* [get_ship_cooldown](#get_ship_cooldown) - Get Ship Cooldown
* [get_ship_nav](#get_ship_nav) - Get Ship Nav
* [jettison](#jettison) - Jettison Cargo
* [jump_ship](#jump_ship) - Jump Ship
* [navigate_ship](#navigate_ship) - Navigate Ship
* [negotiate_contract](#negotiate_contract) - Negotiate Contract
* [orbit_ship](#orbit_ship) - Orbit Ship
* [patch_ship_nav](#patch_ship_nav) - Patch Ship Nav
* [purchase_cargo](#purchase_cargo) - Purchase Cargo
* [purchase_ship](#purchase_ship) - Purchase Ship
* [refuel_ship](#refuel_ship) - Refuel Ship
* [sell_cargo](#sell_cargo) - Sell Cargo
* [ship_refine](#ship_refine) - Ship Refine
* [transfer_cargo](#transfer_cargo) - Transfer Cargo
* [warp_ship](#warp_ship) - Warp Ship

## create_chart

Command a ship to chart the current waypoint.

Waypoints in the universe are uncharted by default. These locations will not show up in the API until they have been charted by a ship.

Charting a location will record your agent as the one who created the chart.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()

req = operations.CreateChartRequest(
    ship_symbol='molestiae',
)

res = s.fleet.create_chart(req, operations.CreateChartSecurity(
    agent_token="",
))

if res.create_chart_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.CreateChartRequest](../../models/operations/createchartrequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.CreateChartSecurity](../../models/operations/createchartsecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.CreateChartResponse](../../models/operations/createchartresponse.md)**


## create_ship_ship_scan

Activate your ship's sensor arrays to scan for ship information.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()

req = operations.CreateShipShipScanRequest(
    ship_symbol='minus',
)

res = s.fleet.create_ship_ship_scan(req, operations.CreateShipShipScanSecurity(
    agent_token="",
))

if res.create_ship_ship_scan_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateShipShipScanRequest](../../models/operations/createshipshipscanrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.CreateShipShipScanSecurity](../../models/operations/createshipshipscansecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.CreateShipShipScanResponse](../../models/operations/createshipshipscanresponse.md)**


## create_ship_system_scan

Activate your ship's sensor arrays to scan for system information.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()

req = operations.CreateShipSystemScanRequest(
    ship_symbol='placeat',
)

res = s.fleet.create_ship_system_scan(req, operations.CreateShipSystemScanSecurity(
    agent_token="",
))

if res.create_ship_system_scan_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateShipSystemScanRequest](../../models/operations/createshipsystemscanrequest.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.CreateShipSystemScanSecurity](../../models/operations/createshipsystemscansecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |


### Response

**[operations.CreateShipSystemScanResponse](../../models/operations/createshipsystemscanresponse.md)**


## create_ship_waypoint_scan

Activate your ship's sensor arrays to scan for waypoint information.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()

req = operations.CreateShipWaypointScanRequest(
    ship_symbol='voluptatum',
)

res = s.fleet.create_ship_waypoint_scan(req, operations.CreateShipWaypointScanSecurity(
    agent_token="",
))

if res.create_ship_waypoint_scan_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateShipWaypointScanRequest](../../models/operations/createshipwaypointscanrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.CreateShipWaypointScanSecurity](../../models/operations/createshipwaypointscansecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.CreateShipWaypointScanResponse](../../models/operations/createshipwaypointscanresponse.md)**


## create_survey

If you want to target specific yields for an extraction, you can survey a waypoint, such as an asteroid field, and send the survey in the body of the extract request. Each survey may have multiple deposits, and if a symbol shows up more than once, that indicates a higher chance of extracting that resource.

Your ship will enter a cooldown between consecutive survey requests. Surveys will eventually expire after a period of time. Multiple ships can use the same survey for extraction.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()

req = operations.CreateSurveyRequest(
    ship_symbol='iusto',
)

res = s.fleet.create_survey(req, operations.CreateSurveySecurity(
    agent_token="",
))

if res.create_survey_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CreateSurveyRequest](../../models/operations/createsurveyrequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.CreateSurveySecurity](../../models/operations/createsurveysecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.CreateSurveyResponse](../../models/operations/createsurveyresponse.md)**


## dock_ship

Attempt to dock your ship at it's current location. Docking will only succeed if the waypoint is a dockable location, and your ship is capable of docking at the time of the request.

The endpoint is idempotent - successive calls will succeed even if the ship is already docked.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()

req = operations.DockShipRequest(
    ship_symbol='excepturi',
)

res = s.fleet.dock_ship(req, operations.DockShipSecurity(
    agent_token="",
))

if res.dock_ship_200_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.DockShipRequest](../../models/operations/dockshiprequest.md)   | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `security`                                                                 | [operations.DockShipSecurity](../../models/operations/dockshipsecurity.md) | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |


### Response

**[operations.DockShipResponse](../../models/operations/dockshipresponse.md)**


## extract_resources

Extract resources from the waypoint into your ship. Send an optional survey as the payload to target specific yields.

### Example Usage

```python
import spacetraders
import dateutil.parser
from spacetraders.models import operations, shared

s = spacetraders.SpaceTraders()

req = operations.ExtractResourcesRequest(
    request_body=operations.ExtractResourcesRequestBody(
        survey=shared.Survey(
            deposits=[
                shared.SurveyDeposit(
                    symbol='recusandae',
                ),
                shared.SurveyDeposit(
                    symbol='temporibus',
                ),
            ],
            expiration=dateutil.parser.isoparse('2022-08-30T20:24:33.984Z'),
            signature='veritatis',
            size=shared.SurveySize.MODERATE,
            symbol='perferendis',
        ),
    ),
    ship_symbol='ipsam',
)

res = s.fleet.extract_resources(req, operations.ExtractResourcesSecurity(
    agent_token="",
))

if res.extract_resources_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ExtractResourcesRequest](../../models/operations/extractresourcesrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.ExtractResourcesSecurity](../../models/operations/extractresourcessecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.ExtractResourcesResponse](../../models/operations/extractresourcesresponse.md)**


## get_my_ship

Retrieve the details of your ship.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()

req = operations.GetMyShipRequest(
    ship_symbol='repellendus',
)

res = s.fleet.get_my_ship(req, operations.GetMyShipSecurity(
    agent_token="",
))

if res.get_my_ship_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetMyShipRequest](../../models/operations/getmyshiprequest.md)   | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `security`                                                                   | [operations.GetMyShipSecurity](../../models/operations/getmyshipsecurity.md) | :heavy_check_mark:                                                           | The security requirements to use for the request.                            |


### Response

**[operations.GetMyShipResponse](../../models/operations/getmyshipresponse.md)**


## get_my_ship_cargo

Retrieve the cargo of your ship.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()

req = operations.GetMyShipCargoRequest(
    ship_symbol='sapiente',
)

res = s.fleet.get_my_ship_cargo(req, operations.GetMyShipCargoSecurity(
    agent_token="",
))

if res.get_my_ship_cargo_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetMyShipCargoRequest](../../models/operations/getmyshipcargorequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.GetMyShipCargoSecurity](../../models/operations/getmyshipcargosecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.GetMyShipCargoResponse](../../models/operations/getmyshipcargoresponse.md)**


## get_my_ships

Retrieve all of your ships.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()

req = operations.GetMyShipsRequest(
    limit=778157,
    page=140350,
)

res = s.fleet.get_my_ships(req, operations.GetMyShipsSecurity(
    agent_token="",
))

if res.get_my_ships_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetMyShipsRequest](../../models/operations/getmyshipsrequest.md)   | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.GetMyShipsSecurity](../../models/operations/getmyshipssecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.GetMyShipsResponse](../../models/operations/getmyshipsresponse.md)**


## get_ship_cooldown

Retrieve the details of your ship's reactor cooldown. Some actions such as activating your jump drive, scanning, or extracting resources taxes your reactor and results in a cooldown.

Your ship cannot perform additional actions until your cooldown has expired. The duration of your cooldown is relative to the power consumption of the related modules or mounts for the action taken.

Response returns a 204 status code (no-content) when the ship has no cooldown.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()

req = operations.GetShipCooldownRequest(
    ship_symbol='at',
)

res = s.fleet.get_ship_cooldown(req, operations.GetShipCooldownSecurity(
    agent_token="",
))

if res.get_ship_cooldown_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetShipCooldownRequest](../../models/operations/getshipcooldownrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.GetShipCooldownSecurity](../../models/operations/getshipcooldownsecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.GetShipCooldownResponse](../../models/operations/getshipcooldownresponse.md)**


## get_ship_nav

Get the current nav status of a ship.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()

req = operations.GetShipNavRequest(
    ship_symbol='at',
)

res = s.fleet.get_ship_nav(req, operations.GetShipNavSecurity(
    agent_token="",
))

if res.get_ship_nav_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetShipNavRequest](../../models/operations/getshipnavrequest.md)   | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.GetShipNavSecurity](../../models/operations/getshipnavsecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.GetShipNavResponse](../../models/operations/getshipnavresponse.md)**


## jettison

Jettison cargo from your ship's cargo hold.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()

req = operations.JettisonRequest(
    request_body=operations.JettisonRequestBody(
        symbol='maiores',
        units=473608,
    ),
    ship_symbol='quod',
)

res = s.fleet.jettison(req, operations.JettisonSecurity(
    agent_token="",
))

if res.jettison_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.JettisonRequest](../../models/operations/jettisonrequest.md)   | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `security`                                                                 | [operations.JettisonSecurity](../../models/operations/jettisonsecurity.md) | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |


### Response

**[operations.JettisonResponse](../../models/operations/jettisonresponse.md)**


## jump_ship

Jump your ship instantly to a target system. When used while in orbit or docked to a jump gate waypoint, any ship can use this command. When used elsewhere, jumping requires a jump drive unit and consumes a unit of antimatter (which needs to be in your cargo).

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()

req = operations.JumpShipRequest(
    request_body=operations.JumpShipRequestBody(
        system_symbol='quod',
    ),
    ship_symbol='esse',
)

res = s.fleet.jump_ship(req, operations.JumpShipSecurity(
    agent_token="",
))

if res.jump_ship_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.JumpShipRequest](../../models/operations/jumpshiprequest.md)   | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `security`                                                                 | [operations.JumpShipSecurity](../../models/operations/jumpshipsecurity.md) | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |


### Response

**[operations.JumpShipResponse](../../models/operations/jumpshipresponse.md)**


## navigate_ship

Navigate to a target destination. The destination must be located within the same system as the ship. Navigating will consume the necessary fuel and supplies from the ship's manifest, and will pay out crew wages from the agent's account.

The returned response will detail the route information including the expected time of arrival. Most ship actions are unavailable until the ship has arrived at it's destination.

To travel between systems, see the ship's warp or jump actions.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()

req = operations.NavigateShipRequest(
    request_body=operations.NavigateShipRequestBody(
        waypoint_symbol='totam',
    ),
    ship_symbol='porro',
)

res = s.fleet.navigate_ship(req, operations.NavigateShipSecurity(
    agent_token="",
))

if res.navigate_ship_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.NavigateShipRequest](../../models/operations/navigateshiprequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.NavigateShipSecurity](../../models/operations/navigateshipsecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.NavigateShipResponse](../../models/operations/navigateshipresponse.md)**


## negotiate_contract

Negotiate Contract

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()

req = operations.NegotiateContractRequest(
    request_body='dolorum',
    ship_symbol='dicta',
)

res = s.fleet.negotiate_contract(req, operations.NegotiateContractSecurity(
    agent_token="",
))

if res.negotiate_contract_200_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.NegotiateContractRequest](../../models/operations/negotiatecontractrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.NegotiateContractSecurity](../../models/operations/negotiatecontractsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.NegotiateContractResponse](../../models/operations/negotiatecontractresponse.md)**


## orbit_ship

Attempt to move your ship into orbit at it's current location. The request will only succeed if your ship is capable of moving into orbit at the time of the request.

The endpoint is idempotent - successive calls will succeed even if the ship is already in orbit.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()

req = operations.OrbitShipRequest(
    ship_symbol='nam',
)

res = s.fleet.orbit_ship(req, operations.OrbitShipSecurity(
    agent_token="",
))

if res.orbit_ship_200_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.OrbitShipRequest](../../models/operations/orbitshiprequest.md)   | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `security`                                                                   | [operations.OrbitShipSecurity](../../models/operations/orbitshipsecurity.md) | :heavy_check_mark:                                                           | The security requirements to use for the request.                            |


### Response

**[operations.OrbitShipResponse](../../models/operations/orbitshipresponse.md)**


## patch_ship_nav

Update the nav data of a ship, such as the flight mode.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations, shared

s = spacetraders.SpaceTraders()

req = operations.PatchShipNavRequest(
    request_body=operations.PatchShipNavRequestBody(
        flight_mode=shared.ShipNavFlightMode.CRUISE,
    ),
    ship_symbol='occaecati',
)

res = s.fleet.patch_ship_nav(req, operations.PatchShipNavSecurity(
    agent_token="",
))

if res.patch_ship_nav_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.PatchShipNavRequest](../../models/operations/patchshipnavrequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.PatchShipNavSecurity](../../models/operations/patchshipnavsecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.PatchShipNavResponse](../../models/operations/patchshipnavresponse.md)**


## purchase_cargo

Purchase cargo.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()

req = operations.PurchaseCargoRequest(
    request_body=operations.PurchaseCargoPurchaseCargoRequest(
        symbol='fugit',
        units=537373,
    ),
    ship_symbol='hic',
)

res = s.fleet.purchase_cargo(req, operations.PurchaseCargoSecurity(
    agent_token="",
))

if res.purchase_cargo_201_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PurchaseCargoRequest](../../models/operations/purchasecargorequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.PurchaseCargoSecurity](../../models/operations/purchasecargosecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.PurchaseCargoResponse](../../models/operations/purchasecargoresponse.md)**


## purchase_ship

Purchase a ship

### Example Usage

```python
import spacetraders
from spacetraders.models import operations, shared

s = spacetraders.SpaceTraders()

req = operations.PurchaseShipRequestBody(
    ship_type=shared.ShipType.SHIP_LIGHT_SHUTTLE,
    waypoint_symbol='totam',
)

res = s.fleet.purchase_ship(req, operations.PurchaseShipSecurity(
    agent_token="",
))

if res.purchase_ship_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PurchaseShipRequestBody](../../models/operations/purchaseshiprequestbody.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.PurchaseShipSecurity](../../models/operations/purchaseshipsecurity.md)       | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.PurchaseShipResponse](../../models/operations/purchaseshipresponse.md)**


## refuel_ship

Refuel your ship from the local market.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()

req = operations.RefuelShipRequest(
    ship_symbol='beatae',
)

res = s.fleet.refuel_ship(req, operations.RefuelShipSecurity(
    agent_token="",
))

if res.refuel_ship_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.RefuelShipRequest](../../models/operations/refuelshiprequest.md)   | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.RefuelShipSecurity](../../models/operations/refuelshipsecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.RefuelShipResponse](../../models/operations/refuelshipresponse.md)**


## sell_cargo

Sell cargo.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()

req = operations.SellCargoRequest(
    request_body=operations.SellCargoSellCargoRequest(
        symbol='commodi',
        units=473600,
    ),
    ship_symbol='modi',
)

res = s.fleet.sell_cargo(req, operations.SellCargoSecurity(
    agent_token="",
))

if res.sell_cargo_201_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.SellCargoRequest](../../models/operations/sellcargorequest.md)   | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `security`                                                                   | [operations.SellCargoSecurity](../../models/operations/sellcargosecurity.md) | :heavy_check_mark:                                                           | The security requirements to use for the request.                            |


### Response

**[operations.SellCargoResponse](../../models/operations/sellcargoresponse.md)**


## ship_refine

Attempt to refine the raw materials on your ship. The request will only succeed if your ship is capable of refining at the time of the request.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()

req = operations.ShipRefineRequest(
    request_body=operations.ShipRefineRequestBody(
        produce=operations.ShipRefineRequestBodyProduce.COPPER,
    ),
    ship_symbol='impedit',
)

res = s.fleet.ship_refine(req, operations.ShipRefineSecurity(
    agent_token="",
))

if res.ship_refine_200_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.ShipRefineRequest](../../models/operations/shiprefinerequest.md)   | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.ShipRefineSecurity](../../models/operations/shiprefinesecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.ShipRefineResponse](../../models/operations/shiprefineresponse.md)**


## transfer_cargo

Transfer cargo between ships.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()

req = operations.TransferCargoRequest(
    request_body=operations.TransferCargoTransferCargoRequest(
        ship_symbol='cum',
        trade_symbol='esse',
        units=216550,
    ),
    ship_symbol='excepturi',
)

res = s.fleet.transfer_cargo(req, operations.TransferCargoSecurity(
    agent_token="",
))

if res.transfer_cargo_200_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.TransferCargoRequest](../../models/operations/transfercargorequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.TransferCargoSecurity](../../models/operations/transfercargosecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.TransferCargoResponse](../../models/operations/transfercargoresponse.md)**


## warp_ship

Warp your ship to a target destination in another system. Warping will consume the necessary fuel and supplies from the ship's manifest, and will pay out crew wages from the agent's account.

The returned response will detail the route information including the expected time of arrival. Most ship actions are unavailable until the ship has arrived at it's destination.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()

req = operations.WarpShipRequest(
    request_body=operations.WarpShipRequestBody(
        waypoint_symbol='aspernatur',
    ),
    ship_symbol='perferendis',
)

res = s.fleet.warp_ship(req, operations.WarpShipSecurity(
    agent_token="",
))

if res.warp_ship_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.WarpShipRequest](../../models/operations/warpshiprequest.md)   | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `security`                                                                 | [operations.WarpShipSecurity](../../models/operations/warpshipsecurity.md) | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |


### Response

**[operations.WarpShipResponse](../../models/operations/warpshipresponse.md)**

