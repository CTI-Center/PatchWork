---
title: "Threat Actors"
source: https://gtidocs.virustotal.com/docs/threat-actors-card
slug: threat-actors-card
section: guides
group: "Global Landscape"
updatedAt: 2026-02-27T12:13:53.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [Global Landscape](README.md) › Threat Actors

---

# threat-actors

Google Threat Intelligence allows you to explore highly contextualized details about threat actors, aggregating highly curated information from Mandiant experts as well as threat actors' insights coming from our partners - trusted sources from the security industry such as MISP, MITRE, etc.

Google Threat Intelligence now aggregates all threat actors insights under one single explorer, giving users the ability to narrow their searches by filtering by different characteristics such as where the information comes from (origin:"Google Threat Intelligence" or origin:Partner), targeted industries, regions, motivations, associated malware and tools, etc.

![Threat Actor cards](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/threat_actor_card_20241121.png)

Users will also have the ability to follow the threat actors' activity to get notifications on new IoCs associated with those particular threat actors and monitor changes to Threat Actor activity over time, such as their updated use of malware families, tools, and vulnerabilities as part of their TTP.

Those notifications will flow into their [IoC Stream](../06-ioc-investigation/ioc-stream-guide.md) - the centralized hub for all IoCs notifications:

![Threat Actor follow](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/threat_actor_follow_20241121.png)

# threat-actor-card

**What information can I find on a threat actor?**

## header

![Threat Actor header](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/threat_actor_header_20241121.png)

In the threat actor's header a user can find the following information:

1. **Creation date:** Date when the threat actor card was generated.
2. **Owner:** Creator of the threat actor card. This information appears at the top right corner: By owner.
3. **Last modification / Update date:** Date when the threat actor card was last updated with any new associated report, malware family, targeted region, etc.
4. **Aliases:** Threat Actor's aliases - other names by which a threat actor is known.
5. **First Activity date:** Date when the first observation about that threat actor was made.
6. **Last Activity date:** Date when the last observation about that threat actor was made.
7. **Source Region:** Known/Suspected country or region of origin for the threat actor.
8. **Motivations:** Threat actor's motivations such as espionage, financial gain, etc.

The header provides quick access to actions you can perform on a threat actor card, such as:

* **Follow:** Ability to follow the threat actors' activity to (1) get notifications on new IoCs associated with those particular threat actors and (2) monitor changes to Threat Actor activity over time, such as their updated use of malware families, tools, and vulnerabilities as part of their TTP. Learn more on the How to follow a threat actor section.
* **Share & Visibility:** Ability to share the threat actor link with other users that have the right privileges to see this kind of information.
* **Download:** Ability to Export all IoCs tied to the threat actor. Users will be able to download just the IoCs identifiers or download the identifiers and metadata.
* **Open in graph:** Ability to get a visual representation on a threat graph of the threat actor and all it's relationships - related IoCs with its own connections, associated malware & tools, etc.

## summary-tab

![Threat Actor summary](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/threat_actor_summary_20241122.png)

This tab displays a comprehensive summary of the threat actor profile. Some sections may vary depending on whether the profile was created by Google Threat Intelligence analysts or a partner.

Left column:

* **Description:** Description of the threat actor.
* **Overview:** Includes information such as threat actor’s aliases, lists the industries and regions known to be targeted by the threat actor, suspected source region,motivations, dates on actor's activity and relevant tags.
* **Associated Malware, Tools & Vulnerabilities:** List of Malware, Tools and Vulnerabilites known to be used or exploited by this threat actor.
* **Associated Campaigns:** Campaigns that this threat actor has been seen involved in.
* **Other Sightings:** Lists all crowdsourced collections tied to this threat actor. A collection is a live report which contains a title, description and a group of IoCs (file hashes, URLs, domains and IP addresses) that are related somehow - same malware family, campaign, etc.
* **Associated Reporting:** Lists all online crowdsourced articles or references talking about the threat actor you are looking at.
* **Associations timeline:** Shows information about key events on the threat actor card such as when was the first IoC associated with this threat actor seen, when was the first associated campaign or reference.
* **Attribution Trace:** This section shows how Google Threat Intelligence analysts have linked this threat actor to other groups. It lists confirmed connections "Merged Groups" and potential connections "Suspected Groups".

Right column:

* **Lookups and submissions trend:** Shows the evolution over the last 2 weeks of the number of lookups and submissions of IoCs tied to the threat actor, allowing users to easily pivot to the telemetry tab to get the full telemetry history of the related IoCs.
* **New activity:** Any modification on new malware, tools, TTPs associated with this threat actor will be shown here.
* **News & Analysis:** Current media publications on cyber security events that are related to the threat actor.

# associations

This tab shows a list of all objects associated with this threat actor. Only partners or staff users have the ability to associate a collection to a threat actor object to avoid adding excessive noise to threat actors. Associations can be filtered by modification date, object type (campaigns, malware, toolkits, collections and vulnerabilities), origin (Google Threat Intelligence or Partners), source regions, targeted regions or targeted industries.

![Threat actor group associations](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/threat_actor_associations_20241121.png)

# iocs

![Threat actor group iocs](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/threat_actor_ioc_20241121.png)

This tab shows all indicators of compromise that have been directly associated with that threat actor or any collections related to it. That means, we are also showing all indicators that have been associated with a specific campaign that is related to our threat actor in play.

From that tab, users can add IoCs to an existing or new collection, calculate commonalities on those indicators (commonalities found in metadata, signatures, sample geometry, threat network infrastructure, distribution vectors, malware config, etc.), calculate a Diff for creating detections or get a visual representation of the IoCs and their relations in a graph.

# telemetry

![Threat actor group telemetry](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/threat_actor_telemetry_20241121.png)

This tab shows the full history of the total number of lookups and submissions of the IoCs tied to a specific threat actor.\
Users can access an overview of total lookups and submissions over time, along with detailed graphs displaying data by region and entity.

Data can be filtered on the left panel to see the statistics on type (lookups or submissions), region or specific entities.

# rules

![Threat actor rules](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/threat_actor_rules_20241121.png)

This tab shows detection rules for this threat actors IoCs, there are Yara, Sigma and IDS rules, and they can be crowdsourced or curated.

# ttps

![Threat actor rules](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/threat_actor_ttps_20241121.png)

This tab shows the Tactics, Techniques, and Procedures (TTPs) associated with this threat actor following the MITRE ATT\&CK framework.

The matrix can be filtered by different categories such as:

* Enterprise / Mobile / ICS
* E2E Attacker Lifecycle / Techniques seen in IoCs

These tactics and techniques can also be exported into [MITRE ATT\&CK Navigator](https://mitre-attack.github.io/attack-navigator/) or downloaded as CSV or JSON.

# community

This tab features a dedicated space for community discussion, it is a section that contains comments posted by the community making observations on the threat actor.

---

← [Threat Profiles](manage-threat-profiles.md) · [up](README.md) · [Malware & Tools](malware-tools.md) →

*Archived from <https://gtidocs.virustotal.com/docs/threat-actors-card>.*
