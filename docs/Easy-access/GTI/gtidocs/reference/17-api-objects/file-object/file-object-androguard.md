---
title: "androguard"
source: https://gtidocs.virustotal.com/reference/file-object-androguard
slug: file-object-androguard
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:01.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › androguard

---

# androguard

information about Android files.

`androguard` shows information about Android APK, DEX and AXML files, extracted with the [Androguard](https://github.com/androguard/androguard) tool.

* `Activities`: <*list of strings*> containing the app's activity names.
* `AndroguardVersion`: <*string*> used Androguard version.
* `AndroidApplication`: <*integer*> Android file type in integer format.
* `AndroidApplicationError`: <*boolean*> whether there was an error processing the application or not.
* `AndroidApplicationInfo`: <*string*> Android file type in readable form ("APK", "DEX", "AXML").
* `AndroidVersionCode`: <*string*> Android version code, read from the manifest.
* `AndroidVersionName`: <*string*> Android version name, read from the manifest.
* `Libraries`: <*list of strings*> containing the app's used library names.
* `main_activity`: <*string*> main activity name, read from the manifest.
* `MinSdkVersion`: <*string*> minimum supported SDK version.
* `Package`: <*string*> package name, read from the manifest.
* `Providers`: <*list of strings*> contains the app's used providers.
* `Receivers`: <*list of strings*> contains the app's used receivers.
* `RiskIndicator`: <*dictionary*> contains two keys: "APK" (structure) and "PERM" (permissions) risk indicators.
  * `APK`: <*dictionary*> names used components and how many there are (i.e. "EXECUTABLE": 3). Keys are strings and values are integers.
  * `PERM`: <*dictionary*> names types of permissions and how many there are (i.e. "DANGEROUS": 11). Keys are strings and values are integers.
* `Services`: <*list of strings*> contains the app's used services.
* `StringsInformation`: <*list of strings*> contains interesting strings found in the app.
* `TargetSdkVersion`: <*string*> Android version the app has been tested for.
* `VTAndroidInfo`: <*float*> internal version of the Androguard tool used by VT.
* `certificate`: <*SSL Certificate*> app certificate details. Check [SSL Certificate](../ssl-certificate-object.md) object to know more about its structure.
* `intent_filters`: <*dictionary*> contains the app's intent filters. The dictionary contains three subfields:
  * `Activities`: <*dictionary*>: intent filters from activities.
    * `action`: <*list of strings*>: defined actions.
    * `category`: <*list of strings*> defined categories.
  * `Receivers`: <*dictionary*> intent filters from receivers.
    * `action`: <*list of strings*> defined actions.
    * `category`: <*list of strings*> defined categories.
  * `Services`: <*dictionary*> intent filters for services.
    * `action`: <*list of strings*> defined actions.
    * `category`: <*list of strings*> defined categories.
* `permission_details`: <*dictionary*> details about the app's required permissions. Keys are permission names and values are dictionaries containing the following fields:
  * `full_description`: <*string*> describes the permission with more detail.
  * `permission_type`: <*string*> describes the type of permission (i.e. normal, dangerous, etc).
  * `short_description`: <*string*> short summary describing the permission.

```json Android APK information
{
  "data": {
		...
    "attributes" : {
      ...
      "androguard": {
        "Activities": ["<strings>"],
        "AndroguardVersion": "<string>",
        "AndroidApplication": <int>,
        "AndroidApplicationError": <boolean>,
        "AndroidApplicationInfo": "<string>",
        "AndroidVersionCode": "<string>",
        "AndroidVersionName": "<string>",
        "Libraries": ["<strings>"],
        "main_activity": "<string>",
        "MinSdkVersion": "<string>",
        "Package": "<string>",
        "Providers": ["<strings>"],
        "Receivers": ["<strings>"],
        "RiskIndicator": {"APK": {"<string>": <int>, ... },
                          "PERM": {"<string>": <int>, ... }},
        "Services": ["<strings>"],
        "StringsInformation": ["<strings>"],
        "TargetSdkVersion": "<string>",
        "VTAndroidInfo": <float>,
        "certificate": {"Issuer": {"DN": "<string>", "O": "<string>", ... },
                        "Subject": {"DN": "<string>","O": "<string>", ... },
                        "serialnumber": "<string>",
                        "thumbprint": "<string>",
                        "validfrom": "<string:%H:%M %p %m/%d/%Y>",
                        "validto": "<string:%H:%M %p %m/%d/%Y>"},
        "intent_filters": {
          	"Activities": {
              	"<string>": {
                  	"action": ["<strings>"],
                 		"category": ["<string>"]
                },...
           	},
            "Receivers": {
              	"<string>": {
                  	"action": ["<strings>"],
                		"category": ["<string>"]
                },...
          	},
            "Services": {
              	"<string>": {
                  	"action": ["<strings>"],
                    "category": ["<string>"]
                },...
             }
         },
         "pemission_details": {
           	"<string>": {
              	"full_description": "<string>",
                "permission_type": "<string>",
                "short_description": "<string>"
            },...
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
            "androguard": {
                "Activities": [
                    "com.blabla.camera.controller.CameraActivity",
                    "com.blabla.camera.controller.SecureCameraActivity",
                    "com.blabla.camera.thirdparty.qrcode.QrCodeActivity",
                    "com.blabla.rapidcapture.RapidPlaceHolderActivity"
                ],
                "AndroguardVersion": "3.0-dev",
                "AndroidApplication": 1,
                "AndroidApplicationError": false,
                "AndroidApplicationInfo": "APK",
                "AndroidVersionCode": "1",
                "AndroidVersionName": "5.1-eng.blabla.20160527.160933",
                "Libraries": [
                    "com.blabla.audioalgo",
                    "com.blabla.blablapostcamera"
                ],
                "main_activity": "com.blabla.blabla.view.activity.Blabla",
                "MinSdkVersion": "16",
                "Package": "com.blabla.camera",
                "Providers": [
                    "com.blablabla.camera.model.PreferenceProvider"
                ],
                "Receivers": [
                    "com.sec.android.app.blabla.broadcast.Blablabl",
                    "com.sec.android.app.blablabla.blabla.DeleteProfileReceiver",
                    "com.sec.android.app.blabla.broadcast.ResetDataReceiver"
                ],
                "RiskIndicator": {
                    "APK": {},
                    "PERM": {
                        "DANGEROUS": 5,
                        "GPS": 2,
                        "INTERNET": 1,
                        "NORMAL": 6,
                        "PRIVACY": 5,
                        "SIGNATUREORSYSTEM": 2,
                        "SIGNATUREORSYSTEMORDEVELOPMENT": 1
                    }
                },
                "Services": [
                    "com.blabla.camera.model.storage.StorageService",
                    "com.blablabla.camera.controller.BatteryDetectService",
                    "com.blabla.rapidcapture.RapidCaptureService",
                    "com.blablabla.camera.controller.DaemonService"
                ],
                "StringsInformation": [
                    "https://",
                    "https://dc.di.atlas.blabla.com",
                    "https://regi.di.atlas.blabla.com",
                    "https://stg-api.di.atlas.blabla.com"
                ],
                "TargetSdkVersion": "19",
                "VTAndroidInfo": 1.41,
                "certificate": {
                    "Issuer": {
                        "C": "CN",
                        "CN": "MyName",
                        "DN": "C:CN, CN:MyName, L:Beijing, O:Blabla, ST:Beijing, OU:Blablabla",
                        "L": "Beijing",
                        "O": "Blabla",
                        "OU": "Blablabla",
                        "ST": "Beijing"
                    },
                    "Subject": {
                        "C": "CN",
                        "CN": "MyName",
                        "DN": "C:CN, CN:MyName, L:Beijing, O:Blablabla, ST:Beijing, OU:Blablabla",
                        "L": "Beijing",
                        "O": "Blablabla",
                        "OU": "Blablabla",
                        "ST": "Beijing"
                    },
                    "serialnumber": "b155424bb4743446",
                    "thumbprint": "af54c24d4240644e64a0c4d742944a64964c4448",
                    "validfrom": "2015-05-14 11:13:58",
                    "validto": "2042-09-29 11:13:58"
                },
                "intent_filters": {
                    "Activities": {
                        "com.blabla.camera.controller.SecureCameraActivity": {
                            "action": [
                                "android.media.action.STILL_IMAGE_CAMERA_SECURE",
                                "android.media.action.IMAGE_CAPTURE_REMOTE_CONTROL",
                                "android.media.action.IMAGE_CAPTURE_SECURE"
                            ],
                            "category": [
                                "android.intent.category.DEFAULT"
                            ]
                        },
                        "com.blablabla.camera.thirdparty.qrcode.QrCodeActivity": {
                            "action": [
                                "com.blablabla.camera.qrcode.SCAN"
                            ],
                            "category": [
                                "android.intent.category.DEFAULT"
                            ]
                        }
                    },
                    "Receivers": {},
                    "Services": {
                        "com.blablabla.rapidcapture.RapidCaptureService": {
                            "action": [
                                "com.blablabla.RapidCapture"
                            ]
                        }
                    }
                },
                "permission_details": {
                    "android.permission.ACCESS_COARSE_LOCATION": {
                        "full_description": "Access coarse location sources, such as the mobile network database, to determine an approximate phone location, where available. Malicious applications can use this to determine approximately where you are.",
                        "permission_type": "dangerous",
                        "short_description": "coarse (network-based) location"
                    },
                    "android.permission.ACCESS_FINE_LOCATION": {
                        "full_description": "Access fine location sources, such as the Global Positioning System on the phone, where available. Malicious applications can use this to determine where you are and may consume additional battery power.",
                        "permission_type": "dangerous",
                        "short_description": "fine (GPS) location"
                    },
                    "android.permission.ACCESS_NETWORK_STATE": {
                        "full_description": "Allows an application to view the status of all networks.",
                        "permission_type": "normal",
                        "short_description": "view network status"
                    },
                    "android.permission.ACCESS_WEATHERCLOCK_PROVIDER": {
                        "full_description": "Unknown permission from android reference",
                        "permission_type": "normal",
                        "short_description": "Unknown permission from android reference"
                    }
                }
            }
        }
    }
}
```

---

← [signature_info](file-object-signature-info.md) · [up](../README.md) · [asf_info](file-object-asf-info.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-androguard>.*
