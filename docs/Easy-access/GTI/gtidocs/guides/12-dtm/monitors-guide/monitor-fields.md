---
title: "Monitor Fields"
source: https://gtidocs.virustotal.com/docs/monitor-fields
slug: monitor-fields
section: guides
group: "DTM"
updatedAt: 2025-09-25T16:58:55.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [DTM](../README.md) › [Monitors](../monitors-guide.md) › Monitor Fields

---

# monitor-fields

# dtm-monitor-&-research-tools-fields-|-docs

> ## Excerpt
>
> When creating Monitors in Digital Threat Monitoring (DTM), the Topics you select for your Monitor Conditions are actually search groups. These search groups match your values against a set of related entity types making it easier to build effective Monitors.

***

When creating Monitors in Digital Threat Monitoring (DTM), the Topics you select for your Monitor Conditions are actually search groups. These search groups match your values against a set of related entity types making it easier to build effective Monitors.

For example, using the `Network Information` topic with a `must contain` Operator and a value of `acme.com` would match if `acme.com` was found in a domain name, URL, or Typosquatted domain. This is because the `Network Information` topic searches across all of those entity types.

The following table includes the available fields in the monitors and the type of data you should enter.

| Monitor Topic | Monitor API Topic | Monitor Matches on Topics &amp;<br>Research Tools Entities | Description |
| --- | --- | --- | --- |
| Bank Identification Number | group_bin | bin | Complete Bank Identification Number |
| bin_foreign | Foreign (non-US) Bank Identification number |  |  |
| bin_partial | Partial Bank Identification number |  |  |
| Brand | group_brand | identity_name | A name of a person, place, company, or thing |
| name | A name of a person, place, company, or thing |  |  |
| organization | The name of an organization |  |  |
| product | The name of a product |  |  |
| brand | Brand name or trademark |  |  |
| product_batch_name | A batch number for a product |  |  |
| Crypto | group_crypto | atom_address | Wallet address for the Cosmos (ATOM) cryptocurrency |
| bch_address | Wallet address for the Bitcoin Cash (BCH) cryptocurrency |  |  |
| btc_address | Wallet address for the Bitcoin (BTC) cryptocurrency |  |  |
| dash_address | Wallet address for the Dash cryptocurrency |  |  |
| doge_address | Wallet address for the Doge cryptocurrency |  |  |
| ltc_address | Wallet address for the Litecoin cryptocurrency |  |  |
| xlm_address | Wallet address for the Stellar (XLM) cryptocurrency |  |  |
| xmr_address | Wallet address for the Monero (XMR) cryptocurrency |  |  |
| zec_address | Wallet address for the Zcash (ZEC) cryptocurrency |  |  |
| Filenames &amp; Paths | group_paths | filename | A name or identifier for a file |
| path | A location of a file or folder on a filesystem |  |  |
| registry_key | A path in the Windows registry |  |  |
| Free Text Search | keyword | <br> | Will text search all fields of the document for the given keyword(s) |
| Hash | group_hash | md5_hash | A MD5 cryptographic hash |
| sha1_hash | A SHA1 cryptographic hash |  |  |
| sha256_hash | A SHA256 cryptographic hash |  |  |
| Industry | label_industry | label_industry | Industry code of the affected industries of the original document<pre>{<br>'ind.aeromil': 'Aerospace and Defense',<br>'ind.agri': 'Agriculture',<br>'ind.auto': 'Automotive',<br>'ind.chemmat': 'Chemicals &amp; Materials',<br>'ind.civil': 'Civil Society &amp; Non-Profits',<br>'ind.constructeng': 'Construction &amp; Engineering',<br>'ind.edu': 'Education',<br>'ind.energyutils': 'Energy &amp; Utilities',<br>'ind.fin': 'Financial Services',<br>'ind.gov': 'Governments',<br>'ind.health': 'Healthcare',<br>'ind.hosp': 'Hospitality',<br>'ind.legalprofserv': 'Legal &amp; Professional Services',<br>'ind.manuf': 'Manufacturing',<br>'ind.mediaentertain': 'Media &amp; Entertainment',<br>'ind.oilgas': 'Oil &amp; Gas',<br>'ind.pharma': 'Pharmaceuticals',<br>'ind.retail': 'Retail',<br>'ind.tech': 'Technology',<br>'ind.telecom': 'Telecommunications',<br>'ind.transport': 'Transportation'<br>}</pre> |
| Language | label_language | label_language | Two-character <a href="https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes" name="" rel="noopener noreferrer" target="_blank" title="">ISO 639-1</a> language code specifying the detected language type |
| Locations | group_location | city | A city or locality name |
| country | A country or nationality name |  |  |
| location_name | The name of a physical place or location |  |  |
| Lucene Text Query (Advanced) | lucene | <br> | Searches all text fields of documents based on the <a href="https://www.elastic.co/guide/en/elasticsearch/reference/7.15/query-dsl-query-string-query.html#query-string-syntax" name="" rel="noopener noreferrer" target="_blank" title="">Lucene query syntax</a><div class="alert alert-info">For more information about using Lucene in DTM, see <a href="https://gtidocs.virustotal.com/home/dtm-lucene-queries" name="Lucene%20Queries%20in%20DTM" title="Lucene Queries in DTM">Lucene Queries in DTM</a></div> |
| Mime-Type | label_type | label_type | Detected MIME type of the originating document. Valid types include: application/font-sfnt, application/javascript, application/json, application/octet-stream, application/pdf, application/pgp-keys, application/postscript, application/vmd.ms-opentype, application/appleworks3, application/dosexec, application/x-empty, application/x-sqlite3, application/x-tar, application/x-wine-extension-ini, application/x-xar, image/gif, image/svg, image/xvg+xml, image/x-portable-greymap, message/news, message/rfc822, text/html, text/plain, text/troff, text/x-asm, text/x-awk, text/x-c, text/x-c++, text/x-diff, text/x-fortran, text/x-java, text/x-lisp, text/x-m4, text/x-makefile, text/x-ms-regedit, text/x-mdos-batch, text/x-objective-c, text/x-pascal, text/x-perl, text/x-php, text/x-po, text/x-python, text/x-ruby, text/x-shellscript, text/x-tex, text/xml, text/x-sgi-movie |
| Network Information | group_network | domain | An <a href="https://datatracker.ietf.org/doc/html/rfc1035" name="" rel="noopener noreferrer" target="_blank" title="">RFC1035</a> domain name |
| ipv4_address | An IPv4 Address |  |  |
| ipv6_address | An IPv6 Address |  |  |
| typosquatted_domain | Accepts a plain fully qualified domain name (not URL's) and will attempt to detect and alert when similar domains are registered |  |  |
| url | An <a href="https://www.ietf.org/rfc/rfc1738.txt" name="" rel="noopener noreferrer" target="_blank" title="">RFC1738</a> uniform resource locator (URL) |  |  |
| Person or Identity | group_identity | client_identifier | An OpenID client identifier |
| email_address | An <a href="https://datatracker.ietf.org/doc/html/rfc5322" name="" rel="noopener noreferrer" target="_blank" title="">RFC5322</a> e-mail address |  |  |
| identity_name | A name of a person, place, company, or thing |  |  |
| name | A name of a person, place, company, or thing |  |  |
| phone_number | A partial or complete phone number |  |  |
| telegram_user_name | A username for the Telegram messaging platform |  |  |
| twitter_handle | A user name for the Twitter platform |  |  |
| Search Collection Type | doc_type | doc_type | The specific document type to match, valid types include:<ul><li>Compromised Credentials</li><li>Document Analysis (supported in <span class="ko-glossary-term" data-toggle="popover" data-content="Application Programming Interface" data-original-title="" title="">API</span> only)</li><li>Domain Discovery</li><li>Email (supported in API only)</li><li>Forum Posts</li><li>Messages</li><li>Pastes</li><li>Shop Listings</li><li>Web Content</li></ul> |
| Social Media | group_social | twitter_handle | X (formerly Twitter) handle |
| telegram_user_name | Telegram username |  |  |
| hashtag | Hashtag value |  |  |
| name | Social media username |  |  |
| icq_uin | ICQ User ID Number |  |  |
| jid | Cisco Jabber user ID |  |  |
| Threat Type | label_threat | Pre-defined list | Threat specifier of the original document. Valid types include:<ul><li><code>information-security/anonymization</code>: Anonymization</li><li><code>information-security/apt</code>: Advanced Persistent Threat</li><li><code>information-security/botnet</code>: Botnet</li><li><code>information-security/compromised</code>: Compromised Infrastructure</li><li><code>information-security/doxing</code>: Personal Information Disclosure</li><li><code>information-security/exploit</code>: Exploit</li><li><code>information-security/health-risk</code>: Health Risk</li><li><code>information-security/information-leak</code>: Information Leak</li><li><code>information-security/information-leak/confidential</code>: Confidential Document Leak</li><li><code>information-security/information-leak/credentials</code>: Credential Leak</li><li><code>information-security/information-leak/payment-cards</code>: Credit Cards</li><li><code>information-security/malicious-activity</code>: Malicious Activity</li><li><code>information-security/malicious-infrastructure</code>: Malicious Infrastructure</li><li><code>information-security/malware</code> -&gt; Malware</li><li><code>information-security/malware/ransomware</code>: Ransomware</li><li><code>information-security/malware/ransomware-victim-listing</code>: Ransomware Victim Listing</li><li><code>information-security/phishing</code>: Phishing</li><li><code>information-security/security-research</code>: Security Research</li><li><code>information-security/spam</code>: Spam</li></ul> |
| Threat Intel | group_threats | cve | A <a href="https://www.cve.org/" name="" rel="noopener noreferrer" target="_blank" title="">Common Vulnerabilities and Exposures (CVE)</a> Identifier |
| threat_group_name | The name of a threat group |  |  |
| threat_name | The name of a particular type of threat |  |  |
| service_name | The name of a service |  |  |
| cwe | A <a href="https://cwe.mitre.org/" name="" rel="noopener noreferrer" target="_blank" title="">Common Weakness Enumeration (CWE)</a> Identifier |  |  |
| Tokens &amp; Key | group_keys | access_token | Access token used by applications to authenticate against protected resources |
| crypto_key_private | Asymmetric cryptography private key |  |  |
| crypto_key_public | Asymmetric cryptograph public key |  |  |
| password_plaintext | A detected plaintext password |  |  |
| predict_password_plaintext | A detected plaintext password (lower confidence) |  |  |

---

← [Monitors](../monitors-guide.md) · [up](../README.md) · [Build Effective Monitors](monitor-scenarios.md) →

*Archived from <https://gtidocs.virustotal.com/docs/monitor-fields>.*
