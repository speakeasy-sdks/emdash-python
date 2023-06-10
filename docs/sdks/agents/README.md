# agents

## Overview

Agents

### Available Operations

* [get_my_agent](#get_my_agent) - My Agent Details

## get_my_agent

Fetch your agent's details.

### Example Usage

```python
import spacetraders
from spacetraders.models import operations

s = spacetraders.SpaceTraders()


res = s.agents.get_my_agent(operations.GetMyAgentSecurity(
    agent_token="",
))

if res.get_my_agent_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `security`                                                                     | [operations.GetMyAgentSecurity](../../models/operations/getmyagentsecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.GetMyAgentResponse](../../models/operations/getmyagentresponse.md)**

