---
doc_id: "mta-wiki:4239"
title: "Modules/hashing"
source_title: "Modules/hashing"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/hashing"
revision_id: 42931
language: "en"
categories: ["Outdated_Pages", "Modules"]
---

# Modules/hashing

|  | This article is (partially) outdated and the information may no longer apply. |
| --- | --- |
| Reason: MTA now supports generic hashing using the hash function |  |

| Module info |  |
| --- | --- |
| Name | Hashing string (alder32, md5) |
| Version | 1.1 |
| Author | 50p |
| Module website | Not available |
| Download link | Here |
| License | BSD |
| Written in | C++ |
| Operating system | Windows only |
| Compatible with | Unknown |

This is hashing string module. It uses 2 algorithms of hashing. One is alder32 (which is not actually the real alder32 algorithm, I do not recommend using it) and one is MD5. Using MD5 you get 32-characters long hexadecimal number.

CURRENTLY IT'S ONLY FOR WINDOWS SERVERS.

## Installation

### Windows

*** Important ***

This module was compiled in Visual C++ 2008, as such it requires Visual C++ 2008 or the Visual C++ 2008 runtime libraries which are considerably smaller. You can get this ~1.8MB Installation package [Here](http://www.microsoft.com/downloads/details.aspx?familyid=9B2DA534-3E03-4391-8A4D-074B9F2BC1BF&displaylang=en).

Uncompress the file hashing.dll into your *C:\Program Files\MTA San Andreas\server\mods\deathmatch\modules\* directory.

Then, add the following line in mtaserver.conf:

```
<module file="hashing.dll" />
```

## Functions

- [alder32](mta://reference/misc/modules-hashing-alder32.md)

- [md5](mta://reference/misc/modules-hashing-md5.md)
