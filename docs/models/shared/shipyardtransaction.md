# ShipyardTransaction


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `agent_symbol`                                                       | *str*                                                                | :heavy_check_mark:                                                   | The symbol of the agent that made the transaction.                   |
| `price`                                                              | *int*                                                                | :heavy_check_mark:                                                   | The price of the transaction.                                        |
| `ship_symbol`                                                        | *str*                                                                | :heavy_check_mark:                                                   | The symbol of the ship that was purchased.                           |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | The timestamp of the transaction.                                    |
| `waypoint_symbol`                                                    | *str*                                                                | :heavy_check_mark:                                                   | The symbol of the waypoint where the transaction took place.         |