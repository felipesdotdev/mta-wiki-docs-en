---
doc_id: "mta-wiki:13519"
title: "Modules/FileSystem/translator/getOutbreakEnabled"
source_title: "Modules/FileSystem/translator/getOutbreakEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/translator/getOutbreakEnabled"
revision_id: 73779
language: "en"
categories: []
---

# Modules/FileSystem/translator/getOutbreakEnabled

This function gets the outbreak-policy of a file translator. If outbreak is enabled then file path requests outside of the translator root are allowed. Otherwise the user can only access files that are accessible from inside the translator root directory.

## Syntax

```
bool translator:setOutbreakEnabled ()
```

## Returns

This function returns true if the outbreak-policy is enabled for this translator, false otherwise.

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

- [setOutbreakEnabled](mta://reference/misc/modules-filesystem-translator-setoutbreakenabled.md)

- getOutbreakEnabled

- [setPathProcessingMode](mta://reference/misc/modules-filesystem-translator-setpathprocessingmode.md)

- [getPathProcessingMode](mta://reference/misc/modules-filesystem-translator-getpathprocessingmode.md)
