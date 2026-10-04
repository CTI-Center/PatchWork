---
title: "YARA Rules"
source: https://gtidocs.virustotal.com/reference/yara-rule-object
slug: yara-rule-object
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:46:32.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › YARA Rules

---

# yara-rules

YARA rules objects

A YARA Rule object represents one of the rules used in our crowdsourced YARA results. It has the following attributes:

* `author`: <*string*> rule author.
* `creation_date`: <*date (UTC timestamp)*> rule's creation date.
* `enabled`: <*boolean*> if the rule is currently running in the VT's crowdsourced rules corpus.
* `included_date`: <*date (UTC timestamp)*> rule's date of inclusion into the VT crowdsourced collection.
* `last_modification_date`: <*date (UTC timestamp)*> rule's last modification.
* `matches`: <*int*> approximate number of matches in VT intelligence for this rule.
* `meta`: <*list of dicts*> key/values containing the rule's meta information.
* `name`: <*string*> rule name.
* `rule`: <*string*> string containing the rule (and any necessary imports or dependencies).
* `tags`: <*list of strings*> rule's tags.
* `threat_categories`: <*list of strings*> rule's threat categories inferred from the files matched.

```json YARA rule example
{
	"data": {
		"attributes": {
			"name": "SUSP_OneNote_Embedded_FileDataStoreObject_Type_Jan23_1",
			"threat_categories": [
				"trojan",
				"downloader",
				"dropper"
			],
			"author": "Florian Roth (Nextron Systems)",
			"matches": 370,
			"enabled": true,
			"rule": "rule SUSP_OneNote_Embedded_FileDataStoreObject_Type_Jan23_1 {\n   meta:\n      description = \"Detects suspicious embedded file types in OneNote files\"\n      author = \"Florian Roth\"\n      reference = \"https://blog.didierstevens.com/\"\n      date = \"2023-01-27\"\n      modified = \"2023-02-27\"\n      score = 65\n   strings:\n      /* GUID FileDataStoreObject https://blog.didierstevens.com/ */\n      $x1 = { e7 16 e3 bd 65 26 11 45 a4 c4 8d 4d 0b 7a 9e ac \n              ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ??\n              ?? ?? ?? ?? 4d 5a } // PE\n      $x2 = { e7 16 e3 bd 65 26 11 45 a4 c4 8d 4d 0b 7a 9e ac \n              ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ??\n              ?? ?? ?? ?? [0-4] 40 65 63 68 6f } // @echo off\n      $x3 = { e7 16 e3 bd 65 26 11 45 a4 c4 8d 4d 0b 7a 9e ac \n              ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ??\n              ?? ?? ?? ?? [0-4] 40 45 43 48 4f } // @ECHO OFF\n      $x4 = { e7 16 e3 bd 65 26 11 45 a4 c4 8d 4d 0b 7a 9e ac \n              ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ??\n              ?? ?? ?? ?? [0-4] 4F 6E 20 45 } // On Error Resume\n      $x5 = { e7 16 e3 bd 65 26 11 45 a4 c4 8d 4d 0b 7a 9e ac \n              ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ??\n              ?? ?? ?? ?? [0-4] 6F 6E 20 65 } // on error resume\n      $x6 = { e7 16 e3 bd 65 26 11 45 a4 c4 8d 4d 0b 7a 9e ac\n              ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ??\n              ?? ?? ?? ?? 4c 00 00 00 } // LNK file\n      $x7 = { e7 16 e3 bd 65 26 11 45 a4 c4 8d 4d 0b 7a 9e ac\n              ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ??\n              ?? ?? ?? ?? 49 54 53 46 } // CHM file\n      $x8 = { e7 16 e3 bd 65 26 11 45 a4 c4 8d 4d 0b 7a 9e ac\n              ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ??\n              ?? ?? ?? ?? [6-200] 3C 68 74 61 3A } // hta:\n      $x9 = { e7 16 e3 bd 65 26 11 45 a4 c4 8d 4d 0b 7a 9e ac\n              ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ??\n              ?? ?? ?? ?? [6-200] 3C 48 54 41 3A } // HTA:\n      $x10 = { e7 16 e3 bd 65 26 11 45 a4 c4 8d 4d 0b 7a 9e ac\n              ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ??\n              ?? ?? ?? ?? [6-200] 3C 6A 6F 62 20 } // WSF file \"<job \"\n   condition:\n      filesize < 10MB and 1 of them\n}",
			"creation_date": 1674777600,
      "included_date": 1674777600,
			"meta": [
				{
					"key": "description",
					"value": "Detects suspicious embedded file types in OneNote files"
				},
				{
					"key": "author",
					"value": "Florian Roth"
				},
				{
					"key": "reference",
					"value": "https://blog.didierstevens.com/"
				},
				{
					"key": "date",
					"value": "2023-01-27"
				},
				{
					"key": "modified",
					"value": "2023-02-27"
				},
				{
					"key": "score",
					"value": 65
				}
			],
			"last_modification_date": 1677575583
		},
		"type": "yara_rule",
		"id": "000544e312|SUSP_OneNote_Embedded_FileDataStoreObject_Type_Jan23_1",
		"links": {
			"self": "https://www.virustotal.com/api/v3/yara_rules/000544e312|SUSP_OneNote_Embedded_FileDataStoreObject_Type_Jan23_1"
		}
	}
}
```

## relationships

In addition to the previously described attributes, YARA rules objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](../01-api-introduction/api-responses/introduction-relationships.md) section.

The following table shows a summary of available relationships for YARA rules objects.

| Relationship  | Description                                    | Accessibility | Return object typ                                     |
| :------------ | :--------------------------------------------- | :------------ | :---------------------------------------------------- |
| yara\_ruleset | Returns the YARA ruleset this rule belongs to. | Everyone.     | A single of [YARA Ruleset](yara-rulesets-object.md). |

---

← [Whois](whois-object.md) · [up](README.md) · [YARA Rulesets](yara-rulesets-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/yara-rule-object>.*
