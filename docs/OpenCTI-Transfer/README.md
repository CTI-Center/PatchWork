# OpenCTI-transfer documentation

The `docs/opencti-transfer` branch keeps these planning documents separate from
the framework, templates, examples and tooling maintained on `development`.
It starts from the framework's v0.7 development baseline.

## Documents

- [OpenCTI and GTI compatibility roadmap](../OpenCTI-Transfer-Plan.md)
- [GTI data structures and source contract](../GTI-Data-Structures.md)
- [GTI to OpenCTI backend compatibility plan](../GTI-OpenCTI-Backend-Plan.md)

These are planning drafts, not a released implementation or a completed licence
audit. The [framework specification](../Patchwork-CTI-Framework.md) remains the
shared baseline.

## Branch-maintenance

Bring framework updates from `development` into this documentation branch when
needed. Do not merge this branch back into `development` merely to synchronize
the framework: that would reintroduce the transfer documents there. Selectively
carry implementation changes back without these planning files.

Branch separation is organizational, not private access control. If the repository
is made public, its branches and existing history are public too. These documents
remain excluded from the framework-only public export.
