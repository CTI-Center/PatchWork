---
title: "Dark Web Communication Channel"
source: https://gtidocs.virustotal.com/reference/dark-web-communication-channel-object
slug: dark-web-communication-channel-object
section: reference
group: "API OBJECTS"
updatedAt: 2026-02-27T12:41:19.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Dark Web](../dark-web-objects.md) › Dark Web Communication Channel

---

# dark-web-communication-channel

A Dark Web Communication Channel object represents the specific location (board or channel) where the communication occurred. Its `type` is set to `ddw_communication_channel` and it is associated to Dark Web Communication object of `type`:`messenger_message` or `type`:`forum_post`.

# object-attributes

Dark Dark Web Communication Channel objects contains the following attributes:

* `name`: <*string*> the name of the communication channel.
* `description`: <*string*> the description of the communication channel.
* `original_id`: <*string*> the unique identifier of the communication channel entity on its original platform.
* `invite_url`: \<string> the invite URL for the communication channel.
* `url`: \<string> he primary landing page or entry point for the communication channel.
* `path`: <*string*> the nested folder or category structure leading to the specific communication channel.
* `channel_type`: <*string*> the classification of the communication channel. Supported values are `forum_board` and `messenger_channel`.

<br />

---

← [Dark Web Communication](dark-web-communication-object.md) · [up](../README.md) · [Dark Web Conversation Thread](dark-web-conversation-thread-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/dark-web-communication-channel-object>.*
