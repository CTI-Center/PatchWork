---
title: "Dark Web Service"
source: https://gtidocs.virustotal.com/reference/dark-web-service-object
slug: dark-web-service-object
section: reference
group: "API OBJECTS"
updatedAt: 2026-02-27T12:41:50.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Dark Web](../dark-web-objects.md) › Dark Web Service

---

# dark-web-service

A Dark Web Service entity represents the platform where a communication occurs, and its `type` is set to `ddw_service`.

# object-attributes

Dark Web Service objects contains the following attributes:

* `name`: <*string*> the name of the service, provided by the original platform.
* `description`: <*string*> the description of the service.
* `original_id`: <*string*> the identifier assigned to the service by the original platform.
* `url`: <*string*> the URL of the service.
* `domain`: <*string*> the domain on which the service is hosted.

# relationships

In addition to the previously described attributes, service objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](../../01-api-introduction/api-responses/introduction-relationships.md) section.

The following table shows a summary of available relationships.

| Relationship   | Return object type                                                                             |
| :------------- | :--------------------------------------------------------------------------------------------- |
| communications | List of [Dark Web Communications](dark-web-communication-object.md) belonging to the service. |

---

← [Dark Web Conversation Thread](dark-web-conversation-thread-object.md) · [up](../README.md) · [Dark Web User Profile](dark-web-user-profile-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/dark-web-service-object>.*
