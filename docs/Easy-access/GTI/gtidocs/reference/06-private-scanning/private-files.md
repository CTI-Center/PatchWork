---
title: "Private Files"
source: https://gtidocs.virustotal.com/reference/private-files
slug: private-files
section: reference
group: "Private Scanning"
updatedAt: 2025-09-25T00:36:53.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [Private Scanning](README.md) › Private Files

---

# private-files

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

Private file scanning is a service that allows you to scan files in Google Threat Intelligence in a privacy preserving fashion. Files uploaded via the private scanning endpoints won't be shared with other Google TI users or partners, and will remain in Google TI only for a brief period of time. The resulting analyses will be ephemeral too.

On the other hand, private analyses won't contain antivirus verdicts, they will contain only the output of all the other characterization tools that we have in Google TI, including sandboxes.

## scanning-flow

Let's see step by step how to scan a file and retrieve the results from an analysis.

First, upload a file using the [/private/files](private-files/upload-file-private-scanning.md) endpoint. If your file is bigger than 32MB, you must use the [/private/files/upload\_url](private-files/private-files-upload-url.md) endpoint to get an upload URL and post the file there.

```python
import requests

api_key = 'your_api_key_here'
path_to_file = 'path_to_your_file_to_scan'

headers = {'x-apikey': api_key}
with open(path_to_file, 'rb') as f:
  params = {
	'enable_internet': True,  # true by default
	'intercept_tls': True, # true by default
	'locale': 'ES_ES'
  }
  # You can also specify the command line arguments of the file as well
  # params['command_line'] = '/s'

  # If the file is >32MB you can first get an upload URL.
  response = requests.get(
    'https://www.virustotal.com/api/v3/private/files/upload_url', headers=headers)
  response.raise_for_status()
  upload_url = response.json()['data']

  response = requests.post(
    upload_url, headers=headers, data=params, files={'file': f})
  response.raise_for_status()

print('Analysis ID: {}'.format(response.json()['data']['id']))
```

The example above should print something like `Analysis ID: OWI0YjE3NTMxNjY3ZDIwOTUyMTU1YmU0MDE0ZjhiZjQ6M2JkMjVkYmIzY2MyNDU1N2I4NjE4Yzg0N2IzYTk3ZTY6MTY1ODkzMzYxNA==`.

Let's check how the analysis is going using the [analysis endpoint](private-analyses/private-analysis.md):

```python
import json
import requests

api_key = 'your_api_key_here'
analysis_id = 'id_from_the_previous_step'

headers = {'x-apikey': api_key}

response = requests.get(
  'https://www.virustotal.com/api/v3/private/analyses/{}'.format(analysis_id),
  headers=headers)
response.raise_for_status()
print(json.dumps(response.json(), indent=2))
```

The response you'll get will be similar to this one (example for both in-progress and finished statuses):

```json In-progress
{
  "meta": {
    "file_info": {
      "size": 7747955,
      "sha256": "6b4bb405d3deea7a63e3ed02dd62a59c69b9458c15a901f3607429325b228ae8",
      "sha1": "ecf34753e10ba34a54d3989abb30460ea2c73972",
      "md5": "3bd25dbb3cc24557b8618c847b3a97e6"
    }
  },
  "data": {
    "attributes": {
      "date": 1658933614,
      "sandbox_status": {
        "Zenbox": {
          "status": "running",
          "in_progress_percent": 78
        }
      },
      "status": "in-progress",
      "pending_stages": {
        "tools": "File's tools",
        "Zenbox": "Sandbox analysis from Zenbox (running)"
      }
    },
    "type": "private_analysis",
    "id": "OWI0YjE3NTMxNjY3ZDIwOTUyMTU1YmU0MDE0ZjhiZjQ6M2JkMjVkYmIzY2MyNDU1N2I4NjE4Yzg0N2IzYTk3ZTY6MTY1ODkzMzYxNA==",
    "links": {
      "item": "https://www.virustotal.com/api/v3/private/files/6b4bb405d3deea7a63e3ed02dd62a59c69b9458c15a901f3607429325b228ae8",
      "self": "https://www.virustotal.com/api/v3/private/analyses/OWI0YjE3NTMxNjY3ZDIwOTUyMTU1YmU0MDE0ZjhiZjQ6M2JkMjVkYmIzY2MyNDU1N2I4NjE4Yzg0N2IzYTk3ZTY6MTY1ODkzMzYxNA=="
    }
  }
}
```
```json Finished
{
  "meta": {
    "file_info": {
      "size": 7747955,
      "sha256": "6b4bb405d3deea7a63e3ed02dd62a59c69b9458c15a901f3607429325b228ae8",
      "sha1": "ecf34753e10ba34a54d3989abb30460ea2c73972",
      "md5": "3bd25dbb3cc24557b8618c847b3a97e6"
    }
  },
  "data": {
    "attributes": {
      "date": 1658933614,
      "sandbox_status": {
        "Zenbox": {
          "status": "finished",
          "in_progress_percent": 100
        }
      },
      "status": "completed"
    },
    "type": "private_analysis",
    "id": "OWI0YjE3NTMxNjY3ZDIwOTUyMTU1YmU0MDE0ZjhiZjQ6M2JkMjVkYmIzY2MyNDU1N2I4NjE4Yzg0N2IzYTk3ZTY6MTY1ODkzMzYxNA==",
    "links": {
      "item": "https://www.virustotal.com/api/v3/private/files/6b4bb405d3deea7a63e3ed02dd62a59c69b9458c15a901f3607429325b228ae8",
      "self": "https://www.virustotal.com/api/v3/private/analyses/OWI0YjE3NTMxNjY3ZDIwOTUyMTU1YmU0MDE0ZjhiZjQ6M2JkMjVkYmIzY2MyNDU1N2I4NjE4Yzg0N2IzYTk3ZTY6MTY1ODkzMzYxNA=="
    }
  }
}
```

