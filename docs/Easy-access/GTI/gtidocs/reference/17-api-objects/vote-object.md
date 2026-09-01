---
title: "Votes"
source: https://gtidocs.virustotal.com/reference/vote-object
slug: vote-object
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T01:07:35.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Votes

---

# votes

vote objects

* `attributes`: data about a specific vote.
  * `date`: when the vote was done.
  * `value`: weight given by this vote (positive or negative) for Community Score.
  * `verdict`: note if vote was for making it "malicious" or "harmless".
* `id`: resource identifier of the vote.
* `links`: contains "self", with a link to the vote itself.
* `type`: value is "vote", that is the object type.

```json "vote" object
{
  "attributes": {"date": <int:timestamp>,
                 "value": <int>,
                 "verdict": "<string>"},
  "id": "<string>",
  "links": {"self": "<string>"},
  "type": "vote"
}
```

---

← [🔀 votes](user-object/user-object-votes.md) · [up](README.md) · [Vulnerability](vulnerability-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/vote-object>.*
