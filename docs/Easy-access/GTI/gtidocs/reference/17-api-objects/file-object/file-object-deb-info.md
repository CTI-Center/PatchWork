---
title: "deb_info"
source: https://gtidocs.virustotal.com/reference/file-object-deb-info
slug: file-object-deb-info
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:07.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › deb_info

---

# deb_info

information about Debian packages.

`deb_info` gives information about [Debian packages](https://wiki.debian.org/Packaging).

* `changelog`: <*dictionary*> information about changes in the packaged version of a project. [More info](https://www.debian.org/doc/debian-policy/ch-source.html#debian-changelog-debian-changelog).
  * `Author`: <*string*> author name.
  * `Date`: <*string*> build/last edited date in `%a, %d %b %Y %H:%M%S %z` [format](http://strftime.org/).
  * `Debian revision`: <*string*> system revision.
  * `Debian version`: <*string*> system version.
  * `Distributions`: <*string*> contains the (space-separated) name(s) of the distribuition(s) where this version of the package should be installed. [More info](https://www.debian.org/doc/debian-policy/ch-controlfields.html#distribution).
  * `Full version`: <*string*> full system version.
  * `Package`: <*string*> package type.
  * `Urgency`: <*string*> description of how important it is to upgrade to this version from previous ones. Possible values are "low", "medium", "high", "emergency" or "critical". [More info](https://www.debian.org/doc/debian-policy/ch-controlfields.html#s-f-urgency).
  * `Version history`: <*string*> system version history.
* `control_metadata`: <*dictionary*> package metadata information. Fields may change from package to package, all values are strings, but some common fields are (more fields listed in the [debian docs](https://www.debian.org/doc/debian-policy/ch-controlfields.html#list-of-fields)):
  * `Maintainer`: <*string*> maintainer identifier.
  * `Description`: <*string*> package description.
  * `Package`: <*string*> package name.
  * `Depends`: <*string*> package dependencies.
  * `Version`: <*string*> package version.
  * `Architecture`: <*string*> architecture for running this software (ie. "i386").
* `control_scripts`: <*dictionary*> scripts to run in package management operations.
  * `postinst`: <*string*> script to run after installation.
  * `postrm`: <*string*> script to run after removal.
  * `preinst`: <*string*> script to run before installation.
  * `prerm`: <*string*> script to run before removal.
* `structural_metadata`: <*dictionary*> package structure information:
  * `contained_files`: <*integer*> number of files inside the package.
  * `contained_items`: <*integer*> number of files and directories inside the package.
  * `max_date`: <*string*> oldest child file modification date in `%Y-%m-%d %H:%M%S` [format](http://strftime.org/).
  * `min_date`: <*string*> most recent child file modification date in `%Y-%m-%d %H:%M%S` [format](http://strftime.org/).

```json Debian packages
{
  "data": {
		...
    "attributes" : {
      ...
      "deb_info": {
        "changelog": {
          	"Author": "<string>",
            "Date": "<string:%a, %d %b %Y %H:%M%S %z>",
            "Debian revision": "<string>",
            "Debian version": "<string>",
            "Distributions": "<string>",
            "Full version": "<string>",
            "Package": "<string>",
            "Urgency": "<string>",
            "Version history": "<string>"
        },
        "control_metadata": {
            "<string>": "<string>", ...
        },
        "control_scripts": {
            "postinst": "<string>",
            "postrm": "<string>",
            "preinst": "<string>",
            "prerm": "<string>"
        },
        "structural_metadata": {
            "contained_files": <int>,
            "contained_items": <int>,
            "max_date": "<string:%Y-%m-%d %H:%M%S>",
            "min_date": "<string:%Y-%m-%d %H:%M%S>"
        }
      }
    }
  }
}
```
```json Example
{
    "data": {
        "attributes": {
            "deb_info": {
                "changelog": {
                    "Author": "Blablabla <support@lablabla.bla>",
                    "Date": "Fri, 15 May 2020 17:25:05 -0700",
                    "Debian revision": "2",
                    "Debian version": "2",
                    "Distributions": "whatever",
                    "Full version": "1.2.13-2",
                    "Package": "blabla-desktop",
                    "Urgency": "medium",
                    "Version history": "1.2.13-2, 1.2.13-1, 1.2.12-1, 1.2.11-2, 1.2.11-1"
                },
                "control_metadata": {
                    "Architecture": "amd64",
                	"Conflicts": "containerd, runc",
                    "Depends": "libc6 (>= 2.14), libnotify4, libappindicator1, libxtst6, libnss3, libasound2, libxss1",
                    "Description": "\n  Blablabla desktop",
                    "Homepage": "https://github.com/blabla/blabla",
                    "Installed-Size": "325997",
                    "License": "GPL-3.0",
                    "Maintainer": "Blablabla <support@blablabla.bla>",
                    "Package": "blabla-desktop",
                    "Priority": "extra",
                    "Provides": "blabla, runc",
                    "Replaces": "blabla, runc",
                    "Section": "default",
                    "Vendor": "Blablabla <support@blabla.org>",
                    "Version": "1.34.1"
                },
                "control_scripts": {
                    "postinst": "#!/bin/bash\n\n# Link to the binary\nln -sf '/opt/blabla/blabla-desktop' '/usr/bin/blabla-desktop'\n\nupdate-mime-database /usr/share/mime || true\nupdate-desktop-database /usr/share/applications || true\n",
                    "postrm": "#!/bin/bash\n\n# Delete the link to the binary\nrm -f '/usr/bin/blabla-desktop'\n",
                  	"preinst": "#!/bin/bash\n# $Id: preinst 127855 2019-01-01 01:45:53Z bird $\n## @file\n# Blabla pre-install.\n#\n\n#\n# Copyright (C) 2006-2019 Blabla Systems\n",
                  	"prerm": "#!/bin/sh\nset -e\n# Automatically added by dh_systemd_start/11.1.6ubuntu2\nif [ -d /run/systemd/system ] && [ \"$1\" = remove ]; then\n\tdeb-systemd-invoke stop 'blabla.service' >/dev/null || true\nfi\n# End automatically added section\n"
                },
                "structural_metadata": {
                    "contained_files": 968,
                    "contained_items": 1160,
                    "max_date": "2020-05-16 00:25:05",
                    "min_date": "2020-05-16 00:08:35"
                }
            }
        }
    }
}
```

---

← [bundle_info](file-object-bundle-info.md) · [up](../README.md) · [magic](file-object-magic.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-deb-info>.*
