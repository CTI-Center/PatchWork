---
title: "Files Behaviour"
source: https://gtidocs.virustotal.com/reference/file-behaviour-summary-object
slug: file-behaviour-summary-object
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-29T14:22:17.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Files Behaviour

---

# files-behaviour

File behaviour reports

File behaviour reports are obtained either by using the [GET /files/\{id}/behaviours](../03-ioc-investigation/files/files-relationships.md) endpoint or the [sandbox behavior feed](../12-ioc-feeds/sandbox-analyses-feed/feeds-file-behaviour.md) . They summarize the observed behaviour during the execution or opening of a file. Note that some of these actions could be triggered by children of the file under consideration.

## object-attributes

In a file\_behaviour object you will find these attributes:

* `analysis_date`: <*integer*> Unix epoch UTC time (seconds).
* `behash`: <*string*> used to find similar behaviour analyses.
* `calls_highlighted`: <*list of strings*> API calls/Syscalls worth highlighting.
* `command_executions`: <*list of strings*> shell command executions observed during the analysis of the given file.
* `files_opened`: <*list of strings*>  files opened during execution.
* `files_written`: <*list of strings*>   files written to during execution.
* `files_deleted`  <*list of strings*> names of the files deleted.
* `files_attribute_changed`: <*list of strings*> full path of files subject to some sort of active attribute modification.
* `has_html_report`: \<boolean> whether there is an HTML report for this behaviour analysis.
* `has_evtx`: \<boolean> whether there is a EVTX file for this behaviour analysis. Check out [/file\_behaviours/\{sandbox\_id}/evtx](#file-behaviour-evtx) for more information.
* `has_memdump`: \<boolean> whether there is a memdump file for this behaviour analysis. Check out [/file\_behaviours/\{sandbox\_id}/memdump](#file-behaviour-memdump).
* `has_pcap`: \<boolean> whether there is a PCAP network capture for this behaviour analysis. Check out [/file\_behaviours/\{sandbox\_id}/pcap](#file_behaviours_pcap) for more information.
* `hosts_file`: <*string*> the hosts file field stores the content of the local hostname-ip mapping  hosts file IF AND ONLY IF the file was modified, else this field is not  populated.
* `ids_alerts`: <*list of dictionaries*> list of IDS alerts, sorted by timestamp. Every item contains the following keys:
  * `alert_context`: <*dictionary*> matched alert context:
    * `dest_ip`: <*string*> destination IP.
    * `dest_port`: <*integer*> destination port.
    * `hostname`: <*string*> if the alert is related to an HTTP communication, destination hostname.
    * `protocol`: <*string*> communication protocol name.
    * `src_ip`: <*string*> source IP.
    * `src_port`: <*integer*> source port.
    * `url`: <*string*> if the alert is related to an HTTP communication, destination URL.
  * `alert_severity`: <*string*> one of `high`, `medium`, `low` or `info`.
  * `rule_category`: <*string*> alert category.
  * `rule_id`: <*string*> rule SID.
  * `rule_msg`: <*string*> alert description.
  * `rule_source`: <*string*> rule source, determined by SID range.
* `processes_terminated`: <*list of strings*> name of the processes that were terminated during the execution of a given file.
* `processes_killed`: <*list of strings*> name of the processes that were killed during the execution of a given file.
* `processes_injected`: <*list of strings*> name of the processes that were subjected to some kind of code injection during the execution of the given file.
* `services_opened`: <*list of strings*> names of the services for which a handle was acquired during the analysis of the given file.
* `services_created`: <*list of strings*> new services created.
* `services_started`: <*list of strings*>  new services started.
* `services_stopped`: <*list of strings*> services stopped during the execution of the given file.
* `services_deleted`: <*list of strings*> services deleted during the execution of the given file.
* `services_bound`: <*list of strings*> service binding, mainly in Android, see: <[https://developer.android.com/guide/components/bound-services.html>](https://developer.android.com/guide/components/bound-services.html>).
* `windows_searched`: <*list of strings*> names of windows that are searched for.
* `windows_hidden`: <*list of strings*>  names of windows that are set up to be invisible.
* `mutexes_opened`: <*list of strings*> name of the mutexes for which the file acquires a handle.
* `mutexes_created`: <*list of strings*> new mutexes created.
* `signals_observed`: <*list of strings*> OS Signals and broadcast events, note that Android broadcasts are categorized here also.
* `invokes`: <*list of strings*> method/functionality called via reflection or some sort of runtime instantiation. The best example are Java reflection calls, in those cases we flatten the structure to a string: \<class>.\<method>.
* `crypto_algorithms_observed`: <*list of strings*> Example: RSA.
* `crypto_keys`: <*list of strings*> e.g. "MySecret".
* `crypto_plain_text`: <*list of strings*> strings that are either ciphered or deciphered during the observed time frame, we record just the plaintext.
* `text_decoded`: <*list of strings*> plaintext which is the result of a decoding operation.
* `text_highlighted`  <*list of strings*> interesting text seen in window dialogs, titles, etc.
* `verdict_confidence`: <*integer*> 99 = 99% confident verdict is correct.
* `ja3_digests`: <*list of strings*> [JA3](https://github.com/salesforce/ja3) fingerprinting of TLS client connections.
* `tls`: <*list of dictionaries*> contacted domains/IPs certificates. Each entry contains the following fields:
  * `issuer`: <*dictionary*> certificate issuer information. Keys are certificate fields (C, CN, O, etc) as string and values are always string.
  * `ja3`: <*string*> certificate JA3.
  * `ja3s`: <*string*> certificate JA3s.
  * `serial_number`: <*string*> certificate serial number.
  * `sni`: <*string*> certificate's server name indication.
  * `subject`: <*dictionary*> certificate subject information. Same format as `issuer` field.
  * `thumbprint`: <*string*> certificate thumbprint.
  * `version`: <*string*> TLS version.
* `sigma_analysis_results`: <*list of dictionaries*> aggregated [sigma](https://github.com/SigmaHQ/sigma) analyses results from all sandbox generated EVTX files. Each item contains the following subfields:
  * `rule_title`: <*string*> matched sigma rule title.
  * `rule_source`: <*string*> sigma ruleset where this rule belongs to.
  * `match_context`: <*dictionary*> specific matched events. This dictionary contains the following key:
    * `values`: <*list of map\<str, str>>* all matched events represented as key-value.
  * `rule_level`: <*string*> rule level, can be either of "critical", "high", "medium", "low".
  * `rule_description`: <*string*> rule description
  * `rule_author`: <*string*> rule author
  * `rule_id`: <*string*> rule ID in VirusTotal. You can use this to find other files matching this same rule.
* `signature_matches`: <*list of dictionaries*>  aggregated list of matching signatures. Each item contains the following subfields:
  * `format`: <*string*> any of the following formats: SIG\_FORMAT\_UNKNOWN, SIG\_FORMAT\_YARA, SIG\_FORMAT\_SIGMA, SIG\_FORMAT\_CAPA or SIG\_FORMAT\_OPENIOC.
  * `authors`: <*dictionary*> list of authors.
  * `rule_src`: <*string*> rule source.
  * `name`: <*string*> rule name.
  * `description`: <*string*> rule description.
* `mitre_attack_techniques`: < \_list of dictionaries\_> aggregated list of mitre attack techniques. Each item contains the following subfields:
  * `signature_description`: <*string*> description.
  * `id`: <*string*> identifier.
  * `severity`: <*string*> severity.

Android specific fields:

* `activities_started`: <*list of strings*> Android activities launched by the app under study.
* `content_model_observers`: <*list of strings*> content for which an Android app registers logic to be informed about any changes to it.
* `content_model_sets`: <*list of dictionaries*> content model entries performed by an Android app.
* `databases_deleted`: <*list of strings*> e.g. Android SQLite DBs deleted.
* `databases_opened`: <*list of strings*> interactions with databases, e.g. when an Android app opens an SQLite DB.
* `permissions_requested`: <*list of strings*> Android permissions requested by the app during runtime. In Windows it should also record process token privilege modifications such as SE\_LOAD\_DRIVER\_PRIVILEGE.
* `shared_preferences_lookups`: <*list of strings*> entries in Android's shared preferences that are checked (<[https://developer.android.com/reference/android/content/SharedPreferences.html>](https://developer.android.com/reference/android/content/SharedPreferences.html>)).
* `shared_preferences_sets`: <*list of dictionaries*> entries written in Android's shared preferences. Every subitem contains the following fields:
  * `key`: <*string*> preference name.
  * `value`: <*string*> set value.
* `signals_hooked`: <*list of strings*> registering a receiver in Android is considered as a broadcast hook. In windows this field will contain `SetWindowsHookExA` activity and the like.
* `system_property_lookups`: <*list of strings*> interactions with Android's system properties dataset (getInt, getString, putInt, putString, etc. all get simply translated into strings. android.os.SystemProperties.).
* `system_property_sets`: <*list of dictionaries*> keys and values set in Android's system properties dataset.

Windows specific fields:

* `modules_loaded`: <*list of strings*> operations related to dynamic loading of libraries, shared objects and components.
* `registry_keys_opened`: <*list of strings*> Windows registry keys for which a handle is acquired.
* `registry_keys_set`: <*list of dictionaries*> keys and values of registry keys that are set. It is a list of dictionaries, each one containing the following fields:
  * `key`: <*string*> modified registry key.
  * `value`: <*string*> value set to the registry key.
* `registry_keys_deleted`: <*list of strings*> names of Windows registry keys that are deleted.

```json File behaviour report
{
    "data": {
        "attributes": {
            "activities_started": [
                "<string>"
            ],
            "analysis_date": <int:timestamp>,
            "behash": "<string>",
            "calls_highlighted": [
                "<string>"
            ],
            "command_executions": [
                "<string>"
            ],
            "files_opened": [
                "<string>"
            ],
            "files_written": [
                "<string>"
            ],
            "has_html_report": <boolean>,
            "has_pcap": <boolean>,
            "ids_results": [  
              {
                "alert_context": {
                  "dest_ip": "<string>",
                  "dest_port": <int>,
                  "hostname": "<string>",
                  "protocol": "<string>",
                  "src_ip": "<string>",
                  "src_port": <int>,
                  "url": "<string>"
                },
                "alert_severity": "<string>",
                "rule_id": "<string>",
                "rule_msg": "<string>",
                "rule_source": "<string>"
              },
            ],
            "last_modification_date": <int:timestamp>,
            "modules_loaded": [
                "<string>"
            ],
            "mutexes_created": [
                "<string>"
            ],
            "mutexes_opened": [
                "<string>"
            ],
            "processes_created": [
                "<string>"
            ],
            "processes_terminated": [
                "<string>"
            ]
            "registry_keys_deleted": [
                "<string>"
            ],
            "registry_keys_opened": [
                "<string>"
            ],
            "registry_keys_set": [
                {
                    "key": "<string>",
                    "value": "<string>"
                }
            ],
            "sandbox_name": "<string>",
            "shared_preferences_sets": [
                {
                    "key": "<string>",
                    "value": "<string>"
                }
            ],
            "sigma_analysis_results": [{
              "rule_title": "<string>",
              "rule_source": "<string>",
              "match_context": [{
                "values": {
                  "<string>": "<string>"}}],
              "rule_level": "<string>",
              "rule_description": "<string>",
              "rule_author": "<string>",
              "rule_id": "<string>"
            }],
            "tags": [
                "<string>"
            ],
            "text_highlighted": [
                "<string>"
            ],
            "tls": [
                {
                    "issuer": {
                        "<string>": "<string>"
                    },
                    "ja3": "<string>",
                    "ja3s": "<string>",
                    "serial_number": "<string>",
                    "sni": "<string>",
                    "subject": {
                        "<string>": "<string>"
                    },
                    "thumbprint": "<string>",
                    "version": "<string>"
                }
            ],
            "verdicts": [
                "<string>"
            ]
        },
        "id": "<file_sha256>_<sandbox_name>",
        "links": {
            "self": "https://www.virustotal.com/api/v3/file_behaviours/<id>"
        },
        "type": "file_behaviour"
    }
}
```
```json Windows example
{
    "data": {
        "attributes": {
            "analysis_date": 1593304117,
            "behash": "3212c1418311361831dd10d10b1914c2",
            "calls_highlighted": [
                "GetTickCount"
            ],
            "dns_lookups": [
                {
                    "hostname": "blablabla.com",
                    "resolved_ips": [
                        "66.66.66.66"
                    ]
                }
            ],
            "files_dropped": [
                {
                    "path": "C:\\Users\\<USER>\\AppData\\Local\\Temp\\blablabla.virus.tmp",
                    "sha256": "031a4a19f216d1d713f1b710b1eb13131811c113a151716c131c1161c191f15b"
                },
                {
                    "path": "C:\\Users\\<USER>\\AppData\\Local\\Temp\\blablabla.tmp",
                    "sha256": "b20a8d88c550981137ed831f2015f5f11517aeb649c29642d9d61dea5ebc37d1"
                }
            ],
            "files_opened": [
                "C:\\Windows\\syswow64\\en-US\\KERNELBASE.dll.mui",
                "C:\\Windows\\syswow64\\en\\KERNELBASE.dll.mui",
                "C:\\Windows\\system32\\netmsg.dll",
                "C:\\Users\\<USER>\\Downloads\\blablabla.virus.exe",
                "C:\\Users\\<USER>\\AppData\\Local\\Temp"
            ],
            "files_written": [
                "C:\\Users\\<USER>\\AppData\\Local\\Temp\\blablabla.virus.tmp",
                "C:\\Users\\<USER>\\AppData\\Local\\Temp\\blablabla.tmp",
                "C:\\Users\\<USER>\\AppData\\Local\\Temp\\blabla.dll"
            ],
            "has_html_report": true,
            "has_pcap": true,
            "http_conversations": [
                {
                    "request_headers": {
                        "accept": "*/*",
                        "accept-encoding": "gzip, deflate",
                        "connection": "Keep-Alive",
                        "host": "blablabla.com",
                        "user-agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)"
                    },
                    "request_method": "GET",
                    "url": "http://blablabla.com/tempfile/blablabla.virus"
                }
            ],
            "ids_results": [
              {
               "alert_context": {
                   "dest_ip": "234.0.0.12",
                   "protocol": "IGMP",
                   "src_ip": "10.0.44.24"
                },
                "alert_severity": "low",
                "rule_id": "2200007",
                "rule_msg": "SURICATA IPv4 padding required ",
                "rule_source": "Suricata Decoder Events"
              },
            ],
            "ip_traffic": [
                {
                    "destination_ip": "66.66.66.66",
                    "destination_port": 80,
                    "transport_layer_protocol": "TCP"
                }
            ],
            "last_modification_date": 1593304118,
            "modules_loaded": [
                "C:\\Users\\<USER>\\Downloads\\blablabla.virus.ENU",
                "C:\\Users\\<USER>\\Downloads\\blablabla.virus.EN",
                "UxTheme.dll"
            ],
            "mutexes_created": [
                "Local\\blablabla-blablabla-blablabla"
            ],
            "mutexes_opened": [
                "blablabla-blablabla-blablabla"
            ],
            "processes_created": [
                "C:\\Users\\<USER>\\AppData\\Local\\Temp\\blablabla.virus.tmp /SL5=$2A0120,2331237,148992,C:\\Users\\<USER>\\Downloads\\blablabla.virus.exe",
                "C:\\Windows\\system32\\regsvr32.exe /s C:\\Windows\\system32\\jscript.dll"
            ],
            "processes_terminated": [
                "C:\\Windows\\system32\\regsvr32.exe /s C:\\Windows\\system32\\jscript.dll"
            ],
            "processes_tree": [
                {
                    "children": [
                        {
                            "children": [
                                {
                                    "name": "C:\\Windows\\system32\\regsvr32.exe /s C:\\Windows\\system32\\jscript.dll",
                                    "process_id": "2700",
                                    "time_offset": 8
                                }
                            ],
                            "name": "C:\\Users\\<USER>\\AppData\\Local\\Temp\\blablabla.virus.tmp /SL5=$2A0120,2331237,148992,C:\\Users\\<USER>\\Downloads\\blablabla.virus.exe",
                            "process_id": "2372",
                            "time_offset": 1
                        }
                    ],
                    "name": "blablabla.virus.exe",
                    "process_id": "2668"
                }
            ],
            "registry_keys_deleted": [
                "HKCR\\JScript\\CLSID",
                "HKCR\\JScript\\OLEScript",
                "HKCR\\JScript",
                "HKCR\\LiveScript\\CLSID",
                "HKCR\\LiveScript\\OLEScript",
                "HKCR\\LiveScript",
                "HKCR\\JavaScript\\CLSID",
                "HKCR\\JavaScript\\OLEScript",
                "HKCR\\JavaScript",
                "HKCR\\JavaScript1.1\\CLSID",
                "HKCR\\JavaScript1.1\\OLEScript"
            ],
            "registry_keys_opened": [
                "HKCU\\Software\\CodeGear\\Locales",
                "HKCU\\Software\\Borland\\Locales",
                "HKCU\\Software\\Borland\\Delphi\\Locales",
                "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\FontSubstitutes",
                "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\FontSubstitutes\\MS Shell Dlg 2",
                "HKLM\\System\\CurrentControlSet\\Control\\Keyboard Layouts\\04090409",
                "HKLM\\Software\\Microsoft\\Windows\\CurrentVersion",
                "HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\ProgramFilesDir",
                "HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\CommonFilesDir",
                "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion",
            ],
            "registry_keys_set": [
                {
                    "key": "Software\\Microsoft\\RestartManager\\Session0000\\Owner",
                    "value": "ॄ"
                },
                {
                    "key": "Software\\Microsoft\\RestartManager\\Session0000\\SessionHash"
                },
                {
                    "key": "Software\\Microsoft\\RestartManager\\Session0000\\Sequence",
                    "value": "1"
                }
            ],
            "sandbox_name": "VirusTotal Jujubox",
            "sigma_analysis_results": [
              {
                "rule_title": "File deletion via CMD (via cmdline)",
                "rule_source": "SOC Prime Threat Detection Marketplace",
                "match_context": [
                  {
                    "values": {
                      "TerminalSessionId": "0",
                      "ProcessGuid": "C784477D-ED34-629E-4105-000000003000",
                      "ProcessId": "4164",
                      "Product": "Microsoft® Windows® Operating System",
                      "Description": "Windows Command Processor",
                      "Company": "Microsoft Corporation",
                      "ParentProcessGuid": "C784477D-ED16-629E-2305-000000003000",
                      "User": "NT AUTHORITY\\SYSTEM",
                      "Hashes": "MD5=4E2ACF4F8A396486AB4268C94A6A245F,SHA256=9A7C58BD98D70631AA1473F7B57B426DB367D72429A5455B433A05EE251F3236,IMPHASH=8542FB14699D84D7E8DA92F66145C7FE",
                      "OriginalFileName": "Cmd.Exe",
                      "ParentImage": "C:\\Program Files\\rempl\\sedlauncher.exe",
                      "FileVersion": "10.0.17134.1 (WinBuild.160101.0800)",
                      "ParentProcessId": "5204",
                      "CurrentDirectory": "C:\\Windows\\system32\\",
                      "CommandLine": "C:\\Windows\\System32\\cmd.exe /c C:\\Windows\\System32\\ipconfig.exe /flushdns >C:\\Windows\\TEMP\\ipconfig.out 2>&1",
                      "EventID": "1",
                      "LogonGuid": "C784477D-EC60-629E-E703-000000000000",
                      "LogonId": "999",
                      "Image": "C:\\Windows\\System32\\cmd.exe",
                      "IntegrityLevel": "System",
                      "ParentCommandLine": "\"C:\\Program Files\\rempl\\sedlauncher.exe\"",
                      "UtcTime": "2022-06-07 06:16:20.702",
                      "RuleName": "-"
                    }
                  },
                  {
                    "values": {
                      "TerminalSessionId": "0",
                      "ProcessGuid": "C784477D-ED34-629E-4405-000000003000",
                      "ProcessId": "1368",
                      "Product": "Microsoft® Windows® Operating System",
                      "Description": "Windows Command Processor",
                      "Company": "Microsoft Corporation",
                      "ParentProcessGuid": "C784477D-ED16-629E-2305-000000003000",
                      "User": "NT AUTHORITY\\SYSTEM",
                      "Hashes": "MD5=4E2ACF4F8A396486AB4268C94A6A245F,SHA256=9A7C58BD98D70631AA1473F7B57B426DB367D72429A5455B433A05EE251F3236,IMPHASH=8542FB14699D84D7E8DA92F66145C7FE",
                      "OriginalFileName": "Cmd.Exe",
                      "ParentImage": "C:\\Program Files\\rempl\\sedlauncher.exe",
                      "FileVersion": "10.0.17134.1 (WinBuild.160101.0800)",
                      "ParentProcessId": "5204",
                      "CurrentDirectory": "C:\\Windows\\system32\\",
                      "CommandLine": "C:\\Windows\\System32\\cmd.exe /c C:\\Windows\\System32\\netsh.exe interface ip delete arpcache >C:\\Windows\\TEMP\\ipconfig.out 2>&1",
                      "EventID": "1",
                      "LogonGuid": "C784477D-EC60-629E-E703-000000000000",
                      "LogonId": "999",
                      "Image": "C:\\Windows\\System32\\cmd.exe",
                      "IntegrityLevel": "System",
                      "ParentCommandLine": "\"C:\\Program Files\\rempl\\sedlauncher.exe\"",
                      "UtcTime": "2022-06-07 06:16:20.741",
                      "RuleName": "-"
                    }
                  }
                ],
                "rule_level": "high",
                "rule_description": "Detects \"cmd\" utilization to self-delete files in some critical Windows destinations.",
                "rule_author": "Ariel Millahuel",
                "rule_id": "f9333cf120369debd56e4e238fffa10bdb2a1497c11e08a082befd02f9f3bdf2"
            },
            {
              "rule_title": "Failed Code Integrity Checks",
              "rule_source": "Sigma Integrated Rule Set (GitHub)",
              "match_context": [
                {
                  "values": {
                    "EventID": "5038",
                    "param1": "\\Device\\HarddiskVolume4\\Program Files (x86)\\sandbox\\driver\\sandbox-driver.sys"
                  }
                }
              ],
              "rule_level": "low",
              "rule_description": "Code integrity failures may indicate tampered executables.",
              "rule_author": "Thomas Patzke",
              "rule_id": "134564d292d785dff102940b8a1ee06dba2d462c5fb852124b3771a49d7885f1"
            },
            {
              "match_context": [
                {
                  "values": {
                    "TerminalSessionId": "0",
                    "ProcessGuid": "C784477D-ED34-629E-4105-000000003000",
                    "ProcessId": "4164",
                    "Product": "Microsoft® Windows® Operating System",
                    "Description": "Windows Command Processor",
                    "Company": "Microsoft Corporation",
                    "ParentProcessGuid": "C784477D-ED16-629E-2305-000000003000",
                    "User": "NT AUTHORITY\\SYSTEM",
                    "Hashes": "MD5=4E2ACF4F8A396486AB4268C94A6A245F,SHA256=9A7C58BD98D70631AA1473F7B57B426DB367D72429A5455B433A05EE251F3236,IMPHASH=8542FB14699D84D7E8DA92F66145C7FE",
                    "OriginalFileName": "Cmd.Exe",
                    "ParentImage": "C:\\Program Files\\rempl\\sedlauncher.exe",
                    "FileVersion": "10.0.17134.1 (WinBuild.160101.0800)",
                    "ParentProcessId": "5204",
                    "CurrentDirectory": "C:\\Windows\\system32\\",
                    "CommandLine": "C:\\Windows\\System32\\cmd.exe /c C:\\Windows\\System32\\ipconfig.exe /flushdns >C:\\Windows\\TEMP\\ipconfig.out 2>&1",
                    "EventID": "1",
                    "LogonGuid": "C784477D-EC60-629E-E703-000000000000",
                    "LogonId": "999",
                    "Image": "C:\\Windows\\System32\\cmd.exe",
                    "IntegrityLevel": "System",
                    "ParentCommandLine": "\"C:\\Program Files\\rempl\\sedlauncher.exe\"",
                    "UtcTime": "2022-06-07 06:16:20.702",
                    "RuleName": "-"
                  }
                },
                {
                  "values": {
                    "TerminalSessionId": "0",
                    "ProcessGuid": "C784477D-ED34-629E-4405-000000003000",
                    "ProcessId": "1368",
                    "Product": "Microsoft® Windows® Operating System",
                    "Description": "Windows Command Processor",
                    "Company": "Microsoft Corporation",
                    "ParentProcessGuid": "C784477D-ED16-629E-2305-000000003000",
                    "User": "NT AUTHORITY\\SYSTEM",
                    "Hashes": "MD5=4E2ACF4F8A396486AB4268C94A6A245F,SHA256=9A7C58BD98D70631AA1473F7B57B426DB367D72429A5455B433A05EE251F3236,IMPHASH=8542FB14699D84D7E8DA92F66145C7FE",
                    "OriginalFileName": "Cmd.Exe",
                    "ParentImage": "C:\\Program Files\\rempl\\sedlauncher.exe",
                    "FileVersion": "10.0.17134.1 (WinBuild.160101.0800)",
                    "ParentProcessId": "5204",
                    "CurrentDirectory": "C:\\Windows\\system32\\",
                    "CommandLine": "C:\\Windows\\System32\\cmd.exe /c C:\\Windows\\System32\\netsh.exe interface ip delete arpcache >C:\\Windows\\TEMP\\ipconfig.out 2>&1",
                    "EventID": "1",
                    "LogonGuid": "C784477D-EC60-629E-E703-000000000000",
                    "LogonId": "999",
                    "Image": "C:\\Windows\\System32\\cmd.exe",
                    "IntegrityLevel": "System",
                    "ParentCommandLine": "\"C:\\Program Files\\rempl\\sedlauncher.exe\"",
                    "UtcTime": "2022-06-07 06:16:20.741",
                    "RuleName": "-"
                  }
                }
              ]
            }
          ],
            "tags": [
                "DIRECT_CPU_CLOCK_ACCESS",
                "RUNTIME_MODULES"
            ],
            "text_highlighted": [
                "Setup",
                "C:\\Windows\\system32\\cmd.exe"
            ],
            "tls": [
                {
                    "issuer": {
                        "C": "US",
                        "CN": "GTS CA 1O1",
                        "O": "Google Trust Services"
                    },
                    "ja3": "28a2c9bd18a11de089ef85a160da29e4",
                    "ja3s": "eca9b8f0f3eae50309eaf901cb822d9b",
                    "serial_number": "00c4ea98ea7e5e1f430200000000870182",
                    "sni": "clients2.google.com",
                    "subject": {
                        "C": "US",
                        "L": "Mountain View",
                        "O": "Google LLC",
                        "ST": "California"
                    },
                    "thumbprint": "c25b1dc8be5f679087ecd28fb5eae7b3985cf604",
                    "version": "TLS 1.2"
                }
            ]
        },
        "id": "5353e23f3653402339c93a8565307c6308ff378e03fcf23a4378f31c434030b0_VirusTotal Jujubox",
        "links": {
            "self": "https://www.virustotal.com/api/v3/file_behaviours/5353e23f3653402339c93a8565307c6308ff378e03fcf23a4378f31c434030b0_VirusTotal Jujubox"
        },
        "type": "file_behaviour"
    }
}
```
```json Android example
{
    "data": {
        "attributes": {
            "activities_started": [
                "com.software.application.Main (com.software.application)",
                "com.blabla.superuser.RequestActivity (com.thirdparty.superuser)"
            ],
            "analysis_date": 1528096752,
            "behash": "3f613ca3cd3a43fd3723539233a23e45",
            "calls_highlighted": [
                "android.telephony.TelephonyManager.getNetworkOperator"
            ],
            "command_executions": [
                "su"
            ],
            "dns_lookups": [
                {
                    "hostname": "blablabla.com",
                    "resolved_ips": [
                        "66.66.66.66"
                    ]
                }
            ],
            "files_copied": [
                {
                    "destination": "/data/data/com.software.application/shared_prefs/PREFS.xml.bak",
                    "source": "/data/data/com.software.application/shared_prefs/PREFS.xml"
                }
            ],
            "files_deleted": [
                "/data/data/com.software.application/shared_prefs/PREFS.xml.bak",
                "/data/data/com.software.application/shared_prefs/PREFS.xml"
            ],
            "files_opened": [
                "/data/data/com.software.application/shared_prefs/PREFS.xml",
                "/data/data/com.software.application/shared_prefs/PREFS.xml.bak"
            ],
            "has_html_report": true,
            "has_pcap": false,
            "http_conversations": [
                {
                    "request_headers": {
                        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                        "accept-encoding": "gzip,deflate",
                        "accept-language": "en-US",
                        "connection": "keep-alive",
                        "host": "www.blablabla.com",
                        "user-agent": "Mozilla/5.0 (Linux; Android 4.4.2; VirtualBox Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Safari/537.36",
                        "x-requested-with": "com.android.browser"
                    },
                    "request_method": "GET",
                    "url": "http://www.blablabla.com/download.php"
                }
            ],
            "ip_traffic": [
                {
                    "destination_ip": "66.66.66.66",
                    "destination_port": 80,
                    "transport_layer_protocol": "TCP"
                }
            ],
            "last_modification_date": 1593383110,
            "sandbox_name": "VirusTotal Droidy",
            "services_opened": [
                "com.google.android.gms.people.service.bg.PeopleBackgroundTasks (com.google.android.gms)",
                "com.google.android.gms.icing.service.IndexWorkerService (com.google.android.gms)",
                "com.google.android.gsf.gtalkservice.PushMessagingRegistrar (com.google.process.gapps)"
            ],
            "shared_preferences_sets": [
                {
                    "key": "NET_OP",
                    "value": "46001"
                },
                {
                    "key": "SMS_DATA_KEY",
                    "value": "blablabla"
                }
            ],
            "signals_hooked": [
                "INTENT_DONE"
            ]
            "system_property_lookups": [
                "debug.force_rtl",
                "debug.second-display.pkg"
            ],
            "tags": [
                "TELEPHONY",
                "SENDS_SMS"
            ],
            "text_highlighted": [
                "Open",
                "This may cause charges on your mobile account.",
                "Remember my choice",
                "Cancel",
                "Send",
                "Download File",
            ]
        },
        "id": "cb41ce8487854d28441b74eef485d4044c7d474942624fde44c364c9c249f438_VirusTotal Droidy",
        "links": {
            "self": "https://www.virustotal.com/api/v3/file_behaviours/cb41ce8487854d28441b74eef485d4044c7d474942624fde44c364c9c249f438_VirusTotal Droidy"
        },
        "type": "file_behaviour"
    }
}
```

## relationships

In addition to the previously described attributes, file behaviour objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](../01-api-introduction/api-responses/introduction-relationships.md)  section.

The following table shows a summary of available relationships.

| Relationship       | Return object type                                          |
| :----------------- | :---------------------------------------------------------- |
| file               | A single [File](file-object.md)                            |
| attack\_techniques | A list of [Attack Techniques](object-attack-techniques.md) |

---

← [powershell_info](file-object/file-object-powershell-info.md) · [up](README.md) · [verdicts](file-behaviour-summary-object/file-behaviour-object-verdicts.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-behaviour-summary-object>.*
