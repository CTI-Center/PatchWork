---
title: "Create a new report"
source: https://gtidocs.virustotal.com/reference/create-report
slug: create-report
section: reference
group: "Reports & Analysis"
updatedAt: 2026-04-10T11:30:34.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Reports & Analysis](../README.md) › [Reports](../reports.md) › Create a new report

---

# create-a-new-report

Use the following endpoint to create [Reports](../../17-api-objects/report-object.md). The data object must be passed within the request body. Upon creation, these reports are **private**; only the owner is authorized to view or modify them.

> ❗️
>
> This endpoint is currently in **Private Preview**.

The following request body template includes all available attributes. Before using it, please remove any mutually exclusive fields.

```json
{
  "data": {
    "type": "collection",
    "attributes": {
      "collection_type": "report",
      "name": "The name of your report",
      "description": "The description of your report",
      "content": "The content of your report",
      "link": "http://test.com",
      "alt_names": [
        "alternative_name_1",
        "alternative_name_2"
      ],
      "author": "Author name",
      "analyst_comment": "Analyst comment",
      "report_confidence": "Custom report confidence",
      "version": 1,
      "tlp": "GREEN",
      "tags": [
        "tag_a",
        "tag_b"
      ],
      "capabilities": [
        {
          "value": "capability_a",
          "confidence": "confirmed",
          "first_seen": 946684800,
          "last_seen": 1262304000,
          "description": "Some more context"
        }
      ],
      "detection_names": [
        {
          "value": "detection_name_a",
          "confidence": "unconfirmed",
          "first_seen": 946684800,
          "last_seen": 1262304000,
          "description": "Some more context"
        }
      ],
      "operating_systems": [
        {
          "value": "your os",
          "confidence": "possible",
          "first_seen": 946684800,
          "last_seen": 1262304000,
          "description": "Some more context"
        }
      ],
      "malware_roles": [
        {
          "value": "Sniffer",
          "confidence": "suspected",
          "first_seen": 946684800,
          "last_seen": 1262304000,
          "description": "Some more context"
        }
      ],
      "motivations": [
        {
          "value": "Hacktivism",
          "confidence": "blocklisted",
          "first_seen": 946684800,
          "last_seen": 1262304000,
          "description": "Some more context"
        }
      ],
      "sponsor_region": "ES",
      "source_region": "UK",
      "source_regions_hierarchy": [
        {
          "confidence": "unconfirmed",
          "country": "US",
          "first_seen": 946684800,
          "last_seen": 1262304000,
          "description": "Some more context"
        }
      ],
      "targeted_regions": [
        "JP",
        "DE"
      ],
      "targeted_regions_hierarchy": [
        {
          "confidence": "unconfirmed",
          "first_seen": 946684800,
          "last_seen": 1262304000,
          "description": "Some more context",
          "country": "JP"
        },
        {
          "confidence": "confirmed",
          "first_seen": 946684800,
          "last_seen": 1262304000,
          "description": "Some more context",
          "country": "FR"
        }
      ],
      "targeted_industries": [
        "Agriculture",
        "Mining"
      ],
      "targeted_industries_tree": [
        {
          "industry_group": "Agriculture",
          "confidence": "suspected",
          "first_seen": 946684800,
          "last_seen": 1262304000,
          "description": "Some more context"
        },
        {
          "industry_group": "Mining",
          "confidence": "confirmed"
        }
      ],
      "first_seen_details": [
        {
          "value": "946684800",
          "confidence": "suspected",
          "first_seen": 946684800,
          "last_seen": 1262304000
        }
      ],
      "last_seen_details": [
        {
          "value": "1262304000",
          "confidence": "confirmed",
          "first_seen": 946684800,
          "last_seen": 1262304000
        }
      ],
      "mitigations": [
        "mitigation_a",
        "mitigation_b"
      ],
      "technologies": [
        {
          "cpe": "Custom cpe",
          "cpe_title": "Custom title",
          "technology_name": "Custom technology",
          "vendor": "Custom vendor"
        }
      ],
      "targeted_informations": [
        "targeted_information_a",
        "targeted_information_b"
      ],
      "affected_systems": [
        "system_a",
        "system_b"
      ],
      "intended_effects": [
        "intended_effect_a",
        "intended_effect_b"
      ],
      "threat_scape": [
        "threat_scape_a",
        "threat_scape_b"
      ]
    },
    "relationships": {
      "associations": {
        "data": [
          {
            "type": "collection",
            "id": "threat-actor--9e6b1b9c-bc43-5c7b-a70e-23cbfe4b5bcf"
          },
          {
            "type": "collection",
            "id": "malware--5bd89727-4a3f-541f-9f64-044b87eb66e5"
          },
          {
            "type": "collection",
            "id": "malware--f872b3e0-c277-5716-baae-885a9c410398"
          },
          {
            "type": "collection",
            "id": "campaign--a84b13cd-886c-5597-816d-dd813b71417b"
          },
          {
            "type": "collection",
            "id": "fbb2387395df252e007ae0856ed4dc2ca6d5de734be2bc55707f93b13393756e"
          },
          {
            "type": "collection",
            "id": "vulnerability--mve-2026-9380"
          }
        ]
      },
      "files": {
        "data": [
          {
            "type": "file",
            "id": "d3efbfd26f392c1a87c95d26a79ff92911b1b58c84c72215e0c28929b07e2ae4"
          }
        ]
      },
      "domains": {
        "data": [
          {
            "type": "domain",
            "id": "google.com"
          }
        ]
      },
      "ip_addresses": {
        "data": [
          {
            "type": "ip_address",
            "id": "173.194.199.113"
          }
        ]
      },
      "urls": {
        "data": [
          {
            "type": "url",
            "url": "https://www.realhostx.com/Cloud/Socket/Adb.zip"
          },
          {
            "type": "url",
            "id": "d685d65bf7b7c5d736017d3f85e2617f326ac6651e4cb1ac594b66eeff6e9b8b"
          }
        ]
      },
      "reports": {
        "data": [
          {
            "type": "collection",
            "id": "report--26-10013924"
          }
        ]
      },
      "attack_techniques": {
        "data": [
          {
            "type": "attack_technique", 
            "id": "T1087"
          }
        ]
      }
    }
  }
}
```

