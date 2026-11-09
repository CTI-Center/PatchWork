> [!NOTE] About this template — Annual Threat Landscape (optional net-assessment profile)
> **Use this when:** producing a retrospective annual or other explicitly bounded threat-landscape assessment for a defined constituency. This is a Markdown presentation profile of [Net Assessment](net-assessment.md), not a new report type, wire schema, ENISA compliance claim or replacement for the core framework.
>
> **Source-derived structure:** ENISA's annual Executive Summary, Methodology, Overview & Trends, Sectoral Analysis, Cybercrime, State-Nexus, FIMI, Hacktivist Threats, Vulnerabilities, Outlook and appendices. See the [page-cited source outline and field dictionary](../Easy-access/ENISA/enisa-threat-landscape-2026-schema.md) for the exact mapping and source issues. Sector choices, observed actors, statistics and rankings are deliberately **not prefilled**.
>
> **Adaptations:** purpose/questions, reproducibility ledgers, explicit Recommendations, release/review/feedback logs and operational owners are methodology-backed/Patchwork additions, not claims that these are annual PDF chapters. What-changed, object references and stable period-start identity come from the base net-assessment.
>
> Picker: [Report Types](../Report-Types.md) · [Vocabularies](../Vocabularies.md) · [Sectors](../Sectors.md) · [Framework](../Patchwork-CTI-Framework.md) · [Publication checklist](../Publication-Checklist.md).
>
> Copy and complete the tables; repeat profiles/rows as needed. Blank cells are intentional. Replace all prompts before release; use “unknown,” “not collected” or “not applicable — reason” for unsupported dimensions, not zero. Retain scope/gap disclosures when omitting an unsupported chapter. Remove these guidance callouts from the completed report.

# `<Member namespace>-<Title>`-—-Annual-Threat-Landscape

## Table-of-contents

> [!TIP] Refresh this navigation after completing the report.
> When repeating sector/threat profiles or omitting unsupported sections, update this list and verify every generated heading link before publication.

