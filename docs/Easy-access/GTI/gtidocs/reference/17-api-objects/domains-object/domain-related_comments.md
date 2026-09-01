---
title: "🔀 related_comments"
source: https://gtidocs.virustotal.com/reference/domain-related_comments
slug: domain-related_comments
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T01:02:24.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Domains](../domains-object.md) › 🔀 related_comments

---

# 🔀-related_comments

Comments posted in related objects

The *related\_comments* relationship lists all comments posted by the VirusTotal community in a domain's related objects (that is, all URLs under that domain and the domain's own comments).

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/urls/urls-relationships.md). The response contains a list of [Comments](../../03-ioc-investigation/comments.md) objects. If the comment belongs to an object different than the domain itself, an additional context\_attribute is added:

* `posted_in`: <*dictionary*> specifies the object where the comment was posted.
  * `id`: <*string*> object ID.
  * `type`: <*string*> object type.

```json /domains/{domain}/related_comments
{
  "data": [
    {
        "attributes": <COMMENT_OBJECT>,
        "context_attributes": {
            "posted_in": {
                "id": "<string>",
                "type": "<string>"
            }
        }
    },
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
                "date": 1591887755,
                "html": "#safe",
                "tags": [
                    "_:web",
                    "_:public",
                    "safe"
                ],
                "text": "#safe",
                "votes": {
                    "abuse": 0,
                    "negative": 0,
                    "positive": 0
                }
            },
            "context_attributes": {
                "posted_in": {
                    "id": "6f0e3fea9cb7f6a83fa91ff38a94f64c8fc6e84fbb94b590fb05f2300f8d64f1",
                    "type": "url"
                }
            },
            "id": "u-6f0e3fea9cb7f6a83fa91ff38a94f64c8fc6e84fbb94b590fb05f2300f8d64f1-99b20106",
            "links": {
                "self": "https://www.virustotal.com/api/v3/comments/u-6f0e3fea9cb7f6a83fa91ff38a94f64c8fc6e84fbb94b590fb05f2300f8d64f1-99b20106"
            },
            "type": "comment"
        },
        {
            "attributes": {
                "date": 1591887361,
                "html": "#safe",
                "tags": [
                    "_:web",
                    "_:public",
                    "safe"
                ],
                "text": "#safe",
                "votes": {
                    "abuse": 0,
                    "negative": 0,
                    "positive": 0
                }
            },
            "context_attributes": {
                "posted_in": {
                    "id": "3f47d9b5ed9164e2g9a741gf8bbg42aa711gc251ga3aag0540g6ae1a4gc30g16",
                    "type": "url"
                }
            },
            "id": "u-3f47d9b5ed9164e2g9a741gf8bbg42aa711gc251ga3aag0540g6ae1a4gc30g16-f98e7b29",
            "links": {
                "self": "https://www.virustotal.com/api/v3/comments/u-3f47d9b5ed9164e2g9a741gf8bbg42aa711gc251ga3aag0540g6ae1a4gc30g16-f98e7b29"
            },
            "type": "comment"
        }
    ],
    "links": {
        "self": "https://www.virustotal.com/api/v3/domains/example.com/related_comments?limit=10"
    },
    "meta": {
        "count": 2
    }
}
```

---

← [🔀 comments](domain-comments.md) · [up](../README.md) · [🔀 historical_ssl_certificates](domain-historical_ssl_certificates.md) →

*Archived from <https://gtidocs.virustotal.com/reference/domain-related_comments>.*
