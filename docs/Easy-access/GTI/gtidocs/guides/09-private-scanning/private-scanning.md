---
title: "Private Scanning"
source: https://gtidocs.virustotal.com/docs/private-scanning
slug: private-scanning
section: guides
group: "Private Scanning"
updatedAt: 2026-06-16T10:42:12.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [Private Scanning](README.md) › Private Scanning

---

# private-scanning

**TL;DR: *See files or URLs through the eyes of Google Threat Intelligence (Google TI) without uploading them to the main threat corpus, in other words, without sharing with other Google TI users or distributing them beyond your organization. Static, dynamic, network and similarity analysis included for files, as well as automated threat intel enrichment, but it will NOT contain our multi-antivirus or url-scan partners verdicts.***

> ⚠️ **IMPORTANT OBSERVATIONS!**
>
> Private Scanning does not replace Google TI's standard upload experience, you must use the [Private Scanning form](https://www.virustotal.com/gui/private-scanning/.) to keep uploads private. When using Private Scanning:
>
> * Submitted files and URLs do not abandon Google TI's infrastructure.
> * All tools acting on the submitted files and URLs run on Google TI infrastructure.
> * Submitted files and URLs are not shared with third parties, unless the file or URL is also uploaded to the standard Google TI service in addition to Private Scanning.
> * Submitted files and URLs are permanently deleted from our private buckets after their retention period expires (usually 24 hours, although the default value can be set in your organization's Private Scanning preferences).
> * **Analysis reports for submitted files and URLs are only visible to users within your organization (Google TI group) and are also permanently deleted after their retention period expires.**
>
> Note that Private Scanning is not meant to substitute Google TI's standard crowdsourced community, but rather complement it in very specific and justified instances in which certain files or URLs can't be shared with security vendors and other industry peers. **If Private Scanning clearly suggests that a file or URL is malicious, we encourage you to upload it to [standard Google TI](https://www.virustotal.com/) in order to share the threat and its context with other defenders.**

Private Scanning allows you to analyze files and URLs with Google TI in a privacy preserving fashion. Files and URLs uploaded via this offering won't be shared with anyone beyond your organization, and will remain in Google TI only for a brief period of time. The resulting analyses will be ephemeral too and only visible to your Google TI group.

Note that private analyses won't contain antivirus verdicts, they will contain only the output of all the other characterization and contextualization tools that we run, including sandboxes.

![Private Overview](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_overview_20230929.png)

As with most of our functionality you have two options to use it, through our [API](https://gtidocs.readme.io/reference/upload-file-private-scanning) or via the web interface. We have also developed a [command-line script](https://storage.googleapis.com/vtcdn/api-scripts/privscan.py) to get you started with automation.

# accessing-the-private-scanning-web-interface

To access this service you can follow the link at the sidebar menu ([https://www.virustotal.com/gui/private-scanning/](https://www.virustotal.com/gui/private-scanning/.)). Note that Private Scanning is a paid offering and you will need specific privileges to access it, please [do not hesitate to request a trial](https://www.virustotal.com/gui/contact-us/premium-services).

![Private Scanning Link](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_link_20240405.png)

In the Private Scanning main view you will see a couple of tabs to switch between the view that allows you to upload a file or URL ("*Scan*") and the view with the list of private analyses ("*Analyses*"). Note that this list only includes analyses of files or URLs submitted by your organization, and note that these reports are only visible to your organization.

![Private Scanning List](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_list_20240405.png)

# analyzing-using-the-private-scanning-module

> ℹ️ **Network connectivity options**
>
> Regardless of whether live interaction is enabled, the network mode can be modified based on the network capabilities of each sandbox, as shown in the last column of each table at <https://gtidocs.virustotal.com/docs/in-house-sandboxes>.
>
> If a file is suspected of connecting to a TOR service, the analysis must be launched using the TOR network mode to resolve access. If a URL is opened in the browser, it will be handled via Firefox without requiring the TOR Browser.
>
> Similarly to files, it is important to emphasize that if a .onion URL is submitted, it will always be forced to TOR network mode, opening the URL in Firefox without needing the TOR Browser.

To upload and analyze a file or URL privately, go to the "*Scan*" section. There are several ways to get there, either by clicking on the corresponding tab in the main view of Private Scanning, or on the link with the text "*go to upload form*" displayed at the top of any view belonging to Private Scanning.

![Private Scanning Links](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_links1_20240405.png)

## analyzing-a-file

> ℹ️ **Compressed files (ZIP, 7z, RAR, tar.bz2, etc)**
>
> 1. It is recommended you unbundle these and scan them individually. This will provide the most thorough analysis. Static analysis will work best with single files.
> 2. In the web interface you may upload a ZIP file less than 3MB with a single bundled file that is password encrypted. This may help bypass Antiviruses checks on the client side.
> 3. Compressed files will be sent to sandboxes and attempts to unencrypted files is done on a best-effort bassis. We will check if the password is `infected`.
> 4. If files in the compressed bundle are extracted, they will appear in the relationships as files you may chose to analyse.

Once you are in the view to scan files, by clicking on the button "*Choose file*" you will be prompted to choose a file from your computer. After the file is chosen you will be requested to confirm the upload.

![Private Scanning Choose a file](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_choose_file_20240405.png)

You may also set detonation options such as whether the dynamic execution in sandboxes should have internet connectivity, the retention time in days that the files and reports will have, after which they will be deleted, or the region in which you want the files to be temporarily stored.

![Private Scanning Options](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_options_20240712.png)

With "Enable Live interaction" selected, you can choose the desired sandbox and maximum timeout.

![Live interaction options](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_live_interactions_20250205.png)

If the file is already available in the standard Google TI open corpus, you will be informed accordingly and you may navigate to the corresponding Google TI ENTERPRISE report.

![Private Scanning Known File](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_knownfile_20240405.png)

As soon as the file is uploaded you'll be redirected to the report view, where you can see the scan progress and preliminary data regarding your file. The full analysis can take several minutes to complete, note that the file will be detonated in multiple sandboxes for a couple of minutes and network traces will be subsequently analyzed with intrusion detection systems.

![Private Scanning Report](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_report_20240405.png)

## analyzing-a-url

In the view for scanning URLs you may specify the URL you want to scan privately. Once introduced, you can run the scan by pressing the *Enter* key.

![Private Scanning Scan a URL](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_scan_url_20240405.png)

As in the case of file analysis, URL analysis provides some options for configuring your analysis. You can specify:

* If the URL should be executed in any of our Sandboxes.
* When Sandboxes executions are enabled, you can enable Live interaction. With live interaction you will have the ability to control the keyboard and mouse to interact with the analysis. Click on the live interaction link which will appear about 30 to 60 seconds after the URL has been uploaded.
* Internet connection options.
* Preferred sanbox locale.
* User agent.
* The retention period days.
* Select a storage region where the files derived from the analysis will be stored.

![Private Scanning URL options](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_url_options_20250923.png)

As soon as the URL is uploaded you'll be redirected to the report view, where you can see the scan progress and preliminary data regarding your URL.

![Private Scanning URL analysis](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_url_analysis_20251007.png)

Once the analysis is completed you will be redirected to the report. The reports are made up of several tabs.

The **Details** tab provides a technical summary of the HTTP response and the HTML content of the analyzed URL.

It shows the final URL reached after any redirections, along with the IP address of the server that provided the content and the HTTP status code of the response. The tab also includes the size and the SHA-256 hash of the response body, which can be used to identify the downloaded content.

A list of all HTTP response headers sent by the server is available, providing details about the web server configuration and how the content should be handled by the browser. Furthermore, information parsed directly from the HTML, such as the page title and the content of its meta tags, is displayed. Finally, the complete redirection chain, showing each URL visited from the initial request to the final destination, is listed.

![Private Scanning URL details tab](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_url_detailstab_20250923.png)

The **Browser** tab provides a comprehensive overview of a URL's behavior when rendered in a web browser. This dynamic analysis offers insights into the resources a page loads, its interactions with servers, and the code it executes. Here's a breakdown of the information you'll find:

* A visual snapshot of the rendered webpage is available, though viewing explicit content may require user permission.
* A summary of key page metrics is provided, including the number of requests, domains, IPs, and the total page size.
* Any recognized brands associated with the URL are identified.
* If the initial URL redirects, the redirection chain is displayed.
* A table lists all HTTP requests made by the page, showing the requested URL, HTTP status code, and other header information.
* A list of global variables present in the page's JavaScript environment is available.
* Details of all cookies set by the page, including their domain, expiration date, name, and value, are provided.
* Messages logged to the browser's developer console are displayed, which can be useful for debugging. For example, a message might indicate that a "development build of Vue" is being used.

![Private Scanning URL browser tab](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_url_browsertab_20250923.png)

The **Behavior** tab provides a detailed report of the activities observed when the URL was accessed in a sandboxed environment. This includes a summary of network communications, interactions with the file system and registry, and process activity, along with screenshots taken during the execution.

The tab details all network communications, such as HTTP requests with their full headers, DNS resolutions showing which domains were contacted, and a list of all IP traffic. It also provides information on encrypted communications, including JA3 digests and TLS certificate details.

File system activities are logged, showing which files were opened, written to, deleted, or dropped onto the system during the analysis. Similarly, any changes made to the Windows Registry are recorded, such as the deletion of registry keys.

The report also provides a comprehensive overview of process and service actions. This includes a list of all processes that were created or terminated, and a process tree that shows the parent-child relationships between them.

Finally, the tab includes screenshots captured at different stages of the analysis, providing a visual record of the URL's behavior in the sandbox. The MITRE ATT\&CK framework is used to map observed behaviors to known adversary tactics and techniques, providing context for the observed actions.

![Private Scanning URL behavior tab](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_url_behaviortab_20250923.png)

The **Relations** tab illustrates the connections between the analyzed URL and other resources. It provides a list of all outgoing links discovered on the page, which are the URLs that the analyzed page links to. Additionally, this tab displays a list of files that were downloaded when the URL was accessed. Each downloaded file is identified by its hash, and the report provides further details about these files.

![Private Scanning URL Relations tab](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_url_relationstab_20250923.png)

The **Content** tab displays the raw content of the URL's response body. It is divided into two main sections: the "DOM tree" and "Strings".

The "DOM tree" view presents the HTML structure of the page, allowing you to inspect the raw HTML code as it was received from the server. You can switch between an "Original" and a "Formatted" view for better readability.

The "Strings" section extracts and lists all the text strings found within the page's content. This can be useful for identifying interesting snippets of text, URLs, or other indicators embedded in the response.

![Private Scanning URL Content tab](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_url_contenttab_20250923.png)

# private-scanning-file-reports

Once the analysis concludes, you will have access to a file report, but as mentioned previously, private analyses won't contain antivirus verdicts, they will only contain the output of all the other analysis and contextualization tools that we have in Google TI, including sandboxes:

* Matches from your active Livehunt rules or from Livehunt rules that have been shared with you.
* Crowdsourced (YARA, SIGMA, IDS, AI) rule matching to produce flags and detections.
* Static and behavioural pattern analysis relevant to produce maliciousness determinations.
* Static tooling such as file signature extractors, file type identification, file format dissection, document macro decoders, strings analysis, etc.
* Dynamic analysis (detonation) in multiple sandboxes. Support for Windows, Mac OS X, Linux and Android. Process, file system, memory, network, etc. analysis.
* Behaviour and static feature mapping to MITRE ATT\&CK matrix.
* Malware configuration extractors and decryptors.
* Threat intel enrichment for all extracted IoCs (embedded IPs, contacted domains, download URLs, etc.).
* Clustering and similarity analysis, including attribution to campaigns, toolkit and actors through similar files.

The reports are made up of several tabs. The **detection tab** displays granular flags coming from crowdsourced (YARA, SIGMA, IDS, AI) matching, as well as sandbox execution verdicts. You may hover over matched rules to open them in a sidebar and export them to improve your security controls.

![Private Scanning Detection](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_detection_20240405.png)

The **details tab** records features extracted through static analysis, this includes, but is not limited to:

* Basic properties: hashes, similarity hashes, file type identification, file size, compiler and packer identification.
* Capabilities and indicators: verbose insights into interesting functionality and properties from a cybersecurity point of view.
* File signature: signature and countersignature chain, software publisher, original file names, etc.
* File format dissectors: PE sections, imports, exports, document macro decoders, etc.

All of the highlighted properties are pivotable, meaning that clicking on them will launch a standard Google TI ENTERPRISE search across the entire Google TI corpus to locate other (non-private) files that exhibit the same property. This is extremely useful to identify other variants of the same attack and gather further context, including potential campaigns or actors tied to the threat.

The **relations tab** lists any related IoCs observed during static and dynamic analysis of the file, these can be used for hunting, remediation and containment purposes, as well as to proactively protect your organization by blocking them in your security solutions. Some of the relationships include:

* Execution parents: files that have been seen dropping the file under study when executed in a sandbox.
* Dropped files: files that are dropped when the file under consideration is detonated in a sandbox.
* Embedded (domains, IPs, URLs): network IoCs seen within the binary body of the file under consideration, e.g. as a string.
* Contacted (domains, IPs, URLs): network resources to which the file reaches out when executed in multiple sandboxes.
* Download URLs: Any URLs that standard Google TI has seen delivering the file under consideration.

Whenever these related IoCs are present in the standard Google TI corpus, they are automatically enriched with reputation and threat context coming from Google TI ENTERPRISE: security vendor detection ratios, geolocation, in-the-wild prevalence, etc. Moreover, all these related IoCs that are present in the standard Google TI corpus are pivotable, meaning that clicking on them will open the IoC report on the standard Google TI ENTERPRISE web interface to help you gather further context.

As a final remark relative to the relations tab, note that when you upload a compressed bundle and it contains a file that is already in the Google TI corpus, we'll let you know so you can pivot to the standard Google TI ENTERPRISE report.

The **behavior tab** displays the execution report summaries for all sandboxes that act on the file. The summary includes notions such as: MITRE ATT\&CK TTPs, file system actions, registry actions, process and service actions, synchronization mechanisms and signals (e.g. mutexes created), network communications, screenshots, etc.

![Private Scanning Behavior](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_behavior_20240405.png)

The activity summary toolbar also allows you to access more technical assets such as network execution traces (PCAPs), detailed dynamic reports (e.g. API calls), windows event logs, memory dumps, etc.

![Private Scanning Activity](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_activity_20240405.png)

The **community tab** will list any Google TI collections that contain a hash for the file under consideration, as well as any threat actors related to those collections.

![Private Scanning Community](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_community_20230929.png)

# locating-similar-files-and-expanding-context

One of the most useful and differentiated features of Private Scanning is pivoting to other similar files in the open Google TI ENTERPRISE corpus. This can be done by acting on the similarity icon in the file summary block, multiple similarity analysis techniques are available:
![](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_similar_20240405.png)

By jumping to other similar files you may understand industry reputation and naming for other variants of the threat, commonalities and in-the-wild patterns, lookup and submission activity (telemetry) for related files, etc.

![Private Scanning Distribution Vectors](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_distributionvectors_20240505.png)

With the similar files you can also leverage Google TI DIFF to automatically build YARA rules for the pertinent malware toolkit and you may gain further insights on the corresponding threat campaign and actors behind it:

![Private Scanning Actors](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_actors_20240405.png)

# deleting-files-and-analysis-reports

The files and their analysis reports in Private Scanning have an expiration date as mentioned above, and are deleted once their retention period expires. However, you can delete both the file and its report even before that time expires. For this purpose go to the report header and open the menu "*More*". There you will find the options to either delete only the file and keep the report (until its retention period ends), or to delete the file and its report immediately:

![Private SCanning Delete](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_delete_20240405.png)

# private-scanning-url-reports

Once the analysis of a URL concludes, you will have access to its URL report. Private analyses won't contain antivirus verdicts, but they will contain the output of other analysis and contextualization tools that we have in Google TI:

The **details tab** displays additional information about the scanned resource, such as the HTTP response headers and body info returned by the server upon asking for the given URL, the list of all redirections until the final URL is reached, etc.

![Private Scanning URL details](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_url_details_20240405.png)

The **behavior tab** displays useful information such as page statistics, cookies, HTTP transactions, a screenshot, etc.

![Private Scanning URL behaviour](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_url_behavior_20240405.png)

# private-analysis-workflow

| Task          | Description                                                 | Duration                       | Dependency |
| :------------ | :---------------------------------------------------------- | :----------------------------- | :--------- |
| Upload        | User uploads sample, analysis ID generated.                 | 1 to 30 seconds; avg 3 seconds | None       |
| Prefilter     | Detect which sandbox to send sample to.                     | 1 to 60 seconds; avg 5sec      | Upload     |
| Sandboxes     | Detonate in sandboxes.                                      | 4 to 15 minutes, avg 7min      | Prefilter  |
| Sigma         | Analyze logs against sigma rules.                           | 1-2 min                        | Sandboxes  |
| IDS           | Analyze network traffic PCAP with snort and suricata rules. | 2-12 min. Avg 3 min.           | Sandboxes  |
| MalwareConfig | Extract malware config and payloads from memory dumps.      | 2-10 min                       | Sandboxes  |

# final-technical-highlights

![Private Scanning Final Highlights](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_highlights_20230929.png)

> ❓
>
> ### **Looking for a benefit analysis?**
>
> You may want to share the [Private Scanning brief](https://assets.virustotal.com/vt-brief-private-scanning.pdf) with your stakeholders or leadership in order to justify its value.

---

← [Management](../08-threat-graph/threat-graph-management.md) · [up](README.md) · [OpenVPN support on private scanning](private-scanning-openvpn.md) →

*Archived from <https://gtidocs.virustotal.com/docs/private-scanning>.*
