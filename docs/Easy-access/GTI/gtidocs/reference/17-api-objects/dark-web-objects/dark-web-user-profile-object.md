---
title: "Dark Web User Profile"
source: https://gtidocs.virustotal.com/reference/dark-web-user-profile-object
slug: dark-web-user-profile-object
section: reference
group: "API OBJECTS"
updatedAt: 2026-02-27T12:42:01.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Dark Web](../dark-web-objects.md) › Dark Web User Profile

---

# dark-web-user-profile

A Dark Web User Profile represents the identity of a communication author, and its `type` is set to `ddw_user_profile`.

# object-attributes

Dark Web User Profile objects contains the following attributes:

* `name`: <*string*> the full name of the user.
* `given_name`: <*string*> the first name of the user.
* `family_name`: <*string*> the last name of the user.
* `last_seen_ip_v4`: <*string*> the last known IPv4 address for the profile.
* `is_bot`: <*boolean*> indicates if the profile belongs to an automated agent.
* `original_id`: <*string*> the unique identifier assigned to the profile by its original platform.
* `phone`: <*list\_of\_strings*> a list of phone numbers associated with the user profile.
* `email`: <*list\_of\_strings*> a list of email addresses associated with the user profile.
* `jid`: <*list\_of\_strings*> a list of Jabber messenger IDs associated with the user profile.
* `discord_handle`: <*list\_of\_strings*> a list of Discord handles associated with the user profile.
* `twitter_handle`: <*list\_of\_strings*> a list of X handles associated with the user profile.
* `tox_id`: <*list\_of\_strings*> a list of TOX messenger IDs associated with the user profile.
* `titles`: <*list\_of\_strings*> a list of titles assigned to the profile (e.g., user ranks on forums).
* `avatar_image`: <*dictionary*> a dictionary containing metadata for the profile's avatar, including `filename`, `size_in_bytes`, `mime_type`, and various cryptographic hashes (`md5_hash`, `sha1_hash`, `sha256_hash`, and `ssdeep_hash`).

---

← [Dark Web Service](dark-web-service-object.md) · [up](../README.md) · [Domains](../domains-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/dark-web-user-profile-object>.*
