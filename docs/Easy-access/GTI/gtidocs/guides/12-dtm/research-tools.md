---
title: "Research Tools"
source: https://gtidocs.virustotal.com/docs/research-tools
slug: research-tools
section: guides
group: "DTM"
updatedAt: 2025-09-25T02:01:58.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [DTM](README.md) › Research Tools

---

# research-tools

Research Tools enables users to safely explore open-source, dark web, and raw data that Google Threat Intelligence has collected for Digital Threat Monitoring. Providing raw threat and related data in an easy interface, Research Tools helps you find what matters, see what is happening in the cyber realm, and thus better protect your business. 

We recommend you use Research Tools as a precursor to creating a Monitor. This will help you create Monitors focused on what matters and reduce false positives. 

To access Research Tools

1. Sign into Google Threat Intelligence.
2. Click the **Digital Threat Monitoring**  on the sidebar menu.
3. Click Research Tools.

## **searching-using-research-tools**

The search bar is intended to meet needs of basic users and advanced users.  There are additional filters on the left side of the search to help you refine your search. If you're an advanced user, you can use the [Lucene query syntax](https://www.elastic.co/guide/en/elasticsearch/reference/7.15/query-dsl-query-string-query.html#query-string-syntax) when creating your query. For Lucene search examples see [Lucene Queries](lucene-queries-in-dtm.md).

1. Enter your search term or terms and hit **Enter**.  In the following screen `aws` is used as a term in the search bar:

   ![](https://storage.googleapis.com/gtidocresources/guides/dtm/images/researchtool_search_20240718.png)

   As you can see in this enhanced view, results are explored and important contextual information is captured at a glance for your review.
2. (Optional) Select one or more **Collection Type** to filter your results. Filters automatically apply as you select them.
3. (Optional) Change the date range by clicking on the calendar icon. The results are automatically filtered when you select the date range. For example, see the following screen where the **Forum Post** is selected with a **Date Range** for **Last 30 Days**.

   ![](https://storage.googleapis.com/gtidocresources/guides/dtm/images/researchtool_filters_20240718.png)
4. Click on one of the results. It will launch in a new page, allowing you to see an overview of the content found and with other tabs **Forum Browser** and **<>Raw (JSON)**.

   **NOTE:**  If you select **Form Post** for the **Collection Type** you get an additional **Forum Browser** tab as shown in the following screen.

   ![](https://storage.googleapis.com/gtidocresources/guides/dtm/images/researchtool_element_overview_20240418.png)
5. Select the **Forum Browser** to browse all the threads in the **Forum Post** with breadcrumbs on the top right for further navigation and digging.

   **NOTE:**  HTML and JAVA scripts are deleted to avoid any malicious content and navigation within a secure environment.

   ![](https://storage.googleapis.com/gtidocresources/guides/dtm/images/researchtool_forum_browser_20240418.png)
6. Clicking on one of the breadcrumb link say **Forum Name** you get the summary of that board.

   ![](https://storage.googleapis.com/gtidocresources/guides/dtm/images/researchtool_forum_details_20240418.png)

---

← [Monitor Compromised Credentials](monitors-guide/monitor-compromised-credentials.md) · [up](README.md) · [Configuring DTM Email Notifications](configuring-dtm-email-notifications.md) →

*Archived from <https://gtidocs.virustotal.com/docs/research-tools>.*
