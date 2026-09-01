---
title: "URLs"
source: https://gtidocs.virustotal.com/reference/urls
slug: urls
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T02:04:18.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [IoC Investigation](README.md) › URLs

---

# urls

Google Threat Intelligence analyses not only files but also URLs. In this section you will find the API endpoints for analysing URLs and getting information about them.

## url-identifiers

Whenever we talk about an URL identifier in this documentation we are referring to a sequence of characters that uniquely identify a specific URL. Those identifiers can adopt two forms:

* The SHA-256 of the canonized URL.
* The string resulting from encoding the URL in base64 (without the "=" padding).

All URL identifiers returned by the Google TI API are in the first form, once you have one of those identifiers you can use it in subsequent calls to the API that require a URL identifier. However, generating such identifiers by yourself can be difficult because of the canonicalization algorithm that must be applied to the URL before computing the SHA-256. The canonicalization makes sure that two URLs that differ only in minor aspects, like some escaped characters, have the same identifier. For that reason we offer the possibility of identifying the URL by encoding it in base64 and using the resulting string as the its identifier. In such cases the URL doesn't need to be canonized, that's done server-side by Google TI.

Notice however that we use unpadded base64 encoding, as defined in [RFC 4648 section 3.2](https://tools.ietf.org/html/rfc4648#section-3.2), which means that the resulting URL identifiers shouldn't be padded with "=" as base64-encoded data usually is.

Here you have some examples of how to generate a URL identifier:

```python
import base64

url_id = base64.urlsafe_b64encode("http://www.somedomain.com/this/is/my/url".encode()).decode().strip("=")
```
```go
import 	"encoding/base64"

var urlID = base64.RawURLEncoding.EncodeToString([]byte("http://www.somedomain.com/this/is/my/url"))
```

---

← [Get all behavior reports for a file](files-behaviours/get-all-behavior-reports-for-a-file.md) · [up](README.md) · [Scan URL](urls/scan-url.md) →

*Archived from <https://gtidocs.virustotal.com/reference/urls>.*
