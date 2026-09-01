---
title: "Activity Log"
source: https://gtidocs.virustotal.com/reference/activity-log
slug: activity-log
section: reference
group: "API OBJECTS"
updatedAt: 2025-11-05T15:02:59.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Activity Log

---

# activity-log

The Activity Log objects provide a time-stamped record of user and system activities within the platform.

These are the object attributes:

* `info.user`: <*string*>: Identifier of the user that was affected by the action
* `ip`: <*string*>: The IP address from which the user performed the action
* `date`: <*string*>: UTC action timestamp
* `action`: <*string*>: Logged action such as: Remove admin from group, Add admin to group, etc

```json Activity Log object
{
    "id": "<_string_>",
    "type": "activity_log_entry",
    "links": {
        "self": "https://www.virustotal.com/api/v3/activity_log_entries/<_string_>"
     },
     "attributes": {
         "info": {
             "user": "<_string_> "
         },
         "ip": "<_string_>",
         "date": "<int:timestamp>",
         "action": "<_string_>"
    }
}
```

---

← [Delete a session](../16-agentic/sessions/delete-session.md) · [up](README.md) · [Agentic Session](agentic-session-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/activity-log>.*
