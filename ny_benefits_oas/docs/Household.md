# Household


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cash_on_hand** | **int** | How much does your whole household has right now in; cash on hand, checking or saving accounts, stocks, bonds or mutual funds. | [optional] 
**living_renting** | **bool** | Renting the current living situation. | [optional] [default to False]
**housing_rental_type** | **str** | The type of rental, if renting. | [optional] [default to '']
**living_owner** | **bool** | A household member owns the home or apartment. | [optional] [default to False]
**living_staying_with_friend** | **bool** | Staying with a friend | [optional] [default to False]
**living_hotel** | **bool** | In a hotel. | [optional] [default to False]
**living_shelter** | **bool** | In a shelter or homeless. | [optional] [default to False]
**living_prefer_not_to_say** | **bool** | Preference to not disclose housing. | [optional] [default to False]

## Example

```python
from openapi_client.models.household import Household

# TODO update the JSON string below
json = "{}"
# create an instance of Household from a JSON string
household_instance = Household.from_json(json)
# print the JSON string representation of the object
print(Household.to_json())

# convert the object into a dict
household_dict = household_instance.to_dict()
# create an instance of Household from a dict
household_from_dict = Household.from_dict(household_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


