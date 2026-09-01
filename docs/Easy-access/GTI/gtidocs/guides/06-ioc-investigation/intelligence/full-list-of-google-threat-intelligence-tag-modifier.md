---
title: "Full list of Google Threat Intelligence tag modifier"
source: https://gtidocs.virustotal.com/docs/full-list-of-google-threat-intelligence-tag-modifier
slug: full-list-of-google-threat-intelligence-tag-modifier
section: guides
group: "IOC Investigation"
updatedAt: 2025-10-30T10:17:57.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [IOC Investigation](../README.md) › [Intelligence / Web searching](../intelligence.md) › Full list of Google Threat Intelligence tag modifier

---

# full-list-of-google-threat-intelligence-tag-modifier

One of the search modifiers available in [Google Threat Intelligence](file-search-modifiers.md) is "tag". This modifier will search for files tagged with the literal provided. Google Threat Intelligence adds tags to all files processed based on hundreds of factors depending on the type of file, information extracted, behaviour, etc.

You can find the description and examples of the most common tags at the [File search modifiers article](file-search-modifiers.md).

[List of Domains tags.](#list-of-domains-tags)

[List of Files tags.](#list-of-files-tags)

[List of IPs tags.](#list-of-ips-tags)

[List of URLs tags.](#list-of-urls-tags)

[List of deprecated tags.](#list-of-deprecated-tags)

# list-of-domains-tags

***

|                 |          |              |             |
| --------------- | -------- | ------------ | ----------- |
| alternative-dns | dga      | dynamic-dns  | hex         |
| non-ascii       | nxdomain | potential-c2 | self-signed |

# list-of-files-tags

***

|                                    |                                |                              |                             |
| ---------------------------------- | ------------------------------ | ---------------------------- | --------------------------- |
| 32bits                             | 32lite                         | 64bits                       | abused-exe-pattern          |
| acidcrypt                          | acprotect                      | acroform                     | activemark                  |
| aes-encoded                        | ahpack                         | ainexe                       | alexprotector               |
| alloy                              | alternative-dns                | aluwain                      | anorganix                   |
| anskya                             | anti-analysis                  | anywhere                     | apatch                      |
| apex                               | apfs                           | apk                          | arm                         |
| armadillo                          | arsc                           | as2                          | as3                         |
| aspack                             | asprotect                      | assembly                     | attachment                  |
| auto-close                         | auto-create                    | auto-modify                  | auto-open                   |
| autoaction                         | axml                           | bambam                       | base64-embedded             |
| base64-string                      | beria                          | bero                         | blade                       |
| blob                               | bobsoft                        | calls-wmi                    | capabilities                |
| cdcops                             | cexe                           | checks-bios                  | checks-cpu-name             |
| checks-disk-space                  | checks-gps                     | checks-hostname              | checks-memory-available     |
| checks-network-adapters            | checks-usb-bus                 | checks-user-input            | checks\_gps                 |
| cicompress                         | cipherwall                     | clipboard                    | code injection              |
| code-injection                     | codelock                       | codesafe                     | compack                     |
| contains-apk                       | contains-deb                   | contains-dmg                 | contains-drv                |
| contains-elf                       | contains-embedded-js           | contains-macho               | contains-msi                |
| contains-pe                        | contains-rom                   | contains-zip                 | copy-file                   |
| coredump                           | corrupt                        | corrupted                    | create-dir                  |
| create-file                        | create-ole                     | createinstall                | crinkler                    |
| crunch                             | crypkey                        | crypt                        | crypto                      |
| cryptz                             | crypwrap                       | cydia                        | dbpe                        |
| ddem                               | dell-pfs                       | depack                       | detect-debug-environment    |
| detect\_debug\_environment         | dex                            | diminisher                   | dingboy                     |
| diprotector                        | direct-cpu-clock-access        | djoin                        | domain-pattern              |
| dos-stub                           | download                       | dropper                      | dshield                     |
| dxpack                             | dyn-calls                      | dyn-class                    | efi                         |
| email-pattern                      | email-spam                     | embedpe                      | empty                       |
| encrypted                          | encryptpe                      | enigma                       | enum-windows                |
| environ                            | escargot                       | eval-function                | exe-embedded                |
| exe-pattern                        | exe32pack                      | execryptor                   | executes-dropped-file       |
| exeguarder                         | exejoiner                      | exelocker                    | exepack                     |
| exepacker                          | exeshield                      | exesmasher                   | exestealth                  |
| exploit                            | exploit-kit                    | expressor                    | ext-interface               |
| ext-prg                            | ezip                           | faulty                       | feokpt                      |
| file-embedded                      | fixuppak                       | flash-embedded               | fres                        |
| freshbind                          | frusion                        | fscommand                    | fsg                         |
| ftp                                | ftp-communication              | fucknjoy                     | fusion                      |
| gamehouse                          | gleam                          | goats                        | goodware                    |
| gpt                                | hackstop                       | handle-file                  | hash-collision              |
| hasp                               | heap-spray                     | hfs                          | hide-app                    |
| hiding-window                      | high-entropy                   | honeypot                     | hosts-modifier              |
| html-control                       | idle                           | iframe                       | impostor                    |
| installshield                      | installstub                    | intel-me                     | invalid-rich-pe-checksum    |
| invalid-rich-pe-duplicated-entries | invalid-rich-pe-linker-version | invalid-rich-pe-modified-iat | invalid-signature           |
| invalid-xref                       | ios                            | ipbprotect                   | ipv4-pattern                |
| irc                                | irc-communication              | jdpack                       | js-embedded                 |
| jspack                             | kbys                           | kgcrypt                      | kkrunchy                    |
| known-distributor                  | krunchy                        | krypton                      | kryptor                     |
| lamecrypt                          | large-file                     | launch-action                | lcc                         |
| legit                              | lib                            | license                      | loadbytes                   |
| lockless                           | lolbin                         | long-base64                  | long-command-line-arguments |
| long-hex                           | long-sleeps                    | ltc                          | lzexe                       |
| lzma                               | mac-app                        | mac-cmd-embedder             | mac-publisher               |
| macro-anti-analysis                | macro-create-ole               | macro-powershell             | macro-run-file              |
| macros                             | malformed                      | malware                      | matcho                      |
| meta-redirect                      | mew                            | microjoiner                  | mmbuilder                   |
| mobile-substrate                   | molebox                        | morphine                     | multi-arch                  |
| mysql                              | mysql-communication            | nakedpack                    | native                      |
| neolite                            | nfo                            | niceprotect                  | noodlecrypt                 |
| northstar                          | npack                          | nsis                         | nspack                      |
| nsrl                               | ntkrnl                         | nullsoft                     | nxdomain                    |
| obfuscated                         | obsidium                       | odex                         | ole-autolink                |
| ole-control                        | ole-embedded                   | ole-link                     | open-file                   |
| opendir                            | orien                          | os-checking                  | overlay                     |
| pack200                            | packman                        | packmaster                   | password-dialog             |
| password-input                     | passwordprotector              | payload                      | pcguard                     |
| pcshrinker                         | pe-armor                       | pearmor                      | pebundle                    |
| pecompact                          | pecrc32                        | pecrypt32                    | pelock                      |
| pemangle                           | penightmare                    | peninja                      | pepack                      |
| peprotect                          | persistence                    | peshield                     | peshit                      |
| pespin                             | petite                         | pex                          | pirit                       |
| pklite                             | pklite32                       | polyene                      | postinst                    |
| postrm                             | preinst                        | prerm                        | punisher                    |
| quarantined                        | radpack                        | rar-embedded                 | rcryptor                    |
| reflection                         | registry                       | relocatable                  | repeated-clock-access       |
| revoked-cert                       | rlpack                         | run-dll                      | run-file                    |
| runtime-modules                    | save-workbook                  | sdprotect                    | sdprotector                 |
| self-delete                        | send-keys                      | sends-sms                    | service-scan                |
| sets-process-name                  | shared-lib                     | shellcode                    | signed                      |
| simplepack                         | smtp                           | smtp-communication           | softdefender                |
| software-collection                | spreader                       | ssh                          | ssh-communication           |
| starforce                          | startup-folder                 | stealth                      | stones                      |
| sudo                               | suspicious-dns                 | suspicious-eip               | suspicious-udp              |
| svkprotector                       | system-library                 | tar-bundle                   | telephony                   |
| telnet                             | telnet-communication           | telock                       | themida                     |
| thinstall                          | tlpack                         | trojan                       | trusted                     |
| tunneling                          | uefi                           | upack                        | upx                         |
| url-pattern                        | usb-autorun                    | vcasm                        | via-tor                     |
| virogen                            | webcops                        | winrar                       | winzip                      |
| wise                               | worm                           | write-file                   | wwpack                      |
| xcr                                | xorcrypt                       | xws                          | yoda                        |
| yodaprot                           | yodaprotect                    | zcode                        | zero-filled                 |
| zip-embedded                       | zipped                         |                              |                             |

# list-of-ips-tags

***

|            |             |             |                |
| ---------- | ----------- | ----------- | -------------- |
| link-local | loopback    | multicast   | private        |
| proxy      | reserved    | self-signed | suspicious-udp |
| tor        | unspecified | vpn         |                |

# list-of-urls-tags

***

|                     |                     |                |                    |
| ------------------- | ------------------- | -------------- | ------------------ |
| 32-bit              | adware              | agenttesla     | andromeda          |
| apk                 | arm                 | avemaria       | azorult            |
| b-tds               | base64-embedded     | bashlite       | bat                |
| bazaloader          | bazarcall           | bazarloader    | blocked-waf        |
| cerber              | clipboard-readwrite | cloned-website | coinminer          |
| contains-apk        | contains-dmg        | contains-msi   | contains-pe        |
| contains-zip        | crypmod             | ddos bot       | dll                |
| doc                 | dom-modification    | downloader     | downloads-apk      |
| downloads-dmg       | downloads-doc       | downloads-elf  | downloads-pdf      |
| downloads-pe        | downloads-zip       | dridex         | elf                |
| emotet              | encoded             | encrypted      | epoch1             |
| epoch2              | exe                 | exploit        | external-resources |
| finderbot           | flubot              | formbook       | gafgyt             |
| geofenced           | glupteba            | gozi           | guloader           |
| hajime              | hancitor            | heodo          | html               |
| icedid              | iframes             | ip             | isfb               |
| ita                 | kovter              | loki           | lokibot            |
| maldoc              | malware             | meta-redirect  | mikoponi           |
| mips                | mirai               | mozi           | multiple-redirects |
| nanocore            | neshta              | netwire        | njrat              |
| non-ascii           | ns-port             | opendir        | password-input     |
| phishing            | phorpiex            | proxy-auth     | pylocky            |
| qakbot              | qbot                | qr-code        | quakbot            |
| raccoon             | rat                 | redlinestealer | remcos             |
| remcosrat           | riskware            | script         | script-load        |
| shellscript         | silentbuilder       | sload          | snakekeylogger     |
| third-party-cookies | tr                  | trackers       | trickbot           |
| ursnif              | webshell            | xls            | xlsb               |
| zenpak              | zip                 | zloader        | zusy               |

# list-of-deprecated-tags

***

|                              |                                    |                                |
| ---------------------------- | ---------------------------------- | ------------------------------ |
| invalid-rich-pe-checksum     | invalid-rich-pe-duplicated-entries | invalid-rich-pe-linker-version |
| invalid-rich-pe-modified-iat | nsrl                               | trusted                        |

---

← [Batch file downloads](batch-file-downloads.md) · [up](../README.md) · [Full list of Google Threat Intelligence behaviour_tags modifier](full-list-of-google-threat-intelligence-behaviour_tags-modifier.md) →

*Archived from <https://gtidocs.virustotal.com/docs/full-list-of-google-threat-intelligence-tag-modifier>.*
