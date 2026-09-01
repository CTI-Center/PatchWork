---
title: "STIX responses"
source: https://gtidocs.virustotal.com/reference/stix-responses
slug: stix-responses
section: reference
group: "API Introduction"
updatedAt: 2025-09-25T00:33:33.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API Introduction](README.md) › STIX responses

---

# stix-responses

The Google Threat Intelligence API primarily returns **JSON** dictionary responses. However, some endpoints allow you to specify **STIX** as the response format, which will be delivered as a **Bundle**, a specific JSON representation of a list composed by objects and relationships:

```json
{
  "id": "<_string_> Bundle identifier. Format: bundle--[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}.",
  "type": "bundle",
  "objects": "<_list of dictionaries_> list of STIX Google TI objects, STIX Extension Definition objects, STIX Relationship and the STIX Identity object.",
  "extensions": "<_dictionary_> extension attribute for pagination.",
  {
    "<_string_> extension definition identifier: Format: extension-definition--[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}":
    {
      "meta": {
        "cursor": "<_string_> current cursor.",
        "next": "<_string_> link to the Bundle next bucket of objects."
      }
    }
  }
}
```

### example-response

```json
{
  "id": "bundle--8fab937e-b694-41e3-b71c-0800271e87d2",
  "type": "bundle",
  "objects": "[...]", 
  "extensions": {
    "extension-definition--acb11b7d-2453-4727-b993-22624af71f46": 
    {
      "meta": {
        "cursor": "abcd1234=",
        "next": "https://www.virustotal.com/api/v3/..."
      }
    }
  }
}
```

# endpoints

To receive a STIX response, call the endpoints in the table below with the query parameter `output_format`=`stix`. Use the `x-tool` header to obtain additional curated information on STIX objects. Endpoints that do not support the STIX format will return an HTTP 400 status code.

