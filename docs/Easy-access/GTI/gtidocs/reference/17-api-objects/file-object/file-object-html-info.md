---
title: "html_info"
source: https://gtidocs.virustotal.com/reference/file-object-html-info
slug: file-object-html-info
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:42:07.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › html_info

---

# html_info

Information from HTML files

`html_info` provides information extracted from HTML files:

* `hrefs`: <*list of strings*>  all `href` attributes found in all tags.
* `iframes`: <*list of dictionaries*> list containing all `iframe` tags. Every item contains:
  * `attributes`: <*dictionary*> the tag's attributes.
* `meta`: <\*list of dictionaries`> contains all `meta\` tags. Every item contains:
  * `content`: <*list of strings*> content of all `meta` tags having that name.
  * `name`: <*string*> name of that `meta` tag.
* `scripts`: <*list of dictionaries*> list containing all `script` tags. Every item contains:
  * `attributes`: <*dictionary*> the tag's attributes.
  * `sha256`: <*string*> in case the script is embedded within the script, this attribute contains its sha256 checksum.
* `title`: <*string*> website's title.
* `trackers`: <*list of dictionaries*> found trackers in the document. Every item contains:
  * `name`: <*string*> tracker name.
  * `trackers`: <*list of dictionaries*> found trackers. Every item contains:
    * `tracker_id`: <*string*> tracker campaign/client ID.
    * `url`: <*string*> script URL.

```json html_info
{
  "data": {
    "attributes": {
      "html_info": {
        "hrefs": [
          "<strings>"
        ],
        "meta": [
          {
            "content": [
              "<strings>"
            ],
            "name": "<string>"
          }
        ],
        "scripts": [
          {
            "attributes": {
              "<string>": "<string>"
            }
            "sha256": "<string>"
          }
        ],
        "title": "<string>",
        "trackers": [
          {
            "name": "<string>",
            "trackers": [
              {
                "tracker_id": "<string>",
                "url": "<string>"
              }
            ]
          }
        ]
      }
    }
  }
}
```
```json Example
{
  "data": {
    "attributes": {
      "html_info": {
        "hrefs": [
          "/images/favicon.ico",
          "https://fonts.googleapis.com/icon?family=Material+Icons",
          "http://example.com/css/style1.css"
        ],
        "meta": [
          {
            "content": [
              "ID"
            ],
            "name": "geo.region"
          },
          {
            "content": [
              "Indonesia"
            ],
            "name": "geo.placename"
          },
          {
            "content": [
              "Coolest webpage ever done before"
            ],
            "name": "description"
          }
        ],
        "scripts": [
          {
            "attributes": {
              "src": "http://example.com/js/jquery-latest.js"
            }
          },
          {
            "attributes": {
              "src": "http://example.com/js/my_js.js",
              "type": "text/javascript"
            }
          },
          {
            "attributes": {
              "type": "text/javascript"
            },
            "sha256": "0df532883768378d35b30e7e32eb35b7231d333bec8c063a2d396c53305d3d96"
          }
        ],
        "title": "A very cool website",
        "trackers": [
          {
            "name": "Google Tag Manager",
            "trackers": [
              {
                "tracker_id": "UA-123331334-11",
                "url": "https://www.googletagmanager.com/gtag/js?id=UA-123331334-11"
              }
            ]
          }
        ]
      }
    }
  }
}
```

---

← [monitor_info](file-object-monitor-info.md) · [up](../README.md) · [🔀 itw_ips](file-object-itw-ips.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-html-info>.*
