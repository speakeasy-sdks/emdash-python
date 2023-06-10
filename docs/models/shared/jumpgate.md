# JumpGate


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `connected_systems`                                                  | list[[ConnectedSystem](../../models/shared/connectedsystem.md)]      | :heavy_check_mark:                                                   | The systems within range of the gate that have a corresponding gate. |
| `faction_symbol`                                                     | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The symbol of the faction that owns the gate.                        |
| `jump_range`                                                         | *float*                                                              | :heavy_check_mark:                                                   | The maximum jump range of the gate.                                  |