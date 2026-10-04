---
title: "Get a behaviour report from a private file"
source: https://gtidocs.virustotal.com/reference/privatefile-behaviourssandbox-id
slug: privatefile-behaviourssandbox-id
section: reference
group: "Private Scanning"
updatedAt: 2025-09-25T00:37:02.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Private Scanning](../README.md) › [Private Files Behaviours](../private-files-behaviours.md) › Get a behaviour report from a private file

---

# get-a-behaviour-report-from-a-private-file

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

Fetches a [Private File Behaviour](../../17-api-objects/private-file-behaviours-object.md) object by ID. It expects the sandbox ID returned by the [GET /private/files/\{id}/behaviours](get-all-behaviour-reports-from-a-private-file.md) endpoint.

```json Example response
{
    "data": {
        "attributes": {
            "behash": "3f4a02b305dde56c7c606849289bb194",
            "calls_highlighted": [
                "GetTickCount"
            ],
            "files_opened": [
                "C:\\Windows\\system32\\ws2_32.dll",
                "C:\\Windows\\system32\\UxTheme.dll",
                "C:\\Windows\\system32\\ole32.dll",
                "C:\\Users\\<USER>\\Downloads\\putty.hlp",
                "C:\\Users\\<USER>\\Downloads\\putty.cnt",
                "C:\\Users\\<USER>\\Downloads\\putty.chm",
                "C:\\Windows\\system32\\user32.dll",
                "C:\\Windows\\system32\\advapi32.dll",
                "C:\\Windows\\system32\\ntmarta.dll",
                "C:\\Windows\\WinSxS\\x86_microsoft.windows.common-controls_6595b64144ccf1df_6.0.7601.18837_none_41e855142bd5705d",
                "C:\\Windows\\Fonts\\staticcache.dat"
            ],
            "has_html_report": true,
            "has_pcap": true,
            "modules_loaded": [
                "UxTheme.dll",
                "IMM32.dll",
                "SspiCli.dll",
                "ADVAPI32.dll"
            ],
            "processes_tree": [
                {
                    "name": "9f9e74241d59eccfe7040bfdcbbceacb374eda397cc53a4197b59e4f6f380a91.exe",
                    "process_id": "2340"
                }
            ],
            "registry_keys_opened": [
                "HKCU\\Software\\SimonTatham\\PuTTY\\Sessions",
                "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\FontLink\\SystemLink",
                "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\LanguagePack\\DataStore_V1.0",
                "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\LanguagePack\\DataStore_V1.0\\Disable",
                "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\LanguagePack\\DataStore_V1.0\\DataFilePath",
                "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\LanguagePack\\SurrogateFallback",
                "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\LanguagePack\\SurrogateFallback\\MS Shell Dlg"
            ],
            "sandbox_name": "VirusTotal Jujubox",
            "tags": [
                "DIRECT_CPU_CLOCK_ACCESS",
                "RUNTIME_MODULES"
            ],
            "text_highlighted": [
                "PuTTY Configuration",
                "&Open",
                "Cate&gory:",
                "C:\\Windows\\system32\\cmd.exe"
            ]
        },
        "id": "9f9e74241d59eccfe7040bfdcbbceacb374eda397cc53a4197b59e4f6f380a91_VirusTotal Jujubox-1658933614",
        "links": {
            "self": "https://www.virustotal.com/api/v3/private/file_behaviours/9f9e74241d59eccfe7040bfdcbbceacb374eda397cc53a4197b59e4f6f380a91_VirusTotal Jujubox-1658933614"
        },
        "type": "private_file_behaviour"
    }
}
```

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
      "name": "Private Files Behaviours"
    }
  ],
  "paths": {
    "/file_behaviours/{sandbox_id}": {
      "get": {
        "tags": [
          "Private Files Behaviours"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "privatefile-behaviourssandbox-id",
        "parameters": [
          {
            "description": "Your API key",
            "in": "header",
            "name": "x-apikey",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Sandbox report ID.",
            "in": "path",
            "name": "sandbox_id",
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
        "summary": "Get a behaviour report from a private file"
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

← [Get the behaviour reports from a private file](get-all-behaviour-reports-from-a-private-file.md) · [up](../README.md) · [Get the EVTX file generated during a private file’s behavior analysis](file-behaviourssandbox-idevtx.md) →

*Archived from <https://gtidocs.virustotal.com/reference/privatefile-behaviourssandbox-id>.*
