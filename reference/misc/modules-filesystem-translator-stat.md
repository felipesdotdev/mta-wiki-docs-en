---
doc_id: "mta-wiki:13509"
title: "Modules/FileSystem/translator/stat"
source_title: "Modules/FileSystem/translator/stat"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/translator/stat"
revision_id: 73769
language: "en"
categories: []
generated_at: "2026-07-26T16:16:12.703861+00:00"
---

# Modules/FileSystem/translator/stat

This function queries common information about a filesystem object and returns it as a dictionary. Example of it's return value:

```
{
    accessTime = 1390997951, -- OS specific time information
    creationTime = 1381999749, -- OS specific time information
    modTime = 1381872826, -- OS specific time information
    size = 1441280, -- size of the filesystem object in bytes
};
```

## Syntax

```
dictionary translator:stat ( string filePath )
```

## Arguments

- **filePath:** the path to the filesystem object that you want to get the statistics of

## Returns

This function returns a statistics structure of the filesystem object pointed at by **filePath**, **false** if **filePath** is not a valid path in the translator or the filesystem object pointed at by it is not accessible.

## Example

Click to collapse [-]
Client

This snippet returns information about the currently running script. It can be used to know when the script has been updated by MTA.

```
-- Grab a generic translator of resource instance directory.
local resRoot = fileCreateTranslator( "/" );

-- Get the information of this script file.
local scriptStats = resRoot:stat( "thisScript.lua" );

-- todo: use this information somehow.
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

- stat

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
