# SpaceTraders SDK

## Overview

SpaceTraders is an open-universe game and learning platform that offers a set of HTTP endpoints to control a fleet of ships and explore a multiplayer universe.

The API is documented using [OpenAPI](https://github.com/SpaceTradersAPI/api-docs). You can send your first request right here in your browser to check the status of the game server.

```json http
{
  "method": "GET",
  "url": "https://api.spacetraders.io/v2",
}
```

Unlike a traditional game, SpaceTraders does not have a first-party client or app to play the game. Instead, you can use the API to build your own client, write a script to automate your ships, or try an app built by the community.

We have a [Discord channel](https://discord.com/invite/jh6zurdWk5) where you can share your projects, ask questions, and get help from other players.




### Available Operations

* [get_status](#get_status) - Get Status
* [register](#register) - Register New Agent

## get_status

Return the status of the game server.

### Example Usage

```python
import spacetraders


s = spacetraders.SpaceTraders(
    security=shared.Security(
        agent_token="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.space_traders.get_status()

if res.get_status_200_application_json_object is not None:
    # handle response
```

## register

Creates a new agent and ties it to a temporary Account.

The agent symbol is a 3-14 character string that will represent your agent. This symbol will prefix the symbol of every ship you own. Agent symbols will be cast to all uppercase characters.

A new agent will be granted an authorization token, a contract with their starting faction, a command ship with a jump drive, and one hundred thousand credits.

> #### Keep your token safe and secure
>
> Save your token during the alpha phase. There is no way to regenerate this token without starting a new agent. In the future you will be able to generate and manage your tokens from the SpaceTraders website.

You can accept your contract using the `/my/contracts/{contractId}/accept` endpoint. You will want to navigate your command ship to a nearby asteroid field and execute the `/my/ships/{shipSymbol}/extract` endpoint to mine various types of ores and minerals.

Return to the contract destination and execute the `/my/ships/{shipSymbol}/deliver` endpoint to deposit goods into the contract.

When your contract is fulfilled, you can call `/my/contracts/{contractId}/fulfill` to retrieve payment.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders(
    security=shared.Security(
        agent_token="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.RegisterRequestBody(
    email='Larue_Rau85@yahoo.com',
    faction=operations.RegisterRequestBodyFaction.GALACTIC,
    symbol='BADGER',
)

res = s.space_traders.register(req)

if res.register_201_application_json_object is not None:
    # handle response
```
