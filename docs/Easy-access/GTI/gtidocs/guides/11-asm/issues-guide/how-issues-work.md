---
title: "How Issues Work"
source: https://gtidocs.virustotal.com/docs/how-issues-work
slug: how-issues-work
section: guides
group: "ASM"
updatedAt: 2025-09-25T00:55:54.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [ASM](../README.md) › [Issues](../issues-guide.md) › How Issues Work

---

# how-issues-work

When inspecting an Entity for vulnerabilities, Attack Surface Management (ASM) performs one of the following types of probes:

* an *active* check, where a benign action is taken on the Entity to test for the existence of a known vulnerability
* a *passive* check, where the technology discovered on the Entity is used to infer potential vulnerabilities

The type of Entity determines the tasks used for probing, which in turn determines how the checks are performed. If an active check is required, all payloads are strategically crafted to avoid any business disruptions to live environments. By using these benign actions, we ensure that we don't compromise the integrity and availability of the systems we are analyzing.

In situations where a public exploit cannot be verified without more aggressive methods, ASM performs a passive check to identify the technology (software and version) on the Entity. This information is then compared against our database of technologies that are known to be vulnerable. If a match is found in the database, then ASM infers that a vulnerability could exist and raises an Issue about it. This type of passive check is often referred to as an *inference*.

However, some items like JavaScript libraries are vulnerable only when used in specific ways, so using just the inference method could potentially produce many false positives. In these cases, an augmented type of passive check is performed by ASM, using additional heuristics to identify potential vulnerabilities. Again, no active checks are made, so anything identified is marked as a potential, not confirmed, vulnerability.

An example of how this comes into play is with the Log4j vulnerabilities.

## log4j

Log4j, originally developed by the Apache Software Foundation, is an open source library used for logging that is used by many different applications worldwide, including web services. Because it's incorporated into other applications and web technologies, there are no actual markers or other external signs that Log4j is in use on any given site. This means that ASM cannot perform a standard passive check to infer if any vulnerabilities exist on the web application directly because of it. Instead, ASM sends a Log4j detection payload to every web application it encounters, and flags any interactions that are detected.

This detection method would be used for any other library or underlying system used to power an application. Because they are not web technologies themselves, there is no way for ASM to determine with absolute certainty when they are actually in use. However, there are heuristics that can make a very educated assumption based on what other technologies are found – for example, if a website employs Java, then there’s a strong likelihood that Log4j is being used. And based on that assumption, ASM will perform various other checks, including active checks specifically crafted to identify any exploitable configurations, to determine whether a potential vulnerability exists.   

For more information about Issues, see [Reviewing Issues](../issues-guide.md) and [ASM Issue Severity Definitions and Examples](issues-severity-definitions.md).

---

← [Issues Severity Definitions and Examples](issues-severity-definitions.md) · [up](../README.md) · [Entities](../entities-guide.md) →

*Archived from <https://gtidocs.virustotal.com/docs/how-issues-work>.*
