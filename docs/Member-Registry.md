# Member-registry

This is the version-controlled registry described in
[framework 4.7](Patchwork-CTI-Framework.md#47-mature-name-collisions-and-the-member-registry).
It reserves member tokens and records mature-name registration order. Acceptance
is by reviewed pull request; a proposal, example or unmerged change is not a
reservation.

## Members

No member registrations have been accepted in this publication snapshot.
The `cc` and `acme` tokens in the examples illustrate the naming grammar; they
are not registrations or permission to publish on another organisation's behalf.

| Token | Exact STIX identity name | Public collision/retraction contact | Accepted at (UTC) |
| --- | --- | --- | --- |

Use a stable lowercase token and a monitored contact the member has approved
for public display. Maintainers record the actual UTC acceptance timestamp,
not an estimated activity date. Do not include credentials or private contact
details. Registered tokens remain reserved when a member retires; record that
status without deleting its historical reservation.

## Mature-names

No mature names have been registered in this publication snapshot.

| Member token | Mature name | Registered aliases | Accepted at (UTC) |
| --- | --- | --- | --- |

Before proposing a name, check this table, the member's lower-tier names and
aliases, and the relevant vendor names, following framework 4.7. Preserve the
first accepted registration and record corrections explicitly. A retired name
that would recreate a collision belongs in the object's description, not its
aliases. Do not infer a registered mature name from a worked example.

## Registration-changes

Follow [the contribution instructions](CONTRIBUTING.md#registering-a-member-or-mature-name).
Provide the member's approval to display its identity and contact, complete the
collision checks and keep changes limited to the registration being proposed.
Git history records when entries were accepted and corrected; consumers should
use the registry from the public distribution they adopted.
