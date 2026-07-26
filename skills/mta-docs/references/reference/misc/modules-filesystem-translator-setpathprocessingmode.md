---
doc_id: "mta-wiki:13520"
title: "Modules/FileSystem/translator/setPathProcessingMode"
source_title: "Modules/FileSystem/translator/setPathProcessingMode"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/translator/setPathProcessingMode"
revision_id: 73780
language: "en"
categories: []
---

# Modules/FileSystem/translator/setPathProcessingMode

This function sets the path-processing-mode for the file translator. The path-processing-mode describes how paths are handled in detail during file-path consuming function calls.

## Syntax

```
void translator:setPathProcessingMode( string mode )
```

## Arguments

- **mode:** value for the translator path-processing-mode (either **distinguished** or **ambivalent_file**)

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

- [setOutbreakEnabled](mta://reference/misc/modules-filesystem-translator-setoutbreakenabled.md)

- [getOutbreakEnabled](mta://reference/misc/modules-filesystem-translator-getoutbreakenabled.md)

- setPathProcessingMode

- [getPathProcessingMode](mta://reference/misc/modules-filesystem-translator-getpathprocessingmode.md)
