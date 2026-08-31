# Graduation-fixture

> `graduation_fixture.bundle.json` is a **synthetic test bundle**, not a worked example. Everything
> in it — target names, personas, dates — is placeholder data, and it is documented here as what
> it is rather than dressed up as a threat narrative. Inventing a fake intelligence story around
> synthetic fixture data would work against the one thing this framework insists on throughout:
> that attribution and activity claims stay tied to real evidence
> ([4.5](../Patchwork-CTI-Framework.md#4.5-attribution-doctrine)).

## What-it's-for

[9.5 Automating the grouping step](../Patchwork-CTI-Framework.md#9.5-automating-the-grouping-step)
describes how tooling may assist — never decide — the move from independent activity clusters to
a temporary group: a tool may *suggest* candidate cluster pairs from shared infrastructure,
overlapping TTPs, or temporal/victimology proximity, but confirmation is a human act, and any
tool-generated group must carry an `inferred` / `pending-review` label.

This bundle is the **"before" state** that a grouping tool or demo would need as input: a small,
deterministic set of Cluster-tier `intrusion-set` objects with no relationships between them yet,
so that whatever grouping logic is being tested or demonstrated has something concrete to operate
on, and its output can be checked against a known starting point.

## What's-in-it

Four independent, unattributed activity clusters, each with exactly one incident and no
relationships to any other cluster:

| Cluster | Alias | MOT | Incident | Observed |
|---|---|---|---|---|
| `cc-CL-UNK-9001` | synthetic-alpha | `UNK` | Synthetic event against Target Alpha | 2025-01-01 – 2025-01-07 |
| `cc-CL-UNK-9002` | synthetic-beta | `UNK` | Synthetic event against Target Beta | 2025-03-01 – 2025-03-07 |
| `cc-CL-UNK-9003` | synthetic-gamma | `UNK` | Synthetic event against Target Gamma | 2025-05-01 – 2025-05-07 |
| `cc-CL-CRI-9004` | synthetic-delta | `CRI` | Synthetic event against Target Delta | 2025-02-01 – 2025-02-07 |

All four clusters carry `x_attribution_tier: Cluster` and confidence 30 (the Cluster-tier
baseline), and are namespaced under the `cc` example member token
([4.2](../Patchwork-CTI-Framework.md#4.2-member-namespaces)). Each incident is linked to its
cluster by a single `attributed-to` relationship — 4 clusters, 4 incidents, 4 edges, 0
cluster-to-cluster relationships. IDs are fixed, sequential placeholders
(`intrusion-set--00000000-0000-4000-8000-000000009001` and similar), not the UUIDv5-derived IDs
`build_bigbrother_access_sale.py` and `build_crescentharvest.py` use — this bundle is meant to be
regenerated or edited directly for a given test, not treated as a stable, citable sample the way
those two are.

## What-using-it-looks-like

Feeding this bundle to a grouping tool exercises exactly the case §9.5 describes: the tool has
four ungrouped clusters to consider. If it finds, say, shared infrastructure or matching TTPs
between two of them, the correct output is a new `cc-TGR-<MOT>-####` temporary-group
`intrusion-set`, `part-of` edges from the matched clusters to it, an `inferred` /
`pending-review` label, and a confidence no higher than the premises it rests on — never a
rewrite of the clusters themselves ([4.1](../Patchwork-CTI-Framework.md#4.1-three-tiers-of-object,-linked)).
This fixture intentionally ships without that outcome: whether and how any of the four clusters
group is exactly what the tooling under test is supposed to decide.
