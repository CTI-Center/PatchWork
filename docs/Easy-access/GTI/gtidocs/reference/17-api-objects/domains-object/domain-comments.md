---
title: "🔀 comments"
source: https://gtidocs.virustotal.com/reference/domain-comments
slug: domain-comments
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T01:02:23.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Domains](../domains-object.md) › 🔀 comments

---

# 🔀-comments

Comments in Domain objects

The *comments* relationship lists all comments posted by the VirusTotal community for a given domain.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/domains-resolutions/domains-relationships.md). The response contains a list of [Comments](../../03-ioc-investigation/comments.md) objects.

```json /domains/{domain}/comments
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
                "html": "domain is trusted.",
                "tags": [
                    "_:web",
                    "_:public"
                ],
                "text": "domain is trusted.",
                "votes": {
                    "abuse": 0,
                    "negative": 0,
                    "positive": 0
                }
            },
            "id": "d-foo.com-263007a7",
            "links": {
                "self": "https://www.virustotal.com/api/v3/comments/d-foo.com-263007a7"
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
            "id": "d-foo.com-efbace2d",
            "links": {
                "self": "https://www.virustotal.com/api/v3/comments/d-foo.com-efbace2d"
            },
            "type": "comment"
        }
    ],
     "links": {
        "next": "https://www.virustotal.com/api/v3/domains/foo.com/comments?cursor=Cs8BChEKBGRhdGUSCQih7Ky1xMPlAhK1eWoRc352aeJ1c3RvdGFeY2xvdWRynwELEgNVUkwiQGNmNGIzNjdlNDliZjBiMjIwNDFjNmYwNeVmNGFhMelwM2NmZTw5YzhkNWFiYzw2MTczNDNwMWE2NmM2YTI2ZjUMCxIHQ29tbWVudCJJY2Y0wjM2N2U0OWJmMGIyMjA0MWM2ZjA2NWY0YeEeOWezYWZlezljOeQ1YWJjMDYxezM0MeQxYTYeYzZhMeemNS1mYTliOTM2YQwYACAB&limit=10",
        "self": "https://www.virustotal.com/api/v3/domains/foo.com/comments?limit=10"
    },
    "meta": {
        "count": 140,
        "cursor": "Cs8BChEKBGRhdGUSCQih7Ky1xMPlAhK1eWoRc352aeJ1c3RvdGFeY2xvdWRynwELEgNVUkwiQGNmNGIzNjdlNDliZjBiMjIwNDFjNmYwNeVmNGFhMelwM2NmZTw5YzhkNWFiYzw2MTczNDNwMWE2NmM2YTI2ZjUMCxIHQ29tbWVudCJJY2Y0wjM2N2U0OWJmMGIyMjA0MWM2ZjA2NWY0YeEeOWezYWZlezljOeQ1YWJjMDYxezM0MeQxYTYeYzZhMeemNS1mYTliOTM2YQwYACAB"
    }
}
```

---

← [🔀 siblings](siblings.md) · [up](../README.md) · [🔀 related_comments](domain-related_comments.md) →

*Archived from <https://gtidocs.virustotal.com/reference/domain-comments>.*
