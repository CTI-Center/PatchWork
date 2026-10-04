---
title: "Flow"
source: https://gtidocs.virustotal.com/reference/flow-object
slug: flow-object
section: reference
group: "API OBJECTS"
updatedAt: 2026-08-03T15:08:56.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Flow

---

# flow

Information about Agentic Flows

> 🚧 Special privileges required
>
> Flows are only available to users with the Google Threat Intelligence (Google TI) Enterprise or Enterprise Plus licenses, and require AI features to be enabled in your group settings.

A **Flow** object is a user-defined automation graph made of *nodes* (steps) and *connections* (edges) that Google Threat Intelligence runs on a trigger. The object `type` is `flow`.

## object-attributes

A flow object contains the following attributes:

* `name`: <*string*> human-readable name of the Flow (required on creation, up to 255 characters).
* `enabled`: <*boolean*> whether the Flow runs on its trigger. A disabled Flow can still be run manually via *Run a Flow now*.
* `nodes`: <*list of dictionaries*> the steps of the Flow. Each node has:
  * `id`: <*string*> node identifier, unique within the Flow.
  * `type`: <*string*> node type. One of `NODE_TYPE_SCHEDULE_TIME`, `NODE_TYPE_RUN_PROMPT`, `NODE_TYPE_SEND_EMAIL`, `NODE_TYPE_RUN_SAVED_SEARCH`, `NODE_TYPE_SAVE_REPORT`.
  * `name`: <*string*> display name of the node.
  * `version`: <*integer*> node schema version.
  * `schedule_node`: <*dictionary*> present when `type` is `NODE_TYPE_SCHEDULE_TIME`.
    * `cron_expression`: <*string*> cron schedule, e.g. `0 9 * * *`.
    * `timezone`: <*string*> IANA timezone, e.g. `UTC`.
  * `run_prompt_node`: <*dictionary*> present when `type` is `NODE_TYPE_RUN_PROMPT`.
    * `prompt`: <*string*> the prompt sent to the Agentic platform.
  * `send_email_node`: <*dictionary*> present when `type` is `NODE_TYPE_SEND_EMAIL`.
    * `notification_emails`: <*list of strings*> recipient addresses.
    * `email_subject`: <*string*> custom subject. Defaults to the Flow name when empty.
    * `message`: <*string*> free-text email body.
  * `run_saved_search_node`: <*dictionary*> present when `type` is `NODE_TYPE_RUN_SAVED_SEARCH`.
    * `saved_search_id`: <*string*> identifier of the saved search to run.
* `connections`: <*list of dictionaries*> the edges wiring nodes together. Each connection has:
  * `source_node_id`: <*string*> id of the node the edge starts from.
  * `target_node_id`: <*string*> id of the node the edge points to.
  * `source_handle`: <*string*> branch label on the source node (e.g. a `true` path); empty for a plain edge.
* `trigger_state`: <*dictionary*> scheduler-managed trigger bookkeeping; `null` when the Flow has no schedule.
  * `last_run_at`: <*integer*> last time the trigger fired (UTC timestamp).
* `creation_date`: <*integer*> Flow creation date (UTC timestamp).
* `last_modification_date`: <*integer*> last modification date (UTC timestamp).

## relationships

A flow object has the following relationships:

| Relationship      | Description                   | Return object type                          |
| ----------------- | ----------------------------- | ------------------------------------------- |
| `group`           | Group that owns the Flow.     | [Group](group-object.md)                   |
| `flow_executions` | The Flow's execution history. | [Flow Execution](flow-execution-object.md) |

---

← [tags](file-behaviour-summary-object/file-behaviour-object-tags.md) · [up](README.md) · [Flow Execution](flow-execution-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/flow-object>.*