Here you can check the analysis progress, as well as the file's basic info. If there is any info in `pending_stages` it means there are still some phases of the analysis running and more info can be added to the file report. You can find information about all the analysis attributes [here](../17-api-objects/private-analyses-object.md).

Once finished, we can retrieve the file report using the [/files/\{id}](private-files/private-files-info.md) endpoint.

```python
import json
import requests

api_key = 'your_api_key_here'
sha256 = 'sha256_of_the_file'

headers = {'x-apikey': api_key}

response = requests.get(
  'https://www.virustotal.com/api/v3/private/files/{}'.format(sha256),
  headers=headers)
response.raise_for_status()
print(json.dumps(response.json(), indent=2))
```

You can find information about the file's attributes in [here](../17-api-objects/private-files-object.md). In this case the SHA256 of the file is `6b4bb405d3deea7a63e3ed02dd62a59c69b9458c15a901f3607429325b228ae8`:

```json File report example
{
	"data": {
		"attributes": {
			"type_description": "PDF",
			"tlsh": "T154761224FDA95CC9C21C5BAA12CB7C0D79CF31D3E9C10986BAEDDB448F209B9488755B",
			"vhash": "9ed7c0b10fe9f9da527181b6198fb89c3",
			"exiftool": {
				"MIMEType": "application/pdf",
				"DerivedFromRenditionClass": "default",
				"CreatorTool": "Adobe InDesign CC 14.0 (Windows)",
				"Language": "es-ES",
				"InstanceID": "uuid:d45baa98-85ca-4f27-91bd-c53f1cebf65b",
				"FileType": "PDF",
				"OriginalDocumentID": "xmp.did:01c55fe4-c514-474e-adfd-185352a4f7e6",
				"Format": "application/pdf",
				"Linearized": "Yes",
				"PDFVersion": "1.4",
				"DocumentID": "xmp.id:d8847550-9bd7-524f-a3ef-514263ba75a4",
				"MetadataDate": "2019:07:11 09:35:27+02:00",
				"XMPToolkit": "Adobe XMP Core 5.6-c016 91.163616, 2018/10/29-16:58:49        ",
				"ModifyDate": "2019:07:11 09:35:27+02:00",
				"HistoryParameters": "from application/x-indesign to application/pdf",
				"RenditionClass": "proof:pdf",
				"Trapped": "False",
				"DerivedFromDocumentID": "xmp.did:0e6a2b88-510d-1a43-ba84-f9c14006fe14",
				"Creator": "Adobe InDesign CC 14.0 (Windows)",
				"Producer": "Adobe PDF Library 15.0",
				"DerivedFromOriginalDocumentID": "xmp.did:01c55fe4-c514-474e-adfd-185352a4f7e6",
				"FileTypeExtension": "pdf",
				"PageCount": "24",
				"TaggedPDF": "Yes",
				"DerivedFromInstanceID": "xmp.iid:a770ad45-83de-d042-b28d-18635d3779f0",
				"CreateDate": "2019:02:26 12:31:48+01:00"
			},
			"trid": [
				{
					"file_type": "Adobe Portable Document Format",
					"probability": 100.0
				}
			],
			"crowdsourced_yara_results": [
				{
					"description": "This signature detects an Adobe Type 1 Font. The Type 1 Font Format is a standardized font format for digital imaging applications.",
					"source": "https://github.com/InQuest/yara-rules-vt",
					"author": "InQuest Labs",
					"ruleset_name": "Adobe_Type_1_Font",
					"rule_name": "Adobe_Type_1_Font",
					"ruleset_id": "0124227417"
				},
				{
					"description": "This signature identifies Adobe Extensible Metadata Platform (XMP) identifiers embedded within files. Defined as a standard for mapping graphical asset relationships, XMP allows for tracking of both parent-child relationships and individual revisions. There are three categories of identifiers: original document, document, and instance. Generally, XMP data is stored in XML format, updated on save/copy, and embedded within the graphical asset. These identifiers can be used to track both malicious and benign graphics within common Microsoft and Adobe document lures.",
					"source": "https://github.com/InQuest/yara-rules-vt",
					"author": "InQuest Labs",
					"ruleset_name": "Adobe_XMP_Identifier",
					"rule_name": "Adobe_XMP_Identifier",
					"ruleset_id": "0121ae37cc"
				},
				{
					"description": "This signature detects a PDF file that contains JavaScript. JavaScript can be used to customize PDFs by implementing objects, methods, and properties. While not inherently malicious, embedding JavaScript inside of a PDF is often used for malicious purposes such as malware delivery or exploitation.",
					"source": "https://github.com/InQuest/yara-rules-vt",
					"author": "InQuest Labs",
					"ruleset_name": "PDF_Containing_JavaScript",
					"rule_name": "PDF_Containing_JavaScript",
					"ruleset_id": "012eee8dbe"
				}
			],
			"creation_date": 1551184308,
			"names": ['helloWorld.pdf'],
			"type_tag": "pdf",
			"size": 7747955,
			"type_extension": "pdf",
			"sigma_analysis_results": [
				{
					"rule_title": "Powershell Create Scheduled Task",
					"rule_source": "Sigma Integrated Rule Set (GitHub)",
					"match_context": [
						{
							"values": {
								"EventID": "4104",
								"ScriptBlockText": "2a9050b8b5565911bbd3de0f9fdb41c96563509fc86f87745820109398fd58d8",
								"ScriptBlockId": "ba2beb8a-766d-4a3a-ad9d-8ba256d8f8a4",
								"MessageNumber": "",
								"MessageTotal": "",
								"Path": ""
							}
						},
						...
					],
					"rule_level": "medium",
					"rule_description": "Adversaries may abuse the Windows Task Scheduler to perform task scheduling for initial or recurring execution of malicious code",
					"rule_author": "frack113",
					"rule_id": "60d527fe5a592cbe8e98428d1412743b909d5625ec8bc91d20e8b6ee8b36db20"
				},
				{
					"rule_title": "Failed Code Integrity Checks",
					"rule_source": "Sigma Integrated Rule Set (GitHub)",
					"match_context": [
						{
							"values": {
								"EventID": "5038",
								"param1": "\\Device\\HarddiskVolume4\\Program Files (x86)\\sandbox\\driver\\sandbox-driver.sys"
							}
						}
					],
					"rule_level": "low",
					"rule_description": "Code integrity failures may indicate tampered executables.",
					"rule_author": "Thomas Patzke",
					"rule_id": "134564d292d785dff102940b8a1ee06dba2d462c5fb852124b3771a49d7885f1"
				}
			],
			"sigma_analysis_summary": {
				"Sigma Integrated Rule Set (GitHub)": {
					"high": 0,
					"medium": 1,
					"critical": 0,
					"low": 1
				}
			},
			"sandbox_verdicts": {
				"Zenbox": {
					"category": "harmless",
					"sandbox_name": "Zenbox",
					"malware_classification": [
						"CLEAN"
					]
				}
			},
			"sha256": "6b4bb405d3deea7a63e3ed02dd62a59c69b9458c15a901f3607429325b228ae8",
			"tags": [
				"pdf"
			],
			"ssdeep": "98304:fva/k8OIVuc+z4jRuBdKLLOjKkRLNAJOvGVr2uMBZsUtGGTNkFAamzZXTydDqB:fS88zp+z4b+nAJOvGhMBZJT5am9uqB",
			"md5": "3bd25dbb3cc24557b8618c847b3a97e6",
			"sha1": "ecf34753e10ba34a54d3989abb30460ea2c73972",
			"magic": "PDF document, version 1.4",
			"sigma_analysis_stats": {
				"high": 0,
				"medium": 1,
				"critical": 0,
				"low": 1
			},
			"pdf_info": {
				"xfa": 0,
				"encrypted": 0,
				"javascript": 0,
				"openaction": 0,
				"js": 1,
				"header": "%PDF-1.4",
				"startxref": 2,
				"xref": 2,
				"num_stream": 234,
				"num_object_streams": 25,
				"acroform": 0,
				"num_launch_actions": 0,
				"num_obj": 304,
				"num_endstream": 234,
				"num_pages": 24,
				"suspicious_colors": 0,
				"flash": 0,
				"embedded_file": 0,
				"jbig2_compression": 0,
				"autoaction": 0,
				"trailer": 2,
				"num_endobj": 304
			}
		},
		"type": "private_file",
		"id": "6b4bb405d3deea7a63e3ed02dd62a59c69b9458c15a901f3607429325b228ae8",
		"links": {
			"self": "https://www.virustotal.com/api/v3/private/files/6b4bb405d3deea7a63e3ed02dd62a59c69b9458c15a901f3607429325b228ae8"
		}
	}
}
```

