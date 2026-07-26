---
doc_id: "mta-wiki:7503"
title: "MTA:Eir/FileSystem/translator/rename"
source_title: "MTA:Eir/FileSystem/translator/rename"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/translator/rename"
revision_id: 73539
language: "en"
categories: []
generated_at: "2026-07-26T16:16:06.221602+00:00"
---

# MTA:Eir/FileSystem/translator/rename

This function moves a file from a source location to a destination location inside of a filesystem. This function is the fastest way to move data from one location to another.

## Syntax

```
bool translator:rename ( string srcPath, string dstPath )
```

## Arguments

- **srcPath:** a path to the source file

- **dstPath:** the path to the destination location where the source file should be moved to

## Returns

This function returns **true** if the file pointed at by **srcPath** could be successfully moved to the new **dstPath** location, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet moves a script file to another location.

```
-- Create a generic translator.
local resRoot = fileCreateTranslator( "/" );

-- Move this script file into a directory called "collection"
resRoot:rename( "thisScript.lua", "trash/thisScript.lua" );
```

## [FileSystem](mta://reference/misc/mta-eir-filesystem.md) Translator Functions

- [open](mta://reference/misc/mta-eir-filesystem-translator-open.md)

- [exists](mta://reference/misc/mta-eir-filesystem-translator-exists.md)

- [createDir](mta://reference/misc/mta-eir-filesystem-translator-createdir.md)

- [chdir](mta://reference/misc/mta-eir-filesystem-translator-chdir.md)

- [delete](mta://reference/misc/mta-eir-filesystem-translator-delete.md)

- [copy](mta://reference/misc/mta-eir-filesystem-translator-copy.md)

- rename

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
