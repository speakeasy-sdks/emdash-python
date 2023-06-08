# contracts

## Overview

Contracts

### Available Operations

* [accept_contract](#accept_contract) - Accept Contract
* [deliver_contract](#deliver_contract) - Deliver Contract
* [fulfill_contract](#fulfill_contract) - Fulfill Contract
* [get_contract](#get_contract) - Get Contract
* [get_contracts](#get_contracts) - List Contracts

## accept_contract

Accept a contract.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()

req = operations.AcceptContractRequest(
    contract_id='illum',
)

res = s.contracts.accept_contract(req, operations.AcceptContractSecurity(
    agent_token="",
))

if res.accept_contract_200_application_json_object is not None:
    # handle response
```

## deliver_contract

Deliver cargo on a given contract.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()

req = operations.DeliverContractRequest(
    request_body=operations.DeliverContractRequestBody(
        ship_symbol='vel',
        trade_symbol='error',
        units=645894,
    ),
    contract_id='suscipit',
)

res = s.contracts.deliver_contract(req, operations.DeliverContractSecurity(
    agent_token="",
))

if res.deliver_contract_200_application_json_object is not None:
    # handle response
```

## fulfill_contract

Fulfill a contract

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()

req = operations.FulfillContractRequest(
    contract_id='iure',
)

res = s.contracts.fulfill_contract(req, operations.FulfillContractSecurity(
    agent_token="",
))

if res.fulfill_contract_200_application_json_object is not None:
    # handle response
```

## get_contract

Get the details of a contract by ID.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()

req = operations.GetContractRequest(
    contract_id='magnam',
)

res = s.contracts.get_contract(req, operations.GetContractSecurity(
    agent_token="",
))

if res.get_contract_200_application_json_object is not None:
    # handle response
```

## get_contracts

List all of your contracts.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()

req = operations.GetContractsRequest(
    limit=891773,
    page=56713,
)

res = s.contracts.get_contracts(req, operations.GetContractsSecurity(
    agent_token="",
))

if res.get_contracts_200_application_json_object is not None:
    # handle response
```
