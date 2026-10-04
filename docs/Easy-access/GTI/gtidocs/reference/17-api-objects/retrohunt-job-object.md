---
title: "Retrohunt Jobs"
source: https://gtidocs.virustotal.com/reference/retrohunt-job-object
slug: retrohunt-job-object
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:44:32.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Retrohunt Jobs

---

# retrohunt-jobs

YARA matching against Google Threat Intelligence's file corpus

A Retrohunt Job object represents a configured job to match a set of YARA rules which runs the Retrohunt job agains the files submitted to Google Threat Intelligence during the past 3 monts (or 1 year for Hunting Pro users). This object is only visible for the account's owner.

## object-attributes

The object contains the following attributes:

* `corpus`: <*string*> files against the Retrohunt job is run against. Can be either "main", which runs the Retrohunt job against all files or "goodware" which runs the job against a set of known goodware. This is useful to know whether the YARA rules raise lots of false positives.
* `creation_date`: <*integer*> job's creation date as UTC timestamp.
* `eta_seconds`: <*integer*> estimated number of remaining seconds until the job ends.
* `finish_date`: <*integer*> date when the Retrohunt job finished
* `notification_email`: <*string*> email to notify when the Retrohunt job ends.
* `num_matches`: <*integer*> number of matches.
* `num_matches_outside_time_range`: <*integer*> number of found matches outside the user's Retrohunt packet.
* `progress`: <*float*> percentage of already processed files.
* `rules`: <*string*> used YARA rules.
* `scanned_bytes`: <*integer*> number of scanned bytes.
* `start_date`: <*integer*> Retrohunt job start date.
* `status`: <*string*> can be either "starting", "running", "aborting", "aborted" or "finished".

```json Retrohunt job object
{
  "data": {
    "attributes": {
      "corpus": "<string>",
      "creation_date": <int:timestamp>,
      "eta_seconds": <int>,
      "finish_date": <int:timestamp>,
      "notification_email": "<string>",
      "num_matches": <int>,
      "num_matches_outside_time_range": <int>,
      "progress": <float>,
      "rules": "<string>",
      "scanned_bytes": <int>,
      "start_date": <int:timestamp>,
      "status": "<string>"
    },
    "id": "<string>",
    "links": {
      "self": "https://www.virustotal.com/api/v3/intelligence/retrohunt_jobs/<id>"
    },
    "type": "retrohunt_job"
  }
}
```
```json Example
{
  "data": {
    "attributes": {
      "corpus": "main",
      "creation_date": 1598966772,
      "eta_seconds": 47441,
      "notification_email": "spellman@company.com",
      "num_matches": 53,
      "num_matches_outside_time_range": 0,
      "progress": 62.06203,
      "rules": "/*\n    Template YARA ruleset\n*/\nrule yara_template\n{\n    strings:\n        $a = \"VirusTotal\"\n    condition:\n        all of them\n}",
      "scanned_bytes": 408163509658865,
      "start_date": 1598966777,
      "status": "running"
    },
    "id": "spellman-1598966772",
    "links": {
      "self": "https://www.virustotal.com/api/v3/intelligence/retrohunt_jobs/spellman-1598966772"
    },
    "type": "retrohunt_job"
  }
}
```

## relationships

In addition to the previously described attributes, Retrohunt Jobs objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](../01-api-introduction/api-responses/introduction-relationships.md) section.

The following table shows a summary of available relationships for retrohunt jobs objects.

| Relationship    | Description                                           | Accessibility | Return object typ                        |
| :-------------- | :---------------------------------------------------- | :------------ | :--------------------------------------- |
| matching\_files | Returns all files matched during the job's execution. | Owner.        | A list of [Files](file-object.md).      |
| owner           | Returns the job's owner.                              | Owner.        | A single [User](user-object.md) object. |

These relationships are detailed in the subsections below.

---

← [Report](report-object.md) · [up](README.md) · [🔀🧑‍💻 matching_files](retrohunt-job-object/retrohunt-job-matching-files.md) →

*Archived from <https://gtidocs.virustotal.com/reference/retrohunt-job-object>.*
