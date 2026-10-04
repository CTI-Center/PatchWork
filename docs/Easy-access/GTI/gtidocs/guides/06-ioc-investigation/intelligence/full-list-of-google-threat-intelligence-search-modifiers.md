---
title: "Full list of Google Threat Intelligence search modifiers"
source: https://gtidocs.virustotal.com/docs/full-list-of-google-threat-intelligence-search-modifiers
slug: full-list-of-google-threat-intelligence-search-modifiers
section: guides
group: "IOC Investigation"
updatedAt: 2026-07-29T13:22:07.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [IOC Investigation](../README.md) › [Intelligence / Web searching](../intelligence.md) › Full list of Google Threat Intelligence search modifiers

---

# full-list-of-google-threat-intelligence-search-modifiers

Although we have the most common modifiers documented with description and examples at:

[File search modifiers article](file-search-modifiers.md).
[IP Address search modifiers article](ip-address-search-modifiers.md).
[Domain search modifiers article](domain-search-modifiers.md).

In this article you will find the full list of modifiers for each entity:

[List of File modifiers](#list-of-file-modifiers)
[List of IP modifiers](#list-of-ip-modifiers)
[List of Domain modifiers](#list-of-file-modifiers)
[List of URL modifiers](#list-of-url-modifiers)
[List of Collection modifiers](#list-of-collection-modifiers)
[List of IOC Stream modifiers](#list-of-ioc-stream-modifiers)

# list-of-file-modifiers

***

|                               |                             |                                |                                |
| ----------------------------- | --------------------------- | ------------------------------ | ------------------------------ |
| acronis                       | ad\_aware                   | ahnlab\_v3                     | alibaba                        |
| alibabacloud                  | alyac                       | androguard                     | androguard\_package            |
| antiy\_avl                    | apex                        | arcabit                        | attack\_tactic                 |
| attack\_technique             | authentihash                | avast                          | avast\_mobile                  |
| avg                           | avira                       | avware                         | babable                        |
| baidu                         | behash                      | behaviour                      | behaviour\_command\_executions |
| behaviour\_created\_processes | behaviour\_files            | behaviour\_injected\_processes | behaviour\_network             |
| behaviour\_processes          | behaviour\_registry         | behaviour\_services            | behaviour\_signature           |
| behaviour\_tags               | bitdam\_atp                 | bitdefender                    | bitdefenderfalx                |
| bitdefendertheta              | bkav                        | bytedefend\_ai\_analysis       | bytedefend\_ai\_verdict        |
| c2ae                          | capa                        | capability\_tag                | cape                           |
| cape\_linux                   | cape\_sandbox               | cat\_quickheal                 | clamav                         |
| clue                          | cmc                         | codeinsight                    | codeinsight\_verdict           |
| collection                    | comment                     | comment\_author                | contacted\_ip                  |
| content                       | cp                          | creation\_date                 | crowdsourced\_ai\_analysis     |
| crowdsourced\_ids             | crowdsourced\_yara\_rule    | crowdstrike                    | ctx                            |
| cyber\_adapt                  | cybereason                  | cylance                        | cynet                          |
| das\_security\_orcas          | deepinstinct                | detectiteasy                   | dns\_lookup\_count             |
| docguard                      | dr\_web\_vxcube             | drweb                          | elastic                        |
| elf\_digest                   | email\_subject              | embedded\_domain               | embedded\_ip                   |
| embedded\_url                 | emsisoft                    | endgame                        | engines                        |
| ep                            | eset\_nod32                 | exodialabs\_ai\_analysis       | exodialabs\_ai\_verdict        |
| exports                       | f\_prot                     | f\_secure                      | f\_secure\_sandbox             |
| filecondis\_dhash             | fireeye                     | first\_submitter               | fortinet                       |
| fs                            | gdata                       | google                         | google\_safe\_browsing         |
| google\_safebrowsing          | goresym                     | gridinsoft                     | gti\_score                     |
| gti\_severity                 | gti\_verdict                | have                           | hispasec\_ai\_analysis         |
| hispasec\_ai\_verdict         | http\_conversation\_count   | huorong                        | ikarus                         |
| imphash                       | imports                     | invincea                       | ip\_traffic\_count             |
| itw                           | jiangmin                    | k7antivirus                    | k7gw                           |
| kaspersky                     | kingsoft                    | la                             | lang                           |
| last\_modification\_date      | lastline                    | lionic                         | ls                             |
| magic                         | magika                      | main\_icon\_dhash              | main\_icon\_md5                |
| malware\_config               | malwarebytes                | malwation                      | maxsecure                      |
| mbc                           | mcafee                      | mcafeed                        | metadata                       |
| microsoft                     | microsoft\_sysinternals     | microworld\_escan              | min\_engines\_banker           |
| min\_engines\_emotet          | name                        | nano\_antivirus                | netguid                        |
| nics\_ai\_analysis            | nics\_ai\_verdict           | nprotect                       | nsfocus\_poma                  |
| omniasec\_ai\_analysis        | omniasec\_ai\_verdict       | os\_x\_sandbox                 | p                              |
| packer                        | paloalto                    | panda                          | permhash                       |
| pickle\_vhash                 | qianxin\_reddrip            | qihoo\_360                     | reaqta\_hive                   |
| reputation                    | resource                    | rich\_pe\_header\_hash         | rising                         |
| rising\_moves                 | s                           | sandbox\_name                  | sangfor                        |
| sangfor\_zsand                | scan\_timeout               | scan\_unsupported              | secneurx                       |
| secondwrite                   | section                     | sectionmd5                     | segment                        |
| sentinelone                   | sha256                      | sigcheck                       | sigma\_critical                |
| sigma\_high                   | sigma\_low                  | sigma\_medium                  | sigma\_rule                    |
| sigma\_ruleset                | similar-to                  | size                           | skyhigh                        |
| sndbox                        | sophos                      | ssdeep                         | submitter                      |
| subspan                       | suggested\_threat\_label    | superantispyware               | symantec                       |
| symantecmobileinsight         | symhash                     | tachyon                        | tag                            |
| tehtris                       | telfhash                    | tencent                        | tencent\_habo                  |
| thehacker                     | threat\_actor               | tlsh                           | totaldefense                   |
| traffic                       | trapmine                    | trellixens                     | trendmicro                     |
| trendmicro\_housecall         | trid                        | trustlook                      | type                           |
| us                            | varist                      | vba32                          | venuseye\_sandbox              |
| vhash                         | vipre                       | virit                          | virobot                        |
| virustotal\_androbox          | virustotal\_box\_of\_apples | virustotal\_cuckoofork         | virustotal\_droidy             |
| virustotal\_jsbox             | virustotal\_jujubox         | virustotal\_observer           | virustotal\_r2dbox             |
| vmray                         | webroot                     | whitearmor                     | xcitium                        |
| yandex                        | yomi\_hunter                | zenbox                         | zenbox                         |
| zenbox\_android               | zenbox\_linux               | zenbox\_macos                  | zillya                         |
| zonealarm                     | zoner                       | zscaler                        |                                |

# list-of-ip-modifiers

***

|                                       |                                   |                                       |                                    |
| ------------------------------------- | --------------------------------- | ------------------------------------- | ---------------------------------- |
| 0xsi\_f33d                            | abusix                            | acronis                               | adminuslabs                        |
| ailabs\_*monitorapp*                  | alienvault                        | alphamountain\_ai                     | alphasoc                           |
| antiy\_avl                            | arcsight\_threat\_intelligence    | asn                                   | aso                                |
| autoshun                              | axur                              | benkow\_cc                            | bfore\_ai\_precrime                |
| bitdefender                           | bkav                              | blueliv                               | certego                            |
| chainpatrol                           | chong\_lua\_dao                   | cins\_army                            | cluster25                          |
| cmc\_threat\_intelligence             | collection                        | comment                               | comment\_author                    |
| communicating\_files\_max\_detections | continent                         | country                               | crdf                               |
| criminal\_ip                          | csis\_security\_group             | cyan                                  | cyble                              |
| cyradar                               | desenmascara\_me                  | detected\_communicating\_files\_count | detected\_downloaded\_files\_count |
| detected\_referring\_files\_count     | detected\_urls\_count             | dns8                                  | domain\_resolutions\_count         |
| downloaded\_files\_max\_detections    | dr\_web                           | emergingthreats                       | emsisoft                           |
| engines                               | ermes                             | eset                                  | estsecurity                        |
| forcepoint\_threatseeker              | fortinet                          | g\_data                               | gcp\_abuse\_intelligence           |
| google\_safebrowsing                  | greensnow                         | greynoise                             | gridinsoft                         |
| gti\_score                            | gti\_severity                     | gti\_verdict                          | guardpot                           |
| have                                  | heimdal\_security                 | hunt\_io\_intelligence                | ip                                 |
| ipsum                                 | jarm                              | juniper\_networks                     | kaspersky                          |
| last\_modification\_date              | levelblue                         | lionic                                | lumu                               |
| malwared                              | malwarepatrol                     | malwares\_com\_url\_checker           | malwareurl                         |
| mimecast                              | netcraft                          | openphish                             | p                                  |
| path                                  | phishfort                         | phishing\_database                    | phishlabs                          |
| phishtank                             | prebytes                          | precisionsec                          | quick\_heal                        |
| quttera                               | referring\_files\_max\_detections | regional\_internet\_registry          | reputation                         |
| safetoopen                            | sansec\_ecomscan                  | scantitan                             | scumware\_org                      |
| seclookup                             | securebrain                       | securolytics                          | snort\_ip\_sample\_list            |
| socradar                              | sophos                            | spam404                               | ssl\_issuer                        |
| ssl\_not\_after                       | ssl\_not\_before                  | ssl\_serial                           | ssl\_subject                       |
| ssl\_thumbprint                       | stopforumspam                     | sucuri\_sitecheck                     | tag                                |
| threat\_actor                         | threathive                        | urlhaus                               | urlquery                           |
| urls\_max\_detections                 | viettel\_threat\_intelligence     | vipre                                 | viriback                           |
| vx\_vault                             | webroot                           | whois                                 | whois\_date                        |
| xcitium\_verdict\_cloud               | yandex\_safebrowsing              | zerocert                              | zerofox                            |

# list-of-domain-modifiers

***

|                               |                                       |                                    |                                       |
| ----------------------------- | ------------------------------------- | ---------------------------------- | ------------------------------------- |
| 0xsi\_f33d                    | a\_record                             | a\_ttl                             | aaaa\_record                          |
| aaaa\_ttl                     | abusix                                | acronis                            | adminuslabs                           |
| ailabs\_*monitorapp*          | alexa\_rank                           | alienvault                         | alphamountain\_ai                     |
| alphasoc                      | antiy\_avl                            | arcsight\_threat\_intelligence     | asn                                   |
| aso                           | autoshun                              | axur                               | benkow\_cc                            |
| bfore\_ai\_precrime           | bitdefender                           | bkav                               | blueliv                               |
| caa\_record                   | caa\_ttl                              | category                           | certego                               |
| chainpatrol                   | chong\_lua\_dao                       | cins\_army                         | cisco\_umbrella\_rank                 |
| cluster25                     | cmc\_threat\_intelligence             | cname\_record                      | cname\_ttl                            |
| collection                    | comment                               | comment\_author                    | communicating\_files\_max\_detections |
| crdf                          | creation\_date                        | criminal\_ip                       | csis\_security\_group                 |
| cyan                          | cyble                                 | cyradar                            | depth                                 |
| desenmascara\_me              | detected\_communicating\_files\_count | detected\_downloaded\_files\_count | detected\_referring\_files\_count     |
| detected\_urls\_count         | dname\_record                         | dname\_ttl                         | dns8                                  |
| domain                        | domain\_regex                         | downloaded\_files\_max\_detections | dr\_web                               |
| emergingthreats               | emsisoft                              | engines                            | ermes                                 |
| eset                          | estsecurity                           | forcepoint\_threatseeker           | fortinet                              |
| fuzzy\_domain                 | g\_data                               | gcp\_abuse\_intelligence           | google\_safebrowsing                  |
| greensnow                     | greynoise                             | gridinsoft                         | gti\_score                            |
| gti\_severity                 | gti\_verdict                          | guardpot                           | have                                  |
| heimdal\_security             | hunt\_io\_intelligence                | ipsum                              | jarm                                  |
| juniper\_networks             | kaspersky                             | last\_modification\_date           | last\_update\_date                    |
| levelblue                     | lionic                                | lumu                               | main\_icon\_dhash                     |
| main\_icon\_md5               | majestic\_rank                        | malwared                           | malwarepatrol                         |
| malwares\_com\_url\_checker   | malwareurl                            | mimecast                           | mx\_record                            |
| mx\_ttl                       | netcraft                              | ns\_record                         | ns\_ttl                               |
| openphish                     | p                                     | parent\_domain                     | path                                  |
| phishfort                     | phishing\_database                    | phishlabs                          | phishtank                             |
| popularity\_rank              | prebytes                              | precisionsec                       | quick\_heal                           |
| quttera                       | referring\_files\_max\_detections     | registrar                          | reputation                            |
| safetoopen                    | sansec\_ecomscan                      | scantitan                          | scumware\_org                         |
| seclookup                     | securebrain                           | securolytics                       | snort\_ip\_sample\_list               |
| soa\_record                   | soa\_ttl                              | socradar                           | sophos                                |
| spam404                       | ssl\_issuer                           | ssl\_not\_after                    | ssl\_not\_before                      |
| ssl\_serial                   | ssl\_subject                          | ssl\_thumbprint                    | statvoo\_rank                         |
| stopforumspam                 | sucuri\_sitecheck                     | tag                                | threat\_actor                         |
| threathive                    | tld                                   | ttl                                | txt\_record                           |
| txt\_ttl                      | urlhaus                               | urlquery                           | urls\_max\_detections                 |
| viettel\_threat\_intelligence | vipre                                 | viriback                           | vx\_vault                             |
| webroot                       | whois                                 | whois\_date                        | xcitium\_verdict\_cloud               |
| yandex\_safebrowsing          | zerocert                              | zerofox                            |                                       |

# list-of-url-modifiers

***

|                          |                                |                               |                          |
| ------------------------ | ------------------------------ | ----------------------------- | ------------------------ |
| 0xsi\_f33d               | abusix                         | acronis                       | adminuslabs              |
| ailabs\_*monitorapp*     | alienvault                     | alphamountain\_ai             | alphasoc                 |
| antiy\_avl               | arcsight\_threat\_intelligence | asn                           | aso                      |
| autoshun                 | axur                           | benkow\_cc                    | bfore\_ai\_precrime      |
| bitdefender              | bkav                           | blueliv                       | category                 |
| certego                  | chainpatrol                    | chong\_lua\_dao               | cins\_army               |
| cluster25                | cmc\_threat\_intelligence      | collection                    | comment                  |
| comment\_author          | contacted\_domain              | contacted\_ip                 | content                  |
| cookie                   | cookie\_value                  | crdf                          | criminal\_ip             |
| csis\_security\_group    | cyan                           | cyble                         | cyradar                  |
| desenmascara\_me         | dns8                           | dr\_web                       | emergingthreats          |
| emsisoft                 | engines                        | ermes                         | eset                     |
| estsecurity              | exact\_path                    | extension                     | first\_submitter         |
| forcepoint\_threatseeker | fortinet                       | fs                            | fuzzy\_hostname          |
| g\_data                  | gcp\_abuse\_intelligence       | google\_safebrowsing          | greensnow                |
| greynoise                | gridinsoft                     | gti\_score                    | gti\_severity            |
| gti\_verdict             | guardpot                       | have                          | header                   |
| header\_value            | heimdal\_security              | hostname                      | hunt\_io\_intelligence   |
| identified\_brand        | ip                             | ipsum                         | javascript\_variable     |
| juniper\_networks        | kaspersky                      | la                            | last\_modification\_date |
| levelblue                | lionic                         | ls                            | lumu                     |
| main\_brand              | main\_icon\_dhash              | main\_icon\_md5               | malwared                 |
| malwarepatrol            | malwares\_com\_url\_checker    | malwareurl                    | max\_url\_positives      |
| meta                     | mimecast                       | netcraft                      | openphish                |
| outgoing\_link           | p                              | parent\_domain                | password                 |
| phishfort                | phishing\_database             | phishlabs                     | phishtank                |
| port                     | prebytes                       | precisionsec                  | query\_field             |
| query\_value             | quick\_heal                    | quttera                       | redirecting\_url         |
| redirects\_to            | reputation                     | response\_code                | response\_positives      |
| response\_sha256         | response\_size                 | s                             | safetoopen               |
| sansec\_ecomscan         | scantitan                      | scheme                        | scumware\_org            |
| seclookup                | securebrain                    | securolytics                  | sha256                   |
| snort\_ip\_sample\_list  | socradar                       | sophos                        | spam404                  |
| stopforumspam            | submitter                      | sucuri\_sitecheck             | tag                      |
| targeted\_brand          | threat\_actor                  | threathive                    | title                    |
| tld                      | tracker                        | url                           | urlhaus                  |
| urlquery                 | username                       | viettel\_threat\_intelligence | vipre                    |
| viriback                 | vx\_vault                      | webroot                       | xcitium\_verdict\_cloud  |
| yandex\_safebrowsing     | zerocert                       | zerofox                       |                          |

# list-of-collection-modifiers

***

|                          |                           |                           |                           |
| ------------------------ | ------------------------- | ------------------------- | ------------------------- |
| available\_mitigation    | capability                | collection\_type          | comment                   |
| comment\_author          | creation\_date            | cvss\_2x\_base\_score     | cvss\_2x\_temporal\_score |
| cvss\_3x\_base\_score    | cvss\_3x\_temporal\_score | cvss\_4x\_score           | description               |
| detection                | domains                   | exploitation\_consequence | exploitation\_state       |
| exploitation\_vector     | files                     | first\_seen               | fs                        |
| have                     | ips                       | last\_modification\_date  | last\_seen                |
| ls                       | malware\_role             | merged\_actor             | motivation                |
| name                     | operating\_system         | origin                    | owner                     |
| priority                 | publisher                 | publisher\_priority       | publisher\_relevance      |
| publisher\_reliability   | references                | report\_type              | risk\_rating              |
| shared\_with\_me         | sigma\_rules              | software\_toolkit         | source\_region            |
| suspected\_threat\_actor | tag                       | targeted\_industry        | targeted\_industry\_group |
| targeted\_region         | threat\_actor             | threat\_actors            | threat\_category          |
| threat\_scape            | urls                      | vulnerability\_filter     | vulnerable\_cpe           |
| vulnerable\_product      | vulnerable\_vendor        |                           |                           |

# list-of-ioc-stream-modifiers

***

|      |              |        |              |
| ---- | ------------ | ------ | ------------ |
| date | entity\_type | origin | source\_type |

<br />

---

← [Intelligence / Web searching](../intelligence.md) · [up](../README.md) · [File search modifiers](file-search-modifiers.md) →

*Archived from <https://gtidocs.virustotal.com/docs/full-list-of-google-threat-intelligence-search-modifiers>.*
