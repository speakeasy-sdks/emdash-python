# ShipCargo


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `capacity`                                                    | *int*                                                         | :heavy_check_mark:                                            | The max number of items that can be stored in the cargo hold. |
| `inventory`                                                   | list[[ShipCargoItem](../../models/shared/shipcargoitem.md)]   | :heavy_check_mark:                                            | The items currently in the cargo hold.                        |
| `units`                                                       | *int*                                                         | :heavy_check_mark:                                            | The number of items currently stored in the cargo hold.       |