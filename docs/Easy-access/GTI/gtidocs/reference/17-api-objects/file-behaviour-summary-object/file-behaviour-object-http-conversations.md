---
title: "http_conversations"
source: https://gtidocs.virustotal.com/reference/file-behaviour-object-http-conversations
slug: file-behaviour-object-http-conversations
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:43:04.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files Behaviour](../file-behaviour-summary-object.md) › http_conversations

---

# http_conversations

HTTP Calls.

`http_conversations` contains a list of **HTTP calls performed by the file under study.** It is a list of dictionaries, every item in the list contains the following fields:

* `request_headers`: <*dictionary*>  contains the request headers. It's a dictionary having both keys and values as *string*.
* `request_method`: <*string*> HTTP request method. Can be any of:
  * `GET`
  * `HEAD`
  * `POST`
  * `PUT`
  * `DELETE`
  * `TRACE`
  * `OPTIONS`
  * `CONNECT`
  * `PATCH`
* `response_body_filetype`: <*string*> response body filetype.
* `response_body_first_ten_bytes`: <*string*> first ten 10 bytes from the response body.
* `response_headers`: <*dictionary*> contains the response headers. It's a dictionary having both keys and values as *string*.
* `response_status_code`: <*integer*> integer of the response status code, e.g. 200.
* `url`: <*string*> the full hostname and path of the looked up URL.

```json HTTP conversations
{
    "data": {
        "attributes": {
            "http_conversations": [
                {
                    "request_headers": {
                        "<string>": "<string>"
                    },
                    "request_method": "<string>",
                    "response_headers": {
                        "<string>": "<string>"
                    },
                    "response_body_filetype": "<string>",
                    "response_body_first_ten_bytes": "<string>",
                    "response_status_code": <int>,
                    "url": "<string>"
                }
            ]
        }
    }
}
```
```json Example
{
    "data": {
        "attributes": {
            "http_conversations": [
                {
                    "request_headers": {
                        "Accept": "*/*",
                        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)"
                    },
                    "request_method": "GET",
                    "response_body_filetype": "PDF",
                    "response_headers": {
                        "Cache-Control": "no-cache",
                        "Connection": "keep-alive",
                        "Content-Type": "text/html; charset=UTF-8",
                        "Date": "Sat, 23 Nov 2019 09:02:26 GMT",
                        "Server": "nginx/1.14.0",
                        "Status-Line": "HTTP/1.1 200",
                        "Transfer-Encoding": "chunked",
                        "Vary": "Accept-Encoding",
                        "X-Powered-By": "PHP/7.2.9"
                    },
                    "response_status_code": 200,
                    "url": "http://foo.blablabla.com/blablabla.pdf"
                }
            ]
        }
    }
}
```

---

← [permissions_checked](file-behaviour-object-permissions-checked.md) · [up](../README.md) · [dns_lookups](file-behaviour-object-dns-lookup.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-behaviour-object-http-conversations>.*
