---
title: "DTM Alert Severity Definitions and Examples"
source: https://gtidocs.virustotal.com/docs/dtm-alert-severity
slug: dtm-alert-severity
section: guides
group: "DTM"
updatedAt: 2025-09-25T00:30:00.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [DTM](../README.md) › [Alerts](../alerts-guide.md) › DTM Alert Severity Definitions and Examples

---

# dtm-alert-severity-definitions-and-examples

This document describes how [Digital Threat Monitoring (DTM)](../digital-threat-monitoring.md) determines the severity ratings for Alerts.

## alert-scoring-framework

[DTM alert scoring](https://cloud.google.com/blog/products/identity-security/alert-scoring-machine-scale/) is governed by two components:

* Confidence, which uses machine learning to score how certain Google TI is in the given alert actually being malicious
* Severity, which scores what the potential impact of the threat is to determine whether an Alert needs further investigation or is ready for review

Too many alerts, especially false positives, can lead to analyst fatigue. The Confidence score's job is to help initially remove any obvious noise, and any other downstream context is then traversed by the Severity scoring model to further divide alerts into either High, Medium, or Low categories.

Several factors are considered when determining Severity including:

* detected entities within the document
* the document's security classifications
* monitor matching criteria, since the severity of an alert should be considered in the context of your specific environment and risk tolerance

## prioritization-of-alerts

Google TI recommends giving priority to the resolution of High severity Alerts, whereas Medium and Low severity Alerts should be triaged afterwards, time permitting. You can sort Alerts by Severity in order to facilitate this process.

The following table outlines a common understanding of the characteristic features of alerts that give rise to different severity categories.

| Alert Severity Definitions |  |  |
| --- | --- | --- |
| <strong>Alert Severity</strong> | <strong>Definitions</strong> | <strong>Examples</strong> |
| High | Indicates a critical security issue or active exploitation attempt that poses an immediate and significant risk to your organization<br><hr /><br>Could lead to data breaches, system compromise, service disruption, or financial loss<br><hr /><br>Suggested Usage:<br><ul><br><li>Investigate within 24 hours</li><br><li>Remediate within 7 days</li><br></ul> | <ul><br><li>Matches a document showing a darknet security breach notification</li><br><li>Document contains a typosquatted domain matching your monitor criteria</li><br><li>Document contains an infrastructure netloc indicator matching your monitor criteria</li><br></ul> |
| Medium | Indicates a security issue or suspicious activity that poses a moderate risk to your organization<br><hr /><br>May lead to unauthorized access, data leakage, or minor service disruption if left unaddressed<br><hr /><br>Suggested Usage:<br><ul><br><li>Investigate within 72 hours</li><br><li>Remediate within 21 days</li><br></ul> | <ul><br><li>Document has a potential leak of confidential matched entity</li><br><li>Contains a credit card bin not matching monitor criteria</li><br><li>Matched document comes from a dark web shop, sells payment cards, accounts, or compromised machines</li><br></ul> |
| Low | Indicates a potential security issue or anomaly that poses a low risk to your organization<br><hr /><br>Unlikely to cause immediate harm, but could contribute to a larger security issue if ignored<br><div>For common low severity alerts, consider automating responses to free up your security team to focus on more critical issues.</div><br><hr /><br>Suggested Usage:<br><ul><br><li>Investigate within 1 month</li><br><li>Remediate within 3 months</li><br></ul> | <ul><br><li>Matches monitor criteria, but does not contain any other security-relevant contextual landmarks or derived findings</li><br></ul> |

---

← [Alerts](../alerts-guide.md) · [up](../README.md) · [Group Alerts](dtm-group-alerts.md) →

*Archived from <https://gtidocs.virustotal.com/docs/dtm-alert-severity>.*
