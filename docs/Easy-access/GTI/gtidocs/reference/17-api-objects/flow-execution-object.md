---
title: "Flow Execution"
source: https://gtidocs.virustotal.com/reference/flow-execution-object
slug: flow-execution-object
section: reference
group: "API OBJECTS"
updatedAt: 2026-08-03T15:08:56.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Flow Execution

---

# flow-execution

Information about Agentic Flow Executions

> 🚧 Special privileges required
>
> Flow Executions are only available to users with the Google Threat Intelligence (Google TI) Enterprise or Enterprise Plus licenses, and require AI features to be enabled in your group settings.

A **Flow Execution** object represents a single run of a [Flow](flow-object.md), created automatically on the Flow's trigger or manually via *Run a Flow now*. The object `type` is `flow_execution`. Executions are read-only through the API except for cancellation.

## object-attributes

A flow execution object contains the following attributes:

* `flow_id`: <*string*> id of the Flow this execution belongs to.
* `status`: <*string*> overall status of the run. One of `EXECUTION_STATUS_RUNNING`, `EXECUTION_STATUS_COMPLETED`, `EXECUTION_STATUS_FAILED`, `EXECUTION_STATUS_CANCELLED`, `EXECUTION_STATUS_PAUSED`, `EXECUTION_STATUS_TIMEOUT`.
* `duration_seconds`: <*integer*> total wall-clock duration of the run in seconds.
* `steps`: <*list of dictionaries*> per-node execution steps, written by the backend as the Flow runs. Each step has:
  * `step_id`: <*string*> step identifier.
  * `node_id`: <*string*> id of the node this step ran.
  * `node_type`: <*string*> type of the node (see [Flow](flow-object.md) node types).
  * `status`: <*string*> step status. One of `STEP_STATUS_PENDING`, `STEP_STATUS_QUEUED`, `STEP_STATUS_IN_PROGRESS`, `STEP_STATUS_SUCCESS`, `STEP_STATUS_FAILURE`, `STEP_STATUS_SKIPPED`, `STEP_STATUS_RETRIED`, `STEP_STATUS_TIMEOUT`, `STEP_STATUS_CANCELLED`.
  * `input_json`: <*string*> JSON-encoded input passed to the node.
  * `output_json`: <*string*> JSON-encoded generic output of the node.
  * `enqueued_at`: <*integer*> when the step was enqueued (UTC timestamp).
  * `started_at`: <*integer*> when the step started (UTC timestamp).
  * `ended_at`: <*integer*> when the step ended (UTC timestamp).
  * `duration_seconds`: <*integer*> step duration in seconds.
  * `error_message`: <*string*> error detail when the step failed.
  * `run_prompt_output`: <*dictionary*> typed output for a Run Prompt node.
    * `session_id`: <*string*> Agentic session created for the prompt.
    * `gti_agentic_response`: <*string*> the agent's response text.
  * `send_email_output`: <*dictionary*> typed output for a Send Email node.
    * `dispatched`: <*boolean*> whether the email was dispatched.
  * `run_saved_search_output`: <*dictionary*> typed output for a Run Saved Search node.
    * `match_count`: <*integer*> number of matched items.
    * `matched_items`: <*list of strings*> identifiers of the matched items.
* `creation_date`: <*integer*> execution creation date (UTC timestamp).
* `last_modification_date`: <*integer*> last modification date (UTC timestamp).

## relationships

A flow execution object has the following relationships:

| Relationship    | Description                                   | Return object type        |
| --------------- | --------------------------------------------- | ------------------------- |
| `flow`          | The current parent Flow.                      | [Flow](flow-object.md)   |
| `flow_snapshot` | The Flow definition frozen at execution time. | [Flow](flow-object.md)   |
| `owner`         | User who triggered the execution.             | [User](user-object.md)   |
| `group`         | Group that owns the execution.                | [Group](group-object.md) |

---

← [Flow](flow-object.md) · [up](README.md) · [Graphs](graph-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/flow-execution-object>.*
