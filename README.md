# SpaceTraders

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/emdash-python.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import spacetraders


s = spacetraders.SpaceTraders(
    security=shared.Security(
        agent_token="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.get_status()

if res.get_status_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations

### [SpaceTraders SDK](docs/spacetraders/README.md)

* [get_status](docs/spacetraders/README.md#get_status) - Get Status
* [register](docs/spacetraders/README.md#register) - Register New Agent

### [agents](docs/agents/README.md)

* [get_my_agent](docs/agents/README.md#get_my_agent) - My Agent Details

### [contracts](docs/contracts/README.md)

* [accept_contract](docs/contracts/README.md#accept_contract) - Accept Contract
* [deliver_contract](docs/contracts/README.md#deliver_contract) - Deliver Contract
* [fulfill_contract](docs/contracts/README.md#fulfill_contract) - Fulfill Contract
* [get_contract](docs/contracts/README.md#get_contract) - Get Contract
* [get_contracts](docs/contracts/README.md#get_contracts) - List Contracts

### [factions](docs/factions/README.md)

* [get_faction](docs/factions/README.md#get_faction) - Get Faction
* [get_factions](docs/factions/README.md#get_factions) - List Factions

### [fleet](docs/fleet/README.md)

* [create_chart](docs/fleet/README.md#create_chart) - Create Chart
* [create_ship_ship_scan](docs/fleet/README.md#create_ship_ship_scan) - Scan Ships
* [create_ship_system_scan](docs/fleet/README.md#create_ship_system_scan) - Scan Systems
* [create_ship_waypoint_scan](docs/fleet/README.md#create_ship_waypoint_scan) - Scan Waypoints
* [create_survey](docs/fleet/README.md#create_survey) - Create Survey
* [dock_ship](docs/fleet/README.md#dock_ship) - Dock Ship
* [extract_resources](docs/fleet/README.md#extract_resources) - Extract Resources
* [get_my_ship](docs/fleet/README.md#get_my_ship) - Get Ship
* [get_my_ship_cargo](docs/fleet/README.md#get_my_ship_cargo) - Get Ship Cargo
* [get_my_ships](docs/fleet/README.md#get_my_ships) - List Ships
* [get_ship_cooldown](docs/fleet/README.md#get_ship_cooldown) - Get Ship Cooldown
* [get_ship_nav](docs/fleet/README.md#get_ship_nav) - Get Ship Nav
* [jettison](docs/fleet/README.md#jettison) - Jettison Cargo
* [jump_ship](docs/fleet/README.md#jump_ship) - Jump Ship
* [navigate_ship](docs/fleet/README.md#navigate_ship) - Navigate Ship
* [negotiate_contract](docs/fleet/README.md#negotiate_contract) - Negotiate Contract
* [orbit_ship](docs/fleet/README.md#orbit_ship) - Orbit Ship
* [patch_ship_nav](docs/fleet/README.md#patch_ship_nav) - Patch Ship Nav
* [purchase_cargo](docs/fleet/README.md#purchase_cargo) - Purchase Cargo
* [purchase_ship](docs/fleet/README.md#purchase_ship) - Purchase Ship
* [refuel_ship](docs/fleet/README.md#refuel_ship) - Refuel Ship
* [sell_cargo](docs/fleet/README.md#sell_cargo) - Sell Cargo
* [ship_refine](docs/fleet/README.md#ship_refine) - Ship Refine
* [transfer_cargo](docs/fleet/README.md#transfer_cargo) - Transfer Cargo
* [warp_ship](docs/fleet/README.md#warp_ship) - Warp Ship

### [systems](docs/systems/README.md)

* [get_jump_gate](docs/systems/README.md#get_jump_gate) - Get Jump Gate
* [get_market](docs/systems/README.md#get_market) - Get Market
* [get_shipyard](docs/systems/README.md#get_shipyard) - Get Shipyard
* [get_system](docs/systems/README.md#get_system) - Get System
* [get_system_waypoints](docs/systems/README.md#get_system_waypoints) - List Waypoints
* [get_systems](docs/systems/README.md#get_systems) - List Systems
* [get_waypoint](docs/systems/README.md#get_waypoint) - Get Waypoint
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
