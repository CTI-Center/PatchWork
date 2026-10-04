---
title: "Get a session"
source: https://gtidocs.virustotal.com/reference/get-session
slug: get-session
section: reference
group: "agentic"
updatedAt: 2026-08-04T08:18:35.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [agentic](../README.md) › [Sessions](../sessions.md) › Get a session

---

# get-a-session

This endpoint returns details for a specific [agentic chat session](../../17-api-objects/agentic-session-object.md) by its unique ID.

# openapi-definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "title": "Agentic",
    "version": "1.0"
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3"
    }
  ],
  "tags": [
    {
      "name": "Sessions",
      "description": "Create, list, retrieve, update, delete and share agentic sessions."
    }
  ],
  "security": [],
  "paths": {
    "/agentspace/sessions/{session_id}": {
      "get": {
        "operationId": "get-session",
        "summary": "Get a session",
        "tags": [
          "Sessions"
        ],
        "deprecated": false,
        "parameters": [
          {
            "name": "session_id",
            "in": "path",
            "required": true,
            "description": "The unique identifier of the session.",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Your API key.",
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
            "description": "Session details.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                },
                "example": {
                  "data": {
                    "type": "agentic_session",
                    "id": "762c2f6d-74d1-44bb-94fe-b39f7eeeb364",
                    "attributes": {
                      "title": "Malware Analysis of hash 4a2b...",
                      "creation_date": "2026-08-03T12:00:00Z",
                      "last_modification_date": "2026-08-03T12:01:30Z",
                      "events": [
                        {
                          "id": "msg-111",
                          "message_type": "USER_MESSAGE",
                          "user_message": {
                            "timestamp_seconds": 1785758400,
                            "widgets": [
                              {
                                "widget_type": "MARKDOWN_TEXT",
                                "markdown_text_widget": {
                                  "text": "Analyze this file."
                                }
                              }
                            ]
                          }
                        },
                        {
                          "id": "msg-222",
                          "message_type": "AGENT_FINAL_RESPONSE",
                          "agent_final_response": {
                            "agent_id": "malware-analyst",
                            "widgets": [
                              {
                                "widget_type": "MARKDOWN_TEXT",
                                "markdown_text_widget": {
                                  "text": "The file is malicious."
                                }
                              }
                            ]
                          }
                        }
                      ]
                    }
                  }
                }
              }
            }
          }
        },
        "security": []
      }
    }
  },
  "x-readme": {
    "explorer-enabled": true,
    "headers": [],
    "proxy-enabled": false,
    "samples-enabled": true
  }
}
```

---

← [List sessions](list-sessions.md) · [up](../README.md) · [Get a session share token](get-session-token.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-session>.*
