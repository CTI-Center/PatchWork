---
title: "Upload a file"
source: https://gtidocs.virustotal.com/reference/files-scan
slug: files-scan
section: reference
group: "IoC Investigation"
updatedAt: 2026-04-17T12:38:47.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Files](../files.md) › Upload a file

---

# upload-a-file

Upload and analyse a file

> 📘 File size
>
> If the file to be uploaded is bigger than 32MB, please use the [/files/upload\_url](files-upload-url.md) endpoint instead which admits files up to 650MB.

Quota counts are not impacted if the submitted file is unique and has no prior record in the our database.

# openapi-definition

```json
{
  "info": {
    "title": "IoC Investigation",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Files"
    }
  ],
  "paths": {
    "/files": {
      "post": {
        "tags": [
          "Files"
        ],
        "description": "",
        "operationId": "files-scan",
        "parameters": [
          {
            "description": "Your API key",
            "example": "<your API key>",
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
            "multipart/form-data": {
              "encoding": {
                "file": {
                  "contentType": "application/octet-stream"
                }
              },
              "example": "/path/to/file",
              "schema": {
                "properties": {
                  "file": {
                    "format": "binary",
                    "type": "string"
                  },
                  "password": {
                    "description": "Optional, password to decompress and scan a file contained in a protected ZIP file.",
                    "type": "string"
                  }
                },
                "type": "object"
              }
            }
          },
          "description": "File to scan",
          "required": true
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n  \"data\": {\n    \"type\": \"analysis\",\n    \"id\": \"OTdiYWM4MjI0NGE2ZjhlNTk4NDZmZDY1YTliMWYwYjM6YzlhNzBhNDM1NzlmZjc5M2E2NGI5Mzk0NmJjNjVhOWE6MTczNzYzMjk2MQ==\",\n    \"links\": {\n      \"self\": \"https://www.virustotal.com/api/v3/private/analyses/OTdiYWM4MjI0NGE2ZjhlNTk4NDZmZDY1YTliMWYwYjM6YzlhNzBhNDM1NzlmZjc5M2E2NGI5Mzk0NmJjNjVhOWE6MTczNzYzMjk2MQ==\"\n    }\n  }}"
                  }
                },
                "schema": {
                  "properties": {
                    "data": {
                      "properties": {
                        "id": {
                          "type": "string"
                        },
                        "type": {
                          "type": "string"
                        },
                        "links": {
                          "properties": {
                            "self": {
                              "type": "string"
                            }
                          }
                        }
                      },
                      "type": "object"
                    }
                  },
                  "type": "object"
                }
              }
            },
            "description": "The analysis ID. Use [/analyses/<analysis_ID>](https://gtidocs.readme.io/reference/analysis) API call to check the analysis status."
          },
          "401": {
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n  \"error\": {\n    \"code\": \"WrongCredentialsError\",\n    \"message\": \"Wrong API key\"\n  }}"
                  }
                },
                "schema": {
                  "properties": {
                    "error": {
                      "properties": {
                        "code": {
                          "type": "string"
                        },
                        "message": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    }
                  },
                  "type": "object"
                }
              }
            },
            "description": "If password was provided and the file isn't a ZIP, it contains more than one file, the password is incorrect, or the file is corrupt."
          }
        },
        "summary": "Upload a file"
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

← [Get a URL for uploading large files](files-upload-url.md) · [up](../README.md) · [Get a file report](file-info.md) →

*Archived from <https://gtidocs.virustotal.com/reference/files-scan>.*
