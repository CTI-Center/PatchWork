---
title: "tags"
source: https://gtidocs.virustotal.com/reference/file-behaviour-object-tags
slug: file-behaviour-object-tags
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:43:11.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files Behaviour](../file-behaviour-summary-object.md) › tags

---

# tags

Sandbox behavior tagged with a complex operation

`tags` field contains a list of labels summarizing key behavioural observations. It can be any of the following:

* `DETECT_DEBUG_ENVIRONMENT`
* `DIRECT_CPU_CLOCK_ACCESS`
* `LONG_SLEEPS`
* `SELF_DELETE` file deletes itself upon execution.
* `HOSTS_MODIFIER` local (resolution mapping) hosts file is modified.
* `INSTALLS_BROWSER_EXTENSION` installs BHO, Chrome Extension, etc.
* `PASSWORD_DIALOG` some sort of password input prompt is displayed.
* `SUDO` promotes to admin privileges.
* `PERSISTENCE` employs persistence mechanisms to survive reboots.
* `SENDS_SMS`
* `CHECKS_GPS`
* `FTP_COMMUNICATION`
* `SSH_COMMUNICATION`
* `TELNET_COMMUNICATION`
* `SMTP_COMMUNICATION`
* `MYSQL_COMMUNICAION`
* `IRC_COMMUNICATION`
* `SUSPICIOUS_DNS` possible DGA (Domain generation algorithm).
* `SUSPICIOUS_UDP` high counts of distinct UDP connections, this may often reveal P2P.
* `BIG_UPSTREAM` large outgoing network traffic
* `TUNNELING` some sort of network tunneling observed, e.g. VPN.
* `CRYPTO` makes use of crypto related APIs.
* `TELEPHONY` makes use of telephony related APIs.
* `RUNTIME_MODULES` dynamically loads DLLs or additional components.
* `REFLECTION` performs reflection calls.

```Text Behaviour tags
{
    "data": {
        "attributes": {
            "tags": [
                "<string>",...
            ]
        }
    }
}
```
```Text Example
{
    "data": {
        "attributes": {
            "tags": [
                "DIRECT_CPU_CLOCK_ACCESS",
                "DETECT_DEBUG_ENVIRONMENT",
                "RUNTIME_MODULES",
                "PERSISTENCE"
            ]
        }
    }
}
```

---

← [🔀 attack_techniques](file-behaviour-object-attack-techniques.md) · [up](../README.md) · [Flow](../flow-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-behaviour-object-tags>.*
