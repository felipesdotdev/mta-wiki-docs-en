---
doc_id: "mta-wiki:13507"
title: "Modules/FileSystem/translator/rename"
source_title: "Modules/FileSystem/translator/rename"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/translator/rename"
revision_id: 73767
language: "en"
categories: []
---

# Modules/FileSystem/translator/rename

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

## [FileSystem](mta://reference/misc/modules-filesystem.md) Translator Functions

- [open](mta://reference/misc/modules-filesystem-translator-open.md)

- [exists](mta://reference/misc/modules-filesystem-translator-exists.md)

- [createDir](mta://reference/misc/modules-filesystem-translator-createdir.md)

- [chdir](mta://reference/misc/modules-filesystem-translator-chdir.md)

- [delete](mta://reference/misc/modules-filesystem-translator-delete.md)

- [copy](mta://reference/misc/modules-filesystem-translator-copy.md)

- rename

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

- [setPathProcessingMode](mta://reference/misc/modules-filesystem-translator-setpathprocessingmode.md)

- [getPathProcessingMode](mta://reference/misc/modules-filesystem-translator-getpathprocessingmode.md)
