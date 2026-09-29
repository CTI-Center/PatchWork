# OpenCTI and Google Threat Intelligence compatibility roadmap

Status: roadmap v0.2, based on a source audit rather than a greenfield assumption. Last reviewed: 2026-09-29. Owners, production deployment, Google Threat Intelligence (GTI) entitlements, connector release, budget and delivery dates remain to be decided.

## 0. Audit basis and confidence

This plan covers two repositories with different roles:

| Repository | Audited state | Role |
| --- | --- | --- |
| PatchWork (`/workspaces/PatchWork`) | Documentation and research corpus | Defines the Patchwork CTI model, vocabularies, report types, examples and desired STIX profile. It is not the application implementation. |
| OpenCTI (`/workspaces/OpenCTI`) | Branch `feat/reputation-ui-enhancements-4424834575097079276`, commit `3828f28d50206e8594bea7de7b824f192cacee32`, package version `7.260910.0` | Full OpenCTI platform plus unreleased reputation/VT work that can accelerate this roadmap. |

The OpenCTI checkout is a dirty feature branch, not a clean tagged release. Its existing graph contained 36,688 nodes and was used to navigate the code before focused source inspection. All branch-only capability below is therefore `experimental` until it is rebased onto the chosen upstream release and passes build, unit, integration, authorization and upgrade tests.

A focused reputation test run produced **six passing files and 29 passing tests**, but three suites failed to load because `reputation-domain.ts` has a parse error around lines 1360–1361. Restoring build/test health is the first delivery gate. No OpenCTI source code was changed during this audit.

Use these evidence labels during delivery:

- `stable candidate`: present in normal OpenCTI architecture; still verify on the pinned release.
- `experimental`: present on the audited feature branch but not release-ready.
- `external`: supplied by another repository or service and not audited here.
- `planned`: must be designed and built.
- `out of scope`: not required for Release 1.

## 1. Goal and definition of compatibility

Use OpenCTI as the maintained CTI platform and security boundary, then add the smallest integrations and extensions needed for a GTI-aligned analyst workflow and the Patchwork analytic model. Do not fork the whole platform or copy Google's branding and proprietary behavior.

“GTI compatible” is not a single standard. GTI exposes native API schemas and selected STIX responses, while OpenCTI uses its own GraphQL model and STIX 2.1 conversion. Compatibility must be stated at four independently testable levels:

1. **Standards:** valid STIX 2.1 and TAXII 2.1 exchange, plus a versioned Patchwork STIX profile.
2. **Data:** explicit GTI JSON/STIX ↔ OpenCTI ↔ Patchwork mappings, identity rules and loss declarations.
3. **Workflow/UI:** familiar search, reputation lookup, investigation, reports, entity navigation, saved views and alerting using OpenCTI building blocks.
4. **API:** an optional GTI-shaped facade for named consumers. This is not part of the first release unless a real consumer contract requires it.

Release 1 should deliver controlled GTI ingestion, Patchwork field round-tripping, a hardened reputation workflow, configured analyst views, policy-safe sharing and operational readiness. It should not claim full GTI product, hunting, sandbox, ASM, DTM, AI or REST API parity.

The source of truth for Patchwork semantics remains [the framework](Patchwork-CTI-Framework.md), [report types](Report-Types.md), [vocabularies](Vocabularies.md) and [sectors](Sectors.md). The checked-in [GTI documentation snapshot](Easy-access/GTI/gtidocs/) is unofficial and must be revalidated against the live service before implementation.

## 2. Audited capability disposition

The implementation strategy is **reuse → configure → extend → build**.

