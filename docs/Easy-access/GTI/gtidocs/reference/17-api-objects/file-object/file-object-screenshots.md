---
title: "🔀 screenshots"
source: https://gtidocs.virustotal.com/reference/file-object-screenshots
slug: file-object-screenshots
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:48.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › 🔀 screenshots

---

# 🔀-screenshots

Screenshots obtained from the execution of the file.

The *screenshots* relationship returns a list of ***screenshots obtained from the execution of the file*** in a sandbox. This relationship is only available for Premium API users.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/files/files-relationships.md). The response contains a list of [Screenshot](../screenshots-object.md) objects.

An Screenshot object contains the following attributes:

* `date`: <*integer*> date the screenshot was taken as UTC timestamp.
* `link`: <*string*> URL containing the screenshot image.
* `sandbox_name`: <*string*> sandbox where the screenshot was taken.

```json /files/{file_hash}/screenshots
{
  "data": [
    {
      "attributes": {
    		"date": <int:timestamp>,
      	"link": "<string>",
      	"sandbox_name": "<string>"
      },
      "id": "<string>,
      "links": {
      	"self": "<string>"
    	},
    	"type": "screenshot"
    },
    ...
  ],
  "links": {
    "next": "<string>",
    "self": "<string>"
    },
  "meta": {
    	"count": <int>,
      "cursor": "<string>"
  }
}
```
```json Example
{
    "data": [
        {
            "attributes": {
                "date": 1590166148,
                "link": "https://vtscreenshot.commondatastorage.googleapis.com/64a3484274244c4846e414544f4c41d4504e5d4ba494f849491643d4b484f415-VirusTotal%20Jujubox-4D4mqHoacbg6KNm5NHbV7S-1590166148.png?GoogleAccessId=758681729565-rc7fgq07icj8c9dm2gi34a4cckv235v1@developer.gserviceaccount.com&Expires=1593442349&Signature=MOvhSzpnUK1S135JupctYUuNf6dcEvS3GNdtJh8LkHk%2FbtamBz%2BmVSu9am6gLLS%2BoYshDwa1nJXz%0AAJoL85yVuo1j8TQnQuFKAeIwF1U9mQ6miEy%2FDxCI7kcmBMIpSm6oTtglQ5RwOSOAIqI3A%2BW3%2F7aS%0Aa2QRtdKs9VttaDCxrGU%3D",
                "sandbox_name": "VirusTotal Jujubox"
            },
            "id": "64a3484274244c4846e414544f4c41d4504e5d4ba494f849491643d4b484f415-VirusTotal Jujubox-4D4mqHoacbg6KNm5NHbV7S-1590166148.png",
            "links": {
                "self": "https://www.virustotal.com/api/v3/screenshots/64a3484274244c4846e414544f4c41d4504e5d4ba494f849491643d4b484f415-VirusTotal Jujubox-4D4mqHoacbg6KNm5NHbV7S-1590166148.png"
            },
            "type": "screenshot"
        }
    ],
    "links": {
        "next": "https://www.virustotal.com/api/v3/files/64a3484274244c4846e414544f4c41d4504e5d4ba494f849491643d4b484f415/screenshots?cursor=65a3289278241cb856e21c5a4fccd1d350ee5dbba997f889c91673d0b986f215-VirusTotal+Jujubox-4D4mqHoacbg6KNm5NHbV7S-1590166148.png&limit=10",
        "self": "https://www.virustotal.com/ui/files/64a3484274244c4846e414544f4c41d4504e5d4ba494f849491643d4b484f415/screenshots?limit=10"
    },
    "meta": {
        "count": 1,
        "cursor": "64a3484274244c4846e414544f4c41d4504e5d4ba494f849491643d4b484f415-VirusTotal Jujubox-4D4mqHoacbg6KNm5NHbV7S-1590166148.png"
    }
}
```

---

← [🔀 memory_pattern_urls](file-object-memory-pattern-urls.md) · [up](../README.md) · [🔀 itw_urls](file-object-itw-urls.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-screenshots>.*
