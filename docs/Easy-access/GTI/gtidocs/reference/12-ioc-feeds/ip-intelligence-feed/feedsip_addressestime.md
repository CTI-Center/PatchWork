---
title: "Get a minutely IP address feed batch"
source: https://gtidocs.virustotal.com/reference/feedsip_addressestime
slug: feedsip_addressestime
section: reference
group: "IoC Feeds"
updatedAt: 2025-09-25T02:07:52.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Feeds](../README.md) › [IP intelligence feed](../ip-intelligence-feed.md) › Get a minutely IP address feed batch

---

# get-a-minutely-ip-address-feed-batch

> 🚧 Special privileges required
>
> IP feeds endpoints are only available to users with a IP feeds license. [Contact us](https://www.virustotal.com/gui/contact-us/) for more information.

With this endpoint you can download an individual one-minute batch by providing a time consisting of a string with format `YYYYMMDDhhmm`. Time `201912010802` will return the batch corresponding to December 1st, 2019 08:02 UTC. You can download batches up to 7 days old, and the most recent batch has always a 60 minutes lag with respect with to the current time. This means that if the current time in UTC is `T` you can download batch `T-60m` but not `T-59m` or any more recent.

Successful calls to this endpoint will return a `302` redirect response to a URL from which the final batch file will be downloaded.

> 🚧 Missing batches
>
> Missing batches are rare, but still can happen occasionally. This doesn't mean that you are losing any IP addresses in the feed, it just means that no batches were generated on a specific minute. The client code should be ready to accept a `404` error while retrieving a batch and proceed with the following one. However, receiving multiple `404` errors in a row for consecutive batches shouldn't happen and should be treated as an error condition.

The downloaded file is a bzip2 compressed UTF-8 text file contains one JSON structure per line, where the structure represents a URL object as returned by the [GET /ip\_addresses/\{ip}](../../03-ioc-investigation/ip-addresses/ip-info.md) endpoint.

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
      "name": "IP intelligence feed"
    }
  ],
  "paths": {
    "/feeds/ip_addresses/{time}": {
      "get": {
        "tags": [
          "IP intelligence feed"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "feedsip_addressestime",
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
        "summary": "Get a minutely IP address feed batch"
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

← [Get an hourly IP address feed batch](feedsip_addresseshourly2time.md) · [up](../README.md) · [URL intelligence feed](../url-intelligence-feed.md) →

*Archived from <https://gtidocs.virustotal.com/reference/feedsip_addressestime>.*