| Area | Audited OpenCTI capability | Decision |
| --- | --- | --- |
| STIX 2.1 | Store-to-STIX conversion and bundle construction exist in `opencti-graphql/src/database/stix-2-1-converter.ts`. | Reuse; add Patchwork/GTI round-trip fixtures and semantic comparison. |
| Object identity | Deterministic standard IDs exist in `src/schema/identifier.js`. | Reuse, but isolate source IDs and test Patchwork mismatches before import. |
| TAXII and feeds | TAXII publication/ingestion, rolling feeds, streams, filtering and tests exist. | Configure and harden; do not build a second TAXII stack. |
| Search and entity UI | Global search and actor, campaign, malware, vulnerability, report and observable views exist. | Reuse and add provenance/mapping affordances only where needed. |
| Dashboards and graph | Dashboards, public dashboards, investigation graph and workspaces exist. | Configure/export layouts; extend only for policy and Patchwork review states. |
| Saved experience | Custom views, entity-layout customization, alerts/triggers and notifications exist. | Configure first; add sharing/ACL behavior only if the pilot proves a gap. |
| Access control | Capabilities/RBAC, markings, Authorized Members and organization segregation exist. | Reuse, then prove enforcement on every derived object, edge, file and export. |
| Extension framework | Module registration and GraphQL schema extension mechanisms exist. | Reuse for narrow modules; avoid a broad core fork. |
| Custom fields | Backend, admin UI, entity rendering, validation/filtering and STIX export utilities exist behind `CUSTOM_FIELDS`. | Experimental accelerator; complete an import/round-trip proof before adoption. |
| Reputation workspace | Workspace, observable tab, GraphQL, cache, credential vault and provider registry exist on this branch. | Repair and harden rather than rebuild; keep branch-only until release gates pass. |
| Google TI feed connector | Not present here; the connector is in the separate OpenCTI connectors repository. | External dependency: pin, audit and integration-test an exact release. |
| Patchwork policy/mapping | No source-ID registry, compatibility register, quarantine or Patchwork policy gate was found. | Build a small adapter/sidecar unless Phase 0 proves native modules sufficient. |
| GTI-shaped REST API | Not present. | P2 decision; GraphQL/TAXII/streams are not GTI API compatibility. |

### 2.1 Experimental reputation baseline

The branch registers VirusTotal, MalwareBazaar, Triage, ANY.RUN and an OpenCTI-state card. It contains per-user encrypted credentials, provider timeouts, Redis caching, normalized verdicts, optional persistence, score/label updates, MalwareAnalysis and ATT&CK-oriented enrichment code, provider identities and an observable reputation tab.

Useful controls already present include the `INVESTIGATION` capability gate, per-user ownership filters, platform-derived encryption, API-key redaction from GraphQL/audit data, endpoint deny-list validation and primary-organization membership validation.

Do not yet describe this as production-ready GTI support:

- the branch has a parse error and only focused unit coverage;
- `endpoint_override` is stored and validated but is not consumed by provider calls;
- provider failure returns an error verdict; it is not a demonstrated persisted-verdict fallback;
- archive-on-lookup defaults to enabled and asks all live enrichment connectors supporting the observable type, not an explicitly selected GTI/VT connector;
- primary organization and default markings are explicitly put on the persisted verdict, but propagation to the observable, derived entities, relationships, notes and files is unproven;
- no explicit Authorized Members assignment was found in the reputation persistence path;
- the “Vendor Service User” is synthesized from the caller, not independently provisioned as a least-privilege service account;
- quota coordination, concurrency control, telemetry/SLOs, secret rotation, e2e authorization, migration and N/N+1 upgrade behavior remain unproven.

These are hardening tasks, not reasons to discard the implementation.

### 2.2 Experimental custom-fields baseline

Custom fields support integer, string/Markdown, boolean, date, select and multi-select definitions with an admin UI and entity placement. Export flattens values into the OpenCTI STIX extension as `x_opencti_cf_*` properties. The `unflattenStixToCustomFieldValues` utility has unit tests, but no production ingestion caller was found; unknown definitions are deliberately skipped.

Use custom fields as the first Patchwork authoring proof of concept, not as an assumed solution. Enable `CUSTOM_FIELDS`, define required fields, import an external bundle, display/edit/filter values, export, re-import and compare semantics. If import wiring or nested Patchwork semantics fail, keep the normative extension in an adapter/sidecar and use custom fields only as a UI/search projection.

## 3. Decisions required before implementation

