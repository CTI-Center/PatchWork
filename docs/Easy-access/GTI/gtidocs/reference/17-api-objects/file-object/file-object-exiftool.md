---
title: "exiftool"
source: https://gtidocs.virustotal.com/reference/file-object-exiftool
slug: file-object-exiftool
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:40:55.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › exiftool

---

# exiftool

information about EXIF metadata from files.

`exiftool` is a program for extracting Exif metadata from different file formats. Metadata shown may vary depending on the file type, and given the nature of Exif metadata, some fields may appear or not. This information is only available for Premium API users

* example: fields from Microsoft Windows PE files.

```
CharacterSet, CodeSize, CompanyName, EntryPoint, FileDescription, FileFlagsMask,
FileOS, FileSize, FileSubtype, FileType, FileTypeExtension, FileVersion,
FileVersionNumber, ImageVersion, InitializedDataSize, InternalName, LanguageCode,
LegalCopyright, LinkerVersion, MIMEType, MachineType, OSVersion, ObjectFileType,
OriginalFileName, PEType, ProductName, ProductVersion, ProductVersionNumber,
Subsystem, SubsystemVersion, TimeStamp, UninitializedDataSize
```

* example: fields from JPEG files.

```
Aperture, ApertureValue, BitsPerSample, BrightnessValue, CircleOfConfusion,
ColorComponents, ColorSpace, Compression, CreateDate, DateTimeOriginal,
DeviceType, EncodingProcess, ExifByteOrder, ExifImageHeight, ExifImageWidth,
ExifVersion, ExposureCompensation, ExposureMode, ExposureProgram, ExposureTime,
FNumber, FOV, FaceDetect, FileType, FileTypeExtension, Flash, FlashpixVersion,
FocalLength, FocalLength35efl, FocalLengthIn35mmFormat, HyperfocalDistance,
ISO, ImageHeight, ImageSize, ImageUniqueID, ImageWidth, InteropIndex,
InteropVersion, LightValue, MIMEType, Make, MakerNoteVersion, MaxApertureValue,
Megapixels, MeteringMode, Model, ModifyDate, Orientation, RawDataByteOrder,
RawDataCFAPattern, ResolutionUnit, ScaleFactor35efl, SceneCaptureType,
ShutterSpeed, ShutterSpeedValue, Software, SubSecCreateDate,
SubSecDateTimeOriginal, SubSecModifyDate, SubSecTime, SubSecTimeDigitized,
SubSecTimeOriginal, ThumbnailImage, ThumbnailLength, ThumbnailOffset,
TimeStamp, WhiteBalance, XResolution, YCbCrPositioning, YCbCrSubSampling,
YResolution
```

* example: fields from PDF files.

```
CreateDate, Creator, CreatorTool, DocumentID, FileType, FileTypeExtension,
Linearized, MIMEType, ModifyDate, PDFVersion, PageCount, Producer, XMPToolkit
```

