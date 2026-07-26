---
doc_id: "mta-wiki:13482"
title: "MTA:Eir/FileSystem/translator/getOutbreakEnabled"
source_title: "MTA:Eir/FileSystem/translator/getOutbreakEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/translator/getOutbreakEnabled"
revision_id: 73551
language: "en"
categories: []
generated_at: "2026-07-26T16:16:06.148099+00:00"
---

# MTA:Eir/FileSystem/translator/getOutbreakEnabled

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

- getOutbreakEnabled

- [setPathProcessingMode](mta://reference/misc/mta-eir-filesystem-translator-setpathprocessingmode.md)

- [getPathProcessingMode](mta://reference/misc/mta-eir-filesystem-translator-getpathprocessingmode.md)