In the case of this analysis we also saw a `sandbox_status` attribute:

```json
 "sandbox_status": {
        "Zenbox": {
          "status": "finished",
          "in_progress_percent": 100
        }
      },
```

Which indicates that we should have a sandbox report for this file, let's go and retrieve the available sandbox reports for the file using the [/files/\{sha256}/behaviours](private-files/private-files-relationships.md) relationship:

```python
import json
import requests

api_key = 'your_api_key_here'
sha256 = 'sha256_of_the_file'

headers = {'x-apikey': api_key}

response = requests.get(
  'https://www.virustotal.com/api/v3/private/files/{}/behaviours'.format(sha256),
  headers=headers)
response.raise_for_status()
print(json.dumps(response.json(), indent=2))
```

```json
{
	"meta": {
		"count": 1
	},
	"data": [
		{
			"attributes": {
				"registry_keys_opened": [
					"HKEY_CURRENT_USER\\",
					"HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_BROWSER_EMULATION",
					"HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Network\\Location Awareness",
					...
				],
				"verdicts": [
					"CLEAN"
				],
				"registry_keys_set": [
					{
						"key": "HKEY_LOCAL_MACHINE\\System\\Acrobatviewercpp473"
					},
					{
						"key": "HKEY_CURRENT_USER\\Software\\Adobe\\Acrobat Reader\\DC\\SessionManagement\\cWindowsCurrent\\cWin0"
					},
					...
				],
				"has_pcap": true,
				"files_written": [
					"C:\\Users\\user\\AppData\\LocalLow\\Adobe\\AcroCef\\DC\\Acrobat\\Cache\\Cache\\data_0",
					"C:\\Users\\user\\AppData\\LocalLow\\Adobe\\AcroCef\\DC\\Acrobat\\Cache\\Cache\\data_1",
					"C:\\Users\\user\\AppData\\LocalLow\\Adobe\\AcroCef\\DC\\Acrobat\\Cache\\Cache\\data_2",
					...
				],
				"has_evtx": true,
				"processes_tree": [
					{
						"process_id": "5496",
						"name": "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe\" \"C:\\Users\\user\\Desktop\\Brochure 20mm.pdf",
						"children": [
							{
								"process_id": "7820",
								"name": "\"C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroCEF\\RdrCEF.exe\" --backgroundcolor=16514043",
								"children": [
									{
										"process_id": "7608",
										"name": "\"C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroCEF\\RdrCEF.exe\" --type=renderer --log-file=\"C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroCEF\\debug.log\" --touch-events=enabled --field-trial-handle=1732,11530644702168122735,15720082148339357008,131072 --disable-features=NetworkService,VizDisplayCompositor --disable-gpu-compositing --lang=en-US --disable-pack-loading --log-file=\"C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroCEF\\debug.log\" --log-severity=disable --product-version=\"ReaderServices/21.1.20142 Chrome/80.0.0.0\" --device-scale-factor=1 --num-raster-threads=2 --enable-main-frame-before-activation --service-request-channel-token=5085289536417954428 --renderer-client-id=2 --mojo-platform-channel-handle=1748 --allow-no-sandbox-job /prefetch:1"
									},
									{
										"process_id": "5312",
										"name": "\"C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroCEF\\RdrCEF.exe\" --type=gpu-process --field-trial-handle=1732,11530644702168122735,15720082148339357008,131072 --disable-features=NetworkService,VizDisplayCompositor --disable-pack-loading --log-file=\"C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroCEF\\debug.log\" --log-severity=disable --product-version=\"ReaderServices/21.1.20142 Chrome/80.0.0.0\" --lang=en-US --gpu-preferences=KAAAAAAAAADgACAgAQAAAAAAAAAAAGAAAAAAABAAAAAIAAAAAAAAACgAAAAEAAAAIAAAAAAAAAAoAAAAAAAAADAAAAAAAAAAOAAAAAAAAAAQAAAAAAAAAAAAAAAFAAAAEAAAAAAAAAAAAAAABgAAABAAAAAAAAAAAQAAAAUAAAAQAAAAAAAAAAEAAAAGAAAA --use-gl=swiftshader-webgl --log-file=\"C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroCEF\\debug.log\" --service-request-channel-token=18430003972017308904 --mojo-platform-channel-handle=1768 --allow-no-sandbox-job --ignored=\" --type=renderer \" /prefetch:2"
									},
									...
								]
							}
						]
					}
				],
				"sandbox_name": "Zenbox",
				"has_html_report": true,
				"sigma_analysis_results": [
					{
						"rule_title": "Failed Code Integrity Checks",
						"rule_source": "Sigma Integrated Rule Set (GitHub)",
						"match_context": [
							{
								"values": {
									"EventID": "5038",
									"param1": "\\Device\\HarddiskVolume4\\Program Files (x86)\\sandbox\\driver\\sandbox-driver.sys"
								}
							}
						],
						"rule_level": "low",
						"rule_description": "Code integrity failures may indicate tampered executables.",
						"rule_author": "Thomas Patzke",
						"rule_id": "134564d292d785dff102940b8a1ee06dba2d462c5fb852124b3771a49d7885f1"
					}
				],
				"behash": "e5decb20b0c6fcc0767b798982aea4f2",
				"files_deleted": [
					"C:\\Users\\user\\AppData\\LocalLow\\Adobe\\AcroCef\\DC\\Acrobat\\Cache\\Code Cache\\js\\05349744be1ad4ad_0",
					"C:\\Users\\user\\AppData\\LocalLow\\Adobe\\AcroCef\\DC\\Acrobat\\Cache\\Code Cache\\js\\0786087c3c360803_0",
					"C:\\Users\\user\\AppData\\LocalLow\\Adobe\\AcroCef\\DC\\Acrobat\\Cache\\Code Cache\\js\\0998db3a32ab3f41_0",
					...
				],
				"files_dropped": [
					{
						"path": "C:\\Users\\user\\AppData\\LocalLow\\Adobe\\AcroCef\\DC\\Acrobat\\Cache\\Code Cache\\js\\index-dir\\temp-index",
						"sha256": "5a2c37f13ef74686a5196d3471f93bf3f6a357fd583518a9e888276bb217e2d8",
						"type": "DOS_COM"
					},
					{
						"path": "C:\\Users\\user\\AppData\\LocalLow\\Adobe\\AcroCef\\DC\\Acrobat\\Cache\\Code Cache\\js\\index-dir\\the-real-index (copy)",
						"sha256": "5a2c37f13ef74686a5196d3471f93bf3f6a357fd583518a9e888276bb217e2d8",
						"type": "DOS_COM"
					},
					{
						"path": "C:\\Users\\user\\AppData\\LocalLow\\Adobe\\AcroCef\\DC\\Acrobat\\Cache\\LOG",
						"sha256": "747870c7db49764621d7a0946b5178e346518dd29e92d1b439acc52e2352405e",
						"type": "TEXT"
					},
					{
						"path": "C:\\Users\\user\\AppData\\LocalLow\\Adobe\\AcroCef\\DC\\Acrobat\\Cache\\LOG.old (copy)",
						"sha256": "747870c7db49764621d7a0946b5178e346518dd29e92d1b439acc52e2352405e",
						"type": "TEXT"
					},
					{
						"path": "C:\\Users\\user\\AppData\\LocalLow\\Adobe\\Acrobat\\DC\\ConnectorIcons\\icon-220802010045Z-184.bmp",
						"sha256": "fb79cdfafade57af83d686de9b52d7e541b1cbbe23eb30de1a5404582eb2118c",
						"type": "BMP"
					},
					{
						"path": "C:\\Users\\user\\AppData\\Local\\Adobe\\Acrobat\\DC\\SOPHIA\\Reader\\Files\\DC_READER_LAUNCH_CARD",
						"sha256": "7dbc1d8484794af808f7a91d72f34a136e6f5791b067e149f2a486c07266c987",
						"type": "TEXT"
					},
					{
						"path": "C:\\Users\\user\\AppData\\Local\\Adobe\\Acrobat\\DC\\SOPHIA\\Reader\\Files\\DC_Reader_RHP_Banner",
						"sha256": "57f36d0e0e83b06d8420b15e8d2f2e2345f731da31e12b82cf03de794ed8ddb7",
						"type": "TEXT"
					},
					{
						"path": "C:\\Users\\user\\AppData\\Local\\Adobe\\Acrobat\\DC\\SOPHIA\\Reader\\Files\\DC_Reader_RHP_Retention",
						"sha256": "a3df133cbe796b03dd572be8012ba34ab2ffb47f79ab9b53f250d9ab3c6a14af",
						"type": "TEXT"
					},
					{
						"path": "C:\\Users\\user\\AppData\\Local\\Adobe\\Acrobat\\DC\\SOPHIA\\Reader\\Files\\Edit_InApp_Aug2020",
						"sha256": "7a7be507d7521b0657071c7173167afcb9e3921927cf40d20eb3354fb001026c",
						"type": "TEXT"
					},
					{
						"path": "C:\\Users\\user\\AppData\\Local\\Adobe\\Acrobat\\DC\\SOPHIA\\Reader\\SOPHIA.json",
						"sha256": "479aa59f277814c9a3f33feb8a18ab04a1a624c4a8a5089b3fff64bef596fcc3",
						"type": "TEXT"
					},
					{
						"path": "C:\\Users\\user\\AppData\\Local\\Temp\\A9rxllkn_j4deps_48o.tmp",
						"sha256": "44017dcb197aec2e68d12f3ca8c7401ab00b157d03fb4c93d724f6fa5e22c3c9",
						"type": "PDF"
					}
				],
				"owner": "virustotal",
				"has_memdump": true,
				"mutexes_created": [
					"\\Sessions\\1\\BaseNamedObjects\\Local\\Acrobat Instance Mutex",
					"\\Sessions\\1\\BaseNamedObjects\\DBWinMutex",
					"\\Sessions\\1\\BaseNamedObjects\\com.adobe.acrobat.rna.RdrCefBrowserLock.DC"
				],
				"files_opened": [
					"C:\\Program Files (x86)",
					"C:\\Program Files (x86)\\",
					"C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\",
					...
				]
			},
			"type": "private_file_behaviour",
			"id": "6b4bb405d3deea7a63e3ed02dd62a59c69b9458c15a901f3607429325b228ae8_Zenbox-1659370675",
			"links": {
				"self": "https://www.virustotal.com/api/v3/private/file_behaviours/6b4bb405d3deea7a63e3ed02dd62a59c69b9458c15a901f3607429325b228ae8_Zenbox-1659370675"
			}
		}
	],
	"links": {
		"self": "https://www.virustotal.com/api/v3/private/files/6b4bb405d3deea7a63e3ed02dd62a59c69b9458c15a901f3607429325b228ae8/behaviours?limit=10"
	}
}
```