```json Exiftool data
{
  "data": {
		...
    "attributes" : {
      ...
      "exiftool": {
         "<string>": "<string>", ... 
      }
    }
  }
}
```
```json Example (PE)
{
    "data": {
        "attributes": {
            "exiftool": {
                "CodeSize": "86528",
                "EntryPoint": "0x5d45",
                "FileFlagsMask": "0x003f",
                "FileOS": "Windows NT 32-bit",
                "FileSubtype": "0",
                "FileType": "Win32 EXE",
                "FileTypeExtension": "exe",
                "FileVersionNumber": "1.0.0.1",
                "ImageFileCharacteristics": "Executable, 32-bit",
                "ImageVersion": "0.0",
                "InitializedDataSize": "15447552",
                "LinkerVersion": "10.0",
                "MIMEType": "application/octet-stream",
                "MachineType": "Intel 386 or later, and compatibles",
                "OSVersion": "5.1",
                "ObjectFileType": "Executable application",
                "PEType": "PE32",
                "ProductVersionNumber": "1.0.0.1",
                "Subsystem": "Windows GUI",
                "SubsystemVersion": "5.1",
                "TimeStamp": "2018:06:10 05:04:21+02:00",
                "UninitializedDataSize": "0"
            }
        }
    }
}
```
```json Example (JPEG)
{
    "data": {
        "attributes": {
            "exiftool": {
                "Aperture": "1.8",
                "ApertureValue": "1.8",
                "ApplicationRecordVersion": "4",
                "BitsPerSample": "8",
                "BlueMatrixColumn": "0.14305 0.06061 0.71391",
                "BlueTRC": "(Binary data 32 bytes, use -b option to extract)",
                "CMMFlags": "Not Embedded, Independent",
                "ChromaticAdaptation": "1.04788 0.02292 -0.05022 0.02959 0.99048 -0.01707 -0.00925 0.01508 0.75168",
                "ChromaticityChannel1": "0.64 0.33",
                "ChromaticityChannel2": "0.3 0.60001",
                "ChromaticityChannel3": "0.14999 0.06",
                "ChromaticityChannels": "3",
                "ChromaticityColorant": "Unknown (0)",
                "CircleOfConfusion": "0.030 mm",
                "CodedCharacterSet": "UTF8",
                "ColorComponents": 3,
                "ColorMode": "RGB",
                "ColorSpace": "sRGB",
                "ColorSpaceData": "RGB ",
                "ColorTemperature": "8200",
                "ComponentsConfiguration": "Y, Cb, Cr, -",
                "ConnectionSpaceIlluminant": "0.9642 1 0.82491",
                "Contrast": "Normal",
                "CreateDate": "2019:07:29 17:27:35",
                "CurrentIPTCDigest": "8ee474b61a0cebeed7a05bee64e7b4dc",
                "DateTimeOriginal": "2019:07:29 17:27:35",
                "DeviceAttributes": "Reflective, Glossy, Positive, Color",
                "EncodingProcess": "Baseline DCT, Huffman coding",
                "ExifByteOrder": "Big-endian (Motorola, MM)",
                "ExifImageHeight": "3670",
                "ExifImageWidth": "5496",
                "ExifVersion": "0230",
                "ExposureCompensation": "0",
                "ExposureMode": "Manual",
                "ExposureProgram": "Manual",
                "ExposureTime": "1/125",
                "FNumber": "1.8",
                "FOV": "24.2 deg",
                "FileType": "JPEG",
                "FileTypeExtension": "jpg",
                "Flash": "Off, Did not fire",
                "FocalLength": "85.0 mm",
                "FocalLength35efl": "85.0 mm (35 mm equivalent: 83.9 mm)",
                "FocalPlaneResolutionUnit": "inches",
                "FocalPlaneXResolution": "3810.584958",
                "FocalPlaneYResolution": "3815.899582",
                "GPSVersionID": "2.3.0.0",
                "GreenMatrixColumn": "0.38512 0.7169 0.09706",
                "GreenTRC": "(Binary data 32 bytes, use -b option to extract)",
                "HyperfocalDistance": "131.91 m",
                "ICCProfileName": "sRGB IEC61966-2.1",
                "IPTCDigest": "8ee474b61a0cebeed7a05bee64e7b4dc",
                "ISO": "200",
                "ImageHeight": 3670,
                "ImageSize": "5496x3670",
                "ImageWidth": 5496,
                "JFIFVersion": "1.01",
                "Lens": "85.0 mm",
                "LensModel": "EF85mm f/1.8 USM",
                "LensSerialNumber": "000003ec67",
                "LightValue": "7.7",
                "MIMEType": "image/jpeg",
                "Make": "Canon",
                "MediaWhitePoint": "0.9642 1 0.82491",
                "Megapixels": 20.2,
                "MetadataDate": "2019:10:15 00:00:01+02:00",
                "MeteringMode": "Spot",
                "Model": "Canon EOS 6D",
                "ModifyDate": "2019:10:15 00:00:01+02:00",
                "Orientation": "Horizontal (normal)",
                "PrimaryPlatform": "Microsoft Corporation",
                "ProfileCMMType": "Little CMS",
                "ProfileClass": "Display Device Profile",
                "ProfileConnectionSpace": "XYZ ",
                "ProfileCopyright": "No copyright, use freely",
                "ProfileCreator": "Little CMS",
                "ProfileDateTime": "2019:10:14 21:14:53",
                "ProfileDescription": "sRGB IEC61966-2.1",
                "ProfileFileSignature": "acsp",
                "ProfileID": "0",
                "ProfileVersion": "4.3.0",
                "Rating": "0",
                "RecommendedExposureIndex": "200",
                "RedMatrixColumn": "0.43604 0.22249 0.01392",
                "RedTRC": "(Binary data 32 bytes, use -b option to extract)",
                "RenderingIntent": "Perceptual",
                "ResolutionUnit": "inches",
                "Saturation": "Normal",
                "ScaleFactor35efl": "1.0",
                "SceneCaptureType": "Standard",
                "SensitivityType": "Recommended Exposure Index",
                "SerialNumber": "305051000710",
                "Sharpness": "Hard",
                "ShutterSpeed": "1/125",
                "ShutterSpeedValue": "1/128",
                "ToneCurve": "Standard",
                "WhiteBalance": "Auto",
                "XMPToolkit": "XMP Core 5.5.0",
                "XResolution": 72,
                "YCbCrSubSampling": "YCbCr4:4:4 (1 1)",
                "YResolution": 72
            }
        }
    }
}
```
```json Example (PDF)
{
    "data": {
        "attributes": {
            "exiftool": {
                "CreateDate": "2020:02:27 18:03:45+03:00",
                "DocumentID": "uuid:5ac8d66b-6716-466c-b665-965766c06571",
                "FileType": "PDF",
                "FileTypeExtension": "pdf",
                "Format": "application/pdf",
                "HasXFA": "No",
                "InstanceID": "uuid:696b3606-6627-606f-b636-769b656676f0",
                "Linearized": "No",
                "MIMEType": "application/pdf",
                "MetadataDate": "2020:02:27 18:03:45+03:00",
                "ModifyDate": "2020:02:27 18:03:45+03:00",
                "PDFVersion": "1.6",
                "PageCount": "2",
                "XMPToolkit": "Adobe XMP Core 5.4-c005 78.147326, 2012/08/23-13:03:03        "
            }
        }
    }
}
```

---

← [Files](../file-object.md) · [up](../README.md) · [ssdeep](file-object-ssdeep.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-exiftool>.*
