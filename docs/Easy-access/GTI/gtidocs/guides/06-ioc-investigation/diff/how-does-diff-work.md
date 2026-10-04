---
title: "How does Diff work?"
source: https://gtidocs.virustotal.com/docs/how-does-diff-work
slug: how-does-diff-work
section: guides
group: "IOC Investigation"
updatedAt: 2025-09-25T00:53:27.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [IOC Investigation](../README.md) › [Diff](../diff.md) › How does Diff work?

---

# how-does-diff-work?

There are multiple steps involved:

**Step 1**: Prepare intermediate results. Each of them MUST fit this criteria:

* It appears exactly as-is in ALL inclusion files.
* It can't appear in ANY of the exclusion files.
* It must be at least 16 bytes long.
* It must not be too long (usually < 256 bytes, but could be 1024 at times).

Application of these criteria often gives more than 10.000 total snippets.

**Step 2**: Keep top snippets amongst the intermediate results

We apply a statistical model to assign a score to each of the previous snippets, and use that score to pick the top 30 of each type -- eg: top 30 binary, top 30 ascii, etc.

The scores are inversely proportional to the expected number of goodware matched by the snippet. That is, a low score means that it would match lots of goodware, while a high score means it would match no goodware at all.

The scores are approximate, therefore it pays off to look past the first or second snippet on the results page.

---

← [Diff](../diff.md) · [up](../README.md) · [Ask questions with Gemini](../search-gemini.md) →

*Archived from <https://gtidocs.virustotal.com/docs/how-does-diff-work>.*