| Decision | Proposed default | Required evidence |
| --- | --- | --- |
| Release 1 meaning | Feed import + Patchwork data fidelity + GTI-aligned workflows; no general GTI API facade | Approved supported/unsupported matrix and named user journeys. |
| Platform baseline | Rebase onto a clean tagged OpenCTI release; carry only reviewed branch commits | Green build, migration plan, upstream-diff inventory and N/N+1 test. |
| Connector | Pin an exact Google TI connector image/tag | Source review, emitted-bundle fixtures, quota/retry behavior and version contract. |
| Data authority | GTI facts stay GTI-attributed; Patchwork judgments are separate and namespaced | Fixtures prove creators, markings and assertions do not collapse. |
| Tenancy | Single organization for the pilot; decide soft segregation versus separate instances before expansion | Existence-leak, relationship, attachment, export and service-account tests. |
| Custom fields | Run the native PoC first; retain a sidecar fallback | Import/edit/filter/export/re-import proof, including unknown definitions. |
| Reputation keys | Centrally governed credentials or tightly controlled per-user BYOK | Rotation/revocation, quota ownership, audit and threat-model decision. |
| Archive behavior | Default off until policy propagation and connector selection are proven | Explicit targeting, handling tests and user-visible configuration. |
| Redistribution | No automatic TAXII/public-dashboard redistribution of licensed GTI content | Written entitlement, retention, recipient and export-policy decision. |
| UI implementation | Configure existing OpenCTI/FDS surfaces before adding components | UAT gap list justifying every extension. |

## 4. Target architecture

```text
Authorized GTI API / STIX endpoints
               │
               ▼
 pinned Google TI connector or source client ─── quota / retry / checkpoint
               │
               ├── restricted raw reference or checksum
               ▼
 canonical source envelope + versioned mapping
               │
               ▼
 identity / licence / marking gate ───────────── quarantine + review
               │
               ▼
 isolated staging OpenCTI ─── reconciliation ─── production OpenCTI
       │                                               │
       │                         ┌─────────────────────┼──────────────────┐
       ▼                         ▼                     ▼                  ▼
 reputation (hardened)      existing search/UI   TAXII/streams     optional API facade
                            + Patchwork fields   policy-filtered   (later, scoped)
```

Architecture rules:

1. Stage and reconcile before production; neither connector nor UI is the security boundary.
2. Key imports by `(source_system, source_object_id)`; preserve original ID, time, type, creator, source/checksum, component versions, markings and licence policy.
3. Apply identity, provenance and handling decisions before the production queue, where an unsafe upsert may already have merged objects.
4. Keep GTI facts, Patchwork assessments and manual equivalence decisions separately attributed and reversible.
5. Fail closed on missing policy, invalid required fields, identity collision or unrecognized normative extension data.
6. Use GraphQL/modules internally and STIX/TAXII for exchange. Never expose GraphQL shapes as a portable compatibility contract.
7. Maintain a small, reviewable patch set and an upstream-contribution path.

## 5. Data and serialization contract

### 5.1 Canonical source envelope

Every ingested object needs an envelope independent of its normalized STIX form:

| Field group | Required values |
| --- | --- |
| Origin | `source_system`, `source_endpoint`, `source_object_id`, `source_type` |
| Time | `source_created`, `source_modified`, `retrieved_at` |
| Raw reference | `raw_media_type`, `raw_sha256`, `raw_payload_ref`, subject to licence policy |
| Policy | creator identity, markings, Authorized Members decision, licence/retention class |
| Reproducibility | connector, mapper, schema and Patchwork profile versions |
| Operations | run ID, checkpoint, status, retries and reconciliation result |
| Honesty | warnings, information loss, unsupported fields and quarantine reason |

Do not store credentials, paid reports or licensed raw payloads in this repository.

### 5.2 Representations

| Representation | Role | Release 1 rule |
| --- | --- | --- |
| GTI native JSON | Source fidelity | Validate the supported subset and retain a controlled raw reference; never call it STIX. |
| GTI STIX | Exchange where supported | Validate identities, extensions, relationships and pagination metadata. |
| Canonical STIX 2.1 | Golden-test and adapter format | Deterministic serialization and semantic round-trip comparison. |
| Patchwork STIX profile | Patchwork classifications and attribution | Fixed extension-definition ID/version and governed vocabularies. |
| OpenCTI GraphQL | Internal application contract | Version-specific; never promise portability. |
| TAXII/stream output | Policy-filtered sharing | Preserve or explicitly project markings, provenance and supported extensions. |
| GTI-shaped REST | Optional future product | OpenAPI and explicit per-field/endpoint compatibility. |

