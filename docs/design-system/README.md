# Patchwork-Signal-Design-System

> **Status:** foundation proposal, v0.1 · **Implementation target:** OpenCTI with Filigran Design System (FDS) · **Visual direction:** dark-first, light-supported analyst workspace

Patchwork Signal is a product design layer for turning OpenCTI into a focused threat-intelligence workbench. It takes inspiration from Google Threat Intelligence's information hierarchy—fast global search, dense evidence views, faceted discovery, strong entity headers, and contextual sidebars—without copying Google branding, trade dress, proprietary scoring, or exact layouts.

This package is documentation-first. It defines the product contract that should be reviewed before production components are changed.

Only this foundation proposal and the token source are included on the framework branch. The component contracts, product patterns, Stitch prompt pack and interactive specimen belong to separate platform development and are not linked here as if they were available. This design-system proposal is excluded from the framework-only public export.

## Start-here

| Artifact | Purpose |
| --- | --- |
| [Token source](tokens.json) | Portable semantic tokens with dark/light modes and their FDS lineage. |
| Component contracts — not included on this branch | Anatomy, variants, states, accessibility, and OpenCTI reuse rules. |
| Product patterns — not included on this branch | Page-level composition for search, entities, reports, graphs, and dashboards. |
| Stitch prompt pack — not included on this branch | Production-ready prompts for the three reference screens when Stitch MCP is connected. |
| Interactive specimen — not included on this branch | Offline browser preview of the tokens and principal workflows. |

## Design-principles

1. **Intelligence before chrome.** Evidence, provenance, freshness, confidence, and relationships have more visual weight than decoration.
2. **Dense, never cryptic.** Compact layouts are allowed; hidden meaning is not. Icons have labels or tooltips, codes have explanations, and every score exposes its basis.
3. **Search is a language.** Natural text and structured filters share one query surface. The UI always shows what will be searched.
4. **Context travels with data.** Markings, source, access scope, ingestion time, and update time remain visible during pivots and export.
5. **Uncertainty is first-class.** Unknown, unavailable, pending, conflicting, and not-applicable are distinct from zero or safe.
6. **Progressive depth.** Scan first, compare second, investigate third. A user can move from summary to evidence without losing the current context.
7. **FDS by default.** Existing Filigran components and tokens are the implementation baseline. A Patchwork component is introduced only for a documented product gap.
8. **Keyboard-complete.** Search, filters, tables, tabs, menus, graph controls, and dialogs must work without a pointer.

## System-architecture

```text
FDS primitives and OpenCTI theme settings
                 ↓
Patchwork semantic tokens (meaning, not raw color names)
                 ↓
FDS components + documented Patchwork gap components
                 ↓
Search, entity, report, graph, dashboard, and policy patterns
                 ↓
OpenCTI product surfaces
```

The semantic layer protects product meaning while OpenCTI retains its theme administration and FDS migration path. For example, a component requests `color.feedback.error`, not a hard-coded red; the dark and light values trace back to the corresponding FDS token in [tokens.json](tokens.json).

## Foundations

### Color

- Dark mode is the default for long-running analyst sessions; light mode is fully supported, not an inversion afterthought.
- Elevation uses surface color and border contrast before shadow. Dark surfaces progress from canvas → panel → raised → emphasis.
- Blue means interaction or information, green means success or a positive system state, amber means uncertainty or warning, and red means destructive/error. Entity-category colors identify object families and never replace a text label.
- Verdicts are combinations of label, icon, explanation, and evidence count. Color alone never communicates maliciousness or confidence.

### Typography

- Product UI: IBM Plex Sans when available, then the system sans-serif stack.
- Observables, STIX IDs, hashes, query syntax, and machine values: IBM Plex Mono when available, then the system monospace stack.
- Default body text is 14px/20px. Compact metadata may use 12px/16px. Report prose uses 16px/26px and a maximum readable line length of 76 characters.
- Use sentence case for controls and headings. Uppercase is reserved for short classification labels and compact tab treatments.

### Spacing-and-density