Check out the [Requests Examples](#requests-examples) section for raw Python code snippets.

### api-endpoints-for-retrieving-google-ti-objects

| Main GTI objects                                                                        | Endpoint                                     | Description                                                                                                  |
| :-------------------------------------------------------------------------------------- | :------------------------------------------- | :----------------------------------------------------------------------------------------------------------- |
| Indicators of Compromise (IoCs) - files, URLs, domains, IP addresses                    | `/api/v3/{type}/{id}`                        | Where `{type}` is an IoC type (`files`, `urls`, `domains`, `ip_addresses`) and `{id}` is a IoC identifier    |
| Threat objects - Threat Actor, Campaign, Malware, IoC collection, Report, Vulnerability | [`/api/v3/collections/{id}`](https://gtidocs.readme.io/reference/get-threat) | Where `{id}` is a Threat Actor, Campaign, Malware, IoC collection, Report or Vulnerability object identifier |

### api-endpoints-for-retrieving-google-ti-objects-associated-or-related-to-other-google-ti-objects

| Main GTI objects       | Related GTI objects | Endpoint                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| :--------------------- | :------------------ | :------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IoCs                   | Threat objects      | [`/api/v3/{type}/{id}/{related_object}`](api-responses/introduction-relationships.md)  | Where `{type}` is an IoC type (`files`, `urls`, `domains`, `ip_addresses`), `{id}` is the IoC identifier and `{related_object}` is the threat object type (`threat_actors`, `campaigns`, `malware_families`, `software-toolkit`, `collection` (for IoC collections), `reports`, `vulnerabilities`). The endpoint returns the STIX Threat objects of the selected type that are associated with the IoC.                                                                                                                                                           |
| Threat objects         | Threat objects      | [`/api/v3/{type}/{id}/{related_object}`](api-responses/introduction-relationships.md)  | Where `{type}` is the main Threat object type, the `{id}` is its identifier and `{related_object}` is the type of the Threat objects that are associated with the main one. Available Threat object types are: `threat_actors`, `campaigns`, `malware_families`, `software-toolkit`, `collection` (for IoC collections), `reports`, `vulnerabilities`. The endpoint returns the STIX Threat objects of the selected type that are associated with the main Threat object.                                                                                         |
| Threat objects         | IoCs                | [`/api/v3/{type}/{id}/{related_object}`](api-responses/introduction-relationships.md)  | Where `{type}` is the Threat object type, the `{id}` is its identifier and `{related_object}` is the type (`files`, `urls`, `domains`, `ip_addresses`) of the IoCs associated with it. Available Threat object types are: `threat_actors`, `campaigns`, `malware_families`, `software-toolkit`, `collection` (for IoC collections), `reports`, `vulnerabilities`. The endpoint returns the STIX IoC objects of the selected type that are associated with the Threat object.                                                                                      |
| IoCs                   | Threat objects      | [`/api/v3/{type}/{id}/associations`](api-responses/introduction-relationships.md)      | Where `{type}` is an IoC type (`files`, `urls`, `domains`, `ip_addresses`) and `{id}` is the IoC identifier. The endpoint returns STIX Threat objects associated with the IoC. To retrieve only specific STIX-supporting associated objects, use the `filter` parameter with the `collection_type` and the desired threat object type (`threat-actor`, `campaign`, `malware-family`, `software-toolkit`, `collection` (for IoC collections) ,`report`, `vulnerability`), for example: `filter=collection_type:campaign` or `filter=collection_type:threat-actor`. |
| IoCs or Threat objects | Attack Pattern      | [`/api/v3/{type}/{id}/attack_techniques`](api-responses/introduction-relationships.md) | Where `{type}` is `files` or `collections` and `{id}` is the file identifier or the Threat object identifier.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

# stix-objects

## stix-identity-object

Every STIX object within this bundle's `objects` list is linked to the Google TI Identity object, representing the entity that has generated the STIX Bundle. This connection is made through each object's `created_by_ref` field, which contains the identifier of the Identity object. Notably, this Identity object is the first item in the bundle's `objects` list.

```json
{
  "type": "bundle",
  "id": "<_string_> Bundle identifier. Format: bundle--[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}.",
  "objects": /* <_list of dictionaries_> list of STIX Google TI objects, STIX Extension Definition objects, STIX Relationship and the STIX Identity object. */
  [
    "<_dictionary_> definition of the STIX Identity object that has generated the STIX Bundle.":
    {
      "spec_version": "2.1",
      "id": "<_string_> Identity object identifier. It can be used to track all the STIX objects contained in the Bundle through the `created_by_ref` attribute. Format: identity--[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}",
      "type": "identity",
      "created": "<_string_> STIX Identity object creation UTC timestamp (YYYY-MM-DDThh:mm:ssZ format).",
      "modified": "<_string_> STIX Identity object last modification UTC timestamp (YYYY-MM-DDThh:mm:ssZ format).",
      "name": "Google Threat Intelligence",
      "identity_class": "organization",
      "contact_information": "contact@virustotal.com"
    }, 

    /* ... The rest of Bundle's STIX objects created by the entity represented by the Identity object. */
  ]
}
```

### example-response

```json
{
  "type": "bundle",
  "id": "bundle--e82cbb40-5aff-51fd-9b72-51f26d5b68c8",
  "objects":
  [
    {
      "spec_version": "2.1",
      "id": "identity--1aa11bb7-5ed3-53e6-9a04-34aefffa322f",
      "type": "identity",
      "created": "2024-11-20T12:00:00Z",
      "modified": "2024-11-20T12:00:00Z",
      "name": "Google Threat Intelligence",
      "identity_class": "organization",
      "contact_information": "contact@virustotal.com"
    }, 

    /* ... The rest of Bundle's STIX objects created by the entity represented by the Identity object. */
  ]
}
```

## stix-google-ti-objects

### stix-representation-of-a-google-ti-ioc-object

Google TI IoC objects include files, URLs, domains, and IP addresses. These objects all share the following STIX format representation.

```json
{
  "type": "bundle",
  "id": "<_string_> Bundle identifier. Format: bundle--[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}.",
  "objects": "<_list of dictionaries_> list of STIX Google TI objects, STIX Extension Definition objects, STIX Relationship and the STIX Identity object.",
  [
    "{}": "<_dictionary_> definition of the STIX Identity object that has generated the STIX Bundle.",
    
    "<_dictionary_> definition of the main requested STIX Google TI object which is an Indicator.":
    { 
      "spec_version": "2.1",
      "created_by_ref": "<_string_> Identity object identifier. Format: identity--[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}.",
      "id": "<_string_> main requested STIX Google TI Indicator object identifier. Format: indicator--[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}.",
      "type": "indicator",
      "created": "<_string_> STIX Indicator object creation UTC timestamp (YYYY-MM-DDThh:mm:ssZ format).",
      "modified": "<_string_> STIX Indicator object last modification UTC timestamp (YYYY-MM-DDThh:mm:ssZ format).",
      "name": "<_string_> STIX Indicator object name.",
      "description": "<_string_> Google Threat Intelligence assessment.",
      "valid_from": "<_string_> STIX Indicator object last analysis UTC timestamp (YYYY-MM-DDThh:mm:ssZ format).",
      "pattern_type": "stix",
      "pattern": "<_string_> STIX pattern of requested STIX Indicator object.",
      "external_references": /* <_list of dictionaries_> list of additional external references of the requested Indicator and their sources. */
      [
        {
          "source_name": "<_string_> external source.",
          "external_id": "<_string_> external Indicator object identifier.",
        }
      ],
      "extensions": /* <_dictionary_> extended information showing Google TI indicator score and assessment.
                    Explanations of the Google TI Indicator score are provided in the Extension Definition object with `type`: `extension-definition` and the same identifier.
                    This object is part of the current Bundle's `objects` list and explanations can be found more exactly on the link of its `schema` parameter. */
      {
        "<_string_> Extension Definition object identifier. Format: extension-definition--[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}.":
        {
          "threat_score":
          {
            "value": "<_integer_> the Google Threat Intelligence score is a function of the Verdict and Severity, and leverages additional internal factors to generate the score. Valid values go from 0 to 100.",
          },
          "severity":
          {
            "value": /* <_string_> threat severity. Existing options:
                      `SEVERITY_NONE` - this is the level assigned to entities with non-malicious verdict
                      `SEVERITY_LOW` - the threat likely has a minor impact but should still be monitored
                      `SEVERITY_MEDIUM` - indicates a potential threat that warrants attention
                      `SEVERITY_HIGH` - immediate action is recommended, the threat could have a critical impact
                      `SEVERITY_UNKNOWN` - not enough data to assess a severity */
          },
          "verdict":
          {
            "value": /* <_string_> threat verdict. Existing options:
                        `VERDICT_BENIGN` - the object is considered harmless
                        `VERDICT_UNDETECTED` - no immediate evidence of malicious intent
                        `VERDICT_SUSPICIOUS` - possible malicious activity detected, requires further investigation
                        `VERDICT_MALICIOUS` - high confidence that the object poses a threat
                        `VERDICT_UNKNOWN` -  we are not able to generate a verdict */
          },
          "description": "<_string_> human readable description of the factors contributing to the verdict and severity classification from Google Threat Intelligence."
        }
      }
    },

    /* ... The rest of Bundle's STIX objects including Relationship objects and Extension Definition objects. */
  ]
}
```

### example-response

```json
{
  "type": "bundle",
  "id": "bundle--5cb17b3e-887e-507c-bf47-fe00f6a9f922",
  "objects":
  [
    /* ... Bundle's STIX Identity object. */

    {
      "spec_version": "2.1",
      "created_by_ref": "identity--1aa11bb7-5ed3-53e6-9a04-34aefffa322f",
      "id": "indicator--cc8b9fbe-e4a9-545f-8902-a3e80c44442d",
      "type": "indicator",
      "created": "2024-06-21T14:23:39Z",
      "modified": "2025-04-02T11:06:21Z",
      "name": "07b417ffa08f12201eceba3688690bd5c947f657be00e3c883f6ec342ec5c344",
      "description": "This indicator is malicious (high severity) with high impact. It was detected by Google's spam and threat filtering engines, it was determined as malicious by a Mandiant analyst, Mandiant's scoring pipeline identified this indicator as malicious and it is associated with a tracked Mandiant threat actor. Analysts should prioritize investigation.",
      "valid_from": "2025-03-26T09:56:09Z",
      "pattern_type": "stix",
      "pattern": "[file:hashes.'SHA-256' = '07b417ffa08f12201eceba3688690bd5c947f657be00e3c883f6ec342ec5c344']",
      "external_references":
      [
        {
          "source_name": "gti",
          "external_id": "07b417ffa08f12201eceba3688690bd5c947f657be00e3c883f6ec342ec5c344"
        }
      ],
      "extensions":
      {
        "extension-definition--d4ff44e6-a017-5b6d-ac64-3d18ba052642":
        {
          "verdict":
          {
            "value": "VERDICT_MALICIOUS"
          },
          "severity":
          {
            "value": "SEVERITY_HIGH"
          },
          "threat_score":
          {
            "value": 100
          },
          "description": "This indicator is malicious (high severity) with high impact. It was detected by Google's spam and threat filtering engines, it was determined as malicious by a Mandiant analyst, Mandiant's scoring pipeline identified this indicator as malicious and it is associated with a tracked Mandiant threat actor. Analysts should prioritize investigation."
        }
      }
    },

    /* ... The rest of Bundle's STIX objects including Relationship objects and Extension Definition objects. */
  ]
}

```

### stix-representation-of-a-google-ti-threat-object

Google TI Threat objects are: Threat Actors, Malware Families, Software and Toolkits, IoC Collections, Reports and Vulnerabilities.

```json
{
  "type": "bundle",
  "id": "<_string_> Bundle identifier. Format: bundle--[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}.",
  "objects": /* <_list of dictionaries_> list of STIX Google TI objects, STIX Extension Definition objects, STIX Relationship and the STIX Identity object. */
  [
    "{}": "<_dictionary_> definition of the STIX Identity object that has generated the STIX Bundle.",
    
    "<_dictionary_> definition of the main requested STIX Google TI object which is a Threat object.":
    {
      "spec_version": "2.1",
      "created_by_ref": "<_string_> Identity object identifier. Format: identity--[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}",
      "id": "<_string_> main requested STIX Google TI Threat object identifier. Format: (threat-actor|malware|campaign|grouping|report|vulnerability)--[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}, where `grouping` refers to IoC collections.",
      "type": "<_string_> STIX Threat object type. Existing types for threat objects are: `threat-actor`, `malware` (for Malware Families, and Software and Toolkit), `campaign`, `grouping` (for IoC Collections), `report`, `vulnerability`.",
      "created": "<_string_> STIX Threat object creation UTC timestamp (YYYY-MM-DDThh:mm:ssZ format).",
      "modified": "<_string_> STIX Threat object last modification UTC timestamp (YYYY-MM-DDThh:mm:ssZ format).",
      "name": "<_string_> STIX Threat object name.",
      "description": "<_string_> STIX Threat object  description.",
      "first_seen": "<_string_> STIX Threat object's first observed activity UTC timestamp for `threat-actor`, `malware` and `campaign` objects type (YYYY-MM-DDThh:mm:ssZ format).",
      "last_seen": "<_string_> STIX Threat object's last observed activity UTC timestamp for `threat-actor`, `malware` and `campaign` objects type (YYYY-MM-DDThh:mm:ssZ format).",
      "published": "<_string_> report publication UTC timestamp, only for `report` objects type (YYYY-MM-DDThh:mm:ssZ format).",
      "malware_types": "<_list of strings_> malware types only for `malware` objects type. Examples: ransomware, trojan, spyware, backdoor, etc.",
      "capabilities": "<_list of strings_> malware capabilities only for `malware` objects type. Examples: Create files, Reads memory, Encrypts data with AES, etc.",
      "is_family": "<_boolean_> true value, only for `malware` objects type.",
      "external_references": /* <_list of dictionaries_> list of additional external references of the requested Threat object and their sources. */
      [
        {
          "source_name": "<_string_> external source.",
          "external_id": "<_string_> external Threat object identifier."
        }
      ],
      "extensions": /* <_dictionary_> extended information showing Google TI risk scoring only for `vulnerability` objects type.
                    Explanations of the Google TI Vulnerability risk scoring are provided in the Extension Definition object with `type`: `extension-definition` and the same identifier.
                    This object is part of the current Bundle's `objects` list and explanations can be found more exactly on the link of its `schema` parameter. */
      {
        "<_string_> Extension Definition object identifier. Format: extension-definition--[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}.":
        {
          "risk_rating": "<_string_> Vulnerability risk rating. Existing options: Low, Medium, High, Critical, Unrated.",
          "exploitation_state": "<_string_> Vulnerability exploitation state. Existing options: Available, Wide, No Known, Confirmed.",
          "exploitation_consequence": "<_string_> Vulnerability exploitation consequences.",
          "exploitation_vectors": "<_list of strings_> list of ways in which the Vulnerabilities can be exploited."
        }
      }
    },

    /* ... The rest of Bundle's STIX objects including Relationship objects and Extension Definition objects. */
  ]
}  
```

### example-response

```json
{
  "type": "bundle",
  "id": "bundle--d2b292b7-b79a-5e03-af52-f7acfb105efd",
  "objects":
  [
    /* ... Bundle's STIX Identity object. */

    {
      "spec_version": "2.1",
      "created_by_ref": "identity--1aa11bb7-5ed3-53e6-9a04-34aefffa322f",
      "id": "vulnerability--58521291-46ec-5b1c-b44f-a79d60609300",
      "type": "vulnerability",
      "created": "2022-01-27T15:10:10Z",
      "modified": "2024-08-05T05:05:19Z",
      "name": "CVE-2021-42758",
      "description": "\n\nThe National Vulnerability Database (NVD) has provided the following description:  \n*An improper access control vulnerability [CWE-284] in FortiWLC 8.6.1 and below may allow an authenticated and remote attacker with low privileges to execute any command as an admin user with full access rights via bypassing the GUI restrictions.*\n\n",
      "external_references":
      [
        {
          "source_name": "gti",
          "external_id": "vulnerability--cve-2021-42758"
        },
        {
          "source_name": "cve",
          "external_id": "CVE-2021-42758"
        },
        {
          "source_name": "mandiant",
          "external_id": "MVE-2021-8671"
        }
      ],
      "extensions":
      {
        "extension-definition--06e04f66-3e1b-59d3-b852-cca5223eeb35":
        {
          "risk_rating": "MEDIUM",
          "exploitation_state": "No Known",
          "exploitation_consequence": "Code Execution",
          "exploitation_vectors":
          [
            "General Network Connectivity"
          ]
        }
      }
    },
    
    /* ... The rest of Bundle's STIX objects including Relationship objects and Extension Definition objects. */
  ]
}
```

### stix-representation-of-google-ti-attack-pattern-object

Attack Patterns can only be retrieved as related objects of other main objects: file IoCs and Threat objects described in previous sections.

```json
{
  "type": "bundle",
  "id": "<_string_> Bundle identifier. Format: bundle--[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}.",
  "objects": /* <_list of dictionaries_> list of STIX Google TI objects, STIX Extension Definition objects, STIX Relationship and the STIX Identity object. */
  [
    "{}": "<_dictionary_> definition of the STIX Identity object that has generated the STIX Bundle.",
    "{}": "<_dictionary_> definition of the main requested STIX Google TI object which is a Threat object or a file Indicator object.",
    
    "<_dictionary_> definition of the STIX Attack Pattern object of the main requested STIX Google TI object which is a Threat object or a file Indicator object.":
    {
      "spec_version": "2.1",
      "created_by_ref": "<_string_> Identity object identifier. Format: identity--[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}.",
      "id": "<_string_> STIX Attack Pattern object identifier. Format: attack-pattern--[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}.",
      "type": "attack-pattern",
      "name": "<_string_> STIX Attack Pattern object name.",
      "description": "<_string_> STIX Attack Pattern object name."
    },
    
    /* ... The rest of Bundle's STIX objects including associated Extension Definition object and Relationship objects. */
  ]
}
```

### example-response

```json
{
  "type": "bundle",
  "id": "bundle--5c67ebf2-0b80-5ff4-abc4-d602193337a6",
  "objects":
  [
    /* ... Bundle's STIX Identity object and main request STIX Threat or file Indicator object. */

    {
      "spec_version": "2.1",
      "created_by_ref": "identity--1aa11bb7-5ed3-53e6-9a04-34aefffa322f",
      "id": "attack-pattern--2b4e6908-f6a8-5c4d-8c8b-9a26529e7343",
      "type": "attack-pattern",
      "name": "OS Credential Dumping",
      "description": "Adversaries may attempt to dump credentials to obtain account login and credential material, normally in the form of a hash or a clear text password. Credentials can be obtained from OS caches, memory, or structures. Credentials can then be used to perform Lateral Movement and access restricted information.\nSeveral of the tools mentioned in associated sub-techniques may be used by both adversaries and professional security testers. Additional custom tools likely exist as well."
    },

    /* ... The rest of Bundle's STIX objects including associated Extension Definition object and Relationship objects. */
  ]
}
```

## stix-extension-definition-mechanism

STIX Extension Definition Mechanism are used for adding extra attributes to STIX objects such as

* Google TI assessment attribute including the Google TI score on IoCs STIX objects (files, URLs, domains, IP addresses)
* Google TI risk scoring attribute on Vulnerabilities STIX objects
* Cursor attribute to paginate through the results on the Bundle STIX objects

The following JSON structure is used for adding extra Google TI information to Indicators and Vulnerabilities objects:

```json
{
  "id": "<_string_> Bundle identifier. Format: bundle--[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}.",
  "type": "bundle",
  "objects": /* <_list of dictionaries_> list of STIX Google TI objects, STIX Extension Definition objects, STIX Relationship and the STIX Identity object. */
  [
    "{}": "<_dictionary_> definition of the STIX Identity object that has generated the STIX Bundle.",
    "{}": "<_dictionary_> definition of the STIX Google TI object which can be an Indicator or a Vulnerability.",

    "<_dictionary_> definition of the STIX Extension Definition object of to the STIX Google TI object that can be an Indicator or a Vulnerability.":
    { 
      "spec_version": "2.1",
      "id": "<_string_> Extension Definition object identifier. Format: extension-definition--[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}.",
      "type": "extension-definition",
      "created": "<_string_> STIX Extension Definition object creation UTC timestamp (YYYY-MM-DDThh:mm:ssZ format).",
      "modified": "<_string_> STIX Extension Definition object last modification UTC timestamp (YYYY-MM-DDThh:mm:ssZ format).",
      "name": "<_string_> STIX Extension Definition object name.",
      "description": "<_string_> STIX Extension Definition object description.",
      "version": "1.0",
      "extension_types":
        [
          "property-extension"
        ],
      "schema": "<_string_> STIX Extension Definition object schema that explains how to interpret the extension data added to the Indicator or to the Vulnerability."
    }, 

    /* ... The rest of Bundle's STIX objects. */
  ]
}
```

The following JSON structure is added to a Bundle STIX objects for pagination:

```json
{
  "id": "<_string_> Bundle identifier. Format: bundle--[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}.",
  "type": "bundle",
  "objects": /* <_list of dictionaries_> list of STIX Google TI objects, STIX Extension Definition objects, STIX Relationship and the STIX Identity object. */
  [
    "{}": "<_dictionary_> The rest of Bundle's STIX objects.",

    "<_dictionary_> definition of the STIX Extension Definition object of to the STIX Bundle used for pagination.":
    { 
      "spec_version": "2.1",
      "id": "<_string_>Extension Definition object identifier. Format: extension-definition--[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}.",
      "type": "extension-definition",
      "created": "<_string_> STIX Extension Definition object creation UTC timestamp (YYYY-MM-DDThh:mm:ssZ format).",
      "modified": "<_string_> STIX Extension Definition object last modification UTC timestamp (YYYY-MM-DDThh:mm:ssZ format).",
      "name": "GTI Bundle Metadata Extension",
      "description": "Adds Bundle custom metadata such as the pagination cursor attribute.",
      "version": "1.0",
      "extension_types":
        [
          "property-extension"
        ],
      "schema": "<_string_> STIX Extension Definition object schema that explains how to interpret the extension data for pagination."
    }
  ],
  "extensions": /* <_dictionary_> extended Bundle data for pagination. */
    {
        "<_string_> Extension Definition object identifier: Format: extension-definition--[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}":
        {
            "meta":
            {
                "cursor": "<_string_> Bundle's current cursor.",
                "next": "<_string_> link to the Bundle next bucket of objects."
            }
        }
    }
}
```

### example-response-on-stix-extension-definition-mechanism-for-google-ti-assessment-on-iocs

```json
{
  "id": "bundle--5fafc5fe-6ff8-5ccf-90b1-4f25de9aff74",
  "type": "bundle",
  "objects": [
    /* ... The rest of Bundle's STIX objects, including the Indicator Google TI object (IoC) that contains the information provided by this Extension Definition objects. */
    
    {
      "spec_version": "2.1",
      "id": "extension-definition--d4ff44e6-a017-5b6d-ac64-3d18ba052642",
      "type": "extension-definition",
      "created": "2024-11-14T12:00:00Z",
      "modified": "2024-11-14T12:00:00Z",
      "name": "GTI Indicator Metadata Extension",
      "description": "Adds Indicator custom metadata such as the GTI assessment and other GTI relevant attributes.",
      "version": "1.0",
      "extension_types":
        [
          "property-extension"
        ],
      "schema": "https://www.virustotal.com/api/v3/stix-extensions/gti-indicator-metadata-extension-v1_0.json"
    }
  ]
}
```

### example-response-on-stix-extension-definition-mechanism-for-risk-scoring-on-vulnerabilities

```json
{
  "id": "bundle--d2b292b7-b79a-5e03-af52-f7acfb105efd",
  "type": "bundle",
  "objects": [
    /* ... The rest of Bundle's STIX objects, including the Vulnerability Google TI object that includes the information provided by this Extension Definition objects. */
  
    {
      "spec_version": "2.1",
      "id": "extension-definition--06e04f66-3e1b-59d3-b852-cca5223eeb35",
      "type": "extension-definition",
      "created": "2024-11-14T12:00:00Z",
      "modified": "2024-11-14T12:00:00Z",
      "name": "GTI Vulnerability Extension",
      "description": "Adds a Vulnerability Threat Risk metadata information.",
      "version": "1.0",
      "extension_types":
      [
        "property-extension"
      ],
      "schema": "https://www.virustotal.com/api/v3/stix-extensions/gti-vulnerability-metadata-extension-v1_0.json"
    }
  ]
}
```

### example-response-on-stix-extension-definition-mechanism-for-pagination

```json
{
  "id": "bundle--5c67ebf2-0b80-5ff4-abc4-d602193337a6",
  "type": "bundle",
  "objects": [
    /* ... The rest of Bundle's STIX objects. */

    {
      "spec_version": "2.1",
      "id": "extension-definition--e0e2bd88-8e87-52d5-b822-3fdd60918598",
      "type": "extension-definition",
      "created": "2024-11-14T12:00:00Z",
      "modified": "2024-11-14T12:00:00Z",
      "name": "GTI Bundle Metadata Extension",
      "description": "Adds Bundle custom metadata such as the pagination cursor attribute.",
      "version": "1.0",
      "extension_types":
      [
        "property-extension"
      ],
      "schema": "https://www.virustotal.com/api/v3/stix-extensions/bundle-metadata-extension-v1_0.json"
    }
  ],
  "extensions":
    {
        "extension-definition--e0e2bd88-8e87-52d5-b822-3fdd60918598":
        {
            "meta":
            {
                "cursor": "eyJsaW1pdCI6IDEwLCAib2Zmc2V0IjogMTB9",
                "next": "https://www.virustotal.com/api/v3/collections/campaign--4964f906-9d66-5cc2-9c73-6a843c86f4e4/attack_techniques?output_format=stix&cursor=eyJsaW1pdCI6IDEwLCAib2Zmc2V0IjogMTB9"
            }
        }
    }
}
```

## stix-relationships

Relationships can link two main GTI objects or connect a main GTI object to an attack pattern.

```json
{
  "type": "bundle",
  "id": "<_string_> Bundle identifier. Format: bundle--[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}.",
  "objects": /* <_list of dictionaries_> list of STIX Google TI objects, STIX Extension Definition objects, STIX Relationship and the STIX Identity object. */
  [
    "{}": "<_dictionary_> definition of the STIX Identity object that has generated the STIX Bundle.",
    "{}": "<_dictionary_> definition of the main requested STIX Google TI object.",
    "{}": "<_dictionary_> definition of the STIX Google TI object that is related to the main STIX Google TI object.",

    "<_dictionary_> definition of the STIX Relationship between the main STIX Google TI object and previous related STIX Google TI object.":
    {
      "spec_version": "2.1",
      "created_by_ref": "<_string_> Identity object identifier. Format: identity--[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}.",
      "id": "<_string_> Relationship identifier. Format: relationship--[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}.",
      "type": "relationship",
      "source_ref": "<_string_> main STIX Google TI object identifiers.",
      "target_ref": "<_string_> related STIX Google TI object identifier.",
      "relationship_type": "<_string_> the type of the Relationship between the main STIX Google TI object and previous related STIX Google TI object. Available options are listed in the table below."
    },
    "{}": "<_dictionary_> definition of the STIX Google TI object that is related to the main STIX Google TI object.",
    "{}": "<_dictionary_> definition of the STIX Relationship between the main STIX Google TI object and previous related STIX Google TI object."
        
    /* ... The rest of Bundle's STIX objects created by the entity represented by the Identity object. */
  ]
}
```

| Main STIX Google TI object type                  | Related STIX Google TI object type               | `relationship_type` |
| :----------------------------------------------- | :----------------------------------------------- | :------------------ |
| `indicator` (file)                               | `attack-pattern`                                 | `indicates`         |
| `indicator` (file, ip\_address, url, domain)     | all except `attack-pattern`                      | `indicates`         |
| all except `indicator`                           | `attack-pattern`                                 | `uses`              |
| `threat_actor`                                   | `threat_actor`                                   | `related-to`        |
| `threat_actor`                                   | `malware` (Malware Family, Software and Toolkit) | `uses`              |
| `threat_actor`                                   | `campaign`                                       | `related-to`        |
| `threat_actor`                                   | `report`                                         | `related-to`        |
| `threat_actor`                                   | `vulnerability`                                  | `targets`           |
| `threat_actor`                                   | `grouping` (IoC collections)                     | `related-to`        |
| `malware` (Malware Family, Software and Toolkit) | `threat_actor`                                   | `authored-by`       |
| `malware` (Malware Family, Software and Toolkit) | `malware` (Malware Family, Software and Toolkit) | `related-to`        |
| `malware` (Malware Family, Software and Toolkit) | `campaign`                                       | `related-to`        |
| `malware` (Malware Family, Software and Toolkit) | `report`                                         | `related-to`        |
| `malware` (Malware Family, Software and Toolkit) | `vulnerability`                                  | `exploits`          |
| `malware` (Malware Family, Software and Toolkit) | `grouping` (IoC collections)                     | `related-to`        |
| `campaign`                                       | `threat_actor`                                   | `related-to`        |
| `campaign`                                       | `malware` (Malware Family, Software and Toolkit) | `uses`              |
| `campaign`                                       | `campaign`                                       | `attributed-to`     |
| `campaign`                                       | `report`                                         | `related-to`        |
| `campaign`                                       | `vulnerability`                                  | `targets`           |
| `campaign`                                       | `grouping` (IoC collections)                     | `related-to`        |
| `report`                                         | all                                              | `related-to`        |
| `vulnerability`                                  | all                                              | `related-to`        |
| `grouping` (IoC collections)                     | all                                              | `related-to`        |

# requests-examples

## iocs-and-threat-objects-reports-example

Get the STIX report of the [ALPHV ransomware **file**](https://www.virustotal.com/gui/file/f837f1cd60e9941aa60f7be50a8f2aaaac380f560db8ee001408f35c1b7a97cb) with sha256 hash f837f1cd60e9941aa60f7be50a8f2aaaac380f560db8ee001408f35c1b7a97cb.

```python
import requests

type = "files"
id = "c251b3f45fea9ebb0712a3769e9dd3594570809cee23ae949da533bb90e876de"
format = "stix"

url = f'https://www.virustotal.com/api/v3/{type}/{id}?output_format={format}'
headers = {
    "x-tool":"stix-integration",
    "accept": "application/json",
    "x-apikey": <api-key>
}

response = requests.get(url, headers=headers)
print(response.text)
```

Get the STIX report of the [UNC3507 **Threat Actor**](https://www.virustotal.com/gui/collection/threat-actor--d5f8230a-15a9-5b71-b8ad-e730e82f79d4) with threat-actor--d5f8230a-15a9-5b71-b8ad-e730e82f79d4 identifier.

```python
import requests

id = "threat-actor--d5f8230a-15a9-5b71-b8ad-e730e82f79d4"
format = "stix"

url = f'https://www.virustotal.com/api/v3/collections/{id}?output_format={format}'
headers = {
    "x-tool":"stix-integration",
    "accept": "application/json",
    "x-apikey": <api-key>
}

response = requests.get(url, headers=headers)
print(response.text)
```

Get the STIX report of [CVE-2024-3400 **vulnerability**](https://www.virustotal.com/gui/collection/vulnerability--cve-2024-3400) with vulnerability--cve-2024-3400 identifier.

```python
import requests

id = "vulnerability--cve-2024-3400"
format = "stix"

url = f'https://www.virustotal.com/api/v3/collections/{id}?output_format={format}'
headers = {
    "x-tool":"stix-integration",
    "accept": "application/json",
    "x-apikey": <api-key>
}
response = requests.get(url, headers=headers)
print(response.text)
```

## associations-and-relationships-example

Get the **list of campaigns** associated with the ["hxxp://185.80.92.143:8998/update\[.\]html"](https://www.virustotal.com/gui/url/bbdf491bdf8b10d8c4466b83d52e78f4cb385bc72bb53022e4e5f59eb45930b7) **URL** indicator with bbdf491bdf8b10d8c4466b83d52e78f4cb385bc72bb53022e4e5f59eb45930b7 identifier.

```python
import requests

type = "urls"
id = "bbdf491bdf8b10d8c4466b83d52e78f4cb385bc72bb53022e4e5f59eb45930b7"
related_object = "campaigns"
format = "stix"

url = f'https://www.virustotal.com/api/v3/{type}/{id}/{related_object}?output_format={format}'
headers = {
    "x-tool":"stix-integration",
    "accept": "application/json",
    "x-apikey": <api-key>
}

response = requests.get(url, headers=headers)
print(response.text)
```

Get the list of **attack techniques** of the [APT44 related **campaign**](https://www.virustotal.com/gui/collection/campaign--22f8e22c-d644-5647-ab57-741a4f33ad59) with campaign--4964f906-9d66-5cc2-9c73-6a843c86f4e4 identifier.

```python
import requests

type = "collections"
id = "campaign--22f8e22c-d644-5647-ab57-741a4f33ad59"
format = "stix"

url = f'https://www.virustotal.com/api/v3/{type}/{id}/attack_techniques?output_format={format}'
headers = {
    "x-tool":"stix-integration",
    "accept": "application/json",
    "x-apikey": <api-key>
}

response = requests.get(url, headers=headers)
print(response.text)
```

Get the **list of reports** associated with the [CVE-2024-3400 **vulnerability**](https://www.virustotal.com/gui/collection/vulnerability--cve-2024-3400) with vulnerability--cve-2024-3400 identifier.

```python
import requests

type = "collections"
id = "campaign--22f8e22c-d644-5647-ab57-741a4f33ad59"
related_object = "reports"
format = "stix"

url = f'https://www.virustotal.com/api/v3/{type}/{id}/{related_object}?output_format={format}'
headers = {
    "x-tool":"stix-integration",
    "accept": "application/json",
    "x-apikey": <api-key>
}

response = requests.get(url, headers=headers)
print(response.text)
```

Get the **list of files** associated with the [RANSOMHUB **malware family**](https://www.virustotal.com/gui/collection/malware--5d30976f-5b42-5ef1-a0fd-2c076c1ef64f) with malware--5d30976f-5b42-5ef1-a0fd-2c076c1ef64f identifier.

```python
import requests

type = "collections"
id = "malware--5d30976f-5b42-5ef1-a0fd-2c076c1ef64f"
related_object = "files"
format = "stix"

url = f'https://www.virustotal.com/api/v3/{type}/{id}/{related_object}?output_format={format}'
headers = {
    "x-tool":"stix-integration",
    "accept": "application/json",
    "x-apikey": <api-key>
}

response = requests.get(url, headers=headers)
print(response.text)
```

---

← [OpenAPI Specifications](openapi-specs.md) · [up](README.md) · [Threat Actors, Malware & Tools, Campaigns, IoC Collection, Country and Industry Profiles](../02-global-landscape/threat-actors-malware-tools-campaigns-ioc-collections.md) →

*Archived from <https://gtidocs.virustotal.com/reference/stix-responses>.*
