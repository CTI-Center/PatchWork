---
title: "🔀 embedded_ips"
source: https://gtidocs.virustotal.com/reference/embedded_ips
slug: embedded_ips
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T02:14:17.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Private Files](../private-files-object.md) › 🔀 embedded_ips

---

# 🔀-embedded_ips

IP addresses contained in the file

The *embedded\_ips* relationship returns the list of ***all IP addresses contained in the body of the sample***.

This relationship can be retrieved using the [relationships API endpoint](../../06-private-scanning/private-files/private-files-relationships.md). The response contains a list of [IP addresses](../ip-object.md) objects.

```json /private/files/{sha256}/embedded_ips
{
  "data": [
    {
      "attributes": {
        ...
      },
      "type": "ip_address",
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
		"count": 2,
		"cursor": "STEKLg=="
	},
	"data": [
		{
			"attributes": {
				.....
			},
			"type": "ip_address",
			"id": "8.8.8.8",
			"links": {
				"self": "http://www.virustotal.com/api/v3/ip_addresses/8.8.8.8"
			}
		}
	],
	"links": {
		"self": "http://www.virustotal.com/api/v3/private/files/079b1db08ac52c94ba8fdbab638134a6a09a510ba10a87c1541ad6c7939a5679/embedded_ips?limit=1",
		"next": "http://www.virustotal.com/api/v3/private/files/079b1db08ac52c94ba8fdbab638134a6a09a510ba10a87c1541ad6c7939a5679/embedded_ips?cursor=STEKLg%3D%3D&limit=1"
	}
}
```

---

← [🔀 embedded_domains](private-files-object-embedded_domains.md) · [up](../README.md) · [Private Files Behaviours](../private-file-behaviours-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/embedded_ips>.*
