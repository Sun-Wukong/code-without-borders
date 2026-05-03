# Person


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age** | **int** | The age of the person. | [optional] 
**student** | **bool** | Whether the person is a student or not. | [optional] 
**student_fulltime** | **bool** | Whether the person is a full-time student or not. | [optional] 
**pregnant** | **bool** | Whether the person is pregnant or not. | [optional] 
**unemployed** | **bool** | Whether the person is employed or not. | [optional] 
**unemployed_worked_last18_months** | **bool** | Whether the person is unemployed and worked within the last 18 months. | [optional] 
**blind** | **bool** | Whether the person is blind or not. | [optional] 
**disabled** | **bool** | Whether the person has disabilities or not. | [optional] 
**veteran** | **bool** | Whether the person is a veteran or not | [optional] 
**benefits_medicaid** | **bool** | Whether the person receives Medicaid benefits or not. | [optional] 
**benefits_medicaid_disability** | **bool** | Whether the person receives disability-related Medicaid benefits or not | [optional] 
**household_member_type** | **str** | What is this person&#39;s relation to the household? | [optional] [default to '']
**living_owner_on_deed** | **bool** | If the household owns the home is the person the owner or on the deed. | [optional] 
**living_rental_on_lease** | **bool** | If the household rental is renting, whether the person on the lease or not. | [optional] 
**incomes** | [**List[Income]**](Income.md) | A collection of one or more income objects. | [optional] 
**expenses** | [**List[Expense]**](Expense.md) | Collection of one or more expense objects | [optional] 

## Example

```python
from openapi_client.models.person import Person

# TODO update the JSON string below
json = "{}"
# create an instance of Person from a JSON string
person_instance = Person.from_json(json)
# print the JSON string representation of the object
print(Person.to_json())

# convert the object into a dict
person_dict = person_instance.to_dict()
# create an instance of Person from a dict
person_from_dict = Person.from_dict(person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


