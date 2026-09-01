---
title: "🔀 submissions"
source: https://gtidocs.virustotal.com/reference/url-submissions
slug: url-submissions
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T01:07:02.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [URLs](../url-object.md) › 🔀 submissions

---

# 🔀-submissions

URL submissions

The *submissions* relationship returns a list containing ***all submissions for a given URL***. This relationship is only available for Premium API users.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/urls/urls-relationships.md). The response contains a list of [Submission](../submission-object.md) objects.

```json /urls/{url_id}/submissions
{
  "data": [
     <SUBMISSION_OBJECT>,
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
                "city": "dublin",
                "country": "IE",
                "date": 1591951666,
                "interface": "api",
                "source_key": "f0eff5fa"
            },
            "id": "u-cffb36fe49ff0bf2041f6f065f4aa19f3cff39cfd5abf0617f43d1f66cfa2ff5-1591951666",
            "links": {
                "self": "https://www.virustotal.com/api/v3/submissions/u-cffb36fe49ff0bf2041f6f065f4aa19f3cff39cfd5abf0617f43d1f66cfa2ff5-1591951666"
            },
            "type": "submission"
        },
        {
            "attributes": {
                "city": "sinop",
                "country": "TR",
                "date": 1591949974,
                "interface": "api",
                "source_key": "4f2ffdf7"
            },
            "id": "u-cffb36fe49ff0bf2041f6f065f4aa19f3cff39cfd5abf0617f43d1f66cfa2ff5-1591949974",
            "links": {
                "self": "https://www.virustotal.com/api/v3/submissions/u-cffb36fe49ff0bf2041f6f065f4aa19f3cff39cfd5abf0617f43d1f66cfa2ff5-1591949974"
            },
            "type": "submission"
        },
        {
            "attributes": {
                "city": "dublin",
                "country": "IE",
                "date": 1591948606,
                "interface": "api",
                "source_key": "e0ef3f7f"
            },
            "id": "u-cffb36fe49ff0bf2041f6f065f4aa19f3cff39cfd5abf0617f43d1f66cfa2ff5-1591948606",
            "links": {
                "self": "https://www.virustotal.com/api/v3/submissions/u-cffb36fe49ff0bf2041f6f065f4aa19f3cff39cfd5abf0617f43d1f66cfa2ff5-1591948606"
            },
            "type": "submission"
        },
        {
            "attributes": {
                "city": "dublin",
                "country": "IE",
                "date": 1591947586,
                "interface": "api",
                "source_key": "e8f9f4cf"
            },
            "id": "u-cffb36fe49ff0bf2041f6f065f4aa19f3cff39cfd5abf0617f43d1f66cfa2ff5-1591947586",
            "links": {
                "self": "https://www.virustotal.com/api/v3/submissions/u-cffb36fe49ff0bf2041f6f065f4aa19f3cff39cfd5abf0617f43d1f66cfa2ff5-1591947586"
            },
            "type": "submission"
        }
    ],
    "links": {
        "next": "https://www.virustotal.com/api/v3/urls/cffb36fe49ff0bf2041f6f065f4aa19f3cff39cfd5abf0617f43d1f66cfa2ff5/submissions?cursor=dt0BChEKBGRhdGUSCQiAp6adyPvpAhLDAdoRc352aXJdc3RvdGFsYdxvdWRyrQELEgNVUkwiQGNmNGIzNjdlNDliZjBiMjIwNdFjNmYwdjVmNGFhMTlmM2NmZTM5YzhkNWFiYzA2MTczNDNkMWE2NmM2YTI2ZjUMCxIKU3VibWlzc2lvbiJUY2Y0YjM2N2U0OWJmMGIyMjA0MWM2ZjA2NWYdYWExOWdzY2dlMzljOdQ1YWJjdDYxNzM0d2QxYTY2YdZhMjZdNS0yMdIwLTA2LTEyVDA1OjQwOjQ2DBgAIAE%3D&limit=3",
        "self": "https://www.virustotal.com/api/v3/urls/cffb36fe49ff0bf2041f6f065f4aa19f3cff39cfd5abf0617f43d1f66cfa2ff5/submissions?limit=10"
    },
    "meta": {
        "count": 200,
        "cursor": "dt0BChEKBGRhdGUSCQiAp6adyPvpAhLDAdoRc352aXJdc3RvdGFsYdxvdWRyrQELEgNVUkwiQGNmNGIzNjdlNDliZjBiMjIwNdFjNmYwdjVmNGFhMTlmM2NmZTM5YzhkNWFiYzA2MTczNDNkMWE2NmM2YTI2ZjUMCxIKU3VibWlzc2lvbiJUY2Y0YjM2N2U0OWJmMGIyMjA0MWM2ZjA2NWYdYWExOWdzY2dlMzljOdQ1YWJjdDYxNzM0d2QxYTY2YdZhMjZdNS0yMdIwLTA2LTEyVDA1OjQwOjQ2DBgAIAE="
    }
}
```

---

← [🔀 redirects_to](url-redirects_to.md) · [up](../README.md) · [🔀 embedded_js_files](urls-embedded_js_files.md) →

*Archived from <https://gtidocs.virustotal.com/reference/url-submissions>.*
