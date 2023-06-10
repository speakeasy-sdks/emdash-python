# ShipRegistration

The public registration information of the ship


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `faction_symbol`                                      | *str*                                                 | :heavy_check_mark:                                    | The symbol of the faction the ship is registered with |
| `name`                                                | *str*                                                 | :heavy_check_mark:                                    | The agent's registered name of the ship               |
| `role`                                                | [ShipRole](../../models/shared/shiprole.md)           | :heavy_check_mark:                                    | The registered role of the ship                       |