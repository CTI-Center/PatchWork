---
title: "Post a message to a new session"
source: https://gtidocs.virustotal.com/reference/create-session
slug: create-session
section: reference
group: "agentic"
updatedAt: 2026-08-05T11:23:19.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [agentic](../README.md) › [Sessions](../sessions.md) › Post a message to a new session

---

# post-a-message-to-a-new-session

Creates a new [session](../../17-api-objects/agentic-session-object.md) by sending the first message to the agent synchronously, and returns the resulting session state. To continue an existing conversation, use [Post a message to a session](post-session-message.md) instead.

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
    "/agentspace/sessions": {
      "post": {
        "operationId": "create-session",
        "summary": "Post a message to a new session",
        "tags": [
          "Sessions"
        ],
        "deprecated": false,
        "parameters": [
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
            "description": "Chat completed synchronously.",
            "headers": {
              "X-Session-Id": {
                "description": "The ID of the session.",
                "schema": {
                  "type": "string"
                }
              }
            },
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
        "requestBody": {
          "content": {
            "multipart/form-data": {
              "schema": {
                "type": "object",
                "required": [
                  "message"
                ],
                "properties": {
                  "message": {
                    "type": "string",
                    "description": "The user message to send to the agent."
                  },
                  "files": {
                    "type": "array",
                    "items": {
                      "type": "string",
                      "format": "binary"
                    },
                    "description": "Optional files to attach to the message as artifacts."
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

← [Create a session from a shared token](create-session-from-token.md) · [up](../README.md) · [Post a message to an existing session](post-session-message.md) →

*Archived from <https://gtidocs.virustotal.com/reference/create-session>.*
