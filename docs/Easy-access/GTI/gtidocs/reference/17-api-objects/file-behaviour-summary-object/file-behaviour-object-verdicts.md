---
title: "verdicts"
source: https://gtidocs.virustotal.com/reference/file-behaviour-object-verdicts
slug: file-behaviour-object-verdicts
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:43:00.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files Behaviour](../file-behaviour-summary-object.md) › verdicts

---

# verdicts

Verdicts to tag a sample from sandbox behaviour

`verdicts` contains a list of **maliciousness classifications** for the file under study **based on its behaviour.** It is a list of strings, that can contain any of the following:

* `CLEAN` clean, whitelisted or undetected.
* `MALWARE` should be detected as malware.
* `GREYWARE` PUA, PUP (possibly unwanted program).
* `RANSOM` Ransom or crypter.
* `PHISHING` Tries to phish the user or deceive him to steel his credentials.
* `BANKER` banking trojan malware.
* `ADWARE` displays unwanted advertisements.
* `EXPLOIT` contains or runs an exploit.
* `EVADER` contains logic to evade analysis.
* `RAT` remote access trojan, may listen for inbound connections.
* `TROJAN` trojan or bot.
* `SPREADER` spreads to USB, other drives, network, etc. Work-like functionality.

```json Verdicts
{
    "data": {
        "attributes": {
            "verdicts": [
                "<string>"
            ]
        }
    }
}
```
```json Example
{
    "data": {
        "attributes": {
            "verdicts": [
                "MALWARE"
            ]
        }
    }
}
```

---

← [Files Behaviour](../file-behaviour-summary-object.md) · [up](../README.md) · [files_dropped](file-behaviour-object-files-dropped.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-behaviour-object-verdicts>.*
