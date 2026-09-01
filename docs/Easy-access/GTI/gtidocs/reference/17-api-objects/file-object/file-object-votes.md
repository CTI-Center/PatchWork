---
title: "🔀 votes"
source: https://gtidocs.virustotal.com/reference/file-object-votes
slug: file-object-votes
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:42:04.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › 🔀 votes

---

# 🔀-votes

Votes for a given file

The *votes* relationship returns a list ***containing the votes for a given file***.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/files/files-relationships.md). The response contains a list of [Vote](../vote-object.md) objects.

```json /files/{file_hash}/votes
{
  "data": [
  	<VOTE_OBJECT>,
    <VOTE_OBJECT>
  ],
  "links": {
    "next": "<string>",
    "self": "<string>"
  },
  "meta": {
    	"count": <int>,
      "cursor": "<string>"
  }
}
```
```json Example
{
  "meta": {
    "count": 4,
    "cursor": "Cs8BChEKBGRhdGUSCQj4_O20wfbmAhK1AWoRc352aXJ1c3RvdGFsY2xvdWRynwELEgZTYW1wbGUiQDg3MDgzODgyY2M2MDE1OTg0ZWIwNDExYTk5ZDM5ODE4MTdmNWRjNWM5MGJhMjRmMDk0MDQyMGM1NTQ4ZDgyZGUMCxIEVm90ZSJJODcwODM4ODJjYzYwMTU5ODRlYjA0MTFhOTlkMzk4MTgxN2Y1ZGM1YzkwYmEyNGYwOTQwNDIwYzU1NDhkODJkZS0wYWExZGQwYQwYACAB"
  },
  "data": [
    {
      "attributes": {
        "date": 1592125710,
        "verdict": "harmless",
        "value": 1
      },
      "type": "vote",
      "id": "f-87083882cc6015984eb0411a99d3981817f5dc5c90ba24f0940420c5548d82de-726b4272",
      "links": {
        "self": "https://www.virustotal.com/api/v3/votes/f-87083882cc6015984eb0411a99d3981817f5dc5c90ba24f0940420c5548d82de-726b4272"
      }
    },
    {
      "attributes": {
        "date": 1578572659,
        "verdict": "harmless",
        "value": 7
      },
      "type": "vote",
      "id": "f-87083882cc6015984eb0411a99d3981817f5dc5c90ba24f0940420c5548d82de-0aa1dd0a",
      "links": {
        "self": "https://www.virustotal.com/api/v3/votes/f-87083882cc6015984eb0411a99d3981817f5dc5c90ba24f0940420c5548d82de-0aa1dd0a"
      }
    }
  ],
  "links": {
    "self": "https://www.virustotal.com/api/v3/files/87083882cc6015984eb0411a99d3981817f5dc5c90ba24f0940420c5548d82de/votes?limit=2",
    "next": "https://www.virustotal.com/api/v3/files/87083882cc6015984eb0411a99d3981817f5dc5c90ba24f0940420c5548d82de/votes?cursor=Cs8BChEKBGRhdGUSCQj4_O20wfbmAhK1AWoRc352aXJ1c3RvdGFsY2xvdWRynwELEgZTYW1wbGUiQDg3MDgzODgyY2M2MDE1OTg0ZWIwNDExYTk5ZDM5ODE4MTdmNWRjNWM5MGJhMjRmMDk0MDQyMGM1NTQ4ZDgyZGUMCxIEVm90ZSJJODcwODM4ODJjYzYwMTU5ODRlYjA0MTFhOTlkMzk4MTgxN2Y1ZGM1YzkwYmEyNGYwOTQwNDIwYzU1NDhkODJkZS0wYWExZGQwYQwYACAB&limit=2"
  }
}
```

---

← [🔀 email_attachments](file-object-email-attachments.md) · [up](../README.md) · [monitor_info](file-object-monitor-info.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-votes>.*
