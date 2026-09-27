# OpenCTI transfer and GTI compatibility plan

Status: proposal — implementation has not started. Owner, target OpenCTI version, deployment environment, Google TI entitlements, and budget: to be decided.

## 1. Goal and boundaries

Use OpenCTI as the maintained CTI platform and security boundary. Configure it to support a Google Threat Intelligence (GTI)-aligned analyst experience: GTI data ingestion, report categories, threat-object navigation, provenance, investigation, and sharing. Preserve the Patchwork CTI framework as a separately identified analytic layer rather than quietly redefining GTI objects. OpenCTI is based on STIX 2.1; the GTI API normally returns its own JSON and supports STIX bundles on specified endpoints. “GTI-compatible” therefore means documented, tested mappings and round-trip behaviour, not that GTI is itself a single conformance standard or that the UI must copy Google's product.[9][5]

This is a **transfer of workflow and data semantics**, not a plan to fork OpenCTI on day one. Prefer configuration, dashboards, workflows and connectors for supported fields. Budget for an adapter/sidecar from the start: Patchwork's extension and identity rules are not guaranteed by stock OpenCTI. OpenCTI supports TLP:AMBER+STRICT and retains the highest marking of a type on updates/merges, but a GTI connector import must be shown to **apply** the correct marking before any object is visible to users. Test each path before promising fidelity; a major frontend fork is a last resort because it must be rebased and security-tested on every upgrade.[14][16][17]

The source of truth for Patchwork's own semantics remains [the framework](Patchwork-CTI-Framework.md), [report types](Report-Types.md), [vocabularies](Vocabularies.md), and [sectors](Sectors.md). The checked-in GTI documentation under [Easy-access/GTI/gtidocs](Easy-access/GTI/gtidocs/) is an unofficial snapshot; use each page's `source` URL and recheck live documentation when implementing. See in particular [GTI STIX responses](Easy-access/GTI/gtidocs/reference/01-api-introduction/stix-responses.md) and [current/retired GTI report types](Easy-access/GTI/gtidocs/guides/07-report-analysis/report-types.md).

## 2. Decisions to make before provisioning

