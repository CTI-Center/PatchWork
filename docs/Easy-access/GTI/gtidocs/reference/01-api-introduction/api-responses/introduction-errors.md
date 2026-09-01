---
title: "Errors"
source: https://gtidocs.virustotal.com/reference/introduction-errors
slug: introduction-errors
section: reference
group: "API Introduction"
updatedAt: 2025-09-25T00:33:28.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API Introduction](../README.md) › [API responses](../api-responses.md) › Errors

---

# errors

The Google Threat Intelligence API follows the conventional HTTP response codes to indicate success or failure. Codes in the `2xx` range indicate success. Codes in the `4xx` range indicate an error in the request (e.g. a missing parameter, a resource was not found). Codes in the `5xx` range indicate an error in Google TI's servers and should be rare.

Unsuccessful requests return additional information about the error in JSON format.

```json An error response
{
  "error": {
    "code": "<error code>",
    "message": "<a message describing the error>"
  }
}
```
```json Example (404)
{
  "error": {
    "code": "NotFoundError",
    "message": "URL \"thisurlidmakesnosenseatall\" not found"
  }
}
```
```json Example (401)
{
  "error": {
    "code": "AuthenticationRequiredError",
    "message": "X-Apikey header is missing"
  }
}
```

The error code is a string with one of the values provided in the table below. The `message` usually provides a little more information about the error.

| HTTP Code | Error code                   | Description                                                                                                             |
| --------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| 400       | BadRequestError              | The API request is invalid or malformed. The message usually provides details about why the request is not valid.       |
| 400       | InvalidArgumentError         | Some of the provided arguments are incorrect.                                                                           |
| 400       | NotAvailableYet              | The resource is not available yet, but will become available later.                                                     |
| 400       | UnselectiveContentQueryError | Content search query is not selective enough.                                                                           |
| 400       | UnsupportedContentQueryError | Unsupported content search query.                                                                                       |
| 401       | AuthenticationRequiredError  | The operation requires an authenticated user. Verify that you have provided your API key.                               |
| 401       | UserNotActiveError           | The user account is not active. Make sure you properly activated your account by following the link sent to your email. |
| 401       | WrongCredentialsError        | The provided API key is incorrect.                                                                                      |
| 403       | ForbiddenError               | You are not allowed to perform the requested operation.                                                                 |
| 404       | NotFoundError                | The requested resource was not found.                                                                                   |
| 409       | AlreadyExistsError           | The resource already exists.                                                                                            |
| 424       | FailedDependencyError        | The request depended on another request and that request failed.                                                        |
| 429       | QuotaExceededError           | You have exceeded one of your quotas (minute, daily or monthly). Daily quotas are reset every day at 00:00 UTC.         |
| 429       | TooManyRequestsError         | Too many requests.                                                                                                      |
| 503       | TransientError               | Transient server error. Retry might work.                                                                               |
| 504       | DeadlineExceededError        | The operation took too long to complete.                                                                                |

---

← [Objects](introduction-objects.md) · [up](../README.md) · [Relationships](introduction-relationships.md) →

*Archived from <https://gtidocs.virustotal.com/reference/introduction-errors>.*
