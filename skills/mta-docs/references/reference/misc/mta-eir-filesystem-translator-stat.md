---
doc_id: "mta-wiki:7505"
title: "MTA:Eir/FileSystem/translator/stat"
source_title: "MTA:Eir/FileSystem/translator/stat"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/translator/stat"
revision_id: 73541
language: "en"
categories: []
---

# MTA:Eir/FileSystem/translator/stat

This function queries common information about a filesystem object and returns it as a dictionary. Example of its return value:

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

## [FileSystem](mta://reference/misc/mta-eir-filesystem.md) Translator Functions

- [open](mta://reference/misc/mta-eir-filesystem-translator-open.md)

- [exists](mta://reference/misc/mta-eir-filesystem-translator-exists.md)

- [createDir](mta://reference/misc/mta-eir-filesystem-translator-createdir.md)

- [chdir](mta://reference/misc/mta-eir-filesystem-translator-chdir.md)

- [delete](mta://reference/misc/mta-eir-filesystem-translator-delete.md)

- [copy](mta://reference/misc/mta-eir-filesystem-translator-copy.md)

- [rename](mta://reference/misc/mta-eir-filesystem-translator-rename.md)

- [size](mta://reference/misc/mta-eir-filesystem-translator-size.md)

- stat

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
