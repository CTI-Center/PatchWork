---
title: "July 14th, 2026 — URL Scanning 2.0, RBAC for Service Accounts, and Invitations Page Improvements"
source: https://gtidocs.virustotal.com/changelog/july-14th-2026-url-scanning-20-rbac-for-service-accounts-and-audit-log-updates
slug: july-14th-2026-url-scanning-20-rbac-for-service-accounts-and-audit-log-updates
section: changelog
group: "Changelog"
retrieved: 2026-09-01
---

[gtidocs](../README.md) › [Changelog](README.md) › [Changelog](README.md) › July 14th, 2026 — URL Scanning 2.0, RBAC for Service Accounts, and Invitations Page Improvements

---

# july-14th,-2026-—-url-scanning-2.0,-rbac-for-service-accounts,-and-invitations-page-improvements

## 🌐-url-scanning-2.0:-from-static-verdicts-to-living-investigations

We are delivering major investigative upgrades to automated URL analysis that turn every URL report into a living, historical view. By moving beyond static reports, this update significantly reduces Mean Time to Resolve (MTTR) for phishing and malicious-link investigations by letting analysts see the page, trace execution, and track evolution.

* **Enriched URL Reports (Powered by full browser instances):** Powerful metadata is now surfaced right inside the investigation workflow. Users can now view live screenshots (to see the rendered page as the victim does), DOM trees, console messages, page stats (network requests, response sizes, cookies), web technologies, and full session parameters.
* **Automated Brand Identification:** By feeding live screenshots and DOM data directly into AI models, the platform visually detects exactly who a site is impersonating, completely defeating advanced text-obfuscation tactics.

![](https://files.readme.io/d142f2b95bc04c3f3976432f5a4dce448616ef5fdac50f6cbbc212cceb7413d1-Screenshot_2026-07-14_at_09.49.37.png)

* **Historical Analysis Pivoting:** Travel back through a URL's timeline with point-in-time snapshots. Report tabs (Summary, Detection, Details, and Content) now dynamically re-render to match that exact historical state—not just the latest scan.

![](https://files.readme.io/4f141ceebf72c5adf498952c3455b5b76eaf0c294d011c301e50af3ebffc2d17-Screenshot_2026-07-14_at_09.45.26.png)

* **Footprint Hunting via Pivotable Technical Identifiers:** Turn a single indicator into an infrastructure map. Key technical markers like response headers, JavaScript global variables, contacted external domains, and Identified Brands are now pivotable and searchable attributes, allowing analysts to instantly find other URLs exhibiting the same technical fingerprint.

**Learn more:** Check out the [URL Report Summary documentation](https://gtidocs.virustotal.com/docs/results-reports#url-report-summary).

## 🔑-role-based-access-control-(rbac)-and-quota-management-for-service-accounts

Service accounts are now managed just like users with full RBAC and Quota Management, strengthening enterprise-grade security and governance on the Google TI platform.

* **Service Accounts RBAC Parity:** You can now assign specific roles and enforce quota limits directly on Service Accounts.
* **Module-Specific Role Filtering:** Locate and review permissions quickly with new mix-and-match filters down to specific module roles, such as GTI Alerts and Private Scanning.
* **Partial/Substring Search:** Substring search is now supported—type any part of a name, description, or email to find what you need instantly.

![](https://files.readme.io/ef13efb8c4188c672100663d0eaf29fb5b3a886b208924f7ca9974ec1ab6266e-Screenshot_2026-07-14_at_10.09.12.png)

## 📋-invitations-page-improvements

We have rolled out further improvements to the Invitations page to make identity governance even more robust and transparent.

* **Sender & Timestamp Visibility:** Administrators can now see exactly who sent an invitation and when it was sent.
* **Extended Invitation Statuses:** We’ve expanded invitation tracking beyond just “pending”. You can now see if an invite has been Joined or Revoked in addition to Pending.
* **Status Filtering:** A new filter allows you to easily sort and view invitations by their current status (Pending, Joined, Revoked) and the roles set in the invite.

![](https://files.readme.io/34bfc9b644fdab85c005574ddb0f99200f924570ede6254ec849ad61a83779c0-Screenshot_2026-07-14_at_10.37.40.png)

<br />

---

← [July 21st, 2026 — Agentic URL Scanning 2.0 Integration, Target Technology Watchlists, and Sharper Domain Reputation](july-21st-2026-agentic-url-scanning-20-integration-target-technology-watchlists-and-sharper-domain-reputation.md) · [up](README.md) · [June 30th, 2026 — Splunk Observed Threats, GTI Score Explainability, and Private Scanning Access Control Lists (ACLs)](june-29th-2026-splunk-observed-threats-gti-score-explainability-and-private-scanning-access-control-lists-acls.md) →

*Archived from <https://gtidocs.virustotal.com/changelog/july-14th-2026-url-scanning-20-rbac-for-service-accounts-and-audit-log-updates>.*
