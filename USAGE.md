<!-- Start SDK Example Usage -->
```python
import spacetraders


s = spacetraders.SpaceTraders(
    security=shared.Security(
        agent_token="",
    ),
)


res = s.get_status()

if res.get_status_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->