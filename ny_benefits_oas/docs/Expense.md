# Expense


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The dollar amount of the expense. | [optional] 
**type** | **str** | The type of the expense (see below). | [optional] 
**frequency** | **str** | How often the expense is paid | [optional] 

## Example

```python
from openapi_client.models.expense import Expense

# TODO update the JSON string below
json = "{}"
# create an instance of Expense from a JSON string
expense_instance = Expense.from_json(json)
# print the JSON string representation of the object
print(Expense.to_json())

# convert the object into a dict
expense_dict = expense_instance.to_dict()
# create an instance of Expense from a dict
expense_from_dict = Expense.from_dict(expense_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


