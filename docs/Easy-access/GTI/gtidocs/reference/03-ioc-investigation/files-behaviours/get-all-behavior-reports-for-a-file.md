---
title: "Get all behavior reports for a file"
source: https://gtidocs.virustotal.com/reference/get-all-behavior-reports-for-a-file
slug: get-all-behavior-reports-for-a-file
section: reference
group: "IoC Investigation"
updatedAt: 2026-02-05T12:43:34.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Files Behaviours](../files-behaviours.md) › Get all behavior reports for a file

---

# get-all-behavior-reports-for-a-file

This endpoint returns behavioural information from each sandbox about the file.

This API call returns all fields contained in the [File behaviour](../../17-api-objects/file-behaviour-summary-object.md) object.

Note some of the entries have

* `has_html_report` if true you may fech the HTML [File behaviour](get-file-behaviour-html.md).
* `has_pcap` if true you may fech the PCAP [File behaviour](file_behaviours_pcap.md).

```json Example response
{
    "meta": {
        "count": 5
    },
    "data": [
        {
            "attributes": {
                "verdicts": [
                    "UNKNOWN_VERDICT"
                ],
                "has_pcap": false,
                "analysis_date": 1669409515,
                "processes_tree": [
                    {
                        "process_id": "2248",
                        "name": "%windir%\\System32\\svchost.exe -k WerSvcGroup"
                    },
                    {
                        "process_id": "2940",
                        "name": "wmiadap.exe /F /T /R"
                    },
                    {
                        "process_id": "2988",
                        "name": "%windir%\\system32\\wbem\\wmiprvse.exe"
                    },
                    {
                        "process_id": "2676",
                        "name": "%SAMPLEPATH%"
                    }
                ],
                "sandbox_name": "C2AE",
                "has_html_report": false,
                "processes_terminated": [
                    "%windir%\\System32\\svchost.exe -k WerSvcGroup",
                    "wmiadap.exe /F /T /R"
                ],
                "behash": "7eb58e30b74038daa9b31b5d9df78cf2",
                "has_evtx": false,
                "last_modification_date": 1669495931,
                "has_memdump": false
            },
            "type": "file_behaviour",
            "id": "edd0a64dc65087ffe453ca94b267169b39458a983b29ac31320fcaa983d0f97e_C2AE",
            "links": {
                "self": "https://www.virustotal.com/api/v3/file_behaviours/edd0a64dc65087ffe453ca94b267169b39458a983b29ac31320fcaa983d0f97e_C2AE"
            }
        },
        {
            "attributes": {
                "mitre_attack_techniques": [
                    {
                        "signature_description": "link function at runtime on Windows",
                        "id": "T1129",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "signature_description": "packed with UPX",
                        "id": "T1027.002",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "link function at runtime on Windows"
                            }
                        ],
                        "signature_description": "link function at runtime on Windows",
                        "id": "T1129",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "packed with UPX"
                            }
                        ],
                        "signature_description": "packed with UPX",
                        "id": "T1027.002",
                        "severity": "IMPACT_SEVERITY_INFO"
                    }
                ],
                "has_pcap": false,
                "analysis_date": 1669611166,
                "sandbox_name": "CAPA",
                "has_html_report": false,
                "behash": "76c6c8e44cd4f1dbddc0f6c2202c1480",
                "has_evtx": false,
                "signature_matches": [
                    {
                        "format": "SIG_FORMAT_CAPA",
                        "rule_src": "rule:\n  meta:\n    name: allocate memory\n    authors:\n      - 0x534a@mailbox.org\n    lib: true\n    scope: basic block\n    mbc:\n      - Memory::Allocate Memory [C0007]\n    examples:\n      - Practical Malware Analysis Lab 03-03.exe_:0x4010EA\n      # ntdll\n      - 563653399B82CD443F120ECEFF836EA3678D4CF11D9B351BB737573C2D856299:0x140001ABA\n  features:\n    - or:\n      - api: kernel32.VirtualAlloc\n      - api: kernel32.VirtualAllocEx\n      - api: kernel32.VirtualAllocExNuma\n      - api: kernel32.VirtualProtect\n      - api: kernel32.VirtualProtectEx\n      - api: NtAllocateVirtualMemory\n      - api: ZwAllocateVirtualMemory\n      - api: NtMapViewOfSection\n      - api: ZwMapViewOfSection\n",
                        "name": "allocate memory",
                        "authors": [
                            "0x534a@mailbox.org"
                        ]
                    },
                    {
                        "format": "SIG_FORMAT_CAPA",
                        "rule_src": "rule:\n  meta:\n    name: allocate RW memory\n    authors:\n      - 0x534a@mailbox.org\n    lib: true\n    scope: basic block\n    mbc:\n      - Memory::Allocate Memory [C0007]\n    examples:\n      - Practical Malware Analysis Lab 17-02.dll_:0x1000D10D\n  features:\n    - and:\n      - match: allocate memory\n      - number: 0x4 = PAGE_READWRITE\n",
                        "name": "allocate RW memory",
                        "authors": [
                            "0x534a@mailbox.org"
                        ]
                    },
                    {
                        "format": "SIG_FORMAT_CAPA",
                        "rule_src": "rule:\n  meta:\n    name: contain loop\n    authors:\n      - moritz.raabe@mandiant.com\n    lib: true\n    scope: function\n    examples:\n      - 08AC667C65D36D6542917655571E61C8:0x406EAA\n  features:\n    - or:\n      - characteristic: loop\n      - characteristic: tight loop\n      - characteristic: recursive call\n",
                        "name": "contain loop",
                        "authors": [
                            "moritz.raabe@mandiant.com"
                        ]
                    },
                    {
                        "rule_src": "rule:\n  meta:\n    name: terminate process\n    namespace: host-interaction/process/terminate\n    authors:\n      - moritz.raabe@mandiant.com\n      - michael.hunhoff@mandiant.com\n      - anushka.virgaonkar@mandiant.com\n    scope: function\n    mbc:\n      - Process::Terminate Process [C0018]\n    examples:\n      - C91887D861D9BD4A5872249B641BC9F9:0x401A77\n      - 9B7CCAA2AE6A5B96E3110EBCBC4311F6:0x10010307\n  features:\n    - or:\n      - api: System.Diagnostics.Process::Kill\n      - api: System.Diagnostics.Process::WaitForExit\n      - api: System.Diagnostics.Process::WaitForExitAsync\n      - and:\n        - optional:\n          - match: open process\n        - or:\n          - api: kernel32.TerminateProcess\n          - api: ntdll.NtTerminateProcess\n          - api: kernel32.ExitProcess\n",
                        "format": "SIG_FORMAT_CAPA",
                        "description": "host-interaction/process/terminate",
                        "name": "terminate process",
                        "authors": [
                            "moritz.raabe@mandiant.com",
                            "michael.hunhoff@mandiant.com",
                            "anushka.virgaonkar@mandiant.com"
                        ]
                    },
                    {
                        "rule_src": "rule:\n  meta:\n    name: link function at runtime on Windows\n    namespace: linking/runtime-linking\n    authors:\n      - moritz.raabe@mandiant.com\n    scope: function\n    att&ck:\n      - Execution::Shared Modules [T1129]\n    examples:\n      - 9324D1A8AE37A36AE560C37448C9705A:0x404130\n      - Practical Malware Analysis Lab 01-04.exe_:0x401350\n  features:\n    - and:\n      - os: windows\n      - or:\n        - api: kernel32.LoadLibrary\n        - api: kernel32.GetModuleHandle\n        - api: kernel32.GetModuleHandleEx\n        - api: ntdll.LdrLoadDll\n      - or:\n        - api: kernel32.GetProcAddress\n        - api: ntdll.LdrGetProcedureAddress\n      - optional:\n        - characteristic: indirect call\n",
                        "format": "SIG_FORMAT_CAPA",
                        "description": "linking/runtime-linking",
                        "name": "link function at runtime on Windows",
                        "authors": [
                            "moritz.raabe@mandiant.com"
                        ]
                    },
                    {
                        "rule_src": "rule:\n  meta:\n    name: packed with UPX\n    namespace: anti-analysis/packer/upx\n    authors:\n      - william.ballenthin@mandiant.com\n    scope: file\n    att&ck:\n      - Defense Evasion::Obfuscated Files or Information::Software Packing [T1027.002]\n    mbc:\n      - Anti-Static Analysis::Software Packing::UPX [F0001.008]\n    examples:\n      - CD2CBA9E6313E8DF2C1273593E649682\n      - Practical Malware Analysis Lab 01-02.exe_:0x0401000\n  features:\n    - or:\n      - and:\n        - format: pe\n        - or:\n          - section: UPX0\n          - section: UPX1\n      - and:\n        - format: elf\n        - or:\n          - string: \"UPX!\"\n",
                        "format": "SIG_FORMAT_CAPA",
                        "description": "anti-analysis/packer/upx",
                        "name": "packed with UPX",
                        "authors": [
                            "william.ballenthin@mandiant.com"
                        ]
                    },
                    {
                        "rule_src": "rule:\n  meta:\n    name: contain a resource (.rsrc) section\n    namespace: executable/pe/section/rsrc\n    authors:\n      - moritz.raabe@mandiant.com\n    scope: file\n    examples:\n      - A933A1A402775CFA94B6BEE0963F4B46:0x41fd25\n  features:\n    - section: .rsrc\n",
                        "format": "SIG_FORMAT_CAPA",
                        "description": "executable/pe/section/rsrc",
                        "name": "contain a resource (.rsrc) section",
                        "authors": [
                            "moritz.raabe@mandiant.com"
                        ]
                    },
                    {
                        "rule_src": "rule:\n  meta:\n    name: (internal) packer file limitation\n    namespace: internal/limitation/file\n    authors:\n      - william.ballenthin@mandiant.com\n    description: |\n      This sample appears to be packed.\n\n      Packed samples have often been obfuscated to hide their logic.\n      capa cannot handle obfuscation well. This means the results may be misleading or incomplete.\n      If possible, you should try to unpack this input file before analyzing it with capa.\n    scope: file\n    examples:\n      - CD2CBA9E6313E8DF2C1273593E649682\n  features:\n    - or:\n      - match: anti-analysis/packer\n",
                        "format": "SIG_FORMAT_CAPA",
                        "description": "This sample appears to be packed.\n\nPacked samples have often been obfuscated to hide their logic.\ncapa cannot handle obfuscation well. This means the results may be misleading or incomplete.\nIf possible, you should try to unpack this input file before analyzing it with capa.\n",
                        "name": "(internal) packer file limitation",
                        "authors": [
                            "william.ballenthin@mandiant.com"
                        ]
                    }
                ],
                "last_modification_date": 1676671463,
                "has_memdump": false
            },
            "type": "file_behaviour",
            "id": "edd0a64dc65087ffe453ca94b267169b39458a983b29ac31320fcaa983d0f97e_CAPA",
            "links": {
                "self": "https://www.virustotal.com/api/v3/file_behaviours/edd0a64dc65087ffe453ca94b267169b39458a983b29ac31320fcaa983d0f97e_CAPA"
            }
        },
        {
            "attributes": {
                "command_executions": [
                    "\"%SAMPLEPATH%\\setup-x86_64.exe\" ",
                    "\"%SAMPLEPATH%\\edd0a64dc65087ffe453ca94b267169b39458a983b29ac31320fcaa983d0f97e.exe\" ",
                    "C:\\Windows\\System32\\wuapihost.exe -Embedding",
                    "\"%SAMPLEPATH%\\file.exe\" "
                ],
                "ip_traffic": [
                    {
                        "transport_layer_protocol": "UDP",
                        "destination_ip": "a83f:8110:e5c0:7cff:e5c0:7cff:e5c0:7cff",
                        "destination_port": 53
                    },
                    {
                        "transport_layer_protocol": "TCP",
                        "destination_ip": "23.216.147.76",
                        "destination_port": 443
                    },
                    {
                        "transport_layer_protocol": "TCP",
                        "destination_ip": "20.99.133.109",
                        "destination_port": 443
                    },
                    {
                        "transport_layer_protocol": "TCP",
                        "destination_ip": "23.216.147.64",
                        "destination_port": 443
                    },
                    {
                        "transport_layer_protocol": "TCP",
                        "destination_ip": "20.99.184.37",
                        "destination_port": 443
                    },
                    {
                        "transport_layer_protocol": "TCP",
                        "destination_ip": "13.107.4.50",
                        "destination_port": 80
                    },
                    {
                        "transport_layer_protocol": "TCP",
                        "destination_ip": "104.86.182.43",
                        "destination_port": 443
                    },
                    {
                        "transport_layer_protocol": "UDP",
                        "destination_ip": "a83f:8110:0:0:100:0:1800:0",
                        "destination_port": 53
                    },
                    {
                        "transport_layer_protocol": "UDP",
                        "destination_ip": "a83f:8110:2c02:0:0:0:0:0",
                        "destination_port": 53
                    },
                    {
                        "transport_layer_protocol": "TCP",
                        "destination_ip": "23.35.98.25",
                        "destination_port": 443
                    },
                    {
                        "transport_layer_protocol": "UDP",
                        "destination_ip": "a83f:8110:1a1a:1aff:1a1a:1aff:1a1a:1aff",
                        "destination_port": 53
                    },
                    {
                        "transport_layer_protocol": "UDP",
                        "destination_ip": "a83f:8110:0:0:1400:1400:2800:3800",
                        "destination_port": 53
                    },
                    {
                        "transport_layer_protocol": "TCP",
                        "destination_ip": "23.40.197.184",
                        "destination_port": 443
                    },
                    {
                        "transport_layer_protocol": "UDP",
                        "destination_ip": "a83f:8110:8d00:100:89:9598:0:8b",
                        "destination_port": 53
                    },
                    {
                        "transport_layer_protocol": "UDP",
                        "destination_ip": "192.168.0.14",
                        "destination_port": 137
                    },
                    {
                        "transport_layer_protocol": "UDP",
                        "destination_ip": "a83f:8110:2800:0:2800:0:1800:0",
                        "destination_port": 53
                    },
                    {
                        "transport_layer_protocol": "UDP",
                        "destination_ip": "a83f:8110:6219:d901:71a4:4e8e:6219:d901",
                        "destination_port": 53
                    },
                    {
                        "transport_layer_protocol": "UDP",
                        "destination_ip": "a83f:8110:4c00:5300:4900:2000:4500:6d00",
                        "destination_port": 53
                    },
                    {
                        "transport_layer_protocol": "UDP",
                        "destination_ip": "a83f:8110:6c00:6c00:2c00:2d00:3300:3600",
                        "destination_port": 53
                    },
                    {
                        "transport_layer_protocol": "UDP",
                        "destination_ip": "a83f:8110:2800:1800:4000:1800:1800:100",
                        "destination_port": 53
                    },
                    {
                        "transport_layer_protocol": "UDP",
                        "destination_ip": "a83f:8110:100:300:4170:7058:3677:366e",
                        "destination_port": 53
                    },
                    {
                        "transport_layer_protocol": "UDP",
                        "destination_ip": "a83f:8110:4600:6900:7200:6500:7700:6100",
                        "destination_port": 53
                    },
                    {
                        "transport_layer_protocol": "UDP",
                        "destination_ip": "a83f:8110:3e05:0:0:0:3e05:0",
                        "destination_port": 53
                    },
                    {
                        "transport_layer_protocol": "UDP",
                        "destination_ip": "192.168.0.19",
                        "destination_port": 137
                    },
                    {
                        "transport_layer_protocol": "UDP",
                        "destination_ip": "192.168.0.1",
                        "destination_port": 137
                    }
                ],
                "processes_injected": [
                    "\\\\?\\C:\\Windows\\system32\\wbem\\WMIADAP.EXE"
                ],
                "processes_tree": [
                    {
                        "process_id": "2888",
                        "name": "%WINDIR%\\explorer.exe",
                        "children": [
                            {
                                "process_id": "3532",
                                "name": "%SAMPLEPATH%\\setup-x86_64.exe"
                            }
                        ]
                    }
                ],
                "has_pcap": false,
                "analysis_date": 1669405151,
                "sandbox_name": "Microsoft Sysinternals",
                "has_html_report": false,
                "processes_terminated": [
                    "C:\\Windows\\System32\\wuapihost.exe"
                ],
                "behash": "5e435041f7d5d1981aa0a0d9419bcd97",
                "files_deleted": [
            
                    "C:\\Windows\\System32\\spp\\store\\2.0\\cache\\cache.dat",
       
                ],
                "files_dropped": [
                   
                ],
                "has_evtx": false,
                "last_modification_date": 1677046497,
                "has_memdump": false,
                "processes_created": [
                    "%SAMPLEPATH%\\setup-x86_64.exe",
                    "%SAMPLEPATH%\\edd0a64dc65087ffe453ca94b267169b39458a983b29ac31320fcaa983d0f97e.exe",
                    "C:\\Windows\\System32\\wuapihost.exe",
                    "%SAMPLEPATH%\\file.exe"
                ],
                "modules_loaded": [
                    "%SAMPLEPATH%\\edd0a64dc65087ffe453ca94b267169b39458a983b29ac31320fcaa983d0f97e.exe",
                    "%SAMPLEPATH%\\file.exe"
                ]
            },
            "type": "file_behaviour",
            "id": "edd0a64dc65087ffe453ca94b267169b39458a983b29ac31320fcaa983d0f97e_Microsoft Sysinternals",
            "links": {
                "self": "https://www.virustotal.com/api/v3/file_behaviours/edd0a64dc65087ffe453ca94b267169b39458a983b29ac31320fcaa983d0f97e_Microsoft Sysinternals"
            }
        },
        {
            "attributes": {
                "registry_keys_opened": [
                    "HKLM\\Software\\Cygwin\\setup",
                    "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\LanguagePack\\DataStore_V1.0",
                    "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\LanguagePack\\DataStore_V1.0\\Disable",
                    "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\LanguagePack\\DataStore_V1.0\\DataFilePath",
                    "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\LanguagePack\\SurrogateFallback",
                    "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\LanguagePack\\SurrogateFallback\\Arial",
                    "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\FontLink\\SystemLink"
                ],
                "calls_highlighted": [
                    "GetTickCount"
                ],
                "tags": [
                    "DIRECT_CPU_CLOCK_ACCESS",
                    "RUNTIME_MODULES"
                ],
                "has_pcap": false,
                "analysis_date": 1669405225,
                "sandbox_name": "VirusTotal Jujubox",
                "has_html_report": true,
                "behash": "2563a14030568b9376fcc24af405d1c8",
                "has_evtx": false,
                "text_highlighted": [
                    "Cygwin Setup",
                    "Cygwin Net Release Setup Program",
                    "This setup program is used for the initial installation of the Cygwin environment as well as all subsequent updates. The pages that follow will guide you through the installation.\n\nPlease note that we",
                    "Setup version 2.924 (64 bit)",
                    "Copyright 2000-2022",
                    "https://cygwin.com",
                    "Finish",
                    "Help"
                ],
                "services_opened": [
                    "AvSynMgr"
                ],
                "last_modification_date": 1669405226,
                "has_memdump": false,
                "modules_loaded": [
                    "KERNEL32.DLL",
                    "ADVAPI32.dll",
                    "COMCTL32.dll",
                    "GDI32.dll",
                    "msvcrt.dll",
                    "ntdll.dll",
                    "ole32.dll",
                    "PSAPI.DLL",
                    "SHELL32.dll",
                    "SHLWAPI.dll",
                    "USER32.dll",
                    "WININET.dll",
                    "WS2_32.dll",
                    "C:\\Windows\\system32\\tzres.dll",
                    "CRYPTBASE.dll",
                    "CLBCatQ.DLL",
                    "C:\\Windows\\system32\\shell32.dll",
                    "UxTheme.dll",
                    "IMM32.dll",
                    "C:\\Windows\\system32\\ole32.dll"
                ],
                "files_opened": [
                    "/etc\\system-fips",
                    "C:\\Windows\\system32\\tzres.dll",
                    "C:\\Users\\<USER>\\Downloads\\setup.rc",
                    "C:\\cygwin64\\etc\\setup\\setup.rc",
                    "C:\\Windows\\system32\\rpcss.dll",
                    "C:\\Windows\\WinSxS\\amd64_microsoft.windows.c..-controls.resources_6595b64144ccf1df_6.0.7600.16385_en-us_106f9be843a9b4e3",
                    "C:\\Windows\\WinSxS\\amd64_microsoft.windows.c..-controls.resources_6595b64144ccf1df_6.0.7600.16385_en-us_106f9be843a9b4e3\\COMCTL32.dll.mui",
                    "C:\\Windows\\system32\\en-US\\USER32.dll.mui",
                    "C:\\Windows\\system32\\UxTheme.dll",
                    "C:\\Windows\\WinSxS\\amd64_microsoft.windows.common-controls_6595b64144ccf1df_6.0.7601.24483_none_e372d88f30fbb845",
                    "C:\\Windows\\Fonts\\staticcache.dat"
                ]
            },
            "type": "file_behaviour",
            "id": "edd0a64dc65087ffe453ca94b267169b39458a983b29ac31320fcaa983d0f97e_VirusTotal Jujubox",
            "links": {
                "self": "https://www.virustotal.com/api/v3/file_behaviours/edd0a64dc65087ffe453ca94b267169b39458a983b29ac31320fcaa983d0f97e_VirusTotal Jujubox"
            }
        },
        {
            "attributes": {
                "signature_matches": [
                    {
                        "id": "825",
                        "match_data": [
                            "More than 3 window changes detected"
                        ],
                        "description": "Found graphical window changes (likely an installer)",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "418",
                        "match_data": [
                            "File size 1381395 > 1048576"
                        ],
                        "description": "Submission file is bigger than most known malware samples",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "509",
                        "refs": [
                            {
                                "ref": "#registry_keys_opened",
                                "value": "HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\Windows\\Safer\\CodeIdentifiers"
                            }
                        ],
                        "match_data": [
                            "HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\Windows\\Safer\\CodeIdentifiers"
                        ],
                        "description": "Reads software policies",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "342",
                        "match_data": [
                            "section name: UPX0",
                            "section name: UPX1"
                        ],
                        "description": "Sample is packed with UPX",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "767",
                        "match_data": [
                            "Next >"
                        ],
                        "description": "Found GUI installer (many successful clicks)",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "206",
                        "refs": [
                            {
                                "ref": "#dns_lookups",
                                "value": "queries for: cygwin.com"
                            }
                        ],
                        "match_data": [
                            "queries for: cygwin.com"
                        ],
                        "description": "Performs DNS lookups",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "715",
                        "match_data": [
                            "clean0.winEXE@1/1@1/1"
                        ],
                        "description": "Classification label",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "625",
                        "match_data": [
                            "HTTP traffic on port 49736 -> 443",
                            "HTTP traffic on port 443 -> 49736"
                        ],
                        "description": "Uses HTTPS",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "624",
                        "description": "Uses HTTPS for network communication, use the 'Proxy HTTPS (port 443) to read its encrypted data' cookbook for further analysis",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "513",
                        "match_data": [
                            "window name: SysTabControl32"
                        ],
                        "description": "Executable creates window controls seldom found in malware",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "507",
                        "match_data": [
                            "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\CLSID\\{00021401-0000-0000-C000-000000000046}\\InProcServer32"
                        ],
                        "description": "Uses an in-process (OLE) Automation server",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "263",
                        "refs": [
                            {
                                "ref": "#memory_dumps",
                                "value": "program.exe, 00000000.00000002.4727768602.00000000001B5000.00000004.00000020.00020000.00000000.sdmp"
                            },
                            {
                                "ref": "#memory_dumps",
                                "value": "program.exe, 00000000.00000002.4727292270.0000000000168000.00000004.00000020.00020000.00000000.sdmp"
                            }
                        ],
                        "match_data": [
                            "Hyper-V RAW",
                            "Hyper-V RAW "
                        ],
                        "description": "May try to detect the virtual machine to hinder analysis (VM artifact strings found in memory)",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "328",
                        "match_data": [
                            "C:\\Windows\\System32\\drivers\\etc\\hosts"
                        ],
                        "description": "Reads the hosts file",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "768",
                        "match_data": [
                            "Number of UI elements: 16",
                            "Number of UI elements: 19",
                            "Number of UI elements: 25",
                            "Number of UI elements: 28",
                            "Number of UI elements: 30"
                        ],
                        "description": "Found window with many clickable UI elements (buttons, textforms, scrollbars etc)",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "433",
                        "match_data": [
                            "Section: UPX1 ZLIB complexity 0.9993296606864275"
                        ],
                        "description": "PE file has section (not .text) which is very likely to contain packed code (zlib compression ratio < 0.011)",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "238",
                        "match_data": [
                            "ftp://cygwin.osuosl.org",
                            "ftp://ftp-stud.hs-esslingen.de/pub/Mirrors/sources.redhat.com/cygwin/https://l",
                            "ftp://ftp.byfly.by",
                            "ftp://ftp.eq.uc.pt",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/http://mc.",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/http://mw",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/https://ftj",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/or",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/r",
                            "ftp://ftp.fau.de/cygwin/",
                            "ftp://ftp.fau.desl.orgor",
                            "ftp://ftp.funet.fi/pub/mirrors/sourceware.org/pub/cygwin/",
                            "ftp://ftp.ha",
                            "ftp://ftp.halifax.rwth-aachen.de/cygwin/.net/",
                            "ftp://ftp.halifax.rwth-aachen.dehttps:/",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/http://cyG",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/http://f",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/http://l",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/http://s",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/https://",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/https://9",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/n/",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/or",
                            "ftp://ftp.inf.tu-dresden.dehttps://",
                            "ftp://ftp.inf.tu-dresden.deor",
                            "ftp://ftp.jaist.ac.jp/pub/cygwin/",
                            "ftp://ftp.jaist.ac.jpt",
                            "ftp://ftp.kaist.ac.kr/cygwin/",
                            "ftp://ftp.kaist.ac.kr/cygwin/https://",
                            "ftp://ftp.kaist.ac.kr/cygwin/p",
                            "ftp://ftp.kaist.ac.kr/cygwin/site",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/http://c",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/http://fK)t",
                            "ftp://ftp.l",
                            "ftp://ftp.l(-Z",
                            "ftp://ftp.lf1",
                            "ftp://ftp.lip6.fr/pub/cygwin/",
                            "ftp://ftp.lip6.fr/pub/cygwin/rror",
                            "ftp://ftp.mirrorservice.orghttp://mirro",
                            "ftp://ftp.mirrorservice.orgn",
                            "ftp://ftp.mirrorservice.orgygwin/",
                            "ftp://ftp.mm",
                            "ftp://ftp.muug.ca",
                            "ftp://ftp.muug.ca/mirror/cygwin/",
                            "ftp://ftp.n",
                            "ftp://ftp.ntu.edu.tw/pub/cygwin/s",
                            "ftp://ftp.rnl.tecnico.ulisboa.pt/pub/cygwin/irror",
                            "ftp://ftp.snt.utwente.nl/pub/software/cygwin/",
                            "ftp://ftp.snt.utwente.nlftp",
                            "ftp://ftp.snt.utwente.nltp",
                            "ftp://ftp.yz.yamagata-u.ac.jp",
                            "ftp://ftp.yz.yamagata-u.ac.jphttps://ft",
                            "ftp://linux.rz.ruhr-uni-bochum.de",
                            "ftp://linux.rz.ruhr-uni-bochum.dehttp:/Z/",
                            "ftp://mirror.cs.vt.edu/pub/cygwin/cygwin/gwin",
                            "ftp://mirror.csclub.uwaterloo.ca/cygwin/ygwin",
                            "ftp://mirror.internode.on.net/pub/cygwin/gwin",
                            "ftp://mirror.internode.on.net/pub/cygwin/http",
                            "ftp://mirror.lagoon.nc",
                            "ftp://mirror.lagoon.nc/cygwin/",
                            "ftp://mirror.lagoon.nc/cygwin/.ca",
                            "ftp://mirror.lagoon.nc/cygwin/https://",
                            "ftp://mirror.lagoon.nc/cygwin/https://c:34",
                            "ftp://mirrors.dotsrc.org/mirrors/cygwin/p",
                            "ftp://mirrors.netix.net/cygwin/http://f",
                            "ftp://mirrors.netix.net/cygwin/http://w",
                            "ftp://mirrors.sonic.net/cygwin/http://f",
                            "ftp://mirrors.sonic.net/cygwin/https://9",
                            "ftp://mirrors.xmission.com/cygwin/",
                            "ftp://mirrors.xmission.comwin",
                            "ftp://sourceware.org/ftp://sources.redhat.com/ftp://gcc.gnu.org/",
                            "ftp://sunsite.icm.edu.pl",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/http://f",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/nt",
                            "http://ac.economia.gob.mx/cps.html0",
                            "http://ac.economia.gob.mx/last.crl0G",
                            "http://acedicom.edicomgroup.com/doc0",
                            "http://acraiz.icpbrasil.gov.br/DPCacraiz.pdf0?",
                            "http://acraiz.icpbrasil.gov.br/LCRacraizv1.crl0",
                            "http://acraiz.icpbrasil.gov.br/LCRacraizv2.crl0",
                            "http://apps.identrust.com/roots/dstrootcax3.p7c0",
                            "http://ca.disig.sk/ca/crl/ca_disig.crl0",
                            "http://ca.mtin.es/mtin/DPCyPoliticas0",
                            "http://ca.mtin.es/mtin/DPCyPoliticas0g",
                            "http://ca.mtin.es/mtin/crl/MTINAutoridadRaiz03",
                            "http://ca.mtin.es/mtin/ocsp0",
                            "http://ca2.mtin.es/mtin/crl/MTINAutoridadRaiz0",
                            "http://certificates.starfieldtech.com/repository/1604",
                            "http://certs.oati.net/repository/OATICA2.crl0",
                            "http://certs.oati.net/repository/OATICA2.crt0",
                            "http://certs.oaticerts.com/repository/OATICA2.crl",
                            "http://certs.oaticerts.com/repository/OATICA2.crt08",
                            "http://cps.chambersign.org/cps/chambersignroot.html0",
                            "http://cps.chambersign.org/cps/chambersroot.html0",
                            "http://cps.letsencrypt.org0",
                            "http://cps.root-x1.letsencrypt.org0",
                            "http://cps.siths.se/sithsrootcav1.html0",
                            "http://crl.certigna.fr/certignarootca.crl01",
                            "http://crl.chambersign.org/chambersignroot.crl0",
                            "http://crl.chambersign.org/chambersroot.crl0",
                            "http://crl.comodoca.com/AAACertificateServices.crl06",
                            "http://crl.defence.gov.au/pki0",
                            "http://crl.dhimyotis.com/certignarootca.crl0",
                            "http://crl.globalsign.net/root-r2.crl0",
                            "http://crl.identrust.com/DSTROOTCAX3CRL.crl0",
                            "http://crl.oces.trust2408.com/oces.crl0",
                            "http://crl.securetrust.com/SGCA.crl0",
                            "http://crl.securetrust.com/STCA.crl0",
                            "http://crl.ssc.lt/root-a/cacrl.crl0",
                            "http://crl.ssc.lt/root-b/cacrl.crl0",
                            "http://crl.ssc.lt/root-c/cacrl.crl0",
                            "http://crl.xrampsecurity.com/XGCA.crl0",
                            "http://crl1.comsign.co.il/crl/comsignglobalrootca.crl0",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/CABD2A79A1076A31F21D253635CB0",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/authrootstl.cab",
                            "http://ctldl.windowsupdate.com:80/msdownload/update/v3/static/trustedr/en/CABD2A79A1076A31F21D253635",
                            "http://cygwin.cathedral-",
                            "http://cygwin.cathedral-10",
                            "http://cygwin.cathedral-N/",
                            "http://cygwin.cathedral-networks.org",
                            "http://cygwin.cathedral-networks.org$",
                            "http://cygwin.cathedral-networks.org&",
                            "http://cygwin.cathedral-networks.org.noG3",
                            "http://cygwin.cathedral-networks.org/",
                            "http://cygwin.cathedral-networks.org/)",
                            "http://cygwin.cathedral-networks.org/-u",
                            "http://cygwin.cathedral-networks.org/.",
                            "http://cygwin.cathedral-networks.org/.d",
                            "http://cygwin.cathedral-networks.org/.iK",
                            "http://cygwin.cathedral-networks.org/.n",
                            "http://cygwin.cathedral-networks.org//",
                            "http://cygwin.cathedral-networks.org//%M",
                            "http://cygwin.cathedral-networks.org///",
                            "http://cygwin.cathedral-networks.org///b",
                            "http://cygwin.cathedral-networks.org//5-",
                            "http://cygwin.cathedral-networks.org//I",
                            "http://cygwin.cathedral-networks.org//T",
                            "http://cygwin.cathedral-networks.org//U",
                            "http://cygwin.cathedral-networks.org//c",
                            "http://cygwin.cathedral-networks.org//f",
                            "http://cygwin.cathedral-networks.org//fB",
                            "http://cygwin.cathedral-networks.org//fQ",
                            "http://cygwin.cathedral-networks.org//l",
                            "http://cygwin.cathedral-networks.org/0",
                            "http://cygwin.cathedral-networks.org/1",
                            "http://cygwin.cathedral-networks.org/1-",
                            "http://cygwin.cathedral-networks.org/3)",
                            "http://cygwin.cathedral-networks.org/5",
                            "http://cygwin.cathedral-networks.org/7",
                            "http://cygwin.cathedral-networks.org/8",
                            "http://cygwin.cathedral-networks.org/:/l",
                            "http://cygwin.cathedral-networks.org/;34",
                            "http://cygwin.cathedral-networks.org/;cygwin.cathedral-networks.org;Europe;Norway;noshow",
                            "http://cygwin.cathedral-networks.org/=",
                            "http://cygwin.cathedral-networks.org/=M",
                            "http://cygwin.cathedral-networks.org/?/",
                            "http://cygwin.cathedral-networks.org/A",
                            "http://cygwin.cathedral-networks.org/D",
                            "http://cygwin.cathedral-networks.org/E3",
                            "http://cygwin.cathedral-networks.org/F(x",
                            "http://cygwin.cathedral-networks.org/J",
                            "http://cygwin.cathedral-networks.org/J(t",
                            "http://cygwin.cathedral-networks.org/L-",
                            "http://cygwin.cathedral-networks.org/Q.",
                            "http://cygwin.cathedral-networks.org/T3",
                            "http://cygwin.cathedral-networks.org/W8Z",
                            "http://cygwin.cathedral-networks.org/X",
                            "http://cygwin.cathedral-networks.org/Z",
                            "http://cygwin.cathedral-networks.org/_",
                            "http://cygwin.cathedral-networks.org/a3",
                            "http://cygwin.cathedral-networks.org/am",
                            "http://cygwin.cathedral-networks.org/au",
                            "http://cygwin.cathedral-networks.org/b/A3",
                            "http://cygwin.cathedral-networks.org/cy",
                            "http://cygwin.cathedral-networks.org/d",
                            "http://cygwin.cathedral-networks.org/de",
                            "http://cygwin.cathedral-networks.org/dh",
                            "http://cygwin.cathedral-networks.org/e8(",
                            "http://cygwin.cathedral-networks.org/et",
                            "http://cygwin.cathedral-networks.org/eta1",
                            "http://cygwin.cathedral-networks.org/ez",
                            "http://cygwin.cathedral-networks.org/fs",
                            "http://cygwin.cathedral-networks.org/ft",
                            "http://cygwin.cathedral-networks.org/ftP-",
                            "http://cygwin.cathedral-networks.org/ftp",
                            "http://cygwin.cathedral-networks.org/hk",
                            "http://cygwin.cathedral-networks.org/i",
                            "http://cygwin.cathedral-networks.org/i&e",
                            "http://cygwin.cathedral-networks.org/ia",
                            "http://cygwin.cathedral-networks.org/inF",
                            "http://cygwin.cathedral-networks.org/inG",
                            "http://cygwin.cathedral-networks.org/inm",
                            "http://cygwin.cathedral-networks.org/ir?",
                            "http://cygwin.cathedral-networks.org/k",
                            "http://cygwin.cathedral-networks.org/k.",
                            "http://cygwin.cathedral-networks.org/lf1",
                            "http://cygwin.cathedral-networks.org/lyT",
                            "http://cygwin.cathedral-networks.org/m",
                            "http://cygwin.cathedral-networks.org/m0",
                            "http://cygwin.cathedral-networks.org/n",
                            "http://cygwin.cathedral-networks.org/oB-f",
                            "http://cygwin.cathedral-networks.org/os",
                            "http://cygwin.cathedral-networks.org/p",
                            "http://cygwin.cathedral-networks.org/p.n",
                            "http://cygwin.cathedral-networks.org/p1",
                            "http://cygwin.cathedral-networks.org/p2",
                            "http://cygwin.cathedral-networks.org/q",
                            "http://cygwin.cathedral-networks.org/r.",
                            "http://cygwin.cathedral-networks.org/rgm",
                            "http://cygwin.cathedral-networks.org/rs",
                            "http://cygwin.cathedral-networks.org/s",
                            "http://cygwin.cathedral-networks.org/sI-",
                            "http://cygwin.cathedral-networks.org/ter.by",
                            "http://cygwin.cathedral-networks.org/th-aachen.derg9",
                            "http://cygwin.cathedral-networks.org/un",
                            "http://cygwin.cathedral-networks.org/us",
                            "http://cygwin.cathedral-networks.org/ux#",
                            "http://cygwin.cathedral-networks.org/x(j",
                            "http://cygwin.cathedral-networks.org/x.:(",
                            "http://cygwin.cathedral-networks.org/y",
                            "http://cygwin.cathedral-networks.org/yd2",
                            "http://cygwin.cathedral-networks.org/z(d",
                            "http://cygwin.cathedral-networks.org3.",
                            "http://cygwin.cathedral-networks.org5",
                            "http://cygwin.cathedral-networks.org:",
                            "http://cygwin.cathedral-networks.org://",
                            "http://cygwin.cathedral-networks.org://F2",
                            "http://cygwin.cathedral-networks.org://M",
                            "http://cygwin.cathedral-networks.orgF",
                            "http://cygwin.cathedral-networks.orgF-",
                            "http://cygwin.cathedral-networks.orgKonk",
                            "http://cygwin.cathedral-networks.orgP",
                            "http://cygwin.cathedral-networks.orga0",
                            "http://cygwin.cathedral-networks.orgala",
                            "http://cygwin.cathedral-networks.orgcew",
                            "http://cygwin.cathedral-networks.orgck",
                            "http://cygwin.cathedral-networks.orgcygX2",
                            "http://cygwin.cathedral-networks.orgetn/",
                            "http://cygwin.cathedral-networks.orgf",
                            "http://cygwin.cathedral-networks.orgf(X",
                            "http://cygwin.cathedral-networks.orgirr",
                            "http://cygwin.cathedral-networks.orgjp",
                            "http://cygwin.cathedral-networks.orgk",
                            "http://cygwin.cathedral-networks.orgkBS",
                            "http://cygwin.cathedral-networks.orglit",
                            "http://cygwin.cathedral-networks.orgn",
                            "http://cygwin.cathedral-networks.orgn/",
                            "http://cygwin.cathedral-networks.orgn/:M",
                            "http://cygwin.cathedral-networks.orgn/qBi",
                            "http://cygwin.cathedral-networks.orgnf.=6P",
                            "http://cygwin.cathedral-networks.orgp.m",
                            "http://cygwin.cathedral-networks.orgp6",
                            "http://cygwin.cathedral-networks.orgr",
                            "http://cygwin.cathedral-networks.orgree",
                            "http://cygwin.cathedral-networks.orgror",
                            "http://cygwin.cathedral-networks.orgt",
                            "http://cygwin.cathedral-networks.orgta-I2",
                            "http://cygwin.cathedral-networks.orgto",
                            "http://cygwin.cathedral-networks.orgu.",
                            "http://cygwin.cathedral-networks.orgv1",
                            "http://cygwin.cathedral-networks.orgv3",
                            "http://cygwin.cathedral-networks.orgw",
                            "http://cygwin.mbwarez",
                            "http://cygwin.mbwarez.dk",
                            "http://cygwin.mbwarez.dk#",
                            "http://cygwin.mbwarez.dk(",
                            "http://cygwin.mbwarez.dk)",
                            "http://cygwin.mbwarez.dk-bochum.dea.A",
                            "http://cygwin.mbwarez.dk-bochum.dee;&",
                            "http://cygwin.mbwarez.dk-bochum.dein/s",
                            "http://cygwin.mbwarez.dk.acc.umu.se/miri",
                            "http://cygwin.mbwarez.dk.aun/",
                            "http://cygwin.mbwarez.dk.auwin/",
                            "http://cygwin.mbwarez.dk.by/pub/mirrors",
                            "http://cygwin.mbwarez.dk.byom/cygwin/",
                            "http://cygwin.mbwarez.dk.de/cygwin/n/",
                            "http://cygwin.mbwarez.dk.iij.ad.jp",
                            "http://cygwin.mbwarez.dk.net/edu.cn",
                            "http://cygwin.mbwarez.dk.org/mirrors/cy",
                            "http://cygwin.mbwarez.dk.orgso.netsl.1",
                            "http://cygwin.mbwarez.dk/",
                            "http://cygwin.mbwarez.dk/#f",
                            "http://cygwin.mbwarez.dk/$",
                            "http://cygwin.mbwarez.dk/.ac.nz.tw/pub",
                            "http://cygwin.mbwarez.dk/.ac.nzn/",
                            "http://cygwin.mbwarez.dk/.c",
                            "http://cygwin.mbwarez.dk/.cathedral-S3",
                            "http://cygwin.mbwarez.dk/.cn/cygwin/1",
                            "http://cygwin.mbwarez.dk/.de/pub/Mirrors/sources.redhat.com/cygwin/",
                            "http://cygwin.mbwarez.dk/.deode.on.netd",
                            "http://cygwin.mbwarez.dk/.iij.ad.jp",
                            "http://cygwin.mbwarez.dk/.jpcygwin/",
                            "http://cygwin.mbwarez.dk/.lip6.frde/mm",
                            "http://cygwin.mbwarez.dk/.net",
                            "http://cygwin.mbwarez.dk/.netet23",
                            "http://cygwin.mbwarez.dk//",
                            "http://cygwin.mbwarez.dk//.cagwin/d.",
                            "http://cygwin.mbwarez.dk///mirror.isoc.",
                            "http://cygwin.mbwarez.dk//MoldovasA",
                            "http://cygwin.mbwarez.dk//cygw",
                            "http://cygwin.mbwarez.dk//cygwin/",
                            "http://cygwin.mbwarez.dk//cygwin/(/",
                            "http://cygwin.mbwarez.dk//cygwin//",
                            "http://cygwin.mbwarez.dk//cygwin///",
                            "http://cygwin.mbwarez.dk//cygwin/l.",
                            "http://cygwin.mbwarez.dk//cygwin/la",
                            "http://cygwin.mbwarez.dk//cygwin/n/",
                            "http://cygwin.mbwarez.dk//cygwin/nnk",
                            "http://cygwin.mbwarez.dk//cygwin/or",
                            "http://cygwin.mbwarez.dk//cygwin/rors.r",
                            "http://cygwin.mbwarez.dk//cygwin/t1l",
                            "http://cygwin.mbwarez.dk//gwin/.de",
                            "http://cygwin.mbwarez.dk//in//u",
                            "http://cygwin.mbwarez.dk//pub/cygwin/",
                            "http://cygwin.mbwarez.dk//win//m",
                            "http://cygwin.mbwarez.dk//win/2-",
                            "http://cygwin.mbwarez.dk//win/n/",
                            "http://cygwin.mbwarez.dk/0",
                            "http://cygwin.mbwarez.dk/1%",
                            "http://cygwin.mbwarez.dk/1K",
                            "http://cygwin.mbwarez.dk/://ftp.kr.free",
                            "http://cygwin.mbwarez.dk/://mirrors.ust)",
                            "http://cygwin.mbwarez.dk/;cygwin.mbwarez.dk;Europe;Denmark;noshow",
                            "http://cygwin.mbwarez.dk/Australi",
                            "http://cygwin.mbwarez.dk/Chinas.7/",
                            "http://cygwin.mbwarez.dk/E",
                            "http://cygwin.mbwarez.dk/Europek",
                            "http://cygwin.mbwarez.dk/I0",
                            "http://cygwin.mbwarez.dk/P",
                            "http://cygwin.mbwarez.dk/Q",
                            "http://cygwin.mbwarez.dk/a",
                            "http://cygwin.mbwarez.dk/alasiaB",
                            "http://cygwin.mbwarez.dk/au.dergmq",
                            "http://cygwin.mbwarez.dk/auin//d.org;(",
                            "http://cygwin.mbwarez.dk/by.ptK3",
                            "http://cygwin.mbwarez.dk/byfly.by/pub/c",
                            "http://cygwin.mbwarez.dk/c.jp",
                            "http://cygwin.mbwarez.dk/ca.de",
                            "http://cygwin.mbwarez.dk/chum.den///",
                            "http://cygwin.mbwarez.dk/ckdomain.de",
                            "http://cygwin.mbwarez.dk/comrrahostr3",
                            "http://cygwin.mbwarez.dk/cygwin/",
                            "http://cygwin.mbwarez.dk/cygwin/.de",
                            "http://cygwin.mbwarez.dk/cygwin//",
                            "http://cygwin.mbwarez.dk/cygwin///",
                            "http://cygwin.mbwarez.dk/cygwin//in/w&",
                            "http://cygwin.mbwarez.dk/cygwin/in//F",
                            "http://cygwin.mbwarez.dk/cygwin/n/",
                            "http://cygwin.mbwarez.dk/cygwin/n/qI%",
                            "http://cygwin.mbwarez.dk/cygwin/n/v",
                            "http://cygwin.mbwarez.dk/cygwin/net/t",
                            "http://cygwin.mbwarez.dk/cygwin/ware.o:",
                            "http://cygwin.mbwarez.dk/cygwin/win/",
                            "http://cygwin.mbwarez.dk/cygwin32/",
                            "http://cygwin.mbwarez.dk/d",
                            "http://cygwin.mbwarez.dk/ddos.net/cygwilZ",
                            "http://cygwin.mbwarez.dk/de",
                            "http://cygwin.mbwarez.dk/de/cygwin/",
                            "http://cygwin.mbwarez.dk/de/cygwin//",
                            "http://cygwin.mbwarez.dk/degwin//",
                            "http://cygwin.mbwarez.dk/e",
                            "http://cygwin.mbwarez.dk/e/cygw",
                            "http://cygwin.mbwarez.dk/ei",
                            "http://cygwin.mbwarez.dk/en.de",
                            "http://cygwin.mbwarez.dk/en.de(",
                            "http://cygwin.mbwarez.dk/en.de.byom",
                            "http://cygwin.mbwarez.dk/et/cygwin/",
                            "http://cygwin.mbwarez.dk/et/cygwin/p0",
                            "http://cygwin.mbwarez.dk/etcom",
                            "http://cygwin.mbwarez.dk/ewin/LIH",
                            "http://cygwin.mbwarez.dk/eworks.orgq-",
                            "http://cygwin.mbwarez.dk/fau.dejp",
                            "http://cygwin.mbwarez.dk/ft.edu.cn/c",
                            "http://cygwin.mbwarez.dk/g/cygwin/",
                            "http://cygwin.mbwarez.dk/g/cygwin/0K",
                            "http://cygwin.mbwarez.dk/gata-u",
                            "http://cygwin.mbwarez.dk/gen.de/",
                            "http://cygwin.mbwarez.dk/gen.de/n/ooN.v",
                            "http://cygwin.mbwarez.dk/gorks.org/",
                            "http://cygwin.mbwarez.dk/gwin/",
                            "http://cygwin.mbwarez.dk/gwin/.free",
                            "http://cygwin.mbwarez.dk/gwin//",
                            "http://cygwin.mbwarez.dk/gwin//.i",
                            "http://cygwin.mbwarez.dk/gwin//gwin/",
                            "http://cygwin.mbwarez.dk/gwin//heY",
                            "http://cygwin.mbwarez.dk/gwin/c.krf3",
                            "http://cygwin.mbwarez.dk/gwin/in/",
                            "http://cygwin.mbwarez.dk/gwin/in/n",
                            "http://cygwin.mbwarez.dk/gwin/na9-",
                            "http://cygwin.mbwarez.dk/gwin/ygwin/",
                            "http://cygwin.mbwarez.dk/hen.de.org/",
                            "http://cygwin.mbwarez.dk/hen.de/cygwin/",
                            "http://cygwin.mbwarez.dk/https://q",
                            "http://cygwin.mbwarez.dk/iij.ad.jp/pub/",
                            "http://cygwin.mbwarez.dk/in.osuosl.org",
                            "http://cygwin.mbwarez.dk/in/",
                            "http://cygwin.mbwarez.dk/in////",
                            "http://cygwin.mbwarez.dk/in//://li"
                        ],
                        "description": "URLs found in memory or binary data",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "90",
                        "match_data": [
                            "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\R0IAZP7Z\\mirrors[1].lst"
                        ],
                        "description": "Creates files inside the user directory",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "7058",
                        "match_data": [
                            "8.43.85.97:443 -> 192.168.2.11:49736 version: TLS 1.2"
                        ],
                        "description": "Uses secure TLS version for HTTPS connections",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "410",
                        "match_data": [
                            "Raw size of UPX1 is bigger than: 0x100000 < 0x140800"
                        ],
                        "description": "PE file has a big raw section",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "description": "Uses HTTPS",
                        "match_data": [
                            "HTTP traffic on port 49714 -> 443",
                            "HTTP traffic on port 443 -> 49714"
                        ],
                        "severity": "IMPACT_SEVERITY_INFO",
                        "id": "625"
                    },
                    {
                        "refs": [
                            {
                                "ref": "#memory_dumps",
                                "value": "executable.exe, 00000000.00000002.4737795738.0000000000C7A000.00000004.00000020.00020000.00000000.sdmp"
                            }
                        ],
                        "description": "May try to detect the virtual machine to hinder analysis (VM artifact strings found in memory)",
                        "match_data": [
                            "Hyper-V RAW"
                        ],
                        "severity": "IMPACT_SEVERITY_INFO",
                        "id": "263"
                    },
                    {
                        "description": "URLs found in memory or binary data",
                        "match_data": [
                            "ftp://ftp-stud.hs-esslingen.dehttp://f",
                            "ftp://ftp-stud.hs-esslingen.dehttps://f",
                            "ftp://ftp.#",
                            "ftp://ftp.byfly.by/pub/cygwin/https://",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/http://l",
                            "ftp://ftp.fau.de/cygwin/os",
                            "ftp://ftp.funet.fi/pub/mirrors/sourceware.org/pub/cygwin/.com/http://m)",
                            "ftp://ftp.funet.fi/pub/mirrors/sourceware.org/pub/cygwin/p",
                            "ftp://ftp.halifax.rwth-aachen.der",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/https://",
                            "ftp://ftp.inf.tu-dresden.deor",
                            "ftp://ftp.jaist.ac.jp/pub/cygwin/",
                            "ftp://ftp.kaist.ac.kr/cygwin/ar",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/http://mX",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/https://L",
                            "ftp://ftp.l",
                            "ftp://ftp.lip6.fr",
                            "ftp://ftp.lip6.fr/pub/cygwin/",
                            "ftp://ftp.lip6.fr/pub/cygwin/http://ftp",
                            "ftp://ftp.muug.ca/mirror/cygwin/yhttps://",
                            "ftp://ftp.ntu.edu.tw/pub/cygwin/",
                            "ftp://ftp.ntua.gr/pub/pc/cygwin/http://",
                            "ftp://ftp.ntua.gr/pub/pc/cygwin/yhttps://",
                            "ftp://ftp.snt.utwente.nl/pub/software/cygwin/",
                            "ftp://ftp.snt.utwente.nl/pub/software/cygwin/ite",
                            "ftp://ftp.snt.utwente.nle",
                            "ftp://ftp.snt.utwente.nlhttps://",
                            "ftp://ftp.yz.yamagata-u.ac.jp/p",
                            "ftp://ftp.yz.yamagata-u.ac.jp/pF",
                            "ftp://ftp.yz.yamagata-u.ac.jp/pub/cygwin//B",
                            "ftp://mirror.checkdomain.de/cygwin/http://f",
                            "ftp://mirror.csclub.uwaterloo.can",
                            "ftp://mirror.datacenter.by/pub/mirrors/cygwin/https://",
                            "ftp://mirror.easyname.at.ac.jphttp://f",
                            "ftp://mirror.easyname.attp",
                            "ftp://mirrors.dotsrc.org/mirrors/cygwin/https://",
                            "ftp://mirrors.dotsrc.orgewin",
                            "ftp://mirrors.netix.net/cygwin/",
                            "ftp://mirrors.netix.net/cygwin/r",
                            "ftp://mirrors.syringanetworks.net/cygwin/",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/http://m",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/http://mz-",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/https://",
                            "ftp://sunsite.icm.edu.plygwin",
                            "http://apps.identrust.com/roots/dstrootcax3.p7c0",
                            "http://cps.letsencrypt.org0",
                            "http://cps.root-x1.letsencrypt.org0",
                            "http://crl.identrust.com/DSTROOTCAX3CRL.crl0",
                            "http://cygwin.cathedral-",
                            "http://cygwin.cathedral-networks.org",
                            "http://cygwin.cathedral-networks.org#",
                            "http://cygwin.cathedral-networks.org/",
                            "http://cygwin.cathedral-networks.org/-",
                            "http://cygwin.cathedral-networks.org/.",
                            "http://cygwin.cathedral-networks.org/.fh",
                            "http://cygwin.cathedral-networks.org/.i",
                            "http://cygwin.cathedral-networks.org/.n",
                            "http://cygwin.cathedral-networks.org/.n/",
                            "http://cygwin.cathedral-networks.org//",
                            "http://cygwin.cathedral-networks.org///",
                            "http://cygwin.cathedral-networks.org//A",
                            "http://cygwin.cathedral-networks.org//A-",
                            "http://cygwin.cathedral-networks.org//a",
                            "http://cygwin.cathedral-networks.org//f",
                            "http://cygwin.cathedral-networks.org//l",
                            "http://cygwin.cathedral-networks.org//wX",
                            "http://cygwin.cathedral-networks.org/6",
                            "http://cygwin.cathedral-networks.org/;;",
                            "http://cygwin.cathedral-networks.org/;cygwin.cathedral-networks.org;Europe;Norway;noshow",
                            "http://cygwin.cathedral-networks.org/?",
                            "http://cygwin.cathedral-networks.org/B",
                            "http://cygwin.cathedral-networks.org/C-",
                            "http://cygwin.cathedral-networks.org/H",
                            "http://cygwin.cathedral-networks.org/L",
                            "http://cygwin.cathedral-networks.org/L4-1&",
                            "http://cygwin.cathedral-networks.org/R",
                            "http://cygwin.cathedral-networks.org/U",
                            "http://cygwin.cathedral-networks.org/Z",
                            "http://cygwin.cathedral-networks.org/_",
                            "http://cygwin.cathedral-networks.org/a",
                            "http://cygwin.cathedral-networks.org/ce",
                            "http://cygwin.cathedral-networks.org/cy",
                            "http://cygwin.cathedral-networks.org/d",
                            "http://cygwin.cathedral-networks.org/e.",
                            "http://cygwin.cathedral-networks.org/ec",
                            "http://cygwin.cathedral-networks.org/ez",
                            "http://cygwin.cathedral-networks.org/e~",
                            "http://cygwin.cathedral-networks.org/fr",
                            "http://cygwin.cathedral-networks.org/ft",
                            "http://cygwin.cathedral-networks.org/gq;",
                            "http://cygwin.cathedral-networks.org/h",
                            "http://cygwin.cathedral-networks.org/i",
                            "http://cygwin.cathedral-networks.org/in4.",
                            "http://cygwin.cathedral-networks.org/l",
                            "http://cygwin.cathedral-networks.org/m",
                            "http://cygwin.cathedral-networks.org/n/L",
                            "http://cygwin.cathedral-networks.org/om",
                            "http://cygwin.cathedral-networks.org/p",
                            "http://cygwin.cathedral-networks.org/p.",
                            "http://cygwin.cathedral-networks.org/pux",
                            "http://cygwin.cathedral-networks.org/r",
                            "http://cygwin.cathedral-networks.org/r/",
                            "http://cygwin.cathedral-networks.org/ro",
                            "http://cygwin.cathedral-networks.org/s",
                            "http://cygwin.cathedral-networks.org/s.",
                            "http://cygwin.cathedral-networks.org/sdD/",
                            "http://cygwin.cathedral-networks.org/t",
                            "http://cygwin.cathedral-networks.org/th",
                            "http://cygwin.cathedral-networks.org/u.",
                            "http://cygwin.cathedral-networks.org/v",
                            "http://cygwin.cathedral-networks.org/wne",
                            "http://cygwin.cathedral-networks.org/x",
                            "http://cygwin.cathedral-networks.org/yn",
                            "http://cygwin.cathedral-networks.org4-",
                            "http://cygwin.cathedral-networks.org9",
                            "http://cygwin.cathedral-networks.org://",
                            "http://cygwin.cathedral-networks.orgB",
                            "http://cygwin.cathedral-networks.orgG",
                            "http://cygwin.cathedral-networks.orgM",
                            "http://cygwin.cathedral-networks.orgX",
                            "http://cygwin.cathedral-networks.orgY",
                            "http://cygwin.cathedral-networks.orgZ",
                            "http://cygwin.cathedral-networks.orga",
                            "http://cygwin.cathedral-networks.orgdot",
                            "http://cygwin.cathedral-networks.orge=",
                            "http://cygwin.cathedral-networks.orgen",
                            "http://cygwin.cathedral-networks.orgh",
                            "http://cygwin.cathedral-networks.orgin/L",
                            "http://cygwin.cathedral-networks.orgj",
                            "http://cygwin.cathedral-networks.orgjp",
                            "http://cygwin.cathedral-networks.orgn/",
                            "http://cygwin.cathedral-networks.orgn/W",
                            "http://cygwin.cathedral-networks.orgn/c",
                            "http://cygwin.cathedral-networks.orgni-",
                            "http://cygwin.cathedral-networks.orgors",
                            "http://cygwin.cathedral-networks.orgp",
                            "http://cygwin.cathedral-networks.orgrs.",
                            "http://cygwin.cathedral-networks.orgstc",
                            "http://cygwin.cathedral-networks.orgtp",
                            "http://cygwin.cathedral-networks.orgv",
                            "http://cygwin.mbwarez.dk",
                            "http://cygwin.mbwarez.dk#",
                            "http://cygwin.mbwarez.dk$",
                            "http://cygwin.mbwarez.dk.dewin/et/X411",
                            "http://cygwin.mbwarez.dk.net",
                            "http://cygwin.mbwarez.dk.net/",
                            "http://cygwin.mbwarez.dk.org",
                            "http://cygwin.mbwarez.dk.orgwin//",
                            "http://cygwin.mbwarez.dk/",
                            "http://cygwin.mbwarez.dk/$w",
                            "http://cygwin.mbwarez.dk/%",
                            "http://cygwin.mbwarez.dk/(",
                            "http://cygwin.mbwarez.dk/.ca/om/q",
                            "http://cygwin.mbwarez.dk/.cn/cygwin/n",
                            "http://cygwin.mbwarez.dk/.jp",
                            "http://cygwin.mbwarez.dk/.org.ilt",
                            "http://cygwin.mbwarez.dk/.twaren.net/Un",
                            "http://cygwin.mbwarez.dk//",
                            "http://cygwin.mbwarez.dk///cygwin/",
                            "http://cygwin.mbwarez.dk//cygwin/",
                            "http://cygwin.mbwarez.dk//cygwin/.c",
                            "http://cygwin.mbwarez.dk//cygwin//a",
                            "http://cygwin.mbwarez.dk//cygwin/:",
                            "http://cygwin.mbwarez.dk//cygwin/F",
                            "http://cygwin.mbwarez.dk//cygwin/V",
                            "http://cygwin.mbwarez.dk//cygwin/g",
                            "http://cygwin.mbwarez.dk//cygwin/h(&1",
                            "http://cygwin.mbwarez.dk//cygwin/win/",
                            "http://cygwin.mbwarez.dk//gwin/n/",
                            "http://cygwin.mbwarez.dk//in/",
                            "http://cygwin.mbwarez.dk//win//",
                            "http://cygwin.mbwarez.dk//ygwin/dG",
                            "http://cygwin.mbwarez.dk/0",
                            "http://cygwin.mbwarez.dk/9",
                            "http://cygwin.mbwarez.dk/:1r.",
                            "http://cygwin.mbwarez.dk/;",
                            "http://cygwin.mbwarez.dk/;cygwin.mbwarez.dk;Europe;Denmark;noshow",
                            "http://cygwin.mbwarez.dk/B",
                            "http://cygwin.mbwarez.dk/Bulgaria",
                            "http://cygwin.mbwarez.dk/China",
                            "http://cygwin.mbwarez.dk/China/d:",
                            "http://cygwin.mbwarez.dk/Europek",
                            "http://cygwin.mbwarez.dk/I",
                            "http://cygwin.mbwarez.dk/X",
                            "http://cygwin.mbwarez.dk/argasso.net",
                            "http://cygwin.mbwarez.dk/chum.de",
                            "http://cygwin.mbwarez.dk/chum.degwin/",
                            "http://cygwin.mbwarez.dk/cn/cygwin/j",
                            "http://cygwin.mbwarez.dk/cygwin/",
                            "http://cygwin.mbwarez.dk/cygwin/)",
                            "http://cygwin.mbwarez.dk/cygwin/.ucalg$",
                            "http://cygwin.mbwarez.dk/cygwin//c",
                            "http://cygwin.mbwarez.dk/cygwin//in/",
                            "http://cygwin.mbwarez.dk/cygwin/1",
                            "http://cygwin.mbwarez.dk/cygwin/X",
                            "http://cygwin.mbwarez.dk/cygwin/n/",
                            "http://cygwin.mbwarez.dk/cygwin/z",
                            "http://cygwin.mbwarez.dk/cygwin32/7",
                            "http://cygwin.mbwarez.dk/cygwin32/V",
                            "http://cygwin.mbwarez.dk/cygwin32/b",
                            "http://cygwin.mbwarez.dk/d.com",
                            "http://cygwin.mbwarez.dk/d.com/cygwin/",
                            "http://cygwin.mbwarez.dk/de/cygwin/",
                            "http://cygwin.mbwarez.dk/dehttp://f",
                            "http://cygwin.mbwarez.dk/deurces.redha=",
                            "http://cygwin.mbwarez.dk/e",
                            "http://cygwin.mbwarez.dk/e=",
                            "http://cygwin.mbwarez.dk/earia",
                            "http://cygwin.mbwarez.dk/ecygwin/",
                            "http://cygwin.mbwarez.dk/edu.sg/mirror/",
                            "http://cygwin.mbwarez.dk/ein/://ft",
                            "http://cygwin.mbwarez.dk/ernode.on.netE",
                            "http://cygwin.mbwarez.dk/et/cygwin/x5",
                            "http://cygwin.mbwarez.dk/etworks.org",
                            "http://cygwin.mbwarez.dk/etworks.org/U",
                            "http://cygwin.mbwarez.dk/etygwin/(5",
                            "http://cygwin.mbwarez.dk/f",
                            "http://cygwin.mbwarez.dk/f1p",
                            "http://cygwin.mbwarez.dk/g$",
                            "http://cygwin.mbwarez.dk/g/cygwin/",
                            "http://cygwin.mbwarez.dk/gwin.uib.no/",
                            "http://cygwin.mbwarez.dk/gwin/",
                            "http://cygwin.mbwarez.dk/gwin//n/;",
                            "http://cygwin.mbwarez.dk/gwin/n//",
                            "http://cygwin.mbwarez.dk/gwin/n/fa-",
                            "http://cygwin.mbwarez.dk/gwin/win/",
                            "http://cygwin.mbwarez.dk/ia",
                            "http://cygwin.mbwarez.dk/iajaist.ac.jp",
                            "http://cygwin.mbwarez.dk/iar.freebsd.oa",
                            "http://cygwin.mbwarez.dk/in/",
                            "http://cygwin.mbwarez.dk/in//",
                            "http://cygwin.mbwarez.dk/in///;",
                            "http://cygwin.mbwarez.dk/in//n//",
                            "http://cygwin.mbwarez.dk/in/in/2",
                            "http://cygwin.mbwarez.dk/in/l.ca/",
                            "http://cygwin.mbwarez.dk/in/n/",
                            "http://cygwin.mbwarez.dk/in/nus.edu?.f1",
                            "http://cygwin.mbwarez.dk/in/tp.kr.fK",
                            "http://cygwin.mbwarez.dk/in/ttp://c&",
                            "http://cygwin.mbwarez.dk/in/x",
                            "http://cygwin.mbwarez.dk/in/ygwin/",
                            "http://cygwin.mbwarez.dk/inf.tu-dresden0",
                            "http://cygwin.mbwarez.dk/l1",
                            "http://cygwin.mbwarez.dk/mirror.e",
                            "http://cygwin.mbwarez.dk/n/",
                            "http://cygwin.mbwarez.dk/n///x",
                            "http://cygwin.mbwarez.dk/n/cygwin/",
                            "http://cygwin.mbwarez.dk/n/n/",
                            "http://cygwin.mbwarez.dk/n/n/in/",
                            "http://cygwin.mbwarez.dk/n/win/",
                            "http://cygwin.mbwarez.dk/netgwin/",
                            "http://cygwin.mbwarez.dk/om/cygwin/",
                            "http://cygwin.mbwarez.dk/om/cygwin/O",
                            "http://cygwin.mbwarez.dk/om/cygwin/n/q",
                            "http://cygwin.mbwarez.dk/or.rafal.ca",
                            "http://cygwin.mbwarez.dk/orgitceware.9-",
                            "http://cygwin.mbwarez.dk/p",
                            "http://cygwin.mbwarez.dk/p://mirror-hk.",
                            "http://cygwin.mbwarez.dk/ps://mirrors.huaweicloud.com/cygwin/",
                            "http://cygwin.mbwarez.dk/r.lagoon.ncp",
                            "http://cygwin.mbwarez.dk/rafal.ca/Q",
                            "http://cygwin.mbwarez.dk/re.mirror.garrj",
                            "http://cygwin.mbwarez.dk/rg/cygwin/",
                            "http://cygwin.mbwarez.dk/rg/cygwin/N",
                            "http://cygwin.mbwarez.dk/rs/sources.red",
                            "http://cygwin.mbwarez.dk/t/cygwin/",
                            "http://cygwin.mbwarez.dk/t/cygwin//#481",
                            "http://cygwin.mbwarez.dk/t/cygwin/z",
                            "http://cygwin.mbwarez.dk/tcygwin//",
                            "http://cygwin.mbwarez.dk/ternode.on.net",
                            "http://cygwin.mbwarez.dk/tp",
                            "http://cygwin.mbwarez.dk/tworks.org",
                            "http://cygwin.mbwarez.dk/tworks.org//f",
                            "http://cygwin.mbwarez.dk/tworks.org/a",
                            "http://cygwin.mbwarez.dk/tworks.orgB",
                            "http://cygwin.mbwarez.dk/win",
                            "http://cygwin.mbwarez.dk/win.mbwarez",
                            "http://cygwin.mbwarez.dk/win/",
                            "http://cygwin.mbwarez.dk/win/;",
                            "http://cygwin.mbwarez.dk/win/in//",
                            "http://cygwin.mbwarez.dk/win/j",
                            "http://cygwin.mbwarez.dk/win/s.org",
                            "http://cygwin.mbwarez.dk/win/so.net/",
                            "http://cygwin.mbwarez.dk/ygwin/",
                            "http://cygwin.mbwarez.dk/ygwin/.net/",
                            "http://cygwin.mbwarez.dk/ygwin/C",
                            "http://cygwin.mbwarez.dk/ygwin/i",
                            "http://cygwin.mbwarez.dk/ygwin/in/",
                            "http://cygwin.mbwarez.dk/ygwin/in/O",
                            "http://cygwin.mbwarez.dk/ygwin/in/n",
                            "http://cygwin.mbwarez.dk/ygwin/j",
                            "http://cygwin.mbwarez.dk/ygwin/ub/c",
                            "http://cygwin.mbwarez.dk/ygwin/ygwin/",
                            "http://cygwin.mbwarez.dk/ywin/siatac",
                            "http://cygwin.mbwarez.dk/yz.yam",
                            "http://cygwin.mbwarez.dkChina",
                            "http://cygwin.mbwarez.dkE",
                            "http://cygwin.mbwarez.dkV",
                            "http://cygwin.mbwarez.dka.cam/",
                            "http://cygwin.mbwarez.dkac.jpet",
                            "http://cygwin.mbwarez.dkargasso.netO5",
                            "http://cygwin.mbwarez.dkbochum.de/-",
                            "http://cygwin.mbwarez.dkcn/cygw",
                            "http://cygwin.mbwarez.dkcomgwin/",
                            "http://cygwin.mbwarez.dkcygwin/",
                            "http://cygwin.mbwarez.dkcygwin/9",
                            "http://cygwin.mbwarez.dkcygwin/B",
                            "http://cygwin.mbwarez.dkde/cygwin/",
                            "http://cygwin.mbwarez.dkdeerks.org",
                            "http://cygwin.mbwarez.dkdein/",
                            "http://cygwin.mbwarez.dkdu.cnin/j",
                            "http://cygwin.mbwarez.dkdu.tw/pu",
                            "http://cygwin.mbwarez.dke/cygwin/n.de",
                            "http://cygwin.mbwarez.dke/pc/prog/cygwi",
                            "http://cygwin.mbwarez.dkerloo.cat/",
                            "http://cygwin.mbwarez.dket/cygwin//",
                            "http://cygwin.mbwarez.dket/cygwin/ay",
                            "http://cygwin.mbwarez.dkftp",
                            "http://cygwin.mbwarez.dkg",
                            "http://cygwin.mbwarez.dkg/cygwin/",
                            "http://cygwin.mbwarez.dkg/cygwin//n/$",
                            "http://cygwin.mbwarez.dkg/cygwin/redha",
                            "http://cygwin.mbwarez.dkgde/cygwin/oo",
                            "http://cygwin.mbwarez.dkgwin/",
                            "http://cygwin.mbwarez.dkin/",
                            "http://cygwin.mbwarez.dkirror.datacente",
                            "http://cygwin.mbwarez.dkirrors.filigrani",
                            "http://cygwin.mbwarez.dkm/cygwin/(",
                            "http://cygwin.mbwarez.dkn/cygwin/t",
                            "http://cygwin.mbwarez.dknet",
                            "http://cygwin.mbwarez.dknet/cygwin/;",
                            "http://cygwin.mbwarez.dknetworks.org/t",
                            "http://cygwin.mbwarez.dkngen.desoftwar",
                            "http://cygwin.mbwarez.dko/cygwin/",
                            "http://cygwin.mbwarez.dkogie.frgwin/",
                            "http://cygwin.mbwarez.dkorgcygwin/7",
                            "http://cygwin.mbwarez.dkorgn",
                            "http://cygwin.mbwarez.dkry.camerica",
                            "http://cygwin.mbwarez.dksargasso.net#",
                            "http://cygwin.mbwarez.dksourcewa",
                            "http://cygwin.mbwarez.dkt/cygwin/t//",
                            "http://cygwin.mbwarez.dkub/cygwin///f",
                            "http://cygwin.mbwarez.dkub/cygwin///m",
                            "http://cygwin.mbwarez.dkud.comcygwin/",
                            "http://cygwin.mbwarez.dkwin/",
                            "http://cygwin.mbwarez.dkx",
                            "http://cygwin.mbwarez.dkygwin/in/",
                            "http://cygwin.mbwarez.dkygwin/m/t",
                            "http://cygwin.mbwarezA",
                            "http://cygwin.mi",
                            "http://cygwin.mirror.constant.com",
                            "http://cygwin.mirror.constant.com%",
                            "http://cygwin.mirror.constant.com/",
                            "http://cygwin.mirror.constant.com/(",
                            "http://cygwin.mirror.constant.com/.byde",
                            "http://cygwin.mirror.constant.com/.org/U-",
                            "http://cygwin.mirror.constant.com//",
                            "http://cygwin.mirror.constant.com///a",
                            "http://cygwin.mirror.constant.com//C5",
                            "http://cygwin.mirror.constant.com//n//7;",
                            "http://cygwin.mirror.constant.com//net//y",
                            "http://cygwin.mirror.constant.com//ygwin/",
                            "http://cygwin.mirror.constant.com/92",
                            "http://cygwin.mirror.constant.com/;cygwin.mirror.constant.com;North",
                            "http://cygwin.mirror.constant.com/cygwin/",
                            "http://cygwin.mirror.constant.com/cygwin/V/",
                            "http://cygwin.mirror.constant.com/e:",
                            "http://cygwin.mirror.constant.com/et",
                            "http://cygwin.mirror.constant.com/et/",
                            "http://cygwin.mirror.constant.com/et/iO",
                            "http://cygwin.mirror.constant.com/gwin/cyH",
                            "http://cygwin.mirror.constant.com/http://m)",
                            "http://cygwin.mirror.constant.com/http://mz-",
                            "http://cygwin.mirror.constant.com/in///0",
                            "http://cygwin.mirror.constant.com/o.net//-",
                            "http://cygwin.mirror.constant.com/o.net/M",
                            "http://cygwin.mirror.constant.com/or.ch",
                            "http://cygwin.mirror.constant.com/r",
                            "http://cygwin.mirror.constant.com/s.org/",
                            "http://cygwin.mirror.constant.com/t",
                            "http://cygwin.mirror.constant.com/t//",
                            "http://cygwin.mirror.constant.com/t/p",
                            "http://cygwin.mirror.constant.com/tr.i",
                            "http://cygwin.mirror.constant.com/win/",
                            "http://cygwin.mirror.constant.com/win/://",
                            "http://cygwin.mirror.constant.com/win/K4",
                            "http://cygwin.mirror.constant.com/win/in/n/",
                            "http://cygwin.mirror.constant.com/win/n/",
                            "http://cygwin.mirror.constant.com/y4",
                            "http://cygwin.mirror.constant.com/ygwin/x",
                            "http://cygwin.mirror.constant.comG",
                            "http://cygwin.mirror.constant.comJ",
                            "http://cygwin.mirror.constant.comet",
                            "http://cygwin.mirror.constant.comn/",
                            "http://cygwin.mirror.constant.comn/$",
                            "http://cygwin.mirror.constant.comn/R4",
                            "http://cygwin.mirror.constant.comn32/V",
                            "http://cygwin.mirror.constant.comnet/",
                            "http://cygwin.mirror.constant.como/or."
                        ],
                        "severity": "IMPACT_SEVERITY_INFO",
                        "id": "238"
                    },
                    {
                        "description": "Uses secure TLS version for HTTPS connections",
                        "match_data": [
                            "8.43.85.97:443 -> 192.168.2.15:49714 version: TLS 1.2"
                        ],
                        "severity": "IMPACT_SEVERITY_INFO",
                        "id": "7058"
                    },
                    {
                        "severity": "IMPACT_SEVERITY_INFO",
                        "match_data": [
                            "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\SystemCertificates\\AuthRoot"
                        ],
                        "id": "198",
                        "description": "Monitors certain registry keys / values for changes (often done to protect autostart functionality)"
                    },
                    {
                        "severity": "IMPACT_SEVERITY_INFO",
                        "match_data": [
                            "HTTP traffic on port 49704 -> 443",
                            "HTTP traffic on port 443 -> 49704"
                        ],
                        "id": "625",
                        "description": "Uses HTTPS"
                    },
                    {
                        "severity": "IMPACT_SEVERITY_INFO",
                        "refs": [
                            {
                                "ref": "#memory_dumps",
                                "value": "program.exe, 00000000.00000002.4544157087.0000000000D09000.00000004.00000020.00020000.00000000.sdmp, program.exe, 00000000.00000002.4542476600.0000000000C8A000.00000004.00000020.00020000.00000000.sdmp"
                            },
                            {
                                "ref": "#memory_dumps",
                                "value": "program.exe, 00000000.00000002.4542476600.0000000000C8A000.00000004.00000020.00020000.00000000.sdmp"
                            }
                        ],
                        "match_data": [
                            "Hyper-V RAW",
                            "Hyper-V RAWh"
                        ],
                        "id": "263",
                        "description": "May try to detect the virtual machine to hinder analysis (VM artifact strings found in memory)"
                    },
                    {
                        "severity": "IMPACT_SEVERITY_INFO",
                        "match_data": [
                            "ftp://cygwin.mirror.rafal.ca/pub/cygwin/",
                            "ftp://ftp-stud.hs-esslingen.der",
                            "ftp://ftp.0",
                            "ftp://ftp.P",
                            "ftp://ftp.acc.umu.se/mirror/cygwin/http$",
                            "ftp://ftp.fau.de/cygwin/c",
                            "ftp://ftp.fsn.hu/pub/cygwin//",
                            "ftp://ftp.fsn.hu/pub/cygwin/rs",
                            "ftp://ftp.ha&",
                            "ftp://ftp.halifax.rwth-aachen.de/cygwin/ygwin",
                            "ftp://ftp.halifax.rwth-aachen.der",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/http://m%Ccpr;",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/https://",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/https://G",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/n",
                            "ftp://ftp.inf.tu-dresden.de",
                            "ftp://ftp.inf.tu-dresden.dewin/s",
                            "ftp://ftp.jaist.ac.jp/pub/cygwin/",
                            "ftp://ftp.kaist.ac.kr/cygwin/http://m",
                            "ftp://ftp.kaist.ac.kr/cygwin/or",
                            "ftp://ftp.kaist.ac.kr/cygwin/win",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/http://m",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/https://",
                            "ftp://ftp.kr.freebsd.orggwin/https://UA",
                            "ftp://ftp.lip6.fr/pub/cygwin/",
                            "ftp://ftp.lip6.fr/pub/cygwin//http://m%Ccpr;",
                            "ftp://ftp.lip6.fr/pub/cygwin//https://t",
                            "ftp://ftp.lip6.fr/pub/cygwin/http://m",
                            "ftp://ftp.lip6.fr/pub/cygwin/win/",
                            "ftp://ftp.lip6.frs",
                            "ftp://ftp.n",
                            "ftp://ftp.ntua.gr/pub/pc/cygwin/http://",
                            "ftp://ftp.rnl.tecnico.ulisboa.pt",
                            "ftp://ftp.snt.utwente.nlp",
                            "ftp://ftp.snt.utwente.nltp",
                            "ftp://ftp.snt.utwente.nlu.edu.cn",
                            "ftp://ftp.yz.yamagata-u.ac.jp/pub/cygwin/",
                            "ftp://ftp.yz.yamagata-u.ac.jphttp://f",
                            "ftp://ftp.yz.yamagata-u.ac.jpp",
                            "ftp://mirror.checkdomain.deftp",
                            "ftp://mirror.cs.vt.edu/pub/cygwin/cygwin/ors",
                            "ftp://mirror.datacenter.by",
                            "ftp://mirror.datacenter.byrrors",
                            "ftp://mirror.easyname.atin",
                            "ftp://mirror.i4",
                            "ftp://mirror.lagoon.nc/cygwin/https://",
                            "ftp://mirror.rise.ph/cygwin/cygwin/",
                            "ftp://mirrors.dotsrc.orgu",
                            "ftp://mirrors.netix.net/cygwin/https://",
                            "ftp://mirrors.netix.net/cygwin/https://y",
                            "ftp://mirrors.sonic.net/cygwin/https://",
                            "ftp://mirrors.sonic.net/cygwin/rs",
                            "ftp://mirrors.xmission.com",
                            "ftp://sourceware.org/ftp://sources.redhat.com/ftp://gcc.gnu.org/",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/https://",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/n",
                            "ftp://sunsite.icm.edu.plp",
                            "http://ac.economia.gob.mx/cps.html0",
                            "http://ac.economia.gob.mx/last.crl0G",
                            "http://acedicom.edicomgroup.com/doc0",
                            "http://acraiz.icpbrasil.gov.br/DPCacraiz.pdf0?",
                            "http://acraiz.icpbrasil.gov.br/LCRacraizv1.crl0",
                            "http://acraiz.icpbrasil.gov.br/LCRacraizv2.crl0",
                            "http://apps.identrust.com/roots/dstrootcax3.p7c0",
                            "http://ca.disig.sk/ca/crl/ca_disig.crl0",
                            "http://ca.mtin.es/mtin/DPCyPoliticas0",
                            "http://ca.mtin.es/mtin/DPCyPoliticas0g",
                            "http://ca.mtin.es/mtin/crl/MTINAutoridadRaiz03",
                            "http://ca.mtin.es/mtin/ocsp0",
                            "http://ca2.mtin.es/mtin/crl/MTINAutoridadRaiz0",
                            "http://certificates.starfieldtech.com/repository/1604",
                            "http://certs.oati.net/repository/OATICA2.crl0",
                            "http://certs.oati.net/repository/OATICA2.crt0",
                            "http://certs.oaticerts.com/repository/OATICA2.crl",
                            "http://certs.oaticerts.com/repository/OATICA2.crt08",
                            "http://cps.chambersign.org/cps/chambersignroot.html0",
                            "http://cps.chambersign.org/cps/chambersroot.html0",
                            "http://cps.letsencrypt.org0",
                            "http://cps.root-x1.letsencrypt.org0",
                            "http://cps.siths.se/sithsrootcav1.html0",
                            "http://crl.certigna.fr/certignarootca.crl01",
                            "http://crl.chambersign.org/chambersignroot.crl0",
                            "http://crl.chambersign.org/chambersroot.crl0",
                            "http://crl.comodoca.com/AAACertificateServices.crl06",
                            "http://crl.defence.gov.au/pki0",
                            "http://crl.dhimyotis.com/certignarootca.crl0",
                            "http://crl.globalsign.net/root-r2.crl0",
                            "http://crl.identrust.com/DSTROOTCAX3CRL.crl0",
                            "http://crl.oces.trust2408.com/oces.crl0",
                            "http://crl.pki.wellsfargo.com/wsprca.crl0",
                            "http://crl.securetrust.com/SGCA.crl0",
                            "http://crl.securetrust.com/STCA.crl0",
                            "http://crl.ssc.lt/root-a/cacrl.crl0",
                            "http://crl.ssc.lt/root-b/cacrl.crl0",
                            "http://crl.ssc.lt/root-c/cacrl.crl0",
                            "http://crl.xrampsecurity.com/XGCA.crl0",
                            "http://crl1.comsign.co.il/crl/comsignglobalrootca.crl0",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/CABD2A79A1076A31F21D253635CB0",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/authrootstl.cab",
                            "http://ctldl.windowsupdate.com/z",
                            "http://ctldl.windowsupdate.com:80/msdownload/update/v3/static/trustedr/en/CABD2A79A1076A31F21D253635",
                            "http://cygwin.cathedral-",
                            "http://cygwin.cathedral-networks.org",
                            "http://cygwin.cathedral-networks.org#",
                            "http://cygwin.cathedral-networks.org$",
                            "http://cygwin.cathedral-networks.org(",
                            "http://cygwin.cathedral-networks.org-hk.koddos.net/cygwin/works.org/nB",
                            "http://cygwin.cathedral-networks.org/",
                            "http://cygwin.cathedral-networks.org/$",
                            "http://cygwin.cathedral-networks.org/%",
                            "http://cygwin.cathedral-networks.org/(",
                            "http://cygwin.cathedral-networks.org/(A",
                            "http://cygwin.cathedral-networks.org/.",
                            "http://cygwin.cathedral-networks.org/.d",
                            "http://cygwin.cathedral-networks.org/.l",
                            "http://cygwin.cathedral-networks.org/.lk",
                            "http://cygwin.cathedral-networks.org/.v",
                            "http://cygwin.cathedral-networks.org//",
                            "http://cygwin.cathedral-networks.org///",
                            "http://cygwin.cathedral-networks.org///#",
                            "http://cygwin.cathedral-networks.org//5",
                            "http://cygwin.cathedral-networks.org//c",
                            "http://cygwin.cathedral-networks.org//f?",
                            "http://cygwin.cathedral-networks.org//ftp.lip6.fro/p",
                            "http://cygwin.cathedral-networks.org//l",
                            "http://cygwin.cathedral-networks.org//m",
                            "http://cygwin.cathedral-networks.org//mN",
                            "http://cygwin.cathedral-networks.org//o",
                            "http://cygwin.cathedral-networks.org/1",
                            "http://cygwin.cathedral-networks.org/5",
                            "http://cygwin.cathedral-networks.org/8",
                            "http://cygwin.cathedral-networks.org/8C",
                            "http://cygwin.cathedral-networks.org/:/&",
                            "http://cygwin.cathedral-networks.org/:EC",
                            "http://cygwin.cathedral-networks.org/;cygwin.cathedral-networks.org;Europe;Norway;noshow",
                            "http://cygwin.cathedral-networks.org/Am",
                            "http://cygwin.cathedral-networks.org/D",
                            "http://cygwin.cathedral-networks.org/E",
                            "http://cygwin.cathedral-networks.org/M",
                            "http://cygwin.cathedral-networks.org/PC",
                            "http://cygwin.cathedral-networks.org/R",
                            "http://cygwin.cathedral-networks.org/U",
                            "http://cygwin.cathedral-networks.org/Y",
                            "http://cygwin.cathedral-networks.org/a",
                            "http://cygwin.cathedral-networks.org/c",
                            "http://cygwin.cathedral-networks.org/d4",
                            "http://cygwin.cathedral-networks.org/e",
                            "http://cygwin.cathedral-networks.org/et",
                            "http://cygwin.cathedral-networks.org/f.",
                            "http://cygwin.cathedral-networks.org/ft",
                            "http://cygwin.cathedral-networks.org/fts",
                            "http://cygwin.cathedral-networks.org/g",
                            "http://cygwin.cathedral-networks.org/g_",
                            "http://cygwin.cathedral-networks.org/ia",
                            "http://cygwin.cathedral-networks.org/in",
                            "http://cygwin.cathedral-networks.org/ixG",
                            "http://cygwin.cathedral-networks.org/kw",
                            "http://cygwin.cathedral-networks.org/lA",
                            "http://cygwin.cathedral-networks.org/laqB4pnJ",
                            "http://cygwin.cathedral-networks.org/m",
                            "http://cygwin.cathedral-networks.org/mit",
                            "http://cygwin.cathedral-networks.org/n/",
                            "http://cygwin.cathedral-networks.org/ni)",
                            "http://cygwin.cathedral-networks.org/om",
                            "http://cygwin.cathedral-networks.org/ot",
                            "http://cygwin.cathedral-networks.org/p",
                            "http://cygwin.cathedral-networks.org/qN3p-",
                            "http://cygwin.cathedral-networks.org/qN6p",
                            "http://cygwin.cathedral-networks.org/r",
                            "http://cygwin.cathedral-networks.org/rX",
                            "http://cygwin.cathedral-networks.org/rb",
                            "http://cygwin.cathedral-networks.org/rr",
                            "http://cygwin.cathedral-networks.org/sc",
                            "http://cygwin.cathedral-networks.org/t",
                            "http://cygwin.cathedral-networks.org/th",
                            "http://cygwin.cathedral-networks.org/tpr",
                            "http://cygwin.cathedral-networks.org/ts",
                            "http://cygwin.cathedral-networks.org/u/",
                            "http://cygwin.cathedral-networks.org/um",
                            "http://cygwin.cathedral-networks.org/unE",
                            "http://cygwin.cathedral-networks.org/wi",
                            "http://cygwin.cathedral-networks.org/y",
                            "http://cygwin.cathedral-networks.org/ygxZ",
                            "http://cygwin.cathedral-networks.org/z",
                            "http://cygwin.cathedral-networks.org/~L",
                            "http://cygwin.cathedral-networks.org0",
                            "http://cygwin.cathedral-networks.org4",
                            "http://cygwin.cathedral-networks.org;C",
                            "http://cygwin.cathedral-networks.orgC",
                            "http://cygwin.cathedral-networks.orgTL",
                            "http://cygwin.cathedral-networks.orgV",
                            "http://cygwin.cathedral-networks.orgY",
                            "http://cygwin.cathedral-networks.orgZMAp1",
                            "http://cygwin.cathedral-networks.orga",
                            "http://cygwin.cathedral-networks.orgatedZ",
                            "http://cygwin.cathedral-networks.orgb",
                            "http://cygwin.cathedral-networks.orgcomR",
                            "http://cygwin.cathedral-networks.orgefi",
                            "http://cygwin.cathedral-networks.orget",
                            "http://cygwin.cathedral-networks.orghumG",
                            "http://cygwin.cathedral-networks.orgkod",
                            "http://cygwin.cathedral-networks.orgli",
                            "http://cygwin.cathedral-networks.orgmi",
                            "http://cygwin.cathedral-networks.orgn.me",
                            "http://cygwin.cathedral-networks.orgn/",
                            "http://cygwin.cathedral-networks.orgr.i",
                            "http://cygwin.cathedral-networks.orgrs.",
                            "http://cygwin.cathedral-networks.orguX",
                            "http://cygwin.cathedral-networks.orguts",
                            "http://cygwin.cathedral-networks.orgx",
                            "http://cygwin.cathedral-networks.org~A",
                            "http://cygwin.mbwarez.dk",
                            "http://cygwin.mbwarez.dk.au",
                            "http://cygwin.mbwarez.dk.bycygwin/",
                            "http://cygwin.mbwarez.dk.de$",
                            "http://cygwin.mbwarez.dk.de/cygwin/r",
                            "http://cygwin.mbwarez.dk.fau.de$",
                            "http://cygwin.mbwarez.dk.ntua.gr/pub/pc-",
                            "http://cygwin.mbwarez.dk.twaren.net/Uni4",
                            "http://cygwin.mbwarez.dk/",
                            "http://cygwin.mbwarez.dk/.ac.nz.by/pubJ",
                            "http://cygwin.mbwarez.dk/.ac.nzS",
                            "http://cygwin.mbwarez.dk/.acc.umu.se/miw",
                            "http://cygwin.mbwarez.dk/.ca",
                            "http://cygwin.mbwarez.dk/.cn/cygwin/",
                            "http://cygwin.mbwarez.dk/.de/cygwin/",
                            "http://cygwin.mbwarez.dk/.degwin//f",
                            "http://cygwin.mbwarez.dk/.gr/pub/pc/cy",
                            "http://cygwin.mbwarez.dk/.gutscheinraus",
                            "http://cygwin.mbwarez.dk/.rise.ph/cy",
                            "http://cygwin.mbwarez.dk/.tech/pub/cyg",
                            "http://cygwin.mbwarez.dk//",
                            "http://cygwin.mbwarez.dk///mirror.ma",
                            "http://cygwin.mbwarez.dk//cy",
                            "http://cygwin.mbwarez.dk//cygwin/",
                            "http://cygwin.mbwarez.dk//cygwin//",
                            "http://cygwin.mbwarez.dk//cygwin/8M~po)",
                            "http://cygwin.mbwarez.dk//cygwin/etw",
                            "http://cygwin.mbwarez.dk//cygwin/goon.",
                            "http://cygwin.mbwarez.dk//cygwin/gw",
                            "http://cygwin.mbwarez.dk//cygwin/in/",
                            "http://cygwin.mbwarez.dk//cygwin/n/",
                            "http://cygwin.mbwarez.dk//cygwin/s://",
                            "http://cygwin.mbwarez.dk//cygwin/t.edu",
                            "http://cygwin.mbwarez.dk//cygwin32/",
                            "http://cygwin.mbwarez.dk//gwin/",
                            "http://cygwin.mbwarez.dk//gwin/htt",
                            "http://cygwin.mbwarez.dk//in/JR",
                            "http://cygwin.mbwarez.dk//in/win//",
                            "http://cygwin.mbwarez.dk//n/",
                            "http://cygwin.mbwarez.dk//n///",
                            "http://cygwin.mbwarez.dk//n/gwin/w",
                            "http://cygwin.mbwarez.dk//pub/cygwin/G",
                            "http://cygwin.mbwarez.dk/0",
                            "http://cygwin.mbwarez.dk/6",
                            "http://cygwin.mbwarez.dk/8K",
                            "http://cygwin.mbwarez.dk/9",
                            "http://cygwin.mbwarez.dk/;cygwin.mbwarez.dk;Europe;Denmark;noshow",
                            "http://cygwin.mbwarez.dk/?",
                            "http://cygwin.mbwarez.dk/C",
                            "http://cygwin.mbwarez.dk/China//",
                            "http://cygwin.mbwarez.dk/China0",
                            "http://cygwin.mbwarez.dk/Europe",
                            "http://cygwin.mbwarez.dk/Fpa",
                            "http://cygwin.mbwarez.dk/Hong",
                            "http://cygwin.mbwarez.dk/I",
                            "http://cygwin.mbwarez.dk/Moldova",
                            "http://cygwin.mbwarez.dk/O",
                            "http://cygwin.mbwarez.dk/Q",
                            "http://cygwin.mbwarez.dk/achen.de",
                            "http://cygwin.mbwarez.dk/argasso.net/9Z",
                            "http://cygwin.mbwarez.dk/auin/in//",
                            "http://cygwin.mbwarez.dk/auirror",
                            "http://cygwin.mbwarez.dk/bochum.de/down%",
                            "http://cygwin.mbwarez.dk/by",
                            "http://cygwin.mbwarez.dk/byfly.byen.de",
                            "http://cygwin.mbwarez.dk/c.jpin/or",
                            "http://cygwin.mbwarez.dk/c.org.ilc.jp0",
                            "http://cygwin.mbwarez.dk/checkdomain",
                            "http://cygwin.mbwarez.dk/chum.de",
                            "http://cygwin.mbwarez.dk/chum.de/cygwin=RAp.1",
                            "http://cygwin.mbwarez.dk/cygwin/",
                            "http://cygwin.mbwarez.dk/cygwin//",
                            "http://cygwin.mbwarez.dk/cygwin/://ft",
                            "http://cygwin.mbwarez.dk/cygwin/F",
                            "http://cygwin.mbwarez.dk/cygwin/in/ix",
                            "http://cygwin.mbwarez.dk/cygwin/n/",
                            "http://cygwin.mbwarez.dk/cygwin/n//ftf",
                            "http://cygwin.mbwarez.dk/cygwin/n/tac",
                            "http://cygwin.mbwarez.dk/cygwin/p://mi",
                            "http://cygwin.mbwarez.dk/cygwin/win/l",
                            "http://cygwin.mbwarez.dk/cygwin/yname.D",
                            "http://cygwin.mbwarez.dk/cygwin32/c",
                            "http://cygwin.mbwarez.dk/d.com/cygwin/",
                            "http://cygwin.mbwarez.dk/e",
                            "http://cygwin.mbwarez.dk/e/cygwin/kod/",
                            "http://cygwin.mbwarez.dk/edu.cnet",
                            "http://cygwin.mbwarez.dk/eetin/",
                            "http://cygwin.mbwarez.dk/en.de",
                            "http://cygwin.mbwarez.dk/et.fion/",
                            "http://cygwin.mbwarez.dk/et/cygwin//7",
                            "http://cygwin.mbwarez.dk/et/cygwin/p",
                            "http://cygwin.mbwarez.dk/etcygwin/.ma",
                            "http://cygwin.mbwarez.dk/etworks.orgy",
                            "http://cygwin.mbwarez.dk/g/cygwin/%Kjp.",
                            "http://cygwin.mbwarez.dk/garr.itrror.d",
                            "http://cygwin.mbwarez.dk/gie.fr",
                            "http://cygwin.mbwarez.dk/gie.frygwin/",
                            "http://cygwin.mbwarez.dk/gwin/",
                            "http://cygwin.mbwarez.dk/gwin/.org//",
                            "http://cygwin.mbwarez.dk/gwin///k",
                            "http://cygwin.mbwarez.dk/gwin/cygwin/9",
                            "http://cygwin.mbwarez.dk/gwin/in/",
                            "http://cygwin.mbwarez.dk/gwin/n//",
                            "http://cygwin.mbwarez.dk/h.de",
                            "http://cygwin.mbwarez.dk/hen.de.com",
                            "http://cygwin.mbwarez.dk/https://mirror2Bupa5",
                            "http://cygwin.mbwarez.dk/ia",
                            "http://cygwin.mbwarez.dk/in/",
                            "http://cygwin.mbwarez.dk/in//",
                            "http://cygwin.mbwarez.dk/in//win/)",
                            "http://cygwin.mbwarez.dk/in/in//X",
                            "http://cygwin.mbwarez.dk/in/in/n/",
                            "http://cygwin.mbwarez.dk/in/in32/",
                            "http://cygwin.mbwarez.dk/in/n.de",
                            "http://cygwin.mbwarez.dk/in/n/",
                            "http://cygwin.mbwarez.dk/in/n/%",
                            "http://cygwin.mbwarez.dk/in/win/twin3",
                            "http://cygwin.mbwarez.dk/in/win32/",
                            "http://cygwin.mbwarez.dk/in/ygwin/",
                            "http://cygwin.mbwarez.dk/irrors/sourcew",
                            "http://cygwin.mbwarez.dk/jp1p",
                            "http://cygwin.mbwarez.dk/m",
                            "http://cygwin.mbwarez.dk/m/cygwin/9JpF",
                            "http://cygwin.mbwarez.dk/min/.",
                            "http://cygwin.mbwarez.dk/n/",
                            "http://cygwin.mbwarez.dk/n/cB",
                            "http://cygwin.mbwarez.dk/n/cygwin/",
                            "http://cygwin.mbwarez.dk/n/cygwin/(",
                            "http://cygwin.mbwarez.dk/n/in/in/",
                            "http://cygwin.mbwarez.dk/net//",
                            "http://cygwin.mbwarez.dk/netm",
                            "http://cygwin.mbwarez.dk/netn/in/",
                            "http://cygwin.mbwarez.dk/ng",
                            "http://cygwin.mbwarez.dk/om",
                            "http://cygwin.mbwarez.dk/om/cygwin/",
                            "http://cygwin.mbwarez.dk/om/cygwin/B",
                            "http://cygwin.mbwarez.dk/om/cygwin/c",
                            "http://cygwin.mbwarez.dk/om/cygwin/d.o$",
                            "http://cygwin.mbwarez.dk/om/cygwin/ja",
                            "http://cygwin.mbwarez.dk/org1",
                            "http://cygwin.mbwarez.dk/p",
                            "http://cygwin.mbwarez.dk/p.inf.tu-dresd",
                            "http://cygwin.mbwarez.dk/pks.orgmi",
                            "http://cygwin.mbwarez.dk/r/cygwin/",
                            "http://cygwin.mbwarez.dk/rks.org/r",
                            "http://cygwin.mbwarez.dk/rro",
                            "http://cygwin.mbwarez.dk/rror.isoc.oC",
                            "http://cygwin.mbwarez.dk/st",
                            "http://cygwin.mbwarez.dk/t/cygwin/",
                            "http://cygwin.mbwarez.dk/t/cygwin//",
                            "http://cygwin.mbwarez.dk/t/cygwin/t",
                            "http://cygwin.mbwarez.dk/then.de",
                            "http://cygwin.mbwarez.dk/ttp://ftp.f",
                            "http://cygwin.mbwarez.dk/ttps://",
                            "http://cygwin.mbwarez.dk/tworks.org/",
                            "http://cygwin.mbwarez.dk/u.cn",
                            "http://cygwin.mbwarez.dk/u.cn/cP",
                            "http://cygwin.mbwarez.dk/u.edu.cnC",
                            "http://cygwin.mbwarez.dk/ub/cygwin/cBVp",
                            "http://cygwin.mbwarez.dk/ucomP",
                            "http://cygwin.mbwarez.dk/wente.nlno/tG",
                            "http://cygwin.mbwarez.dk/win/",
                            "http://cygwin.mbwarez.dk/win/3",
                            "http://cygwin.mbwarez.dk/win/acente",
                            "http://cygwin.mbwarez.dk/win/gwin/O",
                            "http://cygwin.mbwarez.dk/win/in/:",
                            "http://cygwin.mbwarez.dk/win/it",
                            "http://cygwin.mbwarez.dk/win/n/(",
                            "http://cygwin.mbwarez.dk/win/win/",
                            "http://cygwin.mbwarez.dk/win/win/p://Z",
                            "http://cygwin.mbwarez.dk/ygwin/",
                            "http://cygwin.mbwarez.dk/ygwin/.ncH",
                            "http://cygwin.mbwarez.dk/ygwin//",
                            "http://cygwin.mbwarez.dk/ygwin/E",
                            "http://cygwin.mbwarez.dk/ygwin/I",
                            "http://cygwin.mbwarez.dk/ygwin/cyg",
                            "http://cygwin.mbwarez.dk/ygwin/cygwin/",
                            "http://cygwin.mbwarez.dk/ygwin/n/",
                            "http://cygwin.mbwarez.dk0",
                            "http://cygwin.mbwarez.dkI",
                            "http://cygwin.mbwarez.dkaachen.de;",
                            "http://cygwin.mbwarez.dkaachen.dewin/",
                            "http://cygwin.mbwarez.dkachen",
                            "http://cygwin.mbwarez.dkare.mirror.garr",
                            "http://cygwin.mbwarez.dkarez.d",
                            "http://cygwin.mbwarez.dkargasso.netkod/",
                            "http://cygwin.mbwarez.dkauc.nzin/",
                            "http://cygwin.mbwarez.dkauwin/p://ftp"
                        ],
                        "id": "238",
                        "description": "URLs found in memory or binary data"
                    },
                    {
                        "severity": "IMPACT_SEVERITY_INFO",
                        "match_data": [
                            "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\ETCJ2WHM"
                        ],
                        "id": "90",
                        "description": "Creates files inside the user directory"
                    },
                    {
                        "severity": "IMPACT_SEVERITY_INFO",
                        "match_data": [
                            "8.43.85.97:443 -> 192.168.2.9:49704 version: TLS 1.2"
                        ],
                        "id": "7058",
                        "description": "Uses secure TLS version for HTTPS connections"
                    },
                    {
                        "id": "625",
                        "match_data": [
                            "HTTP traffic on port 443 -> 49720",
                            "HTTP traffic on port 49720 -> 443"
                        ],
                        "description": "Uses HTTPS",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "263",
                        "refs": [
                            {
                                "ref": "#memory_dumps",
                                "value": "file.exe, 00000001.00000002.4863440201.000000000013E000.00000004.00000020.00020000.00000000.sdmp"
                            },
                            {
                                "ref": "#memory_dumps",
                                "value": "file.exe, 00000001.00000002.4863975444.0000000000185000.00000004.00000020.00020000.00000000.sdmp, file.exe, 00000001.00000002.4862480485.00000000000B8000.00000004.00000020.00020000.00000000.sdmp"
                            }
                        ],
                        "match_data": [
                            "Hyper-V RAW ^",
                            "Hyper-V RAW"
                        ],
                        "description": "May try to detect the virtual machine to hinder analysis (VM artifact strings found in memory)",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "238",
                        "match_data": [
                            "ftp://cygwin.mirror.rafal.cap",
                            "ftp://ftp.acc.umu.se/mirror/cygwin/http",
                            "ftp://ftp.byfly.by/pub/cygwin/in",
                            "ftp://ftp.byfly.by/pub/cygwin/win/",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/https://",
                            "ftp://ftp.fau.de/cygwin/.can",
                            "ftp://ftp.fau.de/cygwin/c",
                            "ftp://ftp.fs",
                            "ftp://ftp.fsn.hu/pub/cygwin/irror",
                            "ftp://ftp.fsn.hu/pub/cygwin/r",
                            "ftp://ftp.fsn.hu/pub/cygwin/s",
                            "ftp://ftp.fsn.hu/pub/cygwin/ygwin",
                            "ftp://ftp.fsn.huhttps:/",
                            "ftp://ftp.funet.fi",
                            "ftp://ftp.funet.fi/pub/mirrors/sourceware.org/pub/cygwin/gwin/https://",
                            "ftp://ftp.funet.fi/pub/mirrors/sourceware.org/pub/cygwin/org",
                            "ftp://ftp.halifax.rwth-aachen.de/cygwin/http://m",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/http://m~",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/https://",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/https://S",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/https://V",
                            "ftp://ftp.inf.tu-dresden.de/software/windows/cygwin32/kdomain",
                            "ftp://ftp.kaist.ac.kr/cygwin/in/arr.itgen.denet",
                            "ftp://ftp.kr.freebsd.org",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/http://cr",
                            "ftp://ftp.kr.freebsd.orghttps://",
                            "ftp://ftp.kr.freebsd.orgygwin/https://",
                            "ftp://ftp.lip6.fr/pub/cygwin/",
                            "ftp://ftp.lip6.fr/pub/cygwin/in/https://U",
                            "ftp://ftp.lip6.fr/pub/cygwin/p",
                            "ftp://ftp.mirrorservice.org/sites/sourceware.org/pub/cygwin/",
                            "ftp://ftp.mirrorservice.org/sites/sourceware.org/pub/cygwin/gwin",
                            "ftp://ftp.n",
                            "ftp://ftp.nP",
                            "ftp://ftp.ntua.gr/pub/pc/cygwin/",
                            "ftp://ftp.ntua.gr/pub/pc/cygwin/https://U",
                            "ftp://ftp.ntua.grhttps:",
                            "ftp://ftp.rn",
                            "ftp://ftp.rnl.tecnico.ulisboa.pt/pub/cygwin/http://m",
                            "ftp://ftp.snt.utwente.nl",
                            "ftp://ftp.snt.utwente.nlt",
                            "ftp://ftp.x",
                            "ftp://ftp.yz.yamagata-u.ac.jp/pub/cygwin/",
                            "ftp://ftp.yz.yamagata-u.ac.jp/pub/cygwin/c",
                            "ftp://linux.rz.ruhr-uni-bochum.de/cygwin/https://",
                            "ftp://mirror.checkdomain.de/cygwin/https://ftp.i",
                            "ftp://mirror.easyname.athttp://c",
                            "ftp://mirror.internode.on.net/pub/cygwin/",
                            "ftp://mirror.internode.on.netrs",
                            "ftp://mirror.lagoon.nc/cygwin/http://fV",
                            "ftp://mirrors.dotsrc.org/mirrors/cygwin/in/",
                            "ftp://mirrors.dotsrc.orggn.dehttp://f=",
                            "ftp://mirrors.dotsrc.orgn.deom",
                            "ftp://mirrors.xmission.com/cygwin/com/http://fL",
                            "ftp://sourceware.org/ftp://sources.redhat.com/ftp://gcc.gnu.org/",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin///http://m",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/http://m",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/https://",
                            "http://ac.economia.gob.mx/cps.html0",
                            "http://ac.economia.gob.mx/last.crl0G",
                            "http://acedicom.edicomgroup.com/doc0",
                            "http://acraiz.icpbrasil.gov.br/DPCacraiz.pdf0?",
                            "http://acraiz.icpbrasil.gov.br/LCRacraizv1.crl0",
                            "http://acraiz.icpbrasil.gov.br/LCRacraizv2.crl0",
                            "http://apps.identrust.com/roots/dstrootcax3.p7c0",
                            "http://ca.disig.sk/ca/crl/ca_disig.crl0",
                            "http://ca.mtin.es/mtin/DPCyPoliticas0",
                            "http://ca.mtin.es/mtin/DPCyPoliticas0g",
                            "http://ca.mtin.es/mtin/crl/MTINAutoridadRaiz03",
                            "http://ca.mtin.es/mtin/ocsp0",
                            "http://ca2.mtin.es/mtin/crl/MTINAutoridadRaiz0",
                            "http://certificates.starfieldtech.com/repository/1604",
                            "http://certs.oati.net/repository/OATICA2.crl0",
                            "http://certs.oati.net/repository/OATICA2.crt0",
                            "http://certs.oaticerts.com/repository/OATICA2.crl",
                            "http://certs.oaticerts.com/repository/OATICA2.crt08",
                            "http://cps.chambersign.org/cps/chambersignroot.html0",
                            "http://cps.chambersign.org/cps/chambersroot.html0",
                            "http://cps.letsencrypt.org0",
                            "http://cps.root-x1.letsencrypt.org0",
                            "http://cps.siths.se/sithsrootcav1.html0",
                            "http://crl.certigna.fr/certignarootca.crl01",
                            "http://crl.chambersign.org/chambersignroot.crl0",
                            "http://crl.chambersign.org/chambersroot.crl0",
                            "http://crl.comodoca.com/AAACertificateServices.crl06",
                            "http://crl.defence.gov.au/pki0",
                            "http://crl.dhimyotis.com/certignarootca.crl0",
                            "http://crl.globalsign.net/root-r2.crl0",
                            "http://crl.identrust.com/DSTROOTCAX3CRL.crl0",
                            "http://crl.oces.trust2408.com/oces.crl0",
                            "http://crl.pki.wellsfargo.com/wsprca.crl0",
                            "http://crl.securetrust.com/SGCA.crl0",
                            "http://crl.securetrust.com/STCA.crl0",
                            "http://crl.ssc.lt/root-a/cacrl.crl0",
                            "http://crl.ssc.lt/root-b/cacrl.crl0",
                            "http://crl.ssc.lt/root-c/cacrl.crl0",
                            "http://crl.xrampsecurity.com/XGCA.crl0",
                            "http://crl1.comsign.co.il/crl/comsignglobalrootca.crl0",
                            "http://ctldl.windowsupdate.com/R",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/CABD2A79A1076A31F21D253635CB0",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/authrootstl.cab",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en031b9",
                            "http://ctldl.windowsupdate.com:80/msdownload/update/v3/static/trustedr/en/CABD2A79A1076A31F21D253635",
                            "http://cygwin.cathedral-",
                            "http://cygwin.cathedral-.",
                            "http://cygwin.cathedral-networks.org",
                            "http://cygwin.cathedral-networks.org%",
                            "http://cygwin.cathedral-networks.org-itU",
                            "http://cygwin.cathedral-networks.org.",
                            "http://cygwin.cathedral-networks.org/",
                            "http://cygwin.cathedral-networks.org/#",
                            "http://cygwin.cathedral-networks.org/%",
                            "http://cygwin.cathedral-networks.org/(",
                            "http://cygwin.cathedral-networks.org/)",
                            "http://cygwin.cathedral-networks.org/-m",
                            "http://cygwin.cathedral-networks.org/.eS",
                            "http://cygwin.cathedral-networks.org/.o",
                            "http://cygwin.cathedral-networks.org/.s",
                            "http://cygwin.cathedral-networks.org//",
                            "http://cygwin.cathedral-networks.org//&",
                            "http://cygwin.cathedral-networks.org///",
                            "http://cygwin.cathedral-networks.org///E",
                            "http://cygwin.cathedral-networks.org///g",
                            "http://cygwin.cathedral-networks.org//U",
                            "http://cygwin.cathedral-networks.org//f",
                            "http://cygwin.cathedral-networks.org//l",
                            "http://cygwin.cathedral-networks.org//m",
                            "http://cygwin.cathedral-networks.org//mX",
                            "http://cygwin.cathedral-networks.org//o",
                            "http://cygwin.cathedral-networks.org/5",
                            "http://cygwin.cathedral-networks.org/:",
                            "http://cygwin.cathedral-networks.org/:/-",
                            "http://cygwin.cathedral-networks.org/;",
                            "http://cygwin.cathedral-networks.org/;cygwin.cathedral-networks.org;Europe;Norway;noshow",
                            "http://cygwin.cathedral-networks.org/B",
                            "http://cygwin.cathedral-networks.org/D",
                            "http://cygwin.cathedral-networks.org/E",
                            "http://cygwin.cathedral-networks.org/Europe",
                            "http://cygwin.cathedral-networks.org/K",
                            "http://cygwin.cathedral-networks.org/L",
                            "http://cygwin.cathedral-networks.org/M",
                            "http://cygwin.cathedral-networks.org/R",
                            "http://cygwin.cathedral-networks.org/a",
                            "http://cygwin.cathedral-networks.org/a=",
                            "http://cygwin.cathedral-networks.org/c",
                            "http://cygwin.cathedral-networks.org/cy",
                            "http://cygwin.cathedral-networks.org/du",
                            "http://cygwin.cathedral-networks.org/e/",
                            "http://cygwin.cathedral-networks.org/ed",
                            "http://cygwin.cathedral-networks.org/f",
                            "http://cygwin.cathedral-networks.org/ftg",
                            "http://cygwin.cathedral-networks.org/gwN",
                            "http://cygwin.cathedral-networks.org/h",
                            "http://cygwin.cathedral-networks.org/in",
                            "http://cygwin.cathedral-networks.org/irD",
                            "http://cygwin.cathedral-networks.org/k",
                            "http://cygwin.cathedral-networks.org/l(",
                            "http://cygwin.cathedral-networks.org/la",
                            "http://cygwin.cathedral-networks.org/li",
                            "http://cygwin.cathedral-networks.org/m",
                            "http://cygwin.cathedral-networks.org/mT",
                            "http://cygwin.cathedral-networks.org/mi",
                            "http://cygwin.cathedral-networks.org/n/",
                            "http://cygwin.cathedral-networks.org/nl",
                            "http://cygwin.cathedral-networks.org/o.",
                            "http://cygwin.cathedral-networks.org/p",
                            "http://cygwin.cathedral-networks.org/p:",
                            "http://cygwin.cathedral-networks.org/pl",
                            "http://cygwin.cathedral-networks.org/pu_",
                            "http://cygwin.cathedral-networks.org/r",
                            "http://cygwin.cathedral-networks.org/rs",
                            "http://cygwin.cathedral-networks.org/s.",
                            "http://cygwin.cathedral-networks.org/t",
                            "http://cygwin.cathedral-networks.org/t.",
                            "http://cygwin.cathedral-networks.org/t.z",
                            "http://cygwin.cathedral-networks.org/te",
                            "http://cygwin.cathedral-networks.org/tp",
                            "http://cygwin.cathedral-networks.org/tv",
                            "http://cygwin.cathedral-networks.org/uw",
                            "http://cygwin.cathedral-networks.org/w",
                            "http://cygwin.cathedral-networks.org/x",
                            "http://cygwin.cathedral-networks.org0",
                            "http://cygwin.cathedral-networks.org1",
                            "http://cygwin.cathedral-networks.org2",
                            "http://cygwin.cathedral-networks.orgG",
                            "http://cygwin.cathedral-networks.orgM",
                            "http://cygwin.cathedral-networks.orga",
                            "http://cygwin.cathedral-networks.orge",
                            "http://cygwin.cathedral-networks.orget",
                            "http://cygwin.cathedral-networks.orgf",
                            "http://cygwin.cathedral-networks.orgftp",
                            "http://cygwin.cathedral-networks.orggwi",
                            "http://cygwin.cathedral-networks.orgk",
                            "http://cygwin.cathedral-networks.orgl",
                            "http://cygwin.cathedral-networks.orgn",
                            "http://cygwin.cathedral-networks.orgn.ct",
                            "http://cygwin.cathedral-networks.orgn.v",
                            "http://cygwin.cathedral-networks.orgn/",
                            "http://cygwin.cathedral-networks.orgnf.",
                            "http://cygwin.cathedral-networks.orgny",
                            "http://cygwin.cathedral-networks.orgr",
                            "http://cygwin.cathedral-networks.orgs:/",
                            "http://cygwin.cathedral-networks.orgtp",
                            "http://cygwin.cathedral-networks.orgtp:",
                            "http://cygwin.cathedral-networks.orgttp",
                            "http://cygwin.cathedral-networks.orgwaren.net",
                            "http://cygwin.cathedral-networks.orgygw",
                            "http://cygwin.mbwarez",
                            "http://cygwin.mbwarez.dk",
                            "http://cygwin.mbwarez.dk%",
                            "http://cygwin.mbwarez.dk)",
                            "http://cygwin.mbwarez.dk-bochum.detwar",
                            "http://cygwin.mbwarez.dk.ac.jp",
                            "http://cygwin.mbwarez.dk.com/cygwin/",
                            "http://cygwin.mbwarez.dk.com/cygwin/K",
                            "http://cygwin.mbwarez.dk.de",
                            "http://cygwin.mbwarez.dk.de/cygwin/",
                            "http://cygwin.mbwarez.dk.deom/cygwin/",
                            "http://cygwin.mbwarez.dk.fau.de/cygwin/",
                            "http://cygwin.mbwarez.dk.garr.it/n/t",
                            "http://cygwin.mbwarez.dk.garr.itet/",
                            "http://cygwin.mbwarez.dk.neto.",
                            "http://cygwin.mbwarez.dk.org/mirror-hk",
                            "http://cygwin.mbwarez.dk.orge-",
                            "http://cygwin.mbwarez.dk.twaren.netome",
                            "http://cygwin.mbwarez.dk/",
                            "http://cygwin.mbwarez.dk/#",
                            "http://cygwin.mbwarez.dk/$",
                            "http://cygwin.mbwarez.dk/%8",
                            "http://cygwin.mbwarez.dk/-",
                            "http://cygwin.mbwarez.dk/.ac.nz/",
                            "http://cygwin.mbwarez.dk/.com/win/:",
                            "http://cygwin.mbwarez.dk/.de.netynZ",
                            "http://cygwin.mbwarez.dk/.de/",
                            "http://cygwin.mbwarez.dk/.de/cygwin/t",
                            "http://cygwin.mbwarez.dk/.fsn.hue",
                            "http://cygwin.mbwarez.dk/.jpygwin/1",
                            "http://cygwin.mbwarez.dk/.lip6.fr",
                            "http://cygwin.mbwarez.dk/.n",
                            "http://cygwin.mbwarez.dk/.net",
                            "http://cygwin.mbwarez.dk//",
                            "http://cygwin.mbwarez.dk///",
                            "http://cygwin.mbwarez.dk///cygwin/",
                            "http://cygwin.mbwarez.dk///ygwin/K",
                            "http://cygwin.mbwarez.dk///ygwin32/1",
                            "http://cygwin.mbwarez.dk//1",
                            "http://cygwin.mbwarez.dk//cygwin/",
                            "http://cygwin.mbwarez.dk//cygwin//",
                            "http://cygwin.mbwarez.dk//cygwin/in/",
                            "http://cygwin.mbwarez.dk//cygwin/n$",
                            "http://cygwin.mbwarez.dk//cygwin/n/o",
                            "http://cygwin.mbwarez.dk//cygwin/ps://",
                            "http://cygwin.mbwarez.dk//cygwin/win/",
                            "http://cygwin.mbwarez.dk//gwin/",
                            "http://cygwin.mbwarez.dk//gwin/Z",
                            "http://cygwin.mbwarez.dk//in/",
                            "http://cygwin.mbwarez.dk//mirror.easyna",
                            "http://cygwin.mbwarez.dk//pub/cygwin/Z",
                            "http://cygwin.mbwarez.dk//win//A",
                            "http://cygwin.mbwarez.dk/0",
                            "http://cygwin.mbwarez.dk/1",
                            "http://cygwin.mbwarez.dk/3",
                            "http://cygwin.mbwarez.dk/5",
                            "http://cygwin.mbwarez.dk/:",
                            "http://cygwin.mbwarez.dk/;",
                            "http://cygwin.mbwarez.dk/;cygwin.mbwarez.dk;Europe;Denmark;noshow",
                            "http://cygwin.mbwarez.dk/AM",
                            "http://cygwin.mbwarez.dk/C",
                            "http://cygwin.mbwarez.dk/Japan",
                            "http://cygwin.mbwarez.dk/K",
                            "http://cygwin.mbwarez.dk/O",
                            "http://cygwin.mbwarez.dk/U",
                            "http://cygwin.mbwarez.dk/V",
                            "http://cygwin.mbwarez.dk/a8",
                            "http://cygwin.mbwarez.dk/ac.jpneusoft.",
                            "http://cygwin.mbwarez.dk/ad.jp",
                            "http://cygwin.mbwarez.dk/bochum.de://m",
                            "http://cygwin.mbwarez.dk/c.jp",
                            "http://cygwin.mbwarez.dk/c.jpygwin/.c",
                            "http://cygwin.mbwarez.dk/cnico.ulisb",
                            "http://cygwin.mbwarez.dk/cygwin/",
                            "http://cygwin.mbwarez.dk/cygwin//",
                            "http://cygwin.mbwarez.dk/cygwin//t",
                            "http://cygwin.mbwarez.dk/cygwin/K",
                            "http://cygwin.mbwarez.dk/cygwin/e",
                            "http://cygwin.mbwarez.dk/cygwin/l",
                            "http://cygwin.mbwarez.dk/cygwin/n/",
                            "http://cygwin.mbwarez.dk/cygwin/ree",
                            "http://cygwin.mbwarez.dk/cygwin32/",
                            "http://cygwin.mbwarez.dk/d.comwin/",
                            "http://cygwin.mbwarez.dk/de/cygwin/n/D",
                            "http://cygwin.mbwarez.dk/derks.org/j",
                            "http://cygwin.mbwarez.dk/e",
                            "http://cygwin.mbwarez.dk/e/cygwin/s://",
                            "http://cygwin.mbwarez.dk/edu.cnwin/",
                            "http://cygwin.mbwarez.dk/en.dein/l",
                            "http://cygwin.mbwarez.dk/er.it",
                            "http://cygwin.mbwarez.dk/et",
                            "http://cygwin.mbwarez.dk/et/cygwin/e",
                            "http://cygwin.mbwarez.dk/etm.deZ",
                            "http://cygwin.mbwarez.dk/etum.de",
                            "http://cygwin.mbwarez.dk/gie.frygwin/",
                            "http://cygwin.mbwarez.dk/gwin/",
                            "http://cygwin.mbwarez.dk/gwin/-",
                            "http://cygwin.mbwarez.dk/gwin//",
                            "http://cygwin.mbwarez.dk/gwin/2",
                            "http://cygwin.mbwarez.dk/gwin/4",
                            "http://cygwin.mbwarez.dk/gwin/aet/",
                            "http://cygwin.mbwarez.dk/gwin/in/",
                            "http://cygwin.mbwarez.dk/gwin/p",
                            "http://cygwin.mbwarez.dk/gwin/s",
                            "http://cygwin.mbwarez.dk/gwin/u",
                            "http://cygwin.mbwarez.dk/gwin/win/",
                            "http://cygwin.mbwarez.dk/h",
                            "http://cygwin.mbwarez.dk/h.de",
                            "http://cygwin.mbwarez.dk/hen.de",
                            "http://cygwin.mbwarez.dk/hen.dein/w",
                            "http://cygwin.mbwarez.dk/hen.den/",
                            "http://cygwin.mbwarez.dk/https://",
                            "http://cygwin.mbwarez.dk/in/",
                            "http://cygwin.mbwarez.dk/in/&",
                            "http://cygwin.mbwarez.dk/in//",
                            "http://cygwin.mbwarez.dk/in/9G",
                            "http://cygwin.mbwarez.dk/in/:",
                            "http://cygwin.mbwarez.dk/in/ch",
                            "http://cygwin.mbwarez.dk/in/chhinas",
                            "http://cygwin.mbwarez.dk/in/cygwin/D",
                            "http://cygwin.mbwarez.dk/in/gwin/",
                            "http://cygwin.mbwarez.dk/in/gwin/e",
                            "http://cygwin.mbwarez.dk/in/ttp://mQ",
                            "http://cygwin.mbwarez.dk/in/usoft.e",
                            "http://cygwin.mbwarez.dk/in/ygwin/.",
                            "http://cygwin.mbwarez.dk/irrors.ustc",
                            "http://cygwin.mbwarez.dk/ites/sourceware.org/pub/cygwin/ygwin/yz.yamagata-u.ac.jp3",
                            "http://cygwin.mbwarez.dk/loo.cagwin/",
                            "http://cygwin.mbwarez.dk/m",
                            "http://cygwin.mbwarez.dk/m8",
                            "http://cygwin.mbwarez.dk/n/",
                            "http://cygwin.mbwarez.dk/n/cygwin/",
                            "http://cygwin.mbwarez.dk/n/cygwin/edu.",
                            "http://cygwin.mbwarez.dk/n/gwin32/4",
                            "http://cygwin.mbwarez.dk/n/in/",
                            "http://cygwin.mbwarez.dk/n/n/Y",
                            "http://cygwin.mbwarez.dk/n/win/p",
                            "http://cygwin.mbwarez.dk/net",
                            "http://cygwin.mbwarez.dk/netso.net/",
                            "http://cygwin.mbwarez.dk/no/cygwin/",
                            "http://cygwin.mbwarez.dk/o/cygwin/ats",
                            "http://cygwin.mbwarez.dk/om/cygwin/",
                            "http://cygwin.mbwarez.dk/om/cygwin/lftp.twaren.net",
                            "http://cygwin.mbwarez.dk/or.internode.o",
                            "http://cygwin.mbwarez.dk/p6.frV",
                            "http://cygwin.mbwarez.dk/p://ftp.1",
                            "http://cygwin.mbwarez.dk/pub/cygwin/",
                            "http://cygwin.mbwarez.dk/pub/cygwin/c",
                            "http://cygwin.mbwarez.dk/rg",
                            "http://cygwin.mbwarez.dk/rg/cygwin/",
                            "http://cygwin.mbwarez.dk/rg/cygwin/y",
                            "http://cygwin.mbwarez.dk/riapub/cygq",
                            "http://cygwin.mbwarez.dk/rs.163.com",
                            "http://cygwin.mbwarez.dk/rth",
                            "http://cygwin.mbwarez.dk/st",
                            "http://cygwin.mbwarez.dk/st.comn/",
                            "http://cygwin.mbwarez.dk/t/cygwin/;",
                            "http://cygwin.mbwarez.dk/thttps://",
                            "http://cygwin.mbwarez.dk/twin/stc.edu",
                            "http://cygwin.mbwarez.dk/u.cawin/",
                            "http://cygwin.mbwarez.dk/u.cnitr/cygw",
                            "http://cygwin.mbwarez.dk/win//in/",
                            "http://cygwin.mbwarez.dk/win/c",
                            "http://cygwin.mbwarez.dk/win/gwin/",
                            "http://cygwin.mbwarez.dk/win/in/k",
                            "http://cygwin.mbwarez.dk/win/kdomai",
                            "http://cygwin.mbwarez.dk/win/n/",
                            "http://cygwin.mbwarez.dk/win/n/win",
                            "http://cygwin.mbwarez.dk/win/rope",
                            "http://cygwin.mbwarez.dk/win/ygwin/m",
                            "http://cygwin.mbwarez.dk/x/sourceware.o",
                            "http://cygwin.mbwarez.dk/y/pub/mirrors/",
                            "http://cygwin.mbwarez.dk/y2",
                            "http://cygwin.mbwarez.dk/ygwin/",
                            "http://cygwin.mbwarez.dk/ygwin///",
                            "http://cygwin.mbwarez.dk/ygwin/2/",
                            "http://cygwin.mbwarez.dk/ygwin/6",
                            "http://cygwin.mbwarez.dk/ygwin/H",
                            "http://cygwin.mbwarez.dk/ygwin/N",
                            "http://cygwin.mbwarez.dk/ygwin/g.ca",
                            "http://cygwin.mbwarez.dk/ygwin/in/-",
                            "http://cygwin.mbwarez.dk/ygwin/n/",
                            "http://cygwin.mbwarez.dk/ygwin/r",
                            "http://cygwin.mbwarez.dk/ygwin/rors",
                            "http://cygwin.mbwarez.dk/ygwin/t",
                            "http://cygwin.mbwarez.dk/ygwin/tn/",
                            "http://cygwin.mbwarez.dk/ygwin/ygwin/",
                            "http://cygwin.mbwarez.dkD",
                            "http://cygwin.mbwarez.dkG",
                            "http://cygwin.mbwarez.dkK",
                            "http://cygwin.mbwarez.dkMoldova3",
                            "http://cygwin.mbwarez.dkP",
                            "http://cygwin.mbwarez.dkQ8"
                        ],
                        "description": "URLs found in memory or binary data",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "7058",
                        "match_data": [
                            "8.43.85.97:443 -> 192.168.2.14:49720 version: TLS 1.2"
                        ],
                        "description": "Uses secure TLS version for HTTPS connections",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "description": "Monitors certain registry keys / values for changes (often done to protect autostart functionality)",
                        "match_data": [
                            "HKEY_CURRENT_USER_Classes"
                        ],
                        "severity": "IMPACT_SEVERITY_INFO",
                        "id": "198"
                    },
                    {
                        "description": "Uses HTTPS",
                        "match_data": [
                            "HTTP traffic on port 443 -> 49738",
                            "HTTP traffic on port 49738 -> 443"
                        ],
                        "severity": "IMPACT_SEVERITY_INFO",
                        "id": "625"
                    },
                    {
                        "refs": [
                            {
                                "ref": "#memory_dumps",
                                "value": "software.exe, 00000000.00000002.4632916603.0000000000181000.00000004.00000020.00020000.00000000.sdmp"
                            },
                            {
                                "ref": "#memory_dumps",
                                "value": "software.exe, 00000000.00000002.4632393130.0000000000128000.00000004.00000020.00020000.00000000.sdmp"
                            }
                        ],
                        "description": "May try to detect the virtual machine to hinder analysis (VM artifact strings found in memory)",
                        "match_data": [
                            "Hyper-V RAW",
                            "Hyper-V RAWl"
                        ],
                        "severity": "IMPACT_SEVERITY_INFO",
                        "id": "263"
                    },
                    {
                        "description": "URLs found in memory or binary data",
                        "match_data": [
                            "ftp://ftp-stud.hs-esslingen.dein",
                            "ftp://ftp.byfly.by/pub/cygwin/ror",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin//or",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/http://c",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/https://",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/n",
                            "ftp://ftp.fs%CJ",
                            "ftp://ftp.fsn.hu/pub/cygwin/tp",
                            "ftp://ftp.fsn.huy",
                            "ftp://ftp.funet.fi/pub/mirrors/sourceware.org/pub/cygwin/s",
                            "ftp://ftp.halifax.rwth-aachen.de",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/http://m",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/https://",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/n",
                            "ftp://ftp.inf.tu-dresden.de",
                            "ftp://ftp.inf.tu-dresden.dejphttp://maq#",
                            "ftp://ftp.inf.tu-dresden.demirror",
                            "ftp://ftp.jaist.ac.jp/pub/cygwin/",
                            "ftp://ftp.kaist.ac.kr/cygwin/ftp",
                            "ftp://ftp.kaist.ac.kr/cygwin/https://",
                            "ftp://ftp.kaist.ac.kr/cygwin/or",
                            "ftp://ftp.kaist.ac.kr/cygwin/ror",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/https://",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/or",
                            "ftp://ftp.kr.freebsd.orgchen.dep",
                            "ftp://ftp.kr.freebsd.orgetg",
                            "ftp://ftp.kr.freebsd.orggwin/",
                            "ftp://ftp.l",
                            "ftp://ftp.lip6.fr/pub/cygwin/",
                            "ftp://ftp.muug.ca",
                            "ftp://ftp.n",
                            "ftp://ftp.ntua.gr/pub/pc/cygwin/",
                            "ftp://ftp.nu",
                            "ftp://ftp.rnl.tecnico.ulisboa.pt",
                            "ftp://ftp.rnl.tecnico.ulisboa.ptn",
                            "ftp://ftp.snt.utwente.nlst",
                            "ftp://ftp.snt.utwente.nlygwin/http://f",
                            "ftp://ftp.snt.utwente.nlz",
                            "ftp://ftp.twaren.net/Unix/sourceware.org/cygwin/https:",
                            "ftp://ftp.yz.yamagata-u.ac.jp/pub/cygwin/https://",
                            "ftp://ftp.yz.yamagata-u.ac.jp/pub/cygwin/n",
                            "ftp://ftp.yz.yamagata-u.ac.jphttps://",
                            "ftp://ftp.yz.yamagata-u.ac.jpin/",
                            "ftp://linux.rz.ruhr-uni-bochum.de",
                            "ftp://linux.rz.ruhr-uni-bochum.de/cygwin/n/",
                            "ftp://mirror.checkdomain.demirror",
                            "ftp://mirror.checkdomain.deygwin/",
                            "ftp://mirror.cs.vt.edu/pub/cygwin/cygwin/ygwin/",
                            "ftp://mirror.csclub.uwaterloo.ca/cygwin/",
                            "ftp://mirror.csclub.uwaterloo.ca/cygwin/.dk//https://",
                            "ftp://mirror.csclub.uwaterloo.ca/cygwin/http://",
                            "ftp://mirror.easyname.at/cygwin//",
                            "ftp://mirror.easyname.athttp://mirror.)",
                            "ftp://mirror.internode.on.net/pub/cygwin/http",
                            "ftp://mirror.internode.on.net/pub/cygwin/n/",
                            "ftp://mirror.internode.on.net/pub/cygwin/win/https://",
                            "ftp://mirror.internode.on.netin/",
                            "ftp://mirror.lagoon.nc/cygwin/",
                            "ftp://mirror.lagoon.nc/cygwin/r",
                            "ftp://mirror.rise.ph/cygwin/cygwin/http",
                            "ftp://mirrors.dotsrc.org/mirrors/cygwin/.net/",
                            "ftp://mirrors.sonic.net/cygwin/",
                            "ftp://mirrors.syringanetworks.net",
                            "ftp://mirrors.syringanetworks.net/cygwin/",
                            "ftp://sourceware.org/ftp://sources.redhat.com/ftp://gcc.gnu.org/",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/http://mmVT",
                            "http://ac.economia.gob.mx/cps.html0",
                            "http://ac.economia.gob.mx/last.crl0G",
                            "http://acedicom.edicomgroup.com/doc0",
                            "http://acraiz.icpbrasil.gov.br/DPCacraiz.pdf0?",
                            "http://acraiz.icpbrasil.gov.br/LCRacraizv1.crl0",
                            "http://acraiz.icpbrasil.gov.br/LCRacraizv2.crl0",
                            "http://apps.identrust.com/roots/dstrootcax3",
                            "http://apps.identrust.com/roots/dstrootcax3.p7c0",
                            "http://ca.disig.sk/ca/crl/ca_disig.crl0",
                            "http://ca.mtin.es/mtin/DPCyPoliticas0",
                            "http://ca.mtin.es/mtin/DPCyPoliticas0g",
                            "http://ca.mtin.es/mtin/crl/MTINAutoridadRaiz03",
                            "http://ca.mtin.es/mtin/ocsp0",
                            "http://ca2.mtin.es/mtin/crl/MTINAutoridadRaiz0",
                            "http://certificates.starfieldtech.com/repository/1604",
                            "http://certs.oati.net/repository/OATICA2.crl0",
                            "http://certs.oati.net/repository/OATICA2.crt0",
                            "http://certs.oaticerts.com/repository/OATICA2.crl",
                            "http://certs.oaticerts.com/repository/OATICA2.crt08",
                            "http://cps.chambersign.org/cps/chambersignroot.html0",
                            "http://cps.chambersign.org/cps/chambersroot.html0",
                            "http://cps.letsencrypt.org0",
                            "http://cps.root-x1.letsencrypt.org0",
                            "http://cps.siths.se/sithsrootcav1.html0",
                            "http://crl.certigna.fr/certignarootca.crl01",
                            "http://crl.chambersign.org/chambersignroot.crl0",
                            "http://crl.chambersign.org/chambersroot.crl0",
                            "http://crl.comodoca.com/AAACertificateServices.crl06",
                            "http://crl.defence.gov.au/pki0",
                            "http://crl.dhimyotis.com/certignarootca.crl0",
                            "http://crl.globalsign.net/root-r2.crl0",
                            "http://crl.identrust.com/DSTROOTCAX3CRL.crl0",
                            "http://crl.oces.trust2408.com/oces.crl0",
                            "http://crl.pki.wellsfargo.com/wsprca.crl0",
                            "http://crl.securetrust.com/SGCA.crl0",
                            "http://crl.securetrust.com/STCA.crl0",
                            "http://crl.ssc.lt/root-a/cacrl.crl0",
                            "http://crl.ssc.lt/root-b/cacrl.crl0",
                            "http://crl.ssc.lt/root-c/cacrl.crl0",
                            "http://crl.xrampsecurity.com/XGCA.crl0",
                            "http://crl1.comsign.co.il/crl/comsignglobalrootca.crl0",
                            "http://ctldl.windowsupdate.com/Jg-AJ",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/CABD2A79A1076A31F21D253635CB0",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/authrootstl.cab",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/enEM32",
                            "http://ctldl.windowsupdate.com:80/msdownload/update/v3/static/trustedr/en/CABD2A79A1076A31F21D253635",
                            "http://cygwin.cathedral-",
                            "http://cygwin.cathedral-7T",
                            "http://cygwin.cathedral-networks",
                            "http://cygwin.cathedral-networks.org",
                            "http://cygwin.cathedral-networks.org$h",
                            "http://cygwin.cathedral-networks.org-f",
                            "http://cygwin.cathedral-networks.org.ed-",
                            "http://cygwin.cathedral-networks.org/",
                            "http://cygwin.cathedral-networks.org/&G",
                            "http://cygwin.cathedral-networks.org/(v",
                            "http://cygwin.cathedral-networks.org/.",
                            "http://cygwin.cathedral-networks.org/.i",
                            "http://cygwin.cathedral-networks.org/.j",
                            "http://cygwin.cathedral-networks.org//",
                            "http://cygwin.cathedral-networks.org//-v",
                            "http://cygwin.cathedral-networks.org///",
                            "http://cygwin.cathedral-networks.org///.X",
                            "http://cygwin.cathedral-networks.org//=j",
                            "http://cygwin.cathedral-networks.org//NU6",
                            "http://cygwin.cathedral-networks.org//Pj&",
                            "http://cygwin.cathedral-networks.org//SP$",
                            "http://cygwin.cathedral-networks.org//fPV",
                            "http://cygwin.cathedral-networks.org//m",
                            "http://cygwin.cathedral-networks.org/0M",
                            "http://cygwin.cathedral-networks.org/://",
                            "http://cygwin.cathedral-networks.org/;D",
                            "http://cygwin.cathedral-networks.org/;cygwin.cathedral-networks.org;Europe;Norway;noshow",
                            "http://cygwin.cathedral-networks.org/C",
                            "http://cygwin.cathedral-networks.org/Ev5",
                            "http://cygwin.cathedral-networks.org/FX",
                            "http://cygwin.cathedral-networks.org/Hk/",
                            "http://cygwin.cathedral-networks.org/Ih/",
                            "http://cygwin.cathedral-networks.org/Ji/",
                            "http://cygwin.cathedral-networks.org/Jj",
                            "http://cygwin.cathedral-networks.org/Ld",
                            "http://cygwin.cathedral-networks.org/Ti%",
                            "http://cygwin.cathedral-networks.org/Uf%",
                            "http://cygwin.cathedral-networks.org/Uk",
                            "http://cygwin.cathedral-networks.org/W",
                            "http://cygwin.cathedral-networks.org/_",
                            "http://cygwin.cathedral-networks.org/_C",
                            "http://cygwin.cathedral-networks.org/_f#",
                            "http://cygwin.cathedral-networks.org/ad/l",
                            "http://cygwin.cathedral-networks.org/al",
                            "http://cygwin.cathedral-networks.org/an",
                            "http://cygwin.cathedral-networks.org/c",
                            "http://cygwin.cathedral-networks.org/cy",
                            "http://cygwin.cathedral-networks.org/d",
                            "http://cygwin.cathedral-networks.org/eD",
                            "http://cygwin.cathedral-networks.org/f",
                            "http://cygwin.cathedral-networks.org/fr",
                            "http://cygwin.cathedral-networks.org/ftXS",
                            "http://cygwin.cathedral-networks.org/ftnWT",
                            "http://cygwin.cathedral-networks.org/hp",
                            "http://cygwin.cathedral-networks.org/ia",
                            "http://cygwin.cathedral-networks.org/ih",
                            "http://cygwin.cathedral-networks.org/in",
                            "http://cygwin.cathedral-networks.org/j/",
                            "http://cygwin.cathedral-networks.org/jU",
                            "http://cygwin.cathedral-networks.org/jX",
                            "http://cygwin.cathedral-networks.org/kf",
                            "http://cygwin.cathedral-networks.org/lisboa.pth.de/mirror/cygwin/",
                            "http://cygwin.cathedral-networks.org/mRX",
                            "http://cygwin.cathedral-networks.org/ma",
                            "http://cygwin.cathedral-networks.org/mi",
                            "http://cygwin.cathedral-networks.org/nCh",
                            "http://cygwin.cathedral-networks.org/o",
                            "http://cygwin.cathedral-networks.org/oniC",
                            "http://cygwin.cathedral-networks.org/p",
                            "http://cygwin.cathedral-networks.org/p.%j",
                            "http://cygwin.cathedral-networks.org/reLg/",
                            "http://cygwin.cathedral-networks.org/s:",
                            "http://cygwin.cathedral-networks.org/ss",
                            "http://cygwin.cathedral-networks.org/st",
                            "http://cygwin.cathedral-networks.org/t",
                            "http://cygwin.cathedral-networks.org/t-",
                            "http://cygwin.cathedral-networks.org/ti",
                            "http://cygwin.cathedral-networks.org/tp",
                            "http://cygwin.cathedral-networks.org/tpdXb",
                            "http://cygwin.cathedral-networks.org/tt",
                            "http://cygwin.cathedral-networks.org/ur",
                            "http://cygwin.cathedral-networks.org/uy",
                            "http://cygwin.cathedral-networks.org/xk8AU",
                            "http://cygwin.cathedral-networks.org/y",
                            "http://cygwin.cathedral-networks.org/yaT",
                            "http://cygwin.cathedral-networks.org/ygj",
                            "http://cygwin.cathedral-networks.org6j",
                            "http://cygwin.cathedral-networks.org://",
                            "http://cygwin.cathedral-networks.org://2g",
                            "http://cygwin.cathedral-networks.orgAU;",
                            "http://cygwin.cathedral-networks.orgPR%",
                            "http://cygwin.cathedral-networks.orgTl(",
                            "http://cygwin.cathedral-networks.org_f#",
                            "http://cygwin.cathedral-networks.orgag",
                            "http://cygwin.cathedral-networks.orgal-",
                            "http://cygwin.cathedral-networks.orgboc",
                            "http://cygwin.cathedral-networks.orgd.o6",
                            "http://cygwin.cathedral-networks.orgdos",
                            "http://cygwin.cathedral-networks.orgdxQ",
                            "http://cygwin.cathedral-networks.orgd~",
                            "http://cygwin.cathedral-networks.orge",
                            "http://cygwin.cathedral-networks.orge1U",
                            "http://cygwin.cathedral-networks.orgebs",
                            "http://cygwin.cathedral-networks.orgeti",
                            "http://cygwin.cathedral-networks.orgft",
                            "http://cygwin.cathedral-networks.orggwi;f",
                            "http://cygwin.cathedral-networks.orgl-",
                            "http://cygwin.cathedral-networks.orgmT",
                            "http://cygwin.cathedral-networks.orgn/",
                            "http://cygwin.cathedral-networks.orgn/Oj7",
                            "http://cygwin.cathedral-networks.orgomLh",
                            "http://cygwin.cathedral-networks.orgps",
                            "http://cygwin.cathedral-networks.orgr-h",
                            "http://cygwin.cathedral-networks.orgr.c",
                            "http://cygwin.cathedral-networks.orgror",
                            "http://cygwin.cathedral-networks.orgt",
                            "http://cygwin.cathedral-networks.orgtp",
                            "http://cygwin.cathedral-networks.orgtp.",
                            "http://cygwin.cathedral-networks.orgw",
                            "http://cygwin.cathedral-networks.orgwin",
                            "http://cygwin.mbwarez.dk",
                            "http://cygwin.mbwarez.dk.ac.jpin/~d",
                            "http://cygwin.mbwarez.dk.aun/om/",
                            "http://cygwin.mbwarez.dk.de",
                            "http://cygwin.mbwarez.dk.de/cygwin/",
                            "http://cygwin.mbwarez.dk.de/cygwin/n/",
                            "http://cygwin.mbwarez.dk.de/cygwin/nq",
                            "http://cygwin.mbwarez.dk.dk/ygwin/omtZ",
                            "http://cygwin.mbwarez.dk.fau.den.dem$W",
                            "http://cygwin.mbwarez.dk.net",
                            "http://cygwin.mbwarez.dk.net.de/cygw",
                            "http://cygwin.mbwarez.dk.orgmin/n/",
                            "http://cygwin.mbwarez.dk.orgygwin/8k",
                            "http://cygwin.mbwarez.dk.tech//in/",
                            "http://cygwin.mbwarez.dk/",
                            "http://cygwin.mbwarez.dk/$",
                            "http://cygwin.mbwarez.dk/(u$",
                            "http://cygwin.mbwarez.dk/.",
                            "http://cygwin.mbwarez.dk/.cawin/in/gk",
                            "http://cygwin.mbwarez.dk/.cn//win/",
                            "http://cygwin.mbwarez.dk/.cn/cygwin/2QQ",
                            "http://cygwin.mbwarez.dk/.com",
                            "http://cygwin.mbwarez.dk/.de/pub/cygwi",
                            "http://cygwin.mbwarez.dk/.edu.cn",
                            "http://cygwin.mbwarez.dk/.edu.cnr",
                            "http://cygwin.mbwarez.dk/.edu.cntp://l",
                            "http://cygwin.mbwarez.dk/.lagoon.nc",
                            "http://cygwin.mbwarez.dk/.netin/",
                            "http://cygwin.mbwarez.dk/.org/pub/cyQi",
                            "http://cygwin.mbwarez.dk//",
                            "http://cygwin.mbwarez.dk///in//",
                            "http://cygwin.mbwarez.dk//0",
                            "http://cygwin.mbwarez.dk//cygwin/",
                            "http://cygwin.mbwarez.dk//cygwin//",
                            "http://cygwin.mbwarez.dk//cygwin//;k",
                            "http://cygwin.mbwarez.dk//cygwin//Kon",
                            "http://cygwin.mbwarez.dk//cygwin/an",
                            "http://cygwin.mbwarez.dk//cygwin/etrceware.mirror.gar",
                            "http://cygwin.mbwarez.dk//cygwin/tvD",
                            "http://cygwin.mbwarez.dk//cygwin32/",
                            "http://cygwin.mbwarez.dk//cygwin32/;",
                            "http://cygwin.mbwarez.dk//in/",
                            "http://cygwin.mbwarez.dk//in/S",
                            "http://cygwin.mbwarez.dk//in/n/ftYR",
                            "http://cygwin.mbwarez.dk//n/in//",
                            "http://cygwin.mbwarez.dk//n/n/://",
                            "http://cygwin.mbwarez.dk//n/or.dat",
                            "http://cygwin.mbwarez.dk//pub/cygwin/&Dz",
                            "http://cygwin.mbwarez.dk//pub/cygwin/Er",
                            "http://cygwin.mbwarez.dk//pub/cygwingS",
                            "http://cygwin.mbwarez.dk//q",
                            "http://cygwin.mbwarez.dk//so.net/",
                            "http://cygwin.mbwarez.dk//win/",
                            "http://cygwin.mbwarez.dk//win/2/SL",
                            "http://cygwin.mbwarez.dk/0",
                            "http://cygwin.mbwarez.dk/1",
                            "http://cygwin.mbwarez.dk/3.compj",
                            "http://cygwin.mbwarez.dk/5",
                            "http://cygwin.mbwarez.dk/9E",
                            "http://cygwin.mbwarez.dk/;cygwin.mbwarez.dk;Europe;Denmark;noshow",
                            "http://cygwin.mbwarez.dk/;k",
                            "http://cygwin.mbwarez.dk/Asiayq",
                            "http://cygwin.mbwarez.dk/D",
                            "http://cygwin.mbwarez.dk/Q",
                            "http://cygwin.mbwarez.dk/Taiwan/dq",
                            "http://cygwin.mbwarez.dk/UD",
                            "http://cygwin.mbwarez.dk/achen.de",
                            "http://cygwin.mbwarez.dk/agata-u.ac.jp",
                            "http://cygwin.mbwarez.dk/are.mirror.gar",
                            "http://cygwin.mbwarez.dk/argasso.net/=x",
                            "http://cygwin.mbwarez.dk/b-",
                            "http://cygwin.mbwarez.dk/b/cygwin/com",
                            "http://cygwin.mbwarez.dk/b/cygwin/ogad/l",
                            "http://cygwin.mbwarez.dk/boa.pt/u",
                            "http://cygwin.mbwarez.dk/caks",
                            "http://cygwin.mbwarez.dk/cn/cygwin/",
                            "http://cygwin.mbwarez.dk/cn/cygwin/L_",
                            "http://cygwin.mbwarez.dk/com/cygwin/",
                            "http://cygwin.mbwarez.dk/cyg",
                            "http://cygwin.mbwarez.dk/cygwin/",
                            "http://cygwin.mbwarez.dk/cygwin/-D",
                            "http://cygwin.mbwarez.dk/cygwin/.Q",
                            "http://cygwin.mbwarez.dk/cygwin//",
                            "http://cygwin.mbwarez.dk/cygwin/2/",
                            "http://cygwin.mbwarez.dk/cygwin/SY",
                            "http://cygwin.mbwarez.dk/cygwin/d_",
                            "http://cygwin.mbwarez.dk/cygwin/eA",
                            "http://cygwin.mbwarez.dk/cygwin/gwin/gm",
                            "http://cygwin.mbwarez.dk/cygwin/n/",
                            "http://cygwin.mbwarez.dk/cygwin/n//wd",
                            "http://cygwin.mbwarez.dk/cygwin/n/t_L",
                            "http://cygwin.mbwarez.dk/cygwin/s",
                            "http://cygwin.mbwarez.dk/cygwin/ttp",
                            "http://cygwin.mbwarez.dk/cygwin32/",
                            "http://cygwin.mbwarez.dk/d.comin/f/",
                            "http://cygwin.mbwarez.dk/d.coms.org//",
                            "http://cygwin.mbwarez.dk/deso.net//Vj(",
                            "http://cygwin.mbwarez.dk/domain.de/cygw",
                            "http://cygwin.mbwarez.dk/e",
                            "http://cygwin.mbwarez.dk/e/cygwin/",
                            "http://cygwin.mbwarez.dk/e/cygwin//",
                            "http://cygwin.mbwarez.dk/e/cygwin/tnlHf",
                            "http://cygwin.mbwarez.dk/easyname.at",
                            "http://cygwin.mbwarez.dk/ebsd.orgn.nc/yZ",
                            "http://cygwin.mbwarez.dk/ecygwin//",
                            "http://cygwin.mbwarez.dk/edu.cn",
                            "http://cygwin.mbwarez.dk/einrausch.de",
                            "http://cygwin.mbwarez.dk/et/cygwin//esW",
                            "http://cygwin.mbwarez.dk/et/cygwin//wL",
                            "http://cygwin.mbwarez.dk/et/cygwin/or/cygwin/n///GY",
                            "http://cygwin.mbwarez.dk/et/cygwin/z.d",
                            "http://cygwin.mbwarez.dk/etom/m",
                            "http://cygwin.mbwarez.dk/etworks.org/Y",
                            "http://cygwin.mbwarez.dk/etworks.org0i",
                            "http://cygwin.mbwarez.dk/g/cygwin/",
                            "http://cygwin.mbwarez.dk/g/cygwin//",
                            "http://cygwin.mbwarez.dk/g/cygwin//Yt",
                            "http://cygwin.mbwarez.dk/gata-u",
                            "http://cygwin.mbwarez.dk/gie.fr",
                            "http://cygwin.mbwarez.dk/goon.nc/",
                            "http://cygwin.mbwarez.dk/gwin/in/",
                            "http://cygwin.mbwarez.dk/gwin/m/",
                            "http://cygwin.mbwarez.dk/gwin/n/",
                            "http://cygwin.mbwarez.dk/gwin/win/",
                            "http://cygwin.mbwarez.dk/h.de",
                            "http://cygwin.mbwarez.dk/ia$",
                            "http://cygwin.mbwarez.dk/in/",
                            "http://cygwin.mbwarez.dk/in/.freebs",
                            "http://cygwin.mbwarez.dk/in/.hutLZ",
                            "http://cygwin.mbwarez.dk/in//",
                            "http://cygwin.mbwarez.dk/in//n/s",
                            "http://cygwin.mbwarez.dk/in/=A",
                            "http://cygwin.mbwarez.dk/in/enter.",
                            "http://cygwin.mbwarez.dk/in/gwin/",
                            "http://cygwin.mbwarez.dk/in/in/",
                            "http://cygwin.mbwarez.dk/in/in/GY",
                            "http://cygwin.mbwarez.dk/in/n//",
                            "http://cygwin.mbwarez.dk/in/n///miTW4",
                            "http://cygwin.mbwarez.dk/in/n/h_P",
                            "http://cygwin.mbwarez.dk/in/ong",
                            "http://cygwin.mbwarez.dk/in/rror.chi",
                            "http://cygwin.mbwarez.dk/in/ttp://siC",
                            "http://cygwin.mbwarez.dk/in/ygwin///wqCX",
                            "http://cygwin.mbwarez.dk/ina",
                            "http://cygwin.mbwarez.dk/l/pub/cygwi",
                            "http://cygwin.mbwarez.dk/mirror.dogado..C",
                            "http://cygwin.mbwarez.dk/n.uib.no//",
                            "http://cygwin.mbwarez.dk/n/",
                            "http://cygwin.mbwarez.dk/n/cygwin/a/",
                            "http://cygwin.mbwarez.dk/n/gwin/",
                            "http://cygwin.mbwarez.dk/n/win/kY0",
                            "http://cygwin.mbwarez.dk/n/win32/",
                            "http://cygwin.mbwarez.dk/no/",
                            "http://cygwin.mbwarez.dk/nu",
                            "http://cygwin.mbwarez.dk/o",
                            "http://cygwin.mbwarez.dk/om/cygwin/",
                            "http://cygwin.mbwarez.dk/omin/gwin/",
                            "http://cygwin.mbwarez.dk/orks.netn//kpAm",
                            "http://cygwin.mbwarez.dk/p",
                            "http://cygwin.mbwarez.dk/pub/software/c",
                            "http://cygwin.mbwarez.dk/rg/cygwin/",
                            "http://cygwin.mbwarez.dk/rgasso.net/",
                            "http://cygwin.mbwarez.dk/rgasso.net/e2h",
                            "http://cygwin.mbwarez.dk/rgasso.net/fZj",
                            "http://cygwin.mbwarez.dk/rks.orgboc",
                            "http://cygwin.mbwarez.dk/ror/cygwin//"
                        ],
                        "severity": "IMPACT_SEVERITY_INFO",
                        "id": "238"
                    },
                    {
                        "description": "Uses secure TLS version for HTTPS connections",
                        "match_data": [
                            "8.43.85.97:443 -> 192.168.2.9:49738 version: TLS 1.2"
                        ],
                        "severity": "IMPACT_SEVERITY_INFO",
                        "id": "7058"
                    },
                    {
                        "severity": "IMPACT_SEVERITY_INFO",
                        "match_data": [
                            "HTTP traffic on port 49712 -> 443",
                            "HTTP traffic on port 443 -> 49712"
                        ],
                        "id": "625",
                        "description": "Uses HTTPS"
                    },
                    {
                        "severity": "IMPACT_SEVERITY_INFO",
                        "refs": [
                            {
                                "ref": "#memory_dumps",
                                "value": "executable.exe, 00000000.00000002.4517172722.0000000000D79000.00000004.00000020.00020000.00000000.sdmp, executable.exe, 00000000.00000002.4516435918.0000000000D18000.00000004.00000020.00020000.00000000.sdmp"
                            }
                        ],
                        "match_data": [
                            "Hyper-V RAW"
                        ],
                        "id": "263",
                        "description": "May try to detect the virtual machine to hinder analysis (VM artifact strings found in memory)"
                    },
                    {
                        "severity": "IMPACT_SEVERITY_INFO",
                        "match_data": [
                            "ftp://sourceware.org/ftp://sources.redhat.com/ftp://gcc.gnu.org/",
                            "http://apps.identrust.com/roots/dstrootcax3.p7c0",
                            "http://cps.letsencrypt.org0",
                            "http://cps.root-x1.letsencrypt.org0",
                            "http://crl.identrust.com/DSTROOTCAX3CRL.crl0",
                            "http://cygwin.cathedral-networks.org/;cygwin.cathedral-networks.org;Europe;Norway;noshow",
                            "http://cygwin.mbwarez.dk/;cygwin.mbwarez.dk;Europe;Denmark;noshow",
                            "http://cygwin.mirror.constant.com/;cygwin.mirror.constant.com;North",
                            "http://cygwin.mirror.globo.tech/;cygwin.mirror.globo.tech;North",
                            "http://cygwin.mirror.rafal.ca/;cygwin.mirror.rafal.ca;North",
                            "http://cygwin.mirror.uk.sargasso.net/;cygwin.mirror.uk.sargasso.net;Europe;UK;noshow",
                            "http://cygwin.mirrors.hoobly.com/;cygwin.mirrors.hoobly.com;North",
                            "http://cygwin.osuosl.org/;cygwin.osuosl.org;North",
                            "http://cygwin.uib.no/;cygwin.uib.no;Europe;Norway;noshow",
                            "http://cygwin.viem-it.no/;cygwin.viem-it.no;Europe;Norway;noshow",
                            "http://download.nus.edu.sg/mirror/cygwin/;download.nus.edu.sg;Asia;Singapore;noshow",
                            "http://ftp-stud.hs-esslingen.de/pub/Mirrors/sources.redhat.com/cygwin/;ftp-stud.hs-esslingen.de;Euro",
                            "http://ftp.acc.umu.se/mirror/cygwin/;ftp.acc.umu.se;Europe;Sweden;noshow",
                            "http://ftp.byfly.by/pub/cygwin/;ftp.byfly.by;Europe;Belarus;noshow",
                            "http://ftp.eq.uc.pt/software/pc/prog/cygwin/;ftp.eq.uc.pt;Europe;Portugal;noshow",
                            "http://ftp.fau.de/cygwin/;ftp.fau.de;Europe;Germany;noshow",
                            "http://ftp.fsn.hu/pub/cygwin/;ftp.fsn.hu;Europe;Hungary;noshow",
                            "http://ftp.iij.ad.jp/pub/cygwin/;ftp.iij.ad.jp;Asia;Japan;noshow",
                            "http://ftp.inf.tu-dresden.de/software/windows/cygwin32/;ftp.inf.tu-dresden.de;Europe;Germany;noshow",
                            "http://ftp.is.co.za/mirrors/cygwin/;ftp.is.co.za;Africa;South",
                            "http://ftp.jaist.ac.jp/pub/cygwin/;ftp.jaist.ac.jp;Asia;Japan;noshow",
                            "http://ftp.lip6.fr/pub/cygwin/;ftp.lip6.fr;Europe;France;noshow",
                            "http://ftp.ntu.edu.tw/pub/cygwin/;ftp.ntu.edu.tw;Asia;Taiwan;noshow",
                            "http://ftp.ntua.gr/pub/pc/cygwin/;ftp.ntua.gr;Europe;Greece",
                            "http://ftp.rnl.tecnico.ulisboa.pt/pub/cygwin/;ftp.rnl.tecnico.ulisboa.pt;Europe;Portugal;noshow",
                            "http://ftp.snt.utwente.nl/pub/software/cygwin/;ftp.snt.utwente.nl;Europe;Netherlands;noshow",
                            "http://ftp.twaren.net/Unix/sourceware.org/cygwin/;ftp.twaren.net;Asia;Taiwan",
                            "http://ftp.yz.yamagata-u.ac.jp/pub/cygwin/;ftp.yz.yamagata-u.ac.jp;Asia;Japan;noshow",
                            "http://linorg.usp.br/cygwin/;linorg.usp.br;Latin",
                            "http://linux.rz.ruhr-uni-bochum.de/download/cygwin/;linux.rz.ruhr-uni-bochum.de;Europe;Germany;nosho",
                            "http://mirror-hk.koddos.net/cygwin/;mirror-hk.koddos.net;Asia;Hong",
                            "http://mirror.aarnet.edu.au/pub/sourceware/cygwin/;mirror.aarnet.edu.au;Australasia;Australia;noshow",
                            "http://mirror.checkdomain.de/cygwin/;mirror.checkdomain.de;Europe;Germany;noshow",
                            "http://mirror.clarkson.edu/cygwin/;mirror.clarkson.edu;North",
                            "http://mirror.cs.vt.edu/pub/cygwin/cygwin/;mirror.cs.vt.edu;North",
                            "http://mirror.csclub.uwaterloo.ca/cygwin/;mirror.csclub.uwaterloo.ca;North",
                            "http://mirror.datacenter.by/pub/mirrors/cygwin/;mirror.datacenter.by;Europe;Belarus;noshow",
                            "http://mirror.easyname.at/cygwin/;mirror.easyname.at;Europe;Austria;noshow",
                            "http://mirror.internode.on.net/pub/cygwin/;mirror.internode.on.net;Australasia;Australia",
                            "http://mirror.isoc.org.il/pub/cygwin/;mirror.isoc.org.il;Asia;Israel;noshow",
                            "http://mirror.koddos.net/cygwin/;mirror.koddos.net;Europe;Netherlands;noshow",
                            "http://mirror.lagoon.nc/cygwin/;mirror.lagoon.nc;Australasia;New",
                            "http://mirror.rise.ph/cygwin/cygwin/;mirror.rise.ph;Asia;Philippines",
                            "http://mirror.steadfast.net/cygwin/;mirror.steadfast.net;North",
                            "http://mirror.team-cymru.com/cygwin/;mirror.team-cymru.com;North",
                            "http://mirror.terrahost.no/cygwin/;mirror.terrahost.no;Europe;Norway;noshow",
                            "http://mirrors.163.com/cygwin/;mirrors.163.com;Asia;China;noshow",
                            "http://mirrors.dotsrc.org/cygwin/;mirrors.dotsrc.org;Europe;Denmark;noshow",
                            "http://mirrors.kernel.org/sourceware/cygwin/;mirrors.kernel.org;North",
                            "http://mirrors.netix.net/cygwin/;mirrors.netix.net;Europe;Bulgaria;noshow",
                            "http://mirrors.neusoft.edu.cn/cygwin/;mirrors.neusoft.edu.cn;Asia;China;noshow",
                            "http://mirrors.sonic.net/cygwin/;mirrors.sonic.net;North",
                            "http://mirrors.syringanetworks.net/cygwin/;mirrors.syringanetworks.net;North",
                            "http://mirrors.ustc.edu.cn/cygwin/;mirrors.ustc.edu.cn;Asia;China;noshow",
                            "http://mirrors.xmission.com/cygwin/;mirrors.xmission.com;North",
                            "http://muug.ca/mirror/cygwin/;muug.ca;North",
                            "http://r3.i.lencr.org",
                            "http://r3.i.lencr.org/0M",
                            "http://r3.o.lencr.org0",
                            "http://sourceware.mirror.garr.it/cygwin/;sourceware.mirror.garr.it;Europe;Italy;noshow",
                            "http://ucmirror.canterbury.ac.nz/cygwin/;ucmirror.canterbury.ac.nz;Australasia;New",
                            "http://www.gtlib.gatech.edu/pub/cygwin/;www.gtlib.gatech.edu;North",
                            "http://www.gutscheinrausch.de/mirror/cygwin/;www.gutscheinrausch.de;Europe;Germany;noshow",
                            "http://www.mirrorservice.org/sites/sourceware.org/pub/cygwin/;www.mirrorservice.org;Europe;UK;noshow",
                            "http://x1.c.lencr.org/0",
                            "http://x1.i.lencr.org/0",
                            "https://cygwin.cathedral-networks.org/;cygwin.cathedral-networks.org;Europe;Norway",
                            "https://cygwin.com",
                            "https://cygwin.com/W",
                            "https://cygwin.com/mirrors.lst",
                            "https://cygwin.com/mirrors.lst4",
                            "https://cygwin.com/mirrors.lst8",
                            "https://cygwin.com/mirrors.lstDefaulting",
                            "https://cygwin.com/mirrors.lstce",
                            "https://cygwin.com/mirrors.lstdll",
                            "https://cygwin.com/mirrors.lstlF",
                            "https://cygwin.com/mirrors.lstll",
                            "https://cygwin.com/mirrors.lstystem32",
                            "https://cygwin.com/setup-%s.exe",
                            "https://cygwin.com/setup-%s.exeThe",
                            "https://cygwin.com/setup-%s.exe_self-destructlibsolv-self-destruct-pkg()basic_string::append-srczstx",
                            "https://cygwin.com/t",
                            "https://cygwin.com9",
                            "https://cygwin.comzstxzbz2inibasic_string::_M_construct",
                            "https://cygwin.itefix.net/;cygwin.itefix.net;Europe;Germany",
                            "https://cygwin.mbwarez.dk/;cygwin.mbwarez.dk;Europe;Denmark",
                            "https://cygwin.mirror.constant.com/;cygwin.mirror.constant.com;North",
                            "https://cygwin.mirror.globo.tech/;cygwin.mirror.globo.tech;North",
                            "https://cygwin.mirror.uk.sargasso.net/;cygwin.mirror.uk.sargasso.net;Europe;UK",
                            "https://cygwin.mirrors.hoobly.com/;cygwin.mirrors.hoobly.com;North",
                            "https://cygwin.osuosl.org/;cygwin.osuosl.org;North",
                            "https://cygwin.uib.no/;cygwin.uib.no;Europe;Norway",
                            "https://cygwin.viem-it.no/;cygwin.viem-it.no;Europe;Norway",
                            "https://download.nus.edu.sg/mirror/cygwin/;download.nus.edu.sg;Asia;Singapore",
                            "https://ftp-stud.hs-esslingen.de/pub/Mirrors/sources.redhat.com/cygwin/;ftp-stud.hs-esslingen.de;Eur",
                            "https://ftp.acc.umu.se/mirror/cygwin/;ftp.acc.umu.se;Europe;Sweden",
                            "https://ftp.byfly.by/pub/cygwin/;ftp.byfly.by;Europe;Belarus",
                            "https://ftp.eq.uc.pt/software/pc/prog/cygwin/;ftp.eq.uc.pt;Europe;Portugal",
                            "https://ftp.fau.de/cygwin/;ftp.fau.de;Europe;Germany",
                            "https://ftp.fsn.hu/pub/cygwin/;ftp.fsn.hu;Europe;Hungary",
                            "https://ftp.funet.fi/pub/mirrors/sourceware.org/pub/cygwin/;ftp.funet.fi;Europe;Finland",
                            "https://ftp.halifax.rwth-aachen.de/cygwin/;ftp.halifax.rwth-aachen.de;Europe;Germany",
                            "https://ftp.iij.ad.jp/pub/cygwin/;ftp.iij.ad.jp;Asia;Japan",
                            "https://ftp.inf.tu-dresden.de/software/windows/cygwin32/;ftp.inf.tu-dresden.de;Europe;Germany",
                            "https://ftp.jaist.ac.jp/pub/cygwin/;ftp.jaist.ac.jp;Asia;Japan",
                            "https://ftp.kaist.ac.kr/cygwin/;ftp.kaist.ac.kr;Asia;Korea",
                            "https://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/;ftp.kr.freebsd.org;Asia;Korea",
                            "https://ftp.lip6.fr/pub/cygwin/;ftp.lip6.fr;Europe;France",
                            "https://ftp.ntu.edu.tw/pub/cygwin/;ftp.ntu.edu.tw;Asia;Taiwan",
                            "https://ftp.rnl.tecnico.ulisboa.pt/pub/cygwin/;ftp.rnl.tecnico.ulisboa.pt;Europe;Portugal",
                            "https://ftp.snt.utwente.nl/pub/software/cygwin/;ftp.snt.utwente.nl;Europe;Netherlands",
                            "https://ftp.yz.yamagata-u.ac.jp/pub/cygwin/;ftp.yz.yamagata-u.ac.jp;Asia;Japan",
                            "https://gnu.org/licenses/",
                            "https://gnu.org/licenses/gpl.html",
                            "https://linorg.usp.br/cygwin/;linorg.usp.br;Latin",
                            "https://linux.rz.ruhr-uni-bochum.de/download/cygwin/;linux.rz.ruhr-uni-bochum.de;Europe;Germany",
                            "https://mirror-hk.koddos.net/cygwin/;mirror-hk.koddos.net;Asia;Hong",
                            "https://mirror.aarnet.edu.au/pub/sourceware/cygwin/;mirror.aarnet.edu.au;Australasia;Australia",
                            "https://mirror.checkdomain.de/cygwin/;mirror.checkdomain.de;Europe;Germany",
                            "https://mirror.clarkson.edu/cygwin/;mirror.clarkson.edu;North",
                            "https://mirror.clientvps.com/cygwin/;mirror.clientvps.com;Europe;Germany",
                            "https://mirror.csclub.uwaterloo.ca/cygwin/;mirror.csclub.uwaterloo.ca;North",
                            "https://mirror.datacenter.by/pub/mirrors/cygwin/;mirror.datacenter.by;Europe;Belarus",
                            "https://mirror.dogado.de/cygwin/;mirror.dogado.de;Europe;Germany",
                            "https://mirror.easyname.at/cygwin/;mirror.easyname.at;Europe;Austria",
                            "https://mirror.isoc.org.il/pub/cygwin/;mirror.isoc.org.il;Asia;Israel",
                            "https://mirror.koddos.net/cygwin/;mirror.koddos.net;Europe;Netherlands",
                            "https://mirror.lagoon.nc/cygwin/;mirror.lagoon.nc;Australasia;New",
                            "https://mirror.mangohost.net/cygwin/;mirror.mangohost.net;Europe;Moldova",
                            "https://mirror.steadfast.net/cygwin/;mirror.steadfast.net;North",
                            "https://mirror.terrahost.no/cygwin/;mirror.terrahost.no;Europe;Norway",
                            "https://mirrors.163.com/cygwin/;mirrors.163.com;Asia;China",
                            "https://mirrors.163.comhttps://mirrors.aliyun.comhttps://mirror.clientvps.comhttps://cygwin.mirror.c",
                            "https://mirrors.aliyun.com/cygwin/;mirrors.aliyun.com;Asia;China",
                            "https://mirrors.aliyun.comhttps://mirror.clientvps.comhttps://cygwin.mirror.constant.comhttps://poli",
                            "https://mirrors.dotsrc.org/cygwin/;mirrors.dotsrc.org;Europe;Denmark",
                            "https://mirrors.filigrane-technologie.fr/cygwin/;mirrors.filigrane-technologie.fr;Europe;France",
                            "https://mirrors.huaweicloud.com/cygwin/;mirrors.huaweicloud.com;Asia;China",
                            "https://mirrors.kernel.org/sourceware/cygwin/;mirrors.kernel.org;North",
                            "https://mirrors.netix.net/cygwin/;mirrors.netix.net;Europe;Bulgaria",
                            "https://mirrors.neusoft.edu.cn/cygwin/;mirror7",
                            "https://mirrors.neusoft.edu.cn/cygwin/;mirrors.neusoft.edu.cn;Asia;China",
                            "https://mirrors.rit.edu/cygwin/;mirrors.rit.edu;North",
                            "https://mirrors.sjtug.sjtu.edu.cn/cygwin/;mirrors.sjtug.sjtu.edu.cn;Asia;China",
                            "https://mirrors.sonic.net/cygwin/;mirrors.sonic.net;North",
                            "https://mirrors.tencent.com/cygwin/;mirrors.tencent.com;Asia;China",
                            "https://mirrors.ustc.edu.cn/cygwin/;mirrors.ustc.edu.cn;Asia;China",
                            "https://mirrors.xmission.com/cygwin/;mirrors.xmission.com;North",
                            "https://muug.ca/mirror/cygwin/;muug.ca;North",
                            "https://polish-mirror.evolution-host.com/cygwin/;polish-mirror.evolution-host.com;Europe;Poland",
                            "https://sourceware.mirror.garr.it/cygwin/;sourceware.mirror.garr.it;Europe;Italy",
                            "https://sunsite.icm.edu.pl/pub/cygnus/cygwin/;sunsite.icm.edu.pl;Europe;Poland",
                            "https://www.gutscheinrausch.de/mirror/cygwin/;www.gutscheinrausch.de;Europe;Germany",
                            "https://www.mirrorservice.org",
                            "https://www.mirrorservice.org/sites/sourceware.org/pub/cygwin/;www.mirrorservice.org;Europe;UK"
                        ],
                        "id": "238",
                        "description": "URLs found in memory or binary data"
                    },
                    {
                        "severity": "IMPACT_SEVERITY_INFO",
                        "match_data": [
                            "8.43.85.97:443 -> 192.168.2.11:49712 version: TLS 1.2"
                        ],
                        "id": "7058",
                        "description": "Uses secure TLS version for HTTPS connections"
                    },
                    {
                        "id": "625",
                        "match_data": [
                            "HTTP traffic on port 49713 -> 443",
                            "HTTP traffic on port 443 -> 49713"
                        ],
                        "description": "Uses HTTPS",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "263",
                        "refs": [
                            {
                                "ref": "#memory_dumps",
                                "value": "software.exe, 00000000.00000002.4601502652.0000000000C2F000.00000004.00000020.00020000.00000000.sdmp"
                            },
                            {
                                "ref": "#memory_dumps",
                                "value": "software.exe, 00000000.00000002.4601906974.0000000000C85000.00000004.00000020.00020000.00000000.sdmp"
                            }
                        ],
                        "match_data": [
                            "Hyper-V RAW0",
                            "Hyper-V RAW"
                        ],
                        "description": "May try to detect the virtual machine to hinder analysis (VM artifact strings found in memory)",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "238",
                        "match_data": [
                            "ftp://cygwin.mirror.rafal.cars",
                            "ftp://ftp-stud.hs-esslingen.dem",
                            "ftp://ftp.2g?",
                            "ftp://ftp.byfly.by/pub/cyg",
                            "ftp://ftp.byfly.by/pub/cyg%",
                            "ftp://ftp.byfly.by/pub/cygwin/",
                            "ftp://ftp.byfly.by/pub/cygwin/http://dOf",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/p",
                            "ftp://ftp.fs",
                            "ftp://ftp.fsn.hu/pub/cygwin/p",
                            "ftp://ftp.fsn.hu/pub/cygwin/tp",
                            "ftp://ftp.fsn.hut",
                            "ftp://ftp.ha",
                            "ftp://ftp.haA",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/http://mOg",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/http://m_~",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/http://w",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/https://",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/n",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/or",
                            "ftp://ftp.inf.tu-dresden.de",
                            "ftp://ftp.inf.tu-dresden.de.jpor",
                            "ftp://ftp.inf.tu-dresden.degwin/",
                            "ftp://ftp.inf.tu-dresden.degwin/http:/",
                            "ftp://ftp.kaist.ac.kr/cygwin/",
                            "ftp://ftp.kaist.ac.kr/cygwin/win",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/http://m",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/https://",
                            "ftp://ftp.kr.freebsd.orgftp",
                            "ftp://ftp.l",
                            "ftp://ftp.lip6.fr/pub/cygwin/",
                            "ftp://ftp.lip6.fr/pub/cygwin/or",
                            "ftp://ftp.mirrorservice.orgin/r",
                            "ftp://ftp.muug.ca/mirror/cygwin//https://",
                            "ftp://ftp.muug.ca/mirror/cygwin/e",
                            "ftp://ftp.n_db",
                            "ftp://ftp.ntua.gr/pub/pc/cygwin/https://",
                            "ftp://ftp.ntua.gr/pub/pc/cygwin/r",
                            "ftp://ftp.snt.utwente.nl",
                            "ftp://ftp.snt.utwente.nl/pub/software/cygwin/https://",
                            "ftp://ftp.yz.yamagata-u.ac.jp",
                            "ftp://ftp.yz.yamagata-u.ac.jp/pub/cygwin/",
                            "ftp://ftp.yz.yamagata-u.ac.jprs",
                            "ftp://linux.rz.ruhr-uni-bochum.de",
                            "ftp://linux.rz.ruhr-uni-bochum.de/cygwin/ustc",
                            "ftp://linux.rz.ruhr-uni-bochum.de/http",
                            "ftp://mirror.checkdomain.de",
                            "ftp://mirror.checkdomain.de/cygwi(",
                            "ftp://mirror.checkdomain.de/cygwin/",
                            "ftp://mirror.checkdomain.de/cygwin/cygwin",
                            "ftp://mirror.checkdomain.de/cygwin/p",
                            "ftp://mirror.checkdomain.detp",
                            "ftp://mirror.checkdomain.deunsite",
                            "ftp://mirror.cs.vt.edu/pub/cygwin/cygwin/",
                            "ftp://mirror.cs.vt.edu/pub/cygwin/cygwin/p",
                            "ftp://mirror.csclub.uwaterloo.ca/cygwin/oc",
                            "ftp://mirror.datacenter.byirror",
                            "ftp://mirror.easyname.attp",
                            "ftp://mirror.easyname.atygwin/http://f",
                            "ftp://mirror.internode.on.net/pub/cygwin/",
                            "ftp://mirror.internode.on.net/pub/cygwin/gwin/https://",
                            "ftp://mirror.internode.on.nethttp://dOf",
                            "ftp://mirror.internode.on.nethttp://ftp",
                            "ftp://mirrors.dotsrc.org/mirrors/cygwin/",
                            "ftp://mirrors.dotsrc.org/mirrors/cygwin/ygwin",
                            "ftp://mirrors.netix.net/cygwin/http://fG",
                            "ftp://mirrors.netix.net/cygwin/http://w",
                            "ftp://sourceware.org/ftp://sources.redhat.com/ftp://gcc.gnu.org/",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/http://f",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/http://m",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/http://w",
                            "ftp://sunsite.icm.edu.plg/cygwin/",
                            "ftp://sunsite.icm.edu.plix",
                            "ftp://sunsite.icm.edu.plygwin",
                            "http://apps.identrust.com/roots/dstrootcax3.p7c0",
                            "http://cps.letsencrypt.org0",
                            "http://cps.root-x1.letsencrypt.org#",
                            "http://cps.root-x1.letsencrypt.org0",
                            "http://crl.identrust.com/DSTROOTCAX3CRL.crl0",
                            "http://cygwin.cathedral-",
                            "http://cygwin.cathedral-networks.org",
                            "http://cygwin.cathedral-networks.org.fs",
                            "http://cygwin.cathedral-networks.org.ne",
                            "http://cygwin.cathedral-networks.org/",
                            "http://cygwin.cathedral-networks.org/$z",
                            "http://cygwin.cathedral-networks.org/&",
                            "http://cygwin.cathedral-networks.org/&f",
                            "http://cygwin.cathedral-networks.org/(",
                            "http://cygwin.cathedral-networks.org/.9c",
                            "http://cygwin.cathedral-networks.org/.f",
                            "http://cygwin.cathedral-networks.org/.mwi",
                            "http://cygwin.cathedral-networks.org/.o6g;",
                            "http://cygwin.cathedral-networks.org/.t",
                            "http://cygwin.cathedral-networks.org//",
                            "http://cygwin.cathedral-networks.org///",
                            "http://cygwin.cathedral-networks.org///7f",
                            "http://cygwin.cathedral-networks.org///tbF",
                            "http://cygwin.cathedral-networks.org//;",
                            "http://cygwin.cathedral-networks.org//E",
                            "http://cygwin.cathedral-networks.org//Feu",
                            "http://cygwin.cathedral-networks.org//G",
                            "http://cygwin.cathedral-networks.org//cU",
                            "http://cygwin.cathedral-networks.org//do",
                            "http://cygwin.cathedral-networks.org//ftp.is.co.za/mirrors/cygwin/et#f",
                            "http://cygwin.cathedral-networks.org//jJ",
                            "http://cygwin.cathedral-networks.org//m",
                            "http://cygwin.cathedral-networks.org//mFx",
                            "http://cygwin.cathedral-networks.org//y",
                            "http://cygwin.cathedral-networks.org/:",
                            "http://cygwin.cathedral-networks.org/;cygwin.cathedral-networks.org;Europe;Norway;noshow",
                            "http://cygwin.cathedral-networks.org/;e",
                            "http://cygwin.cathedral-networks.org/=",
                            "http://cygwin.cathedral-networks.org/=x",
                            "http://cygwin.cathedral-networks.org/?b",
                            "http://cygwin.cathedral-networks.org/He",
                            "http://cygwin.cathedral-networks.org/I",
                            "http://cygwin.cathedral-networks.org/J",
                            "http://cygwin.cathedral-networks.org/Jx",
                            "http://cygwin.cathedral-networks.org/Le",
                            "http://cygwin.cathedral-networks.org/N",
                            "http://cygwin.cathedral-networks.org/P",
                            "http://cygwin.cathedral-networks.org/Pek",
                            "http://cygwin.cathedral-networks.org/Re",
                            "http://cygwin.cathedral-networks.org/Rh",
                            "http://cygwin.cathedral-networks.org/U",
                            "http://cygwin.cathedral-networks.org/Vq",
                            "http://cygwin.cathedral-networks.org/W",
                            "http://cygwin.cathedral-networks.org/Y",
                            "http://cygwin.cathedral-networks.org/ac",
                            "http://cygwin.cathedral-networks.org/bdl",
                            "http://cygwin.cathedral-networks.org/c",
                            "http://cygwin.cathedral-networks.org/co",
                            "http://cygwin.cathedral-networks.org/cr",
                            "http://cygwin.cathedral-networks.org/cy",
                            "http://cygwin.cathedral-networks.org/cy$b",
                            "http://cygwin.cathedral-networks.org/dJ",
                            "http://cygwin.cathedral-networks.org/ed",
                            "http://cygwin.cathedral-networks.org/ed3",
                            "http://cygwin.cathedral-networks.org/ee",
                            "http://cygwin.cathedral-networks.org/f",
                            "http://cygwin.cathedral-networks.org/fgs",
                            "http://cygwin.cathedral-networks.org/ft",
                            "http://cygwin.cathedral-networks.org/ht",
                            "http://cygwin.cathedral-networks.org/i",
                            "http://cygwin.cathedral-networks.org/ia",
                            "http://cygwin.cathedral-networks.org/in",
                            "http://cygwin.cathedral-networks.org/inKb",
                            "http://cygwin.cathedral-networks.org/irrors/cygwin/n/",
                            "http://cygwin.cathedral-networks.org/it",
                            "http://cygwin.cathedral-networks.org/j",
                            "http://cygwin.cathedral-networks.org/ka",
                            "http://cygwin.cathedral-networks.org/ky",
                            "http://cygwin.cathedral-networks.org/l",
                            "http://cygwin.cathedral-networks.org/mi",
                            "http://cygwin.cathedral-networks.org/n/",
                            "http://cygwin.cathedral-networks.org/n5g",
                            "http://cygwin.cathedral-networks.org/ne",
                            "http://cygwin.cathedral-networks.org/niJg",
                            "http://cygwin.cathedral-networks.org/nl",
                            "http://cygwin.cathedral-networks.org/of",
                            "http://cygwin.cathedral-networks.org/olx",
                            "http://cygwin.cathedral-networks.org/oo",
                            "http://cygwin.cathedral-networks.org/osHy",
                            "http://cygwin.cathedral-networks.org/p",
                            "http://cygwin.cathedral-networks.org/ps",
                            "http://cygwin.cathedral-networks.org/r(c",
                            "http://cygwin.cathedral-networks.org/ra",
                            "http://cygwin.cathedral-networks.org/rahost",
                            "http://cygwin.cathedral-networks.org/rs",
                            "http://cygwin.cathedral-networks.org/s.",
                            "http://cygwin.cathedral-networks.org/s:",
                            "http://cygwin.cathedral-networks.org/stMy",
                            "http://cygwin.cathedral-networks.org/su",
                            "http://cygwin.cathedral-networks.org/teiy",
                            "http://cygwin.cathedral-networks.org/tp",
                            "http://cygwin.cathedral-networks.org/tpzb",
                            "http://cygwin.cathedral-networks.org/w",
                            "http://cygwin.cathedral-networks.org/xeS",
                            "http://cygwin.cathedral-networks.org/xzS",
                            "http://cygwin.cathedral-networks.org/yg",
                            "http://cygwin.cathedral-networks.org/~",
                            "http://cygwin.cathedral-networks.org8",
                            "http://cygwin.cathedral-networks.orgCe",
                            "http://cygwin.cathedral-networks.orgI",
                            "http://cygwin.cathedral-networks.orgJet",
                            "http://cygwin.cathedral-networks.orgM",
                            "http://cygwin.cathedral-networks.orgMi",
                            "http://cygwin.cathedral-networks.orgMz",
                            "http://cygwin.cathedral-networks.orgOeq",
                            "http://cygwin.cathedral-networks.orgW",
                            "http://cygwin.cathedral-networks.orgZ",
                            "http://cygwin.cathedral-networks.orgate",
                            "http://cygwin.cathedral-networks.orgbx",
                            "http://cygwin.cathedral-networks.orgcygxbR",
                            "http://cygwin.cathedral-networks.orgd",
                            "http://cygwin.cathedral-networks.orger.",
                            "http://cygwin.cathedral-networks.orgn",
                            "http://cygwin.cathedral-networks.orgn/",
                            "http://cygwin.cathedral-networks.orgn/o",
                            "http://cygwin.cathedral-networks.orgnetVy",
                            "http://cygwin.cathedral-networks.orgq",
                            "http://cygwin.cathedral-networks.orgr.c",
                            "http://cygwin.cathedral-networks.orgror",
                            "http://cygwin.cathedral-networks.orgstc",
                            "http://cygwin.cathedral-networks.orgt.",
                            "http://cygwin.cathedral-networks.orgte.",
                            "http://cygwin.cathedral-networks.orguts",
                            "http://cygwin.cathedral-networks.orgvfI",
                            "http://cygwin.cathedral-networks.orgx",
                            "http://cygwin.mbwarez.dk",
                            "http://cygwin.mbwarez.dk-bochum.de",
                            "http://cygwin.mbwarez.dk.byn/c.pteIx",
                            "http://cygwin.mbwarez.dk.de/cygwin/e",
                            "http://cygwin.mbwarez.dk.dein/",
                            "http://cygwin.mbwarez.dk.den/win//",
                            "http://cygwin.mbwarez.dk.deork-0",
                            "http://cygwin.mbwarez.dk.fsn.hufr",
                            "http://cygwin.mbwarez.dk.halifax.rwth-a",
                            "http://cygwin.mbwarez.dk.kaist.ac.krmPz",
                            "http://cygwin.mbwarez.dk.netom/cygwin",
                            "http://cygwin.mbwarez.dk.orgks.org",
                            "http://cygwin.mbwarez.dk.orgygwin/",
                            "http://cygwin.mbwarez.dk/",
                            "http://cygwin.mbwarez.dk/#",
                            "http://cygwin.mbwarez.dk/(o",
                            "http://cygwin.mbwarez.dk/)",
                            "http://cygwin.mbwarez.dk/.",
                            "http://cygwin.mbwarez.dk/.ad.jpjp",
                            "http://cygwin.mbwarez.dk/.cah.de",
                            "http://cygwin.mbwarez.dk/.cnpt$q",
                            "http://cygwin.mbwarez.dk/.comin/3",
                            "http://cygwin.mbwarez.dk/.de//:d",
                            "http://cygwin.mbwarez.dk/.de/ia",
                            "http://cygwin.mbwarez.dk/.dede/t/Ve",
                            "http://cygwin.mbwarez.dk/.degwin//3g",
                            "http://cygwin.mbwarez.dk/.desso.net/",
                            "http://cygwin.mbwarez.dk/.hu/pub/cyg",
                            "http://cygwin.mbwarez.dk/.il/pu",
                            "http://cygwin.mbwarez.dk/.twaren.net",
                            "http://cygwin.mbwarez.dk//",
                            "http://cygwin.mbwarez.dk//.ruhr-uni",
                            "http://cygwin.mbwarez.dk///cygwin/",
                            "http://cygwin.mbwarez.dk///cygwin/4",
                            "http://cygwin.mbwarez.dk//cygwin/",
                            "http://cygwin.mbwarez.dk//cygwin//",
                            "http://cygwin.mbwarez.dk//cygwin///",
                            "http://cygwin.mbwarez.dk//cygwin/=aT",
                            "http://cygwin.mbwarez.dk//cygwin/T",
                            "http://cygwin.mbwarez.dk//cygwin/n/",
                            "http://cygwin.mbwarez.dk//cygwin/win/",
                            "http://cygwin.mbwarez.dk//gwin///f5eP",
                            "http://cygwin.mbwarez.dk//gwin/8g",
                            "http://cygwin.mbwarez.dk//in/",
                            "http://cygwin.mbwarez.dk//in/.com",
                            "http://cygwin.mbwarez.dk//in/comBy",
                            "http://cygwin.mbwarez.dk//pub/cygwin/",
                            "http://cygwin.mbwarez.dk//pub/m",
                            "http://cygwin.mbwarez.dk//wbx",
                            "http://cygwin.mbwarez.dk//win//",
                            "http://cygwin.mbwarez.dk//ygwin/",
                            "http://cygwin.mbwarez.dk//ygwin32/C",
                            "http://cygwin.mbwarez.dk/1",
                            "http://cygwin.mbwarez.dk/3",
                            "http://cygwin.mbwarez.dk/3.com",
                            "http://cygwin.mbwarez.dk/5",
                            "http://cygwin.mbwarez.dk/7",
                            "http://cygwin.mbwarez.dk/7b",
                            "http://cygwin.mbwarez.dk/7z",
                            "http://cygwin.mbwarez.dk/:",
                            "http://cygwin.mbwarez.dk/;",
                            "http://cygwin.mbwarez.dk/;cygwin.mbwarez.dk;Europe;Denmark;noshow",
                            "http://cygwin.mbwarez.dk/A",
                            "http://cygwin.mbwarez.dk/Australi",
                            "http://cygwin.mbwarez.dk/Chinaft",
                            "http://cygwin.mbwarez.dk/D",
                            "http://cygwin.mbwarez.dk/E",
                            "http://cygwin.mbwarez.dk/Europe",
                            "http://cygwin.mbwarez.dk/H",
                            "http://cygwin.mbwarez.dk/Moldova",
                            "http://cygwin.mbwarez.dk/N",
                            "http://cygwin.mbwarez.dk/North",
                            "http://cygwin.mbwarez.dk/P",
                            "http://cygwin.mbwarez.dk/R",
                            "http://cygwin.mbwarez.dk/ac.jpdk",
                            "http://cygwin.mbwarez.dk/acenter.by",
                            "http://cygwin.mbwarez.dk/acenter.by/",
                            "http://cygwin.mbwarez.dk/aist.ac.kr3c",
                            "http://cygwin.mbwarez.dk/aliP",
                            "http://cygwin.mbwarez.dk/ant.com/",
                            "http://cygwin.mbwarez.dk/au2",
                            "http://cygwin.mbwarez.dk/b/cygwin//os",
                            "http://cygwin.mbwarez.dk/b/cygwin/in",
                            "http://cygwin.mbwarez.dk/c.jp/pub/cygwinzw",
                            "http://cygwin.mbwarez.dk/cn",
                            "http://cygwin.mbwarez.dk/cn/cygwin/",
                            "http://cygwin.mbwarez.dk/cn/cygwin/)l",
                            "http://cygwin.mbwarez.dk/cygwin/",
                            "http://cygwin.mbwarez.dk/cygwin/.a",
                            "http://cygwin.mbwarez.dk/cygwin/.ch",
                            "http://cygwin.mbwarez.dk/cygwin/.d",
                            "http://cygwin.mbwarez.dk/cygwin//in/",
                            "http://cygwin.mbwarez.dk/cygwin//n/r",
                            "http://cygwin.mbwarez.dk/cygwin//pub/cOxw",
                            "http://cygwin.mbwarez.dk/cygwin/2z",
                            "http://cygwin.mbwarez.dk/cygwin/H",
                            "http://cygwin.mbwarez.dk/cygwin/ali",
                            "http://cygwin.mbwarez.dk/cygwin/in/",
                            "http://cygwin.mbwarez.dk/cygwin/n/",
                            "http://cygwin.mbwarez.dk/cygwin/n/gf",
                            "http://cygwin.mbwarez.dk/cygwin/qd",
                            "http://cygwin.mbwarez.dk/cygwin/~",
                            "http://cygwin.mbwarez.dk/d",
                            "http://cygwin.mbwarez.dk/d.comin/Z",
                            "http://cygwin.mbwarez.dk/de/cygwin/",
                            "http://cygwin.mbwarez.dk/de/cygwin/:",
                            "http://cygwin.mbwarez.dk/de/cygwin/ny",
                            "http://cygwin.mbwarez.dk/dein//n/-f",
                            "http://cygwin.mbwarez.dk/e",
                            "http://cygwin.mbwarez.dk/e/cygwin//",
                            "http://cygwin.mbwarez.dk/e/software/win9f",
                            "http://cygwin.mbwarez.dk/en.de.orgJ",
                            "http://cygwin.mbwarez.dk/erloo.caz",
                            "http://cygwin.mbwarez.dk/et/cyg",
                            "http://cygwin.mbwarez.dk/et/cygwin/",
                            "http://cygwin.mbwarez.dk/et/cygwin/tsr",
                            "http://cygwin.mbwarez.dk/etworks.org/",
                            "http://cygwin.mbwarez.dk/etworks.org/3",
                            "http://cygwin.mbwarez.dk/fsn.hun.dem",
                            "http://cygwin.mbwarez.dk/ftp://linux",
                            "http://cygwin.mbwarez.dk/g/cygwin/",
                            "http://cygwin.mbwarez.dk/gwin",
                            "http://cygwin.mbwarez.dk/gwin/",
                            "http://cygwin.mbwarez.dk/gwin/32/g",
                            "http://cygwin.mbwarez.dk/gwin/A",
                            "http://cygwin.mbwarez.dk/gwin/n/nu",
                            "http://cygwin.mbwarez.dk/gwin/ware/winkg",
                            "http://cygwin.mbwarez.dk/gwin/win/",
                            "http://cygwin.mbwarez.dk/gwin/win//Eek",
                            "http://cygwin.mbwarez.dk/hen.dein/n/)y",
                            "http://cygwin.mbwarez.dk/ie.fr/",
                            "http://cygwin.mbwarez.dk/il",
                            "http://cygwin.mbwarez.dk/in/",
                            "http://cygwin.mbwarez.dk/in/.edu.pl",
                            "http://cygwin.mbwarez.dk/in/.org.ij",
                            "http://cygwin.mbwarez.dk/in/63.com",
                            "http://cygwin.mbwarez.dk/in/cygwin/",
                            "http://cygwin.mbwarez.dk/in/dxP",
                            "http://cygwin.mbwarez.dk/in/ervice.",
                            "http://cygwin.mbwarez.dk/in/gwin/Fd",
                            "http://cygwin.mbwarez.dk/in/in/",
                            "http://cygwin.mbwarez.dk/in/in/n/",
                            "http://cygwin.mbwarez.dk/in/jp",
                            "http://cygwin.mbwarez.dk/in/l.ca/cLo",
                            "http://cygwin.mbwarez.dk/in/n/",
                            "http://cygwin.mbwarez.dk/in/n///",
                            "http://cygwin.mbwarez.dk/in/n/in/s.",
                            "http://cygwin.mbwarez.dk/in/n/n/",
                            "http://cygwin.mbwarez.dk/in/n/qy",
                            "http://cygwin.mbwarez.dk/in/ropec",
                            "http://cygwin.mbwarez.dk/in/warez.d",
                            "http://cygwin.mbwarez.dk/in/win32/O",
                            "http://cygwin.mbwarez.dk/in/ygwin/qe",
                            "http://cygwin.mbwarez.dk/irror",
                            "http://cygwin.mbwarez.dk/irror-hk",
                            "http://cygwin.mbwarez.dk/m/cygwin/",
                            "http://cygwin.mbwarez.dk/m/cygwin/ata-",
                            "http://cygwin.mbwarez.dk/mirror",
                            "http://cygwin.mbwarez.dk/mirror.dogado.",
                            "http://cygwin.mbwarez.dk/mirrors.",
                            "http://cygwin.mbwarez.dk/n",
                            "http://cygwin.mbwarez.dk/n.dein/",
                            "http://cygwin.mbwarez.dk/n.dein/g/",
                            "http://cygwin.mbwarez.dk/n/",
                            "http://cygwin.mbwarez.dk/n//",
                            "http://cygwin.mbwarez.dk/n/05/",
                            "http://cygwin.mbwarez.dk/n/7",
                            "http://cygwin.mbwarez.dk/n/cygwin/",
                            "http://cygwin.mbwarez.dk/n/cygwin//",
                            "http://cygwin.mbwarez.dk/n/cygwin/0f",
                            "http://cygwin.mbwarez.dk/n/cygwin/Jhh",
                            "http://cygwin.mbwarez.dk/n/cygwin/free&g",
                            "http://cygwin.mbwarez.dk/n/gwin/or",
                            "http://cygwin.mbwarez.dk/n/in/",
                            "http://cygwin.mbwarez.dk/n/in/in/",
                            "http://cygwin.mbwarez.dk/n/n/E0",
                            "http://cygwin.mbwarez.dk/n/ygwin/",
                            "http://cygwin.mbwarez.dk/n/ygwin/=l",
                            "http://cygwin.mbwarez.dk/n/ygwin/sn",
                            "http://cygwin.mbwarez.dk/ncent.com",
                            "http://cygwin.mbwarez.dk/netwin/in/",
                            "http://cygwin.mbwarez.dk/no/cygwin/",
                            "http://cygwin.mbwarez.dk/no/cygwin/Ml",
                            "http://cygwin.mbwarez.dk/o",
                            "http://cygwin.mbwarez.dk/om/cygwin/",
                            "http://cygwin.mbwarez.dk/om/cygwin/G",
                            "http://cygwin.mbwarez.dk/org",
                            "http://cygwin.mbwarez.dk/org/n/=",
                            "http://cygwin.mbwarez.dk/owin/",
                            "http://cygwin.mbwarez.dk/p"
                        ],
                        "description": "URLs found in memory or binary data",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "7058",
                        "match_data": [
                            "8.43.85.97:443 -> 192.168.2.10:49713 version: TLS 1.2"
                        ],
                        "description": "Uses secure TLS version for HTTPS connections",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "description": "Uses HTTPS",
                        "match_data": [
                            "HTTP traffic on port 49728 -> 443",
                            "HTTP traffic on port 443 -> 49728"
                        ],
                        "severity": "IMPACT_SEVERITY_INFO",
                        "id": "625"
                    },
                    {
                        "refs": [
                            {
                                "ref": "#memory_dumps",
                                "value": "software.exe, 00000001.00000002.4622195069.0000000000D18000.00000004.00000020.00020000.00000000.sdmp, software.exe, 00000001.00000002.4623016437.0000000000D68000.00000004.00000020.00020000.00000000.sdmp"
                            }
                        ],
                        "description": "May try to detect the virtual machine to hinder analysis (VM artifact strings found in memory)",
                        "match_data": [
                            "Hyper-V RAW"
                        ],
                        "severity": "IMPACT_SEVERITY_INFO",
                        "id": "263"
                    },
                    {
                        "description": "URLs found in memory or binary data",
                        "match_data": [
                            "ftp://cygwin.mirror.rafal.ca/pub/cygwin/en",
                            "ftp://cygwin.mirror.rafal.ca/pub/cygwin/st",
                            "ftp://cygwin.mirror.rafal.cat",
                            "ftp://ftp.Q",
                            "ftp://ftp.byfly.by/pub/cygwin/https://f",
                            "ftp://ftp.byfly.by/pub/cygwin/in/",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/http://c",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/https://",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/https://;",
                            "ftp://ftp.fa",
                            "ftp://ftp.fau.de/cygwin/gen.dehttp://mm",
                            "ftp://ftp.fau.de/cygwin/ix",
                            "ftp://ftp.fau.de/cygwin/mirror",
                            "ftp://ftp.fs",
                            "ftp://ftp.fsj",
                            "ftp://ftp.fsn.hu/pub/cygwin/http://ftp.",
                            "ftp://ftp.halifax.rwth-aachen.de",
                            "ftp://ftp.halifax.rwth-aachen.de/",
                            "ftp://ftp.halifax.rwth-aachen.de/cygwin/ygwin/http://m",
                            "ftp://ftp.halifax.rwth-aachen.dehttps:/h2",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/http://fK",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/http://fu",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/http://m5",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/https://",
                            "ftp://ftp.inf.tu-dresden.deygwin",
                            "ftp://ftp.kaist.ac.kr/cygwin/https://)",
                            "ftp://ftp.kaist.ac.kr/cygwin/rror",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/http://m",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/https://8",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/https://d",
                            "ftp://ftp.kr.freebsd.orgderors",
                            "ftp://ftp.lU/",
                            "ftp://ftp.lip6.fr/pub/cygwin/",
                            "ftp://ftp.lip6.fr/pub/cygwin/p",
                            "ftp://ftp.lip6.fr/pub/cygwin/win/http:",
                            "ftp://ftp.muug.ca/mirror/cygwin/in/",
                            "ftp://ftp.n",
                            "ftp://ftp.ntua.gr",
                            "ftp://ftp.rnl.tecnico.ulisboa.pt/http:",
                            "ftp://ftp.yz.yamagata-u.ac.jp/pub/cygwin/",
                            "ftp://ftp.yz.yamagata-u.ac.jphttps://)",
                            "ftp://linux.rz.ruhr-uni-bochum.de",
                            "ftp://linux.rz.ruhr-uni-bochum.dehttps:",
                            "ftp://mirror.checkdomain.de/cygwin/http",
                            "ftp://mirror.cs.vt.edu/pub/cygwin/cygwin//http",
                            "ftp://mirror.csclub.uwaterlo",
                            "ftp://mirror.datacenter.by/http://ftp.",
                            "ftp://mirror.datacenter.bytechor",
                            "ftp://mirror.easyname.at/cygwin/http://m",
                            "ftp://mirror.easyname.attp",
                            "ftp://mirror.internode.on.net",
                            "ftp://mirror.internode.on.neters",
                            "ftp://mirrors.dotsrc.org/mirrors/cygwin/st",
                            "ftp://mirrors.netix.net/cygwin/",
                            "ftp://mirrors.netix.net/cygwin/http://f",
                            "ftp://mirrors.netix.net/cygwin/https://",
                            "ftp://mirrors.syringanetworks.net/cygwin/",
                            "ftp://sourceware.org/ftp://sources.redhat.com/ftp://gcc.gnu.org/",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/http://l",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/in/https://C",
                            "ftp://sunsite.icm.edu.plygwin",
                            "http://ac.economia.gob.mx/cps.html0",
                            "http://ac.economia.gob.mx/last.crl0G",
                            "http://acedicom.edicomgroup.com/doc0",
                            "http://acraiz.icpbrasil.gov.br/DPCacraiz.pdf0?",
                            "http://acraiz.icpbrasil.gov.br/LCRacraizv1.crl0",
                            "http://acraiz.icpbrasil.gov.br/LCRacraizv2.crl0",
                            "http://apps.identrust.com/roots/dstrootcax3.p7c0",
                            "http://ca.disig.sk/ca/crl/ca_disig.crl0",
                            "http://ca.mtin.es/mtin/DPCyPoliticas0",
                            "http://ca.mtin.es/mtin/DPCyPoliticas0g",
                            "http://ca.mtin.es/mtin/crl/MTINAutoridadRaiz03",
                            "http://ca.mtin.es/mtin/ocsp0",
                            "http://ca2.mtin.es/mtin/crl/MTINAutoridadRaiz0",
                            "http://certificates.starfieldtech.com/repository/1604",
                            "http://certs.oati.net/repository/OATICA2.crl0",
                            "http://certs.oati.net/repository/OATICA2.crt0",
                            "http://certs.oaticerts.com/repository/OATICA2.crl",
                            "http://certs.oaticerts.com/repository/OATICA2.crt08",
                            "http://cps.chambersign.org/cps/chambersignroot.html0",
                            "http://cps.chambersign.org/cps/chambersroot.html0",
                            "http://cps.letsencrypt.org0",
                            "http://cps.root-x1.letsencrypt.org0",
                            "http://cps.siths.se/sithsrootcav1.html0",
                            "http://crl.certigna.fr/certignarootca.crl01",
                            "http://crl.chambersign.org/chambersignroot.crl0",
                            "http://crl.chambersign.org/chambersroot.crl0",
                            "http://crl.comodoca.com/AAACertificateServices.crl06",
                            "http://crl.defence.gov.au/pki0",
                            "http://crl.dhimyotis.com/certignarootca.crl0",
                            "http://crl.globalsign.net/root-r2.crl0",
                            "http://crl.identrust.com/DSTROOTCAX3CRL.crl0",
                            "http://crl.oces.trust2408.com/oces.crl0",
                            "http://crl.pki.wellsfargo.com/wsprca.crl0",
                            "http://crl.securetrust.com/SGCA.crl0",
                            "http://crl.securetrust.com/STCA.crl0",
                            "http://crl.ssc.lt/root-a/cacrl.crl0",
                            "http://crl.ssc.lt/root-b/cacrl.crl0",
                            "http://crl.ssc.lt/root-c/cacrl.crl0",
                            "http://crl.xrampsecurity.com/XGCA.crl0",
                            "http://crl1.comsign.co.il/crl/comsignglobalrootca.crl0",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/CABD2A79A1076A31F21D253635CB0",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/authrootstl.cab",
                            "http://ctldl.windowsupdate.com:80/msdownload/update/v3/static/trustedr/en/CABD2A79A1076A31F21D253635",
                            "http://cygwin.cathedral-g3",
                            "http://cygwin.cathedral-networks.org",
                            "http://cygwin.cathedral-networks.org)",
                            "http://cygwin.cathedral-networks.org.haz&",
                            "http://cygwin.cathedral-networks.org/",
                            "http://cygwin.cathedral-networks.org/)",
                            "http://cygwin.cathedral-networks.org/-6",
                            "http://cygwin.cathedral-networks.org/.S",
                            "http://cygwin.cathedral-networks.org/.dc",
                            "http://cygwin.cathedral-networks.org/.i",
                            "http://cygwin.cathedral-networks.org/.o",
                            "http://cygwin.cathedral-networks.org//",
                            "http://cygwin.cathedral-networks.org///",
                            "http://cygwin.cathedral-networks.org///E/",
                            "http://cygwin.cathedral-networks.org//J-X",
                            "http://cygwin.cathedral-networks.org//S&7",
                            "http://cygwin.cathedral-networks.org//V",
                            "http://cygwin.cathedral-networks.org//f",
                            "http://cygwin.cathedral-networks.org//fA",
                            "http://cygwin.cathedral-networks.org//lV(",
                            "http://cygwin.cathedral-networks.org//m",
                            "http://cygwin.cathedral-networks.org//mirror0",
                            "http://cygwin.cathedral-networks.org//p-V",
                            "http://cygwin.cathedral-networks.org//w",
                            "http://cygwin.cathedral-networks.org//wm&",
                            "http://cygwin.cathedral-networks.org/9",
                            "http://cygwin.cathedral-networks.org/;$",
                            "http://cygwin.cathedral-networks.org/;cygwin.cathedral-networks.org;Europe;Norway;noshow",
                            "http://cygwin.cathedral-networks.org/?",
                            "http://cygwin.cathedral-networks.org/?;",
                            "http://cygwin.cathedral-networks.org/Am.",
                            "http://cygwin.cathedral-networks.org/H",
                            "http://cygwin.cathedral-networks.org/H)",
                            "http://cygwin.cathedral-networks.org/H3",
                            "http://cygwin.cathedral-networks.org/L",
                            "http://cygwin.cathedral-networks.org/L&",
                            "http://cygwin.cathedral-networks.org/U",
                            "http://cygwin.cathedral-networks.org/W",
                            "http://cygwin.cathedral-networks.org/Y3",
                            "http://cygwin.cathedral-networks.org/a3",
                            "http://cygwin.cathedral-networks.org/buu",
                            "http://cygwin.cathedral-networks.org/cB",
                            "http://cygwin.cathedral-networks.org/cy",
                            "http://cygwin.cathedral-networks.org/d",
                            "http://cygwin.cathedral-networks.org/d3",
                            "http://cygwin.cathedral-networks.org/e",
                            "http://cygwin.cathedral-networks.org/ha",
                            "http://cygwin.cathedral-networks.org/i",
                            "http://cygwin.cathedral-networks.org/ia",
                            "http://cygwin.cathedral-networks.org/in",
                            "http://cygwin.cathedral-networks.org/j",
                            "http://cygwin.cathedral-networks.org/k",
                            "http://cygwin.cathedral-networks.org/l",
                            "http://cygwin.cathedral-networks.org/ly",
                            "http://cygwin.cathedral-networks.org/m",
                            "http://cygwin.cathedral-networks.org/mi",
                            "http://cygwin.cathedral-networks.org/nc(",
                            "http://cygwin.cathedral-networks.org/ni",
                            "http://cygwin.cathedral-networks.org/o)Y",
                            "http://cygwin.cathedral-networks.org/on",
                            "http://cygwin.cathedral-networks.org/p/",
                            "http://cygwin.cathedral-networks.org/p1",
                            "http://cygwin.cathedral-networks.org/pl9",
                            "http://cygwin.cathedral-networks.org/q",
                            "http://cygwin.cathedral-networks.org/q.",
                            "http://cygwin.cathedral-networks.org/r-v&",
                            "http://cygwin.cathedral-networks.org/r0",
                            "http://cygwin.cathedral-networks.org/ro-",
                            "http://cygwin.cathedral-networks.org/rz",
                            "http://cygwin.cathedral-networks.org/s/",
                            "http://cygwin.cathedral-networks.org/s/t",
                            "http://cygwin.cathedral-networks.org/st&",
                            "http://cygwin.cathedral-networks.org/t$",
                            "http://cygwin.cathedral-networks.org/tc",
                            "http://cygwin.cathedral-networks.org/te_",
                            "http://cygwin.cathedral-networks.org/tp",
                            "http://cygwin.cathedral-networks.org/u",
                            "http://cygwin.cathedral-networks.org/unS",
                            "http://cygwin.cathedral-networks.org/wn",
                            "http://cygwin.cathedral-networks.org/y1",
                            "http://cygwin.cathedral-networks.org/ygB",
                            "http://cygwin.cathedral-networks.org/~6",
                            "http://cygwin.cathedral-networks.org6",
                            "http://cygwin.cathedral-networks.org://",
                            "http://cygwin.cathedral-networks.orgA&",
                            "http://cygwin.cathedral-networks.orgS",
                            "http://cygwin.cathedral-networks.orgT",
                            "http://cygwin.cathedral-networks.orgb/c",
                            "http://cygwin.cathedral-networks.orgb6",
                            "http://cygwin.cathedral-networks.orgd",
                            "http://cygwin.cathedral-networks.orgi",
                            "http://cygwin.cathedral-networks.orgl",
                            "http://cygwin.cathedral-networks.orgn/",
                            "http://cygwin.cathedral-networks.orgn/V",
                            "http://cygwin.cathedral-networks.orgn/X",
                            "http://cygwin.cathedral-networks.orgn/w3",
                            "http://cygwin.cathedral-networks.orgomH",
                            "http://cygwin.cathedral-networks.orgon",
                            "http://cygwin.cathedral-networks.orgown",
                            "http://cygwin.cathedral-networks.orgp6",
                            "http://cygwin.cathedral-networks.orgtsc",
                            "http://cygwin.cathedral-networks.orgwin",
                            "http://cygwin.cathedral-networks.orgwnl",
                            "http://cygwin.cathedral-networks.orgx",
                            "http://cygwin.cathedral-networks.orgygw",
                            "http://cygwin.cathedral-s-W",
                            "http://cygwin.mbwarez",
                            "http://cygwin.mbwarez.dk",
                            "http://cygwin.mbwarez.dk.",
                            "http://cygwin.mbwarez.dk.ac.jp/N%",
                            "http://cygwin.mbwarez.dk.ac.jpin/aren.net",
                            "http://cygwin.mbwarez.dk.aur/cygwin/",
                            "http://cygwin.mbwarez.dk.byn//7",
                            "http://cygwin.mbwarez.dk.de/cygwin/",
                            "http://cygwin.mbwarez.dk.deorks.orga",
                            "http://cygwin.mbwarez.dk.net",
                            "http://cygwin.mbwarez.dk.netwin/s://e",
                            "http://cygwin.mbwarez.dk.orgcygwin/yg",
                            "http://cygwin.mbwarez.dk/",
                            "http://cygwin.mbwarez.dk/#",
                            "http://cygwin.mbwarez.dk/#p.fau.de",
                            "http://cygwin.mbwarez.dk/$",
                            "http://cygwin.mbwarez.dk/$$",
                            "http://cygwin.mbwarez.dk/%",
                            "http://cygwin.mbwarez.dk/.ac.nz",
                            "http://cygwin.mbwarez.dk/.at/cygwin//;.",
                            "http://cygwin.mbwarez.dk/.cn/cygwin/",
                            "http://cygwin.mbwarez.dk/.cn/cygwin///e",
                            "http://cygwin.mbwarez.dk/.cnygwin/",
                            "http://cygwin.mbwarez.dk/.iij.ad.jpjpQ",
                            "http://cygwin.mbwarez.dk/.nc",
                            "http://cygwin.mbwarez.dk/.nete",
                            "http://cygwin.mbwarez.dk/.netgwin/",
                            "http://cygwin.mbwarez.dk///cygwin/",
                            "http://cygwin.mbwarez.dk//cygwin/",
                            "http://cygwin.mbwarez.dk//cygwin/.gar",
                            "http://cygwin.mbwarez.dk//cygwin//",
                            "http://cygwin.mbwarez.dk//cygwin//sd",
                            "http://cygwin.mbwarez.dk//cygwin/n/",
                            "http://cygwin.mbwarez.dk//gwin//g",
                            "http://cygwin.mbwarez.dk//n/",
                            "http://cygwin.mbwarez.dk/1",
                            "http://cygwin.mbwarez.dk/5A",
                            "http://cygwin.mbwarez.dk/;cygwin.mbwarez.dk;Europe;Denmark;noshow",
                            "http://cygwin.mbwarez.dk/Asia/",
                            "http://cygwin.mbwarez.dk/E",
                            "http://cygwin.mbwarez.dk/Europe",
                            "http://cygwin.mbwarez.dk/F",
                            "http://cygwin.mbwarez.dk/Hong",
                            "http://cygwin.mbwarez.dk/achen.deo",
                            "http://cygwin.mbwarez.dk/agata-u.ac.jp",
                            "http://cygwin.mbwarez.dk/bygwin/",
                            "http://cygwin.mbwarez.dk/c.jp",
                            "http://cygwin.mbwarez.dk/chum.degwin/",
                            "http://cygwin.mbwarez.dk/cn/cygwin/",
                            "http://cygwin.mbwarez.dk/cn/cygwin/.e",
                            "http://cygwin.mbwarez.dk/cnso.net/",
                            "http://cygwin.mbwarez.dk/cygwin/",
                            "http://cygwin.mbwarez.dk/cygwin//",
                            "http://cygwin.mbwarez.dk/cygwin/I",
                            "http://cygwin.mbwarez.dk/cygwin/K",
                            "http://cygwin.mbwarez.dk/cygwin/R2",
                            "http://cygwin.mbwarez.dk/cygwin/W",
                            "http://cygwin.mbwarez.dk/cygwin/et",
                            "http://cygwin.mbwarez.dk/cygwin/gwin/N",
                            "http://cygwin.mbwarez.dk/cygwin/in/",
                            "http://cygwin.mbwarez.dk/cygwin/in//",
                            "http://cygwin.mbwarez.dk/cygwin/n",
                            "http://cygwin.mbwarez.dk/cygwin/n/",
                            "http://cygwin.mbwarez.dk/cygwin/n/N",
                            "http://cygwin.mbwarez.dk/cygwin/win/",
                            "http://cygwin.mbwarez.dk/d.com/cygwin/",
                            "http://cygwin.mbwarez.dk/d.com/gwin/",
                            "http://cygwin.mbwarez.dk/d.comn/",
                            "http://cygwin.mbwarez.dk/de",
                            "http://cygwin.mbwarez.dk/de/cygwin//",
                            "http://cygwin.mbwarez.dk/de/cygwin/EuropeH0",
                            "http://cygwin.mbwarez.dk/derror.easyna",
                            "http://cygwin.mbwarez.dk/e/cygwin/",
                            "http://cygwin.mbwarez.dk/e:",
                            "http://cygwin.mbwarez.dk/ea.ptttps://",
                            "http://cygwin.mbwarez.dk/ebsd.orgc.jp",
                            "http://cygwin.mbwarez.dk/egwin/win/",
                            "http://cygwin.mbwarez.dk/et/cygwin/",
                            "http://cygwin.mbwarez.dk/etn//",
                            "http://cygwin.mbwarez.dk/fly.by.nc",
                            "http://cygwin.mbwarez.dk/g/cygwin/F-c",
                            "http://cygwin.mbwarez.dk/g/cygwin/i",
                            "http://cygwin.mbwarez.dk/g/cygwin/mq",
                            "http://cygwin.mbwarez.dk/g/cygwin/w",
                            "http://cygwin.mbwarez.dk/g/cygwin/~",
                            "http://cygwin.mbwarez.dk/gie.frpt/soft_",
                            "http://cygwin.mbwarez.dk/gwin/",
                            "http://cygwin.mbwarez.dk/gwin//",
                            "http://cygwin.mbwarez.dk/gwin//win/",
                            "http://cygwin.mbwarez.dk/gwin/W",
                            "http://cygwin.mbwarez.dk/gwin/cn/cyd",
                            "http://cygwin.mbwarez.dk/gwin/n/C/B",
                            "http://cygwin.mbwarez.dk/gwin/n/liZ-o",
                            "http://cygwin.mbwarez.dk/gwin/n32/",
                            "http://cygwin.mbwarez.dk/gwin/ope",
                            "http://cygwin.mbwarez.dk/gwin/p://cy/",
                            "http://cygwin.mbwarez.dk/gwin/win/b",
                            "http://cygwin.mbwarez.dk/h.de",
                            "http://cygwin.mbwarez.dk/hen.de",
                            "http://cygwin.mbwarez.dk/hen.deorg/",
                            "http://cygwin.mbwarez.dk/in.uib.no/",
                            "http://cygwin.mbwarez.dk/in/",
                            "http://cygwin.mbwarez.dk/in//",
                            "http://cygwin.mbwarez.dk/in//$",
                            "http://cygwin.mbwarez.dk/in/cygwin/e8",
                            "http://cygwin.mbwarez.dk/in/cygwin/ft",
                            "http://cygwin.mbwarez.dk/in/gwin/l",
                            "http://cygwin.mbwarez.dk/in/in//7",
                            "http://cygwin.mbwarez.dk/in/in/ac",
                            "http://cygwin.mbwarez.dk/in/in/n/",
                            "http://cygwin.mbwarez.dk/in/in/r.",
                            "http://cygwin.mbwarez.dk/in/n/",
                            "http://cygwin.mbwarez.dk/in/ong",
                            "http://cygwin.mbwarez.dk/in/siaN2",
                            "http://cygwin.mbwarez.dk/in/tp://su",
                            "http://cygwin.mbwarez.dk/in/win/",
                            "http://cygwin.mbwarez.dk/in/ygwin",
                            "http://cygwin.mbwarez.dk/inade",
                            "http://cygwin.mbwarez.dk/irror.easynr-",
                            "http://cygwin.mbwarez.dk/jp",
                            "http://cygwin.mbwarez.dk/ly.coml",
                            "http://cygwin.mbwarez.dk/ly.comn/r",
                            "http://cygwin.mbwarez.dk/m.de/cygwin/",
                            "http://cygwin.mbwarez.dk/m/cygwin/",
                            "http://cygwin.mbwarez.dk/mgwin/rrors./",
                            "http://cygwin.mbwarez.dk/n.itefix.nef",
                            "http://cygwin.mbwarez.dk/n/",
                            "http://cygwin.mbwarez.dk/n/al.ca/",
                            "http://cygwin.mbwarez.dk/n/cygw",
                            "http://cygwin.mbwarez.dk/n/gwin/du",
                            "http://cygwin.mbwarez.dk/n/win//",
                            "http://cygwin.mbwarez.dk/n/ygwin/",
                            "http://cygwin.mbwarez.dk/net//63.com",
                            "http://cygwin.mbwarez.dk/net/il",
                            "http://cygwin.mbwarez.dk/ngwin/cente",
                            "http://cygwin.mbwarez.dk/no/cygwin/",
                            "http://cygwin.mbwarez.dk/nter.byuni$",
                            "http://cygwin.mbwarez.dk/o/cygwin/",
                            "http://cygwin.mbwarez.dk/o/cygwin/A",
                            "http://cygwin.mbwarez.dk/o/cygwin/t",
                            "http://cygwin.mbwarez.dk/ochum.depe",
                            "http://cygwin.mbwarez.dk/ochum.deps://p",
                            "http://cygwin.mbwarez.dk/om/cygwin/$/",
                            "http://cygwin.mbwarez.dk/om/cygwin//",
                            "http://cygwin.mbwarez.dk/orgcom",
                            "http://cygwin.mbwarez.dk/p.fau.dein",
                            "http://cygwin.mbwarez.dk/pub/softwarV",
                            "http://cygwin.mbwarez.dk/r.datacente1",
                            "http://cygwin.mbwarez.dk/rg/cygwin/",
                            "http://cygwin.mbwarez.dk/rgasso.net",
                            "http://cygwin.mbwarez.dk/rggwin/t//",
                            "http://cygwin.mbwarez.dk/rlands",
                            "http://cygwin.mbwarez.dk/st.comin/",
                            "http://cygwin.mbwarez.dk/t/cygwin/",
                            "http://cygwin.mbwarez.dk/t/cygwin/O",
                            "http://cygwin.mbwarez.dk/t/cygwin/an",
                            "http://cygwin.mbwarez.dk/t/cygwin/ygw",
                            "http://cygwin.mbwarez.dk/te.nlchen.%",
                            "http://cygwin.mbwarez.dk/tworks.org",
                            "http://cygwin.mbwarez.dk/u.cn/cygwin/.",
                            "http://cygwin.mbwarez.dk/ub/cygwin/%",
                            "http://cygwin.mbwarez.dk/unsite.icm.:",
                            "http://cygwin.mbwarez.dk/win.uib.no///",
                            "http://cygwin.mbwarez.dk/win/",
                            "http://cygwin.mbwarez.dk/win/B",
                            "http://cygwin.mbwarez.dk/win/ac.jp",
                            "http://cygwin.mbwarez.dk/win/gwin/",
                            "http://cygwin.mbwarez.dk/win/in/",
                            "http://cygwin.mbwarez.dk/win/in//",
                            "http://cygwin.mbwarez.dk/win/in/sl",
                            "http://cygwin.mbwarez.dk/win/inam.l",
                            "http://cygwin.mbwarez.dk/win/n/",
                            "http://cygwin.mbwarez.dk/win/n//",
                            "http://cygwin.mbwarez.dk/win/n/in/",
                            "http://cygwin.mbwarez.dk/win/om",
                            "http://cygwin.mbwarez.dk/win/tps://",
                            "http://cygwin.mbwarez.dk/ygwin/",
                            "http://cygwin.mbwarez.dk/ygwin/.net",
                            "http://cygwin.mbwarez.dk/ygwin//",
                            "http://cygwin.mbwarez.dk/ygwin///",
                            "http://cygwin.mbwarez.dk/ygwin///_",
                            "http://cygwin.mbwarez.dk/ygwin//rcf",
                            "http://cygwin.mbwarez.dk/ygwin/P",
                            "http://cygwin.mbwarez.dk/ygwin/a/O",
                            "http://cygwin.mbwarez.dk/ygwin/gwin/f",
                            "http://cygwin.mbwarez.dk/ygwin/in/://%",
                            "http://cygwin.mbwarez.dk/ygwin/no//",
                            "http://cygwin.mbwarez.dk/ygwin/tp://ft"
                        ],
                        "severity": "IMPACT_SEVERITY_INFO",
                        "id": "238"
                    },
                    {
                        "description": "Uses secure TLS version for HTTPS connections",
                        "match_data": [
                            "8.43.85.97:443 -> 192.168.2.12:49728 version: TLS 1.2"
                        ],
                        "severity": "IMPACT_SEVERITY_INFO",
                        "id": "7058"
                    },
                    {
                        "severity": "IMPACT_SEVERITY_INFO",
                        "refs": [
                            {
                                "ref": "#memory_dumps",
                                "value": "software.exe, 00000000.00000002.4957179451.00000000001D6000.00000004.00000020.00020000.00000000.sdmp, software.exe, 00000000.00000002.4956225446.000000000016C000.00000004.00000020.00020000.00000000.sdmp"
                            }
                        ],
                        "match_data": [
                            "Hyper-V RAW"
                        ],
                        "id": "263",
                        "description": "May try to detect the virtual machine to hinder analysis (VM artifact strings found in memory)"
                    },
                    {
                        "severity": "IMPACT_SEVERITY_INFO",
                        "match_data": [
                            "ftp://ftp.=",
                            "ftp://ftp.byfly.by/pub/cygwin/http://f",
                            "ftp://ftp.byfly.by/pub/cygwin/ub/cygwin/cacygwin",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/http://cG",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/win",
                            "ftp://ftp.fsn.hu/pub/cygwin/p",
                            "ftp://ftp.fsn.hu/pub/cygwin/ror",
                            "ftp://ftp.fsn.hu/pub/cygwin/ygwin/https://)",
                            "ftp://ftp.fsn.hur",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/http://d",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/http://f",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/https://",
                            "ftp://ftp.inf.tu-dresden.deftp",
                            "ftp://ftp.inf.tu-dresden.dehttp://ftp.f",
                            "ftp://ftp.inf.tu-dresden.dein",
                            "ftp://ftp.inf.tu-dresden.deygwin",
                            "ftp://ftp.kr.freebsd.org",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/http://c",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/http://f",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/https://",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/https://0",
                            "ftp://ftp.l",
                            "ftp://ftp.lip6.fr/pub/cygwin//https://",
                            "ftp://ftp.m2",
                            "ftp://ftp.muug.ca/mirror/cygwin//or",
                            "ftp://ftp.n",
                            "ftp://ftp.ntua.gr/pub/pc/cygwin/",
                            "ftp://ftp.ntua.gr/pub/pc/cygwin/http:/",
                            "ftp://ftp.rnl.tecnico.ulisboa.pt",
                            "ftp://ftp.yz.yamagata-u.ac.jp/pub/cygwin/http://c",
                            "ftp://linux.rz.ruhr-uni-bochum.de/cygwin/http://c",
                            "ftp://mirror.checkdomain.de/cygwin/",
                            "ftp://mirror.checkdomain.de/cygwin/http",
                            "ftp://mirror.checkdomain.de/cygwin/httpA",
                            "ftp://mirror.checkdomain.de/cygwin/https://",
                            "ftp://mirror.checkdomain.dehttp://w",
                            "ftp://mirror.checkdomain.dein",
                            "ftp://mirror.csclub.uwaterloo.car",
                            "ftp://mirror.datacenter.bymirror",
                            "ftp://mirror.datacenter.byon.ncr",
                            "ftp://mirror.easyname.at/cygwin/r",
                            "ftp://mirror.easyname.atomygwin",
                            "ftp://mirror.lagoon.nc/cygwin/http://f",
                            "ftp://mirror.lagoon.nc/cygwin/http://m",
                            "ftp://mirror.lagoon.nc/cygwin/ror",
                            "ftp://mirrors.dotsrc.org.nethttps://V",
                            "ftp://mirrors.dotsrc.org/mirrors/cygwin/http://muug.ca/",
                            "ftp://mirrors.netix.net/cygwin/http://fL",
                            "ftp://mirrors.netix.net/cygwin/https://",
                            "ftp://mirrors.netix.net/cygwin/https://z",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/https://",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/https://_",
                            "ftp://sunsite.icm.edu.plftp",
                            "http://ac.economia.gob.mx/cps.html0",
                            "http://ac.economia.gob.mx/last.crl0G",
                            "http://acedicom.edicomgroup.com/doc0",
                            "http://acraiz.icpbrasil.gov.br/DPCacraiz.pdf0?",
                            "http://acraiz.icpbrasil.gov.br/LCRacraizv1.crl0",
                            "http://acraiz.icpbrasil.gov.br/LCRacraizv2.crl0",
                            "http://apps.identrust.com/roots/dstrootcax3.p7c0",
                            "http://ca.disig.sk/ca/crl/ca_disig.crl0",
                            "http://ca.mtin.es/mtin/DPCyPoliticas0",
                            "http://ca.mtin.es/mtin/DPCyPoliticas0g",
                            "http://ca.mtin.es/mtin/crl/MTINAutoridadRaiz03",
                            "http://ca.mtin.es/mtin/ocsp0",
                            "http://ca2.mtin.es/mtin/crl/MTINAutoridadRaiz0",
                            "http://certificates.starfieldtech.com/repository/1604",
                            "http://certs.oati.net/repository/OATICA2.crl0",
                            "http://certs.oati.net/repository/OATICA2.crt0",
                            "http://certs.oaticerts.com/repository/OATICA2.crl",
                            "http://certs.oaticerts.com/repository/OATICA2.crt08",
                            "http://cps.chambersign.org/cps/chambersignroot.html0",
                            "http://cps.chambersign.org/cps/chambersroot.html0",
                            "http://cps.letsencrypt.org0",
                            "http://cps.root-x1.letsencrypt.org0",
                            "http://cps.siths.se/sithsrootcav1.html0",
                            "http://crl.certigna.fr/certignarootca.crl01",
                            "http://crl.chambersign.org/chambersignroot.crl0",
                            "http://crl.chambersign.org/chambersroot.crl0",
                            "http://crl.comodoca.com/AAACertificateServices.crl06",
                            "http://crl.defence.gov.au/pki0",
                            "http://crl.dhimyotis.com/certignarootca.crl0",
                            "http://crl.globalsign.net/root-r2.crl0",
                            "http://crl.identrust.com/DSTROOTCAX3CRL.crl0",
                            "http://crl.oces.trust2408.com/oces.crl0",
                            "http://crl.pki.wellsfargo.com/wsprca.crl0",
                            "http://crl.securetrust.com/SGCA.crl0",
                            "http://crl.securetrust.com/STCA.crl0",
                            "http://crl.ssc.lt/root-a/cacrl.crl0",
                            "http://crl.ssc.lt/root-b/cacrl.crl0",
                            "http://crl.ssc.lt/root-c/cacrl.crl0",
                            "http://crl.xrampsecurity.com/XGCA.crl0",
                            "http://crl1.comsign.co.il/crl/comsignglobalrootca.crl0",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/CABD2A79A1076A31F21D253635CB0",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/authrootstl.cab",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/enR(",
                            "http://ctldl.windowsupdate.com:80",
                            "http://ctldl.windowsupdate.com:80/msdownload/update/v3/static/trustedr/en/CABD2A79A1076A31F21D253635",
                            "http://cygwin.cathedral-",
                            "http://cygwin.cathedral-networks.org",
                            "http://cygwin.cathedral-networks.org.ne",
                            "http://cygwin.cathedral-networks.org/",
                            "http://cygwin.cathedral-networks.org/#",
                            "http://cygwin.cathedral-networks.org/$",
                            "http://cygwin.cathedral-networks.org/%",
                            "http://cygwin.cathedral-networks.org/&",
                            "http://cygwin.cathedral-networks.org/)",
                            "http://cygwin.cathedral-networks.org/.",
                            "http://cygwin.cathedral-networks.org/.cN",
                            "http://cygwin.cathedral-networks.org/.m",
                            "http://cygwin.cathedral-networks.org//",
                            "http://cygwin.cathedral-networks.org///",
                            "http://cygwin.cathedral-networks.org//:",
                            "http://cygwin.cathedral-networks.org//c",
                            "http://cygwin.cathedral-networks.org//e",
                            "http://cygwin.cathedral-networks.org//f",
                            "http://cygwin.cathedral-networks.org//j",
                            "http://cygwin.cathedral-networks.org//m",
                            "http://cygwin.cathedral-networks.org//o",
                            "http://cygwin.cathedral-networks.org/1",
                            "http://cygwin.cathedral-networks.org/4",
                            "http://cygwin.cathedral-networks.org/6",
                            "http://cygwin.cathedral-networks.org/8",
                            "http://cygwin.cathedral-networks.org/9",
                            "http://cygwin.cathedral-networks.org/:",
                            "http://cygwin.cathedral-networks.org/:/",
                            "http://cygwin.cathedral-networks.org/;cygwin.cathedral-networks.org;Europe;Norway;noshow",
                            "http://cygwin.cathedral-networks.org/=",
                            "http://cygwin.cathedral-networks.org/A",
                            "http://cygwin.cathedral-networks.org/F",
                            "http://cygwin.cathedral-networks.org/G",
                            "http://cygwin.cathedral-networks.org/L",
                            "http://cygwin.cathedral-networks.org/O",
                            "http://cygwin.cathedral-networks.org/T",
                            "http://cygwin.cathedral-networks.org/U",
                            "http://cygwin.cathedral-networks.org/Y",
                            "http://cygwin.cathedral-networks.org/Z",
                            "http://cygwin.cathedral-networks.org/a",
                            "http://cygwin.cathedral-networks.org/ar",
                            "http://cygwin.cathedral-networks.org/cygwin/s.org/",
                            "http://cygwin.cathedral-networks.org/e",
                            "http://cygwin.cathedral-networks.org/et",
                            "http://cygwin.cathedral-networks.org/f",
                            "http://cygwin.cathedral-networks.org/ft",
                            "http://cygwin.cathedral-networks.org/ft9",
                            "http://cygwin.cathedral-networks.org/ine",
                            "http://cygwin.cathedral-networks.org/k",
                            "http://cygwin.cathedral-networks.org/l",
                            "http://cygwin.cathedral-networks.org/li~",
                            "http://cygwin.cathedral-networks.org/m",
                            "http://cygwin.cathedral-networks.org/mi",
                            "http://cygwin.cathedral-networks.org/n/u",
                            "http://cygwin.cathedral-networks.org/ne8",
                            "http://cygwin.cathedral-networks.org/ni",
                            "http://cygwin.cathedral-networks.org/o",
                            "http://cygwin.cathedral-networks.org/ore",
                            "http://cygwin.cathedral-networks.org/ork",
                            "http://cygwin.cathedral-networks.org/ps",
                            "http://cygwin.cathedral-networks.org/q",
                            "http://cygwin.cathedral-networks.org/slo",
                            "http://cygwin.cathedral-networks.org/su",
                            "http://cygwin.cathedral-networks.org/t",
                            "http://cygwin.cathedral-networks.org/tp",
                            "http://cygwin.cathedral-networks.org/ul",
                            "http://cygwin.cathedral-networks.org/w",
                            "http://cygwin.cathedral-networks.org/wi",
                            "http://cygwin.cathedral-networks.org/x",
                            "http://cygwin.cathedral-networks.org/z",
                            "http://cygwin.cathedral-networks.org0",
                            "http://cygwin.cathedral-networks.org1",
                            "http://cygwin.cathedral-networks.org://",
                            "http://cygwin.cathedral-networks.orgB",
                            "http://cygwin.cathedral-networks.orgI",
                            "http://cygwin.cathedral-networks.orgM",
                            "http://cygwin.cathedral-networks.orgP",
                            "http://cygwin.cathedral-networks.orgR",
                            "http://cygwin.cathedral-networks.orgT",
                            "http://cygwin.cathedral-networks.org_",
                            "http://cygwin.cathedral-networks.orgala",
                            "http://cygwin.cathedral-networks.orgb",
                            "http://cygwin.cathedral-networks.orgdu.",
                            "http://cygwin.cathedral-networks.orgjpo",
                            "http://cygwin.cathedral-networks.orgm",
                            "http://cygwin.cathedral-networks.orgme",
                            "http://cygwin.cathedral-networks.orgn",
                            "http://cygwin.cathedral-networks.orgn/",
                            "http://cygwin.cathedral-networks.orgn/#",
                            "http://cygwin.cathedral-networks.orgnet",
                            "http://cygwin.cathedral-networks.orgom.",
                            "http://cygwin.cathedral-networks.orgr.tD",
                            "http://cygwin.cathedral-networks.orgs",
                            "http://cygwin.cathedral-networks.orgtp:",
                            "http://cygwin.cathedral-networks.orgwen?",
                            "http://cygwin.cathedral-networks.orgz",
                            "http://cygwin.mbwarez",
                            "http://cygwin.mbwarez.dk",
                            "http://cygwin.mbwarez.dk#W",
                            "http://cygwin.mbwarez.dk$",
                            "http://cygwin.mbwarez.dk.ac.jpn/in/",
                            "http://cygwin.mbwarez.dk.byygwin/",
                            "http://cygwin.mbwarez.dk.de/n/",
                            "http://cygwin.mbwarez.dk.kr.freebsd.orgi",
                            "http://cygwin.mbwarez.dk.net.it",
                            "http://cygwin.mbwarez.dk.netA",
                            "http://cygwin.mbwarez.dk.netgw",
                            "http://cygwin.mbwarez.dk.orgygwin/",
                            "http://cygwin.mbwarez.dk/",
                            "http://cygwin.mbwarez.dk/#Y",
                            "http://cygwin.mbwarez.dk/.de/",
                            "http://cygwin.mbwarez.dk/.deon.net",
                            "http://cygwin.mbwarez.dk/.edu.cn/",
                            "http://cygwin.mbwarez.dk/.hu/pub/cygwin",
                            "http://cygwin.mbwarez.dk/.jpygwin/",
                            "http://cygwin.mbwarez.dk//",
                            "http://cygwin.mbwarez.dk///",
                            "http://cygwin.mbwarez.dk///mirror.easyn",
                            "http://cygwin.mbwarez.dk//?",
                            "http://cygwin.mbwarez.dk//cygwin/",
                            "http://cygwin.mbwarez.dk//cygwin/or",
                            "http://cygwin.mbwarez.dk//cygwin32/",
                            "http://cygwin.mbwarez.dk//n/",
                            "http://cygwin.mbwarez.dk//n/ropeZ",
                            "http://cygwin.mbwarez.dk//pub/cygwin/",
                            "http://cygwin.mbwarez.dk//pub/cygwin/P",
                            "http://cygwin.mbwarez.dk/3.com",
                            "http://cygwin.mbwarez.dk/4",
                            "http://cygwin.mbwarez.dk/7",
                            "http://cygwin.mbwarez.dk/:",
                            "http://cygwin.mbwarez.dk/;cygwin.mbwarez.dk;Europe;Denmark;noshow",
                            "http://cygwin.mbwarez.dk/D",
                            "http://cygwin.mbwarez.dk/E",
                            "http://cygwin.mbwarez.dk/Europe",
                            "http://cygwin.mbwarez.dk/F",
                            "http://cygwin.mbwarez.dk/G",
                            "http://cygwin.mbwarez.dk/Hong",
                            "http://cygwin.mbwarez.dk/P",
                            "http://cygwin.mbwarez.dk/Q",
                            "http://cygwin.mbwarez.dk/achen.derg/",
                            "http://cygwin.mbwarez.dk/argasso.net/",
                            "http://cygwin.mbwarez.dk/b",
                            "http://cygwin.mbwarez.dk/boa.pt",
                            "http://cygwin.mbwarez.dk/c",
                            "http://cygwin.mbwarez.dk/c.jpn//",
                            "http://cygwin.mbwarez.dk/cn/cygwin/",
                            "http://cygwin.mbwarez.dk/cn/cygwin/A",
                            "http://cygwin.mbwarez.dk/cn/cygwin/u",
                            "http://cygwin.mbwarez.dk/cyg",
                            "http://cygwin.mbwarez.dk/cygwin/",
                            "http://cygwin.mbwarez.dk/cygwin//s",
                            "http://cygwin.mbwarez.dk/cygwin/:",
                            "http://cygwin.mbwarez.dk/cygwin/gwin/",
                            "http://cygwin.mbwarez.dk/cygwin/ia://",
                            "http://cygwin.mbwarez.dk/cygwin/mir",
                            "http://cygwin.mbwarez.dk/cygwin/n/",
                            "http://cygwin.mbwarez.dk/cygwin/n/A",
                            "http://cygwin.mbwarez.dk/d.com",
                            "http://cygwin.mbwarez.dk/d.comwin/",
                            "http://cygwin.mbwarez.dk/ddos.net/cygwia",
                            "http://cygwin.mbwarez.dk/ent.co",
                            "http://cygwin.mbwarez.dk/er.by/pub/m7",
                            "http://cygwin.mbwarez.dk/et",
                            "http://cygwin.mbwarez.dk/et.fi0",
                            "http://cygwin.mbwarez.dk/et/cygwin/D",
                            "http://cygwin.mbwarez.dk/et/cygwin/u",
                            "http://cygwin.mbwarez.dk/etcygwin/B",
                            "http://cygwin.mbwarez.dk/etoml",
                            "http://cygwin.mbwarez.dk/etworks.org",
                            "http://cygwin.mbwarez.dk/etworks.org/",
                            "http://cygwin.mbwarez.dk/etworks.org/n",
                            "http://cygwin.mbwarez.dk/g/cygwin/",
                            "http://cygwin.mbwarez.dk/g/cygwin/P",
                            "http://cygwin.mbwarez.dk/g/cygwin/cns/cygwin/",
                            "http://cygwin.mbwarez.dk/gwin/",
                            "http://cygwin.mbwarez.dk/gwin/.net/",
                            "http://cygwin.mbwarez.dk/gwin//",
                            "http://cygwin.mbwarez.dk/gwin/2/",
                            "http://cygwin.mbwarez.dk/gwin/Y",
                            "http://cygwin.mbwarez.dk/gwin/h",
                            "http://cygwin.mbwarez.dk/gwin/in/",
                            "http://cygwin.mbwarez.dk/gwin/ror.c",
                            "http://cygwin.mbwarez.dk/gwin/s://",
                            "http://cygwin.mbwarez.dk/gwin/ygwin/m",
                            "http://cygwin.mbwarez.dk/i",
                            "http://cygwin.mbwarez.dk/in/",
                            "http://cygwin.mbwarez.dk/in/.cnn/",
                            "http://cygwin.mbwarez.dk/in//n/B",
                            "http://cygwin.mbwarez.dk/in//win/D",
                            "http://cygwin.mbwarez.dk/in/2",
                            "http://cygwin.mbwarez.dk/in/in/",
                            "http://cygwin.mbwarez.dk/in/in/Y",
                            "http://cygwin.mbwarez.dk/in/n",
                            "http://cygwin.mbwarez.dk/in/n/",
                            "http://cygwin.mbwarez.dk/in/n/://",
                            "http://cygwin.mbwarez.dk/in/win//",
                            "http://cygwin.mbwarez.dk/in/ygwin/",
                            "http://cygwin.mbwarez.dk/inan/n//t",
                            "http://cygwin.mbwarez.dk/inf.tu-dresden",
                            "http://cygwin.mbwarez.dk/inrausch",
                            "http://cygwin.mbwarez.dk/loo.ca",
                            "http://cygwin.mbwarez.dk/m/cygwin/",
                            "http://cygwin.mbwarez.dk/m/cygwin//U",
                            "http://cygwin.mbwarez.dk/m/cygwin/byfl",
                            "http://cygwin.mbwarez.dk/m/cygwin/in/-",
                            "http://cygwin.mbwarez.dk/mirror",
                            "http://cygwin.mbwarez.dk/n/.netrg",
                            "http://cygwin.mbwarez.dk/n///",
                            "http://cygwin.mbwarez.dk/n//gwin/",
                            "http://cygwin.mbwarez.dk/n/Asiame.1",
                            "http://cygwin.mbwarez.dk/n/cygwin/=",
                            "http://cygwin.mbwarez.dk/n/gwin/",
                            "http://cygwin.mbwarez.dk/n/in/c",
                            "http://cygwin.mbwarez.dk/n/win/",
                            "http://cygwin.mbwarez.dk/net/n/",
                            "http://cygwin.mbwarez.dk/nin/",
                            "http://cygwin.mbwarez.dk/o/cygwin/",
                            "http://cygwin.mbwarez.dk/om.com/B",
                            "http://cygwin.mbwarez.dk/om/cygwin/",
                            "http://cygwin.mbwarez.dk/omom/cygwin/",
                            "http://cygwin.mbwarez.dk/org/in/b",
                            "http://cygwin.mbwarez.dk/orggwin/",
                            "http://cygwin.mbwarez.dk/orgrs",
                            "http://cygwin.mbwarez.dk/ost.noz.dkV",
                            "http://cygwin.mbwarez.dk/p",
                            "http://cygwin.mbwarez.dk/ps://mirror-hk",
                            "http://cygwin.mbwarez.dk/pub/cygwin//",
                            "http://cygwin.mbwarez.dk/r.cP",
                            "http://cygwin.mbwarez.dk/rafal.ca/",
                            "http://cygwin.mbwarez.dk/rg/cygwin/",
                            "http://cygwin.mbwarez.dk/rg/sites/sourcC",
                            "http://cygwin.mbwarez.dk/rgP",
                            "http://cygwin.mbwarez.dk/rgasso.net",
                            "http://cygwin.mbwarez.dk/rgasso.net/",
                            "http://cygwin.mbwarez.dk/rks.netn//",
                            "http://cygwin.mbwarez.dk/ropeusch.de/m",
                            "http://cygwin.mbwarez.dk/s/cygwin/",
                            "http://cygwin.mbwarez.dk/s:/p",
                            "http://cygwin.mbwarez.dk/st.comt",
                            "http://cygwin.mbwarez.dk/t",
                            "http://cygwin.mbwarez.dk/t/cygwin//",
                            "http://cygwin.mbwarez.dk/t/cygwin/p",
                            "http://cygwin.mbwarez.dk/tc.edu.cnY",
                            "http://cygwin.mbwarez.dk/tin//in/",
                            "http://cygwin.mbwarez.dk/twaren.net",
                            "http://cygwin.mbwarez.dk/tworks.org/k",
                            "http://cygwin.mbwarez.dk/u.cn/cygwin/$",
                            "http://cygwin.mbwarez.dk/u.cnn/",
                            "http://cygwin.mbwarez.dk/u.cns.orgn/V",
                            "http://cygwin.mbwarez.dk/ua.gr/pub/pc/cn",
                            "http://cygwin.mbwarez.dk/win/",
                            "http://cygwin.mbwarez.dk/win/.redhas",
                            "http://cygwin.mbwarez.dk/win//n/2",
                            "http://cygwin.mbwarez.dk/win/gwin/",
                            "http://cygwin.mbwarez.dk/win/in/Y",
                            "http://cygwin.mbwarez.dk/win/inaUn",
                            "http://cygwin.mbwarez.dk/win/n/",
                            "http://cygwin.mbwarez.dk/win/n/n/",
                            "http://cygwin.mbwarez.dk/win/rg/",
                            "http://cygwin.mbwarez.dk/ygwin/",
                            "http://cygwin.mbwarez.dk/ygwin//",
                            "http://cygwin.mbwarez.dk/ygwin//b",
                            "http://cygwin.mbwarez.dk/ygwin//~",
                            "http://cygwin.mbwarez.dk/ygwin/4",
                            "http://cygwin.mbwarez.dk/ygwin/I",
                            "http://cygwin.mbwarez.dk/ygwin/n/",
                            "http://cygwin.mbwarez.dk/ygwin/r-hk",
                            "http://cygwin.mbwarez.dk://mirrors.ustc",
                            "http://cygwin.mbwarez.dkAsia",
                            "http://cygwin.mbwarez.dkI",
                            "http://cygwin.mbwarez.dkM",
                            "http://cygwin.mbwarez.dkare.org/pub/cyg",
                            "http://cygwin.mbwarez.dkb/cygwin//",
                            "http://cygwin.mbwarez.dkb/cygwin/n/2/",
                            "http://cygwin.mbwarez.dkc",
                            "http://cygwin.mbwarez.dkchen.dee",
                            "http://cygwin.mbwarez.dkcn/cygwin/",
                            "http://cygwin.mbwarez.dkcygwin/",
                            "http://cygwin.mbwarez.dke",
                            "http://cygwin.mbwarez.dken.den/",
                            "http://cygwin.mbwarez.dkeq.uc.pt/softwa",
                            "http://cygwin.mbwarez.dkett.ca",
                            "http://cygwin.mbwarez.dketworks.orgx",
                            "http://cygwin.mbwarez.dkg",
                            "http://cygwin.mbwarez.dkg/cygwin/",
                            "http://cygwin.mbwarez.dkgwin.uib.no/",
                            "http://cygwin.mbwarez.dkgwin/",
                            "http://cygwin.mbwarez.dkgwin/gwin/",
                            "http://cygwin.mbwarez.dkgwin/n//",
                            "http://cygwin.mbwarez.dkgwin/omn//",
                            "http://cygwin.mbwarez.dkh.deks.org/1",
                            "http://cygwin.mbwarez.dkhina",
                            "http://cygwin.mbwarez.dkin/ygwin/",
                            "http://cygwin.mbwarez.dkinraus",
                            "http://cygwin.mbwarez.dkirrors.163.com",
                            "http://cygwin.mbwarez.dkl.jpygwin/",
                            "http://cygwin.mbwarez.dklt.comorg/V",
                            "http://cygwin.mbwarez.dkm/cygwin/",
                            "http://cygwin.mbwarez.dkmcom/cygwin/",
                            "http://cygwin.mbwarez.dkmirror",
                            "http://cygwin.mbwarez.dkn.net"
                        ],
                        "id": "238",
                        "description": "URLs found in memory or binary data"
                    },
                    {
                        "severity": "IMPACT_SEVERITY_INFO",
                        "match_data": [
                            "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\ETCJ2WHM\\mirrors[1].lst"
                        ],
                        "id": "90",
                        "description": "Creates files inside the user directory"
                    },
                    {
                        "id": "198",
                        "match_data": [
                            "HKEY_CURRENT_USER_Classes",
                            "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\SystemCertificates\\AuthRoot"
                        ],
                        "description": "Monitors certain registry keys / values for changes (often done to protect autostart functionality)",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "625",
                        "match_data": [
                            "HTTP traffic on port 443 -> 49717",
                            "HTTP traffic on port 49717 -> 443"
                        ],
                        "description": "Uses HTTPS",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "263",
                        "refs": [
                            {
                                "ref": "#memory_dumps",
                                "value": "file.exe, 00000000.00000002.4637826316.0000000000CCC000.00000004.00000020.00020000.00000000.sdmp, file.exe, 00000000.00000002.4638844961.0000000000D36000.00000004.00000020.00020000.00000000.sdmp"
                            }
                        ],
                        "match_data": [
                            "Hyper-V RAW"
                        ],
                        "description": "May try to detect the virtual machine to hinder analysis (VM artifact strings found in memory)",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "238",
                        "match_data": [
                            "ftp://cygwin.mirror.rafal.ca",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/http://f?",
                            "ftp://ftp.fa",
                            "ftp://ftp.fsn.hu/pub/cygwin/win/",
                            "ftp://ftp.fsn.hu/pub/cygwin/ygwin/https://",
                            "ftp://ftp.funet.fi/pub/mirrors/sourceware.org/pub/cygwin/gwin/https://",
                            "ftp://ftp.halifax.rwth-aachen.de",
                            "ftp://ftp.halifax.rwth-aachen.de/cygwin/",
                            "ftp://ftp.halifax.rwth-aachen.der",
                            "ftp://ftp.halifax.rwth-aachen.des",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/http://f",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/http://m",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/https://",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/https://#",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/ors",
                            "ftp://ftp.inf.tu-dresden.dehttps://",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/http://f",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/http://l",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/https://",
                            "ftp://ftp.kr.freebsd.orgx",
                            "ftp://ftp.kr.freebsd.orgygwin",
                            "ftp://ftp.mirrorservice.org/sites/sourceware.org/pub/cygwin/",
                            "ftp://ftp.n",
                            "ftp://ftp.n1",
                            "ftp://ftp.ntua.gr",
                            "ftp://ftp.ntua.gr/pub/pc/cygwin/r",
                            "ftp://ftp.snt.utwente.nl",
                            "ftp://ftp.snt.utwente.nlix",
                            "ftp://ftp.snt.utwente.nlom",
                            "ftp://ftp.snt.utwente.nlwin/win",
                            "ftp://ftp.yz.yamagata-u.ac.jp/pub/cygwin/ygwin//http",
                            "ftp://ftp.yz.yamagata-u.ac.jphttp://m",
                            "ftp://ftp.yz.yamagata-u.ac.jpin/http:/",
                            "ftp://ftp.yz.yamagata-u.ac.jpp",
                            "ftp://ftp.yz.yamagata-u.ac.jpphttps://c",
                            "ftp://ftp.yz.yamagata-u.ac.jprror",
                            "ftp://linux.rz.ruhr-uni-bochum.de/cygwin/gwin//n/",
                            "ftp://mirror.checkdomain.dehttp://ftp.f",
                            "ftp://mirror.checkdomain.dehttps://",
                            "ftp://mirror.csclub.uwaterloo.ca",
                            "ftp://mirror.datacenter.by/pub/mirrors/cygwin/in/",
                            "ftp://mirror.datacenter.bywin/http://f",
                            "ftp://mirror.easyname.atel",
                            "ftp://mirror.easyname.atftp",
                            "ftp://mirror.internode.on.net/pub/cygwin/http",
                            "ftp://mirror.lagoon.nc/cygwin/r",
                            "ftp://mirror.rise.ph/cygwin/cygwin/http",
                            "ftp://mirrors.dotsrc.org/mirrors/cygwin/https://",
                            "ftp://mirrors.dotsrc.org/mirrors/cygwin/https://mirror",
                            "ftp://mirrors.dotsrc.org/mirrors/cygwin/win/httpsC",
                            "ftp://mirrors.netix.net/cygwin/http://f",
                            "ftp://mirrors.netix.net/cygwin/http://m",
                            "ftp://mirrors.syringanetworks.net/cygwin/https://",
                            "ftp://sourceware.org/ftp://sources.redhat.com/ftp://gcc.gnu.org/",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/https://",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/in/http://w",
                            "ftp://sunsite.icm.edu.plp",
                            "http://acedicom.edicomgroup.com/doc0",
                            "http://acraiz.icpbrasil.gov.br/DPCacraiz.pdf0?",
                            "http://acraiz.icpbrasil.gov.br/LCRacraizv2.crl0",
                            "http://apps.identrust.com/roots/dstrootcax3.p7c0",
                            "http://ca.disig.sk/ca/crl/ca_disig.crl0",
                            "http://certificates.starfieldtech.com/repository/1604",
                            "http://cps.letsencrypt.org0",
                            "http://cps.root-x1.letsencrypt.org0",
                            "http://cps.siths.se/sithsrootcav1.html0",
                            "http://crl.comodoca.com/AAACertificateServices.crl06",
                            "http://crl.defence.gov.au/pki0",
                            "http://crl.identrust.com/DSTROOTCAX3CRL.crl0",
                            "http://crl.oces.trust2408.com/oces.crl0",
                            "http://crl.securetrust.com/STCA.crl0",
                            "http://crl.ssc.lt/root-a/cacrl.crl0",
                            "http://crl.ssc.lt/root-c/cacrl.crl0",
                            "http://crl.xrampsecurity.com/XGCA.crl0",
                            "http://crl1.comsign.co.il/crl/comsignglobalrootca.crl0",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/CABD2A79A1076A31F21D253635CB0",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/authrootstl.cab",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/enI",
                            "http://ctldl.windowsupdate.com:80",
                            "http://ctldl.windowsupdate.com:80/msdownload/update/v3/static/trustedr/en/CABD2A79A1076A31F21D253635",
                            "http://cygwin.cathedral-networks.org",
                            "http://cygwin.cathedral-networks.org.ed",
                            "http://cygwin.cathedral-networks.org.sj",
                            "http://cygwin.cathedral-networks.org/",
                            "http://cygwin.cathedral-networks.org/#5",
                            "http://cygwin.cathedral-networks.org/$",
                            "http://cygwin.cathedral-networks.org/)5",
                            "http://cygwin.cathedral-networks.org/-",
                            "http://cygwin.cathedral-networks.org/-u",
                            "http://cygwin.cathedral-networks.org/.i",
                            "http://cygwin.cathedral-networks.org//",
                            "http://cygwin.cathedral-networks.org///",
                            "http://cygwin.cathedral-networks.org//;",
                            "http://cygwin.cathedral-networks.org//J7",
                            "http://cygwin.cathedral-networks.org//V",
                            "http://cygwin.cathedral-networks.org//c4",
                            "http://cygwin.cathedral-networks.org//f",
                            "http://cygwin.cathedral-networks.org//fU",
                            "http://cygwin.cathedral-networks.org//m",
                            "http://cygwin.cathedral-networks.org/0",
                            "http://cygwin.cathedral-networks.org/5",
                            "http://cygwin.cathedral-networks.org/57I",
                            "http://cygwin.cathedral-networks.org/6",
                            "http://cygwin.cathedral-networks.org/9",
                            "http://cygwin.cathedral-networks.org/:",
                            "http://cygwin.cathedral-networks.org/;",
                            "http://cygwin.cathedral-networks.org/;cygwin.cathedral-networks.org;Europe;Norway;noshow",
                            "http://cygwin.cathedral-networks.org/=",
                            "http://cygwin.cathedral-networks.org/A",
                            "http://cygwin.cathedral-networks.org/B6",
                            "http://cygwin.cathedral-networks.org/D",
                            "http://cygwin.cathedral-networks.org/G",
                            "http://cygwin.cathedral-networks.org/I",
                            "http://cygwin.cathedral-networks.org/I5",
                            "http://cygwin.cathedral-networks.org/I6",
                            "http://cygwin.cathedral-networks.org/K",
                            "http://cygwin.cathedral-networks.org/M",
                            "http://cygwin.cathedral-networks.org/N",
                            "http://cygwin.cathedral-networks.org/N;",
                            "http://cygwin.cathedral-networks.org/S",
                            "http://cygwin.cathedral-networks.org/Un",
                            "http://cygwin.cathedral-networks.org/W0",
                            "http://cygwin.cathedral-networks.org/X",
                            "http://cygwin.cathedral-networks.org/Y",
                            "http://cygwin.cathedral-networks.org/Z",
                            "http://cygwin.cathedral-networks.org/a",
                            "http://cygwin.cathedral-networks.org/aN",
                            "http://cygwin.cathedral-networks.org/aren.net",
                            "http://cygwin.cathedral-networks.org/d",
                            "http://cygwin.cathedral-networks.org/d4t",
                            "http://cygwin.cathedral-networks.org/de",
                            "http://cygwin.cathedral-networks.org/dk",
                            "http://cygwin.cathedral-networks.org/ec",
                            "http://cygwin.cathedral-networks.org/edV",
                            "http://cygwin.cathedral-networks.org/en;",
                            "http://cygwin.cathedral-networks.org/er",
                            "http://cygwin.cathedral-networks.org/fr",
                            "http://cygwin.cathedral-networks.org/ft",
                            "http://cygwin.cathedral-networks.org/ftz",
                            "http://cygwin.cathedral-networks.org/g",
                            "http://cygwin.cathedral-networks.org/ha",
                            "http://cygwin.cathedral-networks.org/i",
                            "http://cygwin.cathedral-networks.org/i-s",
                            "http://cygwin.cathedral-networks.org/ii",
                            "http://cygwin.cathedral-networks.org/in-",
                            "http://cygwin.cathedral-networks.org/k",
                            "http://cygwin.cathedral-networks.org/lb",
                            "http://cygwin.cathedral-networks.org/li",
                            "http://cygwin.cathedral-networks.org/m",
                            "http://cygwin.cathedral-networks.org/mam",
                            "http://cygwin.cathedral-networks.org/mi",
                            "http://cygwin.cathedral-networks.org/n/",
                            "http://cygwin.cathedral-networks.org/no",
                            "http://cygwin.cathedral-networks.org/ork",
                            "http://cygwin.cathedral-networks.org/p",
                            "http://cygwin.cathedral-networks.org/p.k3x",
                            "http://cygwin.cathedral-networks.org/q",
                            "http://cygwin.cathedral-networks.org/ra",
                            "http://cygwin.cathedral-networks.org/ren.net0",
                            "http://cygwin.cathedral-networks.org/rk",
                            "http://cygwin.cathedral-networks.org/s",
                            "http://cygwin.cathedral-networks.org/s/l3",
                            "http://cygwin.cathedral-networks.org/sr",
                            "http://cygwin.cathedral-networks.org/t",
                            "http://cygwin.cathedral-networks.org/t$",
                            "http://cygwin.cathedral-networks.org/te",
                            "http://cygwin.cathedral-networks.org/th",
                            "http://cygwin.cathedral-networks.org/tt",
                            "http://cygwin.cathedral-networks.org/unU",
                            "http://cygwin.cathedral-networks.org/us",
                            "http://cygwin.cathedral-networks.org/w",
                            "http://cygwin.cathedral-networks.org/wa",
                            "http://cygwin.cathedral-networks.org/x",
                            "http://cygwin.cathedral-networks.org/ygX",
                            "http://cygwin.cathedral-networks.org/yn",
                            "http://cygwin.cathedral-networks.org/z6",
                            "http://cygwin.cathedral-networks.org/~",
                            "http://cygwin.cathedral-networks.org2/",
                            "http://cygwin.cathedral-networks.org29I",
                            "http://cygwin.cathedral-networks.org63",
                            "http://cygwin.cathedral-networks.org9",
                            "http://cygwin.cathedral-networks.org://",
                            "http://cygwin.cathedral-networks.orgB2",
                            "http://cygwin.cathedral-networks.orgC",
                            "http://cygwin.cathedral-networks.orgF5",
                            "http://cygwin.cathedral-networks.orgI",
                            "http://cygwin.cathedral-networks.orgI7",
                            "http://cygwin.cathedral-networks.orgL9",
                            "http://cygwin.cathedral-networks.orgN",
                            "http://cygwin.cathedral-networks.orgT6h",
                            "http://cygwin.cathedral-networks.orgZ",
                            "http://cygwin.cathedral-networks.orga-u",
                            "http://cygwin.cathedral-networks.orgain",
                            "http://cygwin.cathedral-networks.orgalaW",
                            "http://cygwin.cathedral-networks.orgb",
                            "http://cygwin.cathedral-networks.orgd",
                            "http://cygwin.cathedral-networks.orge",
                            "http://cygwin.cathedral-networks.orge.",
                            "http://cygwin.cathedral-networks.orgeyq",
                            "http://cygwin.cathedral-networks.orgf",
                            "http://cygwin.cathedral-networks.orgf;t",
                            "http://cygwin.cathedral-networks.orgflyI",
                            "http://cygwin.cathedral-networks.orggwi",
                            "http://cygwin.cathedral-networks.orgia",
                            "http://cygwin.cathedral-networks.orgin/",
                            "http://cygwin.cathedral-networks.orgjp",
                            "http://cygwin.cathedral-networks.orgn/",
                            "http://cygwin.cathedral-networks.orgn/T",
                            "http://cygwin.cathedral-networks.orgnc",
                            "http://cygwin.cathedral-networks.orgnux",
                            "http://cygwin.cathedral-networks.orgon",
                            "http://cygwin.cathedral-networks.orgp.lO3",
                            "http://cygwin.cathedral-networks.orgp/p",
                            "http://cygwin.cathedral-networks.orgr.c",
                            "http://cygwin.cathedral-networks.orgrs.-",
                            "http://cygwin.cathedral-networks.orgsde",
                            "http://cygwin.cathedral-networks.orgt",
                            "http://cygwin.cathedral-networks.orgtac",
                            "http://cygwin.cathedral-networks.orguni",
                            "http://cygwin.cathedral-networks.orguts",
                            "http://cygwin.cathedral-networks.orgwin",
                            "http://cygwin.cathedral-networks.org~",
                            "http://cygwin.cathedral-y",
                            "http://cygwin.mbwarez.dk",
                            "http://cygwin.mbwarez.dk#",
                            "http://cygwin.mbwarez.dk$",
                            "http://cygwin.mbwarez.dk-",
                            "http://cygwin.mbwarez.dk.ac.jp/n/",
                            "http://cygwin.mbwarez.dk.de",
                            "http://cygwin.mbwarez.dk.de.dein/b",
                            "http://cygwin.mbwarez.dk.de/cygwin/.ma",
                            "http://cygwin.mbwarez.dk.de/cygwin//",
                            "http://cygwin.mbwarez.dk.de/cygwin/ter6",
                            "http://cygwin.mbwarez.dk.orgru.com/cyg",
                            "http://cygwin.mbwarez.dk.orguib.no/",
                            "http://cygwin.mbwarez.dk/",
                            "http://cygwin.mbwarez.dk/&",
                            "http://cygwin.mbwarez.dk/.",
                            "http://cygwin.mbwarez.dk/.ac.nz//.",
                            "http://cygwin.mbwarez.dk/.ca//cygwin/9",
                            "http://cygwin.mbwarez.dk/.cn/cygwin//",
                            "http://cygwin.mbwarez.dk/.csclub.uwa",
                            "http://cygwin.mbwarez.dk/.de",
                            "http://cygwin.mbwarez.dk/.de/cygwin/;",
                            "http://cygwin.mbwarez.dk/.internode.Y",
                            "http://cygwin.mbwarez.dk/.net",
                            "http://cygwin.mbwarez.dk/.rise.phj.O",
                            "http://cygwin.mbwarez.dk/.tu",
                            "http://cygwin.mbwarez.dk//",
                            "http://cygwin.mbwarez.dk///",
                            "http://cygwin.mbwarez.dk///in32/",
                            "http://cygwin.mbwarez.dk///sunsite.icm.",
                            "http://cygwin.mbwarez.dk//_",
                            "http://cygwin.mbwarez.dk//c",
                            "http://cygwin.mbwarez.dk//cygwin/",
                            "http://cygwin.mbwarez.dk//cygwin//",
                            "http://cygwin.mbwarez.dk//cygwin///m",
                            "http://cygwin.mbwarez.dk//cygwin//b",
                            "http://cygwin.mbwarez.dk//cygwin/i-L",
                            "http://cygwin.mbwarez.dk//cygwin/t/",
                            "http://cygwin.mbwarez.dk//cygwin32/",
                            "http://cygwin.mbwarez.dk//gwin//",
                            "http://cygwin.mbwarez.dk//in/y",
                            "http://cygwin.mbwarez.dk//n/in/scW",
                            "http://cygwin.mbwarez.dk//n/tps://N",
                            "http://cygwin.mbwarez.dk//sourceware.oT",
                            "http://cygwin.mbwarez.dk//win/://(",
                            "http://cygwin.mbwarez.dk//ygwin/",
                            "http://cygwin.mbwarez.dk/0",
                            "http://cygwin.mbwarez.dk/52",
                            "http://cygwin.mbwarez.dk/:",
                            "http://cygwin.mbwarez.dk/;cygwin.mbwarez.dk;Europe;Denmark;noshow",
                            "http://cygwin.mbwarez.dk/=;2",
                            "http://cygwin.mbwarez.dk/A",
                            "http://cygwin.mbwarez.dk/I",
                            "http://cygwin.mbwarez.dk/P",
                            "http://cygwin.mbwarez.dk/Z",
                            "http://cygwin.mbwarez.dk/alasiaw",
                            "http://cygwin.mbwarez.dk/at/cygwin//",
                            "http://cygwin.mbwarez.dk/aujp",
                            "http://cygwin.mbwarez.dk/auwin/n/",
                            "http://cygwin.mbwarez.dk/auygwin/9",
                            "http://cygwin.mbwarez.dk/b/cygwin/ors.a",
                            "http://cygwin.mbwarez.dk/bly.com/",
                            "http://cygwin.mbwarez.dk/bochum.denc",
                            "http://cygwin.mbwarez.dk/cn/cygwin/",
                            "http://cygwin.mbwarez.dk/cyg",
                            "http://cygwin.mbwarez.dk/cygwin/",
                            "http://cygwin.mbwarez.dk/cygwin//",
                            "http://cygwin.mbwarez.dk/cygwin//m",
                            "http://cygwin.mbwarez.dk/cygwin//n/Y",
                            "http://cygwin.mbwarez.dk/cygwin//w",
                            "http://cygwin.mbwarez.dk/cygwin/;",
                            "http://cygwin.mbwarez.dk/cygwin/g",
                            "http://cygwin.mbwarez.dk/cygwin/gwin/",
                            "http://cygwin.mbwarez.dk/cygwin/ina",
                            "http://cygwin.mbwarez.dk/cygwin/n/",
                            "http://cygwin.mbwarez.dk/cygwin/n/a",
                            "http://cygwin.mbwarez.dk/cygwin/n/sof",
                            "http://cygwin.mbwarez.dk/cygwin/n32/Z4",
                            "http://cygwin.mbwarez.dk/cygwin/nc/W",
                            "http://cygwin.mbwarez.dk/cygwin/r",
                            "http://cygwin.mbwarez.dk/cygwin/wtho",
                            "http://cygwin.mbwarez.dk/de",
                            "http://cygwin.mbwarez.dk/de/cygwin/",
                            "http://cygwin.mbwarez.dk/de/cygwin/ft",
                            "http://cygwin.mbwarez.dk/dein/",
                            "http://cygwin.mbwarez.dk/e.phs",
                            "http://cygwin.mbwarez.dk/et/cygwin/",
                            "http://cygwin.mbwarez.dk/et/cygwin/gwiy7",
                            "http://cygwin.mbwarez.dk/et/cygwin/ttp",
                            "http://cygwin.mbwarez.dk/et://mirrors.s",
                            "http://cygwin.mbwarez.dk/et://www.guts",
                            "http://cygwin.mbwarez.dk/etn/r.easyn",
                            "http://cygwin.mbwarez.dk/etworks.org",
                            "http://cygwin.mbwarez.dk/f",
                            "http://cygwin.mbwarez.dk/fly.bydem$",
                            "http://cygwin.mbwarez.dk/g/cygwin/m",
                            "http://cygwin.mbwarez.dk/garr.iti2g",
                            "http://cygwin.mbwarez.dk/gwin/",
                            "http://cygwin.mbwarez.dk/gwin/(",
                            "http://cygwin.mbwarez.dk/gwin/.de",
                            "http://cygwin.mbwarez.dk/gwin//",
                            "http://cygwin.mbwarez.dk/gwin//sd",
                            "http://cygwin.mbwarez.dk/gwin/a://",
                            "http://cygwin.mbwarez.dk/gwin/edral",
                            "http://cygwin.mbwarez.dk/gwin/in/",
                            "http://cygwin.mbwarez.dk/gwin/n/",
                            "http://cygwin.mbwarez.dk/gwin/o",
                            "http://cygwin.mbwarez.dk/gwin/win/_",
                            "http://cygwin.mbwarez.dk/hen.dein/H",
                            "http://cygwin.mbwarez.dk/in/",
                            "http://cygwin.mbwarez.dk/in//",
                            "http://cygwin.mbwarez.dk/in///",
                            "http://cygwin.mbwarez.dk/in/in/",
                            "http://cygwin.mbwarez.dk/in/in/.ca",
                            "http://cygwin.mbwarez.dk/in/n/n/B",
                            "http://cygwin.mbwarez.dk/isboa.ptG",
                            "http://cygwin.mbwarez.dk/j",
                            "http://cygwin.mbwarez.dk/loo.ca",
                            "http://cygwin.mbwarez.dk/ly.com/rg/e",
                            "http://cygwin.mbwarez.dk/m/cygwin/",
                            "http://cygwin.mbwarez.dk/m/cygwin/-",
                            "http://cygwin.mbwarez.dk/m/cygwin//q",
                            "http://cygwin.mbwarez.dk/mwin/gwin/g",
                            "http://cygwin.mbwarez.dk/n.uib.no/u",
                            "http://cygwin.mbwarez.dk/n/",
                            "http://cygwin.mbwarez.dk/n/cygwin/Y",
                            "http://cygwin.mbwarez.dk/n/gwin/z",
                            "http://cygwin.mbwarez.dk/n/n/et/",
                            "http://cygwin.mbwarez.dk/n/t",
                            "http://cygwin.mbwarez.dk/n/win/",
                            "http://cygwin.mbwarez.dk/n/win/win/V1",
                            "http://cygwin.mbwarez.dk/n/ygwin/",
                            "http://cygwin.mbwarez.dk/nadu.cne",
                            "http://cygwin.mbwarez.dk/netpn",
                            "http://cygwin.mbwarez.dk/ng",
                            "http://cygwin.mbwarez.dk/o",
                            "http://cygwin.mbwarez.dk/ochum.de.jp",
                            "http://cygwin.mbwarez.dk/ode.on.net/Z7",
                            "http://cygwin.mbwarez.dk/om/cygwin/",
                            "http://cygwin.mbwarez.dk/om/cygwin/c",
                            "http://cygwin.mbwarez.dk/omain.de/cygwi",
                            "http://cygwin.mbwarez.dk/omain.deli",
                            "http://cygwin.mbwarez.dk/omm.de/",
                            "http://cygwin.mbwarez.dk/pub/cygwin/",
                            "http://cygwin.mbwarez.dk/pub/software/0",
                            "http://cygwin.mbwarez.dk/rg",
                            "http://cygwin.mbwarez.dk/rg.il",
                            "http://cygwin.mbwarez.dk/rg/88",
                            "http://cygwin.mbwarez.dk/rg/cygwin/",
                            "http://cygwin.mbwarez.dk/rlands",
                            "http://cygwin.mbwarez.dk/rors/cygwin/",
                            "http://cygwin.mbwarez.dk/rror.isoc.o",
                            "http://cygwin.mbwarez.dk/rror/cygwin/",
                            "http://cygwin.mbwarez.dk/rror/cygwin/h",
                            "http://cygwin.mbwarez.dk/rrors.163.com",
                            "http://cygwin.mbwarez.dk/rrors.filigran",
                            "http://cygwin.mbwarez.dk/rrors.neti",
                            "http://cygwin.mbwarez.dk/rs.sjtug.sj",
                            "http://cygwin.mbwarez.dk/s",
                            "http://cygwin.mbwarez.dk/s/cygwin//",
                            "http://cygwin.mbwarez.dk/soft",
                            "http://cygwin.mbwarez.dk/t",
                            "http://cygwin.mbwarez.dk/t/cygwin/",
                            "http://cygwin.mbwarez.dk/t/ks.org",
                            "http://cygwin.mbwarez.dk/tft.edu.cn/cy",
                            "http://cygwin.mbwarez.dk/tp",
                            "http://cygwin.mbwarez.dk/tworks.org/.n",
                            "http://cygwin.mbwarez.dk/u.cn/cygwin/",
                            "http://cygwin.mbwarez.dk/ub/cygwin/I",
                            "http://cygwin.mbwarez.dk/ux.rz.ruhr-un",
                            "http://cygwin.mbwarez.dk/win.uib.no/",
                            "http://cygwin.mbwarez.dk/win/",
                            "http://cygwin.mbwarez.dk/win/.de6",
                            "http://cygwin.mbwarez.dk/win//",
                            "http://cygwin.mbwarez.dk/win/are.or",
                            "http://cygwin.mbwarez.dk/win/gwin/",
                            "http://cygwin.mbwarez.dk/win/ia"
                        ],
                        "description": "URLs found in memory or binary data",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "7058",
                        "match_data": [
                            "8.43.85.97:443 -> 192.168.2.15:49717 version: TLS 1.2"
                        ],
                        "description": "Uses secure TLS version for HTTPS connections",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "description": "Uses HTTPS",
                        "match_data": [
                            "HTTP traffic on port 49698 -> 443",
                            "HTTP traffic on port 443 -> 49698"
                        ],
                        "severity": "IMPACT_SEVERITY_INFO",
                        "id": "625"
                    },
                    {
                        "refs": [
                            {
                                "ref": "#memory_dumps",
                                "value": "file.exe, 00000000.00000002.2766071892.0000000000D26000.00000004.00000020.00020000.00000000.sdmp"
                            },
                            {
                                "ref": "#memory_dumps",
                                "value": "file.exe, 00000000.00000002.2766071892.0000000000D26000.00000004.00000020.00020000.00000000.sdmp, file.exe, 00000000.00000002.2765349898.0000000000CA8000.00000004.00000020.00020000.00000000.sdmp"
                            }
                        ],
                        "description": "May try to detect the virtual machine to hinder analysis (VM artifact strings found in memory)",
                        "match_data": [
                            "Hyper-V RAW{",
                            "Hyper-V RAW"
                        ],
                        "severity": "IMPACT_SEVERITY_INFO",
                        "id": "263"
                    },
                    {
                        "description": "URLs found in memory or binary data",
                        "match_data": [
                            "ftp://cygwin.mirror.rafal.catp",
                            "ftp://ftp.byfly.by/pub/cygwin/irror",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/http://c",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/https://",
                            "ftp://ftp.fau.de/cygwin/",
                            "ftp://ftp.fau.de/cygwin/://mirror.dogado.de",
                            "ftp://ftp.fau.de/cygwin/ygwin/https://",
                            "ftp://ftp.fau.des",
                            "ftp://ftp.fs",
                            "ftp://ftp.fsN",
                            "ftp://ftp.fsn.hu/pub/cygwin/gwin",
                            "ftp://ftp.funet.fi/pub/mirrors/sourceware.org/pub/cygwin//https:///",
                            "ftp://ftp.funet.fi/pub/mirrors/sourceware.org/pub/cygwin/mirror",
                            "ftp://ftp.funet.fi/pub/mirrors/sourceware.org/pub/cygwin/tp",
                            "ftp://ftp.funet.fihttp:",
                            "ftp://ftp.halifax.rwth-aachen.de/cygwin//in",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/de",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/http://l",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/http://m",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/https://",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/https://3",
                            "ftp://ftp.jaist.ac.jp/pub/cygwin/",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/https://",
                            "ftp://ftp.kr.freebsd.orglhttps://",
                            "ftp://ftp.l",
                            "ftp://ftp.lip6.fr/pub/cygwin/https://ft",
                            "ftp://ftp.n",
                            "ftp://ftp.ntua.grhttp:",
                            "ftp://ftp.snt.utwente.nl/pub/software/cygwin/https://",
                            "ftp://ftp.yz.yamagata-u.ac.jp",
                            "ftp://ftp.yz.yamagata-u.ac.jpp",
                            "ftp://mirror.checkdomain.de/cygwin/cygwin",
                            "ftp://mirror.checkdomain.demirror",
                            "ftp://mirror.datacenter.bygchhttp://mZ",
                            "ftp://mirror.datacenter.byhum.de",
                            "ftp://mirror.easyname.at/cygwin/larushttps://",
                            "ftp://mirror.internode.on.net/pub/cygwin/http",
                            "ftp://mirror.lagoon.nc/cygwin/https://I",
                            "ftp://mirrors.dotsrc.org/mirrors/cygwin//cygwin/",
                            "ftp://mirrors.dotsrc.org/mirrors/cygwin/gwin",
                            "ftp://mirrors.dotsrc.org/mirrors/cygwin/http://c/",
                            "ftp://mirrors.dotsrc.org/mirrors/cygwin/https://",
                            "ftp://mirrors.dotsrc.org/mirrors/cygwin/or",
                            "ftp://mirrors.netix.net/cygwin/http://fZ",
                            "ftp://mirrors.sonic.net/cygwin/in/httP",
                            "ftp://mirrors.syringanetworks.net/cygwin/gwin/https://w",
                            "ftp://sourceware.org/ftp://sources.redhat.com/ftp://gcc.gnu.org/",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/https://",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/mirror",
                            "http://ac.economia.gob.mx/cps.html0",
                            "http://ac.economia.gob.mx/last.crl0G",
                            "http://acedicom.edicomgroup.com/doc0",
                            "http://acraiz.icpbrasil.gov.br/DPCacraiz.pdf0?",
                            "http://acraiz.icpbrasil.gov.br/LCRacraizv1.crl0",
                            "http://acraiz.icpbrasil.gov.br/LCRacraizv2.crl0",
                            "http://apps.identrust.com/roots/dstrootcax3.p7c0",
                            "http://ca.disig.sk/ca/crl/ca_disig.crl0",
                            "http://ca.mtin.es/mtin/DPCyPoliticas0",
                            "http://ca.mtin.es/mtin/DPCyPoliticas0g",
                            "http://ca.mtin.es/mtin/crl/MTINAutoridadRaiz03",
                            "http://ca.mtin.es/mtin/ocsp0",
                            "http://ca2.mtin.es/mtin/crl/MTINAutoridadRaiz0",
                            "http://certificates.starfieldtech.com/repository/1604",
                            "http://certs.oati.net/repository/OATICA2.crl0",
                            "http://certs.oati.net/repository/OATICA2.crt0",
                            "http://certs.oaticerts.com/repository/OATICA2.crl",
                            "http://certs.oaticerts.com/repository/OATICA2.crt08",
                            "http://cps.chambersign.org/cps/chambersignroot.html0",
                            "http://cps.chambersign.org/cps/chambersroot.html0",
                            "http://cps.letsencrypt.org0",
                            "http://cps.root-x1.letsencrypt.org0",
                            "http://cps.siths.se/sithsrootcav1.html0",
                            "http://crl.certigna.fr/certignarootca.crl01",
                            "http://crl.chambersign.org/chambersignroot.crl0",
                            "http://crl.chambersign.org/chambersroot.crl0",
                            "http://crl.comodoca.com/AAACertificateServices.crl06",
                            "http://crl.defence.gov.au/pki0",
                            "http://crl.dhimyotis.com/certignarootca.crl0",
                            "http://crl.globalsign.net/root-r2.crl0",
                            "http://crl.identrust.com/DSTROOTCAX3CRL.crl0",
                            "http://crl.oces.trust2408.com/oces.crl0",
                            "http://crl.securetrust.com/SGCA.crl0",
                            "http://crl.securetrust.com/STCA.crl0",
                            "http://crl.ssc.lt/root-a/cacrl.crl0",
                            "http://crl.ssc.lt/root-b/cacrl.crl0",
                            "http://crl.ssc.lt/root-c/cacrl.crl0",
                            "http://crl.xrampsecurity.com/XGCA.crl0",
                            "http://crl1.comsign.co.il/crl/comsignglobalrootca.crl0",
                            "http://ctldl.windowsupdate.com/",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/CABD2A79A1076A31F21D253635CB0",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/authrootstl.cab",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/enR5",
                            "http://ctldl.windowsupdate.com:80/msdownload/update/v3/static/trustedr/en/CABD2A79A1076A31F21D253635",
                            "http://cygwin.cathedral-networks.org",
                            "http://cygwin.cathedral-networks.org.v",
                            "http://cygwin.cathedral-networks.org/",
                            "http://cygwin.cathedral-networks.org/%",
                            "http://cygwin.cathedral-networks.org/)",
                            "http://cygwin.cathedral-networks.org/-",
                            "http://cygwin.cathedral-networks.org/.",
                            "http://cygwin.cathedral-networks.org/.c",
                            "http://cygwin.cathedral-networks.org/.i",
                            "http://cygwin.cathedral-networks.org/.l",
                            "http://cygwin.cathedral-networks.org/.m",
                            "http://cygwin.cathedral-networks.org/.n",
                            "http://cygwin.cathedral-networks.org/.s",
                            "http://cygwin.cathedral-networks.org/.u8",
                            "http://cygwin.cathedral-networks.org//",
                            "http://cygwin.cathedral-networks.org//)",
                            "http://cygwin.cathedral-networks.org///",
                            "http://cygwin.cathedral-networks.org//D",
                            "http://cygwin.cathedral-networks.org//Z",
                            "http://cygwin.cathedral-networks.org//c",
                            "http://cygwin.cathedral-networks.org//f",
                            "http://cygwin.cathedral-networks.org//f:",
                            "http://cygwin.cathedral-networks.org//ftp.ntu.edu.twI",
                            "http://cygwin.cathedral-networks.org//l",
                            "http://cygwin.cathedral-networks.org//m",
                            "http://cygwin.cathedral-networks.org//u",
                            "http://cygwin.cathedral-networks.org/8",
                            "http://cygwin.cathedral-networks.org/9",
                            "http://cygwin.cathedral-networks.org/;cygwin.cathedral-networks.org;Europe;Norway;noshow",
                            "http://cygwin.cathedral-networks.org/B",
                            "http://cygwin.cathedral-networks.org/C",
                            "http://cygwin.cathedral-networks.org/F",
                            "http://cygwin.cathedral-networks.org/G",
                            "http://cygwin.cathedral-networks.org/K",
                            "http://cygwin.cathedral-networks.org/L",
                            "http://cygwin.cathedral-networks.org/X",
                            "http://cygwin.cathedral-networks.org/Z",
                            "http://cygwin.cathedral-networks.org/a",
                            "http://cygwin.cathedral-networks.org/an",
                            "http://cygwin.cathedral-networks.org/at3",
                            "http://cygwin.cathedral-networks.org/c",
                            "http://cygwin.cathedral-networks.org/ck",
                            "http://cygwin.cathedral-networks.org/cy",
                            "http://cygwin.cathedral-networks.org/d",
                            "http://cygwin.cathedral-networks.org/dO",
                            "http://cygwin.cathedral-networks.org/e",
                            "http://cygwin.cathedral-networks.org/e.",
                            "http://cygwin.cathedral-networks.org/ee.",
                            "http://cygwin.cathedral-networks.org/en",
                            "http://cygwin.cathedral-networks.org/f",
                            "http://cygwin.cathedral-networks.org/fr",
                            "http://cygwin.cathedral-networks.org/fs",
                            "http://cygwin.cathedral-networks.org/ft",
                            "http://cygwin.cathedral-networks.org/g",
                            "http://cygwin.cathedral-networks.org/h",
                            "http://cygwin.cathedral-networks.org/hti",
                            "http://cygwin.cathedral-networks.org/i",
                            "http://cygwin.cathedral-networks.org/ic",
                            "http://cygwin.cathedral-networks.org/in",
                            "http://cygwin.cathedral-networks.org/ir",
                            "http://cygwin.cathedral-networks.org/m",
                            "http://cygwin.cathedral-networks.org/mG",
                            "http://cygwin.cathedral-networks.org/ma/",
                            "http://cygwin.cathedral-networks.org/mi",
                            "http://cygwin.cathedral-networks.org/miK",
                            "http://cygwin.cathedral-networks.org/n",
                            "http://cygwin.cathedral-networks.org/n/",
                            "http://cygwin.cathedral-networks.org/ni",
                            "http://cygwin.cathedral-networks.org/o",
                            "http://cygwin.cathedral-networks.org/oo",
                            "http://cygwin.cathedral-networks.org/ot",
                            "http://cygwin.cathedral-networks.org/p",
                            "http://cygwin.cathedral-networks.org/p:",
                            "http://cygwin.cathedral-networks.org/q",
                            "http://cygwin.cathedral-networks.org/r",
                            "http://cygwin.cathedral-networks.org/ro",
                            "http://cygwin.cathedral-networks.org/rs",
                            "http://cygwin.cathedral-networks.org/s.",
                            "http://cygwin.cathedral-networks.org/sj",
                            "http://cygwin.cathedral-networks.org/su",
                            "http://cygwin.cathedral-networks.org/tp",
                            "http://cygwin.cathedral-networks.org/tt",
                            "http://cygwin.cathedral-networks.org/u",
                            "http://cygwin.cathedral-networks.org/um",
                            "http://cygwin.cathedral-networks.org/v",
                            "http://cygwin.cathedral-networks.org/w",
                            "http://cygwin.cathedral-networks.org/wa(",
                            "http://cygwin.cathedral-networks.org0",
                            "http://cygwin.cathedral-networks.org6",
                            "http://cygwin.cathedral-networks.org;",
                            "http://cygwin.cathedral-networks.orgE",
                            "http://cygwin.cathedral-networks.orgH",
                            "http://cygwin.cathedral-networks.orgL",
                            "http://cygwin.cathedral-networks.orgR",
                            "http://cygwin.cathedral-networks.orgT",
                            "http://cygwin.cathedral-networks.orga",
                            "http://cygwin.cathedral-networks.orgb/c",
                            "http://cygwin.cathedral-networks.orgcew",
                            "http://cygwin.cathedral-networks.orgcom",
                            "http://cygwin.cathedral-networks.orgcyg",
                            "http://cygwin.cathedral-networks.orgn/",
                            "http://cygwin.cathedral-networks.orgom",
                            "http://cygwin.cathedral-networks.orgorg3",
                            "http://cygwin.cathedral-networks.orgror%",
                            "http://cygwin.cathedral-networks.orgsde",
                            "http://cygwin.cathedral-networks.orgt",
                            "http://cygwin.cathedral-networks.orgtp:",
                            "http://cygwin.cathedral-networks.orgtpsP",
                            "http://cygwin.cathedral-networks.orgtsc",
                            "http://cygwin.cathedral-networks.orguts",
                            "http://cygwin.cathedral-networks.orgwin",
                            "http://cygwin.cathedral-networks.orgxmi",
                            "http://cygwin.mbwarez",
                            "http://cygwin.mbwarez.dk",
                            "http://cygwin.mbwarez.dk.by.fr-",
                            "http://cygwin.mbwarez.dk.byfly.byo?",
                            "http://cygwin.mbwarez.dk.den/win//:",
                            "http://cygwin.mbwarez.dk.koddos.netet5",
                            "http://cygwin.mbwarez.dk.netgwin/g/",
                            "http://cygwin.mbwarez.dk.netpt",
                            "http://cygwin.mbwarez.dk.ntu.edu.tw/pub",
                            "http://cygwin.mbwarez.dk.rnl.tecnico.ulB",
                            "http://cygwin.mbwarez.dk/",
                            "http://cygwin.mbwarez.dk/%",
                            "http://cygwin.mbwarez.dk/(",
                            "http://cygwin.mbwarez.dk/-",
                            "http://cygwin.mbwarez.dk/.ca/",
                            "http://cygwin.mbwarez.dk/.ca/afal.ca?",
                            "http://cygwin.mbwarez.dk/.cn/cygwin/ft",
                            "http://cygwin.mbwarez.dk/.cnwin/n/",
                            "http://cygwin.mbwarez.dk/.com/cygwin/",
                            "http://cygwin.mbwarez.dk/.de/cygwin/gw",
                            "http://cygwin.mbwarez.dk/.edu.cnJ",
                            "http://cygwin.mbwarez.dk/.hunet",
                            "http://cygwin.mbwarez.dk/.netin/n.net",
                            "http://cygwin.mbwarez.dk/.nz/",
                            "http://cygwin.mbwarez.dk/.sjtu.edu.c",
                            "http://cygwin.mbwarez.dk/.ustc.edu.$",
                            "http://cygwin.mbwarez.dk//",
                            "http://cygwin.mbwarez.dk///",
                            "http://cygwin.mbwarez.dk///mirrors.dots",
                            "http://cygwin.mbwarez.dk///tps://",
                            "http://cygwin.mbwarez.dk//0e",
                            "http://cygwin.mbwarez.dk//cygwin/",
                            "http://cygwin.mbwarez.dk//cygwin/$",
                            "http://cygwin.mbwarez.dk//cygwin/.d",
                            "http://cygwin.mbwarez.dk//cygwin//",
                            "http://cygwin.mbwarez.dk//cygwin/O",
                            "http://cygwin.mbwarez.dk//cygwin32/",
                            "http://cygwin.mbwarez.dk//gwin/",
                            "http://cygwin.mbwarez.dk//gwin//",
                            "http://cygwin.mbwarez.dk//in/ca/",
                            "http://cygwin.mbwarez.dk//in/win/",
                            "http://cygwin.mbwarez.dk//mirror.koddos5",
                            "http://cygwin.mbwarez.dk//mn/",
                            "http://cygwin.mbwarez.dk//n/et",
                            "http://cygwin.mbwarez.dk//n/w.gutscheinrausch.de/mirror/cygwin/",
                            "http://cygwin.mbwarez.dk//pub/cygwin/",
                            "http://cygwin.mbwarez.dk//win/.",
                            "http://cygwin.mbwarez.dk/0",
                            "http://cygwin.mbwarez.dk/2",
                            "http://cygwin.mbwarez.dk/3",
                            "http://cygwin.mbwarez.dk/7J",
                            "http://cygwin.mbwarez.dk/;cygwin.mbwarez.dk;Europe;Denmark;noshow",
                            "http://cygwin.mbwarez.dk/Asiaon",
                            "http://cygwin.mbwarez.dk/B",
                            "http://cygwin.mbwarez.dk/E",
                            "http://cygwin.mbwarez.dk/Europec",
                            "http://cygwin.mbwarez.dk/North",
                            "http://cygwin.mbwarez.dk/Norway",
                            "http://cygwin.mbwarez.dk/Poland.",
                            "http://cygwin.mbwarez.dk/V)",
                            "http://cygwin.mbwarez.dk/achen.de1",
                            "http://cygwin.mbwarez.dk/aledonia",
                            "http://cygwin.mbwarez.dk/ant.com",
                            "http://cygwin.mbwarez.dk/b",
                            "http://cygwin.mbwarez.dk/b/cygwin/te.n",
                            "http://cygwin.mbwarez.dk/chen.",
                            "http://cygwin.mbwarez.dk/chum.de",
                            "http://cygwin.mbwarez.dk/cn/cygwin/",
                            "http://cygwin.mbwarez.dk/com/cygwin/d",
                            "http://cygwin.mbwarez.dk/cyg",
                            "http://cygwin.mbwarez.dk/cygwin/",
                            "http://cygwin.mbwarez.dk/cygwin/(",
                            "http://cygwin.mbwarez.dk/cygwin//",
                            "http://cygwin.mbwarez.dk/cygwin//.",
                            "http://cygwin.mbwarez.dk/cygwin//9",
                            "http://cygwin.mbwarez.dk/cygwin//b",
                            "http://cygwin.mbwarez.dk/cygwin/7",
                            "http://cygwin.mbwarez.dk/cygwin/://",
                            "http://cygwin.mbwarez.dk/cygwin/A",
                            "http://cygwin.mbwarez.dk/cygwin/I",
                            "http://cygwin.mbwarez.dk/cygwin/n/n/",
                            "http://cygwin.mbwarez.dk/cygwin/rror.l",
                            "http://cygwin.mbwarez.dk/cygwin32/",
                            "http://cygwin.mbwarez.dk/d.com",
                            "http://cygwin.mbwarez.dk/d.comwin/on",
                            "http://cygwin.mbwarez.dk/de/cygwin/",
                            "http://cygwin.mbwarez.dk/de/cygwin/tsr",
                            "http://cygwin.mbwarez.dk/deygwin/(",
                            "http://cygwin.mbwarez.dk/e",
                            "http://cygwin.mbwarez.dk/e/cygwin/",
                            "http://cygwin.mbwarez.dk/e/cygwin/in/",
                            "http://cygwin.mbwarez.dk/e/software/win",
                            "http://cygwin.mbwarez.dk/ebsd.orgc.jp",
                            "http://cygwin.mbwarez.dk/et/cygwin/",
                            "http://cygwin.mbwarez.dk/et/cygwin/y",
                            "http://cygwin.mbwarez.dk/etcygwin/",
                            "http://cygwin.mbwarez.dk/etworks.org)",
                            "http://cygwin.mbwarez.dk/etworks.org/",
                            "http://cygwin.mbwarez.dk/f",
                            "http://cygwin.mbwarez.dk/ftp://mi",
                            "http://cygwin.mbwarez.dk/g/cygwin/",
                            "http://cygwin.mbwarez.dk/g/cygwin/:",
                            "http://cygwin.mbwarez.dk/gasso.netd",
                            "http://cygwin.mbwarez.dk/gwin",
                            "http://cygwin.mbwarez.dk/gwin/",
                            "http://cygwin.mbwarez.dk/gwin///",
                            "http://cygwin.mbwarez.dk/gwin/gwin/",
                            "http://cygwin.mbwarez.dk/gwin/n/",
                            "http://cygwin.mbwarez.dk/gwin/n//m",
                            "http://cygwin.mbwarez.dk/gwin/n/x",
                            "http://cygwin.mbwarez.dk/gwin/o.net/K",
                            "http://cygwin.mbwarez.dk/gwin/ps://w",
                            "http://cygwin.mbwarez.dk/gwin/t",
                            "http://cygwin.mbwarez.dk/gwin/win/",
                            "http://cygwin.mbwarez.dk/gygwin/#",
                            "http://cygwin.mbwarez.dk/h.de//n/",
                            "http://cygwin.mbwarez.dk/h.deEurope",
                            "http://cygwin.mbwarez.dk/hen.de",
                            "http://cygwin.mbwarez.dk/https://",
                            "http://cygwin.mbwarez.dk/hum.degwin/&",
                            "http://cygwin.mbwarez.dk/in/",
                            "http://cygwin.mbwarez.dk/in//",
                            "http://cygwin.mbwarez.dk/in//Q",
                            "http://cygwin.mbwarez.dk/in//win/$",
                            "http://cygwin.mbwarez.dk/in/cygwin/",
                            "http://cygwin.mbwarez.dk/in/cygwin/E",
                            "http://cygwin.mbwarez.dk/in/cygwin/che",
                            "http://cygwin.mbwarez.dk/in/gwin/",
                            "http://cygwin.mbwarez.dk/in/in/",
                            "http://cygwin.mbwarez.dk/in/in/t.e~",
                            "http://cygwin.mbwarez.dk/in/p.br/cy",
                            "http://cygwin.mbwarez.dk/in/tp://ftp.l",
                            "http://cygwin.mbwarez.dk/in/win/",
                            "http://cygwin.mbwarez.dk/in/win/W",
                            "http://cygwin.mbwarez.dk/in/ygwin/I",
                            "http://cygwin.mbwarez.dk/in/ygwin/a",
                            "http://cygwin.mbwarez.dk/isboa.pt/pub/c",
                            "http://cygwin.mbwarez.dk/ited",
                            "http://cygwin.mbwarez.dk/k",
                            "http://cygwin.mbwarez.dk/l",
                            "http://cygwin.mbwarez.dk/m/cygwin/",
                            "http://cygwin.mbwarez.dk/m/cygwin/://cy",
                            "http://cygwin.mbwarez.dk/min/Av",
                            "http://cygwin.mbwarez.dk/n.viem-it.n",
                            "http://cygwin.mbwarez.dk/n/",
                            "http://cygwin.mbwarez.dk/n/cygwin/",
                            "http://cygwin.mbwarez.dk/n/gwi",
                            "http://cygwin.mbwarez.dk/n/in32/",
                            "http://cygwin.mbwarez.dk/n/win/",
                            "http://cygwin.mbwarez.dk/n?",
                            "http://cygwin.mbwarez.dk/ncent.comcom",
                            "http://cygwin.mbwarez.dk/ng",
                            "http://cygwin.mbwarez.dk/no/cygwin/",
                            "http://cygwin.mbwarez.dk/ogwin/",
                            "http://cygwin.mbwarez.dk/om/cygwin/",
                            "http://cygwin.mbwarez.dk/om/cygwin/(",
                            "http://cygwin.mbwarez.dk/om/cygwin/J",
                            "http://cygwin.mbwarez.dk/om/cygwin/P",
                            "http://cygwin.mbwarez.dk/om/cygwin/n/",
                            "http://cygwin.mbwarez.dk/omain.de",
                            "http://cygwin.mbwarez.dk/oo",
                            "http://cygwin.mbwarez.dk/ope1",
                            "http://cygwin.mbwarez.dk/or.checkdomain",
                            "http://cygwin.mbwarez.dk/orgb/cygwin/",
                            "http://cygwin.mbwarez.dk/orgomgwin/I",
                            "http://cygwin.mbwarez.dk/ors.do",
                            "http://cygwin.mbwarez.dk/p",
                            "http://cygwin.mbwarez.dk/p.fau.depdu",
                            "http://cygwin.mbwarez.dk/p.funet.fi/pub",
                            "http://cygwin.mbwarez.dk/pub/cygwin/",
                            "http://cygwin.mbwarez.dk/pub/cygwin/ft",
                            "http://cygwin.mbwarez.dk/r-hk.koddos",
                            "http://cygwin.mbwarez.dk/rafal.ca/S",
                            "http://cygwin.mbwarez.dk/rg/cygwin/",
                            "http://cygwin.mbwarez.dk/rg/pub/cygw",
                            "http://cygwin.mbwarez.dk/rgasso.net",
                            "http://cygwin.mbwarez.dk/rgasso.net/R",
                            "http://cygwin.mbwarez.dk/rloo.canet/",
                            "http://cygwin.mbwarez.dk/rrors.163.com",
                            "http://cygwin.mbwarez.dk/rz.ruhr-uni",
                            "http://cygwin.mbwarez.dk/s.netix.net",
                            "http://cygwin.mbwarez.dk/s/cygwin/",
                            "http://cygwin.mbwarez.dk/stralasiaagoo",
                            "http://cygwin.mbwarez.dk/t",
                            "http://cygwin.mbwarez.dk/t.comgwin/",
                            "http://cygwin.mbwarez.dk/t/cygwin/",
                            "http://cygwin.mbwarez.dk/t/cygwin/Unix/sourceware.org/cygwin//n/",
                            "http://cygwin.mbwarez.dk/t/cygwin/Y",
                            "http://cygwin.mbwarez.dk/t/cygwin/n/",
                            "http://cygwin.mbwarez.dk/tc.edu.cn",
                            "http://cygwin.mbwarez.dk/tgwin//usL",
                            "http://cygwin.mbwarez.dk/tn/://ftp.ha6",
                            "http://cygwin.mbwarez.dk/tp://ftp.fa"
                        ],
                        "severity": "IMPACT_SEVERITY_INFO",
                        "id": "238"
                    },
                    {
                        "description": "Uses secure TLS version for HTTPS connections",
                        "match_data": [
                            "8.43.85.97:443 -> 192.168.2.13:49698 version: TLS 1.2"
                        ],
                        "severity": "IMPACT_SEVERITY_INFO",
                        "id": "7058"
                    },
                    {
                        "severity": "IMPACT_SEVERITY_INFO",
                        "match_data": [
                            "HTTP traffic on port 443 -> 49711",
                            "HTTP traffic on port 49711 -> 443"
                        ],
                        "id": "625",
                        "description": "Uses HTTPS"
                    },
                    {
                        "severity": "IMPACT_SEVERITY_INFO",
                        "refs": [
                            {
                                "ref": "#memory_dumps",
                                "value": "program.exe, 00000000.00000002.4532740386.0000000000D67000.00000004.00000020.00020000.00000000.sdmp, program.exe, 00000000.00000002.4532069778.0000000000D1C000.00000004.00000020.00020000.00000000.sdmp"
                            }
                        ],
                        "match_data": [
                            "Hyper-V RAW"
                        ],
                        "id": "263",
                        "description": "May try to detect the virtual machine to hinder analysis (VM artifact strings found in memory)"
                    },
                    {
                        "severity": "IMPACT_SEVERITY_INFO",
                        "match_data": [
                            "ftp://cygwin.mirror.rafal.ca",
                            "ftp://cygwin.mirror.rafal.caors",
                            "ftp://ftp-stud.hs-esslingen.de/pub/Mirrors/sources.redhat.com/cygwin/http://m",
                            "ftp://ftp-stud.hs-esslingen.deors",
                            "ftp://ftp-stud.hs-esslingen.deror",
                            "ftp://ftp.0",
                            "ftp://ftp.I?",
                            "ftp://ftp.byfly.by/pub/cygwin/",
                            "ftp://ftp.byfly.by/pub/cygwin//",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/http://f-",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/http://li60",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/http://m",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/https://",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/rs",
                            "ftp://ftp.fau.de",
                            "ftp://ftp.fau.de/cygwin/me",
                            "ftp://ftp.fs",
                            "ftp://ftp.fsn.hu/pub/cygwin/https://",
                            "ftp://ftp.fsn.hu/pub/cygwin/oc",
                            "ftp://ftp.fsn.hur",
                            "ftp://ftp.fst",
                            "ftp://ftp.ha",
                            "ftp://ftp.halifax.rwth-aachen.de",
                            "ftp://ftp.halifax.rwth-aachen.de/cygwin/",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/http://f",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/http://m",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/or",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/r",
                            "ftp://ftp.inf.tu-dresden.de/software/windows/cygwin32/http://m",
                            "ftp://ftp.inf.tu-dresden.demirror",
                            "ftp://ftp.jaist.ac.jp/pub/cygwin/https:",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/http://cj",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/http://mK1",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/https://",
                            "ftp://ftp.l",
                            "ftp://ftp.lip6.fr/pub/cygwin/",
                            "ftp://ftp.lip6.fr/pub/cygwin/http://f",
                            "ftp://ftp.lip6.fr/pub/cygwin/http://m~",
                            "ftp://ftp.lip6.fr/pub/cygwin/or",
                            "ftp://ftp.lip6.fr/pub/cygwin/p",
                            "ftp://ftp.lip6.fr/pub/cygwin/win",
                            "ftp://ftp.m",
                            "ftp://ftp.mirrorservice.org",
                            "ftp://ftp.n",
                            "ftp://ftp.np",
                            "ftp://ftp.ntu.edu.tw/pub/cygwin/",
                            "ftp://ftp.ntu.edu.tw/pub/cygwin//",
                            "ftp://ftp.ntua.gr",
                            "ftp://ftp.rnl.tecnico.ulisboa.pt",
                            "ftp://ftp.rnl.tecnico.ulisboa.pt/pub/cygwin/n/n",
                            "ftp://ftp.snt.utwente.nl/pub/software/cygwin/",
                            "ftp://ftp.snt.utwente.nlmcygwin",
                            "ftp://ftp.twaren.net/Unix/sourceware.org/cygwin/https::4",
                            "ftp://ftp.yz.yamagata-u.ac.jp/pub/cygwin/",
                            "ftp://ftp.yz.yamagata-u.ac.jp/pub/cygwin/p",
                            "ftp://ftp.yz.yamagata-u.ac.jpor",
                            "ftp://linux.rz.ruhr-uni-bochum.de",
                            "ftp://mirror.checkdomain.de/cygwin/",
                            "ftp://mirror.checkdomain.de/cygwin/http://c?",
                            "ftp://mirror.checkdomain.de/cygwin/in/http://l",
                            "ftp://mirror.checkdomain.decygwin/httpY",
                            "ftp://mirror.checkdomain.dehttp://mirro",
                            "ftp://mirror.checkdomain.deirrors",
                            "ftp://mirror.cs.vt.edu/pub/cygwin/cygwin/",
                            "ftp://mirror.csclub.uwaterloo.ca/cygwin/httP",
                            "ftp://mirror.datacenter.by/pub/mirrors/cygwin/http://c",
                            "ftp://mirror.datacenter.byhttp://f",
                            "ftp://mirror.easyname.atz",
                            "ftp://mirror.internode.on.net/pub/cygwin/ygwin/",
                            "ftp://mirror.rise.ph/cygwin/cygwin/httpF4",
                            "ftp://mirrors.dotsrc.org/mirrors/cygwin/st",
                            "ftp://mirrors.netix.net/cygwin/",
                            "ftp://mirrors.netix.net/cygwin//",
                            "ftp://mirrors.netix.net/cygwin/https://~",
                            "ftp://mirrors.netix.net/cygwin/or",
                            "ftp://mirrors.syringanetworks.net/cygwin/in/rs",
                            "ftp://sourceware.org/ftp://sources.redhat.com/ftp://gcc.gnu.org/",
                            "ftp://sunsite.icm.edu.pl",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/http://ml",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/ygwin",
                            "ftp://sunsite.icm.edu.plhinahttp://ftp",
                            "ftp://sunsite.icm.edu.plhttp://f",
                            "ftp://sunsite.icm.edu.plnorg",
                            "http://apps.identrust.com/roots/dstrootcax3.p7c0",
                            "http://cps.letsencrypt.org0",
                            "http://cps.root-x1.letsencrypt.org0",
                            "http://crl.identrust.com/DSTROOTCAX3CRL.crl0",
                            "http://cygwin.ca",
                            "http://cygwin.cathedral-",
                            "http://cygwin.cathedral-networks.org",
                            "http://cygwin.cathedral-networks.org(",
                            "http://cygwin.cathedral-networks.org-",
                            "http://cygwin.cathedral-networks.org/",
                            "http://cygwin.cathedral-networks.org/%",
                            "http://cygwin.cathedral-networks.org/&",
                            "http://cygwin.cathedral-networks.org/.",
                            "http://cygwin.cathedral-networks.org//",
                            "http://cygwin.cathedral-networks.org//&",
                            "http://cygwin.cathedral-networks.org///",
                            "http://cygwin.cathedral-networks.org//N)",
                            "http://cygwin.cathedral-networks.org//Z",
                            "http://cygwin.cathedral-networks.org//b5",
                            "http://cygwin.cathedral-networks.org//c",
                            "http://cygwin.cathedral-networks.org//f",
                            "http://cygwin.cathedral-networks.org//fy",
                            "http://cygwin.cathedral-networks.org//i6",
                            "http://cygwin.cathedral-networks.org//m",
                            "http://cygwin.cathedral-networks.org/0",
                            "http://cygwin.cathedral-networks.org/1",
                            "http://cygwin.cathedral-networks.org/2/",
                            "http://cygwin.cathedral-networks.org/5G",
                            "http://cygwin.cathedral-networks.org/9/",
                            "http://cygwin.cathedral-networks.org/96",
                            "http://cygwin.cathedral-networks.org/9?",
                            "http://cygwin.cathedral-networks.org/;cygwin.cathedral-networks.org;Europe;Norway;noshow",
                            "http://cygwin.cathedral-networks.org/=",
                            "http://cygwin.cathedral-networks.org/A6",
                            "http://cygwin.cathedral-networks.org/C",
                            "http://cygwin.cathedral-networks.org/D",
                            "http://cygwin.cathedral-networks.org/G",
                            "http://cygwin.cathedral-networks.org/K(",
                            "http://cygwin.cathedral-networks.org/M",
                            "http://cygwin.cathedral-networks.org/P",
                            "http://cygwin.cathedral-networks.org/S(",
                            "http://cygwin.cathedral-networks.org/S.",
                            "http://cygwin.cathedral-networks.org/T",
                            "http://cygwin.cathedral-networks.org/T&",
                            "http://cygwin.cathedral-networks.org/U23",
                            "http://cygwin.cathedral-networks.org/X",
                            "http://cygwin.cathedral-networks.org/Y",
                            "http://cygwin.cathedral-networks.org/an:",
                            "http://cygwin.cathedral-networks.org/b/",
                            "http://cygwin.cathedral-networks.org/c",
                            "http://cygwin.cathedral-networks.org/c4/",
                            "http://cygwin.cathedral-networks.org/cn",
                            "http://cygwin.cathedral-networks.org/cy",
                            "http://cygwin.cathedral-networks.org/d",
                            "http://cygwin.cathedral-networks.org/e",
                            "http://cygwin.cathedral-networks.org/fr",
                            "http://cygwin.cathedral-networks.org/ft",
                            "http://cygwin.cathedral-networks.org/fts5",
                            "http://cygwin.cathedral-networks.org/h7",
                            "http://cygwin.cathedral-networks.org/ir",
                            "http://cygwin.cathedral-networks.org/l",
                            "http://cygwin.cathedral-networks.org/m",
                            "http://cygwin.cathedral-networks.org/m)",
                            "http://cygwin.cathedral-networks.org/m/",
                            "http://cygwin.cathedral-networks.org/mU",
                            "http://cygwin.cathedral-networks.org/mi",
                            "http://cygwin.cathedral-networks.org/mir4",
                            "http://cygwin.cathedral-networks.org/n&",
                            "http://cygwin.cathedral-networks.org/n.",
                            "http://cygwin.cathedral-networks.org/niK/",
                            "http://cygwin.cathedral-networks.org/o",
                            "http://cygwin.cathedral-networks.org/p",
                            "http://cygwin.cathedral-networks.org/rg",
                            "http://cygwin.cathedral-networks.org/s.",
                            "http://cygwin.cathedral-networks.org/s2",
                            "http://cygwin.cathedral-networks.org/sj",
                            "http://cygwin.cathedral-networks.org/sl",
                            "http://cygwin.cathedral-networks.org/t",
                            "http://cygwin.cathedral-networks.org/tsH",
                            "http://cygwin.cathedral-networks.org/u",
                            "http://cygwin.cathedral-networks.org/u.",
                            "http://cygwin.cathedral-networks.org/x",
                            "http://cygwin.cathedral-networks.org/z",
                            "http://cygwin.cathedral-networks.org/z%",
                            "http://cygwin.cathedral-networks.org/~",
                            "http://cygwin.cathedral-networks.org8",
                            "http://cygwin.cathedral-networks.orgA6",
                            "http://cygwin.cathedral-networks.orgC",
                            "http://cygwin.cathedral-networks.orgH",
                            "http://cygwin.cathedral-networks.orgK?",
                            "http://cygwin.cathedral-networks.orgS/",
                            "http://cygwin.cathedral-networks.orgW)",
                            "http://cygwin.cathedral-networks.org_2=",
                            "http://cygwin.cathedral-networks.orgd%",
                            "http://cygwin.cathedral-networks.orgdet5",
                            "http://cygwin.cathedral-networks.orgha",
                            "http://cygwin.cathedral-networks.orghtt",
                            "http://cygwin.cathedral-networks.orgk",
                            "http://cygwin.cathedral-networks.orgk3",
                            "http://cygwin.cathedral-networks.orgmi(q",
                            "http://cygwin.cathedral-networks.orgn/",
                            "http://cygwin.cathedral-networks.orgn/N6",
                            "http://cygwin.cathedral-networks.orgoft",
                            "http://cygwin.cathedral-networks.orgorg",
                            "http://cygwin.cathedral-networks.orgp/p",
                            "http://cygwin.cathedral-networks.orgq",
                            "http://cygwin.cathedral-networks.orgrro",
                            "http://cygwin.cathedral-networks.orgsyn",
                            "http://cygwin.cathedral-networks.orgtp.",
                            "http://cygwin.cathedral-networks.orgttp&",
                            "http://cygwin.cathedral-networks.orgu",
                            "http://cygwin.cathedral-networks.orguwa",
                            "http://cygwin.cathedral-networks.orgw",
                            "http://cygwin.cathedral-networks.orgwar",
                            "http://cygwin.cathedral-networks.orgx",
                            "http://cygwin.cathedral-networks.orgy3&",
                            "http://cygwin.cathedral-networks.orgygw",
                            "http://cygwin.cathedral-networks.orgz",
                            "http://cygwin.cathedral-t5",
                            "http://cygwin.mbwarez",
                            "http://cygwin.mbwarez.dk",
                            "http://cygwin.mbwarez.dk$",
                            "http://cygwin.mbwarez.dk$I)",
                            "http://cygwin.mbwarez.dk.ac.jpor",
                            "http://cygwin.mbwarez.dk.augwin//",
                            "http://cygwin.mbwarez.dk.by/pub/mirrors",
                            "http://cygwin.mbwarez.dk.cab/cygwin/v",
                            "http://cygwin.mbwarez.dk.iij.ad.jp/pub/",
                            "http://cygwin.mbwarez.dk.netm",
                            "http://cygwin.mbwarez.dk.orgin/",
                            "http://cygwin.mbwarez.dk/",
                            "http://cygwin.mbwarez.dk/#",
                            "http://cygwin.mbwarez.dk/%",
                            "http://cygwin.mbwarez.dk/&",
                            "http://cygwin.mbwarez.dk/)",
                            "http://cygwin.mbwarez.dk/-uni-bochum",
                            "http://cygwin.mbwarez.dk/.can/org/",
                            "http://cygwin.mbwarez.dk/.cn/cygwin/i/",
                            "http://cygwin.mbwarez.dk/.cnom/",
                            "http://cygwin.mbwarez.dk/.co.za32/t",
                            "http://cygwin.mbwarez.dk/.de/cygwin/",
                            "http://cygwin.mbwarez.dk/.jp",
                            "http://cygwin.mbwarez.dk/.lagoon.nc",
                            "http://cygwin.mbwarez.dk/.lagoon.nc/",
                            "http://cygwin.mbwarez.dk/.nct",
                            "http://cygwin.mbwarez.dk//",
                            "http://cygwin.mbwarez.dk///",
                            "http://cygwin.mbwarez.dk////",
                            "http://cygwin.mbwarez.dk///cygwin/",
                            "http://cygwin.mbwarez.dk///win/",
                            "http://cygwin.mbwarez.dk//cygwi",
                            "http://cygwin.mbwarez.dk//cygwin/",
                            "http://cygwin.mbwarez.dk//cygwin//4",
                            "http://cygwin.mbwarez.dk//cygwin//b",
                            "http://cygwin.mbwarez.dk//cygwin/mi",
                            "http://cygwin.mbwarez.dk//cygwin/n/y",
                            "http://cygwin.mbwarez.dk//cygwin/rg",
                            "http://cygwin.mbwarez.dk//cygwin/ta",
                            "http://cygwin.mbwarez.dk//cygwin/v",
                            "http://cygwin.mbwarez.dk//cygwin/z",
                            "http://cygwin.mbwarez.dk//cygwin32/",
                            "http://cygwin.mbwarez.dk//cygwip",
                            "http://cygwin.mbwarez.dk//n/",
                            "http://cygwin.mbwarez.dk//u",
                            "http://cygwin.mbwarez.dk//win/com:",
                            "http://cygwin.mbwarez.dk//win/n/x",
                            "http://cygwin.mbwarez.dk//ygwin//c",
                            "http://cygwin.mbwarez.dk/4t",
                            "http://cygwin.mbwarez.dk/5T)",
                            "http://cygwin.mbwarez.dk/6",
                            "http://cygwin.mbwarez.dk/7",
                            "http://cygwin.mbwarez.dk/;",
                            "http://cygwin.mbwarez.dk/;cygwin.mbwarez.dk;Europe;Denmark;noshow",
                            "http://cygwin.mbwarez.dk/Asia",
                            "http://cygwin.mbwarez.dk/Asia/ft",
                            "http://cygwin.mbwarez.dk/Bulgaria",
                            "http://cygwin.mbwarez.dk/D1C",
                            "http://cygwin.mbwarez.dk/Europew",
                            "http://cygwin.mbwarez.dk/I",
                            "http://cygwin.mbwarez.dk/Moldova",
                            "http://cygwin.mbwarez.dk/P",
                            "http://cygwin.mbwarez.dk/S",
                            "http://cygwin.mbwarez.dk/U",
                            "http://cygwin.mbwarez.dk/United",
                            "http://cygwin.mbwarez.dk/ac.jp",
                            "http://cygwin.mbwarez.dk/ac.nz_",
                            "http://cygwin.mbwarez.dk/achen.deX",
                            "http://cygwin.mbwarez.dk/aren.neth-",
                            "http://cygwin.mbwarez.dk/argasso.net/a",
                            "http://cygwin.mbwarez.dk/auin/",
                            "http://cygwin.mbwarez.dk/auygwin//n",
                            "http://cygwin.mbwarez.dk/c.jpks.org",
                            "http://cygwin.mbwarez.dk/c/prog/cygwa",
                            "http://cygwin.mbwarez.dk/chum.de",
                            "http://cygwin.mbwarez.dk/cn/cygwin/D$",
                            "http://cygwin.mbwarez.dk/com/cygwin/",
                            "http://cygwin.mbwarez.dk/cyg",
                            "http://cygwin.mbwarez.dk/cygwin",
                            "http://cygwin.mbwarez.dk/cygwin/",
                            "http://cygwin.mbwarez.dk/cygwin/&",
                            "http://cygwin.mbwarez.dk/cygwin//G",
                            "http://cygwin.mbwarez.dk/cygwin/6",
                            "http://cygwin.mbwarez.dk/cygwin/Z",
                            "http://cygwin.mbwarez.dk/cygwin/in/s.",
                            "http://cygwin.mbwarez.dk/cygwin/ina",
                            "http://cygwin.mbwarez.dk/cygwin/n/",
                            "http://cygwin.mbwarez.dk/cygwin/tp:",
                            "http://cygwin.mbwarez.dk/d.com",
                            "http://cygwin.mbwarez.dk/d.com/cygwin/M",
                            "http://cygwin.mbwarez.dk/d.com/cygwin/a",
                            "http://cygwin.mbwarez.dk/d/cygwin/",
                            "http://cygwin.mbwarez.dk/de/cygwin/r.c",
                            "http://cygwin.mbwarez.dk/degwin/",
                            "http://cygwin.mbwarez.dk/e",
                            "http://cygwin.mbwarez.dk/e/cygwin/com/",
                            "http://cygwin.mbwarez.dk/ecygwin/Y7",
                            "http://cygwin.mbwarez.dk/edu.cn/)",
                            "http://cygwin.mbwarez.dk/en.denl",
                            "http://cygwin.mbwarez.dk/et/cygwin/7",
                            "http://cygwin.mbwarez.dk/et/cygwin/n/",
                            "http://cygwin.mbwarez.dk/et/cygwin/uniK/",
                            "http://cygwin.mbwarez.dk/etn/h%",
                            "http://cygwin.mbwarez.dk/etworks.org/r",
                            "http://cygwin.mbwarez.dk/eu.sg",
                            "http://cygwin.mbwarez.dk/fly.by/pub/",
                            "http://cygwin.mbwarez.dk/ftp.iij.",
                            "http://cygwin.mbwarez.dk/ftp://mi",
                            "http://cygwin.mbwarez.dk/gwin/",
                            "http://cygwin.mbwarez.dk/gwin/.net;2Y",
                            "http://cygwin.mbwarez.dk/gwin///",
                            "http://cygwin.mbwarez.dk/gwin///Un",
                            "http://cygwin.mbwarez.dk/gwin//rors.",
                            "http://cygwin.mbwarez.dk/gwin/2t",
                            "http://cygwin.mbwarez.dk/gwin/32/f",
                            "http://cygwin.mbwarez.dk/gwin/in/",
                            "http://cygwin.mbwarez.dk/gwin/in/c.o4",
                            "http://cygwin.mbwarez.dk/gwin/in/rali",
                            "http://cygwin.mbwarez.dk/gwin/win/",
                            "http://cygwin.mbwarez.dk/h.decnia",
                            "http://cygwin.mbwarez.dk/hu/pub/cygwin/y#",
                            "http://cygwin.mbwarez.dk/in.uib.no/2/",
                            "http://cygwin.mbwarez.dk/in/",
                            "http://cygwin.mbwarez.dk/in//",
                            "http://cygwin.mbwarez.dk/in/I",
                            "http://cygwin.mbwarez.dk/in/X)",
                            "http://cygwin.mbwarez.dk/in/gwin/&",
                            "http://cygwin.mbwarez.dk/in/in/",
                            "http://cygwin.mbwarez.dk/in/in/s:/",
                            "http://cygwin.mbwarez.dk/in/l.ca/",
                            "http://cygwin.mbwarez.dk/in/n//",
                            "http://cygwin.mbwarez.dk/in/o",
                            "http://cygwin.mbwarez.dk/in/tps://",
                            "http://cygwin.mbwarez.dk/in/win32/",
                            "http://cygwin.mbwarez.dk/in/ygwin/",
                            "http://cygwin.mbwarez.dk/in/ygwin/~5",
                            "http://cygwin.mbwarez.dk/irrors",
                            "http://cygwin.mbwarez.dk/ist.ac.jp/p",
                            "http://cygwin.mbwarez.dk/lgaria",
                            "http://cygwin.mbwarez.dk/m%",
                            "http://cygwin.mbwarez.dk/m&",
                            "http://cygwin.mbwarez.dk/m/cygwin//",
                            "http://cygwin.mbwarez.dk/m/cygwin/t/",
                            "http://cygwin.mbwarez.dk/main",
                            "http://cygwin.mbwarez.dk/mcygwin/",
                            "http://cygwin.mbwarez.dk/mirrorservice.",
                            "http://cygwin.mbwarez.dk/mygwin/",
                            "http://cygwin.mbwarez.dk/n",
                            "http://cygwin.mbwarez.dk/n.de",
                            "http://cygwin.mbwarez.dk/n.uib.noor",
                            "http://cygwin.mbwarez.dk/n/",
                            "http://cygwin.mbwarez.dk/n////",
                            "http://cygwin.mbwarez.dk/n//n32/",
                            "http://cygwin.mbwarez.dk/n/com/o/",
                            "http://cygwin.mbwarez.dk/n/cygwin/",
                            "http://cygwin.mbwarez.dk/n/e6",
                            "http://cygwin.mbwarez.dk/n/gwin/",
                            "http://cygwin.mbwarez.dk/n/l.ca/pub",
                            "http://cygwin.mbwarez.dk/n/n/E",
                            "http://cygwin.mbwarez.dk/net.fi/pub/mir",
                            "http://cygwin.mbwarez.dk/neta",
                            "http://cygwin.mbwarez.dk/neth/",
                            "http://cygwin.mbwarez.dk/no/cygwin/",
                            "http://cygwin.mbwarez.dk/ochum.dep/pub6",
                            "http://cygwin.mbwarez.dk/om/cygwin/",
                            "http://cygwin.mbwarez.dk/om/cygwin/~:",
                            "http://cygwin.mbwarez.dk/omC",
                            "http://cygwin.mbwarez.dk/omygwin/",
                            "http://cygwin.mbwarez.dk/oo.ca",
                            "http://cygwin.mbwarez.dk/or",
                            "http://cygwin.mbwarez.dk/orks.net",
                            "http://cygwin.mbwarez.dk/osl.orgorg",
                            "http://cygwin.mbwarez.dk/p",
                            "http://cygwin.mbwarez.dk/p-stud.hs-essl",
                            "http://cygwin.mbwarez.dk/ps.com/cygw",
                            "http://cygwin.mbwarez.dk/pub/cygwin/",
                            "http://cygwin.mbwarez.dk/pub/cygwin/ma",
                            "http://cygwin.mbwarez.dk/q/",
                            "http://cygwin.mbwarez.dk/rafal.ca/",
                            "http://cygwin.mbwarez.dk/rg",
                            "http://cygwin.mbwarez.dk/rg/cygwin/",
                            "http://cygwin.mbwarez.dk/rg/cygwin/.",
                            "http://cygwin.mbwarez.dk/rg/cygwin/H;",
                            "http://cygwin.mbwarez.dk/rmanymagata-u",
                            "http://cygwin.mbwarez.dk/ror.aarnet.edu",
                            "http://cygwin.mbwarez.dk/rors/c",
                            "http://cygwin.mbwarez.dk/rror.garr.iz",
                            "http://cygwin.mbwarez.dk/s/cygwin/m",
                            "http://cygwin.mbwarez.dk/s/cygwin/~",
                            "http://cygwin.mbwarez.dk/sd",
                            "http://cygwin.mbwarez.dk/t/cygwin/et1",
                            "http://cygwin.mbwarez.dk/t/cygwin/rau_",
                            "http://cygwin.mbwarez.dk/ta-u.ac.jpx;S",
                            "http://cygwin.mbwarez.dk/ter",
                            "http://cygwin.mbwarez.dk/tt.com//Mirr",
                            "http://cygwin.mbwarez.dk/uAsiaKon",
                            "http://cygwin.mbwarez.dk/uc.ptjp",
                            "http://cygwin.mbwarez.dk/uy.com/"
                        ],
                        "id": "238",
                        "description": "URLs found in memory or binary data"
                    },
                    {
                        "severity": "IMPACT_SEVERITY_INFO",
                        "match_data": [
                            "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\R0IAZP7Z"
                        ],
                        "id": "90",
                        "description": "Creates files inside the user directory"
                    },
                    {
                        "severity": "IMPACT_SEVERITY_INFO",
                        "match_data": [
                            "8.43.85.97:443 -> 192.168.2.13:49711 version: TLS 1.2"
                        ],
                        "id": "7058",
                        "description": "Uses secure TLS version for HTTPS connections"
                    },
                    {
                        "id": "263",
                        "refs": [
                            {
                                "ref": "#memory_dumps",
                                "value": "software.exe, 00000000.00000002.4470709658.00000000000FD000.00000004.00000020.00020000.00000000.sdmp"
                            },
                            {
                                "ref": "#memory_dumps",
                                "value": "software.exe, 00000000.00000002.4471089039.0000000000163000.00000004.00000020.00020000.00000000.sdmp"
                            }
                        ],
                        "match_data": [
                            "Hyper-V RAWp",
                            "Hyper-V RAW"
                        ],
                        "description": "May try to detect the virtual machine to hinder analysis (VM artifact strings found in memory)",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "238",
                        "match_data": [
                            "ftp://cygwin.mirror.rafal.ca/pub/cygwin/ygwin",
                            "ftp://ftp-stud.hs-esslingen.de",
                            "ftp://ftp-stud.hs-esslingen.de/pub/Mirrors/sources.redhat.com/cygwin/https://.",
                            "ftp://ftp-stud.hs-esslingen.dehttp://m",
                            "ftp://ftp.byfly.by/pub/cygwin//",
                            "ftp://ftp.byfly.by/pub/cygwin/aren.net/Unix/sourceware.org/cygwin/rror.terrahost.nodek/",
                            "ftp://ftp.byfly.by/pub/cygwin/rs",
                            "ftp://ftp.eq.uc.pt",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/http://m",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/http://mG",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/https://",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/https://O",
                            "ftp://ftp.fa",
                            "ftp://ftp.fau.de/cygwin//cygwin//http9",
                            "ftp://ftp.fau.de/cygwin/http://f",
                            "ftp://ftp.fau.de/cygwin/p",
                            "ftp://ftp.fsn.hu/pub/cygwin/",
                            "ftp://ftp.fsn.hu/pub/cygwin/in/",
                            "ftp://ftp.fsn.hu/pub/cygwin/n",
                            "ftp://ftp.fsn.hu/pub/cygwin/ygwin/http://m",
                            "ftp://ftp.fsn.hulhttp:",
                            "ftp://ftp.fsn.hurs",
                            "ftp://ftp.funet.fi",
                            "ftp://ftp.funet.fi/pub/mirrors/sourceware.org/pub/cygwin/",
                            "ftp://ftp.funet.fi/pub/mirrors/sourceware.org/pub/cygwin/e",
                            "ftp://ftp.halifax.rwth-aachen.de/cygwin/dk/irror",
                            "ftp://ftp.halifax.rwth-aachen.der",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/http://m",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/http://mp",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/https://",
                            "ftp://ftp.iij.ad.jphttp",
                            "ftp://ftp.inf.tu-dresden.de",
                            "ftp://ftp.inf.tu-dresden.degor",
                            "ftp://ftp.inf.tu-dresden.derror",
                            "ftp://ftp.jaist.ac.jp/pub/cygwin/",
                            "ftp://ftp.jaist.ac.jp/pub/cygwin/http:/",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/http://m",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/https://",
                            "ftp://ftp.kr.freebsd.orgermany",
                            "ftp://ftp.kr.freebsd.orghttps://",
                            "ftp://ftp.l",
                            "ftp://ftp.m/",
                            "ftp://ftp.mirrorservice.orghttps://ftp.",
                            "ftp://ftp.ntu.edu.tw/pub/cygwin/",
                            "ftp://ftp.ntu.edu.tw/pub/cygwin/https:/",
                            "ftp://ftp.ntua.gr/pub/pc/cygwin//http://m",
                            "ftp://ftp.ntua.gr/pub/pc/cygwin/p",
                            "ftp://ftp.ntua.gr/pub/pc/cygwin/s",
                            "ftp://ftp.rnl.tecnico.ulisboa.pt/pub/cygwin/irror",
                            "ftp://ftp.snt.utwente.nlgwin//",
                            "ftp://ftp.snt.utwente.nlp",
                            "ftp://ftp.twaren.net/Unix/sourceware.org/cygwin/in/koddos",
                            "ftp://ftp.yz.yamagata-u.ac.jp",
                            "ftp://ftp.yz.yamagata-u.ac.jp/p",
                            "ftp://ftp.yz.yamagata-u.ac.jp/pn",
                            "ftp://ftp.yz.yamagata-u.ac.jp/pub/cygwin/",
                            "ftp://ftp.yz.yamagata-u.ac.jp/pub/cygwin/c",
                            "ftp://ftp.yz.yamagata-u.ac.jp/pub/cygwin/http:",
                            "ftp://ftp.yz.yamagata-u.ac.jp/pub/cygwin/https://",
                            "ftp://mirror.checkdomain.de/cygwin/",
                            "ftp://mirror.checkdomain.de/cygwin/cygwin",
                            "ftp://mirror.cs.vt.edu/pub/cygwin/cygwin//n/ite",
                            "ftp://mirror.datacenter.by",
                            "ftp://mirror.datacenter.by/pub/mirrors/cygwin/http://m",
                            "ftp://mirror.datacenter.byp",
                            "ftp://mirror.datacenter.bywin/http://m",
                            "ftp://mirror.easyname.at/cygwin/r",
                            "ftp://mirror.easyname.atch.den/http:/",
                            "ftp://mirror.i",
                            "ftp://mirror.internode.on.net/pub/cygwin/ygwin/r",
                            "ftp://mirror.lagoon.nc/cygwin/",
                            "ftp://mirror.lagoon.nc/cygwin/http://lii",
                            "ftp://mirror.lagoon.nc/cygwin/http://m",
                            "ftp://mirror.lagoon.nc/cygwin/p",
                            "ftp://mirror.lagoon.nc/cygwin/win",
                            "ftp://mirror.rise.ph/cygwin/cygwin/http/",
                            "ftp://mirror.rise.phwarez",
                            "ftp://mirrors.dotsrc.org/mirrors/cygwin/http://f",
                            "ftp://mirrors.dotsrc.org/mirrors/cygwin/rror",
                            "ftp://mirrors.dotsrc.orgn.dehttp://f",
                            "ftp://mirrors.netix.net/cygwin/https://",
                            "ftp://mirrors.xmission.com/cygwin/tp",
                            "ftp://sourceware.org/ftp://sources.redhat.com/ftp://gcc.gnu.org/",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/http://s",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/https://",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/https://J",
                            "ftp://sunsite.icm.edu.plp",
                            "http://apps.identrust.com/roots/dstrootcax3.p7c0",
                            "http://cps.letsencrypt.org0",
                            "http://cps.root-x1.letsencrypt.org0",
                            "http://crl.identrust.com/DSTROOTCAX3CRL.crl0",
                            "http://cygwin.cathedral-",
                            "http://cygwin.cathedral-networks.org",
                            "http://cygwin.cathedral-networks.org-",
                            "http://cygwin.cathedral-networks.org.org/cygwin/",
                            "http://cygwin.cathedral-networks.org/",
                            "http://cygwin.cathedral-networks.org/)",
                            "http://cygwin.cathedral-networks.org/-a",
                            "http://cygwin.cathedral-networks.org/.",
                            "http://cygwin.cathedral-networks.org/.d",
                            "http://cygwin.cathedral-networks.org/.e",
                            "http://cygwin.cathedral-networks.org/.md",
                            "http://cygwin.cathedral-networks.org/.n",
                            "http://cygwin.cathedral-networks.org/.o",
                            "http://cygwin.cathedral-networks.org/.oL",
                            "http://cygwin.cathedral-networks.org/.v",
                            "http://cygwin.cathedral-networks.org//",
                            "http://cygwin.cathedral-networks.org///",
                            "http://cygwin.cathedral-networks.org///1",
                            "http://cygwin.cathedral-networks.org///5",
                            "http://cygwin.cathedral-networks.org///=",
                            "http://cygwin.cathedral-networks.org///Q",
                            "http://cygwin.cathedral-networks.org///T",
                            "http://cygwin.cathedral-networks.org///Z",
                            "http://cygwin.cathedral-networks.org//1",
                            "http://cygwin.cathedral-networks.org//2",
                            "http://cygwin.cathedral-networks.org//L",
                            "http://cygwin.cathedral-networks.org//d",
                            "http://cygwin.cathedral-networks.org//f",
                            "http://cygwin.cathedral-networks.org//f/",
                            "http://cygwin.cathedral-networks.org//l",
                            "http://cygwin.cathedral-networks.org//m",
                            "http://cygwin.cathedral-networks.org//mW",
                            "http://cygwin.cathedral-networks.org//sg",
                            "http://cygwin.cathedral-networks.org//w",
                            "http://cygwin.cathedral-networks.org/9",
                            "http://cygwin.cathedral-networks.org/;cygwin.cathedral-networks.org;Europe;Norway;noshow",
                            "http://cygwin.cathedral-networks.org/=",
                            "http://cygwin.cathedral-networks.org/B",
                            "http://cygwin.cathedral-networks.org/M",
                            "http://cygwin.cathedral-networks.org/P",
                            "http://cygwin.cathedral-networks.org/R",
                            "http://cygwin.cathedral-networks.org/S",
                            "http://cygwin.cathedral-networks.org/U",
                            "http://cygwin.cathedral-networks.org/Un",
                            "http://cygwin.cathedral-networks.org/V",
                            "http://cygwin.cathedral-networks.org/Z",
                            "http://cygwin.cathedral-networks.org/al",
                            "http://cygwin.cathedral-networks.org/ar",
                            "http://cygwin.cathedral-networks.org/au",
                            "http://cygwin.cathedral-networks.org/cj",
                            "http://cygwin.cathedral-networks.org/cy",
                            "http://cygwin.cathedral-networks.org/d",
                            "http://cygwin.cathedral-networks.org/de",
                            "http://cygwin.cathedral-networks.org/doF",
                            "http://cygwin.cathedral-networks.org/e",
                            "http://cygwin.cathedral-networks.org/ed",
                            "http://cygwin.cathedral-networks.org/fs",
                            "http://cygwin.cathedral-networks.org/ft",
                            "http://cygwin.cathedral-networks.org/ftI",
                            "http://cygwin.cathedral-networks.org/ftW",
                            "http://cygwin.cathedral-networks.org/g",
                            "http://cygwin.cathedral-networks.org/in",
                            "http://cygwin.cathedral-networks.org/it",
                            "http://cygwin.cathedral-networks.org/la",
                            "http://cygwin.cathedral-networks.org/li",
                            "http://cygwin.cathedral-networks.org/lo",
                            "http://cygwin.cathedral-networks.org/m",
                            "http://cygwin.cathedral-networks.org/m-",
                            "http://cygwin.cathedral-networks.org/n",
                            "http://cygwin.cathedral-networks.org/n/",
                            "http://cygwin.cathedral-networks.org/p",
                            "http://cygwin.cathedral-networks.org/pT",
                            "http://cygwin.cathedral-networks.org/ps",
                            "http://cygwin.cathedral-networks.org/r.",
                            "http://cygwin.cathedral-networks.org/ra",
                            "http://cygwin.cathedral-networks.org/s.",
                            "http://cygwin.cathedral-networks.org/t",
                            "http://cygwin.cathedral-networks.org/tp",
                            "http://cygwin.cathedral-networks.org/tp#1",
                            "http://cygwin.cathedral-networks.org/ts",
                            "http://cygwin.cathedral-networks.org/u",
                            "http://cygwin.cathedral-networks.org/u.",
                            "http://cygwin.cathedral-networks.org/ub",
                            "http://cygwin.cathedral-networks.org/v",
                            "http://cygwin.cathedral-networks.org/w",
                            "http://cygwin.cathedral-networks.org2",
                            "http://cygwin.cathedral-networks.org4",
                            "http://cygwin.cathedral-networks.org://",
                            "http://cygwin.cathedral-networks.orgC",
                            "http://cygwin.cathedral-networks.orgD",
                            "http://cygwin.cathedral-networks.orgR",
                            "http://cygwin.cathedral-networks.orgali",
                            "http://cygwin.cathedral-networks.orgata",
                            "http://cygwin.cathedral-networks.orgb",
                            "http://cygwin.cathedral-networks.orgb/m",
                            "http://cygwin.cathedral-networks.orgc",
                            "http://cygwin.cathedral-networks.orgc.%",
                            "http://cygwin.cathedral-networks.orgedH",
                            "http://cygwin.cathedral-networks.orgfr4",
                            "http://cygwin.cathedral-networks.orggad",
                            "http://cygwin.cathedral-networks.orght",
                            "http://cygwin.cathedral-networks.orghtt",
                            "http://cygwin.cathedral-networks.orghtt:",
                            "http://cygwin.cathedral-networks.orgi",
                            "http://cygwin.cathedral-networks.orgjp",
                            "http://cygwin.cathedral-networks.orgmir-",
                            "http://cygwin.cathedral-networks.orgn/",
                            "http://cygwin.cathedral-networks.orgn/9",
                            "http://cygwin.cathedral-networks.orgor",
                            "http://cygwin.cathedral-networks.orgran",
                            "http://cygwin.cathedral-networks.orgrr",
                            "http://cygwin.cathedral-networks.orgs/cx",
                            "http://cygwin.cathedral-networks.orgtac",
                            "http://cygwin.cathedral-networks.orgtud",
                            "http://cygwin.cathedral-networks.orguts6",
                            "http://cygwin.cathedral-networks.orgwina",
                            "http://cygwin.mbwarez",
                            "http://cygwin.mbwarez%",
                            "http://cygwin.mbwarez%%qc",
                            "http://cygwin.mbwarez.dk",
                            "http://cygwin.mbwarez.dk-bochum.deg/a",
                            "http://cygwin.mbwarez.dk.ac.jp/",
                            "http://cygwin.mbwarez.dk.at/cygwin/a",
                            "http://cygwin.mbwarez.dk.au",
                            "http://cygwin.mbwarez.dk.aun/lub",
                            "http://cygwin.mbwarez.dk.byygw",
                            "http://cygwin.mbwarez.dk.byygwin/://m",
                            "http://cygwin.mbwarez.dk.de/cygwin/",
                            "http://cygwin.mbwarez.dk.de/cygwin/N",
                            "http://cygwin.mbwarez.dk.org/o.net/c",
                            "http://cygwin.mbwarez.dk.orgP4",
                            "http://cygwin.mbwarez.dk.orgcygwin/w",
                            "http://cygwin.mbwarez.dk/",
                            "http://cygwin.mbwarez.dk/)ci",
                            "http://cygwin.mbwarez.dk/)cn",
                            "http://cygwin.mbwarez.dk/.ac.nz",
                            "http://cygwin.mbwarez.dk/.ad.jp7",
                            "http://cygwin.mbwarez.dk/.cn/cygwin/-hB",
                            "http://cygwin.mbwarez.dk/.de",
                            "http://cygwin.mbwarez.dk/.de/ub/cygwi",
                            "http://cygwin.mbwarez.dk/.degwin/",
                            "http://cygwin.mbwarez.dk/.detp.snt.0",
                            "http://cygwin.mbwarez.dk/.jpin/",
                            "http://cygwin.mbwarez.dk/.kr.free=",
                            "http://cygwin.mbwarez.dk//",
                            "http://cygwin.mbwarez.dk////",
                            "http://cygwin.mbwarez.dk///cygwin/",
                            "http://cygwin.mbwarez.dk///cygwin/X",
                            "http://cygwin.mbwarez.dk///ftp.yz.ya",
                            "http://cygwin.mbwarez.dk///in/n/",
                            "http://cygwin.mbwarez.dk///ygwin/W",
                            "http://cygwin.mbwarez.dk//al.ca/L",
                            "http://cygwin.mbwarez.dk//cygwin.viem-i0",
                            "http://cygwin.mbwarez.dk//cygwin/",
                            "http://cygwin.mbwarez.dk//cygwin//",
                            "http://cygwin.mbwarez.dk//cygwin///W",
                            "http://cygwin.mbwarez.dk//cygwin//H",
                            "http://cygwin.mbwarez.dk//cygwin/E",
                            "http://cygwin.mbwarez.dk//cygwin/m",
                            "http://cygwin.mbwarez.dk//cygwin/o/",
                            "http://cygwin.mbwarez.dk//cygwin32/",
                            "http://cygwin.mbwarez.dk//gwin/",
                            "http://cygwin.mbwarez.dk//in/",
                            "http://cygwin.mbwarez.dk//in//n/4",
                            "http://cygwin.mbwarez.dk//in/n//",
                            "http://cygwin.mbwarez.dk//mirro",
                            "http://cygwin.mbwarez.dk//mirror-hk.",
                            "http://cygwin.mbwarez.dk//n//",
                            "http://cygwin.mbwarez.dk//n//in/",
                            "http://cygwin.mbwarez.dk//n/ror",
                            "http://cygwin.mbwarez.dk//sourceware.orV",
                            "http://cygwin.mbwarez.dk/0",
                            "http://cygwin.mbwarez.dk/05",
                            "http://cygwin.mbwarez.dk/1",
                            "http://cygwin.mbwarez.dk/;",
                            "http://cygwin.mbwarez.dk/;cygwin.mbwarez.dk;Europe;Denmark;noshow",
                            "http://cygwin.mbwarez.dk/Asia",
                            "http://cygwin.mbwarez.dk/China.i%",
                            "http://cygwin.mbwarez.dk/Denmark",
                            "http://cygwin.mbwarez.dk/I",
                            "http://cygwin.mbwarez.dk/M",
                            "http://cygwin.mbwarez.dk/Pc",
                            "http://cygwin.mbwarez.dk/Q",
                            "http://cygwin.mbwarez.dk/Wc",
                            "http://cygwin.mbwarez.dk/ac.jprgin/~",
                            "http://cygwin.mbwarez.dk/ac.nzttps://",
                            "http://cygwin.mbwarez.dk/agata-u.ac.jp",
                            "http://cygwin.mbwarez.dk/amagata-",
                            "http://cygwin.mbwarez.dk/argasso.net/",
                            "http://cygwin.mbwarez.dk/auca.no/ud",
                            "http://cygwin.mbwarez.dk/c.jp/pub/cygwi",
                            "http://cygwin.mbwarez.dk/c/prog/cygw",
                            "http://cygwin.mbwarez.dk/center.byt",
                            "http://cygwin.mbwarez.dk/chum.de//P",
                            "http://cygwin.mbwarez.dk/cn/cygwin/",
                            "http://cygwin.mbwarez.dk/cn/cygwin/(",
                            "http://cygwin.mbwarez.dk/cygwin",
                            "http://cygwin.mbwarez.dk/cygwin/",
                            "http://cygwin.mbwarez.dk/cygwin/.nct",
                            "http://cygwin.mbwarez.dk/cygwin//",
                            "http://cygwin.mbwarez.dk/cygwin//s://",
                            "http://cygwin.mbwarez.dk/cygwin/2/T",
                            "http://cygwin.mbwarez.dk/cygwin/c.jp",
                            "http://cygwin.mbwarez.dk/cygwin/et",
                            "http://cygwin.mbwarez.dk/cygwin/g",
                            "http://cygwin.mbwarez.dk/cygwin/in/n",
                            "http://cygwin.mbwarez.dk/cygwin/n/",
                            "http://cygwin.mbwarez.dk/cygwin/n/r",
                            "http://cygwin.mbwarez.dk/cygwin32/",
                            "http://cygwin.mbwarez.dk/de",
                            "http://cygwin.mbwarez.dk/de/cygwin/",
                            "http://cygwin.mbwarez.dk/e",
                            "http://cygwin.mbwarez.dk/ee/cygwin/z",
                            "http://cygwin.mbwarez.dk/en.dein/",
                            "http://cygwin.mbwarez.dk/etworks.org/G",
                            "http://cygwin.mbwarez.dk/g.cax.net",
                            "http://cygwin.mbwarez.dk/g/cygwin/",
                            "http://cygwin.mbwarez.dk/gen.de",
                            "http://cygwin.mbwarez.dk/gie.frwin/",
                            "http://cygwin.mbwarez.dk/grg.usp.br",
                            "http://cygwin.mbwarez.dk/gwin/",
                            "http://cygwin.mbwarez.dk/gwin//",
                            "http://cygwin.mbwarez.dk/gwin//n/",
                            "http://cygwin.mbwarez.dk/gwin/7",
                            "http://cygwin.mbwarez.dk/gwin/B",
                            "http://cygwin.mbwarez.dk/gwin/de/down",
                            "http://cygwin.mbwarez.dk/gwin/ftp://ft",
                            "http://cygwin.mbwarez.dk/gwin/h",
                            "http://cygwin.mbwarez.dk/gwin/http://m",
                            "http://cygwin.mbwarez.dk/gwin/in/",
                            "http://cygwin.mbwarez.dk/gwin/in/com",
                            "http://cygwin.mbwarez.dk/gwin/n/",
                            "http://cygwin.mbwarez.dk/gwin/n//",
                            "http://cygwin.mbwarez.dk/gwin/org/uxa",
                            "http://cygwin.mbwarez.dk/h.dewin/cat",
                            "http://cygwin.mbwarez.dk/hen.de.by:",
                            "http://cygwin.mbwarez.dk/ia/mirrors/cyg",
                            "http://cygwin.mbwarez.dk/in/",
                            "http://cygwin.mbwarez.dk/in/fr/pub/",
                            "http://cygwin.mbwarez.dk/in/gwin/",
                            "http://cygwin.mbwarez.dk/in/gwin/7",
                            "http://cygwin.mbwarez.dk/in/n//jp",
                            "http://cygwin.mbwarez.dk/in/n/7",
                            "http://cygwin.mbwarez.dk/in/urope",
                            "http://cygwin.mbwarez.dk/in/ygwin/",
                            "http://cygwin.mbwarez.dk/k/ygwin//",
                            "http://cygwin.mbwarez.dk/lip6.fromm",
                            "http://cygwin.mbwarez.dk/m/cygwin/",
                            "http://cygwin.mbwarez.dk/m/cygwin//c",
                            "http://cygwin.mbwarez.dk/main",
                            "http://cygwin.mbwarez.dk/many",
                            "http://cygwin.mbwarez.dk/me.atijp",
                            "http://cygwin.mbwarez.dk/mirror.a2",
                            "http://cygwin.mbwarez.dk/n",
                            "http://cygwin.mbwarez.dk/n.de",
                            "http://cygwin.mbwarez.dk/n//a",
                            "http://cygwin.mbwarez.dk/n/ckdomain",
                            "http://cygwin.mbwarez.dk/n/cygwin/",
                            "http://cygwin.mbwarez.dk/n/cygwin/;",
                            "http://cygwin.mbwarez.dk/n/cygwin/n/",
                            "http://cygwin.mbwarez.dk/n/cygwin/t/",
                            "http://cygwin.mbwarez.dk/n/in//",
                            "http://cygwin.mbwarez.dk/n/in///",
                            "http://cygwin.mbwarez.dk/net/",
                            "http://cygwin.mbwarez.dk/netgwin/ralaF",
                            "http://cygwin.mbwarez.dk/nia",
                            "http://cygwin.mbwarez.dk/nterbury.ac",
                            "http://cygwin.mbwarez.dk/nwin/",
                            "http://cygwin.mbwarez.dk/om/cygwin/",
                            "http://cygwin.mbwarez.dk/org.usp.br?",
                            "http://cygwin.mbwarez.dk/os.net/cygwin/cygwin//",
                            "http://cygwin.mbwarez.dk/p",
                            "http://cygwin.mbwarez.dk/p.jaist.ac.jp",
                            "http://cygwin.mbwarez.dk/p.yz.yP",
                            "http://cygwin.mbwarez.dk/pub/cygwin/",
                            "http://cygwin.mbwarez.dk/pub/cygwin/7",
                            "http://cygwin.mbwarez.dk/rafal.ca/",
                            "http://cygwin.mbwarez.dk/rcewa",
                            "http://cygwin.mbwarez.dk/rg/cygwin/",
                            "http://cygwin.mbwarez.dk/rgasso.net/",
                            "http://cygwin.mbwarez.dk/rgcom/et/yn4",
                            "http://cygwin.mbwarez.dk/rloo.caet/ct",
                            "http://cygwin.mbwarez.dk/rmany",
                            "http://cygwin.mbwarez.dk/rmanyn/datac",
                            "http://cygwin.mbwarez.dk/ropeP",
                            "http://cygwin.mbwarez.dk/rror.datacente",
                            "http://cygwin.mbwarez.dk/rror/cygwin/H",
                            "http://cygwin.mbwarez.dk/sd",
                            "http://cygwin.mbwarez.dk/stralia)",
                            "http://cygwin.mbwarez.dk/t",
                            "http://cygwin.mbwarez.dk/t/cygwin/",
                            "http://cygwin.mbwarez.dk/t/cygwin/n/",
                            "http://cygwin.mbwarez.dk/t/cygwin/slin",
                            "http://cygwin.mbwarez.dk/tp://c",
                            "http://cygwin.mbwarez.dk/tworks.org/",
                            "http://cygwin.mbwarez.dk/tworks.org/E",
                            "http://cygwin.mbwarez.dk/tygwin//",
                            "http://cygwin.mbwarez.dk/u.cn",
                            "http://cygwin.mbwarez.dk/utcygwin/V",
                            "http://cygwin.mbwarez.dk/win/",
                            "http://cygwin.mbwarez.dk/win////c",
                            "http://cygwin.mbwarez.dk/win///U",
                            "http://cygwin.mbwarez.dk/win//;",
                            "http://cygwin.mbwarez.dk/win/1",
                            "http://cygwin.mbwarez.dk/win/R",
                            "http://cygwin.mbwarez.dk/win/gwin/",
                            "http://cygwin.mbwarez.dk/win/in/",
                            "http://cygwin.mbwarez.dk/win/in//8"
                        ],
                        "description": "URLs found in memory or binary data",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "id": "7058",
                        "match_data": [
                            "8.43.85.97:443 -> 192.168.2.9:49712 version: TLS 1.2"
                        ],
                        "description": "Uses secure TLS version for HTTPS connections",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "description": "Uses HTTPS",
                        "match_data": [
                            "HTTP traffic on port 49726 -> 443",
                            "HTTP traffic on port 443 -> 49726"
                        ],
                        "severity": "IMPACT_SEVERITY_INFO",
                        "id": "625"
                    },
                    {
                        "refs": [
                            {
                                "ref": "#memory_dumps",
                                "value": "software.exe, 00000001.00000002.4700881249.0000000000D1B000.00000004.00000020.00020000.00000000.sdmp, software.exe, 00000001.00000002.4701422094.0000000000D84000.00000004.00000020.00020000.00000000.sdmp"
                            },
                            {
                                "ref": "#memory_dumps",
                                "value": "software.exe, 00000001.00000002.4701422094.0000000000D84000.00000004.00000020.00020000.00000000.sdmp"
                            }
                        ],
                        "description": "May try to detect the virtual machine to hinder analysis (VM artifact strings found in memory)",
                        "match_data": [
                            "Hyper-V RAW"
                        ],
                        "severity": "IMPACT_SEVERITY_INFO",
                        "id": "263"
                    },
                    {
                        "description": "URLs found in memory or binary data",
                        "match_data": [
                            "ftp://cygwin.mirror.rafal.ca/pub/cygwin/org//https://r",
                            "ftp://cygwin.mirror.rafal.cahttps://h",
                            "ftp://ftp-stud.hs-esslingen.de/pub/Mirrors/sources.redhat.com/cygwin/http://m",
                            "ftp://ftp-stud.hs-esslingen.dein",
                            "ftp://ftp.byfly.by",
                            "ftp://ftp.byfly.by/pub/cygwin///http:s",
                            "ftp://ftp.eq.uc.pt",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/https://5",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/https://mirror-hk.koddos.net/cygwin/",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/https://r",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/rror",
                            "ftp://ftp.fa",
                            "ftp://ftp.fau.de/cygwin/e",
                            "ftp://ftp.fs",
                            "ftp://ftp.fsn.hu/pub/cygwin/",
                            "ftp://ftp.fsn.hunohttp",
                            "ftp://ftp.funet.fi",
                            "ftp://ftp.ha",
                            "ftp://ftp.halifax.rwth-aachen.de",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/http://m",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/https://",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/ror",
                            "ftp://ftp.iij.ad.jphttpv",
                            "ftp://ftp.inf.tu-dresden.de/software/windows/cygwin32/http://f;",
                            "ftp://ftp.inf.tu-dresden.de/software/windows/cygwin32/https://",
                            "ftp://ftp.inf.tu-dresden.degwin/",
                            "ftp://ftp.inf.tu-dresden.den.hu",
                            "ftp://ftp.inf.tu-dresden.derror",
                            "ftp://ftp.jaist.ac.jp/pub/cygwin/",
                            "ftp://ftp.jaist.ac.jp/pub/cygwin/http:",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/https://",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/https://1",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/https://?",
                            "ftp://ftp.kr.freebsd.org/pub/cygwin.com/cygwin/https://f",
                            "ftp://ftp.lip6.fr/pub/cygwin/https://ft",
                            "ftp://ftp.lip6.fr/pub/cygwin/win",
                            "ftp://ftp.lip6.frhttps:S",
                            "ftp://ftp.m",
                            "ftp://ftp.mirrorservice.orgg",
                            "ftp://ftp.mirrorservice.orgp",
                            "ftp://ftp.muug.ca",
                            "ftp://ftp.n",
                            "ftp://ftp.ntu.edu.tw/pub/cygwin/rs",
                            "ftp://ftp.ntua.gr",
                            "ftp://ftp.ntua.grhttps:7",
                            "ftp://ftp.snt.utwente.nl",
                            "ftp://ftp.snt.utwente.nl/pub/software/cygwin/win/",
                            "ftp://ftp.snt.utwente.nlx",
                            "ftp://ftp.twaren.net/Unix/sourceware.org/cygwin/",
                            "ftp://ftp.yz.yamagata-u.ac.jp",
                            "ftp://ftp.yz.yamagata-u.ac.jp/pub/cygwin/http:",
                            "ftp://ftp.yz.yamagata-u.ac.jp/pub/cygwin/or",
                            "ftp://ftp.yz.yamagata-u.ac.jpa",
                            "ftp://linux.rz.ruhr-uni-bochum.de/cygwin/y",
                            "ftp://mirror.checkdomain.demirror",
                            "ftp://mirror.checkdomain.detp",
                            "ftp://mirror.csclub.uwaterloo.ca/cygwin/",
                            "ftp://mirror.csclub.uwaterloo.cahttps:",
                            "ftp://mirror.datacenter.by.jp/",
                            "ftp://mirror.datacenter.byma",
                            "ftp://mirror.easyname.at/cygwin/http://",
                            "ftp://mirror.internode.on.net/pub/cygwin//cygwin/http:",
                            "ftp://mirror.internode.on.net/pub/cygwin/gwin/http://m",
                            "ftp://mirror.lagoon.nc/cygwin/https://",
                            "ftp://mirror.lagoon.nc/cygwin/r",
                            "ftp://mirrors.dotsrc.org/mirrors/cygwin/",
                            "ftp://mirrors.dotsrc.org/mirrors/cygwin/http://f",
                            "ftp://mirrors.dotsrc.orgst",
                            "ftp://mirrors.netix.net/cygwin/https://%",
                            "ftp://sourceware.org/ftp://sources.redhat.com/ftp://gcc.gnu.org/",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/http://c",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/https://",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/https://q",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/in",
                            "http://ac.economia.gob.mx/cps.html0",
                            "http://ac.economia.gob.mx/last.crl0G",
                            "http://acedicom.edicomgroup.com/doc0",
                            "http://acraiz.icpbrasil.gov.br/DPCacraiz.pdf0?",
                            "http://acraiz.icpbrasil.gov.br/LCRacraizv1.crl0",
                            "http://acraiz.icpbrasil.gov.br/LCRacraizv2.crl0",
                            "http://apps.identrust.com/roots/dstrootcax3.p7c0",
                            "http://ca.disig.sk/ca/crl/ca_disig.crl0",
                            "http://ca.mtin.es/mtin/DPCyPoliticas0",
                            "http://ca.mtin.es/mtin/DPCyPoliticas0g",
                            "http://ca.mtin.es/mtin/crl/MTINAutoridadRaiz03",
                            "http://ca.mtin.es/mtin/ocsp0",
                            "http://ca2.mtin.es/mtin/crl/MTINAutoridadRaiz0",
                            "http://certificates.starfieldtech.com/repository/1604",
                            "http://certs.oati.net/repository/OATICA2.crl0",
                            "http://certs.oati.net/repository/OATICA2.crt0",
                            "http://certs.oaticerts.com/repository/OATICA2.crl",
                            "http://certs.oaticerts.com/repository/OATICA2.crt08",
                            "http://cps.chambersign.org/cps/chambersignroot.html0",
                            "http://cps.chambersign.org/cps/chambersroot.html0",
                            "http://cps.letsencrypt.org0",
                            "http://cps.root-x1.letsencrypt.org0",
                            "http://cps.siths.se/sithsrootcav1.html0",
                            "http://crl.certigna.fr/certignarootca.crl01",
                            "http://crl.chambersign.org/chambersignroot.crl0",
                            "http://crl.chambersign.org/chambersroot.crl0",
                            "http://crl.comodoca.com/AAACertificateServices.crl06",
                            "http://crl.defence.gov.au/pki0",
                            "http://crl.dhimyotis.com/certignarootca.crl0",
                            "http://crl.globalsign.net/root-r2.crl0",
                            "http://crl.identrust.com/DSTROOTCAX3CRL.crl0",
                            "http://crl.oces.trust2408.com/oces.crl0",
                            "http://crl.pki.wellsfargo.com/wsprca.crl0",
                            "http://crl.securetrust.com/SGCA.crl0",
                            "http://crl.securetrust.com/STCA.crl0",
                            "http://crl.ssc.lt/root-a/cacrl.crl0",
                            "http://crl.ssc.lt/root-b/cacrl.crl0",
                            "http://crl.ssc.lt/root-c/cacrl.crl0",
                            "http://crl.xrampsecurity.com/XGCA.crl0",
                            "http://crl1.comsign.co.il/crl/comsignglobalrootca.crl0",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/CABD2A79A1076A31F21D253635CB0",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/authrootstl.cab1",
                            "http://ctldl.windowsupdate.com:80",
                            "http://cygwin.cathedral-",
                            "http://cygwin.cathedral-networks.org",
                            "http://cygwin.cathedral-networks.org&",
                            "http://cygwin.cathedral-networks.org(",
                            "http://cygwin.cathedral-networks.org.",
                            "http://cygwin.cathedral-networks.org.nl",
                            "http://cygwin.cathedral-networks.org/",
                            "http://cygwin.cathedral-networks.org/#",
                            "http://cygwin.cathedral-networks.org/%",
                            "http://cygwin.cathedral-networks.org/)",
                            "http://cygwin.cathedral-networks.org/-",
                            "http://cygwin.cathedral-networks.org/-h",
                            "http://cygwin.cathedral-networks.org/.",
                            "http://cygwin.cathedral-networks.org/.f",
                            "http://cygwin.cathedral-networks.org/.l",
                            "http://cygwin.cathedral-networks.org/.m",
                            "http://cygwin.cathedral-networks.org//",
                            "http://cygwin.cathedral-networks.org//#",
                            "http://cygwin.cathedral-networks.org///",
                            "http://cygwin.cathedral-networks.org///ftp.halifax.rwth-aachen.deps://ftp.eq.uc.ptjp",
                            "http://cygwin.cathedral-networks.org///k",
                            "http://cygwin.cathedral-networks.org//A",
                            "http://cygwin.cathedral-networks.org//C",
                            "http://cygwin.cathedral-networks.org//J",
                            "http://cygwin.cathedral-networks.org//Q",
                            "http://cygwin.cathedral-networks.org//S",
                            "http://cygwin.cathedral-networks.org//T",
                            "http://cygwin.cathedral-networks.org//Y",
                            "http://cygwin.cathedral-networks.org//a",
                            "http://cygwin.cathedral-networks.org//c",
                            "http://cygwin.cathedral-networks.org//f",
                            "http://cygwin.cathedral-networks.org//fN",
                            "http://cygwin.cathedral-networks.org//p",
                            "http://cygwin.cathedral-networks.org//pj",
                            "http://cygwin.cathedral-networks.org//w",
                            "http://cygwin.cathedral-networks.org/1",
                            "http://cygwin.cathedral-networks.org/5",
                            "http://cygwin.cathedral-networks.org/7",
                            "http://cygwin.cathedral-networks.org/;cygwin.cathedral-networks.org;Europe;Norway;noshow",
                            "http://cygwin.cathedral-networks.org/=",
                            "http://cygwin.cathedral-networks.org/A",
                            "http://cygwin.cathedral-networks.org/AmQ",
                            "http://cygwin.cathedral-networks.org/C",
                            "http://cygwin.cathedral-networks.org/E",
                            "http://cygwin.cathedral-networks.org/J",
                            "http://cygwin.cathedral-networks.org/L",
                            "http://cygwin.cathedral-networks.org/R",
                            "http://cygwin.cathedral-networks.org/S",
                            "http://cygwin.cathedral-networks.org/T",
                            "http://cygwin.cathedral-networks.org/W",
                            "http://cygwin.cathedral-networks.org/X",
                            "http://cygwin.cathedral-networks.org/Y",
                            "http://cygwin.cathedral-networks.org/_",
                            "http://cygwin.cathedral-networks.org/a",
                            "http://cygwin.cathedral-networks.org/aZ",
                            "http://cygwin.cathedral-networks.org/bu3",
                            "http://cygwin.cathedral-networks.org/c",
                            "http://cygwin.cathedral-networks.org/ck",
                            "http://cygwin.cathedral-networks.org/d",
                            "http://cygwin.cathedral-networks.org/de",
                            "http://cygwin.cathedral-networks.org/e",
                            "http://cygwin.cathedral-networks.org/edJ",
                            "http://cygwin.cathedral-networks.org/et",
                            "http://cygwin.cathedral-networks.org/f",
                            "http://cygwin.cathedral-networks.org/fl",
                            "http://cygwin.cathedral-networks.org/ft",
                            "http://cygwin.cathedral-networks.org/h",
                            "http://cygwin.cathedral-networks.org/i",
                            "http://cygwin.cathedral-networks.org/in",
                            "http://cygwin.cathedral-networks.org/ix",
                            "http://cygwin.cathedral-networks.org/j",
                            "http://cygwin.cathedral-networks.org/ja",
                            "http://cygwin.cathedral-networks.org/l",
                            "http://cygwin.cathedral-networks.org/la",
                            "http://cygwin.cathedral-networks.org/li",
                            "http://cygwin.cathedral-networks.org/ly",
                            "http://cygwin.cathedral-networks.org/m",
                            "http://cygwin.cathedral-networks.org/m/",
                            "http://cygwin.cathedral-networks.org/n/",
                            "http://cygwin.cathedral-networks.org/nlW",
                            "http://cygwin.cathedral-networks.org/o",
                            "http://cygwin.cathedral-networks.org/oR",
                            "http://cygwin.cathedral-networks.org/p",
                            "http://cygwin.cathedral-networks.org/ps",
                            "http://cygwin.cathedral-networks.org/r",
                            "http://cygwin.cathedral-networks.org/r.",
                            "http://cygwin.cathedral-networks.org/s.",
                            "http://cygwin.cathedral-networks.org/s:",
                            "http://cygwin.cathedral-networks.org/st",
                            "http://cygwin.cathedral-networks.org/t",
                            "http://cygwin.cathedral-networks.org/tp",
                            "http://cygwin.cathedral-networks.org/tt",
                            "http://cygwin.cathedral-networks.org/uk",
                            "http://cygwin.cathedral-networks.org/wB",
                            "http://cygwin.cathedral-networks.org/wiO",
                            "http://cygwin.cathedral-networks.org/y",
                            "http://cygwin.cathedral-networks.org/y8",
                            "http://cygwin.cathedral-networks.org/ygp",
                            "http://cygwin.cathedral-networks.org/yn",
                            "http://cygwin.cathedral-networks.org1",
                            "http://cygwin.cathedral-networks.org2",
                            "http://cygwin.cathedral-networks.org3",
                            "http://cygwin.cathedral-networks.org7",
                            "http://cygwin.cathedral-networks.org://",
                            "http://cygwin.cathedral-networks.org://R",
                            "http://cygwin.cathedral-networks.org=",
                            "http://cygwin.cathedral-networks.orgC",
                            "http://cygwin.cathedral-networks.orgI",
                            "http://cygwin.cathedral-networks.orgN",
                            "http://cygwin.cathedral-networks.orga",
                            "http://cygwin.cathedral-networks.orgcom",
                            "http://cygwin.cathedral-networks.orgd",
                            "http://cygwin.cathedral-networks.orge.o",
                            "http://cygwin.cathedral-networks.orgf",
                            "http://cygwin.cathedral-networks.orghtt",
                            "http://cygwin.cathedral-networks.orghum",
                            "http://cygwin.cathedral-networks.orgin.",
                            "http://cygwin.cathedral-networks.orgir",
                            "http://cygwin.cathedral-networks.orgjp",
                            "http://cygwin.cathedral-networks.orgk",
                            "http://cygwin.cathedral-networks.orgn/",
                            "http://cygwin.cathedral-networks.orgom",
                            "http://cygwin.cathedral-networks.orgrgG",
                            "http://cygwin.cathedral-networks.orgrs.",
                            "http://cygwin.cathedral-networks.orgsyn",
                            "http://cygwin.cathedral-networks.orgt",
                            "http://cygwin.cathedral-networks.orgta-",
                            "http://cygwin.cathedral-networks.orgtp.V",
                            "http://cygwin.cathedral-networks.orgum",
                            "http://cygwin.mbwarez",
                            "http://cygwin.mbwarez.dk",
                            "http://cygwin.mbwarez.dk.ac.jp",
                            "http://cygwin.mbwarez.dk.ac.jp/0",
                            "http://cygwin.mbwarez.dk.comcygwin/",
                            "http://cygwin.mbwarez.dk.de.com/",
                            "http://cygwin.mbwarez.dk.de/cygwin/main.de.",
                            "http://cygwin.mbwarez.dk.degwin//ror",
                            "http://cygwin.mbwarez.dk.fsn.huwin/f",
                            "http://cygwin.mbwarez.dk.funet.fio/",
                            "http://cygwin.mbwarez.dk.garr.it/~",
                            "http://cygwin.mbwarez.dk.net",
                            "http://cygwin.mbwarez.dk.orgwin/.",
                            "http://cygwin.mbwarez.dk.orgygwin/",
                            "http://cygwin.mbwarez.dk/",
                            "http://cygwin.mbwarez.dk/%",
                            "http://cygwin.mbwarez.dk/(",
                            "http://cygwin.mbwarez.dk/.",
                            "http://cygwin.mbwarez.dk/.byfly.byjp",
                            "http://cygwin.mbwarez.dk/.cagwin//",
                            "http://cygwin.mbwarez.dk/.datacente",
                            "http://cygwin.mbwarez.dk/.de/cygwin/",
                            "http://cygwin.mbwarez.dk/.de/cygwin/l",
                            "http://cygwin.mbwarez.dk/.de/cygwin/mi",
                            "http://cygwin.mbwarez.dk/.denz",
                            "http://cygwin.mbwarez.dk/.edu.cn",
                            "http://cygwin.mbwarez.dk/.jp/#",
                            "http://cygwin.mbwarez.dk/.net",
                            "http://cygwin.mbwarez.dk/.net&",
                            "http://cygwin.mbwarez.dk/.netwin/b",
                            "http://cygwin.mbwarez.dk/.terrahost",
                            "http://cygwin.mbwarez.dk//",
                            "http://cygwin.mbwarez.dk///in//",
                            "http://cygwin.mbwarez.dk///mirror.ma",
                            "http://cygwin.mbwarez.dk///mirrors.",
                            "http://cygwin.mbwarez.dk//S",
                            "http://cygwin.mbwarez.dk//cygwin/",
                            "http://cygwin.mbwarez.dk//cygwin/#",
                            "http://cygwin.mbwarez.dk//cygwin//",
                            "http://cygwin.mbwarez.dk//cygwin/en",
                            "http://cygwin.mbwarez.dk//cygwin/g/",
                            "http://cygwin.mbwarez.dk//cygwin/rg/k",
                            "http://cygwin.mbwarez.dk//cygwin/suosl",
                            "http://cygwin.mbwarez.dk//cygwin/win/N",
                            "http://cygwin.mbwarez.dk//cygwin32/",
                            "http://cygwin.mbwarez.dk//cygwin32/2",
                            "http://cygwin.mbwarez.dk//cygwin32/3",
                            "http://cygwin.mbwarez.dk//gwin/n/",
                            "http://cygwin.mbwarez.dk//gwin/n/v",
                            "http://cygwin.mbwarez.dk//gwin32/",
                            "http://cygwin.mbwarez.dk//n/gwin/",
                            "http://cygwin.mbwarez.dk//n/in/",
                            "http://cygwin.mbwarez.dk//pu",
                            "http://cygwin.mbwarez.dk//pub/cygwin/c)",
                            "http://cygwin.mbwarez.dk//win/a",
                            "http://cygwin.mbwarez.dk//ygwin/",
                            "http://cygwin.mbwarez.dk/0",
                            "http://cygwin.mbwarez.dk/1",
                            "http://cygwin.mbwarez.dk/3",
                            "http://cygwin.mbwarez.dk/5",
                            "http://cygwin.mbwarez.dk/:",
                            "http://cygwin.mbwarez.dk/;cygwin.mbwarez.dk;Europe;Denmark;noshow",
                            "http://cygwin.mbwarez.dk/=S",
                            "http://cygwin.mbwarez.dk/L",
                            "http://cygwin.mbwarez.dk/United",
                            "http://cygwin.mbwarez.dk/a",
                            "http://cygwin.mbwarez.dk/ata-u.ac.jp)",
                            "http://cygwin.mbwarez.dk/b/cygwin//l",
                            "http://cygwin.mbwarez.dk/ckdomain.deu",
                            "http://cygwin.mbwarez.dk/cn/cygwin/",
                            "http://cygwin.mbwarez.dk/cn/cygwin/7",
                            "http://cygwin.mbwarez.dk/cygwin/",
                            "http://cygwin.mbwarez.dk/cygwin/%",
                            "http://cygwin.mbwarez.dk/cygwin/&",
                            "http://cygwin.mbwarez.dk/cygwin//",
                            "http://cygwin.mbwarez.dk/cygwin///m",
                            "http://cygwin.mbwarez.dk/cygwin//R",
                            "http://cygwin.mbwarez.dk/cygwin//ft",
                            "http://cygwin.mbwarez.dk/cygwin//r",
                            "http://cygwin.mbwarez.dk/cygwin/G",
                            "http://cygwin.mbwarez.dk/cygwin/cygwinP",
                            "http://cygwin.mbwarez.dk/cygwin/e",
                            "http://cygwin.mbwarez.dk/cygwin/l.ca",
                            "http://cygwin.mbwarez.dk/cygwin/n/",
                            "http://cygwin.mbwarez.dk/cygwin/n/l",
                            "http://cygwin.mbwarez.dk/cygwin/r",
                            "http://cygwin.mbwarez.dk/cygwin/ral",
                            "http://cygwin.mbwarez.dk/cygwin/stc",
                            "http://cygwin.mbwarez.dk/cygwin32/",
                            "http://cygwin.mbwarez.dk/cygwin32/?",
                            "http://cygwin.mbwarez.dk/d",
                            "http://cygwin.mbwarez.dk/d.com/",
                            "http://cygwin.mbwarez.dk/d.com/cygwin/",
                            "http://cygwin.mbwarez.dk/d.comn//",
                            "http://cygwin.mbwarez.dk/d/cygwin/n/",
                            "http://cygwin.mbwarez.dk/dewin/(",
                            "http://cygwin.mbwarez.dk/e/cygwin/.jp",
                            "http://cygwin.mbwarez.dk/ecomt",
                            "http://cygwin.mbwarez.dk/einrausch.de",
                            "http://cygwin.mbwarez.dk/em",
                            "http://cygwin.mbwarez.dk/ep",
                            "http://cygwin.mbwarez.dk/et/cygwin/",
                            "http://cygwin.mbwarez.dk/etgwin/",
                            "http://cygwin.mbwarez.dk/etworks.org/",
                            "http://cygwin.mbwarez.dk/g/cygwin/",
                            "http://cygwin.mbwarez.dk/g/cygwin/7",
                            "http://cygwin.mbwarez.dk/g/cygwin/n",
                            "http://cygwin.mbwarez.dk/gwin/",
                            "http://cygwin.mbwarez.dk/gwin/-",
                            "http://cygwin.mbwarez.dk/gwin/-u.ac.jp",
                            "http://cygwin.mbwarez.dk/gwin//",
                            "http://cygwin.mbwarez.dk/gwin//n/",
                            "http://cygwin.mbwarez.dk/gwin/in/",
                            "http://cygwin.mbwarez.dk/gwin/n///miZ",
                            "http://cygwin.mbwarez.dk/gwin/n/4",
                            "http://cygwin.mbwarez.dk/gwin/no/",
                            "http://cygwin.mbwarez.dk/gwin/tmirror",
                            "http://cygwin.mbwarez.dk/gwin/ware.",
                            "http://cygwin.mbwarez.dk/gwin/win/",
                            "http://cygwin.mbwarez.dk/h.de/mirror/cy",
                            "http://cygwin.mbwarez.dk/h.de/win/.",
                            "http://cygwin.mbwarez.dk/in.de/cygwiB",
                            "http://cygwin.mbwarez.dk/in/",
                            "http://cygwin.mbwarez.dk/in/4",
                            "http://cygwin.mbwarez.dk/in/V",
                            "http://cygwin.mbwarez.dk/in/gwin/",
                            "http://cygwin.mbwarez.dk/in/irror.d",
                            "http://cygwin.mbwarez.dk/in/n/in/b",
                            "http://cygwin.mbwarez.dk/in/n/n/",
                            "http://cygwin.mbwarez.dk/in/n/n/~",
                            "http://cygwin.mbwarez.dk/in/tp://ft",
                            "http://cygwin.mbwarez.dk/in/win/R",
                            "http://cygwin.mbwarez.dk/in/win/S",
                            "http://cygwin.mbwarez.dk/in/ygwin/",
                            "http://cygwin.mbwarez.dk/in/ygwin/E",
                            "http://cygwin.mbwarez.dk/inaa.pt",
                            "http://cygwin.mbwarez.dk/inaf",
                            "http://cygwin.mbwarez.dk/isboa.ptf",
                            "http://cygwin.mbwarez.dk/l/pub/cygwip",
                            "http://cygwin.mbwarez.dk/ly.com/",
                            "http://cygwin.mbwarez.dk/m/cygwin//Unia",
                            "http://cygwin.mbwarez.dk/m/cygwin/cygw",
                            "http://cygwin.mbwarez.dk/mgwin/9",
                            "http://cygwin.mbwarez.dk/n",
                            "http://cygwin.mbwarez.dk/n.uib.no/sl.",
                            "http://cygwin.mbwarez.dk/n/",
                            "http://cygwin.mbwarez.dk/n/.no/.i)",
                            "http://cygwin.mbwarez.dk/n//n/",
                            "http://cygwin.mbwarez.dk/n/cygwin/",
                            "http://cygwin.mbwarez.dk/n/gwin/",
                            "http://cygwin.mbwarez.dk/n/gwin/m-"
                        ],
                        "severity": "IMPACT_SEVERITY_INFO",
                        "id": "238"
                    },
                    {
                        "description": "Uses secure TLS version for HTTPS connections",
                        "match_data": [
                            "8.43.85.97:443 -> 192.168.2.10:49726 version: TLS 1.2"
                        ],
                        "severity": "IMPACT_SEVERITY_INFO",
                        "id": "7058"
                    },
                    {
                        "severity": "IMPACT_SEVERITY_INFO",
                        "match_data": [
                            "HTTP traffic on port 49729 -> 443",
                            "HTTP traffic on port 443 -> 49729"
                        ],
                        "id": "625",
                        "description": "Uses HTTPS"
                    },
                    {
                        "severity": "IMPACT_SEVERITY_INFO",
                        "refs": [
                            {
                                "ref": "#memory_dumps",
                                "value": "file.exe, 00000001.00000002.4527137410.0000000000C59000.00000004.00000020.00020000.00000000.sdmp"
                            },
                            {
                                "ref": "#memory_dumps",
                                "value": "file.exe, 00000001.00000002.4527971958.0000000000CB9000.00000004.00000020.00020000.00000000.sdmp"
                            }
                        ],
                        "match_data": [
                            "Hyper-V RAW0",
                            "Hyper-V RAW"
                        ],
                        "id": "263",
                        "description": "May try to detect the virtual machine to hinder analysis (VM artifact strings found in memory)"
                    },
                    {
                        "severity": "IMPACT_SEVERITY_INFO",
                        "match_data": [
                            "ftp://cygwin.mirror.rafal.ca/pub/cygwin/",
                            "ftp://ftp-stud.hs-esslingen.de",
                            "ftp://ftp-stud.hs-esslingen.dehttp://f",
                            "ftp://ftp.acc.umu.se/mirror/cygwin/http",
                            "ftp://ftp.byfly.by/pub/cygwin/ygwin/httpR",
                            "ftp://ftp.byfly.byet",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/http://m4WB",
                            "ftp://ftp.eq.uc.pt/pub/software/pc/prog/cygwin/https://",
                            "ftp://ftp.fau.de",
                            "ftp://ftp.fs",
                            "ftp://ftp.fsn.hu/pub/cygwin/",
                            "ftp://ftp.fsn.hu/pub/cygwin/echttps://",
                            "ftp://ftp.funet.fi/pub/mirrors/sourceware.org/pub/cygwin/",
                            "ftp://ftp.iij.ad.jp/pub/cygwin/http://w",
                            "ftp://ftp.iij.ad.jphttp",
                            "ftp://ftp.inf.tu-dresden.de/software/windows/cygwin32/n/",
                            "ftp://ftp.inf.tu-dresden.deygwin",
                            "ftp://ftp.kr.freebsd.org",
                            "ftp://ftp.kr.freebsd.orgb/cygwin/",
                            "ftp://ftp.l",
                            "ftp://ftp.lip6.fr/pub/cygwin/https://ft.X",
                            "ftp://ftp.lip6.fr/pub/cygwin/in",
                            "ftp://ftp.lip6.fr/pub/cygwin/p",
                            "ftp://ftp.lip6.fr/pub/cygwin/win/in",
                            "ftp://ftp.m",
                            "ftp://ftp.mirrorservice.org",
                            "ftp://ftp.muug.cah.de.deygwin",
                            "ftp://ftp.n",
                            "ftp://ftp.ncF",
                            "ftp://ftp.ntua.gr",
                            "ftp://ftp.ntua.gr/pub/pc/cygwin/http://f",
                            "ftp://ftp.ntua.gr/pub/pc/cygwin/n/https:r",
                            "ftp://ftp.rnl.tecnico.ulisboa.pt/pub/cygwin/n",
                            "ftp://ftp.snt.utwente.nlc",
                            "ftp://ftp.snt.utwente.nlme",
                            "ftp://ftp.twaren.net/Unix/sourceware.org/cygwin//ac",
                            "ftp://ftp.twaren.net/Unix/sourceware.org/cygwin/https:r",
                            "ftp://ftp.yz.yamagata-u.ac.jphttp://ftp",
                            "ftp://mirror.checkdomain.de/cygwin/",
                            "ftp://mirror.checkdomain.de/cygwin/cygwin",
                            "ftp://mirror.checkdomain.de/cygwin/http",
                            "ftp://mirror.checkdomain.demirror",
                            "ftp://mirror.checkdomain.deygwin",
                            "ftp://mirror.cs.vt.edu/pub/cygwin/cygwin/gwin",
                            "ftp://mirror.cs.vt.edu/pub/cygwin/cygwin/n",
                            "ftp://mirror.easyname.at/cygwin//e",
                            "ftp://mirror.easyname.atost.com",
                            "ftp://mirrors.dotsrc.org/mirrors/cygwin/r",
                            "ftp://mirrors.dotsrc.org/mirrors/cygwin/ygwin/in",
                            "ftp://mirrors.dotsrc.orgcygwin/",
                            "ftp://mirrors.netix.net/cygwin//",
                            "ftp://mirrors.netix.net/cygwin/http://ccg",
                            "ftp://mirrors.netix.net/cygwin/httpR",
                            "ftp://mirrors.sonic.net/cygwin/http",
                            "ftp://mirrors.sonic.net/cygwin/https://",
                            "ftp://mirrors.syringanetworks.net/cygwin/",
                            "ftp://mirrors.xmission.com/cygwin/https://",
                            "ftp://sourceware.org/ftp://sources.redhat.com/ftp://gcc.gnu.org/",
                            "ftp://sunsite.icm.edu.pl",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/http://f",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/https://S",
                            "ftp://sunsite.icm.edu.pl/pub/cygnus/cygwin/https://tb",
                            "ftp://sunsite.icm.edu.plc",
                            "http://ac.economia.gob.mx/cps.html0",
                            "http://ac.economia.gob.mx/last.crl0G",
                            "http://acedicom.edicomgroup.com/doc0",
                            "http://acraiz.icpbrasil.gov.br/DPCacraiz.pdf0?",
                            "http://acraiz.icpbrasil.gov.br/LCRacraizv1.crl0",
                            "http://acraiz.icpbrasil.gov.br/LCRacraizv2.crl0",
                            "http://apps.identrust.com/roots/dstrootcax3.p7c0",
                            "http://ca.disig.sk/ca/crl/ca_disig.crl0",
                            "http://ca.mtin.es/mtin/DPCyPoliticas0",
                            "http://ca.mtin.es/mtin/DPCyPoliticas0g",
                            "http://ca.mtin.es/mtin/crl/MTINAutoridadRaiz03",
                            "http://ca.mtin.es/mtin/ocsp0",
                            "http://ca2.mtin.es/mtin/crl/MTINAutoridadRaiz0",
                            "http://certificates.starfieldtech.com/repository/1604",
                            "http://certs.oati.net/repository/OATICA2.crl0",
                            "http://certs.oati.net/repository/OATICA2.crt0",
                            "http://certs.oaticerts.com/repository/OATICA2.crl",
                            "http://certs.oaticerts.com/repository/OATICA2.crt08",
                            "http://cps.chambersign.org/cps/chambersignroot.html0",
                            "http://cps.chambersign.org/cps/chambersroot.html0",
                            "http://cps.letsencrypt.org0",
                            "http://cps.root-x1.letsencrypt.org0",
                            "http://cps.siths.se/sithsrootcav1.html0",
                            "http://crl.certigna.fr/certignarootca.crl01",
                            "http://crl.chambersign.org/chambersignroot.crl0",
                            "http://crl.chambersign.org/chambersroot.crl0",
                            "http://crl.comodoca.com/AAACertificateServices.crl06",
                            "http://crl.defence.gov.au/pki0",
                            "http://crl.dhimyotis.com/certignarootca.crl0",
                            "http://crl.globalsign.net/root-r2.crl0",
                            "http://crl.identrust.com/DSTROOTCAX3CRL.crl0",
                            "http://crl.oces.trust2408.com/oces.crl0",
                            "http://crl.securetrust.com/SGCA.crl0",
                            "http://crl.securetrust.com/STCA.crl0",
                            "http://crl.ssc.lt/root-a/cacrl.crl0",
                            "http://crl.ssc.lt/root-b/cacrl.crl0",
                            "http://crl.ssc.lt/root-c/cacrl.crl0",
                            "http://crl.xrampsecurity.com/XGCA.crl0",
                            "http://crl1.comsign.co.il/crl/comsignglobalrootca.crl0",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/CABD2A79A1076A31F21D253635CB0",
                            "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/authrootstl.cab",
                            "http://ctldl.windowsupdate.com:80/msdownload/update/v3/static/trustedr/en/CABD2A79A1076A31F21D253635",
                            "http://cygwin.cathedral-",
                            "http://cygwin.cathedral-S",
                            "http://cygwin.cathedral-a",
                            "http://cygwin.cathedral-networks.org",
                            "http://cygwin.cathedral-networks.org%G",
                            "http://cygwin.cathedral-networks.org.fr",
                            "http://cygwin.cathedral-networks.org.i",
                            "http://cygwin.cathedral-networks.org/",
                            "http://cygwin.cathedral-networks.org/$~",
                            "http://cygwin.cathedral-networks.org/&",
                            "http://cygwin.cathedral-networks.org/&%",
                            "http://cygwin.cathedral-networks.org/&gg",
                            "http://cygwin.cathedral-networks.org/-",
                            "http://cygwin.cathedral-networks.org/.",
                            "http://cygwin.cathedral-networks.org/.f",
                            "http://cygwin.cathedral-networks.org/.o",
                            "http://cygwin.cathedral-networks.org/.v",
                            "http://cygwin.cathedral-networks.org//",
                            "http://cygwin.cathedral-networks.org///",
                            "http://cygwin.cathedral-networks.org///lg",
                            "http://cygwin.cathedral-networks.org//Qhk",
                            "http://cygwin.cathedral-networks.org//R",
                            "http://cygwin.cathedral-networks.org//aq",
                            "http://cygwin.cathedral-networks.org//c",
                            "http://cygwin.cathedral-networks.org//f",
                            "http://cygwin.cathedral-networks.org//m",
                            "http://cygwin.cathedral-networks.org//w",
                            "http://cygwin.cathedral-networks.org/4iO",
                            "http://cygwin.cathedral-networks.org/5A",
                            "http://cygwin.cathedral-networks.org/6JX",
                            "http://cygwin.cathedral-networks.org/;cygwin.cathedral-networks.org;Europe;Norway;noshow",
                            "http://cygwin.cathedral-networks.org/B",
                            "http://cygwin.cathedral-networks.org/D",
                            "http://cygwin.cathedral-networks.org/Mb",
                            "http://cygwin.cathedral-networks.org/Nc",
                            "http://cygwin.cathedral-networks.org/P$",
                            "http://cygwin.cathedral-networks.org/TH",
                            "http://cygwin.cathedral-networks.org/UX",
                            "http://cygwin.cathedral-networks.org/YIz",
                            "http://cygwin.cathedral-networks.org/a",
                            "http://cygwin.cathedral-networks.org/a/",
                            "http://cygwin.cathedral-networks.org/aa",
                            "http://cygwin.cathedral-networks.org/ac",
                            "http://cygwin.cathedral-networks.org/ai",
                            "http://cygwin.cathedral-networks.org/ba$",
                            "http://cygwin.cathedral-networks.org/c",
                            "http://cygwin.cathedral-networks.org/ca",
                            "http://cygwin.cathedral-networks.org/cy",
                            "http://cygwin.cathedral-networks.org/d",
                            "http://cygwin.cathedral-networks.org/e",
                            "http://cygwin.cathedral-networks.org/ec",
                            "http://cygwin.cathedral-networks.org/et",
                            "http://cygwin.cathedral-networks.org/e~",
                            "http://cygwin.cathedral-networks.org/fi",
                            "http://cygwin.cathedral-networks.org/g",
                            "http://cygwin.cathedral-networks.org/gw",
                            "http://cygwin.cathedral-networks.org/gwwH",
                            "http://cygwin.cathedral-networks.org/g~;",
                            "http://cygwin.cathedral-networks.org/i",
                            "http://cygwin.cathedral-networks.org/ia",
                            "http://cygwin.cathedral-networks.org/ie",
                            "http://cygwin.cathedral-networks.org/jH",
                            "http://cygwin.cathedral-networks.org/jagGk",
                            "http://cygwin.cathedral-networks.org/j~",
                            "http://cygwin.cathedral-networks.org/k.",
                            "http://cygwin.cathedral-networks.org/m",
                            "http://cygwin.cathedral-networks.org/mi#G7",
                            "http://cygwin.cathedral-networks.org/miXc",
                            "http://cygwin.cathedral-networks.org/n",
                            "http://cygwin.cathedral-networks.org/n/wH",
                            "http://cygwin.cathedral-networks.org/ni",
                            "http://cygwin.cathedral-networks.org/niI",
                            "http://cygwin.cathedral-networks.org/o",
                            "http://cygwin.cathedral-networks.org/o.",
                            "http://cygwin.cathedral-networks.org/oG",
                            "http://cygwin.cathedral-networks.org/oeI",
                            "http://cygwin.cathedral-networks.org/oo",
                            "http://cygwin.cathedral-networks.org/q#",
                            "http://cygwin.cathedral-networks.org/rg",
                            "http://cygwin.cathedral-networks.org/s",
                            "http://cygwin.cathedral-networks.org/s.",
                            "http://cygwin.cathedral-networks.org/s/",
                            "http://cygwin.cathedral-networks.org/ss",
                            "http://cygwin.cathedral-networks.org/tJ",
                            "http://cygwin.cathedral-networks.org/tp",
                            "http://cygwin.cathedral-networks.org/tp&W",
                            "http://cygwin.cathedral-networks.org/ttcF",
                            "http://cygwin.cathedral-networks.org/u$",
                            "http://cygwin.cathedral-networks.org/ub",
                            "http://cygwin.cathedral-networks.org/wi",
                            "http://cygwin.cathedral-networks.org/wi3c",
                            "http://cygwin.cathedral-networks.org/y",
                            "http://cygwin.cathedral-networks.org/yg",
                            "http://cygwin.cathedral-networks.org/yn",
                            "http://cygwin.cathedral-networks.org/y~-",
                            "http://cygwin.cathedral-networks.org/z",
                            "http://cygwin.cathedral-networks.org/zf",
                            "http://cygwin.cathedral-networks.org3Jg",
                            "http://cygwin.cathedral-networks.org4$",
                            "http://cygwin.cathedral-networks.org5gT",
                            "http://cygwin.cathedral-networks.org://",
                            "http://cygwin.cathedral-networks.org;az",
                            "http://cygwin.cathedral-networks.orgB%",
                            "http://cygwin.cathedral-networks.orgD",
                            "http://cygwin.cathedral-networks.orgE",
                            "http://cygwin.cathedral-networks.orgE~",
                            "http://cygwin.cathedral-networks.orgHc",
                            "http://cygwin.cathedral-networks.orgJe2",
                            "http://cygwin.cathedral-networks.orgJiu",
                            "http://cygwin.cathedral-networks.orgKgz",
                            "http://cygwin.cathedral-networks.orgM$",
                            "http://cygwin.cathedral-networks.orgT",
                            "http://cygwin.cathedral-networks.orgUni-c",
                            "http://cygwin.cathedral-networks.orgVeu",
                            "http://cygwin.cathedral-networks.orgX",
                            "http://cygwin.cathedral-networks.orgXoa",
                            "http://cygwin.cathedral-networks.orgag",
                            "http://cygwin.cathedral-networks.orgala/A",
                            "http://cygwin.cathedral-networks.organMG",
                            "http://cygwin.cathedral-networks.orgbJ",
                            "http://cygwin.cathedral-networks.orgbX",
                            "http://cygwin.cathedral-networks.orgc$",
                            "http://cygwin.cathedral-networks.orgce",
                            "http://cygwin.cathedral-networks.orgeo:",
                            "http://cygwin.cathedral-networks.orgfly",
                            "http://cygwin.cathedral-networks.orggH",
                            "http://cygwin.cathedral-networks.orggwi",
                            "http://cygwin.cathedral-networks.orggwi0",
                            "http://cygwin.cathedral-networks.orgg~;",
                            "http://cygwin.cathedral-networks.orgiGl",
                            "http://cygwin.cathedral-networks.orgn/fc",
                            "http://cygwin.cathedral-networks.orgnc",
                            "http://cygwin.cathedral-networks.orgor",
                            "http://cygwin.cathedral-networks.orgp",
                            "http://cygwin.cathedral-networks.orgtscjc",
                            "http://cygwin.cathedral-networks.orgttp",
                            "http://cygwin.cathedral-networks.orgtud_~",
                            "http://cygwin.cathedral-networks.orgu",
                            "http://cygwin.cathedral-networks.orgutsXak",
                            "http://cygwin.cathedral-networks.orgwi",
                            "http://cygwin.cathedral-networks.orgyg",
                            "http://cygwin.cathedral-networks.orgygw",
                            "http://cygwin.mi",
                            "http://cygwin.mirror.constant.com",
                            "http://cygwin.mirror.constant.com/",
                            "http://cygwin.mirror.constant.com/.net/oeI",
                            "http://cygwin.mirror.constant.com/.org",
                            "http://cygwin.mirror.constant.com/.org/g.",
                            "http://cygwin.mirror.constant.com//",
                            "http://cygwin.mirror.constant.com//.$",
                            "http://cygwin.mirror.constant.com//B%",
                            "http://cygwin.mirror.constant.com//Ha",
                            "http://cygwin.mirror.constant.com/3~J",
                            "http://cygwin.mirror.constant.com/4g",
                            "http://cygwin.mirror.constant.com/9",
                            "http://cygwin.mirror.constant.com/;cygwin.mirror.constant.com;North",
                            "http://cygwin.mirror.constant.com/Asia",
                            "http://cygwin.mirror.constant.com/I",
                            "http://cygwin.mirror.constant.com/M$",
                            "http://cygwin.mirror.constant.com/ca",
                            "http://cygwin.mirror.constant.com/co.u(b",
                            "http://cygwin.mirror.constant.com/cygwin.m",
                            "http://cygwin.mirror.constant.com/cygwin/",
                            "http://cygwin.mirror.constant.com/erraSb",
                            "http://cygwin.mirror.constant.com/ftp://mij",
                            "http://cygwin.mirror.constant.com/g/?~F",
                            "http://cygwin.mirror.constant.com/ganetIc",
                            "http://cygwin.mirror.constant.com/gwin/",
                            "http://cygwin.mirror.constant.com/gwin/t",
                            "http://cygwin.mirror.constant.com/in/",
                            "http://cygwin.mirror.constant.com/in//.rH",
                            "http://cygwin.mirror.constant.com/in//G",
                            "http://cygwin.mirror.constant.com/in/f$",
                            "http://cygwin.mirror.constant.com/in/in/",
                            "http://cygwin.mirror.constant.com/n//w",
                            "http://cygwin.mirror.constant.com/n/:b",
                            "http://cygwin.mirror.constant.com/o.net",
                            "http://cygwin.mirror.constant.com/o.net/",
                            "http://cygwin.mirror.constant.com/p://lYb",
                            "http://cygwin.mirror.constant.com/ps://Ag",
                            "http://cygwin.mirror.constant.com/pub/c",
                            "http://cygwin.mirror.constant.com/re/windows/cygwin32/Fb",
                            "http://cygwin.mirror.constant.com/redha",
                            "http://cygwin.mirror.constant.com/s.org/",
                            "http://cygwin.mirror.constant.com/soc.org.",
                            "http://cygwin.mirror.constant.com/t",
                            "http://cygwin.mirror.constant.com/t/",
                            "http://cygwin.mirror.constant.com/tacenter",
                            "http://cygwin.mirror.constant.com/th",
                            "http://cygwin.mirror.constant.com/win/",
                            "http://cygwin.mirror.constant.com/win/-un",
                            "http://cygwin.mirror.constant.com/win//",
                            "http://cygwin.mirror.constant.com/win///",
                            "http://cygwin.mirror.constant.com/ygwin/",
                            "http://cygwin.mirror.constant.com163.co",
                            "http://cygwin.mirror.constant.comD",
                            "http://cygwin.mirror.constant.comI~p",
                            "http://cygwin.mirror.constant.comT%",
                            "http://cygwin.mirror.constant.comYg",
                            "http://cygwin.mirror.constant.combly.co",
                            "http://cygwin.mirror.constant.comn/",
                            "http://cygwin.mirror.constant.comn//",
                            "http://cygwin.mirror.constant.comn/h",
                            "http://cygwin.mirror.constant.comnet/",
                            "http://cygwin.mirror.constant.coms",
                            "http://cygwin.mirror.constant.comtE",
                            "http://cygwin.mirror.constant.comtps://",
                            "http://cygwin.mirror.constant.comwin.mi",
                            "http://cygwin.mirror.globo.tech",
                            "http://cygwin.mirror.globo.tech.net",
                            "http://cygwin.mirror.globo.tech.org/or",
                            "http://cygwin.mirror.globo.tech/",
                            "http://cygwin.mirror.globo.tech/.de/cygwin/x",
                            "http://cygwin.mirror.globo.tech//",
                            "http://cygwin.mirror.globo.tech///",
                            "http://cygwin.mirror.globo.tech//Zgk",
                            "http://cygwin.mirror.globo.tech//cygwin",
                            "http://cygwin.mirror.globo.tech//cygwin/://",
                            "http://cygwin.mirror.globo.tech//cygwin/n/",
                            "http://cygwin.mirror.globo.tech//g",
                            "http://cygwin.mirror.globo.tech//n/L",
                            "http://cygwin.mirror.globo.tech//ub/cygwin/",
                            "http://cygwin.mirror.globo.tech/63.comsb",
                            "http://cygwin.mirror.globo.tech/:",
                            "http://cygwin.mirror.globo.tech/;cygwin.mirror.globo.tech;North",
                            "http://cygwin.mirror.globo.tech/Asiak",
                            "http://cygwin.mirror.globo.tech/S",
                            "http://cygwin.mirror.globo.tech/b/cygwin//cy",
                            "http://cygwin.mirror.globo.tech/ca/cygwin/ft",
                            "http://cygwin.mirror.globo.tech/com/cygwin/",
                            "http://cygwin.mirror.globo.tech/cygwin/",
                            "http://cygwin.mirror.globo.tech/cygwin////c~X",
                            "http://cygwin.mirror.globo.tech/d",
                            "http://cygwin.mirror.globo.tech/f",
                            "http://cygwin.mirror.globo.tech/gasso.net/",
                            "http://cygwin.mirror.globo.tech/gwin/",
                            "http://cygwin.mirror.globo.tech/gwin/K%",
                            "http://cygwin.mirror.globo.tech/gwin/gwin/",
                            "http://cygwin.mirror.globo.tech/gwin/n/i",
                            "http://cygwin.mirror.globo.tech/in/",
                            "http://cygwin.mirror.globo.tech/j",
                            "http://cygwin.mirror.globo.tech/m~",
                            "http://cygwin.mirror.globo.tech/n/",
                            "http://cygwin.mirror.globo.tech/n//cygwin/Na",
                            "http://cygwin.mirror.globo.tech/n/M",
                            "http://cygwin.mirror.globo.tech/n/b/cygwin/",
                            "http://cygwin.mirror.globo.tech/n/cygwin/",
                            "http://cygwin.mirror.globo.tech/n/cygwin/l",
                            "http://cygwin.mirror.globo.tech/n/t",
                            "http://cygwin.mirror.globo.tech/n/win/ps://0b",
                            "http://cygwin.mirror.globo.tech/nettp.a",
                            "http://cygwin.mirror.globo.tech/nf",
                            "http://cygwin.mirror.globo.tech/no//g",
                            "http://cygwin.mirror.globo.tech/or.data(",
                            "http://cygwin.mirror.globo.tech/orgX~",
                            "http://cygwin.mirror.globo.tech/ors.neusoft.e",
                            "http://cygwin.mirror.globo.tech/p://miig",
                            "http://cygwin.mirror.globo.tech/pub/mir",
                            "http://cygwin.mirror.globo.tech/ror.cheOc#",
                            "http://cygwin.mirror.globo.tech/rors.xm:cy",
                            "http://cygwin.mirror.globo.tech/rror",
                            "http://cygwin.mirror.globo.tech/sK",
                            "http://cygwin.mirror.globo.tech/tsrc.or",
                            "http://cygwin.mirror.globo.tech/ttp://m",
                            "http://cygwin.mirror.globo.tech/ttps://",
                            "http://cygwin.mirror.globo.tech/win/W",
                            "http://cygwin.mirror.globo.tech/win/gwin/",
                            "http://cygwin.mirror.globo.tech/ygwin////",
                            "http://cygwin.mirror.globo.tech/ygwin//Hc",
                            "http://cygwin.mirror.globo.tech/ygwin/ftPb",
                            "http://cygwin.mirror.globo.tech/ygwin/win/",
                            "http://cygwin.mirror.globo.techAsiaU~l",
                            "http://cygwin.mirror.globo.techathedral",
                            "http://cygwin.mirror.globo.techca",
                            "http://cygwin.mirror.globo.techcn",
                            "http://cygwin.mirror.globo.techde",
                            "http://cygwin.mirror.globo.techdeG",
                            "http://cygwin.mirror.globo.techgwin/dg",
                            "http://cygwin.mirror.globo.techin/",
                            "http://cygwin.mirror.globo.techin//",
                            "http://cygwin.mirror.globo.techin/pubS",
                            "http://cygwin.mirror.globo.techm/",
                            "http://cygwin.mirror.globo.techn/",
                            "http://cygwin.mirror.globo.techn/://",
                            "http://cygwin.mirror.globo.techn/ps://",
                            "http://cygwin.mirror.globo.techn/t/t",
                            "http://cygwin.mirror.globo.techost.com",
                            "http://cygwin.mirror.globo.techp.br/cygIE",
                            "http://cygwin.mirror.globo.techs.orgNg",
                            "http://cygwin.mirror.globo.techv",
                            "http://cygwin.mirror.globo.techwin/",
                            "http://cygwin.mirror.globo.techwin/p.j",
                            "http://cygwin.mirror.rafal.ca",
                            "http://cygwin.mirror.rafal.ca.com/"
                        ],
                        "id": "238",
                        "description": "URLs found in memory or binary data"
                    },
                    {
                        "severity": "IMPACT_SEVERITY_INFO",
                        "match_data": [
                            "8.43.85.97:443 -> 192.168.2.15:49729 version: TLS 1.2"
                        ],
                        "id": "7058",
                        "description": "Uses secure TLS version for HTTPS connections"
                    }
                ],
                "last_modification_date": 1677046869,
                "mutexes_created": [
                    "\\Sessions\\1\\BaseNamedObjects\\Local\\ZonesCacheCounterMutex",
                    "\\Sessions\\1\\BaseNamedObjects\\Local\\ZonesLockedCacheCounterMutex"
                ],
                "files_opened": [
                    "/etc\\system-fips",
                    "C:\\Users\\user\\AppData\\LocalLow",
                    "C:\\Users\\user\\AppData\\LocalLow\\Microsoft\\CryptnetUrlCache\\MetaData\\AFCF8E76E06245E64045C911C7467E0F",
                    "C:\\Users\\user\\Desktop\\setup.rc",
                    "C:\\Windows\\Globalization\\Sorting\\sortdefault.nls",
                    "C:\\Windows\\SYSTEM32\\CRYPTBASE.DLL",
                    "C:\\Windows\\SYSTEM32\\CRYPTSP.dll",
                    "C:\\Windows\\SYSTEM32\\DNSAPI.dll",
                    "C:\\Windows\\SYSTEM32\\DPAPI.DLL",
                    "C:\\Windows\\SYSTEM32\\IPHLPAPI.DLL",
                    "C:\\Windows\\SYSTEM32\\NTASN1.dll",
                    "C:\\Windows\\SYSTEM32\\SspiCli.dll",
                    "C:\\Windows\\SYSTEM32\\WININET.dll",
                    "C:\\Windows\\SYSTEM32\\WINNSI.DLL",
                    "C:\\Windows\\SYSTEM32\\bcrypt.dll",
                    "C:\\Windows\\SYSTEM32\\cryptnet.dll",
                    "C:\\Windows\\SYSTEM32\\dhcpcsvc.DLL",
                    "C:\\Windows\\SYSTEM32\\dhcpcsvc6.DLL",
                    "C:\\Windows\\SYSTEM32\\en-US\\tzres.dll.mui",
                    "C:\\Windows\\SYSTEM32\\en-US\\winnlsres.dll.mui",
                    "C:\\Windows\\SYSTEM32\\gpapi.dll",
                    "C:\\Windows\\SYSTEM32\\iertutil.dll",
                    "C:\\Windows\\SYSTEM32\\mskeyprotect.dll",
                    "C:\\Windows\\SYSTEM32\\ncrypt.dll",
                    "C:\\Windows\\SYSTEM32\\ntmarta.dll",
                    "C:\\Windows\\SYSTEM32\\ondemandconnroutehelper.dll",
                    "C:\\Windows\\SYSTEM32\\tzres.dll",
                    "C:\\Windows\\SYSTEM32\\urlmon.dll",
                    "C:\\Windows\\SYSTEM32\\webio.dll",
                    "C:\\Windows\\SYSTEM32\\winhttp.dll",
                    "C:\\Windows\\SYSTEM32\\winnlsres.dll",
                    "C:\\Windows\\SYSTEM32\\wintypes.dll",
                    "C:\\Windows\\System32\\CoreMessaging.dll",
                    "C:\\Windows\\System32\\CoreUIComponents.dll",
                    "C:\\Windows\\System32\\TextInputFramework.dll",
                    "C:\\Windows\\System32\\drivers\\etc\\hosts",
                    "C:\\Windows\\System32\\en-US\\CRYPT32.dll.mui",
                    "C:\\Windows\\System32\\en-US\\USER32.dll.mui",
                    "C:\\Windows\\System32\\en-US\\wshqos.dll.mui",
                    "C:\\Windows\\System32\\fwpuclnt.dll",
                    "C:\\Windows\\System32\\rasadhlp.dll",
                    "C:\\Windows\\System32\\wshqos.dll",
                    "C:\\Windows\\WinSxS\\amd64_microsoft.windows.c..-controls.resources_6595b64144ccf1df_6.0.17134.1304_en-us_ea072f00a93a0bdd",
                    "C:\\Windows\\WinSxS\\amd64_microsoft.windows.c..-controls.resources_6595b64144ccf1df_6.0.17134.1304_en-us_ea072f00a93a0bdd\\COMCTL32.dll.mui",
                    "C:\\Windows\\WinSxS\\amd64_microsoft.windows.common-controls_6595b64144ccf1df_6.0.17134.1304_none_d3fbe61b7c93d9f0",
                    "C:\\Windows\\WinSxS\\amd64_microsoft.windows.common-controls_6595b64144ccf1df_6.0.17134.1304_none_d3fbe61b7c93d9f0\\COMCTL32.dll",
                    "C:\\Windows\\system32\\IMM32.DLL",
                    "C:\\Windows\\system32\\drivers\\etc\\hosts",
                    "C:\\Windows\\system32\\dwmapi.dll",
                    "C:\\Windows\\system32\\en-US\\mswsock.dll.mui",
                    "C:\\Windows\\system32\\mswsock.dll",
                    "C:\\Windows\\system32\\ncryptsslp.dll",
                    "C:\\Windows\\system32\\oleaut32.dll",
                    "C:\\Windows\\system32\\rpcss.dll",
                    "C:\\Windows\\system32\\rsaenh.dll",
                    "C:\\Windows\\system32\\schannel.DLL",
                    "C:\\Windows\\system32\\uxtheme.dll",
                    "C:\\Windows\\system32\\uxtheme.dll.Config",
                    "C:\\cygwin64",
                    "C:\\cygwin64\\bin\\cygcheck.exe",
                    "C:\\cygwin64\\bin\\cygwin1.dll",
                    "C:\\cygwin64\\etc\\setup\\setup.rc",
                    "C:\\cygwin64\\var",
                    "C:\\cygwin64\\var\\log",
                    "Nsi",
                    "\\DEVICE\\NETBT_TCPIP_{3882A85B-858A-11EB-B9E1-806E6F6E6963}",
                    "\\DEVICE\\NETBT_TCPIP_{CBA69670-7441-4D46-8A3A-61E0A7B4F41B}",
                    "\\Device\\Afd\\Endpoint",
                    "\\Device\\KsecDD",
                    "\\Device\\RasAcd",
                    "\\DEVICE\\NETBT_TCPIP_{92904508-F335-4574-A127-534547B20089}",
                    "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\ETCJ2WHM",
                    "\\DEVICE\\NETBT_TCPIP_{D98ADCA8-3705-4093-B6B0-210B85CA195B}",
                    "\\DEVICE\\NETBT_TCPIP_{44C728A6-CC3C-434D-B238-E5B6541E3476}",
                    "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\R0IAZP7Z"
                ],
                "analysis_date": 1669406573,
                "sandbox_name": "Zenbox",
                "mitre_attack_techniques": [
                    {
                        "signature_description": "Creates files inside the user directory",
                        "id": "T1036",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "signature_description": "Sample is packed with UPX",
                        "id": "T1027.002",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "signature_description": "PE file has section (not .text) which is very likely to contain packed code (zlib compression ratio < 0.011)",
                        "id": "T1027.002",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "signature_description": "Sample is packed with UPX",
                        "id": "T1027",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "signature_description": "Reads software policies",
                        "id": "T1082",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "signature_description": "Reads the hosts file",
                        "id": "T1018",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "signature_description": "Uses HTTPS",
                        "id": "T1573",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "signature_description": "Uses HTTPS for network communication, use the SSL MITM Proxy cookbook for further analysis",
                        "id": "T1573",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "signature_description": "Performs DNS lookups",
                        "id": "T1095",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "signature_description": "Uses HTTPS",
                        "id": "T1071",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "signature_description": "Performs DNS lookups",
                        "id": "T1071",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "signature_description": "Monitors certain registry keys / values for changes (often done to protect autostart functionality)",
                        "id": "T1012",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "signature_description": "May try to detect the virtual machine to hinder analysis (VM artifact strings found in memory)",
                        "id": "T1518.001",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "90"
                            }
                        ],
                        "signature_description": "Creates files inside the user directory",
                        "id": "T1036",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "433"
                            }
                        ],
                        "signature_description": "PE file has section (not .text) which is very likely to contain packed code (zlib compression ratio < 0.011)",
                        "id": "T1027.002",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "342"
                            }
                        ],
                        "signature_description": "Sample is packed with UPX",
                        "id": "T1027.002",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "342"
                            }
                        ],
                        "signature_description": "Sample is packed with UPX",
                        "id": "T1027",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "263"
                            }
                        ],
                        "signature_description": "May try to detect the virtual machine to hinder analysis (VM artifact strings found in memory)",
                        "id": "T1518.001",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "509"
                            }
                        ],
                        "signature_description": "Reads software policies",
                        "id": "T1082",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "328"
                            }
                        ],
                        "signature_description": "Reads the hosts file",
                        "id": "T1018",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "625"
                            }
                        ],
                        "signature_description": "Uses HTTPS",
                        "id": "T1573",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "624"
                            }
                        ],
                        "signature_description": "Uses HTTPS for network communication, use the SSL MITM Proxy cookbook for further analysis",
                        "id": "T1573",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "206"
                            }
                        ],
                        "signature_description": "Performs DNS lookups",
                        "id": "T1095",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "206"
                            }
                        ],
                        "signature_description": "Performs DNS lookups",
                        "id": "T1071",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "625"
                            }
                        ],
                        "signature_description": "Uses HTTPS",
                        "id": "T1071",
                        "severity": "IMPACT_SEVERITY_INFO"
                    },
                    {
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "198"
                            }
                        ],
                        "signature_description": "Monitors certain registry keys / values for changes (often done to protect autostart functionality)",
                        "id": "T1012",
                        "severity": "IMPACT_SEVERITY_INFO"
                    }
                ],
                "registry_keys_opened": [
                    "HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Internet Settings",
                    "HKEY_CURRENT_USER\\SOFTWARE\\Policies\\Microsoft\\Windows\\CurrentVersion\\Internet Settings",
                    "HKEY_CURRENT_USER\\Software",
                    "HKEY_CURRENT_USER\\Software\\Classes\\Local Settings\\MuiCache\\48\\52C64B7E",
                    "HKEY_CURRENT_USER\\Software\\Cygwin\\setup",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\CTF\\DirectSwitchHotkeys",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Download",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_ALLOW_REVERSE_SOLIDUS_IN_USERINFO_KB932562",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_ALWAYS_USE_DNS_FOR_SPN_KB3022771",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_BUFFERBREAKING_818408",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_BYPASS_CACHE_FOR_CREDPOLICY_KB936611",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_COMPAT_USE_CONNECTION_BASED_NEGOTIATE_AUTH_KB2151543",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_DIGEST_NO_EXTRAS_IN_URI",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_DISABLE_NOTIFY_UNVERIFIED_SPN_KB2385266",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_DISABLE_UNICODE_HANDLE_CLOSING_CALLBACK",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_DISALLOW_NULL_IN_RESPONSE_HEADERS",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_ENABLE_TOKEN_BINDING",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_EXCLUDE_INVALID_CLIENT_CERT_KB929477",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_FIX_CHUNKED_PROXY_SCRIPT_DOWNLOAD_KB843289",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_HTTP_USERNAME_PASSWORD_DISABLE",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_IGNORE_MAPPINGS_FOR_CREDPOLICY",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_IGNORE_POLICIES_ZONEMAP_IF_ESC_ENABLED_KB918915",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_INCLUDE_PORT_IN_SPN_KB908209",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_LOCALMACHINE_LOCKDOWN",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_MIME_HANDLING",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_PERMIT_CACHE_FOR_AUTHENTICATED_FTP_KB910274",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_PRESERVE_SPACES_IN_FILENAMES_KB952730",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_RETURN_FAILED_CONNECT_CONTENT_KB942615",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_SCH_SEND_AUX_RECORD_KB_2618444",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_SKIP_POST_RETRY_ON_INTERNETWRITEFILE_KB895954",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_URI_DISABLECACHE",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_USE_CNAME_FOR_SPN_KB911149",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_USE_IETLDLIST_FOR_DOMAIN_DETERMINATION",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_USE_UTF8_FOR_BASIC_AUTH_KB967545",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_ZONES_CHECK_ZONEMAP_POLICY_KB941001",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\RETRY_HEADERONLYPOST_ONCONNECTIONRESET",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\Security",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\SystemCertificates\\CA",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\SystemCertificates\\CA\\CRLs",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\SystemCertificates\\CA\\CTLs",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\SystemCertificates\\CA\\Certificates",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\SystemCertificates\\CA\\PhysicalStores",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\SystemCertificates\\Disallowed",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\SystemCertificates\\Disallowed\\CRLs",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\SystemCertificates\\Disallowed\\CTLs",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\SystemCertificates\\Disallowed\\Certificates",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\SystemCertificates\\Root",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\SystemCertificates\\Root\\CRLs",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\SystemCertificates\\Root\\CTLs",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\SystemCertificates\\Root\\Certificates",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\SystemCertificates\\SmartCardRoot",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\SystemCertificates\\SmartCardRoot\\CRLs",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\SystemCertificates\\SmartCardRoot\\CTLs",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\SystemCertificates\\SmartCardRoot\\Certificates",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\SystemCertificates\\TrustedPeople",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\SystemCertificates\\TrustedPeople\\CRLs",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\SystemCertificates\\TrustedPeople\\CTLs",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\SystemCertificates\\TrustedPeople\\Certificates",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\SystemCertificates\\trust",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\SystemCertificates\\trust\\CRLs",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\SystemCertificates\\trust\\CTLs",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\SystemCertificates\\trust\\Certificates",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\1",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\1\\KnownFolders",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\5.0\\Cache",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\5.0\\Cache\\Content",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\5.0\\Cache\\Cookies",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\5.0\\Cache\\Extensible Cache",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\5.0\\Cache\\History",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Lockdown_Zones\\",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Lockdown_Zones\\0",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Lockdown_Zones\\1",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Lockdown_Zones\\2",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Lockdown_Zones\\3",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Lockdown_Zones\\4",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\ProtocolDefaults\\",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Zones\\",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Zones\\0",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Zones\\1",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Zones\\2",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Zones\\3",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Zones\\4",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\WinTrust\\Trust Providers\\Software Publishing",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\windows\\CurrentVersion\\Internet Settings",
                    "HKEY_CURRENT_USER\\Software\\Policies",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Internet Explorer",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Internet Explorer\\Main",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Internet Explorer\\Main\\FeatureControl",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Internet Explorer\\Security",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\SystemCertificates\\CA",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\SystemCertificates\\CA\\CRLs",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\SystemCertificates\\CA\\CTLs",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\SystemCertificates\\CA\\Certificates",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\SystemCertificates\\Disallowed",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\SystemCertificates\\Disallowed\\CRLs",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\SystemCertificates\\Disallowed\\CTLs",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\SystemCertificates\\Disallowed\\Certificates",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\SystemCertificates\\TrustedPeople",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\SystemCertificates\\TrustedPeople\\CRLs",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\SystemCertificates\\TrustedPeople\\CTLs",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\SystemCertificates\\TrustedPeople\\Certificates",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\SystemCertificates\\TrustedPublisher\\Safer",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\SystemCertificates\\trust",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\SystemCertificates\\trust\\CRLs",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\SystemCertificates\\trust\\CTLs",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\SystemCertificates\\trust\\Certificates",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Windows\\CurrentVersion\\Internet Settings",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Lockdown_Zones\\",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Lockdown_Zones\\0",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Lockdown_Zones\\1",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Lockdown_Zones\\2",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Lockdown_Zones\\3",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Lockdown_Zones\\4",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Zones\\",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Zones\\0",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Zones\\1",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Zones\\2",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Zones\\3",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Zones\\4",
                    "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Windows\\Explorer",
                    "HKEY_CURRENT_USER\\ZoneMap\\Ranges\\",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\AppID\\setup-x86_64.exe",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\AppID\\{00021401-0000-0000-C000-000000000046}",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\CLSID\\{00021401-0000-0000-C000-000000000046}",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\CLSID\\{00021401-0000-0000-C000-000000000046}\\Elevation",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\CLSID\\{00021401-0000-0000-C000-000000000046}\\InprocHandler",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\CLSID\\{00021401-0000-0000-C000-000000000046}\\InprocHandler32",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\CLSID\\{00021401-0000-0000-C000-000000000046}\\InprocServer32",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\CLSID\\{00021401-0000-0000-C000-000000000046}\\LocalServer",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\CLSID\\{00021401-0000-0000-C000-000000000046}\\LocalServer32",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\CLSID\\{00021401-0000-0000-C000-000000000046}\\TreatAs",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\CLSID\\{057EEE47-2572-4AA1-88D7-60CE2149E33C}",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\CLSID\\{057EEE47-2572-4AA1-88D7-60CE2149E33C}\\Elevation",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\CLSID\\{057EEE47-2572-4AA1-88D7-60CE2149E33C}\\InprocHandler",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\CLSID\\{057EEE47-2572-4AA1-88D7-60CE2149E33C}\\InprocHandler32",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\CLSID\\{057EEE47-2572-4AA1-88D7-60CE2149E33C}\\InprocServer32",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\CLSID\\{057EEE47-2572-4AA1-88D7-60CE2149E33C}\\LocalServer",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\CLSID\\{057EEE47-2572-4AA1-88D7-60CE2149E33C}\\LocalServer32",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\CLSID\\{057EEE47-2572-4AA1-88D7-60CE2149E33C}\\TreatAs",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\Interface\\{00000134-0000-0000-C000-000000000046}",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\Interface\\{00000134-0000-0000-C000-000000000046}\\ProxyStubClsid32",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\Interface\\{A168AADC-1674-49DA-AD4F-4F27DF8760D0}",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\Interface\\{a168aadc-1674-49da-ad4f-4f27df8760d0}\\ProxyStubClsid32",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\AppModel\\Lookaside\\Packages",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\CTF\\",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\CTF\\Compatibility\\setup-x86_64.exe",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Cryptography\\Defaults\\Provider\\Microsoft Enhanced RSA and AES Cryptographic Provider",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Cryptography\\OID\\EncodingType 0",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Cryptography\\OID\\EncodingType 0\\CertDllCreateCertificateChainEngine\\Config\\Default",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Cryptography\\OID\\EncodingType 0\\CertDllOpenStoreProv",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Cryptography\\OID\\EncodingType 0\\CertDllOpenStoreProv\\#16",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Cryptography\\OID\\EncodingType 0\\CertDllOpenStoreProv\\Ldap",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Cryptography\\OID\\EncodingType 0\\CryptDllDecodeObjectEx",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Cryptography\\OID\\EncodingType 1",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Cryptography\\OID\\EncodingType 1\\CertDllOpenStoreProv",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Cryptography\\OID\\EncodingType 1\\CryptDllDecodeObjectEx",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Cryptography\\OID\\EncodingType 1\\CryptDllDecodeObjectEx\\1.2.840.113549.1.9.16.1.1",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Cryptography\\OID\\EncodingType 1\\CryptDllDecodeObjectEx\\1.2.840.113549.1.9.16.2.1",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Cryptography\\OID\\EncodingType 1\\CryptDllDecodeObjectEx\\1.2.840.113549.1.9.16.2.11",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Cryptography\\OID\\EncodingType 1\\CryptDllDecodeObjectEx\\1.2.840.113549.1.9.16.2.12",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Cryptography\\OID\\EncodingType 1\\CryptDllDecodeObjectEx\\1.2.840.113549.1.9.16.2.2",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Cryptography\\OID\\EncodingType 1\\CryptDllDecodeObjectEx\\1.2.840.113549.1.9.16.2.3",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Cryptography\\OID\\EncodingType 1\\CryptDllDecodeObjectEx\\1.2.840.113549.1.9.16.2.4",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\EnterpriseCertificates\\CA\\CRLs",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\EnterpriseCertificates\\CA\\CTLs",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\EnterpriseCertificates\\CA\\Certificates",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\EnterpriseCertificates\\Disallowed\\CRLs",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\EnterpriseCertificates\\Disallowed\\CTLs",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\EnterpriseCertificates\\Disallowed\\Certificates",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\EnterpriseCertificates\\Root\\CRLs",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\EnterpriseCertificates\\Root\\CTLs",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\EnterpriseCertificates\\Root\\Certificates",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\EnterpriseCertificates\\Trust\\CRLs",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\EnterpriseCertificates\\Trust\\CTLs",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\EnterpriseCertificates\\Trust\\Certificates",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\EnterpriseCertificates\\TrustedPeople\\CRLs",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\EnterpriseCertificates\\TrustedPeople\\CTLs",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\EnterpriseCertificates\\TrustedPeople\\Certificates",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_ALLOW_REVERSE_SOLIDUS_IN_USERINFO_KB932562",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_ALWAYS_USE_DNS_FOR_SPN_KB3022771",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_BUFFERBREAKING_818408",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_BYPASS_CACHE_FOR_CREDPOLICY_KB936611",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_COMPAT_USE_CONNECTION_BASED_NEGOTIATE_AUTH_KB2151543",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_DIGEST_NO_EXTRAS_IN_URI",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_DISABLE_NOTIFY_UNVERIFIED_SPN_KB2385266",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_DISABLE_UNICODE_HANDLE_CLOSING_CALLBACK",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_DISALLOW_NULL_IN_RESPONSE_HEADERS",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_ENABLE_PASSPORT_SESSION_STORE_KB948608",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_ENABLE_TOKEN_BINDING",
                    "HKEY_CURRENT_USER\\Software\\Classes",
                    "HKEY_CURRENT_USER\\Software\\Classes\\Local Settings",
                    "HKEY_CURRENT_USER\\Software\\Classes\\Local Settings\\MuiCache\\4d\\52C64B7E",
                    "HKEY_CURRENT_USER_Classes",
                    "HKEY_CURRENT_USER_Classes\\APPID\\{00021401-0000-0000-C000-000000000046}",
                    "HKEY_CURRENT_USER_Classes\\AppID\\software.exe",
                    "HKEY_CURRENT_USER_Classes\\AppID\\{00021401-0000-0000-C000-000000000046}",
                    "HKEY_CURRENT_USER_Classes\\CLSID\\{00021401-0000-0000-C000-000000000046}",
                    "HKEY_CURRENT_USER_Classes\\CLSID\\{00021401-0000-0000-C000-000000000046}\\Elevation",
                    "HKEY_CURRENT_USER_Classes\\CLSID\\{00021401-0000-0000-C000-000000000046}\\InProcServer32",
                    "HKEY_CURRENT_USER_Classes\\CLSID\\{00021401-0000-0000-C000-000000000046}\\InprocHandler",
                    "HKEY_CURRENT_USER_Classes\\CLSID\\{00021401-0000-0000-C000-000000000046}\\InprocHandler32",
                    "HKEY_CURRENT_USER_Classes\\CLSID\\{00021401-0000-0000-C000-000000000046}\\InprocServer32",
                    "HKEY_CURRENT_USER_Classes\\CLSID\\{00021401-0000-0000-C000-000000000046}\\LocalServer",
                    "HKEY_CURRENT_USER_Classes\\CLSID\\{00021401-0000-0000-C000-000000000046}\\LocalServer32",
                    "HKEY_CURRENT_USER_Classes\\CLSID\\{00021401-0000-0000-C000-000000000046}\\TreatAs",
                    "HKEY_CURRENT_USER_Classes\\CLSID\\{057EEE47-2572-4AA1-88D7-60CE2149E33C}",
                    "HKEY_CURRENT_USER_Classes\\CLSID\\{057EEE47-2572-4AA1-88D7-60CE2149E33C}\\Elevation",
                    "HKEY_CURRENT_USER_Classes\\CLSID\\{057EEE47-2572-4AA1-88D7-60CE2149E33C}\\InProcServer32",
                    "HKEY_CURRENT_USER_Classes\\CLSID\\{057EEE47-2572-4AA1-88D7-60CE2149E33C}\\InprocHandler",
                    "HKEY_CURRENT_USER_Classes\\CLSID\\{057EEE47-2572-4AA1-88D7-60CE2149E33C}\\InprocHandler32",
                    "HKEY_CURRENT_USER_Classes\\CLSID\\{057EEE47-2572-4AA1-88D7-60CE2149E33C}\\InprocServer32",
                    "HKEY_CURRENT_USER_Classes\\CLSID\\{057EEE47-2572-4AA1-88D7-60CE2149E33C}\\LocalServer",
                    "HKEY_CURRENT_USER_Classes\\CLSID\\{057EEE47-2572-4AA1-88D7-60CE2149E33C}\\LocalServer32",
                    "HKEY_CURRENT_USER_Classes\\CLSID\\{057EEE47-2572-4AA1-88D7-60CE2149E33C}\\TreatAs",
                    "HKEY_CURRENT_USER_Classes\\Interface\\{00000134-0000-0000-C000-000000000046}",
                    "HKEY_CURRENT_USER_Classes\\Interface\\{00000134-0000-0000-C000-000000000046}\\ProxyStubClsid32",
                    "HKEY_CURRENT_USER_Classes\\Interface\\{A168AADC-1674-49DA-AD4F-4F27DF8760D0}",
                    "HKEY_CURRENT_USER_Classes\\Interface\\{a168aadc-1674-49da-ad4f-4f27df8760d0}\\ProxyStubClsid32",
                    "HKEY_CURRENT_USER_Classes\\Local Settings\\Software\\Microsoft",
                    "HKEY_CURRENT_USER_Classes\\Local Settings\\Software\\Microsoft\\Ole",
                    "HKEY_CURRENT_USER_Classes\\Local Settings\\Software\\Microsoft\\Ole\\FeatureDevelopmentProperties",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\CTF\\Compatibility\\software.exe",
                    "HKEY_CURRENT_USER\\Software\\Classes\\Local Settings\\MuiCache\\46\\52C64B7E",
                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\AppID\\program.exe",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\CTF\\Compatibility\\program.exe",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\AppID\\executable.exe",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\CTF\\Compatibility\\executable.exe",
                    "HKEY_CURRENT_USER\\Software\\Classes\\Local Settings\\MuiCache\\47\\52C64B7E",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\CLSID\\{0358B920-0AC7-461F-98F4-58E32CD89148}",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\CLSID\\{0358b920-0ac7-461f-98f4-58e32cd89148}\\InprocHandler",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\CLSID\\{0358b920-0ac7-461f-98f4-58e32cd89148}\\InprocHandler32",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\CLSID\\{0358b920-0ac7-461f-98f4-58e32cd89148}\\InprocServer32",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\CLSID\\{0358b920-0ac7-461f-98f4-58e32cd89148}\\TreatAs",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\AppID\\file.exe",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\CTF\\Compatibility\\file.exe",
                    "HKEY_CURRENT_USER_Classes\\AppID\\executable.exe",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\AppID\\software.exe",
                    "HKEY_CURRENT_USER_Classes\\AppID\\file.exe",
                    "HKEY_CURRENT_USER_Classes\\AppID\\program.exe",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_EXCLUDE_INVALID_CLIENT_CERT_KB929477",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_FIX_CHUNKED_PROXY_SCRIPT_DOWNLOAD_KB843289",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_HTTP_USERNAME_PASSWORD_DISABLE",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_IGNORE_MAPPINGS_FOR_CREDPOLICY",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_IGNORE_POLICIES_ZONEMAP_IF_ESC_ENABLED_KB918915",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_INCLUDE_PORT_IN_SPN_KB908209",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_LOCALMACHINE_LOCKDOWN",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_MIME_HANDLING",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_PERMIT_CACHE_FOR_AUTHENTICATED_FTP_KB910274",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_PRESERVE_SPACES_IN_FILENAMES_KB952730",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_RETURN_FAILED_CONNECT_CONTENT_KB942615",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_SCH_SEND_AUX_RECORD_KB_2618444",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_SKIP_POST_RETRY_ON_INTERNETWRITEFILE_KB895954",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_URI_DISABLECACHE",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_USE_CNAME_FOR_SPN_KB911149",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_USE_IETLDLIST_FOR_DOMAIN_DETERMINATION",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_USE_UTF8_FOR_BASIC_AUTH_KB967545",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_ZONES_CHECK_ZONEMAP_POLICY_KB941001",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\RETRY_HEADERONLYPOST_ONCONNECTIONRESET",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\OLE",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\OLEAUT",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\SystemCertificates\\AuthRoot\\NULL",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\SystemCertificates\\ROOT\\NULL",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\FontLink\\SystemLink",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\executable.exe",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\LanguagePack\\DataStore_V1.0",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\LanguagePack\\SurrogateFallback",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\LanguagePack\\SurrogateFallback\\Arial",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\LanguagePack\\SurrogateFallback\\MS Shell Dlg",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\msasn1",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\AppModelUnlock",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\FolderDescriptions\\{2B0F765D-C0E9-4171-908E-08A611B84FF6}",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\FolderDescriptions\\{2B0F765D-C0E9-4171-908E-08A611B84FF6}\\PropertyBag",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\FolderDescriptions\\{352481E8-33BE-4251-BA85-6007CAEDCF9D}",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\FolderDescriptions\\{352481E8-33BE-4251-BA85-6007CAEDCF9D}\\PropertyBag",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\FolderDescriptions\\{5E6C858F-0E22-4760-9AFE-EA3317B67173}",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\FolderDescriptions\\{5E6C858F-0E22-4760-9AFE-EA3317B67173}\\PropertyBag",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\FolderDescriptions\\{D9DC8A3B-B784-432E-A781-5A1130A75963}",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\FolderDescriptions\\{D9DC8A3B-B784-432E-A781-5A1130A75963}\\PropertyBag",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\FolderDescriptions\\{F1B32785-6FBA-4FCF-9D55-7B8E7F157091}",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\FolderDescriptions\\{F1B32785-6FBA-4FCF-9D55-7B8E7F157091}\\PropertyBag",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Internet Settings",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\WinHttp",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\OOBE",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Internet Explorer\\Security",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows NT\\DNSClient\\DnsPolicyConfig",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\WindowsStore",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\Appx",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\CurrentVersion\\Internet Settings"
                ],
                "ip_traffic": [
                    {
                        "transport_layer_protocol": "TCP",
                        "destination_ip": "8.43.85.97",
                        "destination_port": 443
                    },
                    {
                        "transport_layer_protocol": "TCP",
                        "destination_ip": "13.107.4.50",
                        "destination_port": 80
                    }
                ],
                "processes_tree": [
                    {
                        "process_id": "6752",
                        "name": "\"C:\\Users\\user\\Desktop\\setup-x86_64.exe\" "
                    }
                ],
                "memory_dumps": [
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4006229143.0000000002A99000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44666880",
                        "size": "20480"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4028714596.0000000002A9F000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44691456",
                        "size": "36864"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4023092884.0000000002A8F000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44625920",
                        "size": "118784"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3986544940.0000000005C06000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "45056",
                        "base_address": "96493568",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4026209520.0000000002AAC000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44744704",
                        "size": "69632"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4054507190.0000000002ABF000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44822528",
                        "size": "36864"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4039446772.0000000002AB7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44789760",
                        "size": "106496"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4012020699.0000000002A9E000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "20480",
                        "base_address": "44687360",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4030636581.0000000002A94000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44646400",
                        "size": "122880"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3985689994.0000000005BE7000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "4096",
                        "base_address": "96366592",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4016297437.0000000002AA4000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44711936",
                        "size": "53248"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4040752177.0000000002A8F000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44625920",
                        "size": "53248"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4015430436.0000000002A98000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44662784",
                        "size": "36864"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4044398789.0000000002ABA000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44802048",
                        "size": "69632"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4003745871.0000000002AA7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44724224",
                        "size": "28672"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3998916328.0000000002A9F000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44691456",
                        "size": "16384"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4037832419.0000000002AB7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44789760",
                        "size": "12288"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3996620218.0000000002AAE000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44752896",
                        "size": "4096"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4734940162.000000000525A000.00000004.00000010.00020000.00000000.sdmp",
                        "size": "24576",
                        "base_address": "86351872",
                        "stage": "MEM_STAGE_EXIT"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4039992924.0000000002ABA000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44802048",
                        "size": "94208"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4047262118.0000000002AC9000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44863488",
                        "size": "65536"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3995960485.0000000002AA4000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "12288",
                        "base_address": "44711936",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4022940810.0000000002AAC000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "12288",
                        "base_address": "44744704",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4054050891.0000000002AD2000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44900352",
                        "size": "8192"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4734038491.0000000001210000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "4096",
                        "base_address": "18939904",
                        "stage": "MEM_STAGE_EXIT"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3987291764.0000000005BC0000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "96206848",
                        "size": "20480"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4046591470.0000000002AB9000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "28672",
                        "base_address": "44797952",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4054923989.0000000002AAE000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "28672",
                        "base_address": "44752896",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4020671692.0000000002A90000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44630016",
                        "size": "8192"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4734817418.0000000002AD8000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_EXIT",
                        "base_address": "44924928",
                        "size": "4096"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4734069058.0000000001280000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "8192",
                        "base_address": "19398656",
                        "stage": "MEM_STAGE_EXIT"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4018148317.0000000002ABB000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44806144",
                        "size": "8192"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4017981928.0000000002A9E000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44687360",
                        "size": "57344"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4004930021.0000000002A9A000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44670976",
                        "size": "32768"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4017932241.0000000002ABB000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44806144",
                        "size": "8192"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4014240923.0000000002AAC000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44744704",
                        "size": "8192"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3996256433.0000000002A9F000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44691456",
                        "size": "20480"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4001342862.0000000002A9D000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44683264",
                        "size": "24576"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4016986043.0000000002ABB000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44806144",
                        "size": "8192"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3997439413.0000000002A97000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44658688",
                        "size": "61440"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4038715677.0000000002AC7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44855296",
                        "size": "12288"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3985425456.0000000005BC5000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "96227328",
                        "size": "135168"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4016403271.0000000002A8F000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44625920",
                        "size": "49152"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4035950922.0000000002AB7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44789760",
                        "size": "45056"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3999845512.0000000002A91000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "32768",
                        "base_address": "44634112",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4046438285.0000000002AD8000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "4096",
                        "base_address": "44924928",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3995422691.0000000002AA9000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44732416",
                        "size": "24576"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4055573607.0000000002AD6000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "4096",
                        "base_address": "44916736",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4040103925.0000000002AAC000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44744704",
                        "size": "24576"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4032872996.0000000002AB7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44789760",
                        "size": "20480"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3996378944.0000000002A92000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "12288",
                        "base_address": "44638208",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4050614442.0000000002AA7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44724224",
                        "size": "20480"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4017013365.0000000002AB8000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44793856",
                        "size": "12288"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4039777145.0000000002ACB000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44871680",
                        "size": "24576"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4734854989.0000000004660000.00000004.00000800.00020000.00000000.sdmp",
                        "size": "4096",
                        "base_address": "73793536",
                        "stage": "MEM_STAGE_EXIT"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4040864152.0000000002A9D000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44683264",
                        "size": "61440"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4055789295.0000000002AD2000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44900352",
                        "size": "16384"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4046491932.0000000002A9C000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44679168",
                        "size": "65536"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3998782377.0000000002A97000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44658688",
                        "size": "4096"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4726416623.000000000010E000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_EXIT",
                        "base_address": "1105920",
                        "size": "151552"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3782890564.000000000011D000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "8192",
                        "base_address": "1167360",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4014664264.0000000002AA7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44724224",
                        "size": "20480"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3996090999.0000000002A92000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "12288",
                        "base_address": "44638208",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4733435997.0000000000880000.00000040.00000001.01000000.00000003.sdmp",
                        "size": "4096",
                        "base_address": "8912896",
                        "stage": "MEM_STAGE_EXIT"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4042878365.0000000002AC7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44855296",
                        "size": "49152"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4034427616.0000000002AA3000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44707840",
                        "size": "16384"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4016801210.0000000002AB7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44789760",
                        "size": "24576"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4054247621.0000000002A8C000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44613632",
                        "size": "139264"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4023633658.0000000002A95000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44650496",
                        "size": "118784"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4008487274.0000000002A95000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44650496",
                        "size": "20480"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3988055647.0000000005BC2000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "96215040",
                        "size": "12288"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4047123716.0000000002A9B000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44675072",
                        "size": "69632"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4037245444.0000000002ACB000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "12288",
                        "base_address": "44871680",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3782934519.0000000000120000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "90112",
                        "base_address": "1179648",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4735148545.0000000005860000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_EXIT",
                        "base_address": "92667904",
                        "size": "196608"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4016009250.0000000002AB7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44789760",
                        "size": "24576"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4015207252.0000000002AA2000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44703744",
                        "size": "61440"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4728013413.0000000000401000.00000040.00000001.01000000.00000003.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_EXIT",
                        "base_address": "4198400",
                        "size": "3780608"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3995482815.0000000002AAB000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44740608",
                        "size": "16384"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4002524145.0000000002A9E000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44687360",
                        "size": "20480"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4009008631.0000000002A98000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44662784",
                        "size": "8192"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4017590892.0000000002A98000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "12288",
                        "base_address": "44662784",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3999778851.0000000002A9F000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44691456",
                        "size": "16384"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4031885746.0000000002AB7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44789760",
                        "size": "20480"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4041244123.0000000002AC7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44855296",
                        "size": "40960"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4020021149.0000000002AAC000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44744704",
                        "size": "61440"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4037656610.0000000002AB7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44789760",
                        "size": "12288"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4013238294.0000000002A9C000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44679168",
                        "size": "8192"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4003832514.0000000002A91000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "16384",
                        "base_address": "44634112",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4006956873.0000000002AAE000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44752896",
                        "size": "40960"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4052016022.0000000002AAC000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "28672",
                        "base_address": "44744704",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4045133120.0000000002AB9000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44797952",
                        "size": "32768"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4009362571.0000000002A8F000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44625920",
                        "size": "36864"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4725891386.00000000000D0000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "24576",
                        "base_address": "851968",
                        "stage": "MEM_STAGE_EXIT"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4733759389.00000000008EA000.00000040.00000001.01000000.00000003.sdmp",
                        "size": "16384",
                        "base_address": "9347072",
                        "stage": "MEM_STAGE_EXIT"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4733863257.00000000008F0000.00000004.00000001.01000000.00000003.sdmp",
                        "size": "69632",
                        "base_address": "9371648",
                        "stage": "MEM_STAGE_EXIT"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4053059860.0000000002ACE000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44883968",
                        "size": "45056"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4013174785.0000000002A98000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "12288",
                        "base_address": "44662784",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3998485081.0000000002A97000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44658688",
                        "size": "4096"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4737287936.0000000005BEC000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "81920",
                        "base_address": "96387072",
                        "stage": "MEM_STAGE_EXIT"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4048804357.0000000002AAC000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44744704",
                        "size": "28672"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4045687309.0000000002A90000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44630016",
                        "size": "24576"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4005332275.0000000002A9E000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44687360",
                        "size": "65536"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4019386609.0000000002A9C000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44679168",
                        "size": "65536"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4735021645.000000000545F000.00000004.00000010.00020000.00000000.sdmp",
                        "size": "4096",
                        "base_address": "88469504",
                        "stage": "MEM_STAGE_EXIT"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4050682987.0000000002A8F000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44625920",
                        "size": "28672"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4047408671.0000000002AB9000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44797952",
                        "size": "28672"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4033294793.0000000002A9D000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44683264",
                        "size": "86016"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4735096415.000000000585E000.00000004.00000010.00020000.00000000.sdmp",
                        "size": "8192",
                        "base_address": "92659712",
                        "stage": "MEM_STAGE_EXIT"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4037152198.0000000002AB7000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "12288",
                        "base_address": "44789760",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3783082496.0000000000116000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "28672",
                        "base_address": "1138688",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4054694906.0000000002A95000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44650496",
                        "size": "102400"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4034691774.0000000002AC9000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44863488",
                        "size": "32768"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4734696648.0000000002AA9000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_EXIT",
                        "base_address": "44732416",
                        "size": "12288"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4045239264.0000000002AC6000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44851200",
                        "size": "16384"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3989203434.0000000005933000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "167936",
                        "base_address": "93532160",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3988497370.0000000005B75000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "95899648",
                        "size": "16384"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4034947139.0000000002ABB000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44806144",
                        "size": "49152"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4054119180.0000000002AD7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44920832",
                        "size": "8192"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4018979853.0000000002ABC000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44810240",
                        "size": "4096"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3986796732.0000000005C08000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "36864",
                        "base_address": "96501760",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3996690471.0000000002A9F000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44691456",
                        "size": "32768"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4019092549.0000000002AA6000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44720128",
                        "size": "24576"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4006627997.0000000002A95000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44650496",
                        "size": "20480"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4010122598.0000000002AB8000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44793856",
                        "size": "20480"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4737017644.0000000005BC2000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_EXIT",
                        "base_address": "96215040",
                        "size": "12288"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4733650132.00000000008D3000.00000040.00000001.01000000.00000003.sdmp",
                        "size": "69632",
                        "base_address": "9252864",
                        "stage": "MEM_STAGE_EXIT"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4031269270.0000000002ABC000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44810240",
                        "size": "45056"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4031995747.0000000002A9D000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44683264",
                        "size": "86016"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4035430962.0000000002AC9000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44863488",
                        "size": "32768"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4019770715.0000000002A9E000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44687360",
                        "size": "94208"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4048207332.0000000002A9B000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44675072",
                        "size": "98304"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3986855662.0000000005C15000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "53248",
                        "base_address": "96555008",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4016938087.0000000002A98000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44662784",
                        "size": "24576"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4044333796.0000000002AD8000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "4096",
                        "base_address": "44924928",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4053600854.0000000002AAE000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44752896",
                        "size": "45056"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4736791880.0000000005B8C000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_EXIT",
                        "base_address": "95993856",
                        "size": "12288"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4021235016.0000000002AA5000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44716032",
                        "size": "57344"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4005570815.0000000002A9E000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44687360",
                        "size": "86016"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4013836750.0000000002A8C000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44613632",
                        "size": "12288"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4039646272.0000000002ABA000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44802048",
                        "size": "94208"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3997774994.0000000002AA9000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44732416",
                        "size": "24576"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3998976426.0000000002AA3000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44707840",
                        "size": "49152"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4018666955.0000000002AAC000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "20480",
                        "base_address": "44744704",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3986980724.0000000005BB9000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "96178176",
                        "size": "49152"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4733533456.000000000088A000.00000040.00000001.01000000.00000003.sdmp",
                        "size": "4096",
                        "base_address": "8953856",
                        "stage": "MEM_STAGE_EXIT"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4044109619.0000000002AB7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44789760",
                        "size": "40960"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4031731160.0000000002AAC000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "24576",
                        "base_address": "44744704",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4047600514.0000000002A92000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44638208",
                        "size": "20480"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4015637038.0000000002AA2000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44703744",
                        "size": "61440"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4022889776.0000000002AA8000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44728320",
                        "size": "16384"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4048054520.0000000002A94000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "16384",
                        "base_address": "44646400",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4002016909.0000000002AA6000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44720128",
                        "size": "53248"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4015821591.0000000002AB7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44789760",
                        "size": "24576"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3996821186.0000000002AAE000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "4096",
                        "base_address": "44752896",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4736553371.0000000005B60000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_EXIT",
                        "base_address": "95813632",
                        "size": "4096"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4031533653.0000000002AC4000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "12288",
                        "base_address": "44843008",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3997011276.0000000002AA3000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44707840",
                        "size": "49152"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4014592623.0000000002A98000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44662784",
                        "size": "45056"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4736886883.0000000005BA5000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "12288",
                        "base_address": "96096256",
                        "stage": "MEM_STAGE_EXIT"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4013953563.0000000002AAE000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44752896",
                        "size": "61440"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4727126622.000000000015A000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "16384",
                        "base_address": "1417216",
                        "stage": "MEM_STAGE_EXIT"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3987457625.0000000005BEC000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "81920",
                        "base_address": "96387072",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4733060915.000000000080E000.00000040.00000001.01000000.00000003.sdmp",
                        "size": "212992",
                        "base_address": "8445952",
                        "stage": "MEM_STAGE_EXIT"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4045763197.0000000002AAC000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "28672",
                        "base_address": "44744704",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4016558919.0000000002A98000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "12288",
                        "base_address": "44662784",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4015962945.0000000002A95000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44650496",
                        "size": "12288"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3988196143.0000000005B95000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "96030720",
                        "size": "24576"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4733835284.00000000008EF000.00000040.00000001.01000000.00000003.sdmp",
                        "size": "4096",
                        "base_address": "9367552",
                        "stage": "MEM_STAGE_EXIT"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4050288119.0000000002A96000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "8192",
                        "base_address": "44654592",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4012081494.0000000002AA7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44724224",
                        "size": "45056"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4006815150.0000000002AA7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44724224",
                        "size": "69632"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4019146778.0000000002ABC000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44810240",
                        "size": "4096"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3819405831.0000000000127000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "28672",
                        "base_address": "1208320",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4734177040.00000000012A0000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "12288",
                        "base_address": "19529728",
                        "stage": "MEM_STAGE_EXIT"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3998708789.0000000002A91000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "16384",
                        "base_address": "44634112",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4032233555.0000000002AB7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44789760",
                        "size": "106496"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4002918121.0000000002A9A000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44670976",
                        "size": "102400"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4004776007.0000000002AA7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44724224",
                        "size": "49152"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3998198879.0000000002A97000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44658688",
                        "size": "4096"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4015870554.0000000002A9E000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44687360",
                        "size": "57344"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4727983909.0000000000400000.00000002.00000001.01000000.00000003.sdmp",
                        "size": "4096",
                        "base_address": "4194304",
                        "stage": "MEM_STAGE_EXIT"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4004381293.0000000002A91000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "16384",
                        "base_address": "44634112",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4011656979.0000000002AA7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44724224",
                        "size": "28672"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3995765211.0000000002AA4000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44711936",
                        "size": "45056"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3999656242.0000000002AA3000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "16384",
                        "base_address": "44707840",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4013879035.0000000002A8F000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44625920",
                        "size": "61440"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4010646453.0000000002ABB000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44806144",
                        "size": "8192"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3996320948.0000000002AAC000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44744704",
                        "size": "12288"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4044293766.0000000002ACB000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44871680",
                        "size": "4096"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4004470266.0000000002A97000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44658688",
                        "size": "4096"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4045542059.0000000002AB7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44789760",
                        "size": "8192"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4043102825.0000000002A8F000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44625920",
                        "size": "28672"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4004140475.0000000002A9E000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44687360",
                        "size": "86016"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4021402773.0000000002AA3000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44707840",
                        "size": "106496"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4040660543.0000000002AB7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44789760",
                        "size": "12288"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4006488551.0000000002A8F000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44625920",
                        "size": "61440"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4733972532.0000000000B0A000.00000004.00000010.00020000.00000000.sdmp",
                        "size": "24576",
                        "base_address": "11575296",
                        "stage": "MEM_STAGE_EXIT"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4030449336.0000000002AC9000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44863488",
                        "size": "4096"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4010178697.0000000002A9E000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "20480",
                        "base_address": "44687360",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4030376976.0000000002AC9000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "4096",
                        "base_address": "44863488",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3994908861.0000000002AA9000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "20480",
                        "base_address": "44732416",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3988020173.0000000005BBD000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "12288",
                        "base_address": "96194560",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4036062852.0000000002AC9000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44863488",
                        "size": "32768"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4008231018.0000000002AB8000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44793856",
                        "size": "20480"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4002302553.0000000002A9D000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "4096",
                        "base_address": "44683264",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3988958017.0000000005B61000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "95817728",
                        "size": "57344"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3985890086.0000000005C01000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "4096",
                        "base_address": "96473088",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3989590517.000000000595E000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "4096",
                        "base_address": "93708288",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4036253821.0000000002AB7000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "45056",
                        "base_address": "44789760",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4055064577.0000000002AD2000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44900352",
                        "size": "28672"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4014311273.0000000002AB2000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44769280",
                        "size": "45056"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3987559979.0000000005C06000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "8192",
                        "base_address": "96493568",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4013794473.0000000002A98000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44662784",
                        "size": "24576"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4055839037.0000000002AAE000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "90112",
                        "base_address": "44752896",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4054419778.0000000002AAE000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "57344",
                        "base_address": "44752896",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4024007432.0000000002AB8000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44793856",
                        "size": "20480"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4001908520.0000000002AA6000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "53248",
                        "base_address": "44720128",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4019013992.0000000002A9E000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44687360",
                        "size": "57344"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4032786147.0000000002AAC000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "24576",
                        "base_address": "44744704",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3986387394.0000000005BEC000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "81920",
                        "base_address": "96387072",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3999302855.0000000002A9F000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44691456",
                        "size": "16384"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4035606629.0000000002A8F000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44625920",
                        "size": "118784"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3988823999.0000000005B99000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "8192",
                        "base_address": "96047104",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4733808768.00000000008EE000.00000080.00000001.01000000.00000003.sdmp",
                        "size": "4096",
                        "base_address": "9363456",
                        "stage": "MEM_STAGE_EXIT"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4734887129.000000000505C000.00000004.00000010.00020000.00000000.sdmp",
                        "size": "16384",
                        "base_address": "84262912",
                        "stage": "MEM_STAGE_EXIT"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4029528576.0000000002AC9000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "4096",
                        "base_address": "44863488",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4737417545.0000000005C01000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "4096",
                        "base_address": "96473088",
                        "stage": "MEM_STAGE_EXIT"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4012533943.0000000002A8F000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44625920",
                        "size": "61440"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4056289768.0000000002AD8000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "4096",
                        "base_address": "44924928",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4033690086.0000000002AB7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44789760",
                        "size": "65536"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4734255421.00000000012AD000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "8192",
                        "base_address": "19582976",
                        "stage": "MEM_STAGE_EXIT"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4056128282.0000000002AD8000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44924928",
                        "size": "4096"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4056093998.0000000002AD8000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "4096",
                        "base_address": "44924928",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4024488909.0000000002AAC000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "24576",
                        "base_address": "44744704",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4007340142.0000000002AA7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44724224",
                        "size": "28672"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4022317364.0000000002ABB000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44806144",
                        "size": "8192"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4045825154.0000000002AB7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44789760",
                        "size": "36864"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4044676095.0000000002A90000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "12288",
                        "base_address": "44630016",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4047478053.0000000002AC5000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44847104",
                        "size": "81920"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4053527862.0000000002ABD000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "36864",
                        "base_address": "44814336",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4003607529.0000000002A9E000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44687360",
                        "size": "32768"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4054576211.0000000002AD2000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44900352",
                        "size": "28672"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4033204353.0000000002A8F000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "24576",
                        "base_address": "44625920",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4006576638.0000000002A9A000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44670976",
                        "size": "16384"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4001767705.0000000002A97000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "16384",
                        "base_address": "44658688",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4047047088.0000000002A91000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "20480",
                        "base_address": "44634112",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4012644172.0000000002A98000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44662784",
                        "size": "24576"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4051522353.0000000002A9B000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44675072",
                        "size": "49152"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3987336676.0000000005BDC000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "40960",
                        "base_address": "96321536",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4047921070.0000000002AC7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44855296",
                        "size": "73728"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4036845271.0000000002ACF000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44888064",
                        "size": "8192"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4041845620.0000000002AAC000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44744704",
                        "size": "28672"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4051008152.0000000002AAC000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "28672",
                        "base_address": "44744704",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4019246509.0000000002A93000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44642304",
                        "size": "102400"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4013393062.0000000002AA7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44724224",
                        "size": "49152"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4002136461.0000000002AAF000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "16384",
                        "base_address": "44756992",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4029685179.0000000002A8F000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "49152",
                        "base_address": "44625920",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3996142179.0000000002A97000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44658688",
                        "size": "53248"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4021955792.0000000002A9A000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44670976",
                        "size": "143360"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4042580922.0000000002AC7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44855296",
                        "size": "40960"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4002356636.0000000002A91000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "16384",
                        "base_address": "44634112",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4006061510.0000000002AA6000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44720128",
                        "size": "53248"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3987533726.0000000005C01000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "4096",
                        "base_address": "96473088",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4017831929.0000000002AAC000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "20480",
                        "base_address": "44744704",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3782668805.0000000000116000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "28672",
                        "base_address": "1138688",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4009600150.0000000002AA7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44724224",
                        "size": "90112"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4028038466.0000000002ABD000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "24576",
                        "base_address": "44814336",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4010055892.0000000002A91000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44634112",
                        "size": "28672"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4005073173.0000000002A97000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44658688",
                        "size": "114688"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4032588017.0000000002ABC000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44810240",
                        "size": "57344"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4024205842.0000000002AA2000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44703744",
                        "size": "40960"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4030911212.0000000002AB7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44789760",
                        "size": "65536"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4005718865.0000000002A8F000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "16384",
                        "base_address": "44625920",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4055133068.0000000002AD6000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44916736",
                        "size": "12288"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4018923487.0000000002AAC000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "20480",
                        "base_address": "44744704",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3988430941.0000000005B7A000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "95920128",
                        "size": "12288"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4052154990.0000000002AB7000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "36864",
                        "base_address": "44789760",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4022479765.0000000002A8F000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "24576",
                        "base_address": "44625920",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4008003780.0000000002AB7000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44789760",
                        "size": "24576"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4049194255.0000000002AAC000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "28672",
                        "base_address": "44744704",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4025486876.0000000002A9C000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44679168",
                        "size": "65536"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4733505140.0000000000886000.00000040.00000001.01000000.00000003.sdmp",
                        "size": "4096",
                        "base_address": "8937472",
                        "stage": "MEM_STAGE_EXIT"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4038653494.0000000002AD0000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44892160",
                        "size": "4096"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4018710295.0000000002ABC000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "4096",
                        "base_address": "44810240",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4007173933.0000000002AB2000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44769280",
                        "size": "45056"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4010850749.0000000002A9E000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "20480",
                        "base_address": "44687360",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4042116826.0000000002ACC000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44875776",
                        "size": "20480"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4047866119.0000000002AB8000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44793856",
                        "size": "4096"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4734215615.00000000012A4000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "12288",
                        "base_address": "19546112",
                        "stage": "MEM_STAGE_EXIT"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4735058670.000000000565F000.00000004.00000010.00020000.00000000.sdmp",
                        "size": "4096",
                        "base_address": "90566656",
                        "stage": "MEM_STAGE_EXIT"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4015021424.0000000002AA6000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44720128",
                        "size": "24576"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4056787570.0000000002AD4000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44908544",
                        "size": "8192"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4053322183.0000000002A9C000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44679168",
                        "size": "118784"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4007474889.0000000002A9A000.00000004.00000020.00020000.00000000.sdmp",
                        "refs": [
                            {
                                "ref": "#signature_matches",
                                "value": "238"
                            }
                        ],
                        "stage": "MEM_STAGE_FREE",
                        "base_address": "44670976",
                        "size": "16384"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.3986101269.0000000005C15000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "53248",
                        "base_address": "96555008",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4011537524.0000000002A9E000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "20480",
                        "base_address": "44687360",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000003.4056564120.0000000002AD8000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "4096",
                        "base_address": "44924928",
                        "stage": "MEM_STAGE_FREE"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4727661403.00000000001A3000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "69632",
                        "base_address": "1716224",
                        "stage": "MEM_STAGE_EXIT"
                    },
                    {
                        "process": "C:\\Users\\user\\Desktop\\program.exe",
                        "file_name": "00000000.00000002.4726329372.0000000000103000.00000004.00000020.00020000.00000000.sdmp",
                        "size": "40960",
                        "base_address": "1060864",
                        "stage": "MEM_STAGE_EXIT"
                    }
                ],
                "has_html_report": true,
                "has_memdump": true,
                "tls": [
                    {
                        "ja3": "37f463bf4616ecd445d4a1937da06e19",
                        "sni": "cygwin.com",
                        "version": "TLS 1.2",
                        "thumbprint": "576089cf2ead1e3ae47d52c0547d0aecf841ddf0",
                        "serial_number": "0403062850b082729a379cce564788cc337c",
                        "subject": {
                            "CN": "cygwin.com"
                        },
                        "ja3s": "567bb420d39046dbfd1f68b558d86382",
                        "issuer": {
                            "C": "US",
                            "CN": "R3"
                        }
                    }
                ],
                "verdicts": [
                    "CLEAN"
                ],
                "ja3_digests": [
                    "37f463bf4616ecd445d4a1937da06e19"
                ],
                "files_written": [
                    "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\History",
                    "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache",
                    "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\WIKWAFRE\\mirrors[1].lst",
                    "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCookies",
                    "C:\\cygwin64",
                    "C:\\cygwin64\\var",
                    "C:\\cygwin64\\var\\log",
                    "\\Device\\ConDrv\\Connect",
                    "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\ETCJ2WHM\\mirrors[1].lst",
                    "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\ETCJ2WHM",
                    "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\R0IAZP7Z\\mirrors[1].lst",
                    "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\R0IAZP7Z"
                ],
                "has_pcap": true,
                "dns_lookups": [
                    {
                        "resolved_ips": [
                            "8.43.85.97"
                        ],
                        "hostname": "cygwin.com"
                    },
                    {
                        "resolved_ips": [
                            "87.248.205.0",
                            "208.111.186.140",
                            "87.248.202.1",
                            "178.79.208.1",
                            "208.111.186.0",
                            "208.111.186.128"
                        ],
                        "hostname": "windowsupdatebg.s.llnwi.net"
                    },
                    {
                        "resolved_ips": [
                            "13.107.4.50"
                        ],
                        "hostname": "c-0001.c-msedge.net"
                    },
                    {
                        "hostname": "au.c-0001.c-msedge.net"
                    }
                ],
                "files_dropped": [
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\WIKWAFRE\\mirrors[1].lst",
                        "sha256": "010e06fc0e1dc130ed311573e22298b3a2c2cd115ec0ceb330b962106e1cc657",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\ETCJ2WHM\\mirrors[1].lst",
                        "sha256": "2d21f8e403d90a0f5f936e7b8eb43d7ea1d219074a6aef7554a8cd07a6c0b6da",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\ETCJ2WHM\\mirrors[1].lst",
                        "sha256": "96ff47b27825dda73368d1fa71db27beceaa96d5d9d9d79d73889639cc24ad55",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\WIKWAFRE\\mirrors[1].lst",
                        "sha256": "f2886fb6d5fe7dcbb8ac4ddfbef558d20b9ffac32ecf676247017c6f28b26b42",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\WIKWAFRE\\mirrors[1].lst",
                        "sha256": "d69015dd3addb05816782d3ae8b6a6c3f5f5ab2c90a61eef9ebcbe8d85e6d0ce",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\ETCJ2WHM\\mirrors[1].lst",
                        "sha256": "ab0a919116d36bdb425b75bcc507bb7e9f78a297cf5c13e2b00dc797fca19780",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\WIKWAFRE\\mirrors[1].lst",
                        "sha256": "55a9546e00d37dd40d38d3654bec55ef93a540f0e1a0c67cc2d14d209defca35",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\ETCJ2WHM\\mirrors[1].lst",
                        "sha256": "55a9546e00d37dd40d38d3654bec55ef93a540f0e1a0c67cc2d14d209defca35",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\ETCJ2WHM\\mirrors[1].lst",
                        "sha256": "728c65b874c4c5309d9c7ef26b080f312e99156af940486cc3328f17d8ffe74f",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\ETCJ2WHM\\mirrors[1].lst",
                        "sha256": "4c264858d85ab04d83531859a646cf238862adb346be08d405def3255026bab1",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\ETCJ2WHM\\mirrors[1].lst",
                        "sha256": "9b1f59b3bd39425706d38f3c95772ba7f80068970295e190489620b925cc6a0d",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\R0IAZP7Z\\mirrors[1].lst",
                        "sha256": "2d21f8e403d90a0f5f936e7b8eb43d7ea1d219074a6aef7554a8cd07a6c0b6da",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\ETCJ2WHM\\mirrors[1].lst",
                        "sha256": "40218bfafedfe5ce15d4b443394c39eae6ec40ecf080f6c9440bb713567f61af",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\R0IAZP7Z\\mirrors[1].lst",
                        "sha256": "3649419a11a2468f02b21d1d1f54d4de4e639b42c71845e4304eed72a2c6151a",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\ETCJ2WHM\\mirrors[1].lst",
                        "sha256": "4ff1e805019b69e19e4fb6f754fe12915d46dfe6373a370e82e4e760d343df95",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\R0IAZP7Z\\mirrors[1].lst",
                        "sha256": "1558a8abd7a1a8d31310961a99ad04bd58cca2a38fdda54cd9c88ff83bc5bd6b",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\ETCJ2WHM\\mirrors[1].lst",
                        "sha256": "184edc88ed81c3056ac4d431232523707e08c6fb4b3fa540a54a4994822e891b",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\R0IAZP7Z\\mirrors[1].lst",
                        "sha256": "7e1710a13c387c714152293b7a18a6e5467dcab4635249f8971a9297995b9f50",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\R0IAZP7Z\\mirrors[1].lst",
                        "sha256": "a095a6e62e173f8128c040e785d240d1241977d96c48b1d2de137fdee230f748",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\ETCJ2WHM\\mirrors[1].lst",
                        "sha256": "65865ea1b6c364345dda7018544d48e9584fc2a70d6cc7bd4a7f35be244abbeb",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\ETCJ2WHM\\mirrors[1].lst",
                        "sha256": "979040e186574ee82bdfdc489af1a0c2fe79e220e34faeddc6cec7fdfa49423e",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\R0IAZP7Z\\mirrors[1].lst",
                        "sha256": "ccfc9ef8448843747c2b90f8f018e3e0b3738ff373aea4efa9115ad44d18025d",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\R0IAZP7Z\\mirrors[1].lst",
                        "sha256": "3c614b0c104028afd0ee97eb84d4f63f38da005268b2707941628a20a4f2f099",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\ETCJ2WHM\\mirrors[1].lst",
                        "sha256": "7e1710a13c387c714152293b7a18a6e5467dcab4635249f8971a9297995b9f50",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\ETCJ2WHM\\mirrors[1].lst",
                        "sha256": "c7c5426c3ca81941c52cb8497ef99ced0acc12dff4cbe33ad9ddfd6b4cdcc930",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\R0IAZP7Z\\mirrors[1].lst",
                        "sha256": "ae6a6e1e1efb906d3dc510c26b96b1611b08fbd07ef1f17434e84b32ca0d6a3f",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\R0IAZP7Z\\mirrors[1].lst",
                        "sha256": "f06ded0a73bb4c0789a0d2e00b21d86894942917ab2e0b1488c443dc68f77571",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\ETCJ2WHM\\mirrors[1].lst",
                        "sha256": "69542e2ac46b793e56ae31ff379ae15b2d7733b6b75b9e7b4279a789add1b8d9",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\ETCJ2WHM\\mirrors[1].lst",
                        "sha256": "06abbdc423b46a1653cec6c087780f7ed67e671b17a167a5b3efc227b73b5abb",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\ETCJ2WHM\\mirrors[1].lst",
                        "sha256": "154587ca83210ce0c9b1ddcbc2550771d73d99817cf1e79cc0ff45dd3a0d5ab2",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\ETCJ2WHM\\mirrors[1].lst",
                        "sha256": "a015d3efbea036dd2d49eeaeb5517ea2a435581e359ffd849b8dacc685097110",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\R0IAZP7Z\\mirrors[1].lst",
                        "sha256": "a27d154eb30d914a5febe44db3bc855a4b12dfb461135e579f8ca93b13880b6c",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\R0IAZP7Z\\mirrors[1].lst",
                        "sha256": "71477cd5de3fa02e5ca21c531412f3bd15f85ee2b359f363a43f62f9b6dbaedc",
                        "type": "TEXT"
                    },
                    {
                        "path": "C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\ETCJ2WHM\\mirrors[1].lst",
                        "sha256": "012fe5f723fe67fca256baa151bbc47f912d3fee8f4deae9c8a7eddb3743a83d",
                        "type": "TEXT"
                    }
                ],
                "behash": "7d3c3f3386c9be1f5441f4b12ddc1edc",
                "has_evtx": true
            },
            "type": "file_behaviour",
            "id": "edd0a64dc65087ffe453ca94b267169b39458a983b29ac31320fcaa983d0f97e_Zenbox",
            "links": {
                "self": "https://www.virustotal.com/api/v3/file_behaviours/edd0a64dc65087ffe453ca94b267169b39458a983b29ac31320fcaa983d0f97e_Zenbox"
            }
        }
    ],
    "links": {
        "self": "https://www.virustotal.com/api/v3/files/edd0a64dc65087ffe453ca94b267169b39458a983b29ac31320fcaa983d0f97e/behaviours?limit=10"
    }
```

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
      "name": "Files Behaviours"
    }
  ],
  "paths": {
    "/files/{id}/behaviours": {
      "get": {
        "tags": [
          "Files Behaviours"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "get-all-behavior-reports-for-a-file",
        "parameters": [
          {
            "description": "SHA-256, SHA-1 or MD5 identifying the file",
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
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
        "summary": "Get all behavior reports for a file"
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

← [Get a summary of all behavior reports for a file](file-all-behaviours-summary.md) · [up](../README.md) · [URLs](../urls.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-all-behavior-reports-for-a-file>.*