From the sandbox reports we can also retrieve the ATT\&CK techniques observed during the executions. This can be done via the `attack_techniques` relationship, or using the [/files/\{id}/behaviour\_mitre\_trees](private-files/private-files-relationships.md) endpoint:

```python
import json
import requests

api_key = 'your_api_key_here'
sha256 = 'sha256_of_the_file'

headers = {'x-apikey': api_key}

response = requests.get(
  'https://www.virustotal.com/api/v3/private/files/{}/behaviour_mitre_trees'.format(sha256),
  headers=headers)
response.raise_for_status()
print(json.dumps(response.json(), indent=2))
```

```json Example
{
	"data": {
		"Zenbox": {
			"tactics": [
				{
					"description": "The adversary is trying to get into your network.\n\nInitial Access consists of techniques that use various entry vectors to gain their initial foothold within a network. Techniques used to gain a foothold include targeted spearphishing and exploiting weaknesses on public-facing web servers. Footholds gained through initial access may allow for continued access, like valid accounts and use of external remote services, or may be limited-use due to changing passwords.",
					"techniques": [
						{
							"description": "Adversaries may gain access to a system through a user visiting a website over the normal course of browsing. With this technique, the user's web browser is typically targeted for exploitation, but adversaries may also use compromised websites for non-exploitation behavior such as acquiring Application Access Token.\nMultiple ways of delivering exploit code to a browser exist, including:\n\nA legitimate website is compromised where adversaries have injected some form of malicious code such as JavaScript, iFrames, and cross-site scripting.\nMalicious ads are paid for and served through legitimate ad providers.\nBuilt-in web application interfaces are leveraged for the insertion of any other kind of object that can be used to display web content or contain a script that executes on the visiting client (e.g. forum posts, comments, and other user controllable web content).\n\nOften the website used by an adversary is one visited by a specific community, such as government, a particular industry, or region, where the goal is to compromise a specific user or set of users based on a shared interest. This kind of targeted campaign is often referred to a strategic web compromise or watering hole attack. There are several known examples of this occurring.\nTypical drive-by compromise process:\n\nA user visits a website that is used to host the adversary controlled content.\nScripts automatically execute, typically searching versions of the browser and plugins for a potentially vulnerable version. \nThe user may be required to assist in this process by enabling scripting or active website components and ignoring warning dialog boxes.\n\n\nUpon finding a vulnerable version, exploit code is delivered to the browser.\nIf exploitation is successful, then it will give the adversary code execution on the user's system unless other protections are in place.\nIn some cases a second visit to the website after the initial scan is required before exploit code is delivered.\n\n\n\nUnlike Exploit Public-Facing Application, the focus of this technique is to exploit software on a client endpoint upon visiting a website. This will commonly give an adversary access to systems on the internal network instead of external systems that may be in a DMZ.\nAdversaries may also use compromised websites to deliver a user to a malicious application designed to Steal Application Access Tokens, like OAuth tokens, to gain access to protected applications and information. These malicious applications have been delivered through popups on legitimate websites.",
							"signatures": [
								{
									"severity": "INFO",
									"description": "High memory usage for Adobe Reader (potential heap spray)"
								}
							],
							"link": "https://attack.mitre.org/techniques/T1189/",
							"id": "T1189",
							"name": "Drive-by Compromise"
						}
					],
					"link": "https://attack.mitre.org/tactics/TA0001/",
					"id": "TA0001",
					"name": "Initial Access"
				},
				{
					"description": "The adversary is trying to figure out your environment.\n\nDiscovery consists of techniques an adversary may use to gain knowledge about the system and internal network. These techniques help adversaries observe the environment and orient themselves before deciding how to act. They also allow adversaries to explore what they can control and what’s around their entry point in order to discover how it could benefit their current objective. Native operating system tools are often used toward this post-compromise information-gathering objective. ",
					"techniques": [
						{
							"description": "Adversaries may enumerate files and directories or may search in specific locations of a host or network share for certain information within a file system. Adversaries may use the information from File and Directory Discovery during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.\nMany command shell utilities can be used to obtain this information. Examples include dir, tree, ls, find, and locate. Custom tools may also be used to gather file and directory information and interact with the Native API. Adversaries may also leverage a Network Device CLI on network devices to gather file and directory information.",
							"signatures": [
								{
									"severity": "INFO",
									"description": "Reads ini files"
								}
							],
							"link": "https://attack.mitre.org/techniques/T1083/",
							"id": "T1083",
							"name": "File and Directory Discovery"
						},
						{
							"description": "An adversary may attempt to get detailed information about the operating system and hardware, including version, patches, hotfixes, service packs, and architecture. Adversaries may use the information from System Information Discovery during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.\nTools such as Systeminfo can be used to gather detailed system information. If running with privileged access, a breakdown of system data can be gathered through the systemsetup configuration tool on macOS. As an example, adversaries with user-level access can execute the df -aH command to obtain currently mounted disks and associated freely available space. Adversaries may also leverage a Network Device CLI on network devices to gather detailed system information. System Information Discovery combined with information gathered from other forms of discovery and reconnaissance can drive payload development and concealment.\nInfrastructure as a Service (IaaS) cloud providers such as AWS, GCP, and Azure allow access to instance and virtual machine information via APIs. Successful authenticated API calls can return data such as the operating system platform and status of a particular instance or the model view of a virtual machine.",
							"signatures": [
								{
									"severity": "INFO",
									"description": "Reads software policies"
								}
							],
							"link": "https://attack.mitre.org/techniques/T1082/",
							"id": "T1082",
							"name": "System Information Discovery"
						}
					],
					"link": "https://attack.mitre.org/tactics/TA0007/",
					"id": "TA0007",
					"name": "Discovery"
				},
				{
					"description": "The adversary is trying to avoid being detected.\n\nDefense Evasion consists of techniques that adversaries use to avoid detection throughout their compromise. Techniques used for defense evasion include uninstalling/disabling security software or obfuscating/encrypting data and scripts. Adversaries also leverage and abuse trusted processes to hide and masquerade their malware. Other tactics’ techniques are cross-listed here when those techniques include the added benefit of subverting defenses. ",
					"techniques": [
						{
							"description": "Adversaries may inject code into processes in order to evade process-based defenses as well as possibly elevate privileges. Process injection is a method of executing arbitrary code in the address space of a separate live process. Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via process injection may also evade detection from security products since the execution is masked under a legitimate process. \nThere are many different ways to inject code into a process, many of which abuse legitimate functionalities. These implementations exist for every major OS but are typically platform specific. \nMore sophisticated samples may perform multiple process injections to segment modules and further evade detection, utilizing named pipes or other inter-process communication (IPC) mechanisms as a communication channel. ",
							"signatures": [
								{
									"severity": "INFO",
									"description": "Spawns processes"
								}
							],
							"link": "https://attack.mitre.org/techniques/T1055/",
							"id": "T1055",
							"name": "Process Injection"
						},
						{
							"description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly elevate privileges. EWM injection is a method of executing arbitrary code in the address space of a separate live process. \nBefore creating a window, graphical Windows-based processes must prescribe to or register a windows class, which stipulate appearance and behavior (via windows procedures, which are functions that handle input/output of data). Registration of new windows classes can include a request for up to 40 bytes of EWM to be appended to the allocated memory of each instance of that class. This EWM is intended to store data specific to that window and has specific application programming interface (API) functions to set and get its value.  \nAlthough small, the EWM is large enough to store a 32-bit pointer and is often used to point to a windows procedure. Malware may possibly utilize this memory location in part of an attack chain that includes writing code to shared sections of the process’s memory, placing a pointer to the code in EWM, then invoking execution by returning execution control to the address in the process’s EWM.\nExecution granted through EWM injection may allow access to both the target process's memory and possibly elevated privileges. Writing payloads to shared sections also avoids the use of highly monitored API calls such as WriteProcessMemory and CreateRemoteThread. More sophisticated malware samples may also potentially bypass protection mechanisms such as data execution prevention (DEP) by triggering a combination of windows procedures and other system functions that will rewrite the malicious payload inside an executable portion of the target process.   \nRunning code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via EWM injection may also evade detection from security products since the execution is masked under a legitimate process. ",
							"signatures": [
								{
									"severity": "INFO",
									"description": "Allocates a big amount of memory (probably used for heap spray)"
								}
							],
							"link": "https://attack.mitre.org/techniques/T1055/011/",
							"id": "T1055.011",
							"name": "Extra Window Memory Injection"
						},
						{
							"description": "Adversaries may attempt to manipulate features of their artifacts to make them appear legitimate or benign to users and/or security tools. Masquerading occurs when the name or location of an object, legitimate or malicious, is manipulated or abused for the sake of evading defenses and observation. This may include manipulating file metadata, tricking users into misidentifying the file type, and giving legitimate task or service names.\nRenaming abusable system utilities to evade security monitoring is also a form of Masquerading.",
							"signatures": [
								{
									"severity": "INFO",
									"description": "Creates files inside the user directory"
								}
							],
							"link": "https://attack.mitre.org/techniques/T1036/",
							"id": "T1036",
							"name": "Masquerading"
						}
					],
					"link": "https://attack.mitre.org/tactics/TA0005/",
					"id": "TA0005",
					"name": "Defense Evasion"
				},
				{
					"description": "The adversary is trying to gain higher-level permissions.\n\nPrivilege Escalation consists of techniques that adversaries use to gain higher-level permissions on a system or network. Adversaries can often enter and explore a network with unprivileged access but require elevated permissions to follow through on their objectives. Common approaches are to take advantage of system weaknesses, misconfigurations, and vulnerabilities. Examples of elevated access include: \n\n* SYSTEM/root level\n* local administrator\n* user account with admin-like access \n* user accounts with access to specific system or perform specific function\n\nThese techniques often overlap with Persistence techniques, as OS features that let an adversary persist can execute in an elevated context.  ",
					"techniques": [
						{
							"description": "Adversaries may inject code into processes in order to evade process-based defenses as well as possibly elevate privileges. Process injection is a method of executing arbitrary code in the address space of a separate live process. Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via process injection may also evade detection from security products since the execution is masked under a legitimate process. \nThere are many different ways to inject code into a process, many of which abuse legitimate functionalities. These implementations exist for every major OS but are typically platform specific. \nMore sophisticated samples may perform multiple process injections to segment modules and further evade detection, utilizing named pipes or other inter-process communication (IPC) mechanisms as a communication channel. ",
							"signatures": [
								{
									"severity": "INFO",
									"description": "Spawns processes"
								}
							],
							"link": "https://attack.mitre.org/techniques/T1055/",
							"id": "T1055",
							"name": "Process Injection"
						},
						{
							"description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly elevate privileges. EWM injection is a method of executing arbitrary code in the address space of a separate live process. \nBefore creating a window, graphical Windows-based processes must prescribe to or register a windows class, which stipulate appearance and behavior (via windows procedures, which are functions that handle input/output of data). Registration of new windows classes can include a request for up to 40 bytes of EWM to be appended to the allocated memory of each instance of that class. This EWM is intended to store data specific to that window and has specific application programming interface (API) functions to set and get its value.  \nAlthough small, the EWM is large enough to store a 32-bit pointer and is often used to point to a windows procedure. Malware may possibly utilize this memory location in part of an attack chain that includes writing code to shared sections of the process’s memory, placing a pointer to the code in EWM, then invoking execution by returning execution control to the address in the process’s EWM.\nExecution granted through EWM injection may allow access to both the target process's memory and possibly elevated privileges. Writing payloads to shared sections also avoids the use of highly monitored API calls such as WriteProcessMemory and CreateRemoteThread. More sophisticated malware samples may also potentially bypass protection mechanisms such as data execution prevention (DEP) by triggering a combination of windows procedures and other system functions that will rewrite the malicious payload inside an executable portion of the target process.   \nRunning code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via EWM injection may also evade detection from security products since the execution is masked under a legitimate process. ",
							"signatures": [
								{
									"severity": "INFO",
									"description": "Allocates a big amount of memory (probably used for heap spray)"
								}
							],
							"link": "https://attack.mitre.org/techniques/T1055/011/",
							"id": "T1055.011",
							"name": "Extra Window Memory Injection"
						}
					],
					"link": "https://attack.mitre.org/tactics/TA0004/",
					"id": "TA0004",
					"name": "Privilege Escalation"
				}
			]
		}
	},
	"links": {
		"self": "https://www.virustotal.com/api/v3/private/files/6b4bb405d3deea7a63e3ed02dd62a59c69b9458c15a901f3607429325b228ae8/behaviour_mitre_trees"
	}
}
```

