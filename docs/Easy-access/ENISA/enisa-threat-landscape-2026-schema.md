# enisa-threat-landscape-2026-schema

## table-of-contents

- [Purpose and provenance](#purpose-and-provenance)
- [Edition and period cautions](#edition-and-period-cautions)
- [Source outline and template mapping](#source-outline-and-template-mapping)
- [Reusable field dictionary](#reusable-field-dictionary)
- [Methodology links and localisation](#methodology-links-and-localisation)
- [Completion and quality gates](#completion-and-quality-gates)

## purpose-and-provenance

This is a **source-derived document outline and reusable field dictionary**, not a JSON Schema, ENISA-mandated standard, full PDF conversion, or machine-readable exchange contract. It supports the optional [annual threat landscape template](../../Report-Templates/annual-threat-landscape.md), a presentation profile of the existing [net-assessment](../../Report-Templates/net-assessment.md) report type. The [methodology](enisa-ctl-methodology-2026.md) supplies the production process; the annual report supplies one concrete presentation. Neither adds a report-type value or STIX extension property.

Source: European Union Agency for Cybersecurity (ENISA), *ENISA Threat Landscape 2026*, September 2026, supplied as “ENISA Threat Landscape 2026_Final.pdf”; ISBN 978-92-9204-807-5; DOI [10.2824/0806036](https://doi.org/10.2824/0806036). SHA-256: `f5e4575085dbb643829c6913893bc70cedc0bee9e01d155e5347b4d276d7d5e3`.

Attribution: © European Union Agency for Cybersecurity (ENISA), 2026. Source reuse is authorised under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) unless otherwise noted. Changes here: headings, structure and analytical dimensions are summarised, mapped and generalised; operational fields are added and labelled below. No annual cover artwork, figures or full PDF are reproduced. Third-party material retains its own rights; see [Third-Party Notices](../../Third-Party-Notices.md).

Inspection used local pdfinfo and pdftotext text extraction only; no external upload. The 101-page PDF was checked against its contents (pp. 5–6), chapter bodies, methodological caveats, figure captions and appendices. **Page convention:** numbered printed pages 2–100 equal their one-based PDF page numbers; cover = PDF 1 (unnumbered), back cover = PDF 101 (unnumbered). The outline below gives both, not a guessed offset.

## edition-and-period-cautions

- The cover and running headers identify **2026 / September 2026**; the Executive Summary opens with “The 2025 cyber threat landscape” (printed/PDF p. 7). These are different fields, not evidence that the edition must be renamed. Methodology explicitly defines **incidents recorded from 1 January 2025 to 31 December 2025** and a **six-month overlap with the previous ETL** (p. 9). “Recorded” must not silently become “occurred.”
- Report edition, activity/recording window, source publication dates, collection cutoff and actual release date must remain separate. The annual PDF does not provide one unambiguous report-wide collection-freeze timestamp. Do not infer it from the cover or PDF file metadata. NIS2 event data have an explicit **14 July 2026 as-of date** for 2025 events (p. 19, note 79); this is a dataset-specific cutoff, not a universal one.
- **Differing EEAS source labels:** Methodology refers to the EEAS “FIMI Threat Landscape 2025” (p. 9), while chapter 5 explicitly draws from the **EEAS 4th report, published March 2026**, analysing 1 January–31 December 2025 (p. 74, note 548). A title/activity-year label and publication year can differ legitimately; these labels alone do not prove a mistaken citation. Preserve both precise locators and verify the cited title, edition and reporting window before reuse; do not merge this distinct corpus into ENISA incident totals.
- Appendix B is headed “CONFIDENCE LEVEL / SYNONYMS” but lists estimative words and percentage bands (p. 100): HIGHLY LIKELY (>90%), LIKELY (60–90%), POSSIBLE (40–60%), PLAUSIBLE (10–40%), UNLIKELY (<10%). Preserve that source wording when describing it. Do **not** equate likelihood of an outcome with confidence in an assessment, source reliability, information credibility or STIX confidence; do not invent boundary rules where bands meet.
- Two captions on p. 93 are labelled **Figure 60** (top 25 CWEs; top 20 vendors). The same page’s prose calls the KEV vendor chart “figure 62,” but its caption is **Figure 61**. Use page + caption, not figure number alone, as a locator, and give new charts their own unique IDs. This profile does not silently renumber the source.

## source-outline-and-template-mapping

Source titles below retain their numbering and meaning (line wrapping normalised). Page ranges are derived from the next chapter/subchapter start and inspected body headings, not claims that every page has a separate heading. Template headings are generalised so future editions are not locked to this edition's sectors or rankings.

| Source section | Printed pages | PDF pages | Reusable destination / interpretation |
| --- | --- | --- | --- |
| Cover | unnumbered | 1 | Report-metadata: edition/title, marking, nominal publication month |
| About ENISA; Contact; Authors; Acknowledgements; Legal notice; Copyright notice | 2–3 | 2–3 | Report-metadata, Sources, Publication-review-and-feedback; replace agency-specific identities |
| Disclaimer | 4 | 4 | Methodology-and-limitations: tool-use and reference-availability disclosure |
| Table of Contents | 5–6 | 5–6 | Navigation for the completed report, not analytical evidence |
| Executive Summary | 7–8 | 7–8 | Key-judgments |
| Methodology | 9–10 | 9–10 | Purpose-and-requirements, Period-covered, Methodology-and-limitations, Sources |
| 1. Overview & Trends | 11–17 | 11–17 | Overview-and-top-threats; cross-cutting incident types, objectives, vectors, dependencies and emerging techniques |
| 2. Sectoral Analysis | 18–37 | 18–37 | Sectoral-analysis; dataset-specific distribution and complementary NIS2 reporting |
| 2.1 Public administration | 20–23 | 20–23 | Repeatable sector profile |
| 2.2 Business services | 24–26 | 24–26 | Repeatable sector profile |
| 2.3 Transport | 27–30 | 27–30 | Repeatable sector profile, with subsector breakdown |
| 2.4 Manufacturing | 31–33 | 31–33 | Repeatable sector profile |
| 2.5 Finance / Banking | 34–37 | 34–37 | Repeatable sector profile; body also discusses other sector concerns, not additional numbered sector chapters |
| 3. Cybercrime Threats | 38–59 | 38–59 | Threat-analysis / Cybercrime |
| 3.1 Key threats | 39–53 | 39–53 | Repeatable threat-family profiles |
| 3.1.1 Fraud and Impersonation | 39–42 | 39–42 | Financially motivated activity, claimants, schemes, actors, sectors |
| 3.1.2 Data breaches | 42–45 | 42–45 | Claims, affected geography/sectors and claim-source distribution |
| 3.1.3 Ransomware deployments | 46–53 | 46–53 | Claims, tempo, operators, geography, sectors and common TTPs |
| 3.2 Sectoral impact | 54 | 54 | Threat-specific sector slice |
| 3.3 Geographical impact | 54–55 | 54–55 | Threat-specific geographic slice |
| 3.4 Key trends | 55–58 | 55–58 | Changes in ecosystem, services, repeat victimisation and operating methods |
| 3.5 Tackling cybercrime in the EU | 59 | 59 | Response/disruption context; optional operation annex |
| 4. State-Nexus Threats | 60–73 | 60–73 | Threat-analysis / State-nexus, with attribution caveats |
| 4.1 Key threats | 60–66 | 60–66 | Reported nexus, intrusion sets, objectives, evidence and unknowns |
| 4.2 Sectoral impact | 67–69 | 67–69 | Targeted sector patterns and case evidence |
| 4.3 Key TTPs and trends | 69–73 | 69–73 | Procedures, infrastructure, vulnerabilities; Table 1 at p. 71 |
| 5. Foreign Information Manipulation & Interference (FIMI) | 74–82 | 74–82 | Threat-analysis / FIMI; explicitly separate externally supplied corpus |
| 5.1 Key threats | 74–82 | 74–82 | EEAS patterns, channels, observables, platforms, strategic objectives and targeting evolution |
| 6. Hacktivist Threats | 83–89 | 83–89 | Threat-analysis / Hacktivism; claims distinguished from confirmed effects |
| 6.1 Key threats | 83–84 | 83–84 | Claimed operations, groups, objectives and OT concerns |
| 6.2 Sectoral impact | 85 | 85 | Threat-specific sector slice |
| 6.3 Geographical impact | 85–87 | 85–87 | Geographic claims, coordination and campaign context |
| 6.4 Key trends | 88–89 | 88–89 | Evolution of methods and ecosystem |
| 7. Vulnerabilities | 90–94 | 90–94 | Vulnerabilities: disclosure corpus, scores, vectors, weaknesses, vendors, exploited subset |
| 8. Outlook and conclusion | 95–96 | 95–96 | Outlook-and-conclusion; bounded implications, not a replacement for a forecasting report |
| Appendix A Law Enforcement Authorities operations in the EU | 97–99 | 97–99 | Optional response/disruption annex: date, action, results/impact, involved countries/entities |
| Appendix B Assessment methodology | 100 | 100 | Analytical-language disclosure; do not replace Patchwork grading |
| About ENISA / office details (back cover) | unnumbered | 101 | Publisher/contact metadata, not a compulsory analytical section |

There is **no standalone Recommendations chapter, bibliography/References chapter, publication-review log or feedback chapter** in this annual PDF. References appear as numbered notes near the supporting claims (including appendices). The template's separate Recommendations, Sources register and Publication-review-and-feedback sections are explicit adaptations, supported by the methodology rather than invented source headings. Likewise, What-changed is inherited from Patchwork's base net-assessment; the source makes comparisons throughout rather than in a chapter of that name.

## reusable-field-dictionary

**Notation:** A = annual source-derived dimension, M = methodology-derived production requirement, P = Patchwork operational addition/localisation. These are human-authored Markdown fields; names below do not create serialised properties. “Required” here means needed for a defensible completed use of this optional profile, **not** a new core validation rule. Repeat rows as needed; use “unknown,” “not collected” or “not applicable — reason” rather than zero for missing evidence.

| Field group / fields | Meaning and completion rule | Basis / source locator |
| --- | --- | --- |
| Identity: title, edition, publisher, authors, contact, rights, marking | Identify this product and its permitted handling; replace source publisher details, do not imply ENISA authorship | A pp. 1–4; P framework provenance/marking |
| Scope: purpose, audience, production requirement, intelligence questions, geography/constituency, sectors/assets | Define what the assessment is intended to answer; record exclusions and owner for each question | A pp. 9–10; M §§2.2.1–2.2.3 |
| Period: start, end, timezone, boundary convention, inclusion-date basis | Required; state whether membership uses occurrence, discovery, reporting or recording date, and how earlier activity reported in-window is handled | A p. 9; M §2.2.3 |
| Publication: edition label, actual release date, revision date/version, stable Published anchor | Keep distinct from period and evidence dates; anchor Patchwork Published to period start and preserve on revision | A cover/p. 9; P base net-assessment and framework §9.2 |
| Collection: source classes/languages, collection window, last inclusion cutoff, dataset version, collection plan | Required per corpus; mark unavailable cutoffs unknown; distinguish late reports from activity dates | A pp. 9–10, p. 19 note 79; M §§2.3–2.4 |
| Evidence: observation/case ID, source reference and locator, source publication date, observed date, collection date, claim/confirmation status, grading | Trace a judgment to observations and independent corroboration; retain reliability and credibility separately for each observation | A pp. 9–10, pp. 46–53, pp. 83–89; M §2.3.2.1; P framework §7.1 |
| Corpus: dataset ID, unit of analysis, N eligible, dedup key, exclusions, unknowns, selection rule | Required for every population used in a table or chart. Incidents, claims, events, victims, channels and observables are not interchangeable | A pp. 9–10, pp. 19, 74; P explicit reproducibility fields |
| Statistic: metric ID, population/filter, numerator n, denominator N, value/unit, known-subset size, rounding, overlap rule | Required for each percentage/ranking; disclose unknown denominator instead of deriving counts from rounded percentages | A pp. 11–12 (known intrusion-vector subset), pp. 18–19, 60, 74; P explicit statistical ledger |
| Ranking: ranked entity, metric, scope, period, N, tie/unknown policy, prior comparable position | Ranking by report/claim volume is not a severity, unique-victim or real-world-prevalence ranking; include unranked/unknown residual where relevant | A pp. 15, 18, 40–49, 64, 84; P tie/comparability controls |
| Threat: incident/activity type, assessed objective, intrusion vector, impact, enabling dependency, cases | Separate method from effect and claimed outcome from verified harm; overlapping threat classes must not be summed as disjoint | A pp. 11–17, 38–59, 83–89 |
| Actor: observed name, source aliases, attributed-by, attribution basis/uncertainty, object reference, assessed motivation/nexus | Source-reported state nexus is not Patchwork political attribution or an automatic promotion/alias merge | A pp. 60–73; P framework §4 |
| Sector: source label, subsector, canonical mapping, affected/targeted status, assignment rule, unknowns | Preserve NIS2 vs non-NIS2 and other source scope; explain chosen primary sector vs unknown and multi-sector effects | A pp. 9, 18–37; M §2.4.3; P Sectors crosswalk |
| Geography: target/impact location, source granularity, direct/indirect/cross-border relevance | Do not infer a country from “Europe” or equate victim location to actor nexus | A pp. 9–10, 54–55, 85–87; M §2.2.3 |
| TTP: procedure, technique ID/name/version, supporting observation, actor/campaign link, detection implication | Evidence-backed mapping, not a match inferred from a broad label or repeated vendor aliases | A p. 53 Figure 42, pp. 69–73; M §2.4.4; P ATT&CK mapping detail |
| Vulnerability: CVE/EUVD, disclosure date, score/version, vector, CWE, vendor/product, exploitation evidence, KEV status/as-of | Keep disclosure corpus, known-exploited corpus and locally observed exploitation separate; vendor counts do not establish product insecurity | A p. 71 Table 1, pp. 90–94; P explicit timestamp/version safeguards |
| FIMI: contributing corpus, period, geography, incident count basis, IMS/attribution, channels/platforms, observables, objectives | Optional where relevant and supported; do not add its units or global targets to EU cyber-incident totals | A pp. 74–82 |
| Change: prior edition/dataset, shared time, coverage/taxonomy changes, comparable metric, residual uncertainty | Required for comparisons; show non-comparability rather than a spurious increase/decrease | A p. 9 six-month overlap and expanded collection; P base What-changed |
| Assessment: judgment, evidence refs, likelihood wording, confidence rationale, alternatives, gaps | Distinguish reported fact and analyst inference; likelihood wording is not an Admiralty grade or an urgency score | A pp. 10, 95–96, 100; M §2.5; P framework §7 |
| Recommendation: finding/gap, action, intended recipient, owner, priority rationale, success measure | Source-backed action addressing an observed gap; owner/measure are local operational additions, not annual source fields | M §2.5; P action tracking |
| Operation annex: date, action, reported result/impact, involved countries/entities, evidence | Optional response/disruption timeline; do not assume a takedown caused an observed decline without analysis | A Appendix A pp. 97–99 |
| Publication control: reviewers, approvals, marking/reference checks, dissemination, feedback owner/channel, correction history | Record who validated evidence and conclusions; substantive updates identify nature/date; feed accepted/rejected feedback into the next cycle | M §§2.5.3–2.7.2; P auditable log |

## methodology-links-and-localisation

- **Direction:** [purpose](enisa-ctl-methodology-2026.md#221-establish-ctl-purpose), [audience](enisa-ctl-methodology-2026.md#222-define-audience), [intelligence requirements](enisa-ctl-methodology-2026.md#223-define-intelligence-requirements) → Purpose-and-requirements and Period-covered.
- **Collection:** [collection plan](enisa-ctl-methodology-2026.md#231-define-collection-plan), [source confidence](enisa-ctl-methodology-2026.md#2321-source-confidence-level) → evidence register and corpus definitions.
- **Processing:** [taxonomy](enisa-ctl-methodology-2026.md#243-cyber-threat-taxonomy), [CTI frameworks](enisa-ctl-methodology-2026.md#244-cti-frameworks), [correlation](enisa-ctl-methodology-2026.md#246-correlate-and-enrich-processed-content) → reproducible deduplication, sector crosswalks and evidence-backed TTPs.
- **Analysis and production:** [performing analysis](enisa-ctl-methodology-2026.md#252-performing-analysis), [validation](enisa-ctl-methodology-2026.md#253-validate-ctl), [textual formats](enisa-ctl-methodology-2026.md#textual-formats) → synthesis, limitations, actions and review.
- **Dissemination and feedback:** [post-publication updates](enisa-ctl-methodology-2026.md#263-post-publication-updates), [receiving](enisa-ctl-methodology-2026.md#271-receiving-feedback) and [actioning feedback](enisa-ctl-methodology-2026.md#272-actioning-feedback) → release/correction/feedback log.

**Patchwork precedence:** retain [sector mappings](../../Sectors.md), [controlled vocabularies](../../Vocabularies.md), [technical attribution doctrine](../../Patchwork-CTI-Framework.md#45-attribution-doctrine), [observation-level Admiralty grading](../../Patchwork-CTI-Framework.md#71-admiralty-grading-attaches-to-the-observation), [stable report identity](../../Patchwork-CTI-Framework.md#92-identity-and-merge-rules) and existing STIX graph. ENISA's EU-relevance score is contextual relevance, not Patchwork threat level (urgency/proximity) or confidence. This template does not make EU-only coverage compulsory for other constituencies.

**Tool-use disclosure is source-specific:** the annual disclaimer (p. 4) says AI supported limited collection/processing, experts validated outputs and no AI-generated content was used in the report. The broader [methodology §2.4.7](enisa-ctl-methodology-2026.md#247-use-of-ai-supported-tools) also allows limited editorial assistance, while reserving trend identification, conclusions and assessments for human analysts. These are not identical statements. Disclose actual practice; do not copy a “no AI” assertion unless true or claim this AI-assisted adaptation is the original ENISA report.

## completion-and-quality-gates

1. Every finding, chart and recommendation resolves to evidence or a clearly labelled analyst assessment; repeated reports of one incident do not manufacture independent evidence.
2. Every percentage resolves to a defined denominator and known/unknown subset; every ranking identifies its metric and scope. Counts and facts from this source edition are **not template defaults**.
3. Every comparison checks period overlap, changing collection coverage, inclusion criteria, date basis and taxonomy. A dataset is an observed snapshot, not a census of all activity (annual pp. 9–10).
4. Every source label keeps enough provenance to reproduce its mapping without changing core vocabularies; actor nexus and confirmed impact are never inferred from claimant branding.
5. Peer/expert review, author approval, marking checks, reference checks and correction/feedback ownership are recorded before release. See the [publication checklist](../../Publication-Checklist.md).
