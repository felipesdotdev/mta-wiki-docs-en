---
doc_id: "mta-wiki:14289"
title: "Modules/CMR Protected"
source_title: "Modules/CMR Protected"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/CMR_Protected"
revision_id: 79346
language: "en"
categories: []
---

# Modules/CMR Protected

| Module info |  |
| --- | --- |
| Name | CMR Protected |
| Version | 1.20 |
| Author | Camargo |
| Module website | CMR Protected |
| Download link | Linux Windows |
| License | Use license |
| Written in | C++ |
| Operating system | Cross-platform |
| Compatible with | 1.x |

The CMR Protected is an alternative module designed to obfuscate and encrypt your code, preventing luac decompilers from accessing your final code.

## Encrypt File

Encrypt server file on [https://secure.cmr.dev.br](https://secure.cmr.dev.br/)

## Installation

### Windows

**64 bit:**

- Extract the file on x64 servers: Typically located at *%PROGRAMFILES%\MTA San Andreas\server\x64\modules\*. If the folder doesn't exist, create it.

**86 bit(32 bit):**

- Extract the file on x86 servers: Typically located at *%PROGRAMFILES%\MTA San Andreas\server\mods\deathmatch\modules\*. If the folder doesn't exist, create it.

**Module configuration:**

- Then, add the following line in mtaserver.conf:

```
<module src="cmr_protected.dll" />
```

Now all you have to do is start your server.

### Linux

**86 bit (32 bit):**

- Extract the file on x86 servers: Typically located at *mods/deathmatch/modules/*. If the folder doesn't exist, create it.

**64 bit:**

- Extract the file on x64 servers: Typically located at *x64/modules/*. If the folder doesn't exist, create it.

**Module configuration:**

- Then, add the following line in mtaserver.conf:

```
<module src="cmr_protected.so" />
```

Now all you have to do is start your server.
