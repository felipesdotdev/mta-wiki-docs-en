---
doc_id: "mta-wiki:7502"
title: "MTA:Eir/FileSystem/translator/copy"
source_title: "MTA:Eir/FileSystem/translator/copy"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/translator/copy"
revision_id: 73592
language: "en"
categories: []
generated_at: "2026-07-26T16:16:06.057446+00:00"
---

# MTA:Eir/FileSystem/translator/copy

This function copies a file from a source location to a file at the destination. The contents of the source file are copied, so that source and destination have the same content. Since the transactions happen through kernel-calls, this function is faster than performing the copying yourself through Lua strings.

## Syntax

```
bool translator:copy ( string srcPath, string dstPath )
```

## Arguments

- **srcPath:** a path to the source file

- **dstPath:** the path to the new file that should be copied into

## Returns

This function returns **true** if the file pointed at by **srcPath** is an accessible file that can be read from and the requested file a **dstPath** could be created and written to, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet backups a copy of client-side configuration for safety purposes.

```
-- Create a generic translator.
local resRoot = fileCreateTranslator( "/" );

resRoot:copy( "config.xml", "backup/config.xml" );
```

## [FileSystem](mta://reference/misc/mta-eir-filesystem.md) Translator Functions

- [open](mta://reference/misc/mta-eir-filesystem-translator-open.md)

- [exists](mta://reference/misc/mta-eir-filesystem-translator-exists.md)

- [createDir](mta://reference/misc/mta-eir-filesystem-translator-createdir.md)

- [chdir](mta://reference/misc/mta-eir-filesystem-translator-chdir.md)

- [delete](mta://reference/misc/mta-eir-filesystem-translator-delete.md)

- copy

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

- [setPathProcessingMode](mta://reference/misc/mta-eir-filesystem-translator-setpathprocessingmode.md)

- [getPathProcessingMode](mta://reference/misc/mta-eir-filesystem-translator-getpathprocessingmode.md)
