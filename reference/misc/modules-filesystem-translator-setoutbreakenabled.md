---
doc_id: "mta-wiki:13518"
title: "Modules/FileSystem/translator/setOutbreakEnabled"
source_title: "Modules/FileSystem/translator/setOutbreakEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/translator/setOutbreakEnabled"
revision_id: 73778
language: "en"
categories: []
generated_at: "2026-07-26T16:16:12.657795+00:00"
---

# Modules/FileSystem/translator/setOutbreakEnabled

This function sets the outbreak-policy of a file translator. If outbreak is enabled then file path requests outside of the translator root are allowed. Otherwise the user can only access files that are accessible from inside the translator root directory.

## Syntax

```
void translator:setOutbreakEnabled ( bool enabled )
```

## Arguments

- **enabled:** value for the translator outbreak-policy

## Returns

This function returns nil.

## Example

```
-- TODO
```

## [FileSystem](mta://reference/misc/modules-filesystem.md) Translator Functions

- [open](mta://reference/misc/modules-filesystem-translator-open.md)

- [exists](mta://reference/misc/modules-filesystem-translator-exists.md)

- [createDir](mta://reference/misc/modules-filesystem-translator-createdir.md)

- [chdir](mta://reference/misc/modules-filesystem-translator-chdir.md)

- [delete](mta://reference/misc/modules-filesystem-translator-delete.md)

- [copy](mta://reference/misc/modules-filesystem-translator-copy.md)

- [rename](mta://reference/misc/modules-filesystem-translator-rename.md)

- [size](mta://reference/misc/modules-filesystem-translator-size.md)

- [stat](mta://reference/misc/modules-filesystem-translator-stat.md)

- [relPath](mta://reference/misc/modules-filesystem-translator-relpath.md)

- [relPathRoot](mta://reference/misc/modules-filesystem-translator-relpathroot.md)

- [absPath](mta://reference/misc/modules-filesystem-translator-abspath.md)

- [absPathRoot](mta://reference/misc/modules-filesystem-translator-abspathroot.md)

- [scanDir](mta://reference/misc/modules-filesystem-translator-scandir.md)

- [scanDirEx](mta://reference/misc/modules-filesystem-translator-scandirex.md)

- [getDirs](mta://reference/misc/modules-filesystem-translator-getdirs.md)

- [getFiles](mta://reference/misc/modules-filesystem-translator-getfiles.md)

- setOutbreakEnabled

- [getOutbreakEnabled](mta://reference/misc/modules-filesystem-translator-getoutbreakenabled.md)

- [setPathProcessingMode](mta://reference/misc/modules-filesystem-translator-setpathprocessingmode.md)

- [getPathProcessingMode](mta://reference/misc/modules-filesystem-translator-getpathprocessingmode.md)
