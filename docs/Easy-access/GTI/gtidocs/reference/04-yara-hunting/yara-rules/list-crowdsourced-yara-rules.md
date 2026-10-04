---
title: "List Crowdsourced YARA Rules"
source: https://gtidocs.virustotal.com/reference/list-crowdsourced-yara-rules
slug: list-crowdsourced-yara-rules
section: reference
group: "YARA Hunting"
updatedAt: 2025-09-25T02:04:55.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [YARA Hunting](../README.md) › [YARA Rules](../yara-rules.md) › List Crowdsourced YARA Rules

---

# list-crowdsourced-yara-rules

This endpoint lists the different Google Threat Intelligence's Crowdsourced YARA rules.

```json Example response
{
	"meta": {
		"cursor": "Ck8KDwoCbG0SCQjdvIy9kdv-AhI4ahFzfnZpcnVzdG90YWxjbG91ZHIjCxIIWWFyYVJ1bGUiFTAwM2UxYzUxZWZ8UEtfQVhBX2Z1bgwYACAB"
	},
	"data": [
		{
			"attributes": {
				"name": "PK_AXA_fun",
				"tags": [
					"AXA"
				],
				"matches": 0,
				"author": "Thomas Damonneville",
				"enabled": true,
				"rule": "rule PK_AXA_fun : AXA\n{\n    meta:\n        description = \"Phishing Kit impersonating AXA banque\"\n        licence = \"GPL-3.0\"\n        author = \"Thomas Damonneville\"\n        reference = \"\"\n        date = \"2023-05-02\"\n        comment = \"Phishing Kit - AXA - using a fun.php page\"\n\n    strings:\n        // the zipfile working on\n        $zip_file = { 50 4b 03 04 }\n        $spec_dir = \"css\"\n        $spec_dir2 = \"images\"\n        // specific file found in PhishingKit\n        $spec_file = \"detail.html\"\n        $spec_file2 = \"fun.php\"\n        $spec_file3 = \"fin.html\"\n        $spec_file4 = \"axa_pp_blanc.min.css\"\n\n    condition:\n        // look for the ZIP header\n        uint32(0) == 0x04034b50 and\n        // make sure we have a local file header\n        $zip_file and\n        // check for file\n        all of ($spec_file*) and\n        all of ($spec_dir*)\n}",
				"creation_date": 1682985600,
				"meta": [
					{
						"key": "description",
						"value": "Phishing Kit impersonating AXA banque"
					},
					{
						"key": "licence",
						"value": "GPL-3.0"
					},
					{
						"key": "author",
						"value": "Thomas Damonneville"
					},
					{
						"key": "reference",
						"value": ""
					},
					{
						"key": "date",
						"value": "2023-05-02"
					},
					{
						"key": "comment",
						"value": "Phishing Kit - AXA - using a fun.php page"
					}
				],
				"last_modification_date": 1683185194
			},
			"type": "yara_rule",
			"id": "003e1c51ef|PK_AXA_fun",
			"links": {
				"self": "https://www.virustotal.com/api/v3/yara_rules/003e1c51ef|PK_AXA_fun"
			}
		}
	],
	"links": {
		"self": "https://www.virustotal.com/api/v3/yara_rules?limit=1",
		"next": "https://www.virustotal.com/api/v3/yara_rules?cursor=Ck8KDwoCbG0SCQjdvIy9kdv-AhI4ahFzfnZpcnVzdG90YWxjbG91ZHIjCxIIWWFyYVJ1bGUiFTAwM2UxYzUxZWZ8UEtfQVhBX2Z1bgwYACAB&limit=1"
	}
}
```

The `filter` parameter allows to filter the rules according to the values of certain attributes. For example you can get only the enabled rules with `enabled:true`. With `name:foo` and `foo` you can search for rules having the word "foo" in their names or in their meta values. Notice however that this only works with full words (words delimited by non-alphanumeric characters), if the rule's name is "foobar" it won't appear if you filter with `name:foo`. You can combine multiple filters separating them with spaces, for example: `filter=enabled:true name:foo`.

All the accepted filters are: `author`, `creation_date`, `enabled`, `included_date`, `last_modification_date`, `name`, `tag`, `threat_category`.

The `order` parameters control the order in which rulesets are returned, accepted orders are: `matches`, `creation_date`, `included_date` and `modification_date`. You can prepend `+` and `-` suffixes to specify ascending and descending orders (examples: `name-`, `creation_date+`, ). If not suffix is specified the order is ascending by default.

# openapi-definition

```json
{
  "info": {
    "title": "YARA Hunting",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "YARA Rules"
    }
  ],
  "paths": {
    "/yara_rules": {
      "get": {
        "tags": [
          "YARA Rules"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "list-crowdsourced-yara-rules",
        "parameters": [
          {
            "description": "Maximum number of rules to retrieve",
            "in": "query",
            "name": "limit",
            "schema": {
              "default": 10,
              "format": "int32",
              "type": "integer",
              "maximum": 40,
              "minimum": 0
            }
          },
          {
            "description": "Return the rules matching the given criteria only",
            "in": "query",
            "name": "filter",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Sort order",
            "in": "query",
            "name": "order",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Continuation cursor",
            "in": "query",
            "name": "cursor",
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
        "summary": "List Crowdsourced YARA Rules"
      }
    }
  },
  "security": [],
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

← [YARA Rules](../yara-rules.md) · [up](../README.md) · [Get a Crowdsourced YARA rule](get-a-crowdsourced-yara-rule.md) →

*Archived from <https://gtidocs.virustotal.com/reference/list-crowdsourced-yara-rules>.*
