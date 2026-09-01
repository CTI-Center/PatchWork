---
title: "SSL Certificate"
source: https://gtidocs.virustotal.com/reference/ssl-certificate-object
slug: ssl-certificate-object
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T02:15:20.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › SSL Certificate

---

# ssl-certificate

SSL certificates information.

SSL certificates associated with domains and IPs. They contain the following information:

* `cert_signature`: dictionary containing certificate's signature and algorithm.
  * `signature`: signature hexdump.
  * `signature_algorithm`: used algorithm (i.e. "sha256RSA").
* `extensions`: dictionary containing all certificate's extensions. Subfields may vary but some common extensions are:
  * `CA`: whether the subject acts as a CA or not.
  * `subject_key_identifier`: identifies the public key being certified.
  * `authority_key_identifier`: identifies the public key to be used to verify the signature on this certificate or CRL.
    * `keyid`: key hexdump.
    * `serial_number`: serial number hexdump.
  * `key_usage`: indicates the purpose for which the certified public key is used.
  * `ca_information_access`: authority information access locations are URLs that are added to a certificate in its authority information access extension.
  * `crl_distribution_points`: identifies the CRL distribution points to which a certificate user should refer to ascertain if the certificate has been revoked.
  * `extended_key_usage`: indicates one or more purposes for which the certified public key may be used, in addition to or in place of the basic purposes indicated in the key usage extension field.
  * `subject_alternative_name`: contains one or more alternative names, using any of a variety of name forms, for the entity that is bound by the CA to the certified public key.
  * `certificate_policies`: different certificate policies will relate to different applications which may use the certified key.
  * `netscape_cert_comment`: used to include free-form text comments inside certificates.
  * `cert_template_name_dc`: BMP data value "DomainController" see MS Q291010.
  * `netscape_certificate`:  identify whether the certificate subject is an SSL client, an SSL server, or a CA.
  * `pe_logotype`: whether the certificate includes a logotype.
  * `old_authority_key_identifier`: whether the certificate has an old authority key identifier extension.
* `first_seen_date`: date the certificate was first retrieved by Google Threat Intelligence.
* `issuer`: dictionary containing the certificate's issuer data.
  * `C`: CountryName.
  * `CN`: CommonName.
  * `L`: Locality.
  * `O`: Organization.
  * `OU`: OrganizationalUnit.
  * `ST`: StateOrProvinceName.
* `public_key`: subject public key info.
  * `algorithm`: any of "RSA", "DSA" or "EC". Indicates the algorithm used to generate the certificate. Depending on this field, one of the following fields is added.
  * `rsa`: RSA public key information.
    * `key_size`: key size.
    * `modulus`: key modulus hexdump.
    * `exponent`: key exponent hexdump.
  * `dsa`: DSA public key information.
    * `p`: p component hexdump.
    * `q`: q component hexdump.
    * `g`: g component hexdump.
    * `pub`: public key hexdump.
  * `ec`: EC public key information.
    * `oid`: curve name.
    * `pub`: public key hexdump.
* `serial_number`: certificate's serial number hexdump.
* `signature_algorithm`: used algorithm for the signature (i.e. "sha1RSA").
* `size`: certificate content length.
* `subject`: dictionary containing the certificate's subject data.
  * `C`: CountryName.
  * `CN`: CommonName.
  * `L`: Locality.
  * `O`: Organization.
  * `OU`: OrganizationalUnit.
  * `ST`: StateOrProvinceName.
* `thumbprint`: certificate's content SHA1 hash.
* `thumbprint_sha256`: certificate's content SHA256 hash.
* `validity`: defines certificate's validity period.
  * `not_after`: expiry date in `%Y-%m-%d %H:%M:%S`  [format](http://strftime.org/).
  * `not_before`: issue date in `%Y-%m-%d %H:%M:%S`  [format](http://strftime.org/).
* `version`: certificate version (typically "V1", "V2" or "V3").

```json SSL Certificate object
{
  "type": "ssl_cert",
  "id": <string>,
  "attributes": {
        "cert_signature": {
          	"signature": "<string>",
            "signature_algorithm": "<string>"
        },
        "extensions": {
        	"CA": <bool>,
          "authority_key_identifier": {
            	"keyid": "<string>",
              "serial_number": "<string>"
          },
          "ca_information_access": {
            	"<string>": "<string>"
          },
          "certificate_policies": ["<strings>"],
          "cert_template_name_dc": "<string>",
          "crl_distribution_points": ["<strings>"],
          "extended_key_usage": ["<strings>"],
          "key_usage": ["<strings>"],
          "netscape_cert_comment": "<string>",
          "netscape_certificate": <bool>,
          "old_authority_key_identifier": <bool>,
          "pe_logotype": <bool>,
          "subject_alternative_name": ["<strings>"],
          "subject_key_identifier": "<string>",
          "tags": ["<strings>"],
          "<additional extensions:string>": "<string>"
        },
        "first_seen_date": <int:timestamp>,
        "issuer": {
          	"C": "<string>",
            "CN": "<string>",
            "L": "<string>",
            "O": "<string>",
            "OU": "<string>",
            "ST": "<string>"
        },
        "public_key": {
        	"algorithm": "<string>",
          	"rsa": {
          		"key_size": <int>,
            	"modulus": "<string>",
            	"exponent": "<string>"
          },
          	"dsa": {
            	"p": "<string>",
            	"q": "<string>",
            	"g": "<string>",
            	"pub": "<string>"
          },
          	"ec": {
          		"oid": "<string>",
              "pub": "<string>"
          }
        },
        "serial_number": "<string>",
        "signature_algorithm": "<string>",
        "size": <int>,
        "subject": {
          	"C": "<string>",
            "CN": "<string>",
            "L": "<string>",
            "O": "<string>",
            "OU": "<string>",
            "ST": "<string>"
        },
        "thumbprint": "<string>",
        "thumbprint_sha256": "<string>",
        "validity": {
          	"not_after": "<strnig:%Y-%m-%d %H:%M:%S>",
            "not_before": "<strnig:%Y-%m-%d %H:%M:%S>"
        },
        "version": "<string>"
    },
 "links": {
    "self": <string>
  }
}
```

---

← [Software and Toolkit](software-toolkit-object.md) · [up](README.md) · [Submissions](submission-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/ssl-certificate-object>.*