This tree could be represented as well as:

```
MITRE ATT&CK tactics and techniques observed by sandbox
└── Zenbox
    ├── TA0001: Initial Access
    │   └── T1189: Drive-by Compromise
    │       └── High memory usage for Adobe Reader (potential heap spray)
    ├── TA0007: Discovery
    │   ├── T1083: File and Directory Discovery
    │   │   └── Reads ini files
    │   └── T1082: System Information Discovery
    │       └── Reads software policies
    ├── TA0005: Defense Evasion
    │   ├── T1055: Process Injection
    │   │   └── Spawns processes
    │   ├── T1055.011: Extra Window Memory Injection
    │   │   └── Allocates a big amount of memory (probably used for heap spray)
    │   └── T1036: Masquerading
    │       └── Creates files inside the user directory
    └── TA0004: Privilege Escalation
        ├── T1055: Process Injection
        │   └── Spawns processes
        └── T1055.011: Extra Window Memory Injection
            └── Allocates a big amount of memory (probably used for heap spray)
```

Now with the dropped files. In the behaviour report we can see several entries under `files_dropped`. Let's then use the [relationships endpoint](private-files/private-files-relationships.md) to retrieve the dropped files:

```python
import json
import requests

api_key = 'your_api_key_here'
sha256 = 'sha256_of_the_file'

headers = {'x-apikey': api_key}

response = requests.get(
  'https://www.virustotal.com/api/v3/private/files/{}/dropped_files'.format(sha256),
  headers=headers)
response.raise_for_status()
print(json.dumps(response.json(), indent=2))
```

