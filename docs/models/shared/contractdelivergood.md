# ContractDeliverGood

The details of a delivery contract. Includes the type of good, units needed, and the destination.


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `destination_symbol`                                            | *str*                                                           | :heavy_check_mark:                                              | The destination where goods need to be delivered.               |
| `trade_symbol`                                                  | *str*                                                           | :heavy_check_mark:                                              | The symbol of the trade good to deliver.                        |
| `units_fulfilled`                                               | *int*                                                           | :heavy_check_mark:                                              | The number of units fulfilled on this contract.                 |
| `units_required`                                                | *int*                                                           | :heavy_check_mark:                                              | The number of units that need to be delivered on this contract. |