- [Report metadata](#report-metadata)
- [Key judgments](#key-judgments)
- [Purpose and requirements](#purpose-and-requirements)
- [Period covered](#period-covered)
- [Methodology and limitations](#methodology-and-limitations)
  - [Collection and processing](#collection-and-processing)
  - [Corpus and denominator register](#corpus-and-denominator-register)
  - [Evidence and assessment practice](#evidence-and-assessment-practice)
  - [Limitations and tool use](#limitations-and-tool-use)
- [Overview and top threats](#overview-and-top-threats)
- [Sectoral analysis](#sectoral-analysis)
  - [Sector profile](#sector-profile)
- [Threat analysis](#threat-analysis)
  - [Cybercrime](#cybercrime)
  - [State nexus](#state-nexus)
  - [FIMI](#fimi)
  - [Hacktivism](#hacktivism)
  - [TTP evidence matrix](#ttp-evidence-matrix)
- [Vulnerabilities](#vulnerabilities)
- [What changed](#what-changed)
- [Outlook and conclusion](#outlook-and-conclusion)
- [Recommendations](#recommendations)
- [Objects referenced](#objects-referenced)
- [Sources](#sources)
- [Publication review and feedback](#publication-review-and-feedback)
- [Optional response and disruption annex](#optional-response-and-disruption-annex)

## Report-metadata

| Field | Value | Completion guidance |
| --- | --- | --- |
| Report Type | net-assessment | Emit the existing report_types value only; “annual-threat-landscape” is a template/profile label, not a new enum |
| Title | | Prefix with the member's stable namespace; distinguish editions |
| Edition / version | | Publication edition label, not necessarily the activity year |
| Published | | **Stable identity anchor: first day of the period covered**, per the base template and framework §9.2; do not change on revision |
| Actual release date | | Real dissemination date, separate from the Published anchor |
| Last revised | | Date/version of this revision; record material changes below |
| Publisher / author | | Member identity; author maps to created_by_ref |
| Contributors / acknowledgements | | Roles and permission to identify contributors |
| TLP / handling restrictions | | Use current core marking values and handling rules; do not inherit the source's marking automatically |
| Source Reliability / Info Credibility | | Report-level sourcing summary if useful; never replace grading of individual observations |
| Threat level | | Core High / Medium / Low urgency/proximity, **not** confidence or ENISA EU relevance |
| Threat domain | | Core Constituency / National / Regional / Partner / World; highest applicable rung |
| Activity category | | One or more existing §5.2 values, not the chapter titles below |
| Observed date | | Required on each incident observation under core rules; annual period is not an incident observed_date |
| Contact / feedback channel | | Responsible team and accessible channel |
| Rights / attribution | | Own content licence and third-party credits; do not imply ENISA authorship/endorsement |

> [!TIP] Compatibility
> This profile adds narrative tables only. Use the [existing classification properties](../Patchwork-CTI-Framework.md#93-classification-properties), [observation-level grading](../Patchwork-CTI-Framework.md#71-admiralty-grading-attaches-to-the-observation) and [identity rules](../Patchwork-CTI-Framework.md#92-identity-and-merge-rules); no automatic serialisation is promised for these additional fields. Keep occurrence/observation, source publication, collection, inclusion cutoff and release dates distinct.

## Key-judgments

> [!TIP] Source-derived: annual Executive Summary, pp. 7–8; methodology [analysis](../Easy-access/ENISA/enisa-ctl-methodology-2026.md#252-performing-analysis).
> Give 3–5 decision-relevant judgments. Separate source-reported facts from your assessment; link evidence and identify uncertainty. Do not equate likelihood of an outcome with confidence in your evidence or with urgency.

| ID | Judgment / implication for this audience | Evidence / metric IDs | Assessment confidence and rationale | Alternative / key gap |
| --- | --- | --- | --- | --- |
| | | | | |

## Purpose-and-requirements

> [!TIP] Methodology-backed adaptation: [purpose](../Easy-access/ENISA/enisa-ctl-methodology-2026.md#221-establish-ctl-purpose), [audience](../Easy-access/ENISA/enisa-ctl-methodology-2026.md#222-define-audience), [intelligence requirements](../Easy-access/ENISA/enisa-ctl-methodology-2026.md#223-define-intelligence-requirements).
> Name the constituency, geography, intended decisions, strategic/tactical/operational readers, covered assets/sectors and exclusions. EU scope is source-specific, not mandatory for every Patchwork member. If recording an EU-relevance score, define its contextual purpose separately from core threat level and confidence.

| Purpose / intended decision | Audience | Geographic / constituency scope | Included assets and sectors | Exclusions / rationale |
| --- | --- | --- | --- | --- |
| | | | | |

| Requirement ID | Stakeholder question | Collection requirement / source classes | Answer location / finding ID | Owner / unresolved gap |
| --- | --- | --- | --- | --- |
| | | | | |

## Period-covered

> [!TIP] Source-derived: annual Methodology pp. 9–10; local identity convention from [base Period-covered](net-assessment.md#period-covered).
> State exact endpoints, timezone and inclusive/exclusive convention. Define the date that determines eligibility: occurrence, discovery, reporting or recording. Explain earlier activity reported within the window, uncertain dates, late reports, revisions, and overlap with previous editions. Do not infer the observation year from the edition label. Published stays anchored to period start even if an in-window source describes earlier activity; document that earlier activity separately.

| Period start | Period end | Timezone / boundary convention | Inclusion-date basis | Treatment of earlier activity / late reporting |
| --- | --- | --- | --- | --- |
| | | | | |

| Collection start/end | Inclusion cutoff / evidence freeze | Dataset version | Prior edition and overlap | Exceptions / dataset-specific cutoffs |
| --- | --- | --- | --- | --- |
| | | | | |

## Methodology-and-limitations

### Collection-and-processing

> [!TIP] Source-derived: annual pp. 9–10; methodology [collection plan](../Easy-access/ENISA/enisa-ctl-methodology-2026.md#231-define-collection-plan), [validation](../Easy-access/ENISA/enisa-ctl-methodology-2026.md#232-validate-sources), [processing](../Easy-access/ENISA/enisa-ctl-methodology-2026.md#24-processing).
> Describe source classes, languages, coverage, selection/exclusion, corroboration, deduplication, sector assignment, claim validation and analytical method. Preserve source labels alongside canonical mappings. Show what you cannot know; OSINT/voluntary reporting is not a complete population. Recording more reports does not establish more underlying activity.

| Dataset ID | Source classes / languages | Collection and selection rules | Unit of analysis | Dedup / overlap / sector assignment rules | Coverage and bias |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

### Corpus-and-denominator-register

> [!TIP] Explicit ledger is a Patchwork reproducibility addition, grounded in annual pp. 9–12, 18–19, 60 and 74.
> Maintain **separate populations** for collected incidents, actor claims, confirmed cases, regulatory events, FIMI incidents/channels/observables and vulnerability disclosures/known-exploited subsets. Define whether a multi-victim campaign counts once or by victim. Explain retractions, repeated claims and cross-category overlap; do not sum overlapping categories as disjoint.

| Corpus ID / version | Scope / period / cutoff | Unit | Eligible N | Known / unknown / excluded counts | Inclusion and dedup rule | Evidence / caveat |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

| Metric ID | Description / population filter | Corpus ID | Numerator n | Denominator N / known subset | Value / unit / rounding | Missingness / overlap / reproducible calculation |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

For a known-vector percentage, identify both **known-vector cases / eligible cases** (coverage) and **vector-specific cases / known-vector cases** (distribution). A subset percentage must never be presented as a share of all incidents. If the denominator cannot be established, label it unknown and restrict the claim; do not reverse-engineer exact counts from rounded percentages. Give every chart a unique metric/figure ID, caption, corpus, filter and source locator.

### Evidence-and-assessment-practice

> [!TIP] Source-derived distinction between reporting and assessment: annual pp. 10, 100. Methodology [source confidence](../Easy-access/ENISA/enisa-ctl-methodology-2026.md#2321-source-confidence-level) and [performing analysis](../Easy-access/ENISA/enisa-ctl-methodology-2026.md#252-performing-analysis).
> Record source reliability A–F and information credibility 1–6 **per observation**, following the core lookup for event confidence. Explain analytical confidence and likelihood wording separately; ENISA Appendix B's percentage bands are not a conversion to Admiralty or STIX confidence. Identify assumptions, alternatives and unresolved conflicts. A repeated source is not independent corroboration.

| Evidence ID / observation ref | Claim / fact observed | Source ID / exact locator | Observed / occurred date and uncertainty | Source publication / collection dates | Reliability / credibility and rationale | Claimed / corroborated / confirmed / disputed |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

### Limitations-and-tool-use

| Limitation / gap | Affected metrics or judgments | Likely bias / consequence | Mitigation / residual uncertainty |
| --- | --- | --- | --- |
| | | | |

| Tools / AI assistance actually used | Permitted task / input handling | Human validation / responsible analyst | Residual error / disclosure |
| --- | --- | --- | --- |
| | | | |

> [!TIP] Be truthful about AI use.
> The annual report's p. 4 declaration describes that report, not yours. Do not copy its “no AI-generated content” assertion into an AI-assisted product. Under [methodology §2.4.7](../Easy-access/ENISA/enisa-ctl-methodology-2026.md#247-use-of-ai-supported-tools), AI may assist defined monitoring, collection and limited editorial tasks, but human analysts identify trends, draw conclusions and approve assessments. Document evidence verification and analytical accountability, including revalidation of any AI-assisted draft. Never upload restricted evidence without authorisation.

## Overview-and-top-threats

> [!TIP] Source-derived: annual chapter 1 pp. 11–17; ranking retained from base net-assessment.
> Summarise incident types, objectives, intrusion vectors, dependencies and impact. State what “top” measures (volume, observed impact, urgency or another justified metric). A claim-volume ranking is not a ranking of verified harm, unique victims or real-world prevalence. Explain ties, unknown/unranked cases, and the ranked population.

| Rank / tie policy | Threat / activity | Actor / family if evidenced | Metric ID / corpus | Why ranked / impact | Prior reports / evidence | Unknowns |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

| Cross-cutting trend / dependency | Supporting observations and metrics | Constituency consequence | Alternative explanation / gap |
| --- | --- | --- | --- |
| | | | |

## Sectoral-analysis

> [!TIP] Source-derived: annual chapter 2 pp. 18–37; method [taxonomy](../Easy-access/ENISA/enisa-ctl-methodology-2026.md#243-cyber-threat-taxonomy). Repeat for sectors actually supported by this edition, **not** a frozen top five.
> Use [Patchwork sectors and source-label crosswalks](../Sectors.md). Distinguish targeted from impacted, subsectors, primary-sector assignment, multi-sector spillover and unknown sectors. Compare regulatory-event and OSINT datasets side by side with their own units, thresholds and denominators; never pool them merely because both refer to the same year.

| Source sector / subsector | Patchwork canonical mapping / mapping caveat | Corpus / metric IDs | Targeted / confirmed impact | Principal threats / objectives | Geographic and dependency context | Evidence / gaps |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

### Sector-profile

| Selected sector | Scale / denominator | Relevant actors / threats / TTPs | Representative evidence | Effect on services / assets | Comparison and uncertainty |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

## Threat-analysis

> [!TIP] Source-derived: annual chapters 3–6. Use the common table for each retained family, then add family-specific analysis below. If evidence is absent, state the collection gap rather than claiming no threat. Chapter labels are analytical groupings, not new activity-category or actor-type values.

| Threat family / profile | Types and assessed objectives | Corpus / metrics / ranking basis | Actors / campaigns / malware and attribution basis | Sectors / geography / impact | TTPs and enabling vulnerabilities | Evidence / limitations |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

### Cybercrime

> Annual pp. 38–59: distinguish fraud/impersonation, data breaches and ransomware deployments; describe their overlap, claims vs validation, tempo, service ecosystems, repeat victimisation and response/disruption context. Do not equate a leak-site listing with a confirmed unique incident. Fill the common table and add supported narrative here.

### State-nexus

> Annual pp. 60–73: report source-attributed nexus and its evidentiary limits, unknown attribution, intrusion sets, objectives, sectoral targeting and TTP evolution. Follow [technical attribution doctrine](../Patchwork-CTI-Framework.md#45-attribution-doctrine); reported nexus is not proof of state responsibility, a mandatory political judgment or permission to merge actor aliases. Fill the common table and add supported narrative here.

### FIMI

> Annual pp. 74–82: optional specialised profile. Identify the contributing report/dataset, time/geographic scope, incident definition, attribution/IMS, channels/platforms, observables, objectives and targeting patterns. Distinguish the contributing analyst's assessment from yours and link licensing/provenance. A global external FIMI corpus is not the same population as constituency cyber incidents; never add its counts to unrelated totals.

| Contributing corpus / reference | Period / geography | Units and denominators | Actors / IMS and attribution uncertainty | Channels / platforms / observables | Objectives / patterns | Evidence / gap |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

### Hacktivism

> Annual pp. 83–89: distinguish ideological claims from independently verified disruption/intrusion, including OT effects. Document actor coordination, political-event timing, sector/geographic patterns and claimed vs confirmed capability. Co-occurring claims do not establish collaboration or shared identity. Fill the common table and add supported narrative here.

### TTP-evidence-matrix

> Annual p. 53 Figure 42 and pp. 69–73; method [CTI frameworks](../Easy-access/ENISA/enisa-ctl-methodology-2026.md#244-cti-frameworks). Record actual procedure evidence before mapping to ATT&CK. Specify technique/sub-technique ID and version; a broad vendor label alone is insufficient.

| Procedure observed | ATT&CK ID / name / version | Actor / campaign / threat family | Evidence / date | Frequency corpus / known coverage if quantified | Detection / defensive implication | Mapping uncertainty |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

## Vulnerabilities

> [!TIP] Source-derived: annual chapter 7 pp. 90–94 and chapter 4 Table 1 p. 71.
> Separate newly disclosed vulnerabilities, known-exploited catalogues and exploitation evidenced within your constituency. State retrieval/as-of dates, score version, unknowns and data-source changes. CWE/vendor/CVSS distributions need their own corpus and denominator; vendor disclosure counts are not a measure of comparative product insecurity. Distinguish severity from exploitation probability and actual impact.

| Corpus / version / as-of | Inclusion / disclosure period | Unit / eligible N / unknowns | Metric IDs: severity, vectors, CWEs, vendors | Known-exploited subset and evidence limits |
| --- | --- | --- | --- | --- |
| | | | | |

| CVE / EUVD / other ID | Product / vendor | Disclosure date | CVSS score / version / vector; CWE | Exploitation evidence / geography / date | KEV status / as-of | Action / advisory / evidence |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

## What-changed

> [!TIP] Patchwork base section; source methodological support pp. 9–10.
> Compare like populations and non-overlapping periods where possible. Identify temporal overlap, new collection sources, wider coverage, changed taxonomy/deduplication and delayed reporting before interpreting growth. Mark “not comparable” with reasons instead of manufacturing trend percentages. Describe entries/exits from rankings and changed character even when rank is stable.

| Prior edition / metric | Current edition / metric | Period overlap / methodological change | Comparable change or not comparable | Interpretation / confidence / evidence |
| --- | --- | --- | --- | --- |
| | | | | |

## Outlook-and-conclusion

> [!TIP] Source-derived: annual chapter 8 pp. 95–96; bounded outlook retained from base net-assessment.
> Explain near-term implications, horizon, assumptions, likelihood and evidence confidence separately. Identify indicators that would change the assessment. Link a dedicated [Trends Forecasting](trends-forecasting.md) report for a substantial forward-looking argument rather than turning this retrospective into one.

| Implication / horizon | Supporting findings | Assumptions / alternatives | Likelihood wording / confidence rationale | Indicators to revisit |
| --- | --- | --- | --- | --- |
| | | | | |

## Recommendations

> [!TIP] **Methodology-backed adaptation**, not an annual source chapter: [analysis and production §2.5](../Easy-access/ENISA/enisa-ctl-methodology-2026.md#25-analysis-and-production).
> Tie actions to evidenced findings and identified gaps; cite existing recommendations/controls where appropriate. Explain applicability and trade-offs. Owner, target date and success measure are local operational additions. Priority is not source reliability or a claim that a measure guarantees protection.

| Finding / gap ID | Recommended action / control reference | Intended recipient / owner | Priority rationale | Target date / success measure | Evidence / assumptions / constraints |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

## Objects-referenced

> [!TIP] Patchwork compatibility section, inherited from net-assessment.
> Reconcile narrative and report object_refs: named actors, campaigns, malware, attack patterns, vulnerabilities, relevant incidents and reports actually referenced. Reuse existing identities; keep source aliases with provenance instead of creating a merge. A named external reference is not automatically a new STIX object.

| Narrative entity / finding | Existing object ID / type | Role / evidence | Included in object_refs / reason if not |
| --- | --- | --- | --- |
| | | | |

## Sources

> [!TIP] Source-derived citations are near claims in the annual report; this central register is a usability adaptation.
> Cite primary sources wherever possible and retain page/section locators. Source IDs must resolve from the evidence ledger and analytical claims. Record access time and a permitted durable reference where practical; do not redistribute restricted or third-party evidence without permission. References to volatile forums/leak sites are evidence, not endorsements or instructions to visit them.

| Source ID | Author / title / publication date | URL / case ID / exact page or section | Access / collection date | Reliability and independence caveat | Rights / handling / availability |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

## Publication-review-and-feedback

> [!TIP] **Methodology-backed adaptation**, not an annual source chapter: [validation](../Easy-access/ENISA/enisa-ctl-methodology-2026.md#253-validate-ctl), [deliverable production](../Easy-access/ENISA/enisa-ctl-methodology-2026.md#255-deliverable-production), [dissemination](../Easy-access/ENISA/enisa-ctl-methodology-2026.md#26-dissemination), [updates](../Easy-access/ENISA/enisa-ctl-methodology-2026.md#263-post-publication-updates), [feedback](../Easy-access/ENISA/enisa-ctl-methodology-2026.md#27-feedback).
> Apply the [core publication checklist](../Publication-Checklist.md). Validate claims, denominators, aliases/attribution, taxonomy, object references, marking, rights and links. Human analysts own conclusions; peer/expert and publication approvals must be recorded. Designate the audience/channel and feedback owner before release.

| Review stage / scope | Reviewer / responsible analyst | Date | Findings / resolution / approval |
| --- | --- | --- | --- |
| | | | |

| Release version | Actual release date | Intended audience / TLP | Channel / format / location | Accountable publisher / feedback channel |
| --- | --- | --- | --- | --- |
| | | | | |

| Version / date | Editorial correction or substantive analytical update | Affected finding / nature of change | Review / notification / rationale |
| --- | --- | --- | --- |
| | | | |

| Feedback date / reference | Audience / issue / new evidence | Decision: accept, adapt or reject / rationale | Owner / action / due date | Effect on current assessment or next collection plan |
| --- | --- | --- | --- | --- |
| | | | | |

Corrections preserve the report's stable title and Published identity anchor. Clearly identify the nature/date of substantive changes and follow core retraction procedures when evidence is withdrawn. Re-check external links at release; later disappearance is a recorded availability issue, not permission to invent replacement evidence. Feed accepted gaps into the next cycle's intelligence requirements.

## Optional-response-and-disruption-annex

> [!TIP] Source-derived: Appendix A pp. 97–99. Retain only when relevant to this assessment; a temporal association after a disruption is not proof of its causal effect.

| Date | Action / operation | Reported result / impact | Countries / entities involved | Evidence / verification limits | Assessed effect / uncertainty |
| --- | --- | --- | --- | --- | --- |
| | | | | | |
