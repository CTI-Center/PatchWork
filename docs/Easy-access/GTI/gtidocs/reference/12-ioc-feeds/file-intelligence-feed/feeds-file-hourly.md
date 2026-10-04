---
title: "Get a hourly file feed batch"
source: https://gtidocs.virustotal.com/reference/feeds-file-hourly
slug: feeds-file-hourly
section: reference
group: "IoC Feeds"
updatedAt: 2025-09-25T02:07:40.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Feeds](../README.md) › [File intelligence feed](../file-intelligence-feed.md) › Get a hourly file feed batch

---

# get-a-hourly-file-feed-batch

> 🚧 Special privileges required
>
> File feeds endpoints are only available to users with a File feeds license. [Contact us](https://www.virustotal.com/gui/contact-us/) for more information.

This endpoint returns a single package containing all minutely packages returned in [/feeds/files/\{time}](feeds-file.md) endpoint for a given hour. The returned file is a `.tar.bz2` file which contains the 60 minutely feeds for that hour.

The provided `time` argument must be in `YYYYMMDDhh` format. For example, time `2021012211` returns the batches correspoding to January 21st 2021 11:00 - 11:59 UTC. You can download batches up to 7 days old, and the most recent batch has always a 2 hours lag with respect with to the current time. This means that if the current time in UTC is T you can download batch T-2h but any more recent.

Successful calls to this endpoint will return a `302` redirect response to a URL from which the final batch file will be downloaded.

The downloaded file is a bzip2 tar file which include 60 files, one for each minute, these are UTF-8 text file which contains one JSON structure per line, where the structure represents a file object as returned by the GET /files/\{id} endpoint. Besides the standard attributes usually found in all file objects, two additional context attributes are also included: download\_url and submitter. The download\_url attribute is a link that can be used to download the file itself, while submitter is a dictionary with lossy-ciphered non-identifiable information about who submitted the file to Google Threat Intelligence. Notice however that submitter is not present in all files as some files are re-analyzed by Google TI without being submitted by some external user.

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
      "name": "File intelligence feed"
    }
  ],
  "paths": {
    "/feeds/files/hourly/{time}": {
      "get": {
        "tags": [
          "File intelligence feed"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "feeds-file-hourly",
        "parameters": [
          {
            "description": "A string in format YYYYMMDDhh",
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
                    "value": "{}"
                  }
                },
                "schema": {
                  "properties": {},
                  "type": "object"
                }
              }
            },
            "description": "200"
          },
          "400": {
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "properties": {},
                  "type": "object"
                }
              }
            },
            "description": "400"
          }
        },
        "security": [],
        "summary": "Get a hourly file feed batch"
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

← [File intelligence feed](../file-intelligence-feed.md) · [up](../README.md) · [Get a per-minute file feed batch](feeds-file.md) →

*Archived from <https://gtidocs.virustotal.com/reference/feeds-file-hourly>.*