> 🚧
>
> Some regions and industries related attributes, require you to choose between a **Simple** or **Complex** (**with extra context**) format. Please note that these formats are mutually exclusive for each category; you must use either the simple field (e.g., source_region) or the complex field (e.g., source_regions_hierarchy), **but never both**.
>
> * _Source_: `source_region` OR `source_regions_hierarchy` (if you want to add extra context)
> * _Targeted Regions_: `targeted_regions` OR `targeted_regions_hierarchy` (if you want to add extra context)
> * _Targeted Industries_: `targeted_industries` OR `targeted_industries_tree` (if you want to add extra context)

## special-attributes

**Required attributes are**:

* `collection_type`: `report`
* `name`: The name of the report
* `description`: The description of the report

**Attributes with fixed values (enums):**

* `tlp`: Valid values are `CLEAR`, `GREEN`, `AMBER` and `RED`.
* `x.confidence`: Valid values are `confirmed`, `unconfirmed`, `possible`, `suspected`, `crowdsourced` and `blocklisted`.
* `x.country`: This field can be set to any **ISO country code** or **country name**.
* `targeted_industries_tree.industry_group`: Valid values are listed [here](https://gtidocs.readme.io/docs/threat-intelligence-objects-modifiers-values) as **targeted\_industry\_group**.
* `malware_roles.value`: Valid values are listed [here](https://gtidocs.readme.io/docs/threat-intelligence-objects-modifiers-values) as **malware\_role**.
* `motivations.value`: Valid values are listed [here](https://gtidocs.readme.io/docs/threat-intelligence-objects-modifiers-values) as **motivation**.
* `source_region`, `sponsor_region` and `targeted_regions`: Valid values are listed [here](https://gtidocs.readme.io/docs/threat-intelligence-objects-modifiers-values) as **source\_region** or **targeted\_region**.

**Other attributes**:

* `x.first_seen` and `x.last_seen`: Valid values are numerical UTC timestamps.
* `relationships.urls[x]`: Each object must contain either a `url` field (the full URL string) or an `id` field (URL the hash identifier).

For other dictionary-based attributes, simply omit any fields you do not wish to explicitly set. For example, if `first_seen` or `last_seen` data is unavailable, you can exclude them from the request entirely as follows:

```json
"targeted_regions_hierarchy": [
  {
    "confidence": "unconfirmed",
    "country": "US"
  }
]
```

Use the first option instead of:

```json
"targeted_regions_hierarchy": [
  {
    "confidence": "unconfirmed",
    "country": "US",
    "first_seen": null,
    "last_seen": null
  }
]
```

# examples

Create a testing report with name, description, motivations, source region, author,  analyst comment and "CLEAR" tlp.

```python

import requests
url = "https://www.virustotal.com/api/v3/collections"

payload = {
    "data": {
        "type": "collection",
        "attributes": {
            "collection_type": "report",
            "name": "My very first report",
            "description": "This is the result of a new creation reports endpoint.",
            "content": (
                "# Endpoint Ingestion Test: \n "
                "Cyber ipsum dolor sit amet, **high-priority telemetry data**. "
                "Integrated threat intelligence indicates a suspicious **POST** request to the backend repository. "
                "Packet inspection reveals _encrypted payloads_ within the request body. "
                "Ensure all metadata attributes—specifically _**source_regions**_ and _**targeted_industries**_—align "
                "with the predefined TLP schemas. \n "
                "- Unauthorized access attempts were mitigated by the firewall configuration.\n "
                "- System logs confirm that any malformed dictionary attributes were omitted during the resource creation process.\n "
                "- Authentication tokens must be regenerated if the Secret_Token expires during the deployment phase."
            ),
            "motivations": [
                {
                    "value": "Influence",
                    "confidence": "possible"
                }
            ],
            "source_region": "ES",
            "author": "TPG team",
            "analyst_comment": "Validation complete",
            "tlp" : "CLEAR"
        }
    }
}
headers = {
    "accept": "application/json",
    "x-apikey": <api-key>,
    "content-type": "application/json"
}
response = requests.post(url, json=payload, headers=headers)
```

# openapi-definition

```json
{
  "info": {
    "title": "Reports & Analysis",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "paths": {
    "/collections": {
      "post": {
        "description": "",
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          },
          "400": {
            "description": "400",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          }
        },
        "parameters": [
          {
            "in": "header",
            "name": "x-apikey",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Your API key."
          }
        ],
        "operationId": "post_collections",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "data": {
                    "type": "string",
                    "description": "Report object.",
                    "format": "json"
                  }
                },
                "required": [
                  "data"
                ]
              }
            }
          }
        }
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

← [Get a report](get-report.md) · [up](../README.md) · [Delete a report](delete-report.md) →

*Archived from <https://gtidocs.virustotal.com/reference/create-report>.*
