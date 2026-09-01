---
title: "Agentic Session"
source: https://gtidocs.virustotal.com/reference/agentic-session-object
slug: agentic-session-object
section: reference
group: "API OBJECTS"
updatedAt: 2026-08-03T14:11:29.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Agentic Session

---

# agentic-session

Information about Google Threat Intelligence Agentic Sessions

An **Agentic Session** object represents a conversation with the Google Threat Intelligence agent. Each session keeps the ordered list of events exchanged with the agent and any artifacts attached to it. The object `type` is `agentic_session`. Sessions are retrieved with [Get a session](../16-agentic/sessions/get-session.md) and enumerated with [List sessions](../16-agentic/sessions/list-sessions.md).

## object-attributes

An agentic session object contains the following attributes:

* `title`: <*string*> title of the session.
* `creation_date`: <*string*> ISO-8601 UTC timestamp of when the session was created.
* `last_modification_date`: <*string*> ISO-8601 UTC timestamp of the session's last modification.
* `events`: <*list of dictionaries*> ordered list of events exchanged with the agent. Each event is a `DisplayableUiMessage` with:
  * `id`: <*string*> unique identifier of the event.
  * `message_type`: <*string*> type of the event. One of `USER_MESSAGE`, `AGENT_THOUGHT`, `AGENT_FINAL_RESPONSE`, `FUNCTION_CALL`, `FUNCTION_RESPONSE`.
  * Depending on `message_type`, the event carries its corresponding payload:
    * `user_message`: <*dictionary*> payload for `USER_MESSAGE`. The message submitted by the user.
    * `agent_thought`: <*dictionary*> payload for `AGENT_THOUGHT`. An intermediate reasoning step produced by the agent.
    * `agent_final_response`: <*dictionary*> payload for `AGENT_FINAL_RESPONSE`. The agent's final answer.
    * `function_call`: <*dictionary*> payload for `FUNCTION_CALL`. A tool invocation requested by the agent.
    * `function_response`: <*dictionary*> payload for `FUNCTION_RESPONSE`. The result returned by a called function.

---

← [Activity Log](activity-log.md) · [up](README.md) · [Alerts](alerts-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/agentic-session-object>.*
