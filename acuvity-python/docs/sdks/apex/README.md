# Apex
(*apex*)

## Overview

Apex is the proxy and detectiono API service of Acuvity.

### Available Operations

* [list_analyzers](#list_analyzers) - List of all available analyzers.
* [create_scan](#create_scan) - Processes the scan request.

## list_analyzers

List of all available analyzers.

### Example Usage

```python
from acuvity import Acuvity

s = Acuvity()

res = s.apex.list_analyzers()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.Analyzer]](../../models/.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| models.Elementalerror | 400, 401, 500         | application/json      |
| models.APIError       | 4XX, 5XX              | \*/\*                 |

## create_scan

Processes the scan request.

### Example Usage

```python
from acuvity import Acuvity

s = Acuvity()

res = s.apex.create_scan(request={
    "bypass_hash": "Alice",
    "user": {
        "claims": [
            "@org=acuvity.ai",
            "given_name=John",
            "family_name=Doe",
        ],
        "name": "Alice",
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.Scanrequest](../../models/scanrequest.md)                   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Scanresponse](../../models/scanresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.Elementalerror   | 400, 401, 403, 422, 500 | application/json        |
| models.APIError         | 4XX, 5XX                | \*/\*                   |