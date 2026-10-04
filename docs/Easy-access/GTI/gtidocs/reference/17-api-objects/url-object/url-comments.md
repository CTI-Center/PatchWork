---
title: "🔀 comments"
source: https://gtidocs.virustotal.com/reference/url-comments
slug: url-comments
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T01:06:52.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [URLs](../url-object.md) › 🔀 comments

---

# 🔀-comments

Comments in URL objects.

The *comments* relationship lists all comments posted by the VirusTotal community for a given URL.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/urls/urls-relationships.md). The response contains a list of [Comments](../comment-object.md) objects.

```json /urls/{url_id}/comments
{
  "data": [
    <COMMENT_OBJECT>,
    <COMMENT_OBJECT>,
    ...
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
    "data": [
        {
            "attributes": {
                "date": 1589288957,
                "html": "URL is trusted.",
                "tags": [
                    "_:web",
                    "_:public"
                ],
                "text": "URL is trusted.",
                "votes": {
                    "abuse": 0,
                    "negative": 0,
                    "positive": 0
                }
            },
            "id": "u-ea2ecfbfdg691g69309g3426dg47de3gba0g3a6egbe91g046g581g720g5f8g01-263007a7",
            "links": {
                "self": "https://www.virustotal.com/api/v3/comments/u-ea2ecfbfdg691g69309g3426dg47de3gba0g3a6egbe91g046g581g720g5f8g01-263007a7"
            },
            "type": "comment"
        },
        {
            "attributes": {
                "date": 1589282315,
                "html": "Gt",
                "tags": [
                    "_:web",
                    "_:public"
                ],
                "text": "Gt",
                "votes": {
                    "abuse": 0,
                    "negative": 0,
                    "positive": 0
                }
            },
            "id": "u-ea2ecfbfdw691w6930w7342wde47dw3cbaw13a6w4bew150w6358wf720w5f8w01-efbace2d",
            "links": {
                "self": "https://www.virustotal.com/api/v3/comments/u-ea2ecfbfdw691w6930w7342wde47dw3cbaw13a6w4bew150w6358wf720w5f8w01-efbace2d"
            },
            "type": "comment"
        }
    ],
     "links": {
        "next": "https://www.virustotal.com/api/v3/urls/cf4b367e49bfwb2204wc6f065w4aa1wf3cfew9cwd5abw06w7343dwa66w6a2wf5/comments?cursor=Cs8BChEKBGRhdGUSCQih7Ky1xMPlAhK1AWoRc352aXJ1c3RvdGFsY2xvdWRynwELEgNVUkwiQGNmNGIzNjdlNDliZjBiMjIwNDFjNmYwNjVmNGFhMTlwM2NmZTw5YzhkNWFiYzw2MTczNDNwMWE2NmM2YTI2ZjUMCxIHQ29tbWVudCJJY2Y0wjM2N2U0OWJmMGIyMjA0MWM2ZjA2NWY0YWExOWYzYWZlMzljOGQ1YWJjMDYxNzM0M2QxYTY2YzZhMjZmNS1mYTliOTM2YQwYACAB&limit=10",
        "self": "https://www.virustotal.com/api/v3/urls/cf4b367e49bfwb2204wc6f065w4aa1wf3cfew9cwd5abw06w7343dwa66w6a2wf5/comments?limit=10"
    },
    "meta": {
        "count": 140,
        "cursor": "Cs8BChEKBGRhdGUSCQih7Ky1xMPlAhK1AWoRc352aXJ1c3RvdGFsY2xvdWRynwELEgNVUkwiQGNmNGIzNjdlNDliZjBiMjIwNDFjNmYwNjVmNGFhMTlwM2NmZTw5YzhkNWFiYzw2MTczNDNwMWE2NmM2YTI2ZjUMCxIHQ29tbWVudCJJY2Y0wjM2N2U0OWJmMGIyMjA0MWM2ZjA2NWY0YWExOWYzYWZlMzljOGQ1YWJjMDYxNzM0M2QxYTY2YzZhMjZmNS1mYTliOTM2YQwYACAB"
    }
}
```

---

← [🔀 analyses](url-analyses.md) · [up](../README.md) · [🔀 related_comments](url-related_comments.md) →

*Archived from <https://gtidocs.virustotal.com/reference/url-comments>.*
