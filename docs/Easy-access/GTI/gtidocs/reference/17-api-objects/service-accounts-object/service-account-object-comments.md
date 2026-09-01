---
title: "🔀 comments"
source: https://gtidocs.virustotal.com/reference/service-account-object-comments
slug: service-account-object-comments
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:44:38.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Service Accounts](../service-accounts-object.md) › 🔀 comments

---

# 🔀-comments

Comments posted by a certain user

The *comments* relationship returns a list of ***all comments posted by a certain Service Account***.

This relationship can be retrieved by using the [relationships API endpoint](../../11-users-and-group-management/user-management/users-relationships.md) and contains a list of [Comment](../comment-object.md) objects.

```json /users/{user_id}/comments
{
  "data": [
    <COMMENT_OBJECT>
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
                "date": 1593902009,
                "html": "#spam #malware",
                "tags": [],
                "text": "#spam #malware",
                "votes": {
                    "abuse": 0,
                    "negative": 0,
                    "positive": 0
                }
            },
            "id": "d-spamverybad.com-905fd26e",
            "links": {
                "self": "https://www.virustotal.com/api/v3/comments/d-spamverybad-905fd26e"
            },
            "type": "comment"
        },
        {
            "attributes": {
                "date": 1560708145,
                "html": "is this a false positive?<br />",
                "tags": [],
                "text": "is this a false positive?\n",
                "votes": {
                    "abuse": 0,
                    "negative": 0,
                    "positive": 0
                }
            },
            "id": "f-cb3c63183c53153833c53b93e5c3e2e315b30c0e3314833d77231bab37e8c33a-a3a313c8",
            "links": {
                "self": "https://www.virustotal.com/api/v3/comments/f-cb3c63183c53153833c53b93e5c3e2e315b30c0e3314833d77231bab37e8c33a-a3a313c8"
            },
            "type": "comment"
        }
    ],
    "links": {
        "self": "https://www.virustotal.com/api/v3/users/spellman/comments?limit=10"
    },
    "meta": {
        "count": 2
    }
}
```

---

← [🔀🧑‍💻 api_quota_group](service-account-object-api-quota-group.md) · [up](../README.md) · [🔀🧑‍💻 groups](service-account-object-groups.md) →

*Archived from <https://gtidocs.virustotal.com/reference/service-account-object-comments>.*
