---
doc_id: "mta-wiki:13483"
title: "MTA:Eir/FileSystem/translator/setPathProcessingMode"
source_title: "MTA:Eir/FileSystem/translator/setPathProcessingMode"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/translator/setPathProcessingMode"
revision_id: 73552
language: "en"
categories: []
generated_at: "2026-07-26T16:16:06.280839+00:00"
---

# MTA:Eir/FileSystem/translator/setPathProcessingMode

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

## [FileSystem](mta://reference/misc/mta-eir-filesystem.md) Translator Functions

- [open](mta://reference/misc/mta-eir-filesystem-translator-open.md)

- [exists](mta://reference/misc/mta-eir-filesystem-translator-exists.md)

- [createDir](mta://reference/misc/mta-eir-filesystem-translator-createdir.md)

- [chdir](mta://reference/misc/mta-eir-filesystem-translator-chdir.md)

- [delete](mta://reference/misc/mta-eir-filesystem-translator-delete.md)

- [copy](mta://reference/misc/mta-eir-filesystem-translator-copy.md)

- [rename](mta://reference/misc/mta-eir-filesystem-translator-rename.md)

- [size](mta://reference/misc/mta-eir-filesystem-translator-size.md)

- [stat](mta://reference/misc/mta-eir-filesystem-translator-stat.md)

- [relPath](mta://reference/misc/mta-eir-filesystem-translator-relpath.md)

- [relPathRoot](mta://reference/misc/mta-eir-filesystem-translator-relpathroot.md)

- [absPath](mta://reference/misc/mta-eir-filesystem-translator-abspath.md)

- [absPathRoot](mta://reference/misc/mta-eir-filesystem-translator-abspathroot.md)

- [scanDir](mta://reference/misc/mta-eir-filesystem-translator-scandir.md)

- [scanDirEx](mta://reference/misc/mta-eir-filesystem-translator-scandirex.md)

- [getDirs](mta://reference/misc/mta-eir-filesystem-translator-getdirs.md)

- [getFiles](mta://reference/misc/mta-eir-filesystem-translator-getfiles.md)

- [setOutbreakEnabled](mta://reference/misc/mta-eir-filesystem-translator-setoutbreakenabled.md)

- [getOutbreakEnabled](mta://reference/misc/mta-eir-filesystem-translator-getoutbreakenabled.md)

- setPathProcessingMode

- [getPathProcessingMode](mta://reference/misc/mta-eir-filesystem-translator-getpathprocessingmode.md)
