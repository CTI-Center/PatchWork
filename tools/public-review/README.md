# Public-review

Prepare a framework-only public copy with an explicit allowlist. The specification,
vocabularies, sectors, report templates, worked examples, reference documents,
images and repository tools are included. Development plans, application prototypes,
hosting configuration, local caches and Git metadata are not copied. Unknown new
top-level documents are excluded until deliberately added to `public_files.py`.

## Prepare-the-copy

From the original repository root, using Python 3.9+ (standard library only):

```sh
python3 tools/check-links/check-links.py --public --all
python3 -m unittest discover -s tools/check-links -p 'test_*.py'
python3 -m unittest discover -s tools/public-review -p 'test_*.py'
python3 tools/public-review/prepare-public.py --output dist/public-review
```

The destination must not already exist. The command copies into a temporary staging
directory, checks **every included Markdown file**, including third-party mirrors,
regenerates the public README's tree, and publishes the copy only if validation
passes. Source files are not deleted or moved. Symlinks are rejected to prevent a
public-looking path from importing private content.

The validation covers local file/image paths, heading fragments, reference-link
destinations and HTML links inside Markdown. It does not probe external websites,
validate third-party redistribution rights or guarantee their availability.

## Publish-safely

**Create a new GitHub repository from the generated copy. Do not make the original
repository public.** Private development documents were previously committed;
deleting or ignoring their current files does not remove older versions from Git
history. The public copy contains no `.git` directory and inherits none of that
history. Never add the original checkout as a remote and push its branches or tags
to the public repository.

Inspect the generated copy, review the source-document licences described in the
[project README](../../README.md#licence), then publish only its contents. This
tool does not create a Git repository, push code or change repository visibility.
