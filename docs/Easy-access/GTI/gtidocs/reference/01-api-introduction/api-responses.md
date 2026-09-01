---
title: "API responses"
source: https://gtidocs.virustotal.com/reference/api-responses
slug: api-responses
section: reference
group: "API Introduction"
updatedAt: 2025-09-25T00:33:25.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API Introduction](README.md) › API responses

---

# api-responses

Most endpoints in the Google Threat Intelligence API return a response in JSON format. Unless otherwise specified, a successful request's response returns a 200 HTTP status code and has the following format:

```json Response structure
{
  "data": <response data>
}
```

`<response data>` is usually an [object](api-responses/introduction-objects.md) or a list of objects, but that's not always the case. An example of this is the [/files/upload\_url](../03-ioc-investigation/files/files-upload-url.md) endpoint, which returns a URL. Refer to each endpoint's documentation to learn more about its return data structure.

---

← [Google Threat Intelligence API Overview](api-overview.md) · [up](README.md) · [Key concepts](api-responses/introduction-key-concepts.md) →

*Archived from <https://gtidocs.virustotal.com/reference/api-responses>.*
