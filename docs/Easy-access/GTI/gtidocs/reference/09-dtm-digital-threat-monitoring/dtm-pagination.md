---
title: "DTM Pagination"
source: https://gtidocs.virustotal.com/reference/dtm-pagination
slug: dtm-pagination
section: reference
group: "DTM (DIGITAL THREAT MONITORING)"
updatedAt: 2025-09-25T00:38:10.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [DTM (DIGITAL THREAT MONITORING)](README.md) › DTM Pagination

---

# dtm-pagination

The REST API supports pagination of results in the form of scrolling. With scrolling, you can page through your results page-by-page, but you cannot jump ahead multiple pages, or back in your page results. The APIs that support LISTing resources (for example, `GET /monitors` or`GET /alerts`) all support pagination.

The APIs that support pagination also support query parameters to define the pagination behavior. The following query parameters are most common:

* `life`: The amount of time in seconds or minutes to keep the pagination context open for. By default its `1m`. If you haven’t fetched next page of results within this time period; the page context is closed and cannot be used. Simply LIST the resources again to restart. Currently the max life is `10m`.
* `sort`: The field to sort the results by. For example, to sort the results by their updated timestamp, you can use `sort=updated_at`. You can also sort by `name` or `id`, for example. The default is `created_at`.
* `order`: The sort order of the results. The possible values are `asc` and `desc` for ascending and descending respectively. The default is `desc`. This order applies the `sort` field.
* `size`: The number of resources to include in each page of results. The default is `10`.
* `since`: Used for filtering the list based on `created_at` date ranges. This is an RFC3339 timestamp that specifies the starting date range for the results. If not specified, all results are returned.
* `until`: Used for filtering the list based on `created_at` date ranges. This is an RFC3339 timestamp that specifies the ending date range for the results. If not specified, all results are returned.

The API uses the [HTTP Link Header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Link) to relay the URI to the next page of results when pagination. The `rel` used in the Link is `next` and will only be included when there’s another page of results. API consumers should use the Link URI exactly as provided in the Link header, as it includes information about your pagination context. No other query parameters can be used when fetching subsequent pages through the Link header URI.

To illustrate pagination, let’s paginate through the two Monitors we created previously. For this example, we’ll paginate the `/monitors` API and tell it to only return one Monitor per page (just for illustration purposes) using the `size` query parameter:

```
curl -k -s -H 'Accept: application/json' -H "x-apikey: ${GTI_API_KEY}" "https://www.virustotal.com/api/v3/dtm/monitors?size=1"
```

This returns a list with our most recent Monitor:

```
{
    "monitors":[
        {
            "id":"cad5n8o5cdt77b0idjlg",
            "name":"army navy us dark",
            "description":"Monitor army or navy for dark activity in the united states",
            "enabled":true,
            "doc_condition":{
                "operator":"all",
                "topic":"match_conditions",
                "match":[
                    {
                        "operator":"must_equal",
                        "topic":"group_brand",
                        "match":[
                            "army",
                            "navy"
                        ]
                    },
                    {
                        "operator":"must_equal",
                        "topic":"group_location",
                        "match":[
                            "us",
                            "usa",
                            "united states"
                        ]
                    },
                    {
                        "operator":"must_equal",
                        "topic":"keyword",
                        "match":[
                            "hack",
                            "password",
                            "root",
                            "malware",
                            "sell",
                            "ransomware"
                        ]
                    }
                ]
            },
            "created_at":"2022-06-03T19:06:11.086Z",
            "updated_at":"2022-06-03T19:06:11.086Z",
            "email_notify_enabled":false,
            "email_notify_immediate":false
        }
    ]
}

```

The response Headers also include the following `Link` header:

```
 <https://www.virustotal.com/api/v3/dtm/monitors?page=cad5n8o5cdt77b0idjlg>; rel="next"
```

If we use the `Link` header URI, we can then fetch our next page of results:

```
curl -k -s -H 'Accept: application/json' -H "x-apikey: ${GTI_API_KEY}" "https://www.virustotal.com/api/v3/dtm/monitors?page=cad5n8o5cdt77b0idjlg"
```

Which returns a list with our other Monitor:

```
{
    "monitors":[
        {
            "id":"cad5l885cdt77b0idivg",
            "name":"monitor mandiant.com",
            "description":"monitor mandiant.com domain for suspicious keywords",
            "enabled":true,
            "doc_condition":{
                "operator":"all",
                "topic":"match_conditions",
                "match":[
                    {
                        "operator":"must_equal",
                        "topic":"group_network",
                        "match":[
                            "mandiant.com"
                        ]
                    },
                    {
                        "operator":"must_contain",
                        "topic":"keyword",
                        "match":[
                            "hack",
                            "password",
                            "root",
                            "malware",
                            "sell",
                            "ransomware"
                        ]
                    }
                ]
            },
            "created_at":"2022-06-03T19:01:53.442Z",
            "updated_at":"2022-06-03T19:01:53.442Z",
            "email_notify_enabled":false,
            "email_notify_immediate":false
        }
    ]
}
```

This time the response does not include the `Link` header, because there is not another page of Monitors to scroll through.

---

← [Catalog Stats](../08-asm-attack-surface-management/library/get_library-catalog-stats.md) · [up](README.md) · [DTM Alerts](dtm-alerts.md) →

*Archived from <https://gtidocs.virustotal.com/reference/dtm-pagination>.*
