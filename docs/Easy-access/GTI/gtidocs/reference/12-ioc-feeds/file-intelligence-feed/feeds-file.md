---
title: "Get a per-minute file feed batch"
source: https://gtidocs.virustotal.com/reference/feeds-file
slug: feeds-file
section: reference
group: "IoC Feeds"
updatedAt: 2025-09-25T02:07:41.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Feeds](../README.md) › [File intelligence feed](../file-intelligence-feed.md) › Get a per-minute file feed batch

---

# get-a-per-minute-file-feed-batch

> 🚧 Special privileges required
>
> File feeds endpoints are only available to users with a File feeds license. [Contact us](https://www.virustotal.com/gui/contact-us/) for more information.

With this endpoint you can download an individual one-minute batch by providing a `time` consisting of a string with format `YYYYMMDDhhmm`. Time `201912010802` will return the batch corresponding to December 1st, 2019 08:02 UTC. You can download batches up to 7 days old, and the most recent batch has always a 60 minutes lag respecting to the current time. This means that if the current time in UTC is `T` you can download batch `T-60m` but not `T-59m` or any more recent.

Successful calls to this endpoint will return a `302` redirect response to a URL from which the final batch file will be downloaded.

> 🚧 Missing batches
>
> Missing batches are rare, but still can happen occasionally. This doesn't mean that you are losing any files in the feed, it just means that no batches were generated on a specific minute. The client code should be ready to accept a `404` error while retrieving a batch and proceed with the following one. However, receiving multiple `404` errors in a row for consecutive batches shouldn't happen and should be treated as an error condition.

The downloaded file is a bzip2 compressed UTF-8 text file contains one JSON structure per line, where the structure represents a file object as returned by the [GET /files/\{id}](../../03-ioc-investigation/files/file-info.md) endpoint. Besides the standard attributes usually found in all file objects, two additional context attributes are also included: `download_url` and `submitter`. The `download_url` attribute is a link that can be used to download the file itself, while `submitter` is a dictionary with lossy-ciphered non-identifiable information about who submitted the file to Google Threat Intelligence. Notice however that `submitter` is not present in all files, it will be absent when files are submitted via the web interface without triggering a new analysis due to recent submissions, or when files are re-analyzed by Google TI without being submitted by some external user.

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
    "/feeds/files/{time}": {
      "get": {
        "tags": [
          "File intelligence feed"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "feeds-file",
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
              "text/plain": {
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
        "summary": "Get a per-minute file feed batch"
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

← [Get a hourly file feed batch](feeds-file-hourly.md) · [up](../README.md) · [Download a file published in the file feed](file-feed-download.md) →

*Archived from <https://gtidocs.virustotal.com/reference/feeds-file>.*
