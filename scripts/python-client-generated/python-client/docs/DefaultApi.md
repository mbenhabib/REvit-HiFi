# swagger_client.DefaultApi

All URIs are relative to *https://api.uber.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**modeldata_get**](DefaultApi.md#modeldata_get) | **GET** /modeldata | 
[**writemodel_post**](DefaultApi.md#writemodel_post) | **POST** /writemodel | 


# **modeldata_get**
> list[ModelData] modeldata_get()



An array of model data

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try: 
    api_response = api_instance.modeldata_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->modeldata_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ModelData]**](ModelData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **writemodel_post**
> ModelDelta writemodel_post(model_delta=model_delta)



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
model_delta = swagger_client.ModelDelta() # ModelDelta | Position transform delta of the model. (optional)

try: 
    api_response = api_instance.writemodel_post(model_delta=model_delta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->writemodel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_delta** | [**ModelDelta**](ModelDelta.md)| Position transform delta of the model. | [optional] 

### Return type

[**ModelDelta**](ModelDelta.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

