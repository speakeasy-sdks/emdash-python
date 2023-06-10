# ShipMount

A mount is installed on the exterier of a ship.


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `deposits`                                                          | list[[ShipMountDeposits](../../models/shared/shipmountdeposits.md)] | :heavy_minus_sign:                                                  | N/A                                                                 |
| `description`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `requirements`                                                      | [ShipRequirements](../../models/shared/shiprequirements.md)         | :heavy_check_mark:                                                  | The requirements for installation on a ship                         |
| `strength`                                                          | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `symbol`                                                            | [ShipMountSymbol](../../models/shared/shipmountsymbol.md)           | :heavy_check_mark:                                                  | N/A                                                                 |