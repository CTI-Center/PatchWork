---
title: "ASM Credential Security Details"
source: https://gtidocs.virustotal.com/docs/asm-credential-security-details
slug: asm-credential-security-details
section: guides
group: "ASM"
updatedAt: 2025-09-25T00:28:58.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [ASM](../README.md) › [Inbound Integrations](../inbound-integrations.md) › ASM Credential Security Details

---

# asm-credential-security-details

To provide the highest level of security, **ASM leverages Google Cloud Secret Manager** for the storage of all customer-provided credentials. This allows our platform to be built upon a foundation of enterprise-grade security controls managed directly by Google.

## security-controls-for-credential-storage-in-asm

When you provide a credential to ASM for an inbound integration, it is stored within GCP Secret Manager. This provides the following safeguards to ensure its confidentiality and integrity at rest.

### confidentiality-via-encryption-at-rest

Protecting the secrecy of your credentials is the primary objective. GCP Secret Manager provides robust, automatic encryption.

* **Automatic Encryption:** Every secret you entrust to ASM is immediately and automatically **encrypted at rest** using the industry-standard **Advanced Encryption Standard with a 256-bit key (AES−256)**. This is not an optional feature; it is enabled by default for all data.

* **Layered Key Management:** The encryption keys used to protect your secrets are themselves encrypted with a set of master keys that are regularly rotated by Google. This layered approach provides defense-in-depth against unauthorized access to the raw credential data.

### integrity-and-granular-access-control

We ensure that your credentials are not only encrypted but are also protected from unauthorized access or modification.

* **Principle of Least Privilege:** ASM adheres strictly to the principle of least privilege using Google Cloud's Identity and Access Management (IAM). This means that only the specific, authorized components of the ASM platform required to perform an inbound integration scan can request access to your credentials. Access is granular and purpose-driven.

* **Data Integrity Verification:** Google Cloud's infrastructure employs multiple layers of checksums and cryptographic verification. When the ASM platform retrieves your credential for a scan, these checks ensure the data has not been corrupted or tampered with while at rest.

### verifiable-security-through-auditing

To provide you with the necessary validation and transparency, all access is logged and auditable.

* **Immutable Audit Trail:** Every administrative action or access attempt made by the ASM platform to your secrets is recorded in Cloud Audit Logs. This creates a detailed and immutable record, providing a verifiable trail of when and for what purpose your credentials were used by our service. This is critical for both security assurance and compliance requirements.

* **Secure Credential Management:** The underlying use of Secret Manager supports best practices like credential versioning. This facilitates the secure rotation of your tokens and keys without service disruption, empowering you to maintain a strong security posture.

In summary, by utilizing GCP Secret Manager as the secure vault for your integration credentials, ASM ensures that your sensitive data is protected by Google's world-class security infrastructure. This provides you with verifiable assurance that the confidentiality, integrity, and controlled availability of your credentials are comprehensively safeguarded.

---

← [ASM Akamai Integration](asm-akamai-integration.md) · [up](../README.md) · [ASM AWS Integration](asm-aws-integration.md) →

*Archived from <https://gtidocs.virustotal.com/docs/asm-credential-security-details>.*
