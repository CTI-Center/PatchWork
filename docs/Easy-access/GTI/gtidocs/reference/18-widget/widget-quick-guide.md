---
title: "Google Threat Intelligence Widget Quick guide"
source: https://gtidocs.virustotal.com/reference/widget-quick-guide
slug: widget-quick-guide
section: reference
group: "Widget"
updatedAt: 2025-09-25T00:46:34.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [Widget](README.md) › Google Threat Intelligence Widget Quick guide

---

# google-threat-intelligence-widget-quick-guide

# google-threat-intelligence-widget-quick-guide

## overview

![GTI Widget Overview](https://storage.googleapis.com/gtidocresources/API/markdown/gti-widget/images/gti_widget_overview_20250820.png)

Google Threat Intelligence Widget creates a standard way to show information powered by Google Threat Intelligence in third party platforms. It is not just a mechanism to consume the Google Threat Intelligence information, but a way to describe what specific information can be integrated in third party applications.

The widget focuses on four main areas described by each tab:

* **The Summary tab** offers a general overview and crucial information about the analyzed file, domain, URL, or IP address. Key elements include the Google Threat Intelligence assessment and the associations section, which lists related high-level objects such as threat actors and malware. Additionally, users can find important information like the verdicts from engine vendors and sandboxes.
* **The IOCs tab** provides a structured list of indicators associated with the observed file, domain, url or ip address. These are pieces of evidence that can indicate malicious activity. The information is organized into relationships.
* **The TTPs (Tactics, Techniques, and Procedures) tab** provides insights into the observed behaviors and methods associated with the analyzed file or threat. It categorizes these behaviors according to the MITRE ATT\&CK framework. This tab helps you understand the "how" behind the threat.
* **The Community tab** provides the comments made by the community in VT and Google Threat Intelligence for the observed indicator.

### demo

We already have a demo view where you can play with several example Iocs or play with different color schemas: <https://www.virustotal.com/gtiwidget/demo>

### feedback

You can report bugs or any kind of feedback using the [contact form](https://www.virustotal.com/gui/contact-us/technical-support).

## widget-use

Generating the Google Threat Intelligence widget is exclusively available to Google Threat Intelligence customers. The process involves two steps for UI integration: first, an ephemeral URL must be generated, and second, this URL is then used within your user interface.

### first-call:

First you need to use the [get-widget-url endpoint](rendering-url/get-widget-url.md):

```
GET https://www.virustotal.com/api/v3/gtiwidget?query=630325cac09ac3fab908f903e3b00d0dadd5fdaa0875ed8496fcbb97a558d0da
```

Where the query can be a sha256 file hash, a domain, an IPv4 address or an url. This step is usually done in the backend and it requires a Google Threat Intelligence API key to call the endpoint.

In order to get the Google Threat Intelligence Assessment in the first call you have to provide also the x-tool header with a value that identifies your integration.

Response example:

```json
{
  "data": {
    "id": "630325cac09ac3fab908f903e3b00d0dadd5fdaa0875ed8496fcbb97a558d0da",
    "type": "file",
    "found": true,
    "gti_assessment": {
      "description": "...",
      "threat_score": {
        "value": 80
      },
      "verdict": {
        "value": "VERDICT_MALICIOUS"
      },
      "serverity": {
        "value": "SEVERITY_HIGH"
      }
    },
    "url": "https://www.virustotal.com/gtiwidget/ABMXx8NjMwMzI1Y2FjMDlhYzNmYWI5MDhmOTAzZTNiMDBkMGRhZGQ1ZmRhYTA4NzVlZDg0OTZmY2JiOTdhNTU4ZDBkYXx8ZmlsZXx8djN8fDE3NDI5ODAzMjF8fDY5ZjZlYjI4ODNiNDdiOTc0ZjJkZGExMjU0OGJhNjkyMzdjODY1NTA1NzM0NDA1ZmJhZTdhNDAwNTRjMTY1OWU"
  }
}
```

This URL is valid for 24 hours and does not require any kind of authentication to call it.

### second-call:

Embed the URL from the response within an iframe.

![GTI Widget in an iframe](https://storage.googleapis.com/gtidocresources/API/markdown/gti-widget/images/gti_widget_iframe_20250820.png)

For optimal display of the widget, a width of 900px is recommended.

## widget-customization

### basic

The widget includes both dark and light themes. The dark theme is the default. To use the light theme, include the query parameter `theme=light` in the API call:

```
GET https://www.virustotal.com/api/v3/gtiwidget?query=630325cac09ac3fab908f903e3b00d0dadd5fdaa0875ed8496fcbb97a558d0da&theme=light
```

![GTI Widget with light theme](https://storage.googleapis.com/gtidocresources/API/markdown/gti-widget/images/gti_widget_light_theme_20250820.png)

Based on our experience with the previous VirusTotal Augment widget, these two theme options should be sufficient for most users' customization needs.

### advanced

For users seeking a more deeply integrated experience, the widget offers six additional query parameters to tailor its color scheme. These include three background color parameters (**bg1**, **bg2**, **bg3**), three foreground color parameters (**fg1**, **fg2**, **fg3**), and an accent (**acc**) color parameter.

These parameters can be used in any combination alongside the existing `theme` parameter to override the default widget colors. All color parameters accept hexadecimal color values.

```
GET https://www.virustotal.com/api/v3/gtiwidget?query=630325cac09ac3fab908f903e3b00d0dadd5fdaa0875ed8496fcbb97a558d0da&theme=light&bg1=ff11ff&acc=00ff00
```

---

← [YARA Rulesets](../17-api-objects/yara-rulesets-object.md) · [up](README.md) · [Rendering URL](rendering-url.md) →

*Archived from <https://gtidocs.virustotal.com/reference/widget-quick-guide>.*
