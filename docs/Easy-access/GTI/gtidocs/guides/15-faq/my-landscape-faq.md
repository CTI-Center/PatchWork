---
title: "My Landscape"
source: https://gtidocs.virustotal.com/docs/my-landscape-faq
slug: my-landscape-faq
section: guides
group: "FAQ"
updatedAt: 2026-03-04T11:25:40.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [FAQ](README.md) › My Landscape

---

# my-landscape

# frequently-asked-questions-(faq)

**Q: How is The Relevance System different from Digital Threat Monitoring (DTM)?**

**A:** While both are vital, they serve different purposes. **DTM** leverages key-term based matching: it looks outward to find leaked employee credentials, brand impersonation, or mentions of your company name on the open/dark web.

**The Relevance System** looks at the *entire global threat landscape* and alerts you if those global threats overlap with your industry or tech stack—even if your company's name is never explicitly mentioned by the attackers.

**Q: Will updating my Organization Profile change my detection?**

**A:** Yes. When you add, remove or change the organization profile, the alerts and context you receive will be impacted in order to more closely match your organization.

**Q: How do I reset my tenant and start from the beginning?**

**A:** If you need to completely rebuild your Organization Profile or clear all historical alert feedback, please file a support ticket.

**Q: What are "Findings" and why does an alert have multiple?**

**A:** A Finding is an immutable, granular record of a specific threat detection event (e.g., a single leaked credential). An Alert is a dynamic container that groups related Findings into a broader Threat Scenario. If an alert has multiple findings, it means the overarching threat campaign has intersected with your organization's profile in several different ways.

**Q: What does the "Created" timestamp mean on an alert?**

**A:** Because an alert is a mutable container for an ongoing Threat Scenario, it is not a static notification. When a new Finding is discovered that matches an existing Threat Scenario for your organization, the system adds that finding to the existing alert. When this happens, the "Created" timestamp is refreshed to reflect when the alert was *last updated* with new intelligence.

**Q: What is Alert Backfilling?**

**A:** When you first configure your Organization Profile, or whenever you add new elements to your Tech Stack, The Relevance System initiates a process called Backfilling. The system takes your newly defined profile and scans it backward against Google's massive repository of historical threat intelligence to identify latent risks. Because this computation takes time, you may notice a slight delay before recent historical alerts populate your dashboard.

---

← [When is an analysis included in the feeds?](when-analysis-feeds.md) · [up](README.md) · [How can I rotate my API key](rotate-api-key.md) →

*Archived from <https://gtidocs.virustotal.com/docs/my-landscape-faq>.*