```json
{
	"meta": {
		"count": 7
	},
	"data": [
    {
			"context_attributes": {
				"paths": [
					"C:\\Users\\user\\AppData\\LocalLow\\Adobe\\Acrobat\\DC\\ConnectorIcons\\icon-220818113819Z-179.bmp"
				],
				"type": "BMP"
			},
			"type": "private_file",
			"id": "fb79cdfafade57af83d686de9b52d7e541b1cbbe23eb30de1a5404582eb2118c",
			"error": {
				"message": "private_file with id \"fb79cdfafade57af83d686de9b52d7e541b1cbbe23eb30de1a5404582eb2118c\" not found",
				"code": "NotFoundError"
			}
		},
		{
			"context_attributes": {
				"paths": [
					"C:\\Users\\user\\AppData\\LocalLow\\Adobe\\AcroCef\\DC\\Acrobat\\Cache\\LOG",
					"C:\\Users\\user\\AppData\\LocalLow\\Adobe\\AcroCef\\DC\\Acrobat\\Cache\\LOG.old (copy)"
				],
				"type": "Text"
			},
			"type": "private_file",
			"id": "91b6de6bdaef3da90329719429752778496c90d09e18eb4fa9eb09450d491937",
			"error": {
				"message": "private_file with id \"91b6de6bdaef3da90329719429752778496c90d09e18eb4fa9eb09450d491937\" not found",
				"code": "NotFoundError"
			}
		},
		{
			"context_attributes": {
				"paths": [
					"C:\\Users\\user\\AppData\\Local\\Adobe\\Acrobat\\DC\\SOPHIA\\Reader\\Files\\DC_READER_LAUNCH_CARD"
				],
				"type": "Text"
			},
			"type": "private_file",
			"id": "87217f01115118d1f4ea31878e1adc116663cea1a84ee6d51e2247fd0192a487",
			"error": {
				"message": "private_file with id \"87217f01115118d1f4ea31878e1adc116663cea1a84ee6d51e2247fd0192a487\" not found",
				"code": "NotFoundError"
			}
		},
		{
			"context_attributes": {
				"paths": [
					"C:\\Users\\user\\AppData\\Local\\Adobe\\Acrobat\\DC\\SOPHIA\\Reader\\Files\\DC_Reader_RHP_Banner"
				],
				"type": "Text"
			},
			"type": "private_file",
			"id": "504f6ba85bdf4408314cf0149eb051e20c124d58dd81c6298d11339f41ae5920",
			"error": {
				"message": "private_file with id \"504f6ba85bdf4408314cf0149eb051e20c124d58dd81c6298d11339f41ae5920\" not found",
				"code": "NotFoundError"
			}
		},
		{
			"context_attributes": {
				"paths": [
					"C:\\Users\\user\\AppData\\Local\\Adobe\\Acrobat\\DC\\SOPHIA\\Reader\\Files\\DC_Reader_RHP_Retention"
				],
				"type": "Text"
			},
			"type": "private_file",
			"id": "415d833225520ab11e208bd5848e1615f0cb43a79cb14096e7bba993f9dd54e1",
			"error": {
				"message": "private_file with id \"415d833225520ab11e208bd5848e1615f0cb43a79cb14096e7bba993f9dd54e1\" not found",
				"code": "NotFoundError"
			}
		},
		{
			"context_attributes": {
				"paths": [
					"C:\\Users\\user\\AppData\\Local\\Adobe\\Acrobat\\DC\\SOPHIA\\Reader\\Files\\Edit_InApp_Aug2020"
				],
				"type": "Text"
			},
			"type": "private_file",
			"id": "84ca723d9b626787fb239593f71535752b003d21a34f0b02b8620ad761368283",
			"error": {
				"message": "private_file with id \"84ca723d9b626787fb239593f71535752b003d21a34f0b02b8620ad761368283\" not found",
				"code": "NotFoundError"
			}
		},
		{
			"context_attributes": {
				"paths": [
					"C:\\Users\\user\\AppData\\Local\\Adobe\\Acrobat\\DC\\SOPHIA\\Reader\\SOPHIA.json"
				],
				"type": "Text"
			},
			"type": "private_file",
			"id": "907ba5e8e68317f3ae8591b717e148bb1e4f5ff38ca3e2318c827ad997f0b18c",
			"error": {
				"message": "private_file with id \"907ba5e8e68317f3ae8591b717e148bb1e4f5ff38ca3e2318c827ad997f0b18c\" not found",
				"code": "NotFoundError"
			}
		}
	],
	"links": {
		"self": "https://www.virustotal.com/api/v3/private/files/6b4bb405d3deea7a63e3ed02dd62a59c69b9458c15a901f3607429325b228ae8/dropped_files?limit=10"
	}
}
```

