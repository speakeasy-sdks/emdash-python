# ShipFuel

Details of the ship's fuel tanks including how much fuel was consumed during the last transit or action.


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `capacity`                                                            | *int*                                                                 | :heavy_check_mark:                                                    | The maximum amount of fuel the ship's tanks can hold.                 |
| `consumed`                                                            | [Optional[ShipFuelConsumed]](../../models/shared/shipfuelconsumed.md) | :heavy_minus_sign:                                                    | N/A                                                                   |
| `current`                                                             | *int*                                                                 | :heavy_check_mark:                                                    | The current amount of fuel in the ship's tanks.                       |