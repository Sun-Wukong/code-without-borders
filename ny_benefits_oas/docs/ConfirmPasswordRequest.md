# ConfirmPasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**new_password** | **str** |  | [optional] 
**verification_code** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.confirm_password_request import ConfirmPasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmPasswordRequest from a JSON string
confirm_password_request_instance = ConfirmPasswordRequest.from_json(json)
# print the JSON string representation of the object
print(ConfirmPasswordRequest.to_json())

# convert the object into a dict
confirm_password_request_dict = confirm_password_request_instance.to_dict()
# create an instance of ConfirmPasswordRequest from a dict
confirm_password_request_from_dict = ConfirmPasswordRequest.from_dict(confirm_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