Apart from the context attributes for each of the file, which indicates us the paths where these files were dropped and the file types, we see a `NotFoundError` for all of them. This is normal since we didn't scan these files yet. Let's analyse the first dropped file for example, by using the `/files/{sha256}/analyse` endpoint:

```python
import requests

api_key = 'your_api_key_here'
sha256 = 'sha256_of_the_dropped_file'

params = {
  'enable_internet': True  # true by default
}
# You can also specify the command line arguments of the file as well
# params['command_line'] = '/s'

response = requests.post(
  'https://www.virustotal.com/api/v3/private/files/{}/analyse'.format(sha256),
  params=params, headers=headers)
response.raise_for_status()

print('Analysis ID: {}'.format(response.json()['data']['id']))
```

Again, we will get a private analysis ID:

```json
{
	"data": {
		"type": "private_analysis",
		"id": "ZmI5Y2VmNGJmZDIwZTkzNmQ5MzY0NTcwMGI2Nzc2M2Q6Tm9uZToxNjYwODI1NDE1"
	}
}
```

And finally we can use this ID to track the analysis progress as before and check the resulting file report as well.

---

← [Delete subscription from a report](../05-reports-analysis/reports/delete-report-subscription-preferences.md) · [up](README.md) · [Upload a file](private-files/upload-file-private-scanning.md) →

*Archived from <https://gtidocs.virustotal.com/reference/private-files>.*