| Decision | Proposed default | Why / evidence required |
| --- | --- | --- |
| Data contract | GTI objects as imported; Patchwork assertions separately attributed and namespaced | Patchwork explicitly differs from GTI: its adversary is an `intrusion-set`, personas are `threat-actor`, and its three attribution tiers remain separate linked objects; see [framework §2.2](Patchwork-CTI-Framework.md#2.2-where-the-standards-disagree,-and-who-wins) and [§4](Patchwork-CTI-Framework.md#4.-adversary-model-and-the-attribution-ladder). Do not auto-convert a GTI actor into a Patchwork Mature tier. |
| Licensing | Confirm GTI API entitlement and OpenCTI edition *before* a pilot | The Google TI connector needs a GTI API key; reports need GTI Enterprise/Enterprise Plus. OpenCTI organization segregation, Authorized Members, Playbooks/automation, Fintel templates and audit-log features are Enterprise Edition; select paid EE or document CE alternatives before depending on them.[7][18] |
| Tenant model | One organization for the first pilot; explicit later decision for multi-member sharing | OpenCTI organization segregation filters visibility in **one shared graph**, not isolated tenants. Test cross-organization name collisions, existence leaks, relationship visibility and connector-service-account privileges; for hard tenant isolation, evaluate separate instances.[10][16] |
| UI | Configure supported fields; budget separate Patchwork capture UI | OpenCTI has configurable dashboards, existing attributes and taxonomies, but no documented configuration path for new arbitrary Patchwork fields/forms. Use a tested external workflow or scoped frontend change for dedicated forms.[2][3][17] |
| Import scope | Start with a narrow reports-only window; enable other collections deliberately | The connector defaults to reports only, with campaigns, actors, malware, vulnerabilities, tools and IOCs opt-in; related report entities can still be fetched. API quota and dedup effects must be measured.[7] |
| External redistribution | No automatic republication of licensed GTI content | Determine contract terms, allowed recipients, retention, PDF rights, and TLP/handling rules with the account owner before TAXII, public dashboards or exports. |
| Version | Pin a tested OpenCTI and connector release pair | The connector README currently lists two minimum OpenCTI versions (6.5.1 and 6.7.7); treat this as unresolved documentation, and test the actual tagged image against the selected platform before deployment.[7] |

## 3. Target architecture

```text
GTI API/authorized feed ──> stock connector ──> isolated staging OpenCTI
           │                                  (no production merge yet)
           └──> restricted raw source archive ──> mapping/identity gate
Patchwork analyst input / sample bundles ────────> validation + extension sidecar
                                                     │
                                         approved production OpenCTI graph
                                                     │
                            configured dashboards / searches / gated exports
```

- The stock external-import connector is the **staging pilot** ingest route, not a direct production feed until identity safety is proven: it transforms external data into STIX 2.1 bundles and OpenCTI upserts same-named entities. Keep staging isolated so a GTI actor cannot merge with a Patchwork actor before the mapping gate. Give each connector a dedicated **Service Account** with the Connector role and scoped token stored in a secret manager; where organization segregation is enabled, service accounts bind to the main organization and bypass Authorized Members by default, so they are not a per-tenant isolation mechanism.[7][10][16]
- In a restricted source archive/registry, keep original GTI ID, source URL, original type/name, source timestamp, raw payload reference or checksum, ingestion time, connector version and applicable markings. OpenCTI canonical STIX IDs may differ from source IDs; never promise that the source ID is the OpenCTI `standard_id`. Never rewrite `created_by_ref` so a GTI assertion looks like a Patchwork member assertion. The GTI STIX format includes a Google TI identity and can include extension definitions and pagination metadata.[5][16]
- Keep transformation code separate from the stock connector if possible; if extension persistence or upstream mappings require modifying connector code, maintain a small, pinned patch with regression fixtures and an upstream contribution path. OpenCTI's workers decide identity and perform upserts after the connector submits a bundle; a connector's own dedup logic cannot override those rules. Gate or transform source objects **before** the production queue and verify that OpenCTI's server-side dedup cannot merge distinct assessments. Never silently collapse a many-to-many attribution relationship into one actor.[16]
- Do not treat OpenCTI's GraphQL/TAXII/live-stream interfaces as a GTI-compatible API. They are OpenCTI interfaces; a GTI-shaped API would be a separately versioned adapter with its own auth and contract tests.[15]

## 4. Compatibility contract and first mapping register

Maintain a versioned table with: GTI source endpoint and JSON field, GTI STIX field/object, OpenCTI type/field, Patchwork type/extension, transformation, information loss, identity key, licence/marking, fixture and test result. Mark each entry `direct`, `transformed`, `display-only`, `unsupported`, or `decision pending`. Start with these rows:

| Source concept | Proposed target | Required test / risk |
| --- | --- | --- |
| GTI report and its type | OpenCTI `report`; retain original GTI type/name and map to Patchwork `report_types` only when explicitly equivalent | Compare live GTI's current/decommissioned catalogue with [Patchwork's 13 authored, 3 retired and 11 feed-assigned values](Report-Types.md). Keep historical types importable but not selectable for new analyst-authored reports; never relabel a GTI report as Patchwork-authored.[12] |
| GTI threat actor | Stock connector creates OpenCTI `intrusion-set`, including when nested under a report | GTI's own STIX response has `threat-actor` objects, whereas the stock connector chooses `intrusion-set`. Preserve original GTI type and ID; prohibit automatic identity merge with Patchwork's Cluster/Temporary/Mature `intrusion-set` and persona `threat-actor`. Explicitly model analyst-approved equivalence links.[5][7] |
| GTI campaign, malware family, software toolkit, vulnerability, technique | OpenCTI `campaign`, `malware`, `tool`, `vulnerability`, `attack-pattern` | Check source references, relationship direction, missing relationships, update semantics and ATT&CK IDs on fixtures. Patchwork campaign `Individual`/`Global` is an analyst assertion, not inferred from a GTI campaign name. |
| GTI domains, IPs, URLs and files | OpenCTI observables plus indicators *when the connector creates them* | Verify pattern, validity, source score, false-positive handling, dedup and export; do not translate GTI score into Patchwork source credibility or threat level.[7] |
| Patchwork MAI | OpenCTI `incident` plus dated observation and source grading | **Known mismatch:** OpenCTI deduplicates Incidents by `name OR alias`; Patchwork requires `name + observed_date`. Distinct observations with the same name can merge and lose separate Admiralty provenance. Before ingest, test an immutable, human-readable observed-date/unique-token naming rule (or an isolation strategy) on two same-named incidents; retaining the extension alone does **not** change OpenCTI's identity key. Keep urgency (`threat_level`) separate from reliability/credibility; see [framework §§3.4, 7.1, 9.2–9.3](Patchwork-CTI-Framework.md).[16] |
| Patchwork attribution ladder/persona | Separate linked `intrusion-set` objects; `threat-actor` persona | Patchwork defines `intrusion-set` → `intrusion-set` `part-of` itself; verify whether the pinned OpenCTI version accepts, displays, filters and re-exports that exact edge. If not, decide explicitly between a documented `related-to` projection with reversible mapping, a sidecar, or a maintained schema patch; do not silently substitute another relationship. Test namespace isolation and review/undo of grouping; see [framework §§4, 9.1](Patchwork-CTI-Framework.md). |
| Patchwork classification | One fixed `extension-definition` and nested `property-extension` | Test import, persistence, filtering, analyst edit, API read, STIX export and re-import of `threat_level`, `threat_domain`, `activity_category`, `observed_date`, `attribution_tier`, `intent` (list) and `campaign_type`. If OpenCTI drops any field, use an explicit adapter/sidecar plus display projection; never claim lossless support until round-trip passes. Extension ID and version are specified in [framework §9.3](Patchwork-CTI-Framework.md#9.3-classification-properties). |
| TLP and provenance | OpenCTI markings, groups/RBAC, creator/source identity | OpenCTI can enforce TLP:AMBER+STRICT, but the stock GTI connector documentation does not establish a default marking for every imported object. Before production, inspect emitted bundles and platform defaults; enforce source-appropriate TLP **and** licence/redistribution handling on entities, relationships and attachments at ingest, fail closed on missing policy, and test with a restricted user. Do not assume either that all GTI STIX payloads are unmarked or that the platform marks them automatically.[7][14][2] |

The stock connector defaults threat-actor and malware alias import to off because GTI aliases may conflict. Keep these defaults until adversary-collision tests pass; names and aliases are *not* proof of identity.[7] Compare actual upstream releases and fixtures, not only this plan's table.

## 5. UI and analyst workflow

**Configuration first:** create dashboards for a GTI-like landing view (new reports, tracked actors, campaigns, malware, vulnerabilities, IoCs, ATT&CK techniques, ingestion health); use saved filters, labels/vocabularies and workflows for triage, review, promotion and publication. Dashboards are permission-aware and exportable as configuration; dashboard layout is not a substitute for enforcing access control on the data.[2][3][4]

**Patchwork-specific workflow:** build an analyst checklist/form prototype for `threat_level`, `threat_domain`, activity category, source reliability/credibility, TLP, observed date, member namespace, attribution tier and evidence links. Treat a dedicated Patchwork authoring surface as a planned deliverable unless the Phase 0 prototype proves a no-code workflow can capture **all** required fields and round-trip them through STIX; OpenCTI's customization of existing attributes is not evidence that arbitrary extension fields appear in stock forms.[17] Default screen sections: source facts vs analyst assessments, provenance/marking banner, evidence chronology, attribution ladder, report type picker, export preview. Imported data is read-only for transformation-owned fields; analyst changes create separately attributed assessments.

**Explicit limits:** no impersonation of GTI branding or assumption of access to Google's proprietary scoring/search/Graph UI; GTI-inspired navigation is a product-design target, not API compatibility. Assess accessibility, keyboard navigation, contrast and mobile layout with actual analysts. Record each UI change as configuration, separate extension, or core fork and measure the upgrade cost.

## 6. Phased delivery and gates

| Phase | Work and concrete deliverable | Exit gate |
| --- | --- | --- |
| 0. Inventory and legal (1–2 weeks, estimate) | Select owners, version/edition, deployment model, entitlements, data volumes, licensing/redistribution, threat model and 20 representative GTI/Patchwork fixtures. Prototype incident identity (`name + observed_date`), `intrusion-set` `part-of`, extension round-trip, marking-on-import and authoring fields. Freeze a compatibility matrix and unsupported-feature list. | Written decisions on editions, GTI access, export rights, Patchwork authority, required adapter/authoring surface and explicit alternatives for failed prototypes. No live ingest without this. |
| 1. Secure OpenCTI baseline (1–2 weeks) | Isolated non-production install; named accounts/roles, marking policies, TLS, backups and restore drill, retention, secret rotation, monitoring, pinned image versions and update runbook. EE adds native activity monitoring/audit logs and UI-configured SSO; if CE is selected, document a tested external audit/auth approach or explicitly defer those features.[18] | Two-user access matrix tested, backup restored, upgrades rehearsed and no broad connector token; audit/SSO route documented for the chosen edition. |
| 2. GTI ingest pilot (1–2 weeks) | Run pinned Google TI connector **only in isolated staging** with limited report types/date range and no PDF or bulk historical backfill initially. Inspect generated bundles and enforce marking policy before release; save fixtures, counts, source IDs, job state, quota/error metrics and a replay log. | Repeat import without unintended merges, recover from a simulated failure/quota pause, reconcile records, inspect actor/alias mapping, and prove restricted users cannot see imported objects that require markings. |
| 3. Semantic adapter (2–4 weeks, scope depends on Phase 0) | Implement required identity isolation, source-ID registry, marking gate and any proven missing transformations: report-type mapping, Patchwork extension preservation, explicit attribution links, two-way STIX fixtures and quarantine for invalid/ambiguous data. | 20 fixture round-trips preserve normative Patchwork fields, TLP, provenance, distinct observations, version/revocation and links; unsupported fields reported, not discarded silently. |
| 4. UI pilot (1–3 weeks) | Exportable dashboards, saved filters, triage workflow and report templates, plus the authoring surface selected in Phase 0. | Five analysts complete report authoring, attribution revision and restricted-data review without breaking provenance or markings; accessibility and upgrade smoke tests pass. |
| 5. Controlled migration and operations (2–4 weeks) | Dry-run historical import in batches; mapping/reconciliation report, cutover and rollback plan, analyst training, runbooks, ownership and monthly upgrade rehearsal. | Signed-off reconciliation, access review, restore and rollback test; only then widen to production feeds/users. |

Time ranges are planning estimates, not commitments; capacity and licence access are unknown. Do not advance a phase with an open identity/marking/data-loss defect.

## 7. Test set and measurable acceptance

1. **Schema:** validate GTI STIX fixtures, Patchwork sample bundles and extension-definition references with a STIX 2.1 validator; test unknown extensions, list-valued `intent`, missing `observed_date`, deprecated `x_` assumptions, and both serialisation directions.
2. **Identity:** import the same fixture twice; modify and revoke; test two members choosing the same actor name, GTI name/alias collision, report `name` + `published`, incident `name` + `observed_date`. Assert no unintended merge or silent field loss; record the actual OpenCTI identity algorithm rather than assuming the framework's [§9.2](Patchwork-CTI-Framework.md#9.2-identity-and-merge-rules) is its implementation.
3. **Attribution:** cluster → temporary → mature promotion retains all tiers and the original evidence. Undo one grouping without rewriting other assessments. A GTI imported actor is not automatically a Patchwork mature actor.
4. **Handling:** TLP-restricted actor/report and PDF are inaccessible through graph search, dashboard, API, export and a lower-privilege account. Test downstream TAXII/stream filters and licences separately.
5. **Operations:** fixed-window ingest reconciles source IDs, deleted/updated objects, quota pause, restart, rollback and replay. Alert on failures, freshness lag, quarantine growth and anomalous volume. Restore from backup, then re-run the import and check idempotence.
6. **Upgrade:** pin a reproducible release pair, run tests against the next OpenCTI/connector versions in staging, and measure drift in mappings, GraphQL schema, UI configuration and migration scripts.

## 8. Risks and non-goals

- **Lossy mapping is the primary risk.** GTI's native `threat-actor` versus stock connector `intrusion-set`, and Patchwork's distinct ladder/persona semantics, cannot be papered over with labels. Treat this as a product decision and a fixture-based integration test, not a cosmetic UI change.[5][7]
- **Security is not inherited automatically.** OpenCTI provides access-control and marking mechanisms, but the deployment, secrets, backups, connector privileges and export rules must be operated and tested. Organization segregation has an Enterprise licensing boundary.[10][11][14]
- **GTI data rights and API quotas** can limit the pilot. The connector documents resumable quota handling, but capacity and contractual sharing permissions must be confirmed for the actual subscription.[7]
- **No full GTI clone, no replacement of GTI's licensed API, no promise of zero-maintenance OpenCTI, and no automatic conversion of GTI confidence scores into Patchwork grades.** The initial release should favor a faithful, auditable integration over feature parity.

## 9. Immediate next actions

1. Confirm whether “GTI-compatible” means **GTI feed import and familiar analyst UI** (recommended first release) or **a GTI API-compatible surface** (a separate later product). Confirm whether Patchwork v0.6 remains the authoritative analyst model.
2. Confirm OpenCTI edition, hosting, single-/multi-organization scope, GTI subscription/API entitlement, redistribution rights, owner and pilot analysts.
3. Pin platform/connector tags and create a staging environment; document observed field behaviour in the compatibility matrix before selecting a UI implementation.
4. Select 20 redacted fixtures from [Real-Examples](Real-Examples/) and authorized GTI test data. Never commit GTI credentials, paid PDFs or licensed raw payloads to this repository.

## Sources

[2] https://docs.opencti.io/latest/usage/dashboards
[3] https://docs.opencti.io/latest/administration/ontologies
[4] https://docs.opencti.io/latest/usage/workflows
[5] https://gtidocs.virustotal.com/reference/stix-responses
[7] https://github.com/OpenCTI-Platform/connectors/blob/master/external-import/google-ti-feeds/README.md
[9] https://docs.opencti.io/latest/usage/data-model
[10] https://docs.opencti.io/latest/administration/organization-segregation
[11] https://docs.opencti.io/latest/administration/users
[12] https://gtidocs.virustotal.com/docs/report-types
[14] https://docs.opencti.io/latest/administration/segregation
[15] https://docs.opencti.io/latest/deployment/integrations
[16] https://docs.opencti.io/latest/usage/deduplication
[17] https://docs.opencti.io/latest/administration/entities
[18] https://docs.opencti.io/latest/administration/enterprise
