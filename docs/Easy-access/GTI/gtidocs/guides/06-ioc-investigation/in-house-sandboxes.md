---
title: "In-house Sandboxes - behavioural analysis products"
source: https://gtidocs.virustotal.com/docs/in-house-sandboxes
slug: in-house-sandboxes
section: guides
group: "IOC Investigation"
updatedAt: 2026-02-11T11:18:10.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [IOC Investigation](README.md) › In-house Sandboxes - behavioural analysis products

---

# in-house-sandboxes---behavioural-analysis-products

Google Threat Intelligence detonates files in virtual controlled environments to trace their activities and communications, producing detailed reports including opened, created and written files, created mutexes, registry keys set, contacted domains, URL lookups, etc. This execution activity is indexed in a faceted fashion in order to allow for instantaneous lookups.

Dynamic analysis capabilities do not only focus on execution traces but also on running static+dynamic analysis plugins to decode RAT malware configs and extract network infrastructure that may have not been observed during real time execution.

Google Threat Intelligence integrates external behavioural engines sandboxes. The list of external partners can be found [here](../01-introduction/contributors.md#behavioral-analysis--sandbox-products).

Find below a description about our in-house sandboxes:

# **box-of-apples**

MacOS x86 sandbox hooking system calls.

| **Operating System** | **Type of file**                                               | **Pcap** | **HTML Report** | **Screenshots** | **Memory Dumps** | **MITRE Signatures** | **Event Logs (EVTX)** | **Network Capabilities** |
| -------------------- | -------------------------------------------------------------- | -------- | --------------- | --------------- | ---------------- | -------------------- | --------------------- | ------------------------ |
| MacOS                | MachO, DMG, PKG,  ISO, shell scripts, apple script, Zipped APP | Yes      | Yes             | Yes             | No               | No                   | No                    | Direct, No Internet      |

# **os-x-sandbox**

MacOS x86 11.6 Sandbox.

> 🚧 Deprecated
>
> No new behavior reports will be generated. Existing reports will remain available.

| **Operating System** | **Type of file**     | **Pcap** | **HTML Report** | **Screenshots** | **Memory Dumps** | **MITRE Signatures** | **Event Logs (EVTX)** | **Network Capabilities** |
| -------------------- | -------------------- | -------- | --------------- | --------------- | ---------------- | -------------------- | --------------------- | ------------------------ |
| MacOS 11.6           | MachO, DMG, PKG, ISO | Yes      | Yes             | Yes             | No               | Yes                  | No                    | Direct, No Internet      |

# **virustotal-droidy**

Google Threat Intelligence Android Sandbox. The API logging is inspired by droidmon.

| **Operating System** | **Type of file**          | **Pcap** | **HTML Report** | **Screenshots** | **Memory Dumps** | **MITRE Signatures** | **Event Logs (EVTX)** | **Network Capabilities** |
| -------------------- | ------------------------- | -------- | --------------- | --------------- | ---------------- | -------------------- | --------------------- | ------------------------ |
| Android 4.4          | Android application (APK) | No       | Yes             | Yes             | No               | No                   | No                    | Direct, No Internet      |

# **virustotal-jujubox**

Windows dynamic analysis sandbox. Frida is used for hooking and tracking Windows API calls.

| **Operating System** | **Type of file**                                                          | **Pcap** | **HTML Report** | **Screenshots** | **Memory Dumps** | **MITRE Signatures** | **Event Logs (EVTX)** | **Network Capabilities** |
| -------------------- | ------------------------------------------------------------------------- | -------- | --------------- | --------------- | ---------------- | -------------------- | --------------------- | ------------------------ |
| Windows 7            | EXE, DLL, MSI, CHM, BAT,  CRX, PDF,  VBS, MS Office Documents, Powershell | Yes      | Yes             | Yes             | No               | No                   | Yes                   | Direct, No Internet      |

# **virustotal-observer**

Windows sysmon based sandbox.

| **Operating System** | **Type of file**                                                        | **Pcap** | **HTML Report** | **Screenshots** | **Memory Dumps** | **MITRE Signatures** | **Event Logs (EVTX)** | **Network Capabilities** |
| -------------------- | ----------------------------------------------------------------------- | -------- | --------------- | --------------- | ---------------- | -------------------- | --------------------- | ------------------------ |
| Windows 7            | EXE, DLL, MSI, CHM, BAT, CRX, PDF, VBS, MS Office Documents, Powershell | No       | No              | No              | No               | No                   | No                    | Direct, No Internet      |

# **virustotal-r2dbox**

R2DBox is an Android 8 sandbox which uses Frida to make the hooks. It  runs on GCE machines.

| **Operating System** | **Type of file**          | **Pcap** | **HTML Report** | **Screenshots** | **Memory Dumps** | **MITRE Signatures** | **Event Logs (EVTX)** | **Network Capabilities** |
| -------------------- | ------------------------- | -------- | --------------- | --------------- | ---------------- | -------------------- | --------------------- | ------------------------ |
| Android 8            | Android application (APK) | Yes      | Yes             | Yes             | No               | No                   | No                    | Direct, No Internet      |

# **zenbox**

Windows 11 Sandbox. It provides MITRE matrix, signature detection and memory dumps. Runs on GC VmwareEngine.

| **Operating System** | **Type of file**                                                                        | **Pcap** | **HTML Report** | **Screenshots** | **Memory Dumps** | **MITRE Signatures** | **Event Logs (EVTX)** | **Network Capabilities** |
| -------------------- | --------------------------------------------------------------------------------------- | -------- | --------------- | --------------- | ---------------- | -------------------- | --------------------- | ------------------------ |
| Windows 11           | EXE, DLL, MSI, CHM, BAT, CRX, PDF, LNK, SVG, VBS, MS Office Documents, Powershell, VHDX | Yes      | Yes             | Yes             | Yes              | Yes                  | Yes                   | Direct, No Internet      |

ZIP files without password will be processed executing the first binary found within the ZIP.

ZIP files with password will be processed only if  the password is "infected".

# **zenbox-android**

Supports APKs up to Android 13 (SDK 33).

| **Operating System** | **Type of file**          | **Pcap** | **HTML Report** | **Screenshots** | **Memory Dumps** | **MITRE Signatures** | **Event Logs (EVTX)** | **Network Capabilities** |
| -------------------- | ------------------------- | -------- | --------------- | --------------- | ---------------- | -------------------- | --------------------- | ------------------------ |
| Android 13           | Android application (APK) | Yes      | Yes             | Yes             | No               | Yes                  | No                    | Direct, No Internet      |

# **zenbox-linux**

Supports X86,  X86\_64, ARM, MIPS.

| **Operating System** | **Type of file**                                   | **Pcap** | **HTML Report** | **Screenshots** | **Memory Dumps** | **MITRE Signatures** | **Event Logs** (EVTX) | **Network Capabilities** |
| -------------------- | -------------------------------------------------- | -------- | --------------- | --------------- | ---------------- | -------------------- | --------------------- | ------------------------ |
| Ubuntu 20.04         | ELF, Scripts, DEB, JAR, ZIP (if inside executable) | Yes      | Yes             | Yes             | No               | Yes                  | No                    | Direct, No Internet      |

ZIP files without password will be processed executing the first binary found within the ZIP.

ZIP files with password will be processed only if  the password is "infected".

# **zenbox-macos**

MacOS Sandbox. Supports X86,  X86\_64, ARM.

| **Operating System** | **Type of file**                           | **Pcap** | **HTML Report** | **Screenshots** | **Memory Dumps** | **MITRE Signatures** | **Event Logs (EVTX)** | **Network Capabilities** |
| -------------------- | ------------------------------------------ | -------- | --------------- | --------------- | ---------------- | -------------------- | --------------------- | ------------------------ |
| MacOS 15             | MachO, APPLESCRIPT, DMG, PKG, Scripts, ZIP | Yes      | Yes             | Yes             | No               | Yes                  | No                    | Direct, No Internet      |

# **capa**

Extraction of behaviour capabilities with [Mandiant CAPA](https://github.com/mandiant/capa)

| **Operating System** | **Type of file** | **Pcap** | **HTML Report** | **Screenshots** | **Memory Dumps** | **MITRE Signatures** | **Event Logs (EVTX)** | **Network Capabilities** |
| -------------------- | ---------------- | -------- | --------------- | --------------- | ---------------- | -------------------- | --------------------- | ------------------------ |
| Windows/Linux        | EXE, ELF, DLLS   | No       | Yes             | No              | No               | Yes                  | No                    | N/A                      |

# **cape-sandbox**

Windows Sandbox using [CAPEv2](https://github.com/kevoreilly/CAPEv2)

| **Operating System** | **Type of file**                                                                                 | **Pcap**           | **HTML Report** | **Screenshots** | **Memory Dumps** | **MITRE Signatures** | **Event Logs (EVTX)** | **Network Capabilities**                            |
| -------------------- | ------------------------------------------------------------------------------------------------ | ------------------ | --------------- | --------------- | ---------------- | -------------------- | --------------------- | --------------------------------------------------- |
| Windows 10           | EXE, DLL, MSI, CHM, BAT,  CRX, PDF,  VBS, MS Office Documents, LibreOffice Documents, Powershell | Yes (with TLSdump) | Yes             | Yes             | Yes              | Yes                  | Yes                   | Direct, No Internet, Simulated, VPN, Country change |

# **cape-linux**

Linux Sandbox using [CAPEv2](https://github.com/kevoreilly/CAPEv2)

| **Operating System** | **Type of file**                    | **Pcap** | **HTML Report** | **Screenshots** | **Memory Dumps** | **MITRE Signatures** | **Sysmon Logs** | **Network Capabilities**                            |
| -------------------- | ----------------------------------- | -------- | --------------- | --------------- | ---------------- | -------------------- | --------------- | --------------------------------------------------- |
| Ubuntu 22.04         | ELF, Scripts, JAR, DEB, PYTHON\_WHL | Yes      | Yes             | Yes             | Yes              | Yes                  | Yes             | Direct, No Internet, Simulated, VPN, Country change |

# **cuckoofork**

Windows XP Sandbox.

> 🚧 Deprecated
>
> No new behavior reports will be generated. Existing reports will remain available.

| **Operating System** | **Type of file**                                                          | **Pcap** | **HTML Report** | **Screenshots** | **Memory Dumps** | **MITRE Signatures** | **Event Logs (EVTX)** | **Network Capabilities** |
| -------------------- | ------------------------------------------------------------------------- | -------- | --------------- | --------------- | ---------------- | -------------------- | --------------------- | ------------------------ |
| Windows XP           | EXE, DLL, MSI, CHM, BAT,  CRX, PDF,  VBS, MS Office Documents, Powershell | Yes      | No              | No              | No               | No                   | No                    | N/A                      |

---

← [External behavioural engines sandboxes](external-sandboxes.md) · [up](README.md) · [Reports & Analysis](../07-report-analysis/reports-and-analysis.md) →

*Archived from <https://gtidocs.virustotal.com/docs/in-house-sandboxes>.*
