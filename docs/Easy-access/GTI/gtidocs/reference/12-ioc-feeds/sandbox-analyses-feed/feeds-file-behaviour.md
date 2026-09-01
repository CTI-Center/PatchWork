---
title: "Get a per-minute file behaviour feed batch"
source: https://gtidocs.virustotal.com/reference/feeds-file-behaviour
slug: feeds-file-behaviour
section: reference
group: "IoC Feeds"
updatedAt: 2025-09-25T02:07:44.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Feeds](../README.md) › [Sandbox analyses feed](../sandbox-analyses-feed.md) › Get a per-minute file behaviour feed batch

---

# get-a-per-minute-file-behaviour-feed-batch

> 🚧 Special privileges required
>
> Sandbox analyses feeds endpoints are only available to users with a Sandbox feeds license. [Contact us](https://www.virustotal.com/gui/contact-us/) for more information.

With this endpoint you can download an individual one-minute batches by providing a `time` consisting of a string with format `YYYYMMDDhhmm`. Time `201912010802` will return the batch corresponding to December 1st, 2019 08:02 UTC. You can download batches up to 7 days old, and the most recent batch has always a 60 minutes lag with respect to the current time. This means that if the current time in UTC is `T` you can download batch `T-60m` but not `T-59m` or any more recent.

Successful calls to this endpoint will return a `302` redirect response to a URL from which the final batch file will be downloaded.

> 🚧 Missing batches
>
> Missing batches are rare, but still can happen occasionally. This doesn't mean that you are losing any files in the feed, it just means that no batches were generated on a specific minute. The client code should be ready to accept a `404` error while retrieving a batch and proceed with the following one. However, receiving multiple `404` errors in a row for consecutive batches shouldn't happen and should be treated as an error condition.

The downloaded file is a bzip2 compressed UTF-8 text file containing one JSON structure per line, where the structure represents a FileBehaviour object as returned by the [GET /files/\{id}/behaviour](../../03-ioc-investigation/files/files-relationships.md) endpoint and is defined by [FileBehaviourSummary Object](../../17-api-objects/file-behaviour-summary-object.md).

The FileBehaviour object will contain an extra attribute (`context_attributes`), which is a JSON structure that contains links for downloading the PCAP, HTML, EVTX and memdump files generated in the analysis through our API without consuming your quota (bear in mind that you will have to use your API Key and add it to the request headers in order to get access to the behaviour reports pointed by those two links).

```json Entry line structure
{
  "attributes": <FileBehaviour object attributes>,
  "context_attributes": {
    "file_md5": "<string>",
    "file_sha1": "<string>",
    "file_type_tag": "<string>",
    "html_report": "https://www.virustotal.com/api/v3/feeds/file-behaviours/<TOKEN>/html",
    "pcap": "https://www.virustotal.com/api/v3/feeds/file-behaviours/<TOKEN>/pcap",
    "evtx": "https://www.virustotal.com/api/v3/feeds/file-behaviours/<TOKEN>/evtx",
    "memdump": "https://www.virustotal.com/api/v3/feeds/file-behaviours/<TOKEN>/memdump"
  },
  "id": "<SHA256_Sandbox name>",
  "type": "file_behaviour",
  "relationshiops": {...},
  "links": {...} 
}
```

# openapi-definition

```json
{
  "components": {
    "securitySchemes": {
      "sec0": {
        "in": "header",
        "name": "x-apikey",
        "type": "apiKey"
      }
    }
  },
  "info": {
    "title": "IoC Feeds",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Sandbox analyses feed"
    }
  ],
  "paths": {
    "/feeds/file_behaviours/{time}": {
      "get": {
        "tags": [
          "Sandbox analyses feed"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "feeds-file-behaviour",
        "parameters": [
          {
            "description": "A string in format YYYYMMDDhhmm",
            "in": "path",
            "name": "time",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Your API key",
            "in": "header",
            "name": "x-apikey",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": ""
                  }
                }
              }
            },
            "description": "200"
          }
        },
        "security": [],
        "summary": "Get a per-minute file behaviour feed batch"
      }
    }
  },
  "security": [
    {
      "sec0": []
    }
  ],
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3"
    }
  ],
  "x-readme": {
    "explorer-enabled": true,
    "headers": [],
    "proxy-enabled": false,
    "samples-enabled": true
  }
}
```

---

← [Get an hourly file behaviour feed batch](feeds-file-behaviour-hourly.md) · [up](../README.md) · [Get the EVTX file generated during a file’s behavior analysis](file-behaviour-feed-evtx.md) →

*Archived from <https://gtidocs.virustotal.com/reference/feeds-file-behaviour>.*
