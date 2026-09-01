---
title: "powershell_info"
source: https://gtidocs.virustotal.com/reference/file-object-powershell-info
slug: file-object-powershell-info
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:42:27.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › powershell_info

---

# powershell_info

`powershell_info` shows information about [Powershell files](https://docs.microsoft.com/en-us/powershell/).

* `cmdlets`: <*list of strings*> cmdlets used in the script.
* `cmdlets_alias`: <*list of strings*> cmdlets alias used in the script.
* `dotnet_calls`: <*list of strings*> .Net calls used in the script.
* `functions`: <*list of strings*> function names defined in the script.
* `ps_variables`: <*list of strings*> variables used by the script.

```json PowerShell files
{
    "data": {
        "attributes": {
            "powershell_info": {
                "cmdlets": [
                    "<string>"
                ],
                "cmdlets_alias": [
                    "<string>"
                ],
                "dotnet_calls": [
                    "<string>"
                ],
                "functions": [
                    "<string>"
                ],
                "ps_variables": [
                    "<string>"
                ]
            }
        }
    }
}
```
```json Example
{
    "data": {
        "attributes": {
            "powershell_info": {
                "cmdlets": [
                    "add-type",
                    "get-process",
                    "get-wmiobject",
                    "new-object",
                    "remove-item"
                ],
                "cmdlets_alias": [
                    "Sleep",
                    "where"
                ],
                "dotnet_calls": [
                    "IO.Compression.CompressionMode",
                    "IO.File",
                    "System.Convert",
                    "System.Diagnostics.Process",
                    "System.Drawing.Graphics",
                    "System.Drawing.Imaging.Encoder"
                ],
                "functions": [
                    "CMDOS",
                    "CURRENT-instance",
                    "CompressedByteArray",
                    "DecompressedByteArray",
                    "info",
                    "process-m"
                ],
                "ps_variables": [
                    "$input",
                    "$null",
                    "$pid"
                ]
            }
        }
    }
}
```

---

← [detectiteasy](file-object-detectiteasy.md) · [up](../README.md) · [Files Behaviour](../file-behaviour-summary-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-powershell-info>.*
