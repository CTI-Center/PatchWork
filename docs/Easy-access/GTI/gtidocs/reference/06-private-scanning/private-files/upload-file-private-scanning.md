---
title: "Upload a file"
source: https://gtidocs.virustotal.com/reference/upload-file-private-scanning
slug: upload-file-private-scanning
section: reference
group: "Private Scanning"
updatedAt: 2025-09-25T00:36:53.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Private Scanning](../README.md) › [Private Files](../private-files.md) › Upload a file

---

# upload-a-file

Upload and analyse a file with Private Scanning

> 📘 File size
>
> If the file to be uploaded is bigger than 32MB, please use the [/private/files/upload\_url](private-files-upload-url.md) endpoint instead which admits files up to 650MB.

# openapi-definition

```json
{
  "info": {
    "title": "Private Scanning",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Private Files"
    }
  ],
  "paths": {
    "/files": {
      "post": {
        "tags": [
          "Private Files"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "upload-file-private-scanning",
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
            "multipart/form-data": {
              "encoding": {
                "file": {
                  "contentType": "application/octet-stream"
                }
              },
              "example": "/path/to/file",
              "schema": {
                "properties": {
                  "command_line": {
                    "description": "Command line arguments to use when running the file in sandboxes.",
                    "type": "string"
                  },
                  "disable_sandbox": {
                    "default": false,
                    "description": "If true, then the file won't be detonated in sandbox environments. False by default.",
                    "type": "string"
                  },
                  "enable_internet": {
                    "default": false,
                    "description": "If the file should have internet access when running in sandboxes. False by default.",
                    "type": "string"
                  },
                  "file": {
                    "format": "binary",
                    "type": "string"
                  },
                  "intercept_tls": {
                    "default": false,
                    "description": "Intercept HTTPS/TLS/SSL communication. Intercept HTTPS to view encypted URLS, hostnames and HTTP headers.  This is detectable by any sample that checks certificates, and makes JA3 hashes unusable.",
                    "type": "string"
                  },
                  "password": {
                    "description": "Optional, password to decompress and scan a file contained in a protected ZIP file.",
                    "type": "string"
                  },
                  "retention_period_days": {
                    "description": "Optional, number of days the report and file are kept in VT (between 1 and 28). If not set it defaults to the group's retention policy preference (1 day by default).",
                    "type": "integer",
                    "default": 1,
                    "format": "int32",
                    "maximum": 28,
                    "minimum": 1
                  },
                  "storage_region": {
                    "description": "Optional, storage region where the file will be stored. By default uses the group's private_scanning.storage_region preference. Allowed values are US, CA, EU, GB",
                    "type": "string",
                    "enum": [
                      "US",
                      "CA",
                      "EU",
                      "GB"
                    ]
                  },
                  "interaction_sandbox": {
                    "description": "Select the sandbox desired for interactive use.",
                    "type": "string",
                    "enum": [
                      "cape_win",
                      "cape_linux"
                    ]
                  },
                  "interaction_timeout": {
                    "description": "Interaction timeout in seconds, minimum value: 60. (1 minute.) Max value: 1800: (30 minutes)",
                    "type": "integer",
                    "default": 60,
                    "format": "int32",
                    "maximum": 1800,
                    "minimum": 60
                  },
                  "locale": {
                    "default": "EN_US",
                    "description": "Preferred sandbox locale. On windows this selection will change the language and keyboard settings of the analysis machine.",
                    "type": "string",
                    "enum": [
                      "EN_US",
                      "AR_SA",
                      "DE_DE",
                      "ES_ES",
                      "PT_BR"
                    ]
                  }
                },
                "required": [
                  "file"
                ],
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
                    "value": "{\n  \"data\": {\n    \"type\": \"private_analysis\",\n    \"id\": \"OTdiYWM4MjI0NGE2ZjhlNTk4NDZmZDY1YTliMWYwYjM6YzlhNzBhNDM1NzlmZjc5M2E2NGI5Mzk0NmJjNjVhOWE6MTczNzYzMjk2MQ==\",\n    \"links\": {\n      \"self\": \"https://www.virustotal.com/api/v3/private/analyses/OTdiYWM4MjI0NGE2ZjhlNTk4NDZmZDY1YTliMWYwYjM6YzlhNzBhNDM1NzlmZjc5M2E2NGI5Mzk0NmJjNjVhOWE6MTczNzYzMjk2MQ==\"\n    }\n  }}"
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
            "description": "The analysis ID. Use [/analyses/<analysis_ID>](https://gtidocs.readme.io/reference/private-analysis) API call to check the analysis status."
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
      "url": "https://www.virustotal.com/api/v3/private"
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

← [Private Files](../private-files.md) · [up](../README.md) · [List private files](list-private-files.md) →

*Archived from <https://gtidocs.virustotal.com/reference/upload-file-private-scanning>.*