A field is supported only after the applicable path passes:

```text
source → validate → normalize → serialize → OpenCTI import → query/filter
       → UI display/edit policy → export → re-import → semantic comparison
```

Semantic equality, not byte equality, is the round-trip criterion. Expected projections and losses belong in a machine-readable compatibility report.

### 5.3 Identity and first mapping register

The audited OpenCTI identifier logic currently uses:

| OpenCTI type | Identity contribution | Patchwork/GTI action |
| --- | --- | --- |
| `report` | normalized `name + published` | Preserve source ID; test updates, same-title reports and timestamp precision. |
| `incident` | normalized `name + created` | Patchwork wants `name + observed_date`; prove a deterministic projection or isolate with a source registry. An extension does not change the OpenCTI ID. |
| `campaign` | normalized name | Treat same-name cross-source records as collision candidates. |
| `intrusion-set` | normalized name | Isolate GTI actors from Patchwork Cluster/Temporary/Mature tiers until reviewed. |
| `malware` | normalized name | Keep aliases disabled until collision tests pass; preserve family/tool semantics. |
| threat-actor group | normalized `name + inner type` | Keep Patchwork persona meaning explicit; do not silently convert tiers/personas. |

Initial mappings:

| Source concept | Target proposal | Release gate |
| --- | --- | --- |
| GTI report/type | OpenCTI report plus retained original type; map to Patchwork `report_types` only when explicitly equivalent | Catalog, attachment, source-ID, marking and update tests pass. |
| GTI actor | Follow the pinned connector's emitted type while retaining original type/ID | No merge with a Patchwork tier/persona without evidence-backed review. |
| Campaign, malware, tool, vulnerability, ATT&CK | Corresponding OpenCTI objects/relationships | Direction, external ID, creator, lifecycle and missing-edge tests pass. |
| Domains, IPs, URLs and files | Observables; indicators only when source semantics justify them | Canonicalization, pattern, score, false-positive, merge and export tests pass. |
| Patchwork MAI | Incident plus dated observation/source grading | Same-named observations on different dates remain recoverable and attributable. |
| Patchwork attribution ladder/persona | Separate linked objects with reversible review decisions | Required self-type `part-of` behavior imports, displays, filters and re-exports, or a documented reversible projection is used. |
| Patchwork classification | Normative extension plus optional custom-field projection | All fields, including list-valued `intent`, round-trip without silent omission. |
| TLP/provenance/licence | Markings, creator, organizations/Authorized Members and export policy | Restricted users cannot discover entity, edge, attachment or count. |

Names and aliases are matching signals, never proof of identity. Preserve revocation/deletion without erasing analyst relationships, reject out-of-order updates, and record reviewer/evidence/time/undo for every manual equivalence.

## 6. UI and analyst workflow

Extend the existing OpenCTI UI rather than creating a new shell.

| Release 1 experience | Existing building block | Work required |
| --- | --- | --- |
| Landing/landscape | Dashboards and public dashboards | Configure intelligence and ingest/review widgets; keep public dashboards disabled for licensed data by default. |
| Universal search | `opencti-front/src/private/components/Search.tsx` | Add provenance/mapping facets only if missing; test permission-safe counts/snippets. |
| IoC/reputation | Reputation workspace and observable tab | Fix build, harden credentials/archive/policy, and add partial/quota/offline states. |
| Entity/report views | Existing routes and overview-layout customization | Add Patchwork/source sections, mapping warnings, export preview and read-only imported values. |
| Investigation | Existing investigation graph | Add evidence chronology, reversible identity decisions, time/policy filters and safe export. |
| Saved views and alerts | Custom views, triggers and notifications | Configure tracked entities/searches; test ownership, sharing and leakage. |
| Patchwork authoring | Custom fields, forms, workflows and reports | Run native PoC; add the smallest FDS-based module only for unmet semantics. |
| Operator view | Connector/ingestion administration plus mapping telemetry | Show tag, checkpoint, quota, lag, errors, quarantine, mapping version and reconciliation. |

