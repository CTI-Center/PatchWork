---
title: "Reference"
source: https://gtidocs.virustotal.com/docs/hunting-reference
slug: hunting-reference
section: guides
group: "IOC Investigation"
updatedAt: 2025-09-27T09:17:34.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [IOC Investigation](../README.md) › [Livehunt](../livehunt-guide.md) › Reference

---

# reference

# livehunt-*vt*-module-reference

This reference provides a detailed list of the various data types that can be matched against when using attributes within the vt module.

* [HTTP Methods](#http-methods)
* [Network Protocols](#network-protocols)
* [Behaviour traits](#behaviour-traits)
* [Behaviour verdicts](#behaviour-verdicts)
* [File types](#file-types)
* [Google TI assessment severity types](#google-ti-assessment-severity-types)
* [Google TI assessment verdicts](#google-ti-assessment-verdicts)

## http-methods

|                        |
| ---------------------- |
| vt.Http.Method.GET     |
| vt.Http.Method.HEAD    |
| vt.Http.Method.PATCH   |
| vt.Http.Method.POST    |
| vt.Http.Method.PUT     |
| vt.Http.Method.DELETE  |
| vt.Http.Method.TRACE   |
| vt.Http.Method.OPTIONS |
| vt.Http.Method.CONNECT |

## network-protocols

|                      |
| -------------------- |
| vt.Net.Protocol.ICMP |
| vt.Net.Protocol.IGMP |
| vt.Net.Protocol.TCP  |
| vt.Net.Protocol.UDP  |
| vt.Net.Protocol.ESP  |
| vt.Net.Protocol.AH   |
| vt.Net.Protocol.L2TP |
| vt.Net.Protoco.SCTP  |

## behaviour-traits

|                                                |
| ---------------------------------------------- |
| vt.BehaviourTrait.BIG\_UPSTREAM                |
| vt.BehaviourTrait.CHECKS\_BIOS                 |
| vt.BehaviourTrait.CHECKS\_CPU\_NAME            |
| vt.BehaviourTrait.CHECKS\_DISK\_SPACE          |
| vt.BehaviourTrait.CHECKS\_GPS                  |
| vt.BehaviourTrait.CHECKS\_HOSTNAME             |
| vt.BehaviourTrait.CHECKS\_MEMORY\_AVAILABLE    |
| vt.BehaviourTrait.CHECKS\_NETWORK\_ADAPTERS    |
| vt.BehaviourTrait.CHECKS\_PCI\_BUS             |
| vt.BehaviourTrait.CHECKS\_USB\_BUS             |
| vt.BehaviourTrait.CLIPBOARD                    |
| vt.BehaviourTrait.CRYPTO                       |
| vt.BehaviourTrait.DECRYPTS\_EXE                |
| vt.BehaviourTrait.DETECT\_DEBUG\_ENVIRONMENT   |
| vt.BehaviourTrait.DIRECT\_CPU\_CLOCK\_ACCESS   |
| vt.BehaviourTrait.EXECUTES\_DROPPED\_FILE      |
| vt.BehaviourTrait.FTP\_COMMUNICATION           |
| vt.BehaviourTrait.HOSTS\_MODIFIER              |
| vt.BehaviourTrait.INSTALLS\_BROWSER\_EXTENSION |
| vt.BehaviourTrait.IRC\_COMMUNICATION           |
| vt.BehaviourTrait.LONG\_SLEEPS                 |
| vt.BehaviourTrait.MACRO\_ANTI\_ANALYSIS        |
| vt.BehaviourTrait.MACRO\_COPY\_FILE            |
| vt.BehaviourTrait.MACRO\_CREATE\_DIR           |
| vt.BehaviourTrait.MACRO\_CREATE\_FILE          |
| vt.BehaviourTrait.MACRO\_CREATE\_OLE           |
| vt.BehaviourTrait.MACRO\_DOWNLOAD\_URL         |
| vt.BehaviourTrait.MACRO\_ENUM\_WINDOWS         |
| vt.BehaviourTrait.MACRO\_ENVIRON               |
| vt.BehaviourTrait.MACRO\_HANDLE\_FILE          |
| vt.BehaviourTrait.MACRO\_HIDE\_APP             |
| vt.BehaviourTrait.MACRO\_OPEN\_FILE            |
| vt.BehaviourTrait.MACRO\_POWERSHELL            |
| vt.BehaviourTrait.MACRO\_REGISTRY              |
| vt.BehaviourTrait.MACRO\_RUN\_DLL              |
| vt.BehaviourTrait.MACRO\_RUN\_FILE             |
| vt.BehaviourTrait.MACRO\_SAVE\_WORKBOOK        |
| vt.BehaviourTrait.MACRO\_SEND\_KEYS            |
| vt.BehaviourTrait.MACRO\_WRITE\_FILE           |
| vt.BehaviourTrait.MYSQL\_COMMUNICATION         |
| vt.BehaviourTrait.OBFUSCATED                   |
| vt.BehaviourTrait.PASSWORD\_DIALOG             |
| vt.BehaviourTrait.PERSISTENCE                  |
| vt.BehaviourTrait.REFLECTION                   |
| vt.BehaviourTrait.RUNTIME\_MODULES             |
| vt.BehaviourTrait.SELF\_DELETE                 |
| vt.BehaviourTrait.SENDS\_SMS                   |
| vt.BehaviourTrait.SMTP\_COMMUNICATION          |
| vt.BehaviourTrait.SSH\_COMMUNICATION           |
| vt.BehaviourTrait.SUDO                         |
| vt.BehaviourTrait.SUSPICIOUS\_DNS              |
| vt.BehaviourTrait.SUSPICIOUS\_UDP              |
| vt.BehaviourTrait.TELEPHONY                    |
| vt.BehaviourTrait.TELNET\_COMMUNICATION        |
| vt.BehaviourTrait.TUNNELING                    |

## behaviour-verdicts

|                                      |
| ------------------------------------ |
| vt.BehaviourVerdict.ADWARE           |
| vt.BehaviourVerdict.BANKER           |
| vt.BehaviourVerdict.CLEAN            |
| vt.BehaviourVerdict.EVADER           |
| vt.BehaviourVerdict.EXPLOIT          |
| vt.BehaviourVerdict.GREYWARE         |
| vt.BehaviourVerdict.MALWARE          |
| vt.BehaviourVerdict.PHISHING         |
| vt.BehaviourVerdict.RANSOM           |
| vt.BehaviourVerdict.RAT              |
| vt.BehaviourVerdict.SPREADER         |
| vt.BehaviourVerdict.TROJAN           |
| vt.BehaviourVerdict.UNKNOWN\_VERDICT |

[Back to top](#reference)

## file-types

| **Type**                   | **Type tags**                                            |
| -------------------------- | -------------------------------------------------------- |
| vt.FileType.ACE            | compressed ace                                           |
| vt.FileType.ANDROID        | executable mobile android apk                            |
| vt.FileType.APPLE          | apple apple-gen                                          |
| vt.FileType.APPLE\_PLIST   | apple appleplist                                         |
| vt.FileType.APPLEDOUBLE    | apple appledouble                                        |
| vt.FileType.APPLESINGLE    | apple applesingle                                        |
| vt.FileType.ARC            | compressed arc                                           |
| vt.FileType.ARJ            | compressed arj                                           |
| vt.FileType.ASD            | compressed asd                                           |
| vt.FileType.ASF            | multimedia video asf                                     |
| vt.FileType.AVI            | multimedia video avi                                     |
| vt.FileType.AWK            | source awk                                               |
| vt.FileType.BMP            | multimedia image bmp                                     |
| vt.FileType.BZIP           | compressed bzip                                          |
| vt.FileType.C              | source c                                                 |
| vt.FileType.CAB            | compressed cab                                           |
| vt.FileType.CAP            | internet cap pcap                                        |
| vt.FileType.CHM            | help chm                                                 |
| vt.FileType.COFF           | executable coff                                          |
| vt.FileType.COOKIE         | internet iecookie                                        |
| vt.FileType.CPP            | source cpp                                               |
| vt.FileType.CRX            | crx chrome extension browser                             |
| vt.FileType.DEB            | executable linux deb                                     |
| vt.FileType.DIB            | multimedia image dib                                     |
| vt.FileType.DIVX           | multimedia video divx                                    |
| vt.FileType.DMG            | executable mac dmg                                       |
| vt.FileType.DOC            | document msoffice text word doc                          |
| vt.FileType.DOCX           | document msoffice text word docx                         |
| vt.FileType.DOS\_COM       | executable dos com                                       |
| vt.FileType.DOS\_EXE       | executable dos mz                                        |
| vt.FileType.DYALOG         | source dyalog                                            |
| vt.FileType.DZIP           | compressed dzip                                          |
| vt.FileType.EBOOK          | document ebook epub                                      |
| vt.FileType.ELF            | executable linux elf                                     |
| vt.FileType.EMAIL          | internet email                                           |
| vt.FileType.EMF            | multimedia image emf                                     |
| vt.FileType.EOT            | font opentype eof                                        |
| vt.FileType.FLAC           | multimedia audio flac                                    |
| vt.FileType.FLC            | multimedia animation flc                                 |
| vt.FileType.FLI            | multimedia animation fli                                 |
| vt.FileType.FLV            | multimedia video flv                                     |
| vt.FileType.FORTRAN        | source fortran                                           |
| vt.FileType.FPX            | multimedia image fpx                                     |
| vt.FileType.GIF            | multimedia image gif                                     |
| vt.FileType.GIMP           | multimedia image gimp                                    |
| vt.FileType.GUL            | document samsungdoc text gul                             |
| vt.FileType.GZIP           | compressed gzip                                          |
| vt.FileType.HTML           | internet html                                            |
| vt.FileType.HWP            | document hangul text hwp                                 |
| vt.FileType.ICO            | multimedia image ico                                     |
| vt.FileType.IN\_DESIGN     | multimedia image indesign                                |
| vt.FileType.IPHONE         | executable mobile iphone ios                             |
| vt.FileType.ISOIMAGE       | compressed isoimage                                      |
| vt.FileType.JAR            | compressed jar                                           |
| vt.FileType.JAVA           | source java                                              |
| vt.FileType.JAVA\_BYTECODE | executable java-bytecode class                           |
| vt.FileType.JAVASCRIPT     | source javascript                                        |
| vt.FileType.JNG            | multimedia image jng                                     |
| vt.FileType.JPEG           | multimedia image jpeg jpg                                |
| vt.FileType.KGB            | compressed kgb                                           |
| vt.FileType.LATEX          | document latex                                           |
| vt.FileType.LINUX          | linux                                                    |
| vt.FileType.LINUX\_KERNEL  | linux                                                    |
| vt.FileType.LNK            | windows lnk                                              |
| vt.FileType.MACH\_O        | executable mac macho                                     |
| vt.FileType.MACINTOSH      | apple macintosh mac macintosh-gen                        |
| vt.FileType.MACINTOSH\_HFS | apple macintosh mac machfs                               |
| vt.FileType.MACINTOSH\_LIB | apple mac maclib                                         |
| vt.FileType.MIDI           | multimedia audio midi                                    |
| vt.FileType.MOV            | multimedia video mov                                     |
| vt.FileType.MP3            | multimedia audio mp3                                     |
| vt.FileType.MP4            | multimedia audio mp4                                     |
| vt.FileType.MPEG           | multimedia video mpeg                                    |
| vt.FileType.MSCOMPRESS     | compressed mscompress                                    |
| vt.FileType.MSI            | installer windows msi                                    |
| vt.FileType.NE\_DLL        | executable windows win16 ne nedll                        |
| vt.FileType.NE\_EXE        | executable windows win16 ne neexe                        |
| vt.FileType.ODF            | document openoffice math odf                             |
| vt.FileType.ODG            | document openoffice draw odg                             |
| vt.FileType.ODP            | document openoffice presentation odp                     |
| vt.FileType.ODS            | document openoffice spreadsheet ods                      |
| vt.FileType.ODT            | document openoffice text odt                             |
| vt.FileType.OGG            | multimedia video ogg                                     |
| vt.FileType.OUTLOOK        | internet email outlook                                   |
| vt.FileType.PALMOS         | executable mobile palmos                                 |
| vt.FileType.PASCAL         | source pascal                                            |
| vt.FileType.PDF            | document pdf                                             |
| vt.FileType.PE\_DLL        | executable windows win32 pe pedll                        |
| vt.FileType.PE\_EXE        | executable windows win32 pe peexe                        |
| vt.FileType.PERL           | source perl                                              |
| vt.FileType.PHP            | source php                                               |
| vt.FileType.PKG            | executable mac pkg                                       |
| vt.FileType.PNG            | multimedia image png                                     |
| vt.FileType.PPSX           | document msoffice presentation powerpoint slideshow ppsx |
| vt.FileType.PPT            | document msoffice presentation powerpoint ppt            |
| vt.FileType.PPTX           | document msoffice presentation powerpoint pptx           |
| vt.FileType.PS             | document ps postscript                                   |
| vt.FileType.PSD            | multimedia image photoshop psd                           |
| vt.FileType.PYTHON         | source python                                            |
| vt.FileType.QUICKTIME      | multimedia video quicktime qt                            |
| vt.FileType.RAR            | compressed rar                                           |
| vt.FileType.RM             | multimedia video realmedia rm                            |
| vt.FileType.ROM            | rom bios firmware                                        |
| vt.FileType.RPM            | linux rpm                                                |
| vt.FileType.RTF            | document msoffice text word rtf                          |
| vt.FileType.RUBY           | source ruby                                              |
| vt.FileType.RZIP           | compressed rzip                                          |
| vt.FileType.SCRIPT         | script                                                   |
| vt.FileType.SEVENZIP       | compressed 7zip                                          |
| vt.FileType.SHELLSCRIPT    | script shell                                             |
| vt.FileType.SVG            | multimedia image svg                                     |
| vt.FileType.SWF            | internet flash swf                                       |
| vt.FileType.SYMBIAN        | executable mobile symbian                                |
| vt.FileType.T3GP           | multimedia video 3gp                                     |
| vt.FileType.TAR            | compressed tar                                           |
| vt.FileType.TARGA          | multimedia image targa                                   |
| vt.FileType.TEXT           | text                                                     |
| vt.FileType.TIFF           | multimedia image tiff                                    |
| vt.FileType.TORRENT        | link internet bittorrent                                 |
| vt.FileType.TTF            | font truetype ttf                                        |
| vt.FileType.WAV            | multimedia audio wav                                     |
| vt.FileType.WINCE          | executable mobile wince                                  |
| vt.FileType.WMA            | multimedia audio wma                                     |
| vt.FileType.WMV            | multimedia video wmv                                     |
| vt.FileType.WOFF           | font openfont woff                                       |
| vt.FileType.XLS            | document msoffice spreadsheet excel xls                  |
| vt.FileType.XLSX           | document msoffice spreadsheet excel xlsx                 |
| vt.FileType.XML            | internet xml                                             |
| vt.FileType.XPI            | browser extension firefox xpi                            |
| vt.FileType.XWD            | multimedia image xwd                                     |
| vt.FileType.ZIP            | compressed zip                                           |
| vt.FileType.ZLIB           | compressed zlib                                          |

[Back to top](#reference)

## google-ti-assessment-severity-types

|                                 |
| ------------------------------- |
| vt.GtiSeverity.SEVERITY\_NONE   |
| vt.GtiSeverity.SEVERITY\_LOW    |
| vt.GtiSeverity.SEVERITY\_MEDIUM |
| vt.GtiSeverity.SEVERITY\_HIGH   |

[Back to top](#reference)

## google-ti-assessment-verdicts

|                                   |
| --------------------------------- |
| vt.GtiVerdict.VERDICT\_BENIGN     |
| vt.GtiVerdict.VERDICT\_UNDETECTED |
| vt.GtiVerdict.VERDICT\_SUSPICIOUS |
| vt.GtiVerdict.VERDICT\_MALICIOUS  |

[Back to top](#reference)

---

← [Network hunting examples](nethunt-examples.md) · [up](../README.md) · [Legacy variables](hunting-legacy-variables.md) →

*Archived from <https://gtidocs.virustotal.com/docs/hunting-reference>.*
