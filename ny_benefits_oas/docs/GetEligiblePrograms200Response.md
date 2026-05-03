# GetEligiblePrograms200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**eligibile_programs** | [**List[EligibleProgram]**](EligibleProgram.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_eligible_programs200_response import GetEligiblePrograms200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEligiblePrograms200Response from a JSON string
get_eligible_programs200_response_instance = GetEligiblePrograms200Response.from_json(json)
# print the JSON string representation of the object
print(GetEligiblePrograms200Response.to_json())

# convert the object into a dict
get_eligible_programs200_response_dict = get_eligible_programs200_response_instance.to_dict()
# create an instance of GetEligiblePrograms200Response from a dict
get_eligible_programs200_response_from_dict = GetEligiblePrograms200Response.from_dict(get_eligible_programs200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


