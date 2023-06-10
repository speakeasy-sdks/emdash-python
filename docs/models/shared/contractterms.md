# ContractTerms


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `deadline`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects)    | :heavy_check_mark:                                                      | The deadline for the contract.                                          |
| `deliver`                                                               | list[[ContractDeliverGood](../../models/shared/contractdelivergood.md)] | :heavy_minus_sign:                                                      | N/A                                                                     |
| `payment`                                                               | [ContractPayment](../../models/shared/contractpayment.md)               | :heavy_check_mark:                                                      | N/A                                                                     |