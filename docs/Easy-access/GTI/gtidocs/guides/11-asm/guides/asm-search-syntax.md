---
title: "Search Syntax for Attack Surface Management"
source: https://gtidocs.virustotal.com/docs/asm-search-syntax
slug: asm-search-syntax
section: guides
group: "ASM"
updatedAt: 2025-09-25T17:11:00.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [ASM](../README.md) › [Guides](../guides.md) › Search Syntax for Attack Surface Management

---

# search-syntax-for-attack-surface-management

The Attack Surface Management (ASM) search syntax operates under a few simple rules:

* Queries of different keywords are AND'd

  > 💡
  >
  > For example: `acme.com port_tcp:80`\
  > Read this as "any Entity with acme.com in the name AND port 80 TCP open"

* Queries of the same keyword are OR'd

  > 💡
  >
  > For example: `acme.com port_tcp:80 port_tcp:443`\
  > Read this as "any Entity with acme.com in the name AND (port 80 TCP OR port 443 TCP open)"

* For negative queries, use `!` (NOT) before the search parameter, or search term

  > 💡
  >
  > For example: `type:!uri`\
  > Read this as "any type but NOT uri"

  > ℹ️
  >
  > The `!` (NOT) works in Issues, Entities, and Technologies but does not work with
  >
  > * Specific date filters like `last_seen_after`, `last_seen_before`, and `first_seen_after`
  > * Collection filters

* The default search field (when no keyword is specified) is the item's "name" (for each of Entity, Issue, and Technology search)

## search-keywords

When searching on the **Issues**, **Entities**, and **Technologies** pages, you can create sophisticated queries using the keyword search, in addition to regular text searches. Accepted search terms together with their applicability on the **Issues**, **Entities**, and **Technologies** pages are defined below.

| Search Keyword          | Pretty Text  <br/> (if different than keyword) | Input                                                                                                                                                                                                                                  | Issues | Entities | Technologies |
| ----------------------- | ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | -------- | ------------ |
| key: `collection`       |                                                | Select from Your Collections                                                                                                                                                                                                           | ✔      | ✔        |              |
| key: `confidence`       |                                                | Confirmed, Potential                                                                                                                                                                                                                   | ✔      |          |              |
| key: `entity_type`      | Entity Type                                    | Text                                                                                                                                                                                                                                   | ✔      |          |              |
| key: `entity_name`      | Entity Name                                    | Text                                                                                                                                                                                                                                   | ✔      |          | ✔            |
| key: `last_seen_after`  | Seen after                                     | YYYY-MM-DD, `last_scan_count_NUMBER` (where `NUMBER` = 1-10)                                                                                                                                                                           | ✔      | ✔        | ✔            |
| key: `last_seen_before` | Seen before                                    | YYYY-MM-DD, `last_scan_count_NUMBER` (where `NUMBER` = 1-10)                                                                                                                                                                           | ✔      | ✔        | ✔            |
| key: `first_seen_after` | First seen after                               | YYYY-MM-DD, `last_scan_count_NUMBER` (where `NUMBER` = 1-10)                                                                                                                                                                           | ✔      | ✔        | ✔            |
| key: `scoped`           | Scoped                                         | True, False, Both                                                                                                                                                                                                                      | ✔      | ✔        |              |
| key: `severity`         |                                                | Critical/1, High/2, Medium/3, Low/4, Informational/5                                                                                                                                                                                   | ✔      |          |              |
| key: `severity_lt`      | Severity is less than                          | 1 - 5                                                                                                                                                                                                                                  | ✔      |          |              |
| key: `severity_gt`      | Severity is greater than                       | 1 - 5                                                                                                                                                                                                                                  | ✔      |          |              |
| key: `status_new`       | Issues                                         | Open, Closed                                                                                                                                                                                                                           | ✔      |          |              |
| key: `status`           | Status is                                      | open\_triaged, open\_in\_progress, closed\_mitigated, closed\_resolved, closed\_duplicate, closed\_out\_of\_scope, closed\_benign, closed\_risk\_accepted, closed\_false\_positive, closed\_no\_reproduce, closed\_tracked\_externally | ✔      |          |              |
| key: `type`             |                                                | Text                                                                                                                                                                                                                                   |        | ✔        |              |
| key: `name`             |                                                | Text                                                                                                                                                                                                                                   |        | ✔        | ✔            |
| key: `tag`              |                                                | Text                                                                                                                                                                                                                                   | ✔      | ✔        |              |
| key: `country`          |                                                | Two letter code, *ex:* FR                                                                                                                                                                                                              |        | ✔        |              |
| key: `hidden`           |                                                | True, False, Both                                                                                                                                                                                                                      |        | ✔        |              |
| key: `http_code`        |                                                | Text                                                                                                                                                                                                                                   |        | ✔        |              |
| key: `http_auth`        |                                                | True, False                                                                                                                                                                                                                            |        | ✔        |              |
| key: `http_auth_basic`  | Has basic auth                                 | True, False                                                                                                                                                                                                                            |        | ✔        |              |
| key: `http_auth_ntlm`   |                                                | True, False                                                                                                                                                                                                                            |        | ✔        |              |
| key: `http_title`       |                                                | Text                                                                                                                                                                                                                                   |        | ✔        |              |
| key: `http_forms`       | Form detected on URI                           | True, False                                                                                                                                                                                                                            |        | ✔        |              |
| key: `technology`       |                                                | Text                                                                                                                                                                                                                                   |        | ✔        |              |
| key: `network`          |                                                | Text                                                                                                                                                                                                                                   |        | ✔        |              |
| key: `port_tcp`         |                                                | Text                                                                                                                                                                                                                                   |        | ✔        |              |
| key: `port_udp`         |                                                | Text                                                                                                                                                                                                                                   |        | ✔        |              |
| key: `issue_count_lt`   | Has issue count less than                      | Number                                                                                                                                                                                                                                 |        | ✔        |              |
| key: `issue_ count_gt`  | Has issue count greater than                   | Number                                                                                                                                                                                                                                 |        | ✔        |              |
| key: `cpe`              |                                                | Text                                                                                                                                                                                                                                   |        | ✔        | ✔            |
| key: `label`            |                                                | Text                                                                                                                                                                                                                                   |        |          | ✔            |
| key: `cpe_type`         | CPE Type                                       | application, service, hardware, os                                                                                                                                                                                                     |        |          | ✔            |
| key: `product`          |                                                | Text                                                                                                                                                                                                                                   |        |          | ✔            |
| key: `vendor`           |                                                | Text                                                                                                                                                                                                                                   |        |          | ✔            |

---

← [Analyzing SSL/TLS Issues](analyzing-ssltls-issues.md) · [up](../README.md) · [Opt Out of Attack Surface Management Scanning](asm-opt-out.md) →

*Archived from <https://gtidocs.virustotal.com/docs/asm-search-syntax>.*
