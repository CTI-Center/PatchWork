---
title: "Submissions"
source: https://gtidocs.virustotal.com/reference/submission-object
slug: submission-object
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T01:06:38.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Submissions

---

# submissions

Information about submissions

Information about a submission.

## object-attributes

A submission contains the following attributes:

* `date`: <*integer*> submission date as UTC timestamp.
* `interface`: <*string*> how the item was submitted (via api, UI, email, etc). Only available for Premium API users.
* `country`: <*string*> country ISO code from which the item was submitted. Only available for Premium API users.
* `city`: <*string*> city name from which the item was submitted. Only available for Premium API users.
* `name`: <*string*> filename the item was submitted with. Only available for Premium API users.
* `source_key`: <*string*> anonymised token that uniquely identifies a submitter. Only available for Premium API users.

```json "submission" object
{
  "data": {
    "attributes": {
      "city": "<string>",
      "country": "<string>",
      "date": <int:timestamp>,
      "interface": "<string>",
      "name": "<string>",
      "source_key": "<string>"
    },
    "id": "<string>",
    "links": {
      "self": "https://www.virustotal.com/api/v3/submissions/<id>"
    },
    "type": "submission"
  }
}
```
```json Example
{
  "data": {
    "attributes": {
      "city": "ashburn",
      "country": "US",
      "date": 1632333331,
      "interface": "api",
      "name": "installer.msi",
      "source_key": "7f6646ad"
    },
    "id": "f-e7a2b2c164285d1203062b752d87d2f72ca9e2810b52a61f281828f28722d609-1632333331",
    "links": {
      "self": "https://www.virustotal.com/api/v3/submissions/f-e7a2b2c164285d1203062b752d87d2f72ca9e2810b52a61f281828f28722d609-1632333331"
    },
    "type": "submission"
  }
}
```

---

← [SSL Certificate](ssl-certificate-object.md) · [up](README.md) · [Threat Actor](threat-actor-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/submission-object>.*
