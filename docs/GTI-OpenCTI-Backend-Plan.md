# GTI → OpenCTI backend compatibility plan v0.1

Status: design proposal, 2026-10-03. No backend code or vendor data changed. The [GTI source contract](GTI-Data-Structures.md) is the first deliverable; this plan maps it to the **currently available** OpenCTI checkout at `/workspaces/OpenCTI`, commit `3828f28d50206e8594bea7de7b824f192cacee32`. Its reputation and custom-field features are branch-specific, so the mapping is conditional on pinning and validating a deployable baseline. See the [existing release roadmap](OpenCTI-Transfer-Plan.md) for wider UI, tenancy, and operational scope.

## Compatibility target

Start with **ingest and preserve supported GTI data** through OpenCTI and STIX 2.1; do not assert binary/API parity with Google Threat Intelligence. A future GTI-shaped REST facade is a different product and needs separately approved endpoint/field/error/pagination contracts. Use a source-specific adapter at the boundary, not a replacement OpenCTI data model or invented GTI fields on every core entity.

```text
GTI native JSON / optional GTI STIX (license-aware fetch)
  → source-schema validation and pagination
  → source envelope + immutable source-ID registry + policy/quarantine
  → explicit native/STIX-to-OpenCTI mapping
  → staged STIX 2.1 import → OpenCTI queries → policy-aware export
  → semantic fixture comparison and documented losses
```

The source envelope holds `source_system`, `(source_type, source_id)`, endpoint, retrieval time, source created/modified times, response format, content hash/restricted raw reference where licensed, mapper/schema version, status, warnings, markings, creator, redistribution policy and checkpoints. Do not put secrets, paid payloads or external API responses in Git. Separate an original GTI assertion, an analyst conclusion and an OpenCTI aggregate verdict.

## First mapping register (proposals, **not** verified round trips)

| GTI source / field | Candidate OpenCTI projection | Preserve separately / decision gate |
| --- | --- | --- |
| Native `file`, `url`, `domain`, `ip_address` | Corresponding cyber observable; a STIX `indicator` only when the source actually provides indicator semantics/pattern. | Native `(type,id)`, value, hashes, vendor scan aggregates and dates. Test URL normalization and ID collision before upsert. |
| `gti_assessment.{verdict,severity,threat_score,contributing_factors,gti_description_cards}` | Separate GTI-attributed assessment/reputation projection on an observable; optional indexed fields for search. | No direct assignment of `threat_score` to OpenCTI `x_opencti_score`, `confidence`, or existing VT-scanner verdict. Retain raw evidence and lack-of-assessment state. |
| GTI threat actor / campaign | Threat actor vs intrusion set selection subject to observed STIX type; campaign → Campaign. | Preserve native collection type, source ID, GTI STIX ID if supplied, aliases and attribution context; don't auto-merge on normalized name. |
| Malware family / software toolkit | Malware family vs Tool, with original STIX `malware` representation retained. | Don't silently collapse family/tool semantics just because GTI STIX may project both as `malware`. |
| GTI report | Report with source publication time only if supplied; explicit object references. | GTI `report_id`, `report_type`, `version`, body access/licensing, original creator and IDs; quarantine a missing required target `published` instead of inventing a date. |
| GTI IoC collection | STIX `grouping` candidate and membership/relationship edges. | **Not** an OpenCTI TAXII collection; preserve membership, direction and paginated counts. Test whether the pinned OpenCTI import accepts this grouping flavor. |
| Vulnerability | Vulnerability with CVE as external reference if present; ATT&CK objects/relationships where provided. | MVE ID and vendor risk/EPSS/CVSS provenance; unknown GTI extensions remain in the source envelope until supported. |
| GTI `tlp`, `private`, owner/viewers and licensing | Markings plus actual OpenCTI Authorized Members/organization enforcement and export policy. | `private` is not a TLP marking; failing to map either must block distribution, not default to public. |
| Native relationship descriptors / GTI STIX SROs | Source→target STIX relationships only when meaning/direction are confirmed. | Keep original relation name, relationship ID (if any), cursor and unresolved/not-found descriptors. A list of descriptors is not proof of full fetch. |
| Threat profile | Deferred: separate private preferences/recommendations service, if needed. | Not an actor or shared STIX object by default; clarify owner-specific access before implementation. |

