# Google Threat Intelligence data structures: source contract v0.1

Status: design draft, 2026-10-03. This describes a **supported subset** for an importer; it is not an official GTI schema, a GTI API emulator, or a change to OpenCTI. The local GTI reference snapshot was retrieved on 2026-09-01; selected points were checked against the official documentation through Context7 on 2026-10-03. Capture permitted, redacted live responses before promoting these types to production validators. GTI access, fields and redistribution depend on subscription and policy.

See the [backend mapping and implementation plan](GTI-OpenCTI-Backend-Plan.md) and the [broader compatibility roadmap](OpenCTI-Transfer-Plan.md).

## 1. Three different wire formats

| Format | Documented shape | Interpretation |
| --- | --- | --- |
| Native GTI JSON | `{ "data": { "type", "id", "attributes", "links", "relationships"? } }`; lists use `data: []` and pagination metadata. | GTI's source contract; `(type, id)` identifies an object. Do **not** treat it as STIX. |
| GTI STIX 2.1 | `bundle` with `objects`, Google TI `identity`, STIX entities/relationships and `extension-definition` objects; some paginated bundles have `extensions` metadata. Requested using `output_format=stix` on supported endpoints; `x-tool` requests curated information. | A separate, optional source representation. Its STIX IDs are not interchangeable with native IDs or OpenCTI's internal IDs. Unsupported endpoints may return 400. |
| OpenCTI STIX / GraphQL | OpenCTI's own STIX conversion and its version-specific GraphQL schema. | Import/export or application projection, **not** the GTI wire contract. |

