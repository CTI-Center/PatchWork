---
title: "Get started with DTM"
source: https://gtidocs.virustotal.com/docs/get-started-dtm
slug: get-started-dtm
section: guides
group: "DTM"
updatedAt: 2025-09-25T02:01:19.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [DTM](README.md) › Get started with DTM

---

# get-started-with-dtm

## introduction

DTM is a powerful cybersecurity solution designed to identify data leaks, discussions about your organization, and emerging attack patterns before they impact you.

By following this brief guide, you will be able to get a better understanding of how DTM works and how to get it initially setup.

## brief-overview:-how-dtm-works

1. **Monitor Topics**: DTM continuously scours the surface and dark web for suspicious content. This includes paste sites, forum posts, malicious emails, and other sources and extracts key entities like names, domains, URLs, and organizations, while categorizing the content by language, threat type, and industry.\
   You can create a monitor in DTM to receive near real-time notifications and alerts when specific conditions are met.
2. **Monitoring and Detection**: DTM constantly scans the deep and dark web for mentions of your specified topics or entities. You define these areas of interest in [monitors](monitors-guide.md), and when a match is found in collected content, an alert is generated.
3. **Alerts and Analysis**: When DTM finds relevant information, it generates [alerts](alerts-guide.md). These alerts serve as investigative leads for your analytic team.

## getting-started:-key-steps

Before creating monitors, we recommend using [Research Tools](research-tools.md) to safely explore open-source, dark web, and raw data that Google Threat Intelligence has collected. Once you have an understanding of what's available, you'll need to create Monitors and then review Alerts.

1. **Define Your Monitor Topics**: Carefully choose your [monitor topics and keywords](monitors-guide/monitor-fields.md) to ensure DTM focuses on the most relevant information. Consider including:
   * Your organization's name and variations
   * Key brands and products
   * Registered web domains
   * Executive names (VIP users)
   * Organization-specific terms
   * Network Information (External IP addresses or ranges)

2. **Set Up Monitors**: We have created several standardized templates that cover the most common use cases. In addition to these we have the Create a Custom Monitor.\
   We suggest [starting with these monitors](monitors-guide.md):

   * Domain Protection
   * Initial Access Broker
   * Compromised Credential
   * Ransomware

     ![monitor templates](https://storage.googleapis.com/gtidocresources/guides/dtm/images/dtm_monitor_create.png)

3. **Review and Respond**: Setup notifications for your [alerts](alerts-guide.md), build your own delivery schedule based on your needs with both immediate notification or scheduled delivery, and take appropriate action to mitigate risks.

## additional-considerations

DTM is a valuable tool for staying ahead of cyber threats. By proactively monitoring the digital landscape, you'll be better equipped to protect your organization's data, and bottom line. To maximize value and adoption, consider the following:

* **Test Your Monitors** using the Test Monitor function when building a monitor to see if your monitor will pull back any data.

  ![How to test a monitor](https://storage.googleapis.com/gtidocresources/guides/dtm/images/dtm_monitor_config.png)

* **Use Research Tools** to search our historical holdings. To conduct a search, simply enter a term into the [research tools](research-tools.md) search bar.

* **Implement your password complexity policies in compromised credentials monitors** for easier analysis of credentials which may be at higher risk since they match your organization’s password complexity requirements. This improved context typically results in more actionable alerts.

* **Perform domain ownership verification** if you want to see full output of passwords in the [compromised credentials monitor](monitors-guide/monitor-compromised-credentials.md). We don't allow users to see the discovered passwords until an administrator can [verify you own your domain](https://support.google.com/a/answer/183895?hl=en).

* **Integrate with Existing Tools**: If possible, integrate DTM with your security information and event management (SIEM) system to centralize threat information. [Our powerful API](https://gtidocs.virustotal.com/reference/get-alerts) lets you integrate with other tools as part of your remediation workflows.

* **Monitor tuning may be required** to optimize your results. We cannot eliminate all unwanted alerts, but our goal is to generate a manageable quantity of high ***quality*** alerts for your team. As you use DTM, refine your monitors based on the types of alerts you're receiving. Using the [LuceneText Query](monitors-guide/monitor-scenarios.md#lucene-text-query) options, you can adjust and tune the data coming in from the monitors.

* **Implement risk-based prioritization** to address the most critical issues first.

* **Collaborate closely with IT and Operations teams** to expedite remediation and response efforts.

* **Involve additional Intelligence Stakeholders** as you collect your intelligence requirements for building monitors. Members of various teams are often intelligence stakeholders who have information that can be input into DTM as a monitor.

Should you have any additional questions, don't forget to utilize our [Google Cloud Community Forums](https://www.googlecloudcommunity.com/gc/Mandiant-Forums/ct-p/mandiant-forums); or reach out to our [support team](https://www.virustotal.com/gui/contact-us).

---

← [ASM API Limits and Quotas](../11-asm/asm-limits-quotas.md) · [up](README.md) · [Alerts](alerts-guide.md) →

*Archived from <https://gtidocs.virustotal.com/docs/get-started-dtm>.*
