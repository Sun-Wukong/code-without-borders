# Income


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The dollar amount of the income. | [optional] 
**type** | **str** | The type of the income | [optional] 
**frequency** | **str** | How often the income is received. | [optional] 

## Example

```python
from openapi_client.models.income import Income

# TODO update the JSON string below
json = "{}"
# create an instance of Income from a JSON string
income_instance = Income.from_json(json)
# print the JSON string representation of the object
print(Income.to_json())

# convert the object into a dict
income_dict = income_instance.to_dict()
# create an instance of Income from a dict
income_from_dict = Income.from_dict(income_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