References: [GTI objects](Easy-access/GTI/gtidocs/reference/01-api-introduction/api-responses/introduction-objects.md), [relationships](Easy-access/GTI/gtidocs/reference/01-api-introduction/api-responses/introduction-relationships.md), [STIX responses](Easy-access/GTI/gtidocs/reference/01-api-introduction/stix-responses.md); official pages: [objects](https://gtidocs.virustotal.com/reference/introduction-objects), [STIX responses](https://gtidocs.virustotal.com/reference/stix-responses).

## 2. Draft source-facing types

The following TypeScript is a **design notation**, not checked-in runtime code. Optional properties mean the API may omit a field because of the endpoint, query, entitlement, or object. `unknown` means the importer must retain the value for validation; it must never silently discard it. Object type labels and collection-type labels must be read from the response, not inferred from the URL.

```ts
type GtiDescriptor = { type: string; id: string };
type GtiRelationship = {
  data: GtiDescriptor | Array<GtiDescriptor | {
    type: string; id: string; error: { code: string; message?: string }
  }> | null;
  meta?: { cursor?: string };
  links?: { self?: string; related?: string; next?: string };
};
type GtiNativeObject<A extends Record<string, unknown>> = GtiDescriptor & {
  attributes: A;
  links?: { self?: string };
  relationships?: Record<string, GtiRelationship>;
};
type GtiObjectResponse<A extends Record<string, unknown>> = {
  data: GtiNativeObject<A>;
};
type GtiListResponse<A extends Record<string, unknown>> = {
  data: Array<GtiNativeObject<A>>;
  meta?: { cursor?: string };
  links?: { next?: string };
};

type GtiVerdict = 'VERDICT_BENIGN' | 'VERDICT_UNDETECTED' |
  'VERDICT_SUSPICIOUS' | 'VERDICT_MALICIOUS' | 'VERDICT_UNKNOWN';
type GtiSeverity = 'SEVERITY_NONE' | 'SEVERITY_LOW' |
  'SEVERITY_MEDIUM' | 'SEVERITY_HIGH' | 'SEVERITY_UNKNOWN';
type GtiAssessment = {
  verdict?: { value: GtiVerdict | string };
  severity?: { value: GtiSeverity | string };
  // Provisional: prose describes an integer; published examples use { value: integer }.
  threat_score?: number | { value: number };
  description?: string;
  contributing_factors?: Record<string, unknown>;
  gti_description_cards?: Record<string, Array<{
    influence?: string; title?: string; sub_title?: string;
    collection_type?: string;
    related_links?: Array<{ title: string; url: { object_type: string; id: string } }>;
  }>>;
};
type GtiIocAttributes = Record<string, unknown> & {
  gti_assessment?: GtiAssessment;
  last_analysis_date?: number;       // Unix UTC seconds, where documented
  last_modification_date?: number;   // Unix UTC seconds, where documented
  last_analysis_stats?: Record<string, number>;
  tags?: string[];
  reputation?: number;               // Community votes; NOT GTI threat_score
};
type GtiThreatCollectionAttributes = Record<string, unknown> & {
  collection_type: string;           // e.g. threat_actor, campaign, report, collection
  name?: string; description?: string;
  origin?: string; private?: boolean; tlp?: string;
  creation_date?: number; last_modification_date?: number;
  tags?: string[];
};
type GtiReportAttributes = GtiThreatCollectionAttributes & {
  content?: string; report_id?: string; report_type?: string;
  author?: string; report_confidence?: string; version?: number;
  executive_summary?: string;
};
type GtiVulnerabilityAttributes = GtiThreatCollectionAttributes & {
  cve_id?: string; mve_id?: string; cvss?: Record<string, unknown>;
  epss?: Record<string, unknown>; risk_rating?: string;
  exploitation_state?: string; field_sources?: unknown[];
};
type GtiStixBundle = {
  type: 'bundle'; id: string;
  objects: Array<Record<string, unknown>>; // validate per STIX 2.1 object/extension
  extensions?: Record<string, { meta?: { cursor?: string; next?: string } }>;
};
```

These types intentionally leave the vendor's top-level `type` open: GTI groups threat objects behind `/collections/{id}`, whereas the nested `attributes.collection_type` and the STIX `type` use different labels. Define an endpoint-specific, observed discriminator catalog before freezing a runtime tagged union; never silently turn `threat_actor` into `threat-actor` or `malware_family` into `malware`.

## 3. Initial object catalog and required fixtures

| Source family | Native fields to capture first (all optional unless specified by the response) | Important distinct semantics |
| --- | --- | --- |
| File, URL, domain, IPv4 | `(type, id)`, analysis timestamps/stats, `gti_assessment` if returned, relationship descriptors; file hashes, URL/network value where present. | Keep observed identifier and observable value separately. URL ID can be a URL hash or unpadded Base64. A harmless/unknown verdict is not equivalent to “no assessment.” |
| Threat actor, campaign | `collection_type`, name, aliases, description, origin, TLP, first/last-seen detail arrays, targets, relationships. | Claims about region, attribution and activity have source and confidence; names are not safe cross-source merge keys. |
| Malware family, software/toolkit | Same collection base plus roles, capabilities and related indicators. | Preserve family-vs-tool distinction even if a STIX representation uses `malware` for both. |
| Report | Collection base plus `content`, `report_id`, `report_type`, `version`, author, confidence, executive summary. | Distinguish report creation, modification and publication dates; **do not manufacture `published`** when absent from a source representation. Retain report IDs/version. |
| IoC collection | Collection base and member descriptors/relationship cursor. | GTI collection is a threat-intelligence object; it is **not** an OpenCTI TAXII collection, and its STIX projection uses `grouping`. |
| Vulnerability | Collection base plus CVE/MVE IDs, CVSS/EPSS, risk/exploitation and field-level sources. | Store vendor risk separate from OpenCTI scoring; CVE and MVE are not interchangeable IDs. |
| Threat profile | Private/user-configured interests, recommendations, related entities and access rules. | A saved threat-profile configuration is **not** a threat actor. Defer until authenticated fixtures establish its complete object shape. |

Object references: [file](Easy-access/GTI/gtidocs/reference/17-api-objects/file-object.md), [URL](Easy-access/GTI/gtidocs/reference/17-api-objects/url-object.md), [domain](Easy-access/GTI/gtidocs/reference/17-api-objects/domains-object.md), [IPv4](Easy-access/GTI/gtidocs/reference/17-api-objects/ip-object.md), [actor](Easy-access/GTI/gtidocs/reference/17-api-objects/threat-actor-object.md), [campaign](Easy-access/GTI/gtidocs/reference/17-api-objects/campaign-object.md), [malware family](Easy-access/GTI/gtidocs/reference/17-api-objects/malware-family-object.md), [toolkit](Easy-access/GTI/gtidocs/reference/17-api-objects/software-toolkit-object.md), [report](Easy-access/GTI/gtidocs/reference/17-api-objects/report-object.md), [collection](Easy-access/GTI/gtidocs/reference/17-api-objects/ioc-collection-object.md), [vulnerability](Easy-access/GTI/gtidocs/reference/17-api-objects/vulnerability-object.md), [threat profile](Easy-access/GTI/gtidocs/reference/17-api-objects/threat-profile-object.md).

## 4. STIX projection is a separate contract

The documented GTI STIX export represents IoCs as STIX `indicator` objects with patterns and GTI assessment extensions; threat objects as `threat-actor`, `campaign`, `malware` (including families/toolkits), `grouping` (IoC collections), `report` and `vulnerability`. Bundles can include a GTI identity, relationship and extension-definition objects and a bundle-level pagination extension. **Never** confuse a native file/domain/IP/URL with a STIX Indicator, or assume a default GTI JSON response is a STIX Bundle. Preserve `created_by_ref`, original IDs, `external_references`, extension ID/payload and each relationship's direction/type; separately record pagination cursors until fully consumed. The set of available STIX endpoints is narrower than the native API.

## 5. Acceptance rules for a future runtime parser

1. Retain the raw `(type, id)` pair; reject missing/invalid required envelope fields. Preserve unknown source fields or explicitly record their loss.
2. `gti_assessment` is only expected under appropriate request context (`x-tool`) and entitlement: record `present`, `not_requested`, `absent`, `unavailable` or `error` **as importer metadata**, never synthesize an all-clear verdict. Validate score range `0..100` only after the published score-shape ambiguity is resolved with authorized examples.
3. Preserve a one-to-many relationship's descriptors, `NotFoundError` placeholders and pagination. A page is not a complete relationship set until its cursor/next link is exhausted.
4. Keep Unix epoch seconds and STIX ISO-8601 timestamps distinct in the source record; convert only in the mapping layer and retain original values.
5. Treat all code blocks in archived docs as explanatory, not guaranteed parseable JSON; obtain redacted real fixtures under an appropriate GTI license and verify each field before declaring it supported.
