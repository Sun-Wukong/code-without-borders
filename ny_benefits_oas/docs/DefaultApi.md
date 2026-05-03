# openapi_client.DefaultApi

All URIs are relative to *https://screeningapi.cityofnewyork.us*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate**](DefaultApi.md#authenticate) | **POST** /authToken | 
[**confirm_password**](DefaultApi.md#confirm_password) | **POST** /confirmPassword | 
[**forgot_password**](DefaultApi.md#forgot_password) | **POST** /forgotPassword | 
[**get_bulk_eligibility_programs**](DefaultApi.md#get_bulk_eligibility_programs) | **POST** /bulkSubmission/import | 
[**get_eligible_programs**](DefaultApi.md#get_eligible_programs) | **POST** /eligibilityPrograms | 


# **authenticate**
> Token authenticate(credentials=credentials)

### Example


```python
import openapi_client
from openapi_client.models.credentials import Credentials
from openapi_client.models.token import Token
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://screeningapi.cityofnewyork.us
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://screeningapi.cityofnewyork.us"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    credentials = openapi_client.Credentials() # Credentials | The retrieved token can be provided in the request header of the Screening endpoints to make an authenticated request. (optional)

    try:
        api_response = api_instance.authenticate(credentials=credentials)
        print("The response of DefaultApi->authenticate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->authenticate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials** | [**Credentials**](Credentials.md)| The retrieved token can be provided in the request header of the Screening endpoints to make an authenticated request. | [optional] 

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | OK |  -  |
**405** | OK |  -  |
**406** | OK |  -  |
**500** | Internal Server Error |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_password**
> ForgotPassword200Response confirm_password(confirm_password_request=confirm_password_request)

### Example


```python
import openapi_client
from openapi_client.models.confirm_password_request import ConfirmPasswordRequest
from openapi_client.models.forgot_password200_response import ForgotPassword200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://screeningapi.cityofnewyork.us
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://screeningapi.cityofnewyork.us"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    confirm_password_request = openapi_client.ConfirmPasswordRequest() # ConfirmPasswordRequest | Payload to confirm password change (optional)

    try:
        api_response = api_instance.confirm_password(confirm_password_request=confirm_password_request)
        print("The response of DefaultApi->confirm_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->confirm_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **confirm_password_request** | [**ConfirmPasswordRequest**](ConfirmPasswordRequest.md)| Payload to confirm password change | [optional] 

### Return type

[**ForgotPassword200Response**](ForgotPassword200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success Response |  -  |
**400** | Bad Request |  -  |
**404** | OK |  -  |
**405** | OK |  -  |
**406** | OK |  -  |
**500** | Internal Server Error |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forgot_password**
> ForgotPassword200Response forgot_password(forgot_password_request=forgot_password_request)

### Example


```python
import openapi_client
from openapi_client.models.forgot_password200_response import ForgotPassword200Response
from openapi_client.models.forgot_password_request import ForgotPasswordRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://screeningapi.cityofnewyork.us
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://screeningapi.cityofnewyork.us"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    forgot_password_request = openapi_client.ForgotPasswordRequest() # ForgotPasswordRequest | Payload for a password reset request (optional)

    try:
        api_response = api_instance.forgot_password(forgot_password_request=forgot_password_request)
        print("The response of DefaultApi->forgot_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->forgot_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forgot_password_request** | [**ForgotPasswordRequest**](ForgotPasswordRequest.md)| Payload for a password reset request | [optional] 

### Return type

[**ForgotPassword200Response**](ForgotPassword200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success Response |  -  |
**400** | Bad Request |  -  |
**404** | OK |  -  |
**405** | OK |  -  |
**406** | OK |  -  |
**500** | Internal Server Error |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bulk_eligibility_programs**
> GetEligiblePrograms200Response get_bulk_eligibility_programs(body, interested_programs=interested_programs)

### Example

* Api Key Authentication (ApiKey):

```python
import openapi_client
from openapi_client.models.get_eligible_programs200_response import GetEligiblePrograms200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://screeningapi.cityofnewyork.us
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://screeningapi.cityofnewyork.us"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    body = 'body_example' # str | Request payload for bulk import
    interested_programs = 'interested_programs_example' # str | Pipe-separated list of program codes a user is interested in. If specified, the Screening API will only return programs included in this list. Program codes should always be passed in upper case. (optional)

    try:
        api_response = api_instance.get_bulk_eligibility_programs(body, interested_programs=interested_programs)
        print("The response of DefaultApi->get_bulk_eligibility_programs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_bulk_eligibility_programs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| Request payload for bulk import | 
 **interested_programs** | **str**| Pipe-separated list of program codes a user is interested in. If specified, the Screening API will only return programs included in this list. Program codes should always be passed in upper case. | [optional] 

### Return type

[**GetEligiblePrograms200Response**](GetEligiblePrograms200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: text/csv
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | OK |  -  |
**405** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_eligible_programs**
> GetEligiblePrograms200Response get_eligible_programs(submission, interested_programs=interested_programs)

### Example

* Api Key Authentication (ApiKey):

```python
import openapi_client
from openapi_client.models.get_eligible_programs200_response import GetEligiblePrograms200Response
from openapi_client.models.submission import Submission
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://screeningapi.cityofnewyork.us
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://screeningapi.cityofnewyork.us"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    submission = openapi_client.Submission() # Submission | Request payload for individual form submission
    interested_programs = 'interested_programs_example' # str | Pipe-separated list of program codes a user is interested in. If specified, the Screening API will only return programs included in this list. Program codes should always be passed in upper case. (optional)

    try:
        api_response = api_instance.get_eligible_programs(submission, interested_programs=interested_programs)
        print("The response of DefaultApi->get_eligible_programs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_eligible_programs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission** | [**Submission**](Submission.md)| Request payload for individual form submission | 
 **interested_programs** | **str**| Pipe-separated list of program codes a user is interested in. If specified, the Screening API will only return programs included in this list. Program codes should always be passed in upper case. | [optional] 

### Return type

[**GetEligiblePrograms200Response**](GetEligiblePrograms200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | OK |  -  |
**405** | OK |  -  |
**406** | OK |  -  |
**500** | Internal Server Error |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

