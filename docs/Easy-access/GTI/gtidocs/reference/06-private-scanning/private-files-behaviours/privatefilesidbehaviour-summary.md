---
title: "Get a summary of all behavior reports for a file"
source: https://gtidocs.virustotal.com/reference/privatefilesidbehaviour-summary
slug: privatefilesidbehaviour-summary
section: reference
group: "Private Scanning"
updatedAt: 2025-09-25T00:37:10.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Private Scanning](../README.md) › [Private Files Behaviours](../private-files-behaviours.md) › Get a summary of all behavior reports for a file

---

# get-a-summary-of-all-behavior-reports-for-a-file

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

This endpoint returns a summary with behavioural information about the private file. The summary consists in merging together the reports produced by the multiple sandboxes we have integrated in VirusTotal.

This API call returns all fields contained in the [Private File Behaviour](../../17-api-objects/private-file-behaviours-object.md) object, except the ones that make sense only for individual sandboxes:

* `behash`
* `has_html_report`
* `has_pcap`
* `last_modification_date`
* `sandbox_name`

```json Example response
{
    "data": {
        "calls_highlighted": [
            "GetTickCount"
        ],
        "files_opened": [
            "C:\\WINDOWS\\system32\\winime32.dll",
            "C:\\WINDOWS\\system32\\ws2_32.dll",
            "C:\\WINDOWS\\system32\\ws2help.dll",
            "C:\\WINDOWS\\system32\\psapi.dll",
            "C:\\WINDOWS\\system32\\imm32.dll",
            "C:\\WINDOWS\\system32\\lpk.dll",
            "C:\\WINDOWS\\system32\\usp10.dll",
            "C:\\WINDOWS\\WinSxS\\x86_Microsoft.Windows.Common-Controls_6595b64144ccf1df_6.0.2600.5512_x-ww_35d4ce83\\comctl32.dll",
            "C:\\WINDOWS\\system32\\winmm.dll",
            "C:\\WINDOWS\\system32\\winspool.drv",
            "C:\\WINDOWS\\WindowsShell.Manifest",
            "C:\\WINDOWS\\system32\\shell32.dll",
            "C:\\WINDOWS\\system32\\MSCTF.dll"
        ],
        "modules_loaded": [
            "comctl32.dll",
            "C:\\WINDOWS\\system32\\ws2_32.dll",
            "C:\\WINDOWS\\system32\\MSCTF.dll",
            "version.dll",
            "C:\\WINDOWS\\system32\\msctfime.ime",
            "C:\\WINDOWS\\system32\\ole32.dll",
            "USER32.dll",
            "IMM32.dll",
            "C:\\WINDOWS\\system32\\user32.dll"
        ],
        "mutexes_created": [
            "CTF.LBES.MutexDefaultS-1-5-21-1482476501-1645522239-1417001333-500",
            "CTF.Compart.MutexDefaultS-1-5-21-1482476501-1645522239-1417001333-500",
            "CTF.Asm.MutexDefaultS-1-5-21-1482476501-1645522239-1417001333-500",
            "CTF.Layouts.MutexDefaultS-1-5-21-1482476501-1645522239-1417001333-500",
            "CTF.TMD.MutexDefaultS-1-5-21-1482476501-1645522239-1417001333-500",
            "CTF.TimListCache.FMPDefaultS-1-5-21-1482476501-1645522239-1417001333-500MUTEX.DefaultS-1-5-21-1482476501-1645522239-1417001333-500",
            "MSCTF.Shared.MUTEX.EBH"
        ],
        "mutexes_opened": [
            "ShimCacheMutex"
        ],
        "processes_terminated": [
            "C:\\Documents and Settings\\Administrator\\Local Settings\\Temp\\EB93A6\\996E.exe"
        ],
        "processes_tree": [
            {
                "name": "****.exe",
                "process_id": "1036"
            },
            {
                "name": "9f9e74241d59eccfe7040bfdcbbceacb374eda397cc53a4197b59e4f6f380a91.exe",
                "process_id": "2340"
            }
        ],
        "registry_keys_opened": [
            "\\Registry\\Machine\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\996E.exe",
            "\\Registry\\MACHINE\\System\\CurrentControlSet\\Control\\SafeBoot\\Option",
            "\\Registry\\Machine\\Software\\Policies\\Microsoft\\Windows\\Safer\\CodeIdentifiers",
            "\\REGISTRY\\MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\Safer\\CodeIdentifiers\\TransparentEnabled",
            "\\REGISTRY\\USER\\S-1-5-21-1482476501-1645522239-1417001333-500\\Software\\Policies\\Microsoft\\Windows\\Safer\\CodeIdentifiers",
            "\\Registry\\Machine\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\COMCTL32.dll",
            "\\Registry\\Machine\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\SHELL32.dll",
            "\\Registry\\Machine\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\comdlg32.dll",
            "\\Registry\\Machine\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\WINMM.dll",
            "\\REGISTRY\\MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Drivers32\\wave",
            "\\REGISTRY\\MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Drivers32\\wave1",
            "\\REGISTRY\\MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Drivers32\\wave2",
            "\\REGISTRY\\MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Drivers32\\wave3",
            "\\REGISTRY\\MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Drivers32\\wave4",
            "\\REGISTRY\\MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Drivers32\\wave5"
        ],
        "tags": [
            "DIRECT_CPU_CLOCK_ACCESS",
            "RUNTIME_MODULES"
        ],
        "text_highlighted": [
            "&Open",
            "&Cancel",
            "&About",
            "Cate&gory:",
            "Host &Name (or IP address)",
            "&Port",
            "22",
            "Connection type:",
            "Ra&w",
            "&Telnet",
            "Rlog&in"
        ]
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
    "/files/{id}/behaviour_summary": {
      "get": {
        "tags": [
          "Private Files Behaviours"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "privatefilesidbehaviour-summary",
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
            "description": "File's SHA-256",
            "in": "path",
            "name": "id",
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
        "summary": "Get a summary of all behavior reports for a file"
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

← [Get a summary of all MITRE ATT&CK techniques observed in a file](get-summary-all-mitre-attack-techniques-observed-in-a-file.md) · [up](../README.md) · [Private Analyses](../private-analyses.md) →

*Archived from <https://gtidocs.virustotal.com/reference/privatefilesidbehaviour-summary>.*