- Base unit: 4px. Standard sequence: 4, 8, 12, 16, 24, 32, 48, 64.
- `compact` is for high-volume analyst queues and 36px control/row heights.
- `comfortable` is for reports, administration, and mixed audiences and uses 44px control/row heights.
- Density changes spacing and hit-area padding, never information or capabilities.

### Shape-and-depth

- Small controls and chips: 6px radius. Cards and panels: 8px. Dialogs: 10px.
- Borders define most grouping. Shadows are reserved for transient overlays, menus, and dialogs.
- A 2px focus ring with 2px offset is mandatory on every interactive element.

### Motion

- Use 120ms for hover/focus feedback, 180ms for overlays, and at most 240ms for page-level transitions.
- Never animate continuously to imply live data. Show a timestamp and explicit refresh state.
- Respect `prefers-reduced-motion`; all essential state changes remain understandable with animation disabled.

## Compatibility-contract

The first implementation should be an adapter over OpenCTI rather than a replacement UI library.

| Concern | Contract |
| --- | --- |
| Components | Prefer `@filigran/design-system`; use existing OpenCTI primitives when FDS has no equivalent; add a new primitive only after a gap is documented. |
| Theme | Preserve OpenCTI admin theme overrides. Semantic aliases resolve through the active light/dark theme rather than bypassing it. |
| Data | Components receive display-ready view models but retain STIX/OpenCTI IDs for navigation, actions, and telemetry. |
| Permissions | Hide neither the existence nor reason for an unavailable operation: render disabled actions with a permission explanation when disclosure is safe. |
| Markings | TLP/PAP and custom markings remain attached to selections, clipboard operations, downloads, and exports. |
| Localization | No layout relies on fixed English string widths. Dates, numbers, and relative time use locale-aware formatters. |
| Accessibility | Target WCAG 2.2 AA; automated checks are necessary but keyboard and screen-reader reviews are release gates. |

## Responsive-model

The product is desktop-first because investigation workflows need spatial context, but it must degrade predictably.

| Width | Behavior |
| --- | --- |
| ≥ 1440px | Rail + primary work area + contextual sidebar. Facets may remain pinned. |
| 1024–1439px | Rail + work area; contextual sidebar becomes a drawer. |
| 768–1023px | Collapsible rail; filters and context are modal sheets; tables prioritize essential columns. |
| < 768px | Read/triage mode only. Complex graph editing and bulk authoring present a clear desktop requirement. |

## Accessibility-release-gates

- Logical landmarks and one visible `h1` per screen.
- A skip link and deterministic focus return for drawers/dialogs.
- Contrast of at least 4.5:1 for body text and 3:1 for large text and meaningful UI boundaries.
- Minimum 24×24px pointer target, with 36×36px the compact product default.
- Tables expose sortable state, selected-row state, and bulk-action scope.
- Graph information has an equivalent navigable list/table view.
- Live ingestion or job updates are announced only when user-relevant; avoid noisy live regions.
- Truncation never destroys access to the full observable, identifier, label, or provenance value.

## Governance

Every component and pattern has one of four maturity levels: `proposal`, `pilot`, `stable`, or `deprecated`. Promotion requires:

1. FDS/OpenCTI reuse review;
2. dark, light, compact, and comfortable examples;
3. keyboard, focus, and screen-reader behavior;
4. loading, empty, error, partial, stale, restricted, and quota states where relevant;
5. screenshots or visual regression coverage;
6. an owner and migration note.

Changes to semantic meaning require design and threat-intelligence review. Raw value changes that preserve meaning require design-system review. Product teams may not create page-local verdict or marking colors.

## GTI-inspiration-boundary

The reference material is used to learn from workflow conventions, not to reproduce a branded product. Safe inspiration includes information density, search-centered navigation, faceted filtering, report/entity hierarchy, contextual evidence, and visible freshness. Do not use Google names or logos, duplicate GTI screens pixel-for-pixel, adopt proprietary score language, or imply affiliation.

## Stitch-status

Stitch MCP was not available in the current tool environment when v0.1 was authored. The Stitch prompt pack is the platform handoff contract, maintained outside this branch: once the connector is available, generate the three reference screens, record the returned project/screen IDs there, and review the output against the acceptance checklist before treating it as design input.
