---
title: "signature_info"
source: https://gtidocs.virustotal.com/reference/file-object-signature-info
slug: file-object-signature-info
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:00.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › signature_info

---

# signature_info

Information about signed PE and Mach-O files.

`signature_info` contains information about digital signature for Windows Executable and Mach-O files, extracted from the [Sigcheck](https://docs.microsoft.com/en-us/sysinternals/downloads/sigcheck) tool in Windows Executables and the Codesign command line utility in Mach-O files.

Fields returned for Windows Executables:

* `comments`: <*string*> from the file's version resource, if found.
* `copyright`: <*string*> from the file’s version resource, if found.
* `counter signers`: <*string*> string with counter signers Common Names. Names separated by `; ` characters.
* `counter signers details`: <*list of dictionaries*> details about each counter signer certificate.
  * `algorithm`: <*string*> the ones used for creating the key pairs.
  * `cert issuer`: <*string*> company that issued the certificate.
  * `name`: <*string*> certificate subject.
  * `serial number`: <*string*> in hex, byte by byte separated by spaces.
  * `status`: <*string*> it can say "Valid" or state the problem with the certificate if any (i.e. ""This certificate or one of the certificates in the certificate chain is not time valid.").
  * `thumbprint`: <*string*> hex representation of the certificate hash.
  * `valid from`:  <*string*> validity start date, in `%H:%M %p %m/%d/%Y` [format](http://strftime.org/).
  * `valid to`: <*string*> expiry date, in `%H:%M %p %m/%d/%Y` [format](http://strftime.org/).
  * `valid usage`: <*string*> indicates which situations the certificate is valid for (i.e. "Code Signing").
* `description`: <*string*> from the file's version resource, if found.
* `file version`: <*string*> from the file’s version resource, if found.
* `internal name`: <*string*> from the file's version resource, if found.
* `original name`: <*string*> from the file’s version resource, if found.
* `product`: <*string*> from the file's version resource, if found.
* `signing date`: <*string*> when the file was signed, in `%H:%M %p %m/%d/%Y` [format](http://strftime.org/).
* `x509`: <*list of dictionaries*> list of certificates found in the file. Every item in the list is an [SSL Certificate](../ssl-certificate-object.md) object, but returning just the following fields from the object:
  * `algorithm`: <*string*> the ones used for creating the key pairs.
  * `cert issuer`: <*string*> company that issued the certificate. Extracted from the certificate's `issuer.CN` field.
  * `name`: <*string*> certificate subject.
  * `serial number`: <*string*> in hex, byte by byte separated by spaces.
  * `thumbprint`: <*string*> hex representation of the certificate hash.
  * `valid from`: <*string*> validity start date, in `%H:%M %p %m/%d/%Y` [format](http://strftime.org/).
  * `valid to`: <*string*> expiry date, in `%H:%M %p %m/%d/%Y` [format](http://strftime.org/).
  * `valid usage`: <*string*> indicates which situations the certificate is valid for (i.e. "Code Signing"). Extracted from "extended key usage" certificate extension.

For Mach-O, DMG, IPA and ZIP files, fields from codesign tool are returned. They'll always be *string* keys and values. The most common ones are:

* `Authority`: <*string*> CA authority.
* `CDHash`: <*string*> code directory hash value. This code allows the system to verify that the contents of a binary have not changed since being code-signed.
* `CMSDigest`: <*string*> Cryptographic Message Syntax digest.
* `CMSDigestType`: <*string*> CMS digest type.
* `CandidateCDHash sha256`: <*string*>
* `CandidateCDHashFull sha256`: <*string*>
* `Format`: <*string*> file type.
* `Identifier`: <*string*> app id.
* `Info.plist`: <*string*> info.plist file.
* `Page size`: <*string*> certificate page size.
* `Signature size`: <*string*> how big the signature is in bytes.
* `TeamIdentifier`: <*string*> ID from the team who developed the executable.
* `Timestamp`: <*string*> date when the certificate was generated in `%b %d, %Y at %H:%M:%S %p` [format](http://strftime.org/).

Fields returned for both:

* `signers`: <*string*> string with signers Common Names. Separated by a `; ` character.
* `singers details`: <*list of dictionaries*> contains details about each signer certificate.
  * `algorithm`: <*string*> the ones used for creating the key pairs.
  * `cert issuer`: <*string*> company that issued the certificate.
  * `name`: <*string*> certificate subject.
  * `serial number`: <*string*> in hex, byte by byte separated by spaces.
  * `status`: <*string*> it can say "Valid" or state the problem with the certificate if any (i.e. ""This certificate or one of the certificates in the certificate chain is not time valid.").
  * `thumbprint`: <*string*> hex representation of the certificate hash.
  * `valid from`: <*string*> validity start date, in `%H:%M %p %m/%d/%Y` [format](http://strftime.org/).
  * `valid to`: <*string*> expiry date, in `%H:%M %p %m/%d/%Y` [format](http://strftime.org/).
  * `valid usage`: <*string*> indicates which situations the certificate is valid for (i.e. "Code Signing").
* `verified`: <*string*> status of the certificate. if can say "Signed", "Unsigned", or if there is any problem with the signature it will be noted here (i.e. "A certificate was explicitly revoked by its issuer.").

```json Signature information
{
  "data": {
		...
    "attributes" : {
      ...
      "signature_info": {
        "Authority": "<string>",
        "CDHash": "<string>",
        "CMSDigest": "<string>",
        "comments": "<string>",
        "copyright": "<string>",
        "counter signers": "<string>",
        "counter signers details": [
            {
                "algorithm": "<string>",
                "cert issuer": "<string>",
                "name": "<string>",
                "serial number": "<string>",
                "status": "<string>",
                "thumbprint": "<string>",
                "valid from": "<string:%H:%M %p %m/%d/%Y>",
                "valid to": "<string:%H:%M %p %m/%d/%Y>",
                "valid usage": "<string>"
            } ...
        ],
        "description": "<string>",
        "file version": "<string>",
        "Format": "<string">,
        "Identifier": "<string>",
        "internal name": "<string>",
        "original name": "<string>",
        "Page size": "<string>",
        "product": "<string>",
        "signers": "<string>",
        "signers details": [
              {
                  "algorithm": "<string>",
                  "cert issuer": "<string>",
                  "name": "<string>",
                  "serial number": "<string>",
                  "status": "<string>",
                  "thumbprint": "<string>",
                  "valid from": "<string:%H:%M %p %m/%d/%Y>",
                  "valid to": "<string:%H:%M %p %m/%d/%Y>",
                  "valid usage": "<string>"
              }, ...
        ],
        "signing date": "<string:%H:%M %p %m/%d/%Y>",
        "verified": "<string>",
        "x509": [
            {
                "algorithm": "<string>",
                "cert issuer": "<string>",
                "name": "<string>",
                "serial number": "<string>",
                "thumbprint": "<string>",
                "valid from": "<string:%H:%M %p %m/%d/%Y>",
                "valid to": "<string:%H:%M %p %m/%d/%Y>",
                "valid_usage": "<string>"
            }, ...
        ],
        "<string>": "<string>",..
    }
  }
}
```
```json Example (PE)
{
    "data": {
        "attributes": {
            "signature_info": {
                "copyright": "Copyright \u00a9 2011-2020 Blablabla Corporation",
                "counter signers": "Symantec Time Stamping Services Signer - G4; Symantec Time Stamping Services CA - G2; Thawte Timestamping CA",
                "counter signers details": [
                    {
                        "algorithm": "sha1RSA",
                        "cert issuer": "Symantec Time Stamping Services CA - G2",
                        "name": "Symantec Time Stamping Services Signer - G4",
                        "serial number": "BE BF F4 B8 B8 FE BF B5 6E B4 D8 BA 98 1B BA 50",
                        "status": "Valid",
                        "thumbprint": "65439529B65973E5192D5FF245E6757ADF5835E4",
                        "valid from": "12:00 AM 10/18/2012",
                        "valid to": "11:59 PM 12/29/2020",
                        "valid usage": "Timestamp Signing"
                    },
                    {
                        "algorithm": "sha1RSA",
                        "cert issuer": "Thawte Timestamping CA",
                        "name": "Symantec Time Stamping Services CA - G2",
                        "serial number": "EE E3 EB FB EC E6 4E E9 EA 4B EA E7 D4 E6 FC 3B",
                        "status": "Valid",
                        "thumbprint": "6C04453FFDD408B83407C09482FB4D15F45334B1",
                        "valid from": "12:00 AM 12/21/2012",
                        "valid to": "11:59 PM 12/30/2020",
                        "valid usage": "Timestamp Signing"
                    }
                ],
                "description": "blablabla",
                "file version": "1.0.10",
                "internal name": "blablabla",
                "original name": "blablabla.exe",
                "product": "blablabla",
                "signers": "blablabla Corporation; Symantec Class 3 SHA256 Code Signing CA - G2; VeriSign Universal Root Certification Authority",
                "signers details": [
                    {
                        "algorithm": "sha256RSA",
                        "cert issuer": "Symantec Class 3 SHA256 Code Signing CA - G2",
                        "name": "Blablabla Corporation",
                        "serial number": "A2 A7 A5 E9 A1 A5 21 AC A7 AF AC 49 AA EA 12 A5",
                        "status": "Valid",
                        "thumbprint": "0120353D101D3CF28483570A536BD13DAC3A43DD",
                        "valid from": "12:00 AM 07/09/2018",
                        "valid to": "11:59 PM 07/09/2021",
                        "valid usage": "Code Signing"
                    },
                    {
                        "algorithm": "sha256RSA",
                        "cert issuer": "VeriSign Universal Root Certification Authority",
                        "name": "Symantec Class 3 SHA256 Code Signing CA - G2",
                        "serial number": "FC FB F5 35 4A F7 DB F4 E7 F1 5F F1 69 FA FB A8",
                        "status": "Valid",
                        "thumbprint": "1392E4C7FF2529517E921077BB22664D287E270D",
                        "valid from": "12:00 AM 07/22/2014",
                        "valid to": "11:59 PM 07/21/2024",
                        "valid usage": "Code Signing"
                    },
                    {
                        "algorithm": "sha256RSA",
                        "cert issuer": "VeriSign Universal Root Certification Authority",
                        "name": "VeriSign Universal Root Certification Authority",
                        "serial number": "E0 1A E4 64 21 E3 13 E1 03 EE BB E4 E2 1A E5 1D",
                        "status": "Valid",
                        "thumbprint": "36796A35666772306D30A56B87360FA76BB76D54",
                        "valid from": "12:00 AM 04/02/2008",
                        "valid to": "11:59 PM 12/01/2037",
                        "valid usage": "Server Auth, Client Auth, Email Protection, Code Signing, Timestamp Signing"
                    }
                ],
                "signing date": "12:51 AM 6/23/2020",
                "verified": "Signed",
                "x509": [
                    {
                        "algorithm": "sha1RSA",
                        "cert issuer": "Thawte Timestamping CA",
                        "name": "Symantec Time Stamping Services CA - G2",
                        "serial number": "EE E3 EB FB EC E6 4E E9 EA 4B EA E7 D4 E6 FC 3B",
                        "thumbprint": "6C04453FFDD408B83407C09482FB4D15F45334B1",
                        "valid from": "2012-12-21 00:00:00",
                        "valid to": "2020-12-30 23:59:59",
                        "valid_usage": "Timestamp Signing"
                    },
                    {
                        "algorithm": "sha1RSA",
                        "cert issuer": "Symantec Time Stamping Services CA - G2",
                        "name": "Symantec Time Stamping Services Signer - G4",
                        "serial number": "BE BF F4 B8 B8 FE BF B5 6E B4 D8 BA 98 1B BA 50",
                        "thumbprint": "65439529B65973E5192D5FF245E6757ADF5835E4",
                        "valid from": "2012-10-18 00:00:00",
                        "valid to": "2020-12-29 23:59:59",
                        "valid_usage": "ff"
                    }
                ]
            }
        }
    }
}
```
```json Example (Mach-O)
{
    "data": {
        "attributes": {
            "signature_info": {
                "Authority": "Apple Root CA",
                "CDHash": "b3ff35553bd3983397213056b38b8335c23bd338",
                "CMSDigest": "b33f05553bd6983297216356bf838365c30bd233c99cc83ad199354ed333b99a",
                "CMSDigestType": "2",
                "CandidateCDHash sha256": "b3f405554bd6943297416056b48b8345c204d248",
                "CandidateCDHashFull sha256": "b3f405551b46983294216056b48b8365420bd234c99cc84ad199454ed4b3499a",
                "Format": "Mach-O thin (x86_64)",
                "Hash choices": "sha256",
                "Identifier": "blablabla",
                "Info.plist": "not bound",
                "Page size": "4096",
                "Runtime Version": "10.15.4",
                "Sealed Resources": "none",
                "Signature size": "4617",
                "TeamIdentifier": "38HJRH7QH9",
                "Timestamp": "Jun 23, 2020 at 2:21:00 AM",
                "signers": "Apple Inc.; Apple Inc.; Apple Inc.",
                "signers details": [
                    {
                        "algorithm": "sha1WithRSAEncryption",
                        "cert issuer": "Apple Inc.",
                        "name": "Apple Inc.",
                        "serial number": "2",
                        "status": "Valid",
                        "thumbprint": "611E5B662C593A08FF58D14AE22452D198DF6C60",
                        "valid from": "09:40 PM 04/25/2006",
                        "valid to": "09:40 PM 02/09/2035",
                        "valid usage": ""
                    },
                    {
                        "algorithm": "sha1WithRSAEncryption",
                        "cert issuer": "Apple Inc.",
                        "name": "Apple Inc.",
                        "serial number": "1D EB CC 43 96 DA 01",
                        "status": "Valid",
                        "thumbprint": "FF6797793A3CD798DC5B2ABEF56F73EDC9F83A64",
                        "valid from": "09:48 PM 02/07/2013",
                        "valid to": "09:48 PM 02/07/2023",
                        "valid usage": ""
                    },
                    {
                        "algorithm": "sha256WithRSAEncryption",
                        "cert issuer": "Apple Inc.",
                        "name": "Apple Inc.",
                        "serial number": "4C A8 1F 77 D5 E3 3F",
                        "status": "NotTrusted",
                        "thumbprint": "B93BDAAAF1A8846B34BA32332635CB2B84853DA8",
                        "valid from": "07:10 AM 01/07/2016",
                        "valid to": "12:00 AM 02/07/2023",
                        "valid usage": ""
                    }
                ],
                "verified": "MissingPlist"
            }
        }
    }
}
```

---

← [pe_info](file-object-pe-info.md) · [up](../README.md) · [androguard](file-object-androguard.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-signature-info>.*
