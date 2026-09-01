---
title: "ipa_info"
source: https://gtidocs.virustotal.com/reference/file-object-ipa-info
slug: file-object-ipa-info
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:12.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › ipa_info

---

# ipa_info

information about iOS App Store Package files.

`ipa_info` returns infomation about [Apple IPA files](https://en.wikipedia.org/wiki/.ipa).

* `apps`: <*list of macho\_info objects*> each item on the list contains metadata information from one of the Mach-O executables inside the app. Check the [macho\_info](file-object-macho-info.md) reference to get more information about the fields contained in each dictionary of the list.
* `itunes`: <*dictionary*> contains the information stored at the [`iTunesMetadata.plist`](https://docs.microsoft.com/en-us/xamarin/ios/deploy-test/app-distribution/itunesmetadata?tabs=macos) file. This file is used to provide information to iTunes about an iOS application. Returned fields may change from file to file.
* `plist`: <*dictionary*> contains the information stored at the [`Info.plist`](https://developer.apple.com/documentation/bundleresources/information_property_list) file. Every app and plug-in uses an `Info.plist` file to store configuration data in a place where the system can easily access it. OS X and iOS use `Info.plist` files to determine what icon to display for a bundle, what document types are supported, and many other behaviours that have an impact outside the bundle itself. The returned fields may change, since not all apps have the same `Info.plist` file, but the most common returned fields are:
  * `CBundleIdentifier`: <*string*> unique identifier for a bundle. [More info](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleidentifier).
  * `CFBundleSupportedPlatforms`: <*list of strings*> list of supported platforms.
  * `CFAppleHelpAnchor`: <*string*> the name of the bundle's HTML help file. [More info](https://developer.apple.com/documentation/bundleresources/information_property_list/cfapplehelpanchor).
  * `CFBundleIcons`: <*dictionary*> information about all the icons used. [More info](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleicons). Every subitem is a dictionary having the icon type as key and a the following subkeys:
    * `CFBundleIconFiles`: <*list of strings*> icon file names. [More info](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleiconfiles).
    * `CFBundleIconName`: <*string*> the name of the asset that represents the app icon. [More info](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleiconname).
  * `CFBundleInfoDictionaryVersion`: <*string*> the current version of the Information Property List structure. [More info](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleinfodictionaryversion).
  * `CFBundleShortVersionString`: <*string*> release or version number of the bundle. [More info](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring).
  * `CFBundleDisplayName`: <*string*> user-visible name of the bundle. [More info](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundledisplayname).
  * `CFBundleName`: <*string*> user-visible short name for the bundle. [More info](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundlename).
  * `CFBundlePackageType`: <*string*> bundle type. [More info](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundlepackagetype).
  * `CFBundleSignature`: <*string*> The Bundle Signature is analogous to the "Creator Code" found in classic MacOS and exists only for compatibility with classic MacOS apps and documents. Modern apps don't need to worry about assiging a bundle signature. It is initialized as "????" in new Xcode projects.
  * `CFBundleDevelopmentRegion`: <*string*> the default language and region for the bundle, as a language ID. [More info](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundledevelopmentregion).
  * `CFBundleExecutable`: <*string*> the name of the bundle’s executable file. [More info](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleexecutable).
  * `MinimumOSVersion`: <*string*> the miminimum operating system version required for the app to run on iOS, tvOS, and watchOS. [More info](https://developer.apple.com/documentation/bundleresources/information_property_list/minimumosversion).
* `provision`: <*dictionary*> contains information stored at the `embedded.mobileprovision` file. This file is embedded into the app and is required for the app to be accepted onto the Apple App Store. The provisioning profile is used to sign the app and it's necessary to install and run it on a device. The returned fields may change, since not all apps have the same provision file, but the most common returned fields are:
  * `AppIDName`: <*string*> application ID name.
  * `ApplicationIdentifierPrefix`: <*list of strings*> code signing identifier for the running app.
  * `CreationDate`: <*string*> date of app creation in `%Y-%m-%d %H:%M:%S` [format](http://strftime.org/).
  * `Entitlements`: <*dictionary*> allows a specific capability or opts the app into a specific service. [More info](https://developer.apple.com/documentation/bundleresources/entitlements). Additional subfields may appear, but some common ones are:
    * `application-identifier`: <*string*> complete application identifier.
    * `get-task-allow`: <*boolean*>
    * `keychain-access-groups`: <*list of strings*> the identifiers for the keychain groups that the app may share items with. [More info](https://developer.apple.com/documentation/bundleresources/entitlements/keychain-access-groups).
  * `ExpirationDate`: <*string*> app expiration date in `%Y-%m-%d %H:%M:%S` [format](http://strftime.org/).
  * `Name`: <*string*> application name.
  * `Platform`: <*list of strings*> supported platforms.
  * `TeamIdentifier`: <*list of strings*> team identifier.
  * `TeamName`: <*string*> team name.
  * `TimeToLive`: <*integer*> number of days in which the app is valid.
  * `UUID`: <*string*> unique identifier.
  * `Version`: <*integer*> app version.

```json Apple IPA files
{
    "data": {
        "attributes": {
            "ipa_info": {
                "apps": [
                    <MACHO_INFO>
                ],
                "plist": {
                    "CFBundleDevelopmentRegion": "<string>",
                    "CFBundleDisplayName": "<string>",
                    "CBundleIdentifier": "<string>",
                    "CFBundleSupportedPlatforms": ["<string>",...],
                    "CFAppleHelpAnchor": "<string>",
                    "CFBundleIcons": {
                      "<string>": {
                        "CFBundleIconFiles": ["<string>",...],
                        "CFBundleIconName": "<string>"
                      }, ...
                    },
                    "CFBundleInfoDictionaryVersion": "<string>",
                    "CFBundleShortVersionString": "<string>",
                    "CFBundleName": "<string>",
                    "CFBundlePackageType": "<string>",
                    "CFBundleSignature": "<string>",
                    "MinimumOSVersion": "<string>",
                    "<string>": <value>...
                },
                "provision": {
                    "AppIDName": "<string>",
                    "ApplicationIdentifierPrefix": [
                        "<string>"
                    ],
                    "CreationDate": "<string:%Y-%m-%d %H:%M:%S>",
                    "Entitlements": {
                        "application-identifier": "<string>",
                        "get-task-allow": false,
                        "keychain-access-groups": [
                            "<string>"
                        ],
                        "<string>": <value>
                    },
                    "ExpirationDate": "<string:%Y-%m-%d %H:%M:%S>",
                    "Name": "<string>",
                    "Platform": [
                        "<string>"
                    ],
                    "TeamIdentifier": [
                        "<string>"
                    ],
                    "TeamName": "<string>",
                    "TimeToLive": <int>,
                    "UUID": "<string>",
                    "Version": <int>
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
            "ipa_info": {
                "apps": [
                    {
                        "commands": [
                            {
                                "type": "LC_DYLD_INFO_ONLY"
                            },
                            {
                                "type": "LC_SYMTAB"
                            },
                            {
                                "type": "LC_DYSYMTAB"
                            },
                            {
                                "type": "LC_LOAD_DYLINKER"
                            },
                            {
                                "type": "LC_UUID"
                            }
                        ],
                        "headers": {
                            "cpu_subtype": "ARM_V7",
                            "cpu_type": "ARM",
                            "entrypoint": "0xe5ed",
                            "file_type": "executable file",
                            "flags": [
                                "BINDS_TO_WEAK",
                                "DYLDLINK",
                                "NOUNDEFS",
                                "PIE",
                                "TWOLEVEL",
                                "WEAK_DEFINES"
                            ],
                            "magic": "0xfeedface",
                            "num_cmds": 54,
                            "size_cmds": 5564
                        },
                        "libs": [
                            "/System/Library/Frameworks/blabla.framework/blablabla",
                            "/System/Library/Frameworks/bleble.framework/blebleble"
                        ],
                        "segments": [
                            {
                                "fileoff": "0x0",
                                "filesize": "0x0",
                                "name": "__PAGEZERO",
                                "sections": [],
                                "vmaddr": "0x0",
                                "vmsize": "0x4000"
                            },
                            {
                                "fileoff": "0x0",
                                "filesize": "0x990000",
                                "name": "__TEXT",
                                "sections": [
                                    {
                                        "flags": [
                                            "SECTION_ATTRIBUTES_USR",
                                            "SECTION_ATTRIBUTES_SYS"
                                        ],
                                        "name": "__text",
                                        "type": "S_REGULAR"
                                    },
                                    {
                                        "flags": [
                                            "SECTION_ATTRIBUTES_USR",
                                            "SECTION_ATTRIBUTES_SYS"
                                        ],
                                        "name": "__picsymbolstub4",
                                        "type": "S_SYMBOL_STUBS"
                                    }
                                ],
                                "vmaddr": "0x4000",
                                "vmsize": "0x990000"
                            }
                        ],
                        "tags": [
                            "arm"
                        ],
                        "vhash": "8515a158945ee205dba8592253dc5a5f"
                    }
                ],
                "plist": {
                    "AppuploaderNet": "7e530551-5ad5-4545-b556-a5ae559c5804",
                    "BuildMachineOSBuild": "18G103",
                    "CFBundleDevelopmentRegion": "zh_CN",
                    "CFBundleDisplayName": "blabla",
                    "CFBundleExecutable": "blabla",
                    "CFBundleIcons": {
                        "CFBundlePrimaryIcon": {
                            "CFBundleIconFiles": [
                                "AppIcon20x20",
                                "AppIcon29x29",
                                "AppIcon40x40",
                                "AppIcon57x57",
                                "AppIcon60x60"
                            ],
                            "CFBundleIconName": "AppIcon"
                        }
                    },
                    "CFBundleIcons~ipad": {
                        "CFBundlePrimaryIcon": {
                            "CFBundleIconFiles": [
                                "AppIcon20x20",
                                "AppIcon29x29",
                                "AppIcon40x40",
                                "AppIcon57x57",
                                "AppIcon60x60",
                                "AppIcon50x50",
                                "AppIcon72x72",
                                "AppIcon76x76",
                                "AppIcon83.5x83.5"
                            ],
                            "CFBundleIconName": "AppIcon"
                        }
                    },
                    "CFBundleIdentifier": "mobile.blabla.af05.x10.ios001",
                    "CFBundleInfoDictionaryVersion": "6.0",
                    "CFBundleName": "blabla",
                    "CFBundlePackageType": "APPL",
                    "CFBundleShortVersionString": "1.7.0",
                    "CFBundleSignature": "????",
                    "CFBundleSupportedPlatforms": [
                        "iPhoneOS"
                    ],
                    "CFBundleURLTypes": [
                        {
                            "CFBundleTypeRole": "Editor",
                            "CFBundleURLName": "weixin",
                            "CFBundleURLSchemes": [
                                ""
                            ]
                        }
                    ],
                    "CFBundleVersion": "170",
                    "DTCompiler": "com.apple.compilers.llvm.clang.1_0",
                    "DTPlatformBuild": "17A566",
                    "DTPlatformName": "iphoneos",
                    "DTPlatformVersion": "13.0",
                    "DTSDKBuild": "17A566",
                    "DTSDKName": "iphoneos13.0",
                    "DTXcode": "1100",
                    "DTXcodeBuild": "11A420a",
                    "LSApplicationQueriesSchemes": [
                        "alipayqr",
                        "wechat",
                        "weixin",
                        "sinaweibohd",
                        "sinaweibo",
                        "sinaweibosso",
                        "weibosdk",
                        "weibosdk2.5",
                        "mqqapi"
                    ],
                    "LSRequiresIPhoneOS": true,
                    "Localizedresources can be mixed": true,
                    "MinimumOSVersion": "8.0",
                    "NSAppTransportSecurity": {
                        "NSAllowsArbitraryLoads": true,
                        "NSExceptionDomains": {
                            "blabla.cn": {
                                "NSExceptionAllowsInsecureHTTPLoads": true,
                                "NSIncludesSubdomains": true
                            }
                        }
                    },
                    "NSCameraUsageDescription": "blablabla",
                    "NSPhotoLibraryAddUsageDescription": "blablabla",
                    "NSPhotoLibraryUsageDescription": "blablabla",
                    "UIBackgroundModes": [
                        "remote-notification"
                    ],
                    "UIDeviceFamily": [
                        1,
                        2
                    ],
                    "UILaunchStoryboardName": "LaunchScreen",
                    "UIPrerenderedIcon": true,
                    "UIRequiredDeviceCapabilities": {
                        "accelerometer": true,
                        "opengles-1": true
                    },
                    "UIRequiresFullScreen": true,
                    "UIStatusBarHidden": false,
                    "UISupportedInterfaceOrientations": [
                        "UIInterfaceOrientationPortrait",
                        "UIInterfaceOrientationPortraitUpsideDown"
                    ],
                    "UIViewControllerBasedStatusBarAppearance": false
                },
                "provision": {
                    "AppIDName": "blablabla",
                    "ApplicationIdentifierPrefix": [
                        "KW555E65TD"
                    ],
                    "CreationDate": "2019-08-01 03:52:56",
                    "Entitlements": {
                        "application-identifier": "KW555E65TD.*",
                        "com.apple.developer.default-data-protection": "NSFileProtectionComplete",
                        "com.apple.developer.networking.networkextension": [
                            "app-proxy-provider",
                            "content-filter-provider",
                            "packet-tunnel-provider",
                            "dns-proxy"
                        ],
                        "com.apple.developer.pass-type-identifiers": [
                            "KW555E65TD.*"
                        ],
                        "com.apple.developer.team-identifier": "KW555E65TD",
                        "com.apple.developer.ubiquity-container-identifiers": [
                            "KW555E65TD.*"
                        ],
                        "com.apple.developer.ubiquity-kvstore-identifier": "KW555E65TD.*",
                        "get-task-allow": false,
                        "inter-app-audio": true,
                        "keychain-access-groups": [
                            "KW555E65TD.*"
                        ]
                    },
                    "ExpirationDate": "2020-07-31 03:52:56",
                    "IsXcodeManaged": false,
                    "Name": "20190801_ppp iOS Distribution",
                    "Platform": [
                        "iOS"
                    ],
                    "ProvisionsAllDevices": true,
                    "TeamIdentifier": [
                        "KW555E65TD"
                    ],
                    "TeamName": "Blabla Company",
                    "TimeToLive": 365,
                    "UUID": "295c66b6-6946-6c69-6648-68166a566364",
                    "Version": 1
                }
            }
        }
    }
}
```
```json Example (itunes field)
{
    "data": {
        "attributes": {
            "ipa_info": {
                "apps": [
                    {
                        "commands": [
                            {
                                "type": "LC_DYLD_INFO_ONLY"
                            },
                            {
                                "type": "LC_SYMTAB"
                            },
                            {
                                "type": "LC_DYSYMTAB"
                            }
                        ],
                        "headers": {
                            "cpu_subtype": "ARM_V7",
                            "cpu_type": "ARM",
                            "entrypoint": "0x41a1d",
                            "file_type": "executable file",
                            "flags": [
                                "BINDS_TO_WEAK",
                                "DYLDLINK",
                                "NOUNDEFS",
                                "PIE",
                                "TWOLEVEL",
                                "WEAK_DEFINES"
                            ],
                            "magic": "0xfeedface",
                            "num_cmds": 50,
                            "size_cmds": 5272
                        },
                        "libs": [
                            "/System/Library/Frameworks/AVFoundation.framework/AVFoundation",
                            "/System/Library/Frameworks/AdSupport.framework/AdSupport",
                            "/System/Library/Frameworks/AssetsLibrary.framework/AssetsLibrary",
                            "/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox",
                            "/System/Library/Frameworks/CFNetwork.framework/CFNetwork"
                        ],
                        "segments": [
                            {
                                "fileoff": "0x0",
                                "filesize": "0x0",
                                "name": "__PAGEZERO",
                                "sections": [],
                                "vmaddr": "0x0",
                                "vmsize": "0x4000"
                            },
                            {
                                "fileoff": "0x0",
                                "filesize": "0x650000",
                                "name": "__TEXT",
                                "sections": [
                                    {
                                        "flags": [
                                            "SECTION_ATTRIBUTES_USR",
                                            "SECTION_ATTRIBUTES_SYS"
                                        ],
                                        "name": "__text",
                                        "type": "S_REGULAR"
                                    },
                                    {
                                        "flags": [
                                            "SECTION_ATTRIBUTES_USR",
                                            "SECTION_ATTRIBUTES_SYS"
                                        ],
                                        "name": "__picsymbolstub4",
                                        "type": "S_SYMBOL_STUBS"
                                    }
                                ],
                                "vmaddr": "0x4000",
                                "vmsize": "0x650000"
                            }
                        ],
                        "signature": {
                            "Identifier": "com.blabla.music"
                        },
                        "tags": [
                            "signed",
                            "arm"
                        ],
                        "vhash": "4b5b5f85f1256d547a5cc5805c7565cb"
                    }
                ],
                "itunes": {
                    "acctHashId": "1e69753e257e546d5837562f57bb5b75655f6b51f5e75055",
                    "artistId": 1515515775,
                    "artistName": "Blabla bla bla",
                    "bundleVersion": "1015",
                    "copyright": " Blablabla Studio",
                    "drmVersionNumber": 0,
                    "fileExtension": ".app",
                    "genre": "",
                    "genreId": 6013,
                    "itemId": 5115559575,
                    "itemName": "Blabla Music Player",
                    "kind": "software",
                    "playlistArtistName": "",
                    "playlistName": "Blabla bla bla",
                    "product-type": "ios-app",
                    "purchaseDate": "2016-05-09 11:17:39",
                    "rating": {
                        "content": "Advisory.NO.GAMBLING_CONTESTS and Advisory.NO.UNRESTRICTED_WEB_ACCESS",
                        "label": "4+",
                        "rank": 100,
                        "system": "itunes-games"
                    },
                    "releaseDate": "2016-05-07T03:13:24Z",
                    "s": 143465,
                    "softwareIcon57x57URL": "http://a1825.phobos.apple.com/us/r30/Purple30/v4/d0/43/bb/5045bb50-d52a-5550-c459-b0af5e495e25/icon114x114.jpeg",
                    "softwareIconNeedsShine": false,
                    "softwareSupportedDeviceIds": [
                        2,
                        9,
                        4
                    ],
                    "softwareVersionBundleId": "com.blabla.music",
                    "softwareVersionExternalIdentifier": 817357515,
                    "softwareVersionExternalIdentifiers": [
                        817357515
                    ],
                    "vendorId": 115225175,
                    "versionRestrictions": 16545005
                }
            }
        }
    }
}
```

---

← [image_code_injections](file-object-image-code-injections.md) · [up](../README.md) · [jar_info](file-object-jar-info.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-ipa-info>.*
