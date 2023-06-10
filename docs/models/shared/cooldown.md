# Cooldown

A cooldown is a period of time in which a ship cannot perform certain actions.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `expiration`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The date and time when the cooldown expires in ISO 8601 format       |
| `remaining_seconds`                                                  | *int*                                                                | :heavy_check_mark:                                                   | The remaining duration of the cooldown in seconds                    |
| `ship_symbol`                                                        | *str*                                                                | :heavy_check_mark:                                                   | The symbol of the ship that is on cooldown                           |
| `total_seconds`                                                      | *int*                                                                | :heavy_check_mark:                                                   | The total duration of the cooldown in seconds                        |