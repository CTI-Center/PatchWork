---
title: "Get an hourly IP address feed batch"
source: https://gtidocs.virustotal.com/reference/feedsip_addresseshourly2time
slug: feedsip_addresseshourly2time
section: reference
group: "IoC Feeds"
updatedAt: 2025-09-25T02:07:51.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Feeds](../README.md) › [IP intelligence feed](../ip-intelligence-feed.md) › Get an hourly IP address feed batch

---

# get-an-hourly-ip-address-feed-batch

> 🚧 Special privileges required
>
> IP feeds endpoints are only available to users with a IP feeds license. [Contact us](https://www.virustotal.com/gui/contact-us/) for more information.

This endpoint returns a single package containing all minutely packages returned in [`/feeds/ip_addresses/{time}`](feedsip_addressestime.md) endpoint for a given hour. The returned file is a .tar.bz2 file which contains the 60 minutely feeds for that hour.

The provided time argument must be in `YYYYMMDDhh` format. For example, time `2021012211` returns the batches correspoding to January 21st 2021 11:00 - 11:59 UTC. You can download batches up to 7 days old, and the most recent batch has always a 2 hours lag with respect with to the current time. This means that if the current time in UTC is T you can download batch T-2h but any more recent.

Successful calls to this endpoint will return a `302` redirect response to a URL from which the final batch file will be downloaded.

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
    "/feeds/ip_addresses/hourly/{time}": {
      "get": {
        "tags": [
          "IP intelligence feed"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "feedsip_addresseshourly2time",
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
        "summary": "Get an hourly IP address feed batch"
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

← [IP intelligence feed](../ip-intelligence-feed.md) · [up](../README.md) · [Get a minutely IP address feed batch](feedsip_addressestime.md) →

*Archived from <https://gtidocs.virustotal.com/reference/feedsip_addresseshourly2time>.*
