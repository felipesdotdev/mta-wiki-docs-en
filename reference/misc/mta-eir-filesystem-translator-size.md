---
doc_id: "mta-wiki:7504"
title: "MTA:Eir/FileSystem/translator/size"
source_title: "MTA:Eir/FileSystem/translator/size"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/translator/size"
revision_id: 73540
language: "en"
categories: []
generated_at: "2026-07-26T16:16:06.293398+00:00"
---

# MTA:Eir/FileSystem/translator/size

This function queries the size of a filesystem object. The size of a filesystem object is the count of bytes that it logically fills on the storage media.

## Syntax

```
int translator:size ( string filePath )
```

## Arguments

- **filePath:** the path to the filesystem object that you want to get the size of

## Returns

This function returns the count of bytes that the filesystem object is logically taking on the storage medium, **false** if **filePath** is not a valid path in the translator or the filesystem object pointed at by it is not accessible.

## Example

Click to collapse [-]
Client

This snippet calculates the size of a resource and prints it to the debug console.

```
-- Get the handle to the resource instance directory.
local resRoot = fileCreateTranslator( "/" );

-- Calculate the size of every file in it.
local fileSizeCount = 0;

local function fileIteratorSum( filePath )
    fileSizeCount = fileSizeCount + resRoot:size( filePath );
end

-- Iterate through the entire directory tree, including the sub-directories.
resRoot:scanDirEx( "/", "*", nil, fileIteratorSum, true );

-- Output the size to the console.
outputDebugString( "resource size: " .. fileSizeCount );
```

## [FileSystem](mta://reference/misc/mta-eir-filesystem.md) Translator Functions

- [open](mta://reference/misc/mta-eir-filesystem-translator-open.md)

- [exists](mta://reference/misc/mta-eir-filesystem-translator-exists.md)

- [createDir](mta://reference/misc/mta-eir-filesystem-translator-createdir.md)

- [chdir](mta://reference/misc/mta-eir-filesystem-translator-chdir.md)

- [delete](mta://reference/misc/mta-eir-filesystem-translator-delete.md)

- [copy](mta://reference/misc/mta-eir-filesystem-translator-copy.md)

- [rename](mta://reference/misc/mta-eir-filesystem-translator-rename.md)

- size

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
