---
title: "Create a new Retrohunt job"
source: https://gtidocs.virustotal.com/reference/create-retrohunt-job
slug: create-retrohunt-job
section: reference
group: "YARA Hunting"
updatedAt: 2025-09-25T00:36:32.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [YARA Hunting](../README.md) › [Retrohunt](../retrohunt.md) › Create a new Retrohunt job

---

# create-a-new-retrohunt-job

This endpoint creates a new Retrohunt job. The request's body must have the following structure:

```json Example request
{
  "data": {
    "type": "retrohunt_job",
    "attributes": {
      "rules": "rule foobar { strings: $ = \"foobar\" condition: all of them }",
      "notification_email": "notifications@acme.com",
      "corpus": "main",
      "time_range": {
        "start": 1545145761,
        "end": 1547737720
      }
    }
  }
}
```

The `rules` attribute is required, but `notification_email`, `corpus` and `time_range` are optional. You should provide  `notification_email` if you want to receive an email notification when the job is finished, while `corpus` allows you to select which dataset you want to scan with your job. There are two different corpuses: "main" and "goodware". The "main" corpus is the default one, composed of files sent to Google Threat Intelligence during the last few months. The "goodware" corpus is a random selection of \~1.000.000 files from the [NSRL](https://www.nist.gov/software-quality-group/national-software-reference-library-nsrl) that are not detected by any antivirus engine. This corpus contains multiple file types, and is useful for testing your YARA rules for false positives. If the `corpus` attribute is not specified the "main" corpus will be used.

> 🚧 Retrohunt limits
>
> Each user can run up to 10 Retrohunt jobs at the same time, when you reach that limit you must wait for one of the running jobs to finish before launching a new one. Additionally, each job can contain up to 300 YARA rules.

If you want your job to scan files sent to Google TI within a certain time range you can use the  `time_range` attribute to specify the desired range. Both the `start` and `end` fields in `time_range` should be the UNIX timestamp for the minimum and upper bound of the time range in UTC, and they should be within the maximum range allowed by your Retrohunt privileges. All users can scan up to 90 days back, and this can go up to 180 or 365 days for more privileged users. If `start` is not specified your Retrohunt job will scan back to the limit allowed by your privileges, and if `end` is not specified it will scan up to the most recent files.

Returns the newly created [Retrohunt Job](../../17-api-objects/retrohunt-job-object.md) object.

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
      "name": "Retrohunt"
    }
  ],
  "paths": {
    "/intelligence/retrohunt_jobs": {
      "post": {
        "tags": [
          "Retrohunt"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "create-retrohunt-job",
        "parameters": [
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
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "properties": {
                  "data": {
                    "default": "{     \"type\": \"retrohunt_job\",     \"attributes\": {       \"rules\": \"rule foobar { strings: $ = \\\"foobar\\\" condition: all of them }\",       \"corpus\": \"main\"    }   }",
                    "description": "A Retrohunt job",
                    "format": "json",
                    "type": "string"
                  }
                },
                "required": [
                  "data"
                ],
                "type": "object"
              }
            }
          }
        },
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
        "summary": "Create a new Retrohunt job"
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

← [Get a list of Retrohunt jobs](get-retrohunt-jobs.md) · [up](../README.md) · [Delete a Retrohunt job](delete-retrohunt-job.md) →

*Archived from <https://gtidocs.virustotal.com/reference/create-retrohunt-job>.*