Imported transformation-owned values are read-only. Analyst corrections create separately attributed assessments or explicit mapping decisions. Target WCAG 2.2 AA, keyboard access, responsive layout and explicit loading, empty, partial, rate-limit and error states. Use the Filigran Design System for frontend additions where components exist.

## 7. Security, governance and operations

Release 1 must prove:

- least-privilege human, connector and provider execution identities;
- encryption, rotation, revocation and non-disclosure of provider secrets;
- quota ownership and prevention of uncontrolled parallel vendor calls;
- marking, organization and Authorized Members propagation to every derived object, edge, note, file and export;
- absence of existence/count leaks through search, dashboards, graph, GraphQL, TAXII and streams;
- safe endpoint handling, egress allow-listing and SSRF controls;
- licence, retention, download and redistribution enforcement;
- audit events for credentials/configuration, mapping, quarantine, merge and export;
- backup/restore, replay, rollback and platform/connector N/N+1 upgrades;
- metrics for freshness, errors, 429/quota, cache, queue lag, quarantine and reconciliation drift.

Organization segregation is a shared-graph control, not hard multitenancy. Use separate instances if tests require hard isolation.

## 8. Delivery phases and gates

| Phase | Estimate | Deliverable | Exit gate |
| --- | --- | --- | --- |
| 0. Stabilize and freeze contract | 1–2 weeks | Clean release baseline; reputation parse/build fix; branch diff; edition/rights/tenancy decisions; connector tag; 20+ fixtures; custom-field and identity spikes | Green focused tests/typecheck; signed matrix; no rights blocker; spike results recorded. |
| 1. Secure platform foundation | 1–2 weeks | Reproducible staging; roles, markings, organizations, service identities, secrets, backups; configured TAXII/streams/dashboards | Access matrix, restore, rotation and leakage tests pass; identities are least privilege. |
| 2. GTI ingestion pilot | 2–3 weeks | Pinned external connector/client; narrow reports/IoCs window; source envelope; quota/checkpoint metrics and reconciliation | Repeat/restart/quota tests are idempotent; bundles captured; policy holds; no unexplained merge. |
| 3. Semantic/serialization layer | 2–4 weeks | Mapping register; source-ID registry; identity/marking/licence gate; Patchwork extension/custom-field projection; quarantine | Golden corpus passes import/query/export/re-import with zero silent required-field/policy loss. |
| 4. Analyst workflow | 2–3 weeks | Configured dashboards/search/views/alerts/investigation; hardened reputation; Patchwork authoring and operator telemetry | Five analysts complete critical tasks; provenance, access, accessibility and performance pass. |
| 5. Production hardening | 2–4 weeks | Load/security/e2e/upgrade suites; migration rehearsal; SLOs, alerts, runbooks, training and rollback | Signed reconciliation, restore/rollback and N/N+1 rehearsal; no open P0/P1 defect. |

With a stable four-to-six-person team and parallel work, target **6–9 weeks for a narrow pilot** and **10–16 weeks for production Release 1**. These are planning ranges. Estimate a GTI-shaped API, large backfill, hard multitenancy, hunting/sandbox parity, ASM, DTM or AI separately.

Do not advance while build health, identity, marking, provenance, licence or silent-data-loss gates are open.

## 9. Prioritized backlog

