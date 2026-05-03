# Authenticate405Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**errors** | [**List[ErrorModel]**](ErrorModel.md) |  | [optional] 

## Example

```python
from openapi_client.models.authenticate405_response import Authenticate405Response

# TODO update the JSON string below
json = "{}"
# create an instance of Authenticate405Response from a JSON string
authenticate405_response_instance = Authenticate405Response.from_json(json)
# print the JSON string representation of the object
print(Authenticate405Response.to_json())

# convert the object into a dict
authenticate405_response_dict = authenticate405_response_instance.to_dict()
# create an instance of Authenticate405Response from a dict
authenticate405_response_from_dict = Authenticate405Response.from_dict(authenticate405_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


