# gtidocs-mirror

Keeps `docs/Easy-access/GTI/gtidocs/` in step with the Google Threat Intelligence
documentation hub, <https://gtidocs.virustotal.com/docs/>.

```bash
python3 tools/gtidocs-mirror/mirror.py                     # refresh everything
python3 tools/gtidocs-mirror/mirror.py --section guides    # guides | reference | changelog
python3 tools/gtidocs-mirror/mirror.py --dry-run           # discover and report only
python3 tools/gtidocs-mirror/mirror.py --use-cache         # reuse pages already fetched
python3 tools/gtidocs-mirror/mirror.py --no-images         # leave images hotlinked
```

Python 3.9+, standard library only. A full refresh takes roughly fifteen minutes and
writes about a thousand files, so it is deliberately not wired into anything automatic —
run it when you want the snapshot moved forward.

## What-it-relies-on

Two things the hub happens to publish, neither of them a documented API:

- **`<page-url>.md` returns that page's markdown source.** Upstream advertises this in a
  line prepended to every response; the mirror strips that line.
- **Every rendered page embeds its whole navigation tree** as a `"sidebar":[…]` JSON blob
  in the HTML. That is where the group titles, page titles, slugs, ordering and nesting
  come from — `llms.txt` is a flat list and cannot reproduce the hierarchy.

`llms.txt` is still fetched, as the source for the changelog section and as a coverage
cross-check: slugs it lists that the sidebar does not are reported rather than dropped.

If either affordance disappears, the script fails loudly rather than writing a damaged
archive.

## What-it-does-to-each-page

1. Strips the `Fetch the complete documentation index at: …llms.txt…` preamble.
2. Rebuilds the frontmatter — `title`, `source`, `slug`, `section`, `group`, upstream
   `updatedAt`, and the `retrieved` date.
3. Rewrites heading **text** to this repository's kebab-case convention (see the root
   `README.md`): lowercased, each run of whitespace collapsed to one hyphen, everything
   else preserved. Heading *levels* are left exactly as upstream publishes them, which is
   what keeps a refresh diff readable.
4. Converts readme.io's MDX components to plain markdown — `<Image>` to `![]()`,
   `<Callout>` to a blockquote. `<Image>` renders as nothing in both Obsidian and GitHub,
   so this is what makes the archived images visible at all. Any other component type is
   reported at the end of the run instead of being silently left in the output.
5. Downloads `files.readme.io` assets to `gtidocs/img/` and relinks them.
6. Rewrites internal links to relative paths, translating `#anchors` through each target
   page's heading map. A link to a slug that was not mirrored — hidden, deleted, or out
   of scope — keeps its absolute URL rather than pointing at a file that does not exist.
7. Adds a breadcrumb, a prev/next footer in sidebar order, and a link back to the live
   page.

Indexes (`README.md` at the root, per section and per group) are generated too. Nothing
under `gtidocs/` should be hand-edited — the next refresh overwrites it.

## Fetching-politely

`robots.txt` allows all three sections. The hub still answers a burst of requests with a
Cloudflare-style interstitial — **HTTP 200 with an HTML body**, which is why the fetcher
validates the body rather than trusting the status code. On a challenge it backs *every*
worker off for twenty seconds, not just the refused request, then retries, alternating
between `gtidocs.virustotal.com` and `gtidocs.readme.io`. Pages that still fail get up to
three serial retry sweeps; anything unresolved after that is listed and the run exits
non-zero.

Raw responses are cached under `.cache/` (git-ignored) so an interrupted run can resume
with `--use-cache`.

## Output-is-deterministic

Same upstream in, byte-identical files out. Re-running immediately after a successful run
leaves `git status` clean, which means a refresh diff shows real upstream changes and
nothing else.
