---
title: "🔀 embedded_domains"
source: https://gtidocs.virustotal.com/reference/private-files-object-embedded_domains
slug: private-files-object-embedded_domains
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T02:14:16.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Private Files](../private-files-object.md) › 🔀 embedded_domains

---

# 🔀-embedded_domains

Domains contained in the file

The *embedded\_domains* relationship returns the list of ***all domains contained in the body of the sample***.

This relationship can be retrieved using the [relationships API endpoint](../../06-private-scanning/private-files/private-files-relationships.md). The response contains a list of [Domains](../domains-object.md) objects.

```json /private/files/{sha256}/embedded_domains
{
  "data": [
    {
      "attributes": {
        ...
      },
      "type": "domain",
      "id": <string>
    }  ,
    ...
  ],
  "links": {
    "next": <string>,
    "self": <string>
  },
  "meta": {
    "count": <int>,
    "cursor": <string>
  }
}
```
```json Example
{
	"meta": {
		"count": 15,
		"cursor": "STEKLg=="
	},
	"data": [
		{
			"attributes": {
				.....
			},
			"type": "domain",
			"id": "google.com",
			"links": {
				"self": "http://www.virustotal.com/api/v3/domains/google.com"
			}
		}
	],
	"links": {
		"self": "http://www.virustotal.com/api/v3/private/files/079b1db08ac52c94ba8fdbab638134a6a09a510ba10a87c1541ad6c7939a5679/embedded_domains?limit=1",
		"next": "http://www.virustotal.com/api/v3/private/files/079b1db08ac52c94ba8fdbab638134a6a09a510ba10a87c1541ad6c7939a5679/embedded_domains?cursor=STEKLg%3D%3D&limit=1"
	}
}
```

---

← [🔀 embedded_urls](embedded_urls.md) · [up](../README.md) · [🔀 embedded_ips](embedded_ips.md) →

*Archived from <https://gtidocs.virustotal.com/reference/private-files-object-embedded_domains>.*
