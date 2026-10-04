---
title: "Phishing & Brand Monitoring"
source: https://gtidocs.virustotal.com/docs/use-cases-phishing-brand-monitoring
slug: use-cases-phishing-brand-monitoring
section: guides
group: "Use Cases & Best Practices"
updatedAt: 2026-01-14T14:15:26.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [Use Cases & Best Practices](../README.md) › [Use cases and other resources](../use-cases.md) › Phishing & Brand Monitoring

---

# phishing-&-brand-monitoring

Phishing, fraud, and brand impersonation attacks are evolving rapidly—becoming more targeted, more convincing, and harder to detect. These threats can damage customer trust, disrupt operations, and put sensitive assets at risk. Organizations must stay vigilant and respond quickly when signs of compromise appear.

## how-can-google-threat-intelligence-help?

Google Threat Intelligence (Google TI) provides deep visibility and context to help you detect and understand these threats before they escalate. With insights derived from billions of daily signals, global telemetry, and expert analysis, Google TI gives your team the intelligence edge needed to stay ahead of evolving attacker tactics.\
Google TI enables you to:

* Analyze malicious activity with rich context to assess severity, intent, and potential impact.
* Identify impersonation campaigns targeting your brand, infrastructure, digital assets, or customer base.
* Monitor third-party risk by tracking suspicious activity originating from vendors or partners.
* Protect sensitive data by identifying potential leaks or misuse of proprietary information.

## use-cases

### comprehensive-brand-and-domain-impersonation-monitoring

Detect malicious activity, brand impersonation, and typosquatted domains targeting your organization or users.

Google TI allows you to uncover URLs, domains, and visual assets used by attackers to mimic your brand for phishing or fraud—whether through lookalike domains or reused logos and icons.

**How to do it**

| **A. Detect Suspicious URLs Using Your Brand Name**\<br>Attackers often register URLs that include your brand name to mislead users. You can detect these by searching for URLs that contain your brand but are not part of your legitimate domains.<br>1. Go to [Google TI Search](https://www.virustotal.com/gui/home/search).<br>2. Start by crafting queries to identify suspicious indicators:\<br>Search for URLs that contain your brand name but are not part of your legitimate domains:<br>```<br>entity:url content:"my brand" not parent_domain:”my_org_domain”<br>```<br>3. Refine your results with filters\<br>Reduce the scope by adding more modifiers such as title, first seen and positives.<br>```<br>title:”my title” fs:30d+ p:1+<br>```<br>**B. Identify Typosquatted Domains**<br>Typosquatting is a common tactic where attackers register misspelled or lookalike versions of your domain to trick users. Google TI can help detect these using fuzzy logic.<br>1. Run this query in [Google TI Search](https://www.virustotal.com/gui/home/search):\<br>Search for domains that are typographically similar to your legitimate domains but are not controlled by you.<br>```<br>entity:domain fuzzy_domain:my_org_domain.com<br>```<br>2. Refine your results with filters\<br>Use filters such as creation\_date or gti\_verdict to prioritize newly registered or malicious domains.<br>***C. Find Domains Reusing Your Brand’s Visual Identity***<br>1. Find your favicon’s dhash:<br>* Search your legitimate domain in Google TI<br>* Click on the favicon to retrieve its main\_icon\_dhash value<br>2. Use this query to find reuse across domains:<br>```<br>entity:domain main_icon_dhash:mydhash<br>```<br>You can also find documents or binaries using the same icon for deceptive purposes. Add filters like  not parent\_domain:"my\_org\_domain", creation\_date:30d+ or gti\_verdict:malicious to further refine the results.<br>You can refine your searches by adding modifiers like gti\_verdict:malicious to only include domains identified as malicious by Google TI, or creation\_date:30d+ to find newly created urls. You can automate any of these queries using the Google TI [API](https://gtidocs.readme.io/reference/api-overview) to enable continuous monitoring and alerting for brand impersonation activity. | [Comprehensive Brand and Domain Impersonation Monitoring](https://www.youtube.com/watch?v=TOFIWdKONRM) |
| --- | --- |

### hunting-for-phishing-targeting-your-organization

Proactively identify phishing attempts that mimic your brand by tracking suspicious URLs based on shared characteristics.

With Google TI’s Livehunt and YARA-based detection, you can build targeted rules to surface phishing infrastructure that reuses elements like your favicon, page titles, or domain structure.

**How to do it**

| 1. Navigate to the [Livehunt section](https://www.virustotal.com/gui/hunting/rulesets) within Google Threat Intelligence, click on New Livehunt Ruleset and select “New ruleset to get URLs”.<br>2. Click on the Structure tool on the left menu and write your url, in the example we use [http://www.acme.com](http://www.acme.com)<br>3. Click on the relevant information you want to create the rule with, and combine the values in a single rule. In the example we use url.favicon.dhash, url.html\_title and domain.root<br>Combine the extracted values into a YARA rule that identifies phishing attempts mimicking your brand.<br>```yara<br>import "vt"<br>rule example_phishing_rule {<br>condition:<br>vt.net.url.favicon.dhash == "6190b6b8595c5523"<br>and<br>vt.net.url.html_title icontains "ACME Laboratories"<br>and not<br>vt.net.domain.root == "acme.com"<br>}<br>```<br>This YARA rule would trigger if a domain uses the same favicon as yours, a title containing “ACME Laboratories” (not case-sensitive) and its root domain is not acme.com.<br>4. Save and activate your Livehunt rules. You will receive notifications when new samples matching your criteria are observed on the [IoC Stream](https://www.virustotal.com/gui/ioc-notifications).<br>You can learn more about Livehunts in the documentation. To keep reading about how to protect your organization from Phishing, check our [Phishing Exposed blogpost](https://security.googlecloudcommunity.com/google-threat-intelligence-67/google-threat-intelligence-phishing-exposed-5406). | [Hunting malicious activity abusing your Infrastructure](https://www.youtube.com/watch?v=p6SoLquAsdU) |
| --- | --- |

---

← [Incident Response](use-cases-incident-response.md) · [up](../README.md) · [Vulnerability Management](use-cases-vulnerability-management.md) →

*Archived from <https://gtidocs.virustotal.com/docs/use-cases-phishing-brand-monitoring>.*