| Epic | Priority | Deliverable | Acceptance evidence |
| --- | --- | --- | --- |
| REP-001 Branch stabilization | P0 | Parse/typecheck fixes, tests and clean rebase | Clean build; focused suite passes; reviewed diff. |
| GOV-001 Scope and rights | P0 | Entitlements, retention, redistribution and ownership | Approved decision and data-flow diagram. |
| ARC-001 Platform ADRs | P0 | Version, edition, hosting, tenancy, patch/upstream and connector decisions | ADRs include alternatives and rollback. |
| SEC-001 Policy propagation | P0 | Markings/org/Authorized Members rules for all derived content | Cross-user leakage suite passes across UI/API/export. |
| SEC-002 Provider credentials | P0 | Key model, rotation, quota and egress controls | Rotation/revocation and secret-leak tests pass. |
| DATA-001 Compatibility register | P0 | Machine-readable object/field/relationship/status/loss map | Every Release 1 field has owner, fixture and status. |
| DATA-002 Source registry | P0 | Envelope, bidirectional IDs, lifecycle and reconciliation | Collision, replay, out-of-order and undo tests pass. |
| DATA-003 Patchwork STIX | P0 | Extension, vocabularies, examples and validator rules | Independent validation and semantic round-trip pass. |
| DATA-004 Custom-fields PoC | P0 | Definition, import wiring, form/filter and round-trip proof | No silently skipped normative value; fallback recorded. |
| ING-001 GTI connector pilot | P0 | Pinned connector, narrow scope and quota/checkpoint telemetry | Restart, 429, 5xx, malformed and repeat-import tests pass. |
| ING-002 Policy gate | P0 | Identity, marking, licence/schema checks and quarantine | Invalid/ambiguous data fails closed and is replayable. |
| REP-002 Reputation hardening | P0 | Targeted archive, safe default, real service identity, fallback semantics and integration tests | Vendor failure, cache, quota, policy, audit and auth tests pass. |
| UI-001 Analyst configuration | P0 | Dashboards, search, layouts, custom views and alerts | Exportable config and UAT evidence. |
| UI-002 Patchwork workflow | P0 | Authoring, evidence, mapping review and export preview | Fields/relationships round-trip without altering source facts. |
| UI-003 Investigation | P1 | Time/evidence/policy graph and reversible decisions | UAT, permission and performance tests pass. |
| OPS-001 Deployment/observability | P0 | IaC, secrets, metrics, alerts, SLOs and runbooks | Fresh staging build and failure/quota game day pass. |
| OPS-002 Recovery/upgrades | P0 | Backup, restore, rollback and N/N+1 matrix | Timed rehearsal passes with reconciliation. |
| QA-001 Golden corpus/CI | P0 | 20+ fixtures and compatibility report | CI blocks silent loss, merge and policy regressions. |
| API-001 GTI facade | P2 | Consumer-approved subset and OpenAPI | Named need, contract tests and explicit incompatibilities. |

P0 is required for Release 1. P1 may land in Release 1.1. P2 requires a separate product decision.

## 10. Acceptance and quality objectives

Required suites:

1. **Build/migration:** lint, typecheck, focused unit/integration, schema generation, migrations and clean install.
2. **Contract/data:** GTI native subset, STIX 2.1, absent/unknown fields, Unicode/timestamps/enums, Patchwork extensions and semantic re-import.
3. **Identity/lifecycle:** repeat/out-of-order import, update, revoke/delete, source-ID resolution, report `name + published`, actual incident `name + created`, Patchwork `name + observed_date`, actor/malware collisions and reversible equivalence.
4. **Reputation:** normalization, timeout/429/quota, cache/reanalyze, key isolation/rotation, archive-off default, explicit connector selection, actual offline semantics and no credential leakage.
5. **Security:** markings, organizations, Authorized Members, object/edge/file visibility, direct access, search/count leakage, service identities, TAXII/stream/export and public dashboards.
6. **UI:** analyst journeys, permission states, accessibility, keyboard/screen reader, responsive layout, partial/error/quota behavior and upgrade smoke tests.
7. **Reliability:** representative load, checkpoint/replay, connector/platform outage, backup restore, rollback and N/N+1 upgrade.

Initial objectives, calibrated after volume testing:

- 100% of Release 1 fields and relationships in the compatibility register.
- 100% of accepted objects carry source identity, mapping version and policy outcome.
- Zero silent required-field, marking, provenance, licence or relationship loss.
- Zero unintended identity merges in regression tests.
- At least 99.5% successful processing of valid in-scope objects, excluding quarantine.
- Agreed p95 source-to-search freshness, with quota pauses reported separately.
- 100% replayability from a checkpoint and retained raw reference/checksum.
- No open P0/P1 security, build or data-integrity defect at production release.
- Five pilot analysts complete critical scenarios without a critical accessibility issue.