GTI source evidence: [native objects](Easy-access/GTI/gtidocs/reference/01-api-introduction/api-responses/introduction-objects.md), [native relationships](Easy-access/GTI/gtidocs/reference/01-api-introduction/api-responses/introduction-relationships.md), [GTI STIX types and extension definitions](Easy-access/GTI/gtidocs/reference/01-api-introduction/stix-responses.md), and the per-object links in the [source contract](GTI-Data-Structures.md). The official GTI references were retrieved through Context7. OpenCTI uses [STIX 2.1 in its data model](https://github.com/OpenCTI-Platform/docs/blob/main/docs/usage/data-model.md); verify against the pinned checkout for behavior.

## OpenCTI integration points and identified gaps

- STIX export boundary: `src/database/stix-2-1-converter.ts` builds core STIX and flattens custom fields into the OpenCTI extension. Ingestion, not just export, needs a proven inverse round trip.
- Identity boundary: `src/schema/identifier.js` computes report identity from `name + published`, and campaign/intrusion-set/malware from names. Introduce a source-ID registry and pre-upsert collision check; don't assume a GTI external ID prevents core merges.
- Experimental custom fields: `src/modules/customField/custom-field-stix-utils.ts` exports `x_opencti_cf_*` values; the inverse helper has **no production call site found** in this checkout. Probe an actual import before using fields as normative GTI storage. Unknown definitions are skipped, so fail visibly at the adapter boundary.
- Experimental reputation: `src/modules/reputation/providers/virustotal-provider.ts` derives verdicts from `last_analysis_stats`. This is **not** GTI `gti_assessment`, and community `reputation` is not GTI `threat_score`. Keep distinct provider identity, score scale, provenance and time.
- Use OpenCTI's existing `modules/ingestion/` and connector/bundle paths; audit the separately maintained Google TI connector at a pinned version before assuming it emits the required native fields, GTI STIX extensions, mappings, or licensed bodies.

All source paths in this section are relative to `/workspaces/OpenCTI/opencti-platform/opencti-graphql/` unless otherwise stated. Earlier feature-branch audit also found a parse error in `reputation-domain.ts`; do not build against that branch until it is repaired and green. The findings above are source inspection, **not** passing end-to-end compatibility tests.

## Delivery sequence and exit criteria

| Gate | Work | Proof before the next gate |
| --- | --- | --- |
| 0. Source contract | Review [GTI structures](GTI-Data-Structures.md) with GTI entitlements; collect minimal redacted permitted fixtures (four IoCs, actor/campaign, family/tool, report, collection, vulnerability, missing/benign assessment, 2-page relationship and STIX Bundle). | Confirm discriminators and score shapes; record endpoint, headers, optionality, field ownership and fixture hashes. No licensed data in Git. |
| 1. Mapping specification | For each field, declare `exact`, `transformed`, `source-only`, `deferred`, or `unsupported`; specify source ID ↔ OpenCTI ID, temporal, attribution, markings and relationship policies. | Machine-readable mapping register and review of ambiguous cases (actor/intrusion set, grouping, tool, report publication, benign indicators). |
| 2. Adapter spike | Implement a separate, versioned GTI reader/validator and STIX mapper with idempotent checkpoints, pagination, per-field loss reports and quarantine. Reuse a pinned connector when it demonstrably satisfies these contracts. | Offline fixtures exercise malformed IDs, missing assessment, unknown fields/extensions, collisions, pagination and blocked redistribution. |
| 3. Staged OpenCTI round trip | Import to disposable OpenCTI; query under authorized/restricted users; export and re-import. Prove custom-field inverse or keep source-only storage. | Semantic equality for supported fields, loss ledger for unsupported fields, identity/marking/relationship/security checks; no unexplained dropped fields or leaked counts. |
| 4. Release hardening | Repair the baseline branch, pin connector/platform versions, test upgrades, quotas/retry and retention. Only then expose UI projections. | CI green; N/N+1 migrations; service-account audit, licence policy and operator runbook approved. |

Before gate 2, agree on the one concrete compatibility target for Release 1: **GTI ingestion + preserved source facts in OpenCTI**, or a **named GTI API client requiring specific response endpoints**. The latter adds a separate facade and should not be smuggled into an ingestion milestone.