An epic is done only when its contract status, implementation, migrations, authorization, observability, documentation, rollback and compatibility fixtures are complete.

## 11. Deferred and missing features

| Capability | Release decision |
| --- | --- |
| Full GTI API behavior | Deferred; define a subset only for a validated consumer. |
| YARA/Livehunt/Retrohunt and sandbox control plane | Integrate/deep-link existing services first; decide after Release 1. |
| Attack Surface Management | Release 2 at earliest; requires a separate asset/collector model. |
| Digital Threat Monitoring/dark web | Release 2 at earliest after legal/collection review. |
| AI/agentic analysis | Deferred until citation, evaluation, privacy and authorization controls exist. |
| Proprietary GTI scoring/search/graph parity | Non-goal; map only documented, licensed fields and behavior. |
| Hard multitenancy in one graph | Non-goal; use separate instances when hard isolation is required. |

## 12. First 30 days

### Week 1 — make the baseline trustworthy

- Fix the reputation parse error in a dedicated implementation task and obtain green typecheck/tests.
- Choose a clean OpenCTI release base; inventory branch commits to carry, upstream or discard.
- Name product, CTI, security, platform, QA and GTI account/legal owners.
- Approve Release 1 compatibility levels, non-goals and rights constraints.

### Week 2 — freeze contracts and fixtures

- Select the Google TI connector release and capture representative emitted bundles.
- Build 20+ authorized/redacted fixtures covering collisions, markings, updates, revocation and malformed input.
- Create the machine-readable compatibility register and source-envelope schemas.
- Threat-model per-user keys, archive-by-default, synthetic provider users and cross-organization behavior.

### Week 3 — retire the highest risks

- Run the `CUSTOM_FIELDS` import/edit/filter/export/re-import spike.
- Test report, incident, actor and malware identity against the real identifier implementation.
- Test marking, organization and Authorized Members over a complete reputation/connector-derived subgraph.
- Prove or reject Patchwork `intrusion-set` `part-of` and extension round-trips.

### Week 4 — start the controlled pilot

- Deploy reproducible staging with least-privilege accounts, backups and telemetry.
- Run a narrow reports/IoCs connector window with quota/checkpoint/reconciliation reporting.
- Configure dashboard, search/entity layouts, investigation and reputation from existing UI.
- Publish spike results, unsupported behavior, revised estimates and backlog; proceed only if build, rights, identity and policy gates pass.

## 13. Audited source evidence

Key OpenCTI paths, relative to `/workspaces/OpenCTI`:

- STIX/identity: `opencti-platform/opencti-graphql/src/database/stix-2-1-converter.ts`, `src/schema/identifier.js`.
- TAXII/feeds: `src/modules/ingestion/ingestion-taxii-collection.ts`, `src/modules/dataSharing/taxiiCollection-domain.ts`, `src/http/httpTaxii.js`.
- Custom fields: `src/modules/customField/`, frontend `settings/custom_fields/`, `EntitySettingCustomFields.tsx`, and `src/config/conf.js`.
- Reputation: `src/modules/reputation/`, frontend `workspaces/reputation/`, and `tests/01-unit/modules/reputation/`.
- Existing UI: frontend `Search.tsx`, `workspaces/dashboards/`, `workspaces/investigations/`, `custom_views/`, alerts/triggers and overview layouts.
- Branch notes: `docs/GTI_SANDBOX_STIX_STANDARD.md`, `docs/VIRUSTOTAL_MALWARE_REPORT_PLAN.md`, `docs/reputation-feature-plan.md`.

External material to revalidate at implementation time:

- OpenCTI documentation: https://docs.opencti.io/latest/
- Google TI connector: https://github.com/OpenCTI-Platform/connectors/tree/master/external-import/google-ti-feeds
- GTI STIX responses: https://gtidocs.virustotal.com/reference/stix-responses
- GTI report types: https://gtidocs.virustotal.com/docs/report-types